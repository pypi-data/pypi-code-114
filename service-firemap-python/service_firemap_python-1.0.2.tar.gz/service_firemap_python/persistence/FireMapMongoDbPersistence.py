# -*- coding: utf-8 -*-
from typing import Optional, List

import pymongo
from bson import Decimal128
from pip_services3_commons.data import FilterParams, PagingParams, DataPage
from pip_services3_mongodb.persistence import IdentifiableMongoDbPersistence

from .IFireMapPersistence import IFireMapPersistence
from ..data.version1.FireMapTileBlockV1 import FireMapTileBlockV1


class FireMapMongoDbPersistence(IdentifiableMongoDbPersistence, IFireMapPersistence):

    def __init__(self):
        super().__init__('firemap')
        self._max_page_size = 1000

    def __compose_filter(self, filter: FilterParams):
        filter = filter or FilterParams()
        criteria = []

        flng = filter.get_as_nullable_float('flng')
        flat = filter.get_as_nullable_float('flat')
        tlng = filter.get_as_nullable_float('tlng')
        tlat = filter.get_as_nullable_float('tlat')

        zoom = filter.get_as_nullable_integer('zoom')

        coordinates = filter.get_as_nullable_string('coordinates')

        if isinstance(coordinates, str):
            coordinates = coordinates.split(',')
        if not isinstance(coordinates, list):
            coordinates = None

        flng2 = None
        tlng2 = None

        # round to the next tile for current zoom
        if all([flng, flat, tlng, tlat]):
            # if coordinates is left top and right bottom corners
            if flat > tlat:
                flat, tlat = tlat, flat

            # if coordinates pass through the last meridian
            if flng > tlng:
                flng2 = -180
                tlng2 = tlng
                tlng = 180

        # get blocks for coordinates
        if coordinates:
            for location in coordinates:
                lat, long = location.split(';')
                lat, long = float(lat), float(long)
                criteria.extend([{'$and': [{'flng': {'$lte': long}}, {'tlng': {'$gte': long}},
                                           {'flat': {'$gte': lat}}, {'tlat': {'$lte': lat}}]}])

            criteria = [{'$or': criteria}]

        if flng and tlng and flat and tlat:
            # check intersections of tile block in passed coordinates
            criteria2 = None

            if flng2 and tlng2:
                criteria2 = self.__compose_intersect_request(flng2, tlng2, 'lng')

            criteria.extend(self.__compose_intersect_request(flng, tlng, 'lng'))

            if criteria2:
                criteria.extend(criteria2)
                criteria = [{'$or': criteria}]

            criteria.extend(self.__compose_intersect_request(flat, tlng, 'lat'))

        if zoom:
            criteria.append({'zoom': zoom})

        return None if len(criteria) < 1 else {'$and': criteria}

    def __compose_intersect_request(self, point1: float, point2: float, type_coord: str) -> List[dict]:
        request: List[dict] = []

        if type_coord == 'lat':
            request = [
                {
                    '$or': [
                        {'$and': [{'flat': {'$lte': point1}}, {'flat': {'$gte': point2}}, {'tlat': {'$lte': point2}}]},
                        {'flat': {'$gte': point1}, 'tlat': {'$lte': point2}},
                        {'flat': {'$gte': point1}, 'tlat': {'$lte': point1}},
                        {'flat': {'$lte': point1}, 'tlat': {'$gte': point2}},
                    ]
                }
            ]
        elif type_coord == 'lng':
            request = [
                {
                    '$or': [
                        {'$and': [{'flng': {'$gte': point1}}, {'flng': {'$lte': point2}}, {'tlng': {'$gte': point2}}]},
                        {'flng': {'$lte': point1}, 'tlng': {'$gte': point2}},
                        {'flng': {'$lte': point1}, 'tlng': {'$gte': point1}},
                        {'flng': {'$gte': point1}, 'tlng': {'$lte': point2}},
                    ]
                }
            ]
        return request

    def get_tile_blocks_by_filter(self, correlation_id: Optional[str], filter: FilterParams,
                                  paging: PagingParams) -> DataPage:
        # get blocks in passed coordinates
        page = self.get_page_by_filter(correlation_id, self.__compose_filter(filter), paging, None, None)

        return page

    def update_tile_blocks(self, correlation_id: Optional[str], updates: List[FireMapTileBlockV1]):
        if updates is None:
            return

        operations = []

        for update in updates:
            update_item = self._convert_from_public(update)
            operation = pymongo.operations.UpdateOne({'_id': update_item['_id']}, {'$set': update_item}, upsert=True)
            operations.append(operation)

        result = self._collection.bulk_write(operations)

        if len(result.bulk_api_result['writeErrors']) == 0 and len(result.bulk_api_result['writeConcernErrors']) == 0:
            self._logger.trace(correlation_id, "Updated %s firemap blocks %s", self._collection_name, len(operations))
        else:
            self._logger.trace(correlation_id, "Updating %s firemap failed %s", self._collection_name, len(operations))

    def _convert_from_public(self, value: FireMapTileBlockV1) -> dict:
        decimal_keys = ['flng', 'flat', 'tlng', 'tlat']

        converted = super()._convert_from_public(value)

        for id in value.tiles.keys():
            tiles = super()._convert_from_public(value.tiles[id])

            # convert coordinates to mongo decimals
            for key in decimal_keys:
                tiles[key] = Decimal128(str(tiles[key]))

            converted['tiles'][id] = tiles

        for key in decimal_keys:
            converted[key] = Decimal128(str(converted[key]))

        return converted

    def _convert_to_public(self, value: dict) -> FireMapTileBlockV1:
        decimal_keys = ['flng', 'flat', 'tlng', 'tlat']

        for key in decimal_keys:
            value[key] = float(str(value[key]))

        converted = super()._convert_to_public(value)

        for id in value['tiles'].keys():
            # convert coordinates from mongo decimals
            for key in decimal_keys:
                value['tiles'][id][key] = float(str(value['tiles'][id][key]))

            converted.tiles[id] = super()._convert_to_public(value['tiles'][id])

        return converted
