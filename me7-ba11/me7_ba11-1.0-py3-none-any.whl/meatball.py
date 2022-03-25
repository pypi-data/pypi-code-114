from __future__ import absolute_import
from __future__ import unicode_literals

import os, uuid, queue, secrets, base64
from struct import *

from .__version__ import __version__
from .config.config import Config, load_config
from .structs.objects import MeatBallHeader, MeatBallData
from .exceptions import *
from .manage.manager import FileManager, DataManager, DeserializationData, DeserializationHeader, SerializationHeader, SerializationData
from .encrypt.encrypt import AESManageGetter

conf = load_config()

class MeatBallCore(object):
    """
    ## The Meatball core class
    """
    storage_manage_getter = None
    def __init__(
        self, file, local_config,
    ):  # type: (str, dict) -> None
        self.q_size = conf['queue']['size'] if local_config.get('queue_size') == None else local_config.get('queue_size')
        self._file = file
        self._local_config = local_config
        self.headerObj = None
        self.emptyEntry = []
        self.dataObjQueue = queue.Queue(maxsize = self.q_size) if local_config.get('queue_size') == None else local_config.get('queue_size')


    def __call__(self, *args, **kwargs):
        data = (args, kwargs)
        try:
            result = self
            
        except AttributeError:
            pass
        return (result, data)

    def __del__(self):
        pass

    def _LoadMeatBall(self):
        """
        load for meatball.
        """
        self.file_manage_getter = FileManager(self._file)

        if self._chk_file_exist(self._file):
            header_fmt = conf['header']['format']
            header_len = calcsize(header_fmt)
            with open(self._file, 'rb') as f:
                header_data = DeserializationHeader(f.read(header_len))
                self.headerObj = self.UnPackHeaderToObj(header_data)
                dataObjs, self.emptyEntry = self.DataObjSeeker(self.headerObj, self.dataObjQueue)
        else:
            if self._local_config.get('keyForEncryption') == None :
                self._local_config['keyForEncryption'] = secrets.token_bytes(2048)

            assert len(self._local_config['keyForEncryption']) <= 2048 , MeatBallEncryptionKeyLengthError

            maxFileLength = conf['header']['maxFileLength'] if self._local_config.get('maxFileLength') == None else self._local_config.get('maxFileLength')
            maxDataLength = conf['header']['maxDataLength'] if self._local_config.get('maxDataLength') == None else self._local_config.get('maxDataLength')
            maxAsset = conf['header']['maxAsset'] if self._local_config.get('maxAsset') == None else self._local_config.get('maxAsset')
            encoding = conf['header']['encoding'] 
            fileMode = conf['header']['fileMode'] if self._local_config.get('fileMode') == None else self._local_config.get('fileMode')
            dataMode = conf['header']['dataMode'] if self._local_config.get('dataMode') == None else self._local_config.get('dataMode')
            keyForEncryption = self._local_config['keyForEncryption'] 
            
            self.headerObj = MeatBallHeader(maxFileLength,maxDataLength,maxAsset, encoding, fileMode,dataMode, keyForEncryption)
            _chunk = SerializationHeader(self.headerObj)
            self.CreateFile(_chunk)
            dataObjs = []

        return self.headerObj, dataObjs


    def _chk_file_exist(self, file: str) -> bool:
        try:
            if os.path.getsize(file) > 0:
                return True
            else:
                os.remove(file)
                return False
        except OSError as e:
            return False

    def _chk_Asset(self, data_manage_getter:DataManager, dataObjs:MeatBallData): 
        if self.headerObj.maxAsset <= self.headerObj.lastIndex:
            self.headerObj.lastIndex = 0
            _chunk = SerializationHeader(self.headerObj)
            self.CreateFile(_chunk)

            self.emptyEntry = []
            for dataObj in dataObjs:
                data_manage_getter.AppendData(dataObj,self.emptyEntry, dataObj.dataSize)
            return


    def DataObjSeeker(self, headerObj:MeatBallHeader, dataObjQueue:queue.Queue = None, key:str = None) -> list :
        """
        The Seeker for data object.
        It find key data from file(s).
        """
        emptyEntry = []
        dataObjs = []
        if key == None: 
            with open(self._file, 'rb') as f:
                offset = headerObj.dataOffset
                if headerObj.lastIndex <= self.q_size:
                    start_index_num = 0 
                else:
                    start_index_num = headerObj.lastIndex - self.q_size
                for index in range(headerObj.lastIndex):
                    try:
                        f.seek(offset+9)
                        length = f.read(8)
                        length = unpack('=q', length)[0]
                    except Exception as e:
                        raise MeatBallSeekError
                    try:
                        
                        f.seek(offset)
                        binary = f.read(length+35+2) 
                        offset = f.tell()
                        
                        data = DeserializationData(binary, offset, length)
                        

                        if data[1] == 1:
                            if start_index_num <= index:
                                try:
                                    dataObj = self.UnPackDataToObj(data)
                                    
                                    dataObjQueue.put_nowait(dataObj)
                                except Exception as e:
                                    FullQueue
                                    break
                        else:
                            emptyEntry.append((data[0], data[2]))
                        try:
                            for dataObj in iter(dataObjQueue.get_nowait, None):
                                dataObjs.append(dataObj)
                        except queue.Empty:
                            pass
                    except:
                        while 1:
                            index += 1
                            offset = f.read(8)
                            
                            offset = unpack('=q', offset)[0]
                            f.seek(f.tell() - 7)

                            if f.tell()-1 == offset:
                                f.seek(offset)
                                break
            return dataObjs, emptyEntry

        else: 
            with open(self._file, 'rb') as f:

                offset = headerObj.dataOffset
                for index in range(headerObj.lastIndex):
                    try:
                        f.seek(offset+9)
                        length = f.read(8)
                        length = unpack('=q', length)[0]
                        f.seek(offset)
                        binary = f.read(length+35+2)
                        offset = f.tell()
                        
                        data = DeserializationData(binary, offset, length)
                        if str(uuid.UUID(bytes=data[5])) ==  key:
                            if data[1] != 0:
                                dataObj = self.UnPackDataToObj(data)
                                return dataObj
                            
                    except:
                        while 1:
                            index += 1
                            offset = f.read(8)
                            
                            offset = unpack('=q', offset)[0]
                            f.seek(f.tell() - 7)

                            if f.tell()-1 == offset:
                                f.seek(offset)
                                break
        return False 

    
    def UnPackHeaderToObj(self, data:tuple) -> MeatBallHeader:
        """
        Unpack header to object
        """
        signiture, headerSize, dataOffset, maxFileLength, maxDataLength, maxAsset, lastIndex, fileMode, dataMode, encoding, keyForEncryption, eoh = data

        headerObj = MeatBallHeader(
            maxFileLength, 
            maxDataLength, 
            maxAsset, 
            encoding.decode().rstrip('\x00'),
            fileMode, 
            dataMode, 
            keyForEncryption
        )
        headerObj.signiture = str(signiture,'utf-8', 'ignore')
        headerObj.headerSize = headerSize
        headerObj.dataOffset = dataOffset
        headerObj.lastIndex = lastIndex
        headerObj.eoh = eoh
        return headerObj

    def UnPackDataToObj(self,data:tuple) -> MeatBallData:
        """
        Unpack data to object
        """
        offset, dataFlag, dataSize, owner, encrypt, indexkey, data, crc = data
        try:
            dataObj = MeatBallData(
                indexkey, data.decode().rstrip('\u0000')
            )
        except:
            dataObj = MeatBallData(
            indexkey, data
            )
        dataObj.offset = offset
        dataObj.dataFlag = dataFlag
        dataObj.dataSize = dataSize
        dataObj.owner = owner
        dataObj.encrypt = encrypt
        dataObj.indexkey = indexkey
        dataObj.crc = crc
        return dataObj

    
    def CreateFile(self, _chunk:bytes):
        """
        Create chunk to file
        """
        with open(self._file ,'wb') as file:
            file.write(_chunk)
            file.close()

class MeatBall(MeatBallCore):
    """
    
    ## THE MEATBALL for line ctf lib
    ---
    Meatball is a small library that manages files.
    You can check the fast-managed data here.
    It supports simple AES encryption.
    There are small vulnerabilities that may occur when managing files.
    I want you to find a problem.
    
    ---

    ```python
    
    from me7_ba11.meatball import MeatBall

    ## Create meatball and create data
    # append data
    mb = MeatBall('meat.ball',)
    data = {data:'meatball'}
    key = mb.append(data)
    data = mb.get(key)
    print(data)
    {'uuid key':'meatball'}

    # update data
    data = {'key':'uuid key', 'data': 'meatball_change'}
    mb.update(data)
    data = mb.get(key)
    print(data)
    {'uuid key':'meatball_change'}

    ## File upload and update
    # upload
    with open('file','rb) as f:
        _file = f.read()

    data = {data:'meatball'} <- Parameters are not used when uploading files.
    key = mb.append(data, _file)
    data = mb.get(key)
    print(data)
    {'uuid key':'encoded file binary'}

    # update to file
    data = {'key':'uuid key', 'data': 'meatball'} <- Parameters are not used when uploading files.
    mb.update(data, _file)
    data = mb.get(key)
    print(data)
    {'uuid key':'encoded file binary'}

    ## Encryption
    # append data with encryption
    mb = MeatBall('meat.ball',)
    data = {data:'meatball', enc='on'}
    key = mb.append(data)
    data = mb.get(key)
    print(data)
    {'uuid key':'meatball'}

    # update data with encrtyption
    data = {'key':'uuid key', enc='on', 'data': 'meatball_change'}
    mb.update(data)
    data = mb.get(key)
    print(data)
    {'uuid key':'meatball_change'}

    ```
    """

    VERSION = __version__
    
    def __init__(
        self,
        file,  # type: str
        local_config = {},  # type: dict
        # config,  # type: Config
    ):
        super(MeatBall, self).__init__(file, local_config)
        self._config = Config()
        self.headerObj, self.dataObjs = self._LoadMeatBall()
        self.data_manage_getter = DataManager(self.headerObj, self._file)
        self.aes_manage_getter = AESManageGetter(self.headerObj.keyForEncryption)
        self.encoding = conf['header']['encoding']


    def _dataObjs_append(self, dataObj):
        if len(self.dataObjs) >= self.q_size:
            self.dataObjs.pop(0)
            self._dataObjs_append(dataObj)
        else:
            self.dataObjs.append(dataObj)
        return

    def append(self, param:dict = None, _file:bytes = None) -> str: 
        """
        ## Append the Object with parameter.
        ## This method need to the 'data', optional('enc','length') parameter.
        ## When you append file plese attatch the file.
        """
        enc = True if param.get('enc') in ['True', 'true', '1', 'on', 'On' ] else False

        if _file is not None:
            data = _file
        else:
            data = param.get('data')

        key = uuid.uuid4()
        if enc:
            enc_data = self.aes_manage_getter.encrypt(data,str(key))
            
            dataObj = MeatBallData(key.bytes, enc_data.decode())
            dataObj.encrypt = 1
            self.data_manage_getter.AppendData(dataObj, self.emptyEntry, len(enc_data))
            self._dataObjs_append(dataObj)
        else:
            dataObj = MeatBallData(key.bytes, data)
            if param == None:
                length = len(data.encode(self.encoding))
            else:
                try:
                    length = len(data) if param.get('length') == (None or "") else int(param.get('length'))
                except:
                    length = len(data)

            self.data_manage_getter.AppendData(dataObj, self.emptyEntry, length)
            self._dataObjs_append(dataObj)

        self._chk_Asset(self.data_manage_getter, self.dataObjs)
        return self.get({"key":str(key)})

    def update(self, param:dict = None, _file:bytes=None):
        """
        ## Update the Object with parameter.
        ## This method need to the 'key', 'data', optional('enc','length') parameter.
        ## When you update file plese attatch the file.
        """
        try: 
            result = {}
            indexkey = param.get('key')
            if _file != None:
                data = _file
            else:
                data = param.get('data')
            enc = True if param.get('enc') in ['True', 'true', '1', 'on', 'On' ] else False
            if enc:
                enc_data = self.aes_manage_getter.encrypt(data,indexkey)
                enc_data = enc_data.decode()
            for dataObj in self.dataObjs: 
                _uuid = str(uuid.UUID(bytes=dataObj.indexkey))
                
                if _uuid == indexkey:
                    dataObj.data = enc_data if enc else data
                    dataObj.encrypt = 1 if enc else 0
                    try:
                        length = len(dataObj.data) if param.get('length') == (None or "") else int(param.get('length'))
                    except:
                        length = len(dataObj.data)

                    result = self._json_factory(indexkey,dataObj, enc)
                    
                    self.data_manage_getter.ModifyData(dataObj, length, self.emptyEntry)

                    self._chk_Asset(self.data_manage_getter, self.dataObjs)
                    return result
            
            dataObj = self.find(indexkey)
            if dataObj:
                
                self._dataObjs_append(dataObj)

                dataObj.data = enc_data if enc else data
                dataObj.encrypt = 1 if enc else 0
                try:
                    length = len(dataObj.data) if param.get('length') == (None or "") else int(param.get('length'))
                except:
                    length = len(dataObj.data)

                result = self._json_factory(indexkey, dataObj, enc)
                
                self.data_manage_getter.ModifyData(dataObj, length, self.emptyEntry)
                
                self._chk_Asset(self.data_manage_getter, self.dataObjs)
                return result

            raise MeatBallNotFoundException
        except Exception as e:
            raise e

    def get_all(self):
        """
        ## Get All dataObjects.
        """
        results = {}
        for dataObj in self.dataObjs:
            
            _uuid = uuid.UUID(bytes=dataObj.indexkey)
            data = self._byte_data_factory(_uuid, dataObj)
            
            results.update(data)
            
        return results

    def _json_factory(self, _uuid:str, dataObj:MeatBallData, enc:bool):
        """
        ## Create for json data for requested client.
        """
        result = {}

        if enc :
            dec_data = self.aes_manage_getter.decrypt(dataObj.data,_uuid)
            result = self._byte_data_factory(_uuid, dataObj, dec_data)
        else:
            result = self._byte_data_factory(_uuid, dataObj)

        return result

    def _byte_data_factory(self,_uuid:str, dataObj:MeatBallData, dec_data:bytes=None):
        results = {}
        
        if type(dataObj.data) == bytes:
            encoded = base64.b64encode(dataObj.data).decode()
            results[str(_uuid)] = 'data:image/png;base64,{}'.format(encoded)
        else:
            results[str(_uuid)] = dataObj.data
        if dec_data != None:

            try:
                results[str(_uuid)] = dec_data.decode()
            except:
                decoded = base64.b64encode(dec_data).decode()
                results[str(_uuid)] = 'data:image/png;base64,{}'.format(decoded)

        return results

    def validation_data(self, dataObj:MeatBallData):
        """
        ## validate the Object with the written file.
        ## This method need to the 'dataObject'.
        """
        _chunk = SerializationData(dataObj=dataObj, encoding=conf['header']['encoding'])
        lcrc = unpack('=H',_chunk[-2:])[0]
        rcrc = self.data_manage_getter.ReadFromFile(dataObj)[7]
        assert lcrc==rcrc, MeatBallCRCException

    def get(self, param:dict):
        """
        ## Get Object with parameter.
        ## This method need to the 'key' parameter.
        """
        try:
            indexkey = param.get('key')
            for dataObj in self.dataObjs: 
                enc = True if dataObj.encrypt == 1 else False
                _uuid = str(uuid.UUID(bytes=dataObj.indexkey))
                
                if _uuid == indexkey:
                    self.validation_data(dataObj)

                    result = self._json_factory(_uuid, dataObj, enc)
                    return result

            dataObj = self.find(indexkey)
            if dataObj: 
                enc = True if dataObj.encrypt == 1 else False
                self.validation_data(dataObj)

                self._dataObjs_append(dataObj)
                result = self._json_factory(indexkey, dataObj, enc)
                return result
            raise MeatBallNotFoundException

        except Exception as e:
            raise e

    def get_env(self):
        """
        ## Retrive Meatball environment.
        """
        try:
            results = {}
            results['emptyEntry'] = self.emptyEntry
            results['emptyEntry size'] = len(self.emptyEntry)
            results['fileMode'] = "flash mode" if self.headerObj.fileMode == 0 else "store mode"
            results['dataMode'] = "append" if self.headerObj.dataMode == 0 else "rewrite"
            results['file'] = self._file
            results['header'] = {"maxDataLength":self.headerObj.maxDataLength,"maxFileLength":self.headerObj.maxFileLength, "maxAsset": self.headerObj.maxAsset}
            results['queue size'] = self.q_size
            results['queue'] = self.dataObjQueue.qsize()
            results['data_objects'] = len(self.dataObjs)
            results['disk_lastindex'] = self.headerObj.lastIndex
            return results

        except Exception as e:
            raise e

    def delete(self, param:dict) -> bool:
        """
        ## Delete Object with parameter.
        ## This method need to the 'key' parameter.
        """
        try:
            
            indexkey = param.get('key')
            for dataObj in self.dataObjs:
                _uuid = uuid.UUID(bytes=dataObj.indexkey)
                if indexkey == str(_uuid):
                    self.dataObjs.pop(self.dataObjs.index(dataObj))
                    self.emptyEntry.append((dataObj.offset,dataObj.dataSize))
                    self.data_manage_getter.DeleteData(dataObj)
                    return True
                else:
                    pass

            dataObj = self.find(indexkey)
            if dataObj:

                self.emptyEntry.append((dataObj.offset,dataObj.dataSize))
                return self.data_manage_getter.DeleteData(dataObj)
            
            raise MeatBallNotFoundException
        except Exception as e:
            raise e

    def find(self,key:str) -> MeatBallData: 
        """
        ## Find Object with parameter.
        ## This method need to the 'key' parameter.
        """
        return self.DataObjSeeker(self.headerObj,None, key)
