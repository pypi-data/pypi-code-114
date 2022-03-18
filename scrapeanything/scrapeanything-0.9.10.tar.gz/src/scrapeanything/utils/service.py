from scrapeanything.utils.config import Config
from scrapeanything.database.repository import Repository
from scrapeanything.integration.excel import Excel
from scrapeanything.integration.csv import Csv
from scrapeanything.scraper.parser import Parser
from scrapeanything.database.models import Model
from scrapeanything.utils.constants import *

import requests
from enum import Enum

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

    def wget(self, url: str, parameters: dict=None, method: Methods=Methods.GET) -> any:
        return requests.get(url, data = parameters)
