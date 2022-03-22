from typing import Any, TypeVar, Union

from sqlalchemy.orm import InstrumentedAttribute
from sqlalchemy.sql.elements import UnaryExpression

__all__ = [
    'ResponseType',
    'OrderByType',
]

ResponseType = TypeVar('ResponseType', bound=Any)
OrderByType = Union[UnaryExpression, InstrumentedAttribute]
