from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Union

from atoti_core import coordinates_to_java_description, keyword_only_dataclass

from .._java_api import JavaApi
from ..measure_description import MeasureDescription
from ..scope._utils import LeafLevels
from .utils import convert_measure_args

Operand = Union[MeasureDescription, str]


@dataclass(frozen=True)
class Operator:  # pylint: disable=keyword-only-dataclass
    """An operator to create a calculated measure from other measures."""

    _name: str
    _operands: Sequence[Operand]

    @staticmethod
    def mul(operands: Sequence[MeasureDescription]) -> Operator:
        """Multiplication operator."""
        return Operator(_name="mul", _operands=operands)

    @staticmethod
    def truediv(operands: Sequence[MeasureDescription]) -> Operator:
        """Division operator."""
        return Operator(_name="truediv", _operands=operands)

    @staticmethod
    def floordiv(operands: Sequence[MeasureDescription]) -> Operator:
        """Division operator."""
        return Operator(_name="floordiv", _operands=operands)

    @staticmethod
    def add(operands: Sequence[MeasureDescription]) -> Operator:
        """Addition operator."""
        return Operator(_name="add", _operands=operands)

    @staticmethod
    def sub(operands: Sequence[MeasureDescription]) -> Operator:
        """Subtraction operator."""
        return Operator(_name="sub", _operands=operands)

    @staticmethod
    def neg(operand: MeasureDescription) -> Operator:
        """Neg operator."""
        return Operator(_name="neg", _operands=[operand])

    @staticmethod
    def mod(operands: Sequence[MeasureDescription]) -> Operator:
        """Modulo operator."""
        return Operator(_name="mod", _operands=operands)


@dataclass(eq=False)
class CalculatedMeasure(MeasureDescription):  # pylint: disable=keyword-only-dataclass
    """A calculated measure is the result of an operation between other measures."""

    _operator: Operator

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        return java_api.create_measure(
            cube_name,
            measure_name,
            "CALCULATED",
            self._operator._name,
            convert_measure_args(
                java_api=java_api,
                cube_name=cube_name,
                args=self._operator._operands,
            ),
        )


@keyword_only_dataclass
@dataclass(eq=False)
class AggregatedMeasure(MeasureDescription):
    """Aggregated Measure."""

    _underlying_measure: MeasureDescription
    _agg_fun: str
    _on_levels: Optional[LeafLevels]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = self._underlying_measure._distil(
            java_api=java_api, cube_name=cube_name
        )

        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "LEAF_AGGREGATION",
            underlying_name,
            [
                coordinates_to_java_description(level_coordinates)
                for level_coordinates in (
                    self._on_levels.levels_coordinates if self._on_levels else []
                )
            ],
            self._agg_fun,
        )
        return distilled_name
