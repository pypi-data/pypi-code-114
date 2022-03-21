# -*- coding: utf-8

from porm.model import DBModel
from porm.types.core import (
    DatetimeType,
    FloatType,
    IntegerType,
    VarcharType,
)
import pymysql

from tisdb.config import TsdbConfig

__all__ = (
    "Mtsv",
    "Tkv",
    "TkvUkRel",
)

TSDB_CONFIG = TsdbConfig(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    db="icuser",
    charset="utf8",
    autocommit=0,
    cursorclass=pymysql.cursors.DictCursor,
)


class TsdbModel(DBModel):
    __DATABASE__ = TSDB_CONFIG["db"]
    __CONFIG__ = TSDB_CONFIG


class Mtsv(TsdbModel):
    zzid = IntegerType(pk=True, required=False)
    metric = VarcharType(required=True)
    taguk = VarcharType(required=True)
    ts = DatetimeType(required=True, format="%Y-%m-%d'T'%H:%M:%S.SSSZ")
    value = FloatType(required=True)


class Tkv(TsdbModel):
    zzid = IntegerType(pk=True, required=False)
    tagk = VarcharType(required=True)
    tagv = VarcharType(required=True)


class TkvUkRel(TsdbModel):
    tkv_pk = IntegerType(pk=True, required=False)
    taguk = VarcharType(required=True)


class Metric(TsdbModel):
    bid = VarcharType(required=False)
    metric = VarcharType(required=True)
    taguk = VarcharType(required=True)
    ts = DatetimeType(required=True)
    createtime = DatetimeType(required=False)
    updatetime = DatetimeType(required=False)
    fieldk = VarcharType(required=True)
    fieldv = VarcharType(required=True)


class Tag(TsdbModel):
    tagid = VarcharType(require=True)
    tagk = VarcharType(required=True)
    tagv = VarcharType(required=True)
    createtime = DatetimeType(required=True)
    updatetime = DatetimeType(required=True)


class Tag_Rel(TsdbModel):
    tagid = VarcharType(require=True)
    taguk = VarcharType(required=True)
    createtime = DatetimeType(required=True)
    updatetime = DatetimeType(required=True)
