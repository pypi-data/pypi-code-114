# -*- coding: utf-8 -*-
from abc import ABC
from typing import Optional, List

from ..data.version1 import LocationV1, FireMapTileV1, FireMapUpdateV1
from ..logic import IFireMapListenerV1


class IFireMapController(ABC):
    def get_tiles(self, correlation_id: Optional[str], of: LocationV1, to: LocationV1, zoom: Optional[int]) -> List[FireMapTileV1]:
        pass

    def update_tiles(self, correlation_id: Optional[str], updates: List[FireMapUpdateV1]):
        pass
