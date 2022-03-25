# coding: utf-8
import base64, hashlib
from Crypto import Random

from Crypto.Cipher import AES
from Crypto import Random
from me7_ba11.exceptions import *

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 

class AESManageGetter:
    def __init__(self, keyForEncryption:bytes) -> None:
        self.keyForEncryption = keyForEncryption


    def encrypt(self, raw, secret):
        try:
            if type(raw) == bytes:
                encoded_raw = base64.b64encode(raw).decode()
                raw = pad(encoded_raw).encode('ascii')
            else:
                encoded_raw = base64.b64encode(raw.encode('utf-8')).decode()
                raw = pad(encoded_raw).encode('ascii')
            secret = secret.encode("utf-8") + self.keyForEncryption
            private_key = hashlib.sha256(secret).digest()
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(private_key, AES.MODE_CBC, iv)
            return base64.b64encode(iv + cipher.encrypt(raw))
        except Exception as e:
            raise MeatBallEncryptionException
    
    def decrypt(self, enc, secret):
        try:
            secret = secret.encode("utf-8") + self.keyForEncryption
            private_key = hashlib.sha256(secret).digest()
            enc = base64.b64decode(enc)
            iv = enc[:16]
            cipher = AES.new(private_key, AES.MODE_CBC, iv)
            encoded_raw = unpad(cipher.decrypt(enc[16:]))
            if len(encoded_raw) != 0:
                return base64.b64decode(encoded_raw.decode('utf-8'))
            else:
                raise MeatBallDecryptionError
        except Exception as e:
            raise MeatBallDecryptionException
