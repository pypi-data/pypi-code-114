from passlib.context import CryptContext

class VerifyKeys:
    """ Encrypt and Verify keys """

    def __init__(self):
        """ Initialize the class """
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def encrypt(self, key):
        """ Encrypt key
        :param key: Key to encrypt
        :return: Encrypted Key
        """
        return self.pwd_context.hash(key)

    def verify(self, plain_key, encrypted_key):
        """ Compare encrypted and plain keys
        :param plain_key: Plain text Key
        :param encrypted_key: Encrypted Key
        :return: Whether the keys are equal or not
        """
        return self.pwd_context.verify(plain_key, encrypted_key)
