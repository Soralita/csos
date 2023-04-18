import qrcode
from alipay import AliPay
import time

# 密钥工具生成的私钥，和支付宝公钥（我保存在了文件中）
app_private_key_string = open("app_private_key.pem").read()
alipay_public_key_string = open("alipayPublicKey_RSA2.txt").read()

print(alipay_public_key_string)
'''
这里打印应该是这种格式（如果支付宝密钥生成工具生成的密钥没有头尾要自己加上）
私钥格式：
-----BEGIN RSA ** KEY-----
    base64 encoded content
-----END RSA PRIVATE KEY-----

公钥格式：
-----BEGIN PUBLIC KEY-----
    base64 encoded content
-----END PUBLIC KEY-----
'''

alipay = AliPay(
    appid="2021003189630875",   # 应用列表中“应用2.0签约******”的appid
    app_notify_url=None,    # 默认回调url
    app_private_key_string=app_private_key_string,  # 应用私钥
    alipay_public_key_string=alipay_public_key_string,  # 支付宝公钥
    sign_type="RSA2", # RSA 或者 RSA2(具体要看你的密钥是什么类型)
    debug=False  # 默认False
)
print(alipay)

auth_code="284084344951080085"
out_trade_no = "out_trade_no_07"
# 创建订单
result = alipay.api_alipay_trade_pay(
    out_trade_no=out_trade_no,
    scene="bar_code",
    auth_code=auth_code,
    subject="subject_title",
    total_amount=0.01,
)

if result["code"] == "10000":
    print("Order is paid")
print(result)

# 这里应该打印出{'code': '10000', 'msg': 'Success', 'out_trade_no': 'out_trade_no_123', 'qr_code': 'https://qr.alipay.com/bax05832mvaotxhcpjeh6074'}
# 其中用qr_code生成二维码，支付宝扫描即可付款
# 用qr_code生成二维码





# check order status
paid = False
for i in range(30):
    # check every 3s, and 10 times in all
    print("now sleep 3s")
    time.sleep(3)
    result = alipay.api_alipay_trade_query(out_trade_no=out_trade_no)
    if result.get("trade_status", "") == "TRADE_SUCCESS":
        paid = True
        break
    print("not paid...")

# order is not paid in 30s , cancel this order
if paid is False:
    print("支付失败，取消订单")
    alipay.api_alipay_trade_cancel(out_trade_no=out_trade_no)
else:
    print("支付成功")

