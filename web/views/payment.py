import os
import subprocess
import sys

BASE_DIR=r"C:\Users\Soral\PycharmProjects\csos"
APP_ID="2021003189630875"
PRIVATE_KEY_FILE=os.path.join(BASE_DIR,"csos","utils","app_private_key.pem")
PUBLIC_KEY_FILE=os.path.join(BASE_DIR,"csos","utils","alipayPublicKey_RSA2.txt")
QRCODE_FILE=os.path.join(BASE_DIR,'static','qrcode.png')

print(PRIVATE_KEY_FILE)
# 密钥工具生成的私钥，和支付宝公钥（我保存在了文件中）
app_private_key_string = open(PRIVATE_KEY_FILE).read()
alipay_public_key_string = open(PUBLIC_KEY_FILE).read()

print(alipay_public_key_string)


import qrcode
from alipay import AliPay, DCAliPay, ISVAliPay
from alipay.utils import AliPayConfig
import time
from myadmin.models import Payment

alipay = AliPay(
    appid="2021003189630875",
    app_notify_url=None,  # 默认回调 url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=False,  # 默认 False
    verbose=True,  # 输出调试数据
    config=AliPayConfig(timeout=15)  # 可选，请求超时时间
)


# app_private_key_string = open("yourPrivateKey.key").read()
# app_public_key_cert_string = open("yourPrivateCert.crt").read()
# alipay_public_key_cert_string = open("alipayPublicCert.crt").read()
# alipay_root_cert_string = open("alipayRootCert.crt").read()
# dc_alipay = DCAliPay(
#     appid="appid",
#     app_notify_url="http://example.com/app_notify_url",
#     app_private_key_string=app_private_key_string,
#     app_public_key_cert_string=app_public_key_cert_string,
#     alipay_public_key_cert_string=alipay_public_key_cert_string,
#     alipay_root_cert_string=alipay_root_cert_string
# )

def pay_qrcode(op):

    out_trade_no = "payment_id_"+str(op.order_id)
    print(out_trade_no)
    total_amount=0.01
    # TODO 支付宝商品名修改
    subject_title="支付宝接口测试调用"
    result=None
    try:
        # 创建订单
        result = alipay.api_alipay_trade_precreate(
            subject=subject_title,  # 订单标题
            out_trade_no=out_trade_no,  # 订单号（不可重复）
            total_amount=0.01  # 订单金额，单位元
        )
    except Exception as err:
        print(err)


    print(result)
    qr = qrcode.QRCode(version=5,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4,
                       )
    qr.add_data(result['qr_code'])
    qr.make(fit=True)
    img = qr.make_image()
    img.save(QRCODE_FILE)

def pay_trade(op):
    KEYBOARDLISTEN_FILE=os.path.join(BASE_DIR,"csos","utils","keyboardListen.py")
    p=subprocess.Popen([sys.executable, KEYBOARDLISTEN_FILE], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    auth_code=p.stdout.read().decode("utf-8")
    print(auth_code,type(auth_code))

    #获取 op 传入的Payment数据
    out_trade_no = "payment_id_" + str(op.order_id)
    print(out_trade_no)
    total_amount = 0.01
    # TODO 支付宝商品名修改
    subject_title = "支付宝接口测试调用"


    result = alipay.api_alipay_trade_pay(
        out_trade_no=out_trade_no,
        scene="bar_code",
        auth_code=auth_code,
        subject=subject_title,
        total_amount=0.01,
    )

    if result["code"] == "10000":
        print("Order is paid")
    print(result)

def check_order_status(out_trade_no):
    # check order status
    """返回TRUE 该订单支付成功,30秒计时"""
    paid = False
    for i in range(10):
        # check every 3s, and 10 times in all
        print("now sleep 3s")
        time.sleep(3)
        result = alipay.api_alipay_trade_query(out_trade_no="out_trade_no")
        if result.get("trade_status", "") == "TRADE_SUCCESS":
            paid = True

            break
        print("not paid...")

    # order is not paid in 30s , cancel this order
    if paid is False:
        alipay.api_alipay_trade_cancel(out_trade_no=out_trade_no)

    return paid