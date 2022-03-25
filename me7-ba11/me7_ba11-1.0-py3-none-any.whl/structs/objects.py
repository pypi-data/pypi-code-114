

class MeatBallHeader(object):
    """
    header of meatball

    |  Signiture  |  Header Size  |  Data Offset  |  Max File Length  |  Max Data Length  |  Max Asset  |  last index  |    File Mode       |  Data Mode  |  Encoding  |  Key For Encryption  |  EOH     |
    |   2 byte    |  8 byte       |  8 byte       |  8 byte           |  8 byte           |  8 byte     |     8 byte   |    1 byte          |  1 byte     |  10 byte   |  2048 byte           |  4 byte  |
    
    # File Mode -> 0 : flash mode, 1: storage mode
    # Data Mode -> 0 : append,  1: rewrite mode
    
    
    """
    signiture = "MB"
    headerSize = None
    dataOffset = None
    maxFileLength = None
    maxDataLength = None
    maxAsset = None
    lastIndex = 0
    fileMode = None 
    dataMode = None
    encoding = None
    keyForEncryption = None
    eoh = 0xff484F45

    def __init__(self, 
        maxFileLength,
        maxDataLength,
        maxAsset ,  
        encoding, 
        fileMode , 
        dataMode , 
        keyForEncryption, 
    ): #type: (int, int,int,str,int,int,str) -> None
        self.maxFileLength = maxFileLength
        self.maxDataLength = maxDataLength
        self.maxAsset = maxAsset
        self.encoding = encoding
        self.fileMode = fileMode
        self.dataMode = dataMode
        self.keyForEncryption = keyForEncryption


class MeatBallData(object):
    """
    Data struct of meatball
    |  offset    |  Flag   |  Data Size  |  Owner  |  Encrypt  |  index key     |  Data           |        CRC      |
    |  8 byte    |  1 byte |  8 byet     |  1 byte |  1 byte   |  16byte        |  MEATBALLLLLLL  |        2byte    |

    Flag : 1 use 0 deleted(appended)
    Owner : user/admin # TODO
    Encrypt : true/false
    object overflow data leak

    """
    offset = None
    dataFlag = None
    dataSize = None
    owner = None
    encrypt = 0 # 
    indexkey = None #
    data = None
    crc = None
    
    def __init__(self,  indexkey:bytes, data) -> None:
        self.indexkey = indexkey
        self.data = data
