import binascii
from struct import *
from me7_ba11.structs.objects import MeatBallHeader, MeatBallData
from me7_ba11.config.config import load_config
from me7_ba11.exceptions import *


conf= load_config()

def DeserializationHeader(bytes:bytes) -> tuple:
    """
    Deserialization header
    """
    header_fmt = conf['header']['format']
    header_len = calcsize(header_fmt)
    struct_unpack = Struct(header_fmt).unpack_from
    return struct_unpack(bytes)

def DeserializationData(_bytes:bytes, offset:int, size:int)-> tuple:
    """
    Deserialization data
    """
    length = size
    data_fmt = "=qbqbb16s{l}sH".format(l= length)
    data_len = calcsize(data_fmt)
    struct_unpack = Struct(data_fmt).unpack_from
    _unpack_data = struct_unpack(_bytes)    

    crc = binascii.crc32(_bytes[:-2]) & 0xffff
    if crc != _unpack_data[7]:
        raise MeatBallCRCException
    return _unpack_data


def SerializationHeader(headerObj:MeatBallHeader) -> bytes:
    """
    Serialization Header
    """
    signiture = pack('<2s',headerObj.signiture.encode(headerObj.encoding))
    maxFileLength = pack('q',headerObj.maxFileLength)
    maxDataLength = pack('q',headerObj.maxDataLength)
    maxAsset = pack('q',headerObj.maxAsset)
    lastIndex = pack('q',headerObj.lastIndex)
    fileMode = pack('b',headerObj.fileMode)
    dataMode = pack('b',headerObj.dataMode)
    encoding = pack('10s',headerObj.encoding.encode(headerObj.encoding))
    keyForEncryption = pack('2048s',headerObj.keyForEncryption)
    eoh = pack('<I',headerObj.eoh)

    header_fmt = conf['header']['format']
    header_len = calcsize(header_fmt)
    
    headerObj.headerSize = header_len
    headerObj.dataOffset = header_len

    headerSize = pack('q', header_len)
    dataOffset = pack('q', header_len)
    _chunk = signiture + headerSize + dataOffset + maxFileLength + maxDataLength + maxAsset + lastIndex + fileMode + dataMode + encoding + keyForEncryption + eoh
    return _chunk

def SerializationData(dataObj:MeatBallData, encoding:str = None) -> bytes:
    """
    Serialization Data
    """
    if encoding == None:
        encoding = 'UTF-8'
    else:
        encoding = encoding

    try:
        length = len(dataObj.data.encode(conf['header']['encoding']))
        length = dataObj.dataSize if length < dataObj.dataSize  else length
    except:
        length = len(dataObj.data)
        length = dataObj.dataSize if length < dataObj.dataSize  else length

    offset = pack('q',dataObj.offset)
    dataFlag = pack('b',dataObj.dataFlag)

    dataSize = pack('q',length)
    owner = pack('b',dataObj.owner)
    encrypt = pack('b',dataObj.encrypt)
    indexkey = pack('16s', dataObj.indexkey)

    if type(dataObj.data) == bytes:
        data = pack('{l}s'.format(l= length), dataObj.data)
    else:
        data = pack('{l}s'.format(l= length), bytes(dataObj.data,encoding))
    
    _chunk = offset + dataFlag + dataSize + owner + encrypt + indexkey + data
    
    crc = binascii.crc32(_chunk) & 0xffff
    crc = pack('H',crc)

    _chunk = _chunk+crc

    return _chunk

class FileManager:
    """
    ## File Manager for meatball. 
    It is a function responsible for input/output of files.
    """
    file = None
    fileSize = None
    fileList = []
    headerObj = None
    maxFileLength = conf['header']['maxFileLength']
    fileMode = conf['header']['fileMode']
    def __init__(self, file): # type: (str) -> None
        self.file = file
    
    def __call__(self, headerObj:MeatBallHeader):
        pass
    def ExtendFile(self, fileSize):
        if self.maxFileLength < fileSize:
            raise MeatBallExceedMaxFileLength(fileSize)
        pass


class DataManager:
    """
    # mode of operation 0 : append,  1: rewrite mode
    """
    fileMode = conf['header']['fileMode']
    dataMode = conf['header']['dataMode']


    
    def __init__(
        self, 
        headerObj, 
        file
    ): # type: (MeatBallHeader, str) -> None
        self.headerObj = headerObj
        self.file = file
        


    def UpdateIndex(self,value = None) -> None:
        if value == None:
            self.headerObj.lastIndex += 1
        else:
            self.headerObj.lastIndex = value
            
        with open(self.file,'r+b') as f:
            f.seek(42)
            lastIndex = pack('q',self.headerObj.lastIndex)
            f.write(lastIndex)


    def AppendData(self, dataObj:MeatBallData, emptyEntry:list , dataSize:int):
        try:
            dataObj.dataFlag = 1
            dataObj.dataSize = dataSize 
            dataObj.owner = 0 

            if self.headerObj.maxDataLength < dataSize:
                raise MeatBallExceedMaxDataLength(dataSize)

            if self.dataMode == 1:
                
                for entry in emptyEntry: 
                    if entry[1] >= dataSize:
                        dataObj.offset = entry[0]
                        dataObj.dataSize = entry[1]
                        
                        _chunk = SerializationData(dataObj,self.headerObj.encoding)

                        with open(self.file,'r+b') as f:
                            f.seek(dataObj.offset)
                            f.write(_chunk)
                        emptyEntry.pop(emptyEntry.index(entry))
                        return 

                with open(self.file,'a+b') as file:
                    file.seek(0,2)
                    dataObj.offset = file.tell()

                    _chunk = SerializationData(dataObj,self.headerObj.encoding)
                    file.write(_chunk)
                self.UpdateIndex()
                return         
            else:
                with open(self.file,'a+b') as file:
                    file.seek(0,2)
                    dataObj.offset = file.tell()

                    _chunk = SerializationData(dataObj,self.headerObj.encoding)
                    file.write(_chunk)
                self.UpdateIndex()
            return 
        except Exception as e:
            raise e
                    

    def ModifyData(self, dataObj:MeatBallData, size_new:int, emptyEntry:list):
        try:
            if dataObj.dataSize < size_new: 

                emptyEntry.append((dataObj.offset,dataObj.dataSize))

                self.DeleteData(dataObj)
                
                self.AppendData(dataObj,emptyEntry,size_new) 

            else:                 
                _chunk = SerializationData(dataObj,conf['header']['encoding'])
                
                with open(self.file,'r+b') as f:
                    f.seek(dataObj.offset)
                    f.write(_chunk)
        except Exception as e:
            raise MeatBallModifyException

    def ReadFromFile(self, dataObj:MeatBallData):

        data_fmt = "=qbqbb16s{l}sH".format(l= dataObj.dataSize)
        data_len = calcsize(data_fmt) 
        struct_unpack = Struct(data_fmt).unpack_from

        with open(self.file,'rb') as f:
            f.seek(dataObj.offset)
            data = f.read(data_len)
            
            result = struct_unpack(data)

            offset, dataFlag, dataSize, owner, encrypt, indexKey, data, crc = result
            if offset !=  dataObj.offset:
                raise DataReadError(offset, self.file)
            return result


    def DeleteData(self,dataObj:MeatBallData):
        offset = dataObj.offset

        with open(self.file,'r+b') as f:
            f.seek(offset+8)
            f.write(b'\x00')
            length = f.read(8)
            length = unpack('=q', length)[0]
            f.seek(offset)
            _chunk = f.read(length+35)

            crc = binascii.crc32(_chunk) & 0xffff
            crc = pack('H',crc)
            _chunk = _chunk + crc


            f.seek(offset)
            f.write(_chunk)
            return True