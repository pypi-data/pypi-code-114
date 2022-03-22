# -*- coding: utf-8 -*-

from pip_services3_commons.config import ConfigParams
from pip_services3_data.persistence import JsonFilePersister

from service_firemap_python.persistence import FireMapMemoryPersistence


class FireMapFilePersistence(FireMapMemoryPersistence):

    def __init__(self, path: str = None):
        super().__init__()
        self._persister = JsonFilePersister(path)

        self._loader = self._persister
        self._saver = self._persister

    def configure(self, config: ConfigParams):
        super().configure(config)
        self._persister.configure(config)
