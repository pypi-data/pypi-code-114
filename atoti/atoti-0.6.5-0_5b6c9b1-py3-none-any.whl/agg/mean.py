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
    value="mean",
    example="""
        >>> m["Quantity.MEAN"] = tt.agg.mean(table["Quantity"])
        >>> cube.query(m["Quantity.MEAN"])
          Quantity.MEAN
        0        370.00""".replace(
        "\n", "", 1
    ),
)
def mean(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="MEAN", operand=operand, scope=scope)
