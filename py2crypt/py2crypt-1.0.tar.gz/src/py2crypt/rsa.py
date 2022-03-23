from cryptography.hazmat.primitives.asymmetric.padding import MGF1, PSS, OAEP
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

BACKEND = default_backend()

class RSA:
    """ Generates a local wallet that contains an RSA private key. """

    __slots__ = ('__private_key', 'hash_algorithm')

    PUBLIC_EXPONENT = 65537

    def __init__(self, private_key=None, length: int = 4096):
        """ Initialize object attributes.

        :param length: private key length
        :param private_key: existing private key """

        self.hash_algorithm = hashes.SHA512()

        if not private_key:
            self.__private_key = rsa.generate_private_key(public_exponent=self.PUBLIC_EXPONENT, key_size=length, backend=BACKEND)
        else:
            self.__private_key = private_key

    def private_key(self):
        """ Return the local private key.

        :return: the private key """

        return self.__private_key

    def public_key(self):
        """ Return the public key of the local private key.

         :return: the public key """

        return self.__private_key.public_key()

    def encrypt(self, public_key, plaintext: bytes) -> bytes:
        """ Encrypt data.

        :param public_key: the peer public key
        :param plaintext: the text/data that is going to be encrypted
        :return: bytes datatype that contains the encrypted text """

        return public_key.encrypt(plaintext, OAEP(mgf=MGF1(algorithm=self.hash_algorithm), algorithm=self.hash_algorithm, label=None))

    def decrypt(self, ciphertext: bytes) -> bytes:
        """ Decrypt encrypted data.

        :param ciphertext: the encrypted data that is going to be decrypted
        :return: the plain text content """

        return self.__private_key.decrypt(ciphertext, OAEP(mgf=MGF1(algorithm=self.hash_algorithm), algorithm=self.hash_algorithm, label=None))

    def sign(self, content: bytes) -> bytes:
        """ Sign data with private key.

        :param content: the content to be signed by your private key
        :return: the final signature """

        return self.__private_key.sign(content, PSS(mgf=MGF1(self.hash_algorithm), salt_length=PSS.MAX_LENGTH), self.hash_algorithm)

    def verify(self, public_key, signature: bytes, content: bytes) -> bool:
        """ Verify a signature.

        :param public_key: the peer public key
        :param signature: the signature the peer signed
        :param content: the content signed
        :return: boolean indicating if the signature is valid """

        try:
            boolean = public_key.verify(signature, content, PSS(mgf=MGF1(self.hash_algorithm), salt_length=PSS.MAX_LENGTH), self.hash_algorithm)

            if boolean is None:
                return True
        except InvalidSignature:
            pass
        return False
