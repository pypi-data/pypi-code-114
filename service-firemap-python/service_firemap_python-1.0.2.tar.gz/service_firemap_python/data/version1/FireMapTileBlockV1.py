# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Dict

from . import FireMapTileV1


@dataclass
class FireMapTileBlockV1:
    id: str  # Rounder center lng_lat_zoom
    zoom: int  # Zoom level
    flng: float  # From longitude
    flat: float  # From latitude
    tlng: float  # To longitude
    tlat: float  # To latitude

    tiles: Dict[str, FireMapTileV1]  # Map tiles
