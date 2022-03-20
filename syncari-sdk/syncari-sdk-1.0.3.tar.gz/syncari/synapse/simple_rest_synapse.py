from abc import abstractmethod
import json
from enum import Enum
from syncari.models.core import (Record, Result)
from syncari.models.request import Response, Request
from syncari.rest.client import SyncariRestClient
from syncari.synapse.abstract_synapse import Synapse

class CrudOperation(Enum):
    """
        Identifies all crud operations
    """
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    GET = 'GET'
    DELETE = 'DELETE'

class SimpleRestSynapse(Synapse):
    """
        A simple rest synapse class that implements standard rest methods.
    """

    def __init__(self, request: Request, id_field: str, response_path: str) -> None:
        super().__init__(request)
        self.rest_client = None
        self.id_field = id_field
        self.response_path = response_path

    @abstractmethod
    def get_rest_client(self):
        pass

    def synapse_info(self):
        return super().synapse_info()

    def init(self):
        return super().init()

    def refresh_token(self):
        return super().refresh_token()

    def get_access_token(self):
        return super().get_access_token()

    def describe(self):
        return super().describe()

    def read(self):
        return super().read()

    def get(self):
        return self.__crud(CrudOperation.GET)

    def create(self):
        return self.__crud(CrudOperation.CREATE)

    def update(self):
        return self.__crud(CrudOperation.UPDATE)

    def delete(self):
        return self.__crud(CrudOperation.DELETE)

    def extract_webhook_identifier(self):
        return super().extract_webhook_identifier()

    def process_webhook(self):
        return super().process_webhook()

    @abstractmethod
    def process_single_row(self):
        pass

    def __crud(self, operation):
        entity_name = self.request.body.entity.apiName
        super().print(self.get.__name__, self.request)
        rest_client = self.get_rest_client()
        eds = []
        for data in self.request.body.data:
            data = Record.parse_obj(data)
            resp = None
            try:
                if operation is CrudOperation.GET:
                    resp = rest_client.rest_request('GET', '/' + entity_name + "s" + "/" + data.id, params=rest_client.auth_config, json=data.values)
                elif operation is CrudOperation.CREATE:
                    resp = rest_client.rest_request('POST', '/' + entity_name + "s", params=rest_client.auth_config, json=data.values)
                elif operation is CrudOperation.UPDATE:
                    resp = rest_client.rest_request('PUT', '/' + entity_name + "s" + "/" + data.id, params=rest_client.auth_config, json=data.values)
                elif operation is CrudOperation.DELETE:
                    resp = rest_client.rest_request('DELETE', '/' + entity_name + "s" + "/" + data.id, params=rest_client.auth_config)

                if self.response_path in resp.json():
                    row = resp.json()[self.response_path]
                    if operation is CrudOperation.GET:
                        eds.append(self.process_single_row(entity_name, self.request.body.entity, row).json())
                    else:
                        eds.append(Result(id=row[self.id_field],syncariId=data.syncariEntityId,success=True).json())
            except Exception as e:
                eds.append(Result(id=data.id,syncariId=data.syncariEntityId,success=False,errors=[str(e)]).json())
        return Response(body=json.dumps(eds))

    