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
    value="distinct count",
    example="""
        >>> m["Price.DISTINCT_COUNT"] = tt.agg.count_distinct(table["Price"])
        >>> cube.query(m["Price.DISTINCT_COUNT"])
          Price.DISTINCT_COUNT
        0                    3""".replace(
        "\n", "", 1
    ),
)
def count_distinct(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="DISTINCT_COUNT", operand=operand, scope=scope)
