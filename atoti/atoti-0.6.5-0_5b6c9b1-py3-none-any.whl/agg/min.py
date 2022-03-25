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
    value="minimum",
    example="""
        >>> m["Minimum Price"] = tt.agg.min(table["Price"])
        >>> cube.query(m["Minimum Price"])
          Minimum Price
        0         12.50""".replace(
        "\n", "", 1
    ),
)
def min(  # pylint: disable=redefined-builtin
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="MIN", operand=operand, scope=scope)
