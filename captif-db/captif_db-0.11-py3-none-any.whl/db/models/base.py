from decimal import Decimal
from sqlalchemy.inspection import inspect
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm.properties import ColumnProperty
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import MetaData

from captif_db.helpers.models import query_to_frame


naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


metadata = MetaData(naming_convention=naming_convention)
Base = declarative_base(metadata=metadata)


class Table:
    """
    Used to provide some additional functionality to ORM models.

    """

    __index_column__ = None

    @classmethod
    def read_table(cls, db_session, include_hybrid=False):
        """
        Load the entire database table into a DataFrame. Provide a SQLalchemy session
        object.
        """
        return query_to_frame(
            db_session.query(cls), cls.__index_column__, include_hybrid
        )

    @classmethod
    def fields(cls, include_hybrid=False):
        if include_hybrid:
            return cls.properties() + cls.hybrid_properties()
        return cls.properties()

    @classmethod
    def properties(cls):
        return [
            pp.key for pp in inspect(cls).all_orm_descriptors if cls.is_property(pp)
        ]

    @staticmethod
    def is_property(orm_descriptor):
        try:
            return isinstance(orm_descriptor.prop, ColumnProperty)
        except AttributeError:
            return False

    @classmethod
    def hybrid_properties(cls):
        return [
            pp.__name__
            for pp in inspect(cls).all_orm_descriptors
            if isinstance(pp, hybrid_property)
        ]

    @staticmethod
    def _to_list(s):
        return [s] if isinstance(s, str) else list(s)

    def as_dict(self, include_hybrid=False):
        dd = {}
        for kk in self.fields(include_hybrid=include_hybrid):
            vv = getattr(self, kk)
            if isinstance(vv, Decimal):
                vv = float(vv)
            dd[kk] = vv
        return dd

    def equivalent(self, obj):
        return self.as_dict() == obj.as_dict()
