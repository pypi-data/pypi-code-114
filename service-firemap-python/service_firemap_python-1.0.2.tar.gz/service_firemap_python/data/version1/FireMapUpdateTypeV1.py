# -*- coding: utf-8 -*-

from enum import Enum


class FireMapUpdateTypeV1(str, Enum):
    CLEAR = 'clear'
    SMOKE = 'smoke'
    FIRE = 'fire'
