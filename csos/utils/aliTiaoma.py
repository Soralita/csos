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
out_trade_no="test_tiaoma_1"
subject="testPycharm"
auth_code="285236045889172434"
result = alipay.api_alipay_trade_pay(
    out_trade_no=out_trade_no,
    scene="bar_code",
    auth_code=auth_code,
    subject=subject,
    discountable_amount=10,
    total_amount=0.01,
    notify_url="https://example.com/notify" # 可选，不填则使用默认notify url
)

if  result["code"] == "10000":
    print("Order is paid")
else:
    print(result)