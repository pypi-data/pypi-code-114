# -*- coding: utf-8 -*-

from abc import ABC
from typing import Optional, List

from service_firemap_python.data.version1.FireMapTileV1 import FireMapTileV1


class IFireMapListenerV1(ABC):

    def map_updated(self, correlation_id: Optional[str], zoom: int, tiles: List[FireMapTileV1]):
        pass
