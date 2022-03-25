from __future__ import annotations

from typing import Optional, Union

from ...agg._agg import agg
from ...agg._utils import ColumnOrOperation, MeasureOrMeasureConvertible
from ...measure_description import MeasureDescription
from ...scope import Scope


def distinct(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return an array measure representing the distinct values of the passed measure."""
    return agg("DISTINCT", operand=operand, scope=scope)
