# -*- coding: utf-8 -*- 
# Time: 2022-03-01 11:02
# Copyright (c) 2022
# author: Euraxluo

import redis
import requests
from typing import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta, sessionmaker
from contextlib import contextmanager
from concurrent.futures import ThreadPoolExecutor


class Register:
    """
    注册服务
    """
    _amap_web_api_keys = []  # 高德地图WebApiKey列表
    _session = None
    _pool: ThreadPoolExecutor = None
    _logger = None
    _osrm_host = None
    _redis = None
    _persistence_uri = None
    _orm_engine = None
    _orm_session = None
    _orm_base = None
    _geohashing_keys = 'distance_matrix:geohashing_keys'

    @classmethod
    def setup(cls, keys: List[str], logger, pool_size: int = 2,
              osrm_host: str = None,
              conn: redis.Redis = None,
              persistence_uri: str = None,
              database: str = None,
              database_log: bool = False,
              geohashing_keys: str = "distance_matrix:geohashing_keys"):
        """

        :param database_log: 数据库操作sql日志
        :param keys:
        :param logger:
        :param pool_size: 该服务维护的线程池大小,默认为 2
        :param osrm_host:
        :param conn: redis connection
        :param persistence_uri: mysql_pymysql://username:password@host:port
        :param database: database_name
        :param geohashing_keys: geohashing_keys,to storage all cache edges in redis sortedset
        :return:
        """
        cls._amap_web_api_keys = keys
        cls._logger = logger
        cls._osrm_host = osrm_host
        cls._geohashing_keys = geohashing_keys
        cls._redis = conn
        cls._database = database
        cls._pool = ThreadPoolExecutor(max_workers=pool_size)
        if persistence_uri is not None:
            cls._persistence_uri = persistence_uri
            cls.setup_orm(database_log)

    @classmethod
    def setup_orm(cls, database_log: bool = False):
        cls._orm_engine = create_engine(cls._persistence_uri, echo=database_log)
        cls.create_persistence_database()
        cls._orm_session = sessionmaker(autocommit=False, autoflush=False, bind=cls._orm_engine)
        cls._orm_base: DeclarativeMeta = declarative_base()

    @classmethod
    def create_persistence_database(cls):
        create_str = f"CREATE DATABASE IF NOT EXISTS {cls._database} ;"
        cls._orm_engine.execute(create_str)
        cls._orm_engine.execute(f"USE {cls._database};")
        cls._orm_engine.execute(f"show tables;")

    @classmethod
    def session(cls, pool_connections=3, pool_maxsize=3, max_retries=3):
        if cls._session:
            return cls._session
        cls._session = requests.Session()
        cls._adapter = requests.adapters.HTTPAdapter(pool_connections=pool_connections, pool_maxsize=pool_maxsize,
                                                     max_retries=max_retries)
        cls._session.mount('http://', cls._adapter)
        cls._session.mount('https://', cls._adapter)
        return cls._session

    @property
    def keys(self) -> list:
        return Register._amap_web_api_keys

    @property
    def logger(self):
        return Register._logger

    @property
    def redis(self) -> redis.Redis:
        return Register._redis

    @property
    def osrm_host(self) -> str:
        return Register._osrm_host

    @property
    def persistence_uri(self) -> str:
        return Register._persistence_uri

    @property
    def orm_base(self) -> DeclarativeMeta:
        return Register._orm_base

    @property
    def orm_engine(self):
        return Register._orm_engine

    @contextmanager
    def orm(self):
        db = Register._orm_session()
        yield db
        db.close()

    @property
    def geohashing_keys(self):
        return Register._geohashing_keys

    @property
    def pool(self):
        return Register._pool

    @classmethod
    def shutdown(cls):
        cls._pool.shutdown()  # 关闭自己申请的线程池
        cls._orm_engine.dispose()  # 关闭自己创建的数据的全部链接
        # 不必关闭redis链接,因为不是我们创建的


register = Register()

__all__ = ["register"]
