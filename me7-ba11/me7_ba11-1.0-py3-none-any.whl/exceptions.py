class MeatBallException(Exception):
    def __init__(self, message="Common Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class FileOpenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class FullQueue(Exception):
    def __init__(self, message="Full Queue"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallDecryptionError(Exception):
    def __init__(self, message="Decryption Error"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallEncryptionKeyLengthError(Exception):
    def __init__(self, size,message="EncryptionKeyLengthError"):
        self.message = message
        self.size = size
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} {self.size}'

class MeatBallSeekError(Exception):
    def __init__(self, message="File Seek Error"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallExceedMaxFileLength(Exception):
    def __init__(self, size:int, message="ExceedMaxFileLength"):
        self.message = message
        self.size = size
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} the Size of you inserted {self.size}'

class MeatBallExceedMaxDataLength(Exception):
    def __init__(self, size:int, message="ExceedMaxDataLength"):
        self.message = message
        self.size = size
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message} the Size of you inserted {self.size}'

class MeatBallCRCException(Exception):
    def __init__(self, message="CRC Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallEncryptionException(Exception):
    def __init__(self, message="Encryption Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallDecryptionException(Exception):
    def __init__(self, message="Decryption Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'
        
        
class MeatBallAppendException(Exception):
    def __init__(self, message="MeatBallManager Append Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallModifyException(Exception):
    def __init__(self, message="MeatBallManager Modify Exception"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class MeatBallNotFoundException(Exception):
    def __init__(self, message="Could Not Found Data"):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}'

class FileNotAllowed(Exception):
    def __init__(self, _file_extension,message="File Not Allowed"):
        self.message = message
        self._file_extension = _file_extension
        super().__init__(self.message)
    def __str__(self):
        return f'{self._file_extension} {self.message}'

class DataSizeError(Exception):
    """
    Data Size overflow
    """
    def __init__(self, size_org: int, size_new: int, message="Data Size is overflowed"):
        self.size_org = size_org
        self.size_new = size_new
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.size_org} / {self.size_new} -> {self.message}'

class DataTypeError(Exception):
    """
    Data Type Error
    """
    def __init__(self, _type: str, message="Data type is missmatch"):
        self.type = _type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.type} -> {self.message}'

class DataReadError(Exception):
    """
    Data Type Error
    """
    def __init__(self, offset: str,  fileName: str, message="Data Read Error "):
        self.offset = offset 
        self.message = message
        self.fileName = fileName
        super().__init__(self.message)
    def __str__(self):
        with open(self.fileName,'rb') as f:
            f.seek(self.offset)
            data = f.read(4)
        return f'Debug : DataOffset : {self.offset} {data} -> {self.message} HexTrace : {data.hex()}'

