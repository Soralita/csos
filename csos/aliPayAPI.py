import requests
import json
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme as pkcs1_15
import base64
import time

# 支付宝API URL
url = 'https://openapi.alipay.com/gateway.do'

# 应用ID、商户号和私钥
app_id = 'YOUR_APP_ID'
mch_id = 'YOUR_MCH_ID'
private_key = 'YOUR_PRIVATE_KEY'

# 订单信息
order_info = {
    'out_trade_no': 'YOUR_OUT_TRADE_NO',
    'total_amount': '1.00',
    'subject': 'YOUR_SUBJECT',
    'product_code': 'QUICK_MSECURITY_PAY'
}

# 快速排序
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 生成签名
def generate_sign(data, private_key):
    # 将字典按照键名升序排序
    keys = sorted(data.keys())
    # 拼接键值对字符串
    key_value_str = '&'.join(['{}={}'.format(key, data[key]) for key in keys])
    # 对字符串进行SHA256哈希
    h = SHA256.new(key_value_str.encode('utf-8'))
    # 使用私钥进行RSA签名
    private_key_obj = RSA.import_key(private_key)
    signer = pkcs1_15.new(private_key_obj)
    sign = signer.sign(h)
    # 将签名进行Base64编码
    sign = base64.b64encode(sign).decode('utf-8')
    return sign

# 构造API请求参数
data = {
    'app_id': app_id,
    'method': 'alipay.trade.app.pay',
    'format': 'JSON',
    'charset': 'utf-8',
    'sign_type': 'RSA2',
    'timestamp': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
    'version': '1.0',
    'biz_content': json.dumps(order_info)
}

# 生成签名并添加到请求参数中
sign = generate_sign(data, private_key)
data['sign'] = sign

# 发送API请求
response = requests.post(url, data=data)

# 处理API返回结果
result = response.json()
if result['code'] == '10000':
    # 订单生成成功
    order_string = result['alipay_trade_app_pay_response']['body']
    print('订单生成成功，支付宝支付链接为：{}'.format(order_string))
else:
    # 订单生成失败
    print('订单生成失败，错误码为：{}，错误信息为：{}'.format(result['code'], result['msg']))
