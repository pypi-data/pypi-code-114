from cryptography.hazmat.primitives.ciphers.algorithms import AES as AESAlgorithm
from cryptography.hazmat.primitives.ciphers.modes import CTR
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.backends import default_backend
from os import urandom

IV_SIZE = 16 # bytes

AES128_SIZE = 16 # bytes
AES192_SIZE = 24 # bytes
AES256_SIZE = 32 # bytes

BACKEND = default_backend()

class AES:
    """ Create an object based on key to encrypt and decrypt data using AES-CTR. """

    __slots__ = ('__key')

    def __init__(self, key: bytes) -> None:
        """ Initialize object attributes.

        :param key: the cipher key used to encrypt """

        self.__key = key

    def __cipher(self, nonce: bytes) -> Cipher:
        """ Create cipher object.

        :param nonce: unique value that will never be reused. Does not need to be kept secret """

        return Cipher(AESAlgorithm(self.__key), CTR(nonce), backend=BACKEND)

    def encrypt(self, plaintext: bytes) -> bytes:
        """ Encrypt data.

        :param plaintext: the text/data that is going to be encrypted
        :return: bytes datatype that contains nonce + encrypted text """

        nonce = urandom(IV_SIZE)
        cipher = self.__cipher(nonce).encryptor()

        return nonce + cipher.update(plaintext) + cipher.finalize()

    def decrypt(self, ciphertext: bytes) -> bytes:
        """ Decrypt encrypted data.

        :param ciphertext: the encrypted data that is going to be decrypted
        :return: the plain text content """

        nonce, ciphertext = ciphertext[:IV_SIZE], ciphertext[IV_SIZE:]
        cipher = self.__cipher(nonce).decryptor()

        return cipher.update(ciphertext) + cipher.finalize()
