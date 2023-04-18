import base64
from pyasn1.codec.der import decoder
from pyasn1_modules import rfc5208

# 读取文本文件中的私钥内容
with open('应用私钥RSA2048.txt', 'r') as f:
    key_data = f.read()

# 提取私钥内容
start_index = key_data.index('-----BEGIN PRIVATE KEY-----') + len('-----BEGIN PRIVATE KEY-----')
end_index = key_data.index('-----END PRIVATE KEY-----')
key_data = key_data[start_index:end_index]

# 解码为 DER 编码的二进制私钥数据
key_bytes = base64.b64decode(key_data)


# 解析 DER 编码的二进制私钥数据为 ASN.1 结构体对象
key_obj, _ = decoder.decode(key_bytes, asn1Spec=rfc5208.PrivateKeyInfo())

# 转换为标准的 RSA 私钥格式的字符串
key_str = key_obj["privateKeyAlgorithm"]["parameters"].asOctets().hex()
key_str = "-----BEGIN PRIVATE KEY-----\n" + "\n".join([key_str[i:i+64] for i in range(0, len(key_str), 64)]) + "\n-----END PRIVATE KEY-----"

# 将标准的 RSA 私钥格式的字符串保存到文件中
with open('private_key.pem', 'w') as f:
    f.write(key_str)
