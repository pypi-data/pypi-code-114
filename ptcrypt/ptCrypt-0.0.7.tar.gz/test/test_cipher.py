from ptCrypt.Symmetric.AES import AES
from ptCrypt.Symmetric.BlockCipher import BlockCipher


def testCipherCreation():

    cipher = AES(b"1234")
    cipher.blockSize = 1
    someFun(cipher)


def someFun(value: BlockCipher):
    print(AES.blockSize)
    print(value.key)