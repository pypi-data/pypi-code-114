import hashlib
from cryptography.fernet import Fernet

import base64

import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Crypto():

    def __init__(self):
        pass

    def _generate_key(self, passphrase):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=passphrase.encode(),
            iterations=390000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))
        return key

    def encrypt(self, text, passphrase):
        f = Fernet(self._generate_key(passphrase))
        return f.encrypt(text.encode())


    def decrypt(self, encrypted_text, passphrase):
        f = Fernet(self._generate_key(passphrase))

        return f.decrypt(encrypted_text.encode())

