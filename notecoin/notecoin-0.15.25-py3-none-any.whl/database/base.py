import logging
import os

from notetool.secret import read_secret
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker


class BaseTable(object):
    def json(self):
        res = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return res


uri = read_secret(cate1='notecoin', cate2='dataset', cate3='db_path')
uri = uri or f'sqlite:///{os.path.abspath(os.path.dirname(__file__))}/data/notecoin.db'
#engine = create_engine(uri, echo=True)
engine = create_engine(uri)
Base = declarative_base()
session = scoped_session(sessionmaker(
    autocommit=True,
    # autoflush=True,
    bind=engine))


logging.info(f'uri:{uri}')


def create_all():
    Base.metadata.create_all(engine)
    session.commit()
