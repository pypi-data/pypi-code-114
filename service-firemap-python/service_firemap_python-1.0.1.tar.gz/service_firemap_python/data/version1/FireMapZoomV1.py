# -*- coding: utf-8 -*-
from enum import IntEnum


class FireMapZoomV1(IntEnum):
    """
    Each zoom level determines a resolution grid
    """
    Zoom50m = 0
    Zoom1km = 1
    Zoom20km = 2
    Zoom50km = 3
    Zoom100km = 4