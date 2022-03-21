from bson.objectid import ObjectId
from requests.exceptions import ConnectionError
from contextlib import suppress
from fastapi.encoders import jsonable_encoder
from datetime import datetime
import motor.motor_asyncio
import json
import logging
import inspect

from .exceptions import *
from .models import *


class CyberUtils(dict):

    def __init__(self, config: ModelConfig, log_level: int = logging.INFO):
        config = jsonable_encoder(config)
        self.__load_config__(config)
        self.app_name = config.get('app_name')
        self.app_token = config.get('app_token')
        logging.basicConfig(level=log_level,
                            format='%(asctime)s | %(levelname)s | %(message)s')
        self.__logger__ = logging.getLogger(__name__)
        self.logger = CyberLogger(ModelLogger(url=config.get('logger', 'http://127.0.0.1')), self)
        self.db = CyberDB(config.get('database', {}), self)
        self.caller = CyberCaller(config.get('services', {}), self)
        super().__init__()

    def __load_config__(self, config: dict):
        self.app_name = config.get('app_name', None)
        if not self.app_name:
            raise CyberUtilConfigMissing("Application name missing")
        self.app_token = config.get('app_token', None)
        if not self.app_token:
            raise CyberUtilConfigMissing("Application token missing")

    def __prepare_log__(self, message: object, status_code: int = None, status_name: str = 'info',
                        method: str = None, log_server: bool = False, stack=None):
        the_class = None
        with suppress(KeyError):
            the_class = stack[1][0].f_locals["self"].__class__.__name__
            the_method = stack[1][0].f_code.co_name
        method_caller = f'{self.app_name} | {the_class}.{the_method}()' if the_class and the_method else self.app_name
        status_code = f"{' | ' if method_caller else ''}{status_code}" if status_code else ''
        method_type = f"{' | ' if status_code or method_caller else ''}{method.upper()}" if method else ''
        msg_content = f"{' | ' if status_code or method_caller else ''}{message}" if isinstance(message, str) else ''
        if isinstance(message, dict):
            msg_final = f"{method_caller}{status_code}{method_type}"
            is_json = True
            getattr(self.__logger__, status_name)(f"{method_caller}{status_code}{method_type}")
            print(json.dumps(message, ensure_ascii=False, indent=4))
        else:
            msg_final = f"{method_caller}{status_code}{method_type}{msg_content}"
            is_json = False
            getattr(self.__logger__, status_name)(f"{method_caller}{status_code}{method_type}{msg_content}")
        if hasattr(self, "caller") and log_server:
            send_content = dict(app_name=self.app_name, content=msg_content, logtime=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            if the_class and the_method:
                send_content.update(dict(caller=f"{the_class}.{the_method}()"))
            if status_code:
                send_content.update(dict(status_code=status_code))
            if method_type:
                send_content.update(dict(method_type=method_type))
            self.caller.do('post', self.logger, json_content=ModelLog(**send_content).__dict__())
        return dict(message=message, status_code=status_code)

    def log(self, message: object, status_code: int = None, status_name: str = 'info', method: str = None, log_server=True):
        if not hasattr(logging, status_name):
            self.__logger__.error(f"CyberLogger does not support {status_name} status name")
            return
        msg_final, is_json, log_for_server = self.__prepare_log__(message, status_code, status_name, method, log_server, inspect.stack())
        getattr(self.__logger__, status_name)(msg_final)
        if is_json:
            print(json.dumps(message, ensure_ascii=False, indent=4))
        self.caller.do('post', self.logger, json_content=ModelLog(**log_for_server).__dict__())


class CyberModel(dict):

    def __init__(self, config: dict, utils: CyberUtils):
        self.log = utils.log
        self.update(config)
        super().__init__()


class CyberLogger(CyberModel):

    def __init__(self, config: ModelLogger, utils: CyberUtils):
        config = jsonable_encoder(config)
        super().__init__(config, utils)


class CyberCaller(CyberModel):

    def __init__(self, config: ModelServices, utils: CyberUtils):
        config = jsonable_encoder(config)
        super().__init__(config, utils)
        self.headers = {
            'User-Agent': f"PyCyberUtils 0.0.1",
            'Cyber-Service-Name': utils.app_name,
            'Cyber-Service-Token': utils.app_token
        }

    def do(self, method: str, service: object, api: str = '', data: object = {}, json_content: dict = {},
           params: dict = {}, files: dict = None, headers: dict = None, timeout: int = 3):
        if method.lower() == 'post':
            from requests import post as caller
        else:
            from requests import get as caller
        if not api and isinstance(data, str):
            api = f"/{data}"
            data = dict()
        conf = {}
        if isinstance(service, str):
            conf = self.get(service, {})
        elif isinstance(service, CyberModel):
            conf = dict(enabled=True, url=service.get('url', ''))
        if conf.get('enabled', True):
            if url := conf.get('url', '').removesuffix('/'):
                try:
                    data.update(conf.get('data', {}))
                    json_content.update(conf.get('json', {}))
                    params.update(conf.get('params', {}))
                    self.log(f"{url}{api}", method=method, log_server=False)
                    if result := caller(url=f"{url}{api}", data=data, json=json_content, files=files,
                                        params=params, headers=self.headers if not headers else headers,
                                        timeout=timeout):
                        self.log(f"Recibimos la respuesta de {service}", status_code=result.status_code, log_server=False, status_name='debug')
                        if conf.get('type', '') == 'json':
                            return self.log(result.json(), result.status_code, log_server=False)
                        return self.log(result.content.decode('cp1252'), result.status_code, log_server=False)
                    return self.log(dict(error="No response from endpoint"), status_code=0, status_name='error', log_server=False)
                except ConnectionError as e:
                    return self.log(dict(error=str(e)), status_code=0, status_name='error', log_server=False)
            raise CyberCallerConfigMissing(f"Missing endpoint for service", service)


class CyberDB(CyberModel):

    def __init__(self, config: ModelDatabase, utils: CyberUtils):
        config = jsonable_encoder(config)
        super().__init__(config, utils)
        self.user = self.password = self.db_name = None
        self.host = '127.0.0.1'
        self.port = 27017
        mongo_uri = f'mongodb://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}?authSource=admin'
        self.client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
        self.log(self.user)

    def __init_db__(self, config: dict):
        if any([True for n in [self.user, self.password, self.db_name, self.host, self.port] if not n]):
            raise CyberDBConfigMissing("Missing any of this fields in database config: user, password, db_name, host or port")

    def collection(self, collection_name: str):
        self.log(f"Recogemos coleccion {collection_name}")
        return self.client.byg_data.get_collection(collection_name)

    @staticmethod
    def parse_helper(result: dict) -> dict:
        result['_id'] = str(result['_id'])
        return dict(result)

    async def retrieve_all(self,
                           collection_name: str,
                           query: dict = None,
                           filter_fields: dict = None) -> list:
        results = []
        async for result in self.collection(collection_name).find(
                query, filter_fields):
            print(result)
            results.append(self.parse_helper(result))
        return results

    async def retrieve_one(self, collection_name: str, id_obj: str) -> dict:
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            return self.parse_helper(result)

    async def insert(self, collection_name: str, data: dict) -> dict:
        result = await self.collection(collection_name).insert_one(data)
        new_result = await self.collection(collection_name).find_one(
            {"_id": result.inserted_id})
        return self.parse_helper(new_result)

    async def change(self, collection_name: str, id_obj: str,
                     data: dict) -> bool:
        if len(data) < 1:
            return False
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            updated_result = await self.collection(collection_name).update_one(
                {"_id": ObjectId(id_obj)}, {"$set": data})
            if updated_result:
                return True
            return False

    async def delete(self, collection_name: str, id_obj: str) -> bool:
        result = await self.collection(collection_name).find_one(
            {"_id": ObjectId(id_obj)})
        if result:
            await self.collection(collection_name).delete_one(
                {"_id": ObjectId(id_obj)})
            return True
