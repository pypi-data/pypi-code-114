from __future__ import annotations

from typing import Optional, Union

from ..measure_description import MeasureDescription
from ..scope import Scope
from ._agg import agg
from ._utils import ColumnOrOperation, MeasureOrMeasureConvertible


def count(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    """Return a measure equal to the number of aggregated elements.

    With a table column, it counts the number of facts.
    With a measure and a level, it counts the number of level members.
    To count the number of distinct elements, use :func:`atoti.agg.count_distinct`.
    """
    return agg(agg_fun="COUNT", operand=operand, scope=scope)
