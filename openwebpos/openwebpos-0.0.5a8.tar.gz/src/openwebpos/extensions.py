from flask_sqlalchemy import Model, SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declared_attr, has_inherited_table
from flask_migrate import Migrate


class CustomModel(Model):
    @declared_attr
    def id(cls):
        for base in cls.__mro__[1:-1]:
            if getattr(base, '__table__', None) is not None:
                col_type = sa.ForeignKey(base.id)
                break
        else:
            col_type = sa.Integer
        return sa.Column(col_type, primary_key=True)


db = SQLAlchemy(model_class=CustomModel)
migrate = Migrate()
