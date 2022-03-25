from scrapeanything.utils.config import Config
from scrapeanything.database.repository import Repository
from scrapeanything.database.models import Model
from scrapeanything.utils.constants import *

import requests
from enum import Enum

from scrapeanything.utils.types import Types

class Methods(Enum):
    POST = 'POST'
    GET = 'GET'
    PUT = 'PUT'

class Service:

    def __init__(self, config: Config=None, repository: Repository=None) -> None:
        if repository is not None:
            self.repository = repository
    
        if config is not None:
            self.config = config
    
    def __del__(self):
        if hasattr(self, 'repository'):
            self.repository.close()

    def all(self) -> 'list[Model]':
        entities = self.repository.all(entity_type=self.entity_type)
        return entities

    def load(self, entity: Model) -> Model:
        entity = self.repository.load(entity=entity)
        return entity

    def save(self, entity: Model) -> None:
        self.repository.save(entity=entity)

    def wget(self, url: str, parameters: dict=None, method: Methods=Methods.GET, response_type: str=Types.JSON) -> any:
        if method == Methods.GET:
            response = requests.get(url=url, data=parameters)
        elif method == Methods.POST:
            response = requests.post(url=url, data=parameters)
        else:
            raise Exception(f'{method} method is not supported')

        if response_type == Types.JSON:
            return response.json()
        elif response_type == Types.STRING:
            return response.text
        else:
            raise Exception(f'{response_type} response type is not supported')


