from typing import Any
from ..domain.value_obj import Result


try:
    from sqlalchemy.ext.declarative import declarative_base
    SQLALCHEMY_ENV = True
except:
    SQLALCHEMY_ENV = False

if SQLALCHEMY_ENV:
    SqlalchemyBase = declarative_base()

class BaseDO:
    def to_json(self):
        return vars(self)

    def from_json(self):
        raise NotImplementedError

