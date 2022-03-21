#-*- coding: utf-8 -*-

import os
import sys
from copy import deepcopy

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import logging
from tisdb.config import TsdbConfig
from tisdb.client2 import MetricdbClient
from tisdb.client import TsdbClient
from tisdb.types import StoreType

logger = logging.getLogger("tisdb")


def make_db_params(key):
    params = {}
    env_vars = [
        (part, f"TISDB_{key}_{part.upper()}")
        for part in ("host", "port", "user", "password")
    ]

    for param, env_var in env_vars:
        if value := os.environ.get(env_var):
            params[param] = int(value) if param == "port" else value
    return params


PORM_PARAMS = make_db_params("PORM")


def db_loader(engine: str, client: str = 'TSDB', **params):
    db_params = deepcopy(PORM_PARAMS)
    db_params.update(params)
    Clazz = TsdbClient if client.upper() == 'TSDB' else MetricdbClient
    return Clazz(
        store_type=StoreType[engine.upper()], conn_conf=TsdbConfig(**db_params)
    )


class QueryLogHandler(logging.Handler):
    def __init__(self, *args, **kwargs):
        self.queries = []
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        self.queries.append(record)
