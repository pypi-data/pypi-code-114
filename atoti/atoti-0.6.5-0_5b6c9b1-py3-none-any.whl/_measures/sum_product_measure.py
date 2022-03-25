from dataclasses import dataclass
from typing import Collection, Iterable, Optional

from atoti_core import is_array_type

from .._java_api import JavaApi
from ..column import Column
from ..function import value
from ..measure_description import MeasureDescription
from .calculated_measure import AggregatedMeasure
from .utils import get_measure_name


@dataclass(eq=False)
class SumProductFieldsMeasure(
    MeasureDescription
):  # pylint: disable=keyword-only-dataclass
    """Sum of the product of factors for table fields."""

    _factors: Collection[Column]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        # Checks fields are in the selection, otherwise use the other sum product implementation because UDAF needs
        # fields in the selection.
        selection_fields = java_api.get_selection_fields(cube_name)
        if all(factor.name in selection_fields for factor in self._factors):
            factors_and_type = {}
            for factor in self._factors:
                if (
                    is_array_type(factor.data_type.java_type)
                    and factor.data_type.java_type != "double[]"
                ):
                    raise TypeError(
                        f"Unsupported operation. Only array columns of type double[] are supported and {factor} is not."
                    )
                factors_and_type[factor.name] = factor.data_type.java_type
            return java_api.create_measure(
                cube_name,
                measure_name,
                "SUM_PRODUCT_UDAF",
                [factor.name for factor in self._factors],
                factors_and_type,
            )
        return AggregatedMeasure(
            _underlying_measure=SumProductEncapsulationMeasure(
                [value(factor) for factor in self._factors]
            ),
            _agg_fun="SUM_PRODUCT",
            _on_levels=None,
        )._do_distil(java_api=java_api, cube_name=cube_name, measure_name=measure_name)


@dataclass(eq=False)
class SumProductEncapsulationMeasure(
    MeasureDescription
):  # pylint: disable=keyword-only-dataclass
    """Create an intermediate measure needing to be aggregated with the key "SUM_PRODUCT"."""

    _factors: Iterable[MeasureDescription]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:

        return java_api.create_measure(
            cube_name,
            measure_name,
            "SUM_PRODUCT_ENCAPSULATION",
            [
                get_measure_name(java_api=java_api, measure=factor, cube_name=cube_name)
                for factor in self._factors
            ],
        )
