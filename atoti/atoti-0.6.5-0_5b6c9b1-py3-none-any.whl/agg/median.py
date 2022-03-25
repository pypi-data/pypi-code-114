from __future__ import annotations

from typing import Optional, Union

from atoti_core import doc

from ..measure_description import MeasureDescription
from ..scope import Scope
from ._utils import (
    BASIC_ARGS_DOC,
    BASIC_DOC,
    ColumnOrOperation,
    MeasureOrMeasureConvertible,
)
from .quantile import quantile


@doc(
    BASIC_DOC,
    args=BASIC_ARGS_DOC,
    value="median",
    example="""
        >>> m["Median Price"] = tt.agg.median(table["Price"])
        >>> cube.query(m["Median Price"])
          Median Price
        0        25.90""".replace(
        "\n", "", 1
    ),
)
def median(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return quantile(operand, q=0.5, scope=scope)
