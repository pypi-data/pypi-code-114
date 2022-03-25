from __future__ import annotations

from typing import Optional, Union

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope import Scope
from ._agg import agg
from ._utils import (
    BASIC_ARGS_DOC,
    BASIC_DOC,
    ColumnOrOperation,
    MeasureOrMeasureConvertible,
)


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="sum of the square",
    example="""
        >>> m["Other.SQUARE_SUM"] = tt.agg.square_sum(table["Other"])
        >>> cube.query(m["Other.SQUARE_SUM"])
          Other.SQUARE_SUM
        0                9""".replace(
        "\n", "", 1
    ),
)
def square_sum(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="SQ_SUM", operand=operand, scope=scope)
