from dataclasses import dataclass
from typing import Optional

from .._java_api import JavaApi
from .._py4j_utils import as_java_object
from ..measure_description import LiteralMeasureValue, MeasureDescription


@dataclass(eq=False)
class LiteralMeasure(MeasureDescription):  # pylint: disable=keyword-only-dataclass
    """A measure equal to a literal value."""

    _value: LiteralMeasureValue

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        val = as_java_object(self._value, gateway=java_api.gateway)
        distilled_name = java_api.create_measure(
            cube_name, measure_name, "LITERAL", val
        )
        return distilled_name
