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
    value="sum",
    example="""
        >>> m["Quantity.SUM"] = tt.agg.sum(table["Quantity"])
        >>> cube.query(m["Quantity.SUM"])
          Quantity.SUM
        0        1,110""".replace(
        "\n", "", 1
    ),
)
def sum(  # pylint: disable=redefined-builtin
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="SUM", operand=operand, scope=scope)
