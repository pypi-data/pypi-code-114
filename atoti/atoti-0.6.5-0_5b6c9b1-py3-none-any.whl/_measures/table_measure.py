from dataclasses import dataclass
from typing import Iterable, Optional

from atoti_core import keyword_only_dataclass

from .._java_api import JavaApi
from ..level import Level
from ..measure_description import MeasureDescription
from ..type import DataType


@keyword_only_dataclass
@dataclass(eq=False)
class TableMeasure(MeasureDescription):
    """Measure based on the column of a table."""

    _column_name: str
    _agg_fun: str
    _table_name: str

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        return java_api.aggregated_measure(
            cube_name=cube_name,
            measure_name=measure_name,
            table_name=self._table_name,
            column_name=self._column_name,
            agg_function=self._agg_fun,
            required_levels_coordinates=[],
        )


@keyword_only_dataclass
@dataclass(eq=False)
class SingleValueTableMeasure(MeasureDescription):
    """Single value aggregated measure based on the column of a table."""

    _column_name: str
    _table_name: str
    _column_data_type: DataType
    _levels: Optional[Iterable[Level]] = None

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        # levels = [] if self._levels is None else self._levels

        distilled_name = java_api.value_measure(
            cube_name=cube_name,
            measure_name=measure_name,
            table_name=self._table_name,
            column_name=self._column_name,
            column_type=self._column_data_type,
            required_levels_coordinates=[level._coordinates for level in self._levels]
            if self._levels is not None
            else None,
        )

        return distilled_name
