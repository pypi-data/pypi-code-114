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
    value="sum of the positive values",
    example="""
        >>> m["Quantity.LONG"] = tt.agg.long(table["Quantity"])
        >>> cube.query(m["Quantity.LONG"])
          Quantity.LONG
        0         1,110""".replace(
        "\n", "", 1
    ),
)
def long(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="LONG", operand=operand, scope=scope)
