try:
    from .hkdf import HKDF
except ImportError:
    from hkdf import HKDF

from hmac import digest, compare_digest
from hashlib import sha512

class HMAC:

    __slots__ = ('__key', 'hash_algorithm')

    def __init__(self, key: bytes) -> None:
        self.__key = key
        self.hash_algorithm = sha512

    def digest(self, message: bytes) -> bytes:
        """ Return digest of message for given secret key and digest (hash algorithm).

        :param message: the message to be authenticated
        :return: digest of message """

        return digest(key=self.__key, msg=message, digest=self.hash_algorithm)

def hmac_compare(message: bytes, key: bytes, hmac: bytes, digest=sha512) -> bool:
    """ This function uses an approach designed to prevent timing analysis by avoiding content-based short circuiting behaviour, making it appropriate for cryptography.

    :param message: the message used in the HMAC you are comparing
    :param key: the key used  in the HMAC you are comparing
    :param hmac: the HMAC you are comparing
    :return: a boolean indicating if the HMACs are the same """

    hmac_obj = HMAC(key)
    hmac_obj.hash_algorithm = digest

    if compare_digest(hmac_obj.digest(message), hmac):
        return True
    return False
