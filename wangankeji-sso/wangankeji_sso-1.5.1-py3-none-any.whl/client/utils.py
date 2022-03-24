import base64
import random

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_v1_5 as RSA_CIPER
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature

#
# # AES（对称加密）相关参数
# AES_KEY = 'CHPF1xk7OBfkGIqLoq6VbE0s5DXawHsF'
# # 使用MODE_CBC, MODE_CFB, MODE_OFB这几种模式之一时，请携带参数iv
# AES_IV = 'JSd4a3GCJOHx0Wfr'
# 暂支持以下种模式
"""
MODE_ECB = 1
MODE_CBC = 2
MODE_CFB = 3
MODE_OFB = 5
"""
AES_ENCRYPT_MODE = AES.MODE_CBC

# key支持16、24和32个字节三种格式，也就是128,192和256位
AES_KEY_SIZE = 32

# 支持iv的模式
APPLICABLE_FOR_IV = [AES.MODE_CBC, AES.MODE_CFB, AES.MODE_OFB]

# RSA（非对称加密）相关参数
RSA_KEY_SIZE = 2048


def aes_key_iv(size=AES_KEY_SIZE):
    """
    获取aes加密密钥和向量
    """
    key = Random.get_random_bytes(size)
    iv = Random.get_random_bytes(16)
    return key, iv


def pkcs7padding(data):
    """
    填充数据
    """
    # AES.block_size 16位
    bs = AES.block_size
    padding = bs - len(data) % bs
    padding_text = chr(padding) * padding
    return data + padding_text.encode('utf-8')


def pkcs7unpadding(data):
    """
    解填充数据
    """
    lengt = len(data)
    unpadding = data[lengt - 1]
    # ord()
    return data[0:lengt - unpadding]


def rsa_key(size=RSA_KEY_SIZE):
    """
    获取rsa公钥和私钥
    """
    random_generator = Random.new().read
    rsa = RSA.generate(size, random_generator)
    # 生成私钥
    private_key = rsa.exportKey()
    # 生成公钥
    public_key = rsa.publickey().exportKey()
    return public_key, private_key


class Aes:
    @staticmethod
    def encrypt(data: [str, bytes], key, iv, res_type='str'):
        """
        AES加密
        :param data:加密内容
        :param key:加密密钥
        :param iv:加密向量，非必须参数，指定某些模式时需要携带
        :param res_type:返回值类型,默认返回字符串，期望返回bytes时指定此参数值为'bytes'
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'

        if not isinstance(key, (str, bytes)):
            return 'Unsupported type for key!'

        if iv and not isinstance(iv, (str, bytes)):
            return 'Unsupported type for iv!'

        if isinstance(data, str):
            data = data.encode()

        if isinstance(key, str):
            key = key.encode()

        if isinstance(iv, str):
            iv = iv.encode()

        if AES_ENCRYPT_MODE in APPLICABLE_FOR_IV:
            data = pkcs7padding(data)
            cipher = AES.new(key, AES_ENCRYPT_MODE, iv)
        else:
            cipher = AES.new(key, AES_ENCRYPT_MODE)
        encrypted = cipher.encrypt(data)
        if res_type == 'bytes':
            return base64.b64encode(encrypted)
        else:
            return base64.b64encode(encrypted).decode()

    @staticmethod
    def decrypt(data: [str, bytes], key, iv, res_type='str'):
        """
        AES解密
        :param data:解密内容
        :param key:解密密钥
        :param iv:解密向量，非必须参数，指定某些模式时需要携带
        :param res_type:返回值类型,默认返回字符串，期望返回bytes时指定此参数值为'bytes'
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'

        if not isinstance(key, (str, bytes)):
            return 'Unsupported type for key!'

        if iv and not isinstance(iv, (str, bytes)):
            return 'Unsupported type for iv!'

        if isinstance(data, str):
            data = data.encode()

        if isinstance(key, str):
            key = key.encode()

        if isinstance(iv, str):
            iv = iv.encode()

        data = base64.b64decode(data)
        if AES_ENCRYPT_MODE in APPLICABLE_FOR_IV:
            cipher = AES.new(key, AES_ENCRYPT_MODE, iv)
            decrypted = cipher.decrypt(data)
            decrypted = pkcs7unpadding(decrypted)
        else:
            cipher = AES.new(key, AES_ENCRYPT_MODE)
            decrypted = cipher.decrypt(data)
        if res_type == 'bytes':
            return decrypted
        else:
            return decrypted.decode()

    @staticmethod
    def get_iv():
        """
        生成长度为16的随机字符串
        包含以下字符:
        qwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&amp;*()_+-={}[];':"|,./&lt;&gt;?
        :return:
        """
        seed = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%^&*()_+-={}[];':\"|,./<>?"
        return ''.join(random.choices(seed, k=16))


class Rsa:
    @staticmethod
    def encrypt(data: [str, bytes], public_key, res_type='str'):
        """
        RSA加密
        :param data:加密内容
        :param public_key:加密公钥
        :param res_type:返回值类型,默认返回字符串，期望返回bytes时指定此参数值为'bytes'
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'
        if not isinstance(public_key, (str, bytes)):
            return 'Unsupported type for public_key!'
        if isinstance(data, str):
            data = data.encode()
        if isinstance(public_key, bytes):
            public_key = public_key.decode()
        pub_key = RSA.importKey(public_key)
        cipher = RSA_CIPER.new(pub_key)
        encrypt_text = base64.b64encode(cipher.encrypt(bytes(data)))
        if res_type == 'bytes':
            return encrypt_text
        else:
            return encrypt_text.decode()

    @staticmethod
    def decrypt(data: [str, bytes], private_key, res_type='str'):
        """
        RSA解密
        :param data:解密内容
        :param private_key:解密私钥
        :param res_type:返回值类型,默认返回字符串，期望返回bytes时指定此参数值为'bytes'
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'
        if not isinstance(private_key, (str, bytes)):
            return 'Unsupported type for private_key!'
        if isinstance(data, str):
            data = data.encode()
        if isinstance(private_key, bytes):
            private_key = private_key.decode()
        pri_key = RSA.importKey(private_key)
        cipher = RSA_CIPER.new(pri_key)
        decrypt_text = cipher.decrypt(base64.b64decode(data), 0)
        if res_type == 'bytes':
            return decrypt_text
        else:
            return decrypt_text.decode()

    @staticmethod
    def sign(data: [str, bytes], private_key, res_type='str'):
        """
        RSA私钥加签
        :param data:加签内容
        :param private_key:签名私钥
        :param res_type:返回值类型,默认返回字符串，期望返回bytes时指定此参数值为'bytes'
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'
        if not isinstance(private_key, (str, bytes)):
            return 'Unsupported type for private_key!'
        if isinstance(data, str):
            data = data.encode()
        if isinstance(private_key, bytes):
            private_key = private_key.decode()

        pri_key = RSA.importKey(private_key)
        signer = PKCS1_signature.new(pri_key)
        digest = SHA.new()
        digest.update(data)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        if res_type == 'bytes':
            return signature
        else:
            return signature.decode()

    @staticmethod
    def verify(data: [str, bytes], signature: [str, bytes], public_key):
        """
        RSA公钥验签
        :param data: 验证内容
        :param signature: 加签内容
        :param public_key:验签公钥
        """
        if not isinstance(data, (str, bytes)):
            return 'Unsupported data type!'
        if not isinstance(signature, (str, bytes)):
            return 'Unsupported signature type!'
        if not isinstance(public_key, (str, bytes)):
            return 'Unsupported type for public_key!'
        if isinstance(data, str):
            data = data.encode()
        if isinstance(signature, str):
            signature = signature.encode()
        if isinstance(public_key, bytes):
            public_key = public_key.decode()

        pub_key = RSA.importKey(public_key)
        verifier = PKCS1_signature.new(pub_key)
        digest = SHA.new()
        digest.update(data)
        verification_res = verifier.verify(digest, base64.b64decode(signature))

        return verification_res


def get_aes_key_from_public_key(public_key):
    """
    获取用于AES加解密的key，从SSO公钥的第128个字符后开始读取，取出16个字符 (需要先处理换行符)
    :return:
    """
    # 移除密钥头标记
    return '\n'.join(public_key.split('\n')[1:]).replace('\r', '').replace('\n', '')[128:128 + 16]
