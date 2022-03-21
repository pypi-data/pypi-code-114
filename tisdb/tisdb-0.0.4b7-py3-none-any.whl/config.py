# -*- coding: utf-8

from __future__ import annotations
from sortedcontainers.sorteddict import SortedDict
from pymysql.cursors import DictCursor


class TsdbConfig(SortedDict):
    """Tsdb client config

    Args:
        host (str): connection host
        port (int): port
        user (str): auth user
        password (str): auth password
        db (str): tsdb namespace
        charset (str): conn charset
        autocommit (int): auto commit or not. Defaults to 0 means no
    """

    def __init__(
        self,
        host: str = "localhost",
        port: int = 3306,
        user: str = "root",
        password: str = "root",
        db: str = "icuser",
        charset: str = "utf8",
        autocommit: int = 0,
        cursorclass=DictCursor,
        database: str = None
    ):
        super().__init__(
            host=host,
            user=user,
            password=password,
            port=port,
            db=db or database,
            charset=charset,
            autocommit=autocommit,
            cursorclass=cursorclass,
        )
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db or database

    def copy(self) -> TsdbConfig:
        tmp = SortedDict()
        tmp.update(self)
        return TsdbConfig(**tmp)
