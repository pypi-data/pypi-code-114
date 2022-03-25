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
    value="product",
    example="""
        >>> m["Other.PROD"] = tt.agg.prod(table["Other"])
        >>> cube.query(m["Other.PROD"])
          Other.PROD
        0          4""".replace(
        "\n", "", 1
    ),
)
def prod(  # pylint: disable=redefined-builtin
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return agg(agg_fun="MULTIPLY", operand=operand, scope=scope)
