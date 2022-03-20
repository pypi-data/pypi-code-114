# -*- coding: utf-8

from enum import Enum


class OpType(Enum):
    INSERT_IGNORE = 1
    UPSERT = 2
    INSERT_ON_DUPLICATE_KEY_UPDATE = 3


class StoreType(Enum):
    PORM = 1
    MYSQL = 2
    TIDB = 3
