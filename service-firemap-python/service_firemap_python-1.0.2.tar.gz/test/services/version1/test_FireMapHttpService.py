# -*- coding: utf-8 -*-
import datetime
from typing import List

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.convert import JsonConverter
from pip_services3_commons.data import IdGenerator
from pip_services3_commons.random import RandomArray, RandomFloat, RandomInteger
from pip_services3_commons.refer import References, Descriptor
from pip_services3_rpc.test.TestCommandableHttpClient import TestCommandableHttpClient

from service_firemap_python.data.version1 import FireMapUpdateV1, \
    FireMapUpdateTypeV1, LocationV1, FireMapTileV1
from service_firemap_python.logic import FireMapController
from service_firemap_python.map_utils import FireMapUtil
from service_firemap_python.persistence import FireMapMemoryPersistence
from service_firemap_python.services.version1 import FireMapsCommandableHttpServiceV1


class TestFireMapHttpService:
    _persistence: FireMapMemoryPersistence
    _controller: FireMapController
    _service: FireMapsCommandableHttpServiceV1
    _client: TestCommandableHttpClient

    def setup_method(self):
        rest_config = ConfigParams.from_tuples(
            'connection.protocol', 'http',
            'connection.port', 3000,
            'connection.host', 'localhost'
        )

        self._persistence = FireMapMemoryPersistence()
        self._persistence.configure(ConfigParams())

        self._controller = FireMapController()
        self._controller.configure(ConfigParams())

        self._service = FireMapsCommandableHttpServiceV1()
        self._service.configure(ConfigParams())

        self._client = TestCommandableHttpClient('v1/firemap')
        self._client.configure(rest_config)

        references = References.from_tuples(
            Descriptor('eic-stopfires-services-firemap', 'persistence', 'memory', 'default', '1.0'),
            self._persistence,
            Descriptor('eic-stopfires-services-firemap', 'controller', 'default', 'default', '1.0'),
            self._controller,
            Descriptor('eic-stopfires-services-firemap', 'service', 'http', 'default', '1.0'),
            self._service)

        self._controller.set_references(references)
        self._service.set_references(references)

        self._persistence.open(None)
        self._persistence.clear(None)
        self._service.open(None)
        self._client.open(None)

    def teardown_method(self):
        self._persistence.close(None)
        self._service.close(None)
        self._client.close(None)

    def test_get_and_update_fire_maps(self):
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

        self._client.call_command('update_tiles', None, JsonConverter.to_json({'updates': updates}))

        res = self._client.call_command('get_tiles', None, {})

        assert isinstance(res, list)
        assert len(res) > 0

        # test filters
        params = {
            'flat': -10, 'flng': -50,
            'tlat': 45, 'tlng': 50,
            'zoom': 2
        }

        res = self._client.call_command('get_tiles', None, params)

        # json to tiles
        tiles: List[FireMapTileV1] = []
        for tile in res:
            tiles.append(FireMapTileV1.from_json(tile))

        for tile in tiles:
            assert tile.zoom == 2
            assert params['flat'] <= tile.flat <= params['tlat']
            assert params['flng'] <= tile.flng <= params['tlng']
            assert params['flat'] <= tile.tlat <= params['tlat']
            assert params['flng'] <= tile.tlng <= params['tlng']

        # update created tiles
        update = updates[0]
        update.people = 150

        zoom = 0
        locator = FireMapUtil.get_locator(LocationV1(update.lat, update.long))
        locator = FireMapUtil.compose_tile_loc_by_zoom(locator, zoom)

        self._client.call_command('update_tiles', None, JsonConverter.to_json({'updates': [update]}))

        res = self._client.call_command('get_tiles', None, {'zoom': zoom})

        # json to tiles
        tiles: List[FireMapTileV1] = []
        for tile in res:
            tiles.append(FireMapTileV1.from_json(tile))

        assert len(tiles) > 0
        tile = list(filter(lambda x: x.id == locator, tiles))[0]

        assert tile.id == locator
        assert tile.people_count == 150
