# -*- coding: utf-8 -*-

from pip_services3_commons.config import ConfigParams

from service_firemap_python.persistence import FireMapFilePersistence
from test.persistence.FireMapPersistenceFixture import FireMapPersistenceFixture


class TestFireMapFilePersistence:
    persistence: FireMapFilePersistence
    fixture: FireMapPersistenceFixture

    def setup_method(self):
        self.persistence = FireMapFilePersistence()
        self.persistence.configure(ConfigParams.from_tuples(
            'path', './data/firemap.test.json'
        ))

        self.fixture = FireMapPersistenceFixture(self.persistence)

        self.persistence.open(None)
        self.persistence.clear(None)

    def teardown_method(self):
        self.persistence.close(None)

    def test_get_and_update_fire_maps(self):
        self.fixture.test_get_and_update_fire_maps()
