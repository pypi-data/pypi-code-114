from abc import *
from ptCrypt.Symmetric.Cipher import Cipher


class BlockCipher(Cipher):

    class WrongBlockSizeException(Exception):
        pass

    @property
    @staticmethod
    @abstractmethod
    def blockSize():
        pass