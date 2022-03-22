# -*- coding: utf-8 -*-
from typing import List, Optional

from pip_services3_commons.data import FilterParams, PagingParams, DataPage
from pip_services3_components.log import LogLevel
from pip_services3_data.persistence import IdentifiableMemoryPersistence

from .IFireMapPersistence import IFireMapPersistence
from ..data.version1 import FireMapTileBlockV1, FireMapTileV1
from ..data.version1 import LocationV1


class FireMapMemoryPersistence(IdentifiableMemoryPersistence, IFireMapPersistence):

    def __init__(self):
        super().__init__()

        self._items: List[FireMapTileBlockV1] = []

    def __compose_filter(self, filter: FilterParams):
        filter = filter or FilterParams()
        locations = []

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

        # get blocks for coordinates
        if coordinates:
            for location in coordinates:
                lat, long = location.split(';')
                locations.append(LocationV1(float(lat), float(long)))

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

        def inner(item: FireMapTileV1) -> bool:
            # if item inside flng, flat, tlng, tlat coordinates
            not_in_range = lambda x1, x2, of, to: (of is not None and to is not None) and not (
                    to >= x1 >= of or to >= x2 >= of)

            if not_in_range(item.flng, item.tlng, flng, tlng) and (
                    (flng2 is None and tlng2 is None) or not_in_range(item.flng, item.tlng, flng2, tlng2)):
                return False
            if not_in_range(item.flat, item.tlat, flat, tlat):
                return False
            if zoom is not None and zoom != item.zoom:
                return False

            if locations:
                for location in locations:
                    if item.flng <= location.long <= item.tlng and item.flat >= location.lat >= item.tlat:
                        return True
                return False

            return True

        return inner

    def get_tile_blocks_by_filter(self, correlation_id: Optional[str], filter: FilterParams,
                                  paging: PagingParams) -> DataPage:
        # get blocks in passed coordinates
        page = self.get_page_by_filter(correlation_id, self.__compose_filter(filter), paging, None, None)

        return page

    def update_tile_blocks(self, correlation_id: Optional[str], updates: List[FireMapTileBlockV1]):
        if updates is None:
            return

        # hack to disable logging in the set method. to avoid console overflow
        _log_lvl = self._logger.get_level()
        try:
            self._logger.set_level(LogLevel.Nothing)
            for update in updates:
                self.set(correlation_id, update)
        finally:
            self._logger.set_level(_log_lvl)

        self._logger.trace(correlation_id, "Updated %s firemap blocks", len(updates))
