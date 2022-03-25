from __future__ import annotations

from typing import Optional, Union

from atoti_core import doc

from .._docs_utils import STD_AND_VAR_DOC, VAR_DOC_KWARGS
from .._runtime_type_checking_utils import VarianceMode
from ..measure_description import MeasureDescription
from ..scope import Scope
from ._count import count
from ._utils import (
    QUANTILE_STD_AND_VAR_DOC_KWARGS,
    SCOPE_DOC,
    ColumnOrOperation,
    MeasureOrMeasureConvertible,
)
from .mean import mean
from .square_sum import square_sum


@doc(
    STD_AND_VAR_DOC,
    SCOPE_DOC,
    **{**VAR_DOC_KWARGS, **QUANTILE_STD_AND_VAR_DOC_KWARGS},
)
def var(
    operand: Union[ColumnOrOperation, MeasureOrMeasureConvertible],
    *,
    mode: VarianceMode = "sample",
    scope: Optional[Scope] = None,
) -> MeasureDescription:
    size = count(operand, scope=scope)
    mean_value = mean(operand, scope=scope)
    population_var = square_sum(operand, scope=scope) / size - mean_value * mean_value
    if mode == "population":
        return population_var
    # Apply Bessel's correction
    return population_var * size / (size - 1)
