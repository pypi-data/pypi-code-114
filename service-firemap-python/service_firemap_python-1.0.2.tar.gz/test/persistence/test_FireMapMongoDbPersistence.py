# -*- coding: utf-8 -*-
import os

from pip_services3_commons.config import ConfigParams

from service_firemap_python.persistence import FireMapMongoDbPersistence
from test.persistence.FireMapPersistenceFixture import FireMapPersistenceFixture

mongodb_uri = os.environ.get('MONGO_SERVICE_URI')
mongodb_host = os.environ.get('MONGO_SERVICE_HOST') or 'localhost'
mongodb_port = os.environ.get('MONGO_SERVICE_PORT') or 27017
mongodb_database = os.environ.get('MONGO_SERVICE_DB') or 'test'


class TestFireMapMongoDbPersistence:
    persistence: FireMapMongoDbPersistence
    fixture: FireMapPersistenceFixture

    def setup_method(self):
        self.persistence = FireMapMongoDbPersistence()
        self.persistence.configure(ConfigParams.from_tuples(
            'connection.uri', mongodb_uri,
            'connection.host', mongodb_host,
            'connection.port', mongodb_port,
            'connection.database', mongodb_database,
        ))

        self.fixture = FireMapPersistenceFixture(self.persistence)

        self.persistence.open(None)
        self.persistence.clear(None)

    def teardown_method(self):
        self.persistence.close(None)

    def test_get_and_update_fire_maps(self):
        self.fixture.test_get_and_update_fire_maps()
