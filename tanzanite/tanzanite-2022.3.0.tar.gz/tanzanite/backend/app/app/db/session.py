# -*- coding: utf-8 -*-

"""
Database session resources.
"""

# Standard imports
import databases

# External imports
import sqlalchemy
from sqlalchemy.ext.declarative import (
    DeclarativeMeta,
    declarative_base,
)
from sqlalchemy.orm import sessionmaker

# Local imports
from tanzanite.core.config import settings


URI = settings.SQLALCHEMY_DATABASE_URI
database = databases.Database(URI)
Base: DeclarativeMeta = declarative_base()


# Using sqlite3 for testing and simple deployments, and postgresql for
# production deployments.
#
# Note that sqlite3 databases that have tables where the primary key is an
# autoincrementing integer do not behave the same as some other databases, in
# that the id values may be reused. This hapens when you delete the record
# with the highest id value (N) and then create a new record, which will
# have its id autoincremented from the N-1 value, reusing the id value N.


SUPPORTED_DIALECTS = ['sqlite', 'postgres']
DIALECT = settings.SQLALCHEMY_DATABASE_DIALECT
if DIALECT not in SUPPORTED_DIALECTS:
    DIALECTS = ','.join([f'{i}' for i in SUPPORTED_DIALECTS])
    raise RuntimeError(
        f"[-] DIALECT '{DIALECT}' not supported: "
        f"only [{DIALECTS}]"
    )
if DIALECT == 'sqlite':
    engine = sqlalchemy.create_engine(
        URI,
        connect_args={'check_same_thread': False},
        # min_size=2,
        # max_size=10,
    )
else:
    engine = sqlalchemy.create_engine(
        URI,
        pool_pre_ping=True,
    )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_engine():
    """
    Return the sqlalchemy engine.
    """
    return engine


# vim: set fileencoding=utf-8 ts=4 sw=4 tw=0 et :
