from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import SECP256R1, SECP384R1, SECP521R1, SECP224R1, SECP192R1
BACKEND = default_backend()

class ECDH:
    """ Generates a local wallet that contains a private key that will be used to exchange ECDH keys between peers. """

    __slots__ = ('__private_key')

    def __init__(self, curve = ec.SECP521R1()):
        self.__private_key = ec.generate_private_key(curve, BACKEND)

    def private_key(self):
        """ Return the local private key.

        :return: the private key """

        return self.__private_key

    def public_key(self):
        """ Return the public key of the local private key.

        :return: the public key """

        return self.__private_key.public_key()

    def exchange(self, public_key):
        """ Performs a key exchange operation using the provided algorithm with the peer's public key.

        :param public_key: the peer's public key
        :return: the shared key """

        return self.__private_key.exchange(ec.ECDH(), public_key)
