from dataclasses import dataclass
from typing import Any, Optional

from atoti_core import (
    BaseLevel,
    HierarchyCoordinates,
    ReprJson,
    deprecated,
    keyword_only_dataclass,
)
from typeguard import typeguard_ignore

from ._java_api import JavaApi
from ._level_condition import LevelCondition, _level_coordinates_to_measure_description
from ._level_isin_condition import LevelIsinCondition
from .comparator import Comparator, _comparator_to_order, _order_to_comparator
from .measure_description import MeasureConvertible, MeasureDescription
from .order import NaturalOrder, Order
from .type import DataType


@keyword_only_dataclass
@typeguard_ignore
@dataclass(eq=False)
class Level(BaseLevel, MeasureConvertible):
    """Level of a :class:`atoti.Hierarchy`.

    A level is a sub category of a hierarchy.
    Levels have a specific order with a parent-child relationship.

    In a :guilabel:`Pivot Table`, a single-level hierarchy will be displayed as a flat attribute while a multi-level hierarchy will display the first level and allow users to expand each member against the next level and display sub totals.

    For example, a :guilabel:`Geography` hierarchy can have a :guilabel:`Continent` as the top level where :guilabel:`Continent` expands to :guilabel:`Country` which in turns expands to the leaf level: :guilabel:`City`.
    """

    _column_name: str
    _data_type: DataType
    _hierarchy_coordinates: HierarchyCoordinates
    _cube_name: str
    _java_api: JavaApi
    _order: Order = NaturalOrder()

    @property
    def dimension(self) -> str:
        """Name of the dimension holding the level."""
        return self._hierarchy_coordinates[0]

    @property
    def hierarchy(self) -> str:
        """Name of the hierarchy holding the level."""
        return self._hierarchy_coordinates[1]

    @property
    def data_type(self) -> DataType:
        """Type of the level members."""
        return self._data_type

    @property
    def comparator(self) -> Comparator:
        """Deprecated, use :attr:`atoti.Level.order` instead."""
        deprecated("`Level.comparator` is deprecated, use `Level.order` instead.")
        return _order_to_comparator(self._order)

    @comparator.setter
    def comparator(self, value: Comparator) -> None:
        deprecated("`Level.comparator` is deprecated, use `Level.order` instead.")
        self.order = _comparator_to_order(value)

    @property
    def order(self) -> Order:
        """Order in which to sort the level's members.

        Defaults to ascending :class:`atoti.NaturalOrder`.
        """
        return self._order

    @order.setter
    def order(self, value: Order) -> None:
        self._java_api.update_level_order(
            value,
            cube_name=self._cube_name,
            level_coordinates=self._coordinates,
        )
        self._java_api.refresh()
        self._order = value

    def _to_measure_description(
        self, agg_fun: Optional[str] = None
    ) -> MeasureDescription:
        """Convert this column into a measure."""
        return _level_coordinates_to_measure_description(self._coordinates, agg_fun)

    def _repr_json_(self) -> ReprJson:
        data = {
            "dimension": self.dimension,
            "hierarchy": self.hierarchy,
            "type": str(self.data_type),
        }
        if self.order is not None:
            data["order"] = self.order._key
        return (data, {"expanded": True, "root": self.name})

    def isin(self, *members: Any) -> LevelIsinCondition:
        return LevelIsinCondition(level_coordinates=self._coordinates, members=members)

    def __eq__(self, other: Any) -> LevelCondition:  # type: ignore[override]
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="eq", value=other
        )

    def __ne__(self, other: Any) -> LevelCondition:  # type: ignore[override]
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="ne", value=other
        )

    def __lt__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="lt", value=other
        )

    def __le__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="le", value=other
        )

    def __gt__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="gt", value=other
        )

    def __ge__(self, other: Any) -> LevelCondition:
        if isinstance(other, MeasureDescription):
            return NotImplemented
        return LevelCondition(
            level_coordinates=self._coordinates, operator="ge", value=other
        )

    # This is needed otherwise errors like "TypeError: unhashable type: 'Level'" are thrown.
    # This is a "eq=False" dataclass so hash method is generated "according to how eq" is set but
    # the desired behavior is to use BitwiseOperatorsOnly.__hash__().
    def __hash__(self) -> int:
        return hash(self._coordinates)
