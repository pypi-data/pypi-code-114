# -*- coding: utf-8 -*-
import datetime

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.data import IdGenerator
from pip_services3_commons.random import RandomArray, RandomFloat, RandomInteger
from pip_services3_commons.refer import References, Descriptor

from service_firemap_python.data.version1 import FireMapUpdateV1, FireMapUpdateTypeV1, LocationV1
from service_firemap_python.logic import FireMapController
from service_firemap_python.map_utils import FireMapUtil
from service_firemap_python.persistence import FireMapMemoryPersistence


class TestFireMapController:
    persistence: FireMapMemoryPersistence
    controller: FireMapController

    def setup_method(self):
        self.persistence = FireMapMemoryPersistence()
        self.persistence.configure(ConfigParams())

        self.controller = FireMapController()
        self.controller.configure(ConfigParams())

        references = References.from_tuples(
            Descriptor('eic-stopfires-services-firemap', 'persistence', 'memory', 'default', '1.0'), self.persistence,
            Descriptor('eic-stopfires-services-firemap', 'controller', 'default', 'default', '1.0'), self.controller
        )

        self.controller.set_references(references)

        self.persistence.open(None)
        self.persistence.clear(None)

    def teardown_method(self):
        self.persistence.close(None)

    def test_get_and_update_tiles(self):
        # generate updates
        updates = []
        for i in range(10):
            updates.append(
                FireMapUpdateV1(
                    type=RandomArray.pick([e.value for e in FireMapUpdateTypeV1]),
                    time=datetime.datetime.now(),
                    drone_id=IdGenerator.next_long(),
                    long=RandomFloat.next_float(-180, 180),
                    lat=RandomFloat.next_float(-90, 90),
                    people=RandomInteger.next_integer(0, 15)
                )
            )

        self.controller.update_tiles(None, updates)

        tiles = self.controller.get_tiles(None, None, None, 3)

        assert isinstance(tiles, list)
        assert len(tiles) > 0

        # test filters
        of = LocationV1(lat=-10, long=-50)
        to = LocationV1(lat=45, long=50)
        tiles = self.controller.get_tiles(None, of, to, 2)

        for tile in tiles:
            assert tile.zoom == 2
            assert of.lat <= tile.flat <= to.lat
            assert of.long <= tile.flng <= to.long
            assert of.lat <= tile.tlat <= to.lat
            assert of.long <= tile.tlng <= to.long

        # update created tiles
        update = updates[0]
        update.people = 150

        zoom = 0
        locator = FireMapUtil.get_locator(LocationV1(update.lat, update.long))
        locator = FireMapUtil.compose_tile_loc_by_zoom(locator, zoom)

        self.controller.update_tiles(None, [update])

        tiles = self.controller.get_tiles(None, None, None, zoom)
        assert len(tiles) > 0
        tile = list(filter(lambda x: x.id == locator, tiles))[0]

        assert tile.id == locator
        assert tile.people_count == 150
