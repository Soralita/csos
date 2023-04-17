import keyboard
import requests

# 微信付款码API
def wechat_pay(auth_code):
    url = 'https://api.mch.weixin.qq.com/pay/micropay'
    params = {
        'appid': 'YOUR_APP_ID',
        'mch_id': 'YOUR_MCH_ID',
        'nonce_str': 'YOUR_NONCE_STR',
        'auth_code': auth_code,
        'body': '支付测试',
        'out_trade_no': 'YOUR_OUT_TRADE_NO',
        'total_fee': '1',
        'spbill_create_ip': 'YOUR_IP_ADDRESS',
        'notify_url': 'YOUR_NOTIFY_URL',
        'trade_type': 'MICROPAY',
    }
    response = requests.post(url, data=params)
    print(response.text)

# 支付宝付款码API
def alipay_pay(auth_code):
    url = 'https://openapi.alipay.com/gateway.do'
    params = {
        'app_id': 'YOUR_APP_ID',
        'method': 'alipay.trade.pay',
        'format': 'JSON',
        'charset': 'utf-8',
        'sign_type': 'RSA2',
        'timestamp': 'YOUR_TIMESTAMP',
        'version': '1.0',
        'notify_url': 'YOUR_NOTIFY_URL',
        'biz_content': {
            'out_trade_no': 'YOUR_OUT_TRADE_NO',
            'scene': 'bar_code',
            'auth_code': auth_code,
            'subject': '测试支付宝付款码',
            'total_amount': '0.01',
        },
    }
    response = requests.post(url, json=params)
    print(response.text)

# 处理付款码
def process_auth_code(auth_code):
    if auth_code.isdigit():
        # 判断是否为微信付款码
        if auth_code.startswith(('10', '11', '12', '13', '14', '15')):
            # 处理微信付款码
            wechat_pay(auth_code)
        # 判断是否为支付宝付款码
        elif auth_code.startswith(('25', '26', '27', '28', '29', '30')):
            # 处理支付宝付款码
            alipay_pay(auth_code)
        else:
            print('未知付款码类型：', auth_code)
    else:
        print('未知付款码类型：', auth_code)

# 监听键盘事件
def on_key_press(event):
    if event.event_type == 'down':
        key = ''
        # 处理付款码
        while (event.name != 'enter'):
            if event.name != 'enter':
                key = key + event.name
            elif event.name == 'enter':
                break
        process_auth_code(key)

# 主函数
def main():
    # # 监听键盘事件
    # keyboard.on_press(on_key_press)
    #
    # # 进入消息循环
    # keyboard.wait()
    while True:
        process_auth_code(input())

if __name__ == '__main__':
    main()
