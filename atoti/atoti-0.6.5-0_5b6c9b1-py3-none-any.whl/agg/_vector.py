from __future__ import annotations

from typing import Optional, Union

from ..measure_description import MeasureDescription
from ..scope import Scope
from ._agg import agg
from ._utils import ColumnOrOperation, MeasureOrMeasureConvertible


def vector(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return an array measure representing the values of the passed operand across the specified scope."""
    return agg(agg_fun="VECTOR", operand=operand, scope=scope)
