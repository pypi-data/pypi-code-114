from atoti_core import coordinates_to_java_description

from .._measures.generic_measure import GenericMeasure
from ..level import Level
from ..measure_description import MeasureDescription


def shift(
    measure: MeasureDescription, on: Level, *, offset: int = 1
) -> MeasureDescription:
    """Return a measure equal to the passed measure shifted to another member.

    Args:
        measure: The measure to shift.
        on: The level to shift on.
        offset: The amount of members to shift by.

    """
    return GenericMeasure(
        "LEAD_LAG",
        measure,
        coordinates_to_java_description(on._hierarchy_coordinates),
        offset,
    )
