from __future__ import annotations

from typing import Optional, Union

from atoti_core import doc

from .._docs_utils import STD_AND_VAR_DOC, STD_DOC_KWARGS
from .._runtime_type_checking_utils import VarianceMode
from ..math import sqrt
from ..measure_description import MeasureDescription
from ..scope import Scope
from ._utils import (
    QUANTILE_STD_AND_VAR_DOC_KWARGS,
    SCOPE_DOC,
    ColumnOrOperation,
    MeasureOrMeasureConvertible,
)
from .var import var


@doc(
    STD_AND_VAR_DOC,
    SCOPE_DOC,
    **{**STD_DOC_KWARGS, **QUANTILE_STD_AND_VAR_DOC_KWARGS},
)
def std(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    mode: VarianceMode = "sample",
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    return sqrt(var(operand, mode=mode, scope=scope))
