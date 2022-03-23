""" Reference: https://soatok.blog/2021/11/17/understanding-hkdf/ """

from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand as HKDFExpandClass, HKDF as HKDFClass
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

BACKEND = default_backend()

class HKDF:
    """ Convert a secret into key material suitable for use in encryption, integrity checking or authentication.
    It is suitable for deriving keys of a fixed size used for other cryptographic operations. """

    __slots__ = ('__info', '__length', 'hash_algorithm')

    def __init__(self, info: bytes, length: int = 32) -> None:
        """ Initialize object attributes.

        :param info: key derivation data
        :param length: the final length of the derived key """

        self.__info = info
        self.__length = length

        self.hash_algorithm = hashes.SHA512()

    def derive(self, material: bytes, salt: bytes|None = None) -> bytes:
        """ Derives a new key from the input key material.

        :param material: the input key material
        :param salt: the salt that is used to randomize the KDF's output. Optional, but highly recommended
        :return: the derived key """

        hkdf = HKDFClass(algorithm=self.hash_algorithm, length=self.__length, info=self.__info, salt=salt, backend=BACKEND)

        return hkdf.derive(material)

class HKDFExpand:
    """ HKDF consists of two stages, extract and expand. This class exposes an expand only version of HKDF that is suitable when the key material is already cryptographically strong.
    HKDFExpand should only be used if the key material is cryptographically strong. You should use HKDF if you are unsure. """

    def __init__(self, info: bytes, length: int = 32) -> None:
        self.__info = info
        self.__length = length

        self.hash_algorithm = hashes.SHA512()

    def derive(self, material):
        """ Derives a new key from the input key material.

        :param material: the input key material
        :return: the derived key """

        hkdf = HKDFExpandClass(algorithm=self.hash_algorithm, length=self.__length, info=self.__info, backend=BACKEND)

        return hkdf.derive(material)
