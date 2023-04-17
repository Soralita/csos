import requests
import json
import hashlib
import time
import xmltodict

# 微信支付API URL
url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'

# 商户号和API密钥
mch_id = 'YOUR_MCH_ID'
api_key = 'YOUR_API_KEY'

# 订单信息
order_info = {
    'appid': 'YOUR_APP_ID',
    'mch_id': mch_id,
    'nonce_str': str(int(time.time())),
    'body': 'YOUR_ORDER_BODY',
    'out_trade_no': 'YOUR_OUT_TRADE_NO',
    'total_fee': 1,  # 单位为分
    'spbill_create_ip': 'YOUR_CLIENT_IP',
    'notify_url': 'YOUR_NOTIFY_URL',
    'trade_type': 'APP'
}

# 生成签名
def generate_sign(data, api_key):
    # 将字典按照键名升序排序
    keys = sorted(data.keys())
    # 拼接键值对字符串
    key_value_str = '&'.join(['{}={}'.format(key, data[key]) for key in keys])
    # 在字符串末尾拼接API密钥
    key_value_str += '&key=' + api_key
    # 计算MD5哈希值并转化为大写
    sign = hashlib.md5(key_value_str.encode('utf-8')).hexdigest().upper()
    return sign

# 构造API请求参数
data = {
    'appid': order_info['appid'],
    'mch_id': order_info['mch_id'],
    'nonce_str': order_info['nonce_str'],
    'body': order_info['body'],
    'out_trade_no': order_info['out_trade_no'],
    'total_fee': order_info['total_fee'],
    'spbill_create_ip': order_info['spbill_create_ip'],
    'notify_url': order_info['notify_url'],
    'trade_type': order_info['trade_type']
}

# 生成签名并添加到请求参数中
sign = generate_sign(data, api_key)
data['sign'] = sign

# 将请求参数转化为XML格式
xml_data = '<xml>\n{}\n</xml>'.format('\n'.join(['<{0}>{1}</{0}>'.format(key, value) for key, value in data.items()]))

# 发送API请求
response = requests.post(url, data=xml_data.encode('utf-8'), headers={'Content-Type': 'application/xml'})

# 处理API返回结果
result = json.loads(json.dumps(xmltodict.parse(response.content)))['xml']
if result['return_code'] == 'SUCCESS':
    # 订单生成成功
    prepay_id = result['prepay_id']
    print('订单生成成功，预支付ID为：{}'.format(prepay_id))
else:
    # 订单生成失败
    print('订单生成失败，错误码为：{}，错误信息为：{}'.format(result['return_code'], result['return_msg']))
