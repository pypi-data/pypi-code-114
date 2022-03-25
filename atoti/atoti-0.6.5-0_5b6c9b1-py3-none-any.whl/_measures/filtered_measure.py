from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Collection, Dict, List, Optional

from atoti_core import (
    JavaType,
    coordinates_to_java_description,
    is_boolean_type,
    is_numeric_type,
    is_primitive_type,
    keyword_only_dataclass,
)

from .._condition import Condition
from .._data_type_error import DataTypeError
from .._hierarchy_isin_condition import HierarchyIsinCondition
from .._java_api import JavaApi
from .._level_condition import LevelCondition
from .._level_isin_condition import LevelIsinCondition
from .._py4j_utils import as_java_object, to_java_object_list
from ..measure_description import MeasureDescription
from ..type import DataType


def is_object_type(java_type: JavaType) -> bool:
    return not is_primitive_type(java_type)


TYPE_TO_PREDICATE: Dict[str, Callable[[JavaType], bool]] = {
    "numeric": is_numeric_type,
    "boolean": is_boolean_type,
    "object": is_object_type,
}


@keyword_only_dataclass
@dataclass(eq=False)
class WhereMeasure(MeasureDescription):
    """A measure that returns the value of other measures based on conditions."""

    _true_measure: MeasureDescription
    _false_measure: Optional[MeasureDescription]
    _conditions: Collection[MeasureDescription]

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        underlying_name = self._true_measure._distil(
            java_api=java_api, cube_name=cube_name, measure_name=None
        )
        underlying_else_name = (
            self._false_measure._distil(java_api=java_api, cube_name=cube_name)
            if self._false_measure is not None
            else None
        )
        if underlying_else_name is not None:
            java_api.publish_measures(cube_name)
            self._validate_type_compatibility(
                true_value_type=java_api.get_measure(
                    cube_name, underlying_name
                ).underlying_type,
                false_value_type=java_api.get_measure(
                    cube_name, underlying_else_name
                ).underlying_type,
            )

        conditions_names = [
            condition._distil(java_api=java_api, cube_name=cube_name)
            for condition in self._conditions
        ]
        distilled_name = java_api.create_measure(
            cube_name,
            measure_name,
            "WHERE",
            underlying_name,
            underlying_else_name,
            conditions_names,
        )
        return distilled_name

    def _validate_type_compatibility(
        self, true_value_type: DataType, false_value_type: DataType
    ) -> None:
        """Ensures that a where measure that does define a *_false_measure* selects a measure that is compatible type-wise.

        Two types are compatible if they both have the same type among the following: numeric, boolean or object.
        """
        for data_type_to_validate, func in TYPE_TO_PREDICATE.items():
            if func(true_value_type.java_type) and not func(false_value_type.java_type):
                raise DataTypeError(
                    "Trying to filter measure: "
                    + self._true_measure.name
                    + " using tt.where, but the given false_value is not compatible with this measure. "
                    + "Ensure that false_value is returning "
                    + data_type_to_validate
                    + " values, just like true_value."
                )


@keyword_only_dataclass
@dataclass(eq=False)
class LevelValueFilteredMeasure(MeasureDescription):
    """A measure on a part of the cube filtered on a level value."""

    _underlying_measure: MeasureDescription
    _conditions: Collection[Condition] = ()

    def _do_distil(
        self, *, java_api: JavaApi, cube_name: str, measure_name: Optional[str] = None
    ) -> str:
        from ..level import Level

        # Distill the underlying measure
        underlying_name = self._underlying_measure._distil(
            java_api=java_api, cube_name=cube_name, measure_name=None
        )

        conditions: List[Dict[str, Any]] = []

        for condition in self._conditions:
            if isinstance(condition, LevelCondition):
                conditions.append(
                    {
                        "level": coordinates_to_java_description(
                            condition.level_coordinates
                        ),
                        "type": "other",
                        "operation": condition.operator,
                        "value": condition.value.name,
                    }
                    if isinstance(condition.value, Level)
                    else {
                        "level": coordinates_to_java_description(
                            condition.level_coordinates
                        ),
                        "type": "literal",
                        "operation": condition.operator,
                        "value": as_java_object(
                            condition.value, gateway=java_api.gateway
                        ),
                    }
                )
            if isinstance(condition, LevelIsinCondition):
                conditions.append(
                    {
                        "level": coordinates_to_java_description(
                            condition.level_coordinates
                        ),
                        "type": "literal",
                        "operation": condition.operator,
                        "value": to_java_object_list(
                            condition.members, gateway=java_api.gateway
                        ),
                    }
                )
            if isinstance(condition, HierarchyIsinCondition):
                conditions.append(
                    {
                        "level": coordinates_to_java_description(
                            (
                                condition.hierarchy_coordinates[0],
                                condition.hierarchy_coordinates[1],
                                condition.level_names[0],
                            )
                        ),
                        "type": "literal",
                        "operation": condition.operator,
                        "value": [
                            {
                                coordinates_to_java_description(
                                    (
                                        condition.hierarchy_coordinates[0],
                                        condition.hierarchy_coordinates[1],
                                        level_name,
                                    )
                                ): value
                                for level_name, value in zip(
                                    condition.level_names, member_path
                                )
                            }
                            for member_path in condition.member_paths
                        ],
                    }
                )

        # Create the filtered measure and return its name.
        distilled_name = java_api.create_measure(
            cube_name, measure_name, "FILTER", underlying_name, conditions
        )
        return distilled_name
