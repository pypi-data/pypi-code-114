from ptCrypt.Symmetric.BlockCipher import BlockCipher
from ptCrypt.Symmetric.Cipher import Cipher
from ptCrypt.Math.base import xor


class AES(BlockCipher):
    """AES cipher implementation according to FIPS-197.

    AES is a block cipher with block size of 16 bytes. There are three variants of AES with different key lengths and count of rounds:
        * AES-128 - 128-bit (16 bytes) key with 10 rounds
        * AES-192 - 192-bit (24 bytes) key with 12 rounds
        * AES-256 - 256-bit (32 bytes) key with 14 rounds

    This implementation will use appropriate variant according to the size of key passed to the constructor.
    Note that only encrypt() and decyprt() functions are instance-dependent, all other functions are static, and may be used without instantiating the object.
    """

    SBox = [
        0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 
        0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 
        0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 
        0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 
        0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 
        0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 
        0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8, 
        0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 
        0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 
        0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 
        0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 
        0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 
        0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 
        0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 
        0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 
        0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
    ]

    InvSBox = [
        0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
        0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
        0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
        0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
        0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
        0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
        0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
        0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
        0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
        0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
        0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
        0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
        0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
        0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
        0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
        0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
    ]

    blockSize = 16
    
    @property
    def key(self):
        return self._key
    
    def __init__(self, key: bytes):
        """Creates instance of AES cipher with given key.
        Will throw UnsupportedKeyLengthException if passed key is not 16, 24 or 32 bytes long.

        Parameters:
            key: bytes
                Secret key that will be used for encryption and decryption. Must have length of 16, 24 or 32 bytes.
        
        """
        if len(key) == 16: self._rounds = 10
        elif len(key) == 24: self._rounds = 12
        elif len(key) == 32: self._rounds = 14
        else:
            raise Cipher.UnsupportedKeyLengthException("Passed key with wrong length. AES standard only supports keys of sizes 4, 6 or 8 bytes")

        self._key = key
        self._roundKeys = AES.keyExpansion(self._key)
    
    def encrypt(self, data: bytes) -> bytes:
        """Encrypts one block of data. 
        Encryption operation is specified by FIPS-197, section 5.1
        Will throw WrongBlockSizeException if given data size is not equal to 16 bytes

        Parameters:
            data: bytes
                Data to be encrypted. Must be exactly 16 bytes long
        
        Returns:
            ciphertext: bytes
                Encrypted data
        """

        if len(data) != AES.blockSize: 
            raise BlockCipher.WrongBlockSizeException(f"Required data of size {AES.blockSize} bytes but {len(data)} bytes given")

        state = AES.bytesToState(data)

        AES.addRoundKey(state, self._roundKeys[0])

        for i in range(1, self._rounds):
            AES.subBytes(state)
            AES.shiftRows(state)
            AES.mixColumns(state)
            AES.addRoundKey(state, self._roundKeys[i])
            
        AES.subBytes(state)
        AES.shiftRows(state)
        AES.addRoundKey(state, self._roundKeys[-1])

        return AES.stateToBytes(state)

    def decrypt(self, data: bytes):
        """Decrypts one block of data. 
        Decryption operation is specified by FIPS-197, section 5.3
        Will throw WrongBlockSizeException if given data size is not equal to 16 bytes

        Parameters:
            data: bytes
                Encrypted data to be decrypted. Must be exactly 16 bytes long
        
        Returns:
            ciphertext: bytes
                Decrypted data
        """

        if len(data) != AES.blockSize:
            raise BlockCipher.WrongBlockSizeException(f"Required data of size {AES.blockSize} bytes but {len(data)} bytes given")
        state = AES.bytesToState(data)

        AES.addRoundKey(state, self._roundKeys[-1])

        for i in range(self._rounds - 1, 0, -1):
            AES.invShiftRows(state)
            AES.invSubBytes(state)
            AES.addRoundKey(state, self._roundKeys[i])
            AES.invMixColumns(state)
        
        AES.invShiftRows(state)
        AES.invSubBytes(state)
        AES.addRoundKey(state, self._roundKeys[0])

        return AES.stateToBytes(state)
    
    def addRoundKey(state: list, key: bytes):
        """AES AddRoundKey operation on cipher state specified by FIPS-197, section 5.1.4
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array
        
        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
                
            key: bytes
                16 bytes of AES round key
        """
        for r in range(len(state)):
            for c in range(len(state[r])):
                state[r][c] = state[r][c] ^ key[r + len(state) * c]

    def subBytes(state):
        """AES SubBytes operation on cipher state specified by FIPS-197, section 5.1.1
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """
        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] = AES.SBox[state[i][j]]
    
    def invSubBytes(state):
        """AES InvSubBytes operation on cipher state specified by FIPS-197, section 5.3.2
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """
        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] = AES.InvSBox[state[i][j]]

    def shiftRows(state):
        """AES ShiftRows operation on cipher state specified by FIPS-197, section 5.1.2
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """
        t = state[1][0]
        state[1][0] = state[1][1]
        state[1][1] = state[1][2]
        state[1][2] = state[1][3]
        state[1][3] = t
        
        state[2][0], state[2][2] = state[2][2], state[2][0]
        state[2][1], state[2][3] = state[2][3], state[2][1]

        t = state[3][3]
        state[3][3] = state[3][2]
        state[3][2] = state[3][1]
        state[3][1] = state[3][0]
        state[3][0] = t
    
    def invShiftRows(state):
        """AES InvShiftRows operation on cipher state specified by FIPS-197, section 5.3.1
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """

        t = state[1][3]
        state[1][3] = state[1][2]
        state[1][2] = state[1][1]
        state[1][1] = state[1][0]
        state[1][0] = t

        state[2][0], state[2][2] = state[2][2], state[2][0]
        state[2][1], state[2][3] = state[2][3], state[2][1]

        t = state[3][0]
        state[3][0] = state[3][1]
        state[3][1] = state[3][2]
        state[3][2] = state[3][3]
        state[3][3] = t

    def mixColumns(state):
        """AES MixColumns operation on cipher state specified by FIPS-197, section 5.1.3
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """
        for i in range(4):
            s0c = state[0][i]
            s1c = state[1][i]
            s2c = state[2][i]
            s3c = state[3][i]
            state[0][i] = AES.gmul(0x02, s0c) ^ AES.gmul(0x03, s1c) ^ s2c ^ s3c
            state[1][i] = s0c ^ AES.gmul(0x02, s1c) ^ AES.gmul(0x03, s2c) ^ s3c
            state[2][i] = s0c ^ s1c ^ AES.gmul(0x02, s2c) ^ AES.gmul(0x03, s3c)
            state[3][i] = AES.gmul(0x03, s0c) ^ s1c ^ s2c ^ AES.gmul(0x02, s3c)
    
    def invMixColumns(state):
        """AES InvMixColumns operation on cipher state specified by FIPS-197, section 5.3.3
        Operation is performed in-place, i.e. passed state list will be changed without allocating new array

        Parameters:
            state: list
                AES cipher state - 4 x 4 matrix of bytes
        """
        for i in range(4):
            s0c = state[0][i]
            s1c = state[1][i]
            s2c = state[2][i]
            s3c = state[3][i]
            state[0][i] = AES.gmul(0x0e, s0c) ^ AES.gmul(0x0b, s1c) ^ AES.gmul(0x0d, s2c) ^ AES.gmul(0x09, s3c)
            state[1][i] = AES.gmul(0x09, s0c) ^ AES.gmul(0x0e, s1c) ^ AES.gmul(0x0b, s2c) ^ AES.gmul(0x0d, s3c)
            state[2][i] = AES.gmul(0x0d, s0c) ^ AES.gmul(0x09, s1c) ^ AES.gmul(0x0e, s2c) ^ AES.gmul(0x0b, s3c)
            state[3][i] = AES.gmul(0x0b, s0c) ^ AES.gmul(0x0d, s1c) ^ AES.gmul(0x09, s2c) ^ AES.gmul(0x0e, s3c)

    def keyExpansion(key: bytes) -> list:
        """AES key schedule. Creates round keys for AES encryption and decryption from main key. Will return None if passed key size is not equal to 16, 24 or 32 bytes.
        Algorithm is specified by FIPS-197, section 5.2, although you might want to check this https://en.wikipedia.org/wiki/AES_key_schedule for better example.

        Parameters:
            key: bytes
                AES secret key. Must be 16, 24 or 32 bytes long, otherwise None will be returned.
        
        Returns:
            roundKeys: list
                List of round keys, size of the list depends on size of the key:
                    
                    * 11 keys for 16 bytes key
                    * 13 keys for 24 bytes key
                    * 15 keys for 32 bytes key
                    * None for all other key sizes
        """
        Rcon = [
            b"\x00\x00\x00\x00",
            b"\x01\x00\x00\x00",
            b"\x02\x00\x00\x00", 
            b"\x04\x00\x00\x00", 
            b"\x08\x00\x00\x00", 
            b"\x10\x00\x00\x00", 
            b"\x20\x00\x00\x00", 
            b"\x40\x00\x00\x00", 
            b"\x80\x00\x00\x00", 
            b"\x1b\x00\x00\x00", 
            b"\x36\x00\x00\x00"
        ]
        n = len(key) // 4
        if n == 4:
            r = 11
        elif n == 6:
            r = 13
        elif n == 8:
            r = 15
        else:
            return None
        
        keyWords = [key[4 * i: 4 * i + 4] for i in range(n)]
        
        resultWords = []
        for i in range(4 * r):
            if i < n: resultWords.append(keyWords[i])
            elif i >= n and i % n == 0:
                Wi1 = [AES.SBox[byte] for byte in resultWords[i - 1]]
                Wi1 = Wi1[1:] + Wi1[:1]
                Wi1 = b"".join(bytes([byte]) for byte in Wi1)
                Win = resultWords[i - n]
                resultWords.append(xor(xor(Win, Wi1), Rcon[i // n]))
            elif i >= n and n > 6 and i % n == 4:
                Win = resultWords[i - n]
                Wi1 = b"".join([bytes([AES.SBox[byte]]) for byte in resultWords[i - 1]])
                resultWords.append(xor(Win, Wi1))
            else:
                resultWords.append(xor(resultWords[i - n], resultWords[i - 1]))
        
        roundKeys = []
        for i in range(r):
            roundKeys.append(resultWords[4 * i] + resultWords[4 * i + 1] + resultWords[4 * i + 2] + resultWords[4 * i + 3])

        return roundKeys

    def bytesToState(data: bytes) -> list:
        """Helper function for converting bytes to AES state matrix.
        Will throw an exception if data size is not equal to 16 bytes.

        Parameters:
            data: bytes
                Data to convert
            
        Returns:
            state: list
                4 x 4 matrix of bytes
        """
        if len(data) != AES.blockSize:
            raise BlockCipher.WrongBlockSizeException(f"Data size is incorrect. Required {AES.blockSize} bytes, but received {len(data)}.")

        state = [[0, 0, 0, 0] for _ in range(4)]
        for r in range(4):
            for c in range(4):
                state[r][c] = data[r + 4 * c]
        return state

    def stateToBytes(state: list) -> bytes:
        """Helper function for converting AES state matrix to bytes

        Parameters:
            state: list
                4 x 4 AES state matrix (any matrix will be processed actually)
            
        Returns:
            data: bytes
                state matrix converted to bytes
        """

        result = b""
        for r in range(len(state)):
            for c in range(len(state[r])):
                result += bytes([state[c][r]])
        return result

    def gmul(a: int, b: int) -> int:
        """Helper function for performing AES GF(2^8) multiplication.
        Algorithm is taken from https://en.wikipedia.org/wiki/Rijndael_MixColumns

        Parameters:
            a, b: int
                Integer representation of polynomials in GF(2^8)
        
        Returns:
            result: int
                Integer representation of multiplied a and b in GF(2^8)
        """

        res = 0
        for _ in range(8):
            if b & 1 == 1: res ^= a
            highBitSet = (a & 0x80) != 0
            a = (a << 1) & 0xff
            if highBitSet: a = a ^ 0x1b
            b >>= 1
        return res