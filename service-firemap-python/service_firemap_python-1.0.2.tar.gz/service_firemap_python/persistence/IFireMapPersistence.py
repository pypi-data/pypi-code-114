# -*- coding: utf-8 -*-
from abc import ABC
from typing import Optional, List

from pip_services3_commons.data import PagingParams, FilterParams, DataPage

from ..data.version1.FireMapTileBlockV1 import FireMapTileBlockV1


class IFireMapPersistence(ABC):
    def get_tile_blocks_by_filter(self, correlation_id: Optional[str], filter: FilterParams, paging: PagingParams) -> DataPage:
        pass

    def update_tile_blocks(self, correlation_id: Optional[str], updates: List[FireMapTileBlockV1]):
        pass

