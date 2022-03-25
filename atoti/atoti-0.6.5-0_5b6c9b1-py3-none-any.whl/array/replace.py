from __future__ import annotations

from typing import Mapping, Union

from .._measures.generic_measure import GenericMeasure
from ..measure_description import MeasureDescription
from ._utils import check_array_type


def replace(
    measure: MeasureDescription,
    replacements: Union[Mapping[float, float], Mapping[int, int]],
) -> MeasureDescription:
    """Return a measure where elements equal to a key of the *replacements* mapping are replaced with the corresponding value.

    Args:
        measure: The array measure in which to replace the elements.
        replacements: The mapping from the old values to the new ones.

    Example:

        >>> df = pd.DataFrame(
        ...     columns=["Store ID", "New quantity", "Old quantity"],
        ...     data=[
        ...         (
        ...             "Store 1",
        ...             [12, 6, 2, 20],
        ...             [6, 3, 0, 10],
        ...         ),
        ...         ("Store 2", [16, 8, 12, 15], [4, 4, 6, 3]),
        ...         ("Store 3", [8, -10, 0, 33], [8, 0, 2, 11]),
        ...     ],
        ... )
        >>> table = session.read_pandas(df, table_name="Prices", keys=["Store ID"])
        >>> cube = session.create_cube(table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Old quantity"] = tt.value(table["Old quantity"])
        >>> m["New quantity"] = tt.value(table["New quantity"])
        >>> m["Quantity ratio"] = m["New quantity"] / m["Old quantity"]
        >>> m["Quantity ratio"].formatter = "ARRAY[',']"
        >>> cube.query(m["Quantity ratio"], levels=[l["Store ID"]])
                         Quantity ratio
        Store ID
        Store 1    2.0,2.0,Infinity,2.0
        Store 2         4.0,2.0,2.0,5.0
        Store 3   1.0,-Infinity,0.0,3.0

        The function can be used to replace **infinity** with another value more suited to follow up computations:

        >>> import math
        >>> m["Quantity ratio without infinity"] = tt.array.replace(
        ...     m["Quantity ratio"], {math.inf: 1, -math.inf: -1}
        ... )
        >>> m["Quantity ratio without infinity"].formatter = "ARRAY[',']"
        >>> cube.query(m["Quantity ratio without infinity"], levels=[l["Store ID"]])
                 Quantity ratio without infinity
        Store ID
        Store 1                  2.0,2.0,1.0,2.0
        Store 2                  4.0,2.0,2.0,5.0
        Store 3                 1.0,-1.0,0.0,3.0

    """
    check_array_type(measure)
    return GenericMeasure("VECTOR_REPLACE", replacements, [measure])
