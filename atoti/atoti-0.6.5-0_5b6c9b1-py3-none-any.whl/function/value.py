from __future__ import annotations

from typing import Iterable, Optional

from .._measures.table_measure import SingleValueTableMeasure
from ..column import Column
from ..level import Level
from ..measure_description import MeasureDescription


def value(
    column: Column, *, levels: Optional[Iterable[Level]] = None
) -> MeasureDescription:
    """Return a measure equal to the value of the given table column.

    Args:
        column: The table column to get the value from.
        levels: The levels that must be expressed for this measure to possibly be non-null.

            When ``None``, the measure will also be ``None`` if the levels corresponding to the keys of *column*'s table are not expressed.

            Passing an empty collection propagate the value on all levels when possible.

    Example:
        >>> sales_df = pd.DataFrame(
        ...     columns=["Month", "City", "Product"],
        ...     data=[
        ...         ("January", "Manchester", "Ice cream"),
        ...         ("January", "London", "Ice cream"),
        ...         ("January", "London", "Burger"),
        ...         ("March", "New York", "Ice cream"),
        ...         ("March", "New York", "Burger"),
        ...     ],
        ... )
        >>> products_df = pd.DataFrame(
        ...     columns=["Name", "Month", "Purchase price"],
        ...     data=[
        ...         ("Ice cream", "January", 10.0),
        ...         ("Ice cream", "February", 10.0),
        ...         ("Ice cream", "March", 10.0),
        ...         ("Burger", "January", 10.0),
        ...         ("Burger", "February", 10.0),
        ...         ("Burger", "March", 8.0),
        ...     ],
        ... )
        >>> sales_table = session.read_pandas(
        ...     sales_df, keys=["Month", "City", "Product"], table_name="Sales"
        ... )
        >>> products_table = session.read_pandas(
        ...     products_df, keys=["Name", "Month"], table_name="Products"
        ... )
        >>> sales_table.join(
        ...     products_table, mapping={"Month": "Month", "Product": "Name"}
        ... )
        >>> cube = session.create_cube(sales_table)
        >>> l, m = cube.levels, cube.measures
        >>> m["Purchase price"] = tt.value(products_table["Purchase price"])

        By default, the values do not propagate:

        >>> cube.query(
        ...     m["Purchase price"],
        ...     m["contributors.COUNT"],
        ...     include_totals=True,
        ...     levels=[l["Month"], l["City"], l["Product"]],
        ... )
                                     Purchase price contributors.COUNT
        Month   City       Product
        Total                                                        5
        January                                                      3
                London                                               2
                           Burger             10.00                  1
                           Ice cream          10.00                  1
                Manchester                                           1
                           Ice cream          10.00                  1
        March                                                        2
                New York                                             2
                           Burger              8.00                  1
                           Ice cream          10.00                  1

        To propagate the values to the :guilabel:`City` level, the measure can instead be defined as follows:

        >>> m["Purchase price"] = tt.value(
        ...     products_table["Purchase price"], levels=[l["City"]]
        ... )

        With this definition, if all products of a city share the same purchase price, then the city inherits that price:

        >>> cube.query(
        ...     m["Purchase price"],
        ...     m["contributors.COUNT"],
        ...     include_totals=True,
        ...     levels=[l["Month"], l["City"], l["Product"]],
        ... )
                                     Purchase price contributors.COUNT
        Month   City       Product
        Total                                                        5
        January                                                      3
                London                        10.00                  2
                           Burger             10.00                  1
                           Ice cream          10.00                  1
                Manchester                    10.00                  1
                           Ice cream          10.00                  1
        March                                                        2
                New York                                             2
                           Burger              8.00                  1
                           Ice cream          10.00                  1

        Since the measure has not been defined to propagate on :guilabel:`Product`, changing the order of the levels prevents any propagation:

        >>> cube.query(
        ...     m["Purchase price"],
        ...     m["contributors.COUNT"],
        ...     include_totals=True,
        ...     levels=[l["Month"], l["Product"], l["City"]],
        ... )
                                     Purchase price contributors.COUNT
        Month   Product   City
        Total                                                        5
        January                                                      3
                Burger                                               1
                          London              10.00                  1
                Ice cream                                            2
                          London              10.00                  1
                          Manchester          10.00                  1
        March                                                        2
                Burger                                               1
                          New York             8.00                  1
                Ice cream                                            1
                          New York            10.00                  1

        Using ``levels=[]``, the value propagates to :guilabel:`Month` too:

        >>> m["Purchase price"] = tt.value(products_table["Purchase price"], levels=[])
        >>> cube.query(
        ...     m["Purchase price"],
        ...     m["contributors.COUNT"],
        ...     include_totals=True,
        ...     levels=[l["Month"], l["City"], l["Product"]],
        ... )
                                     Purchase price contributors.COUNT
        Month   City       Product
        Total                                                        5
        January                               10.00                  3
                London                        10.00                  2
                           Burger             10.00                  1
                           Ice cream          10.00                  1
                Manchester                    10.00                  1
                           Ice cream          10.00                  1
        March                                                        2
                New York                                             2
                           Burger              8.00                  1
                           Ice cream          10.00                  1

        When filtering out the members with a different :guilabel:`Product Price`, it even propagates all the way to the grand total:

        >>> cube.query(
        ...     m["Purchase price"],
        ...     m["contributors.COUNT"],
        ...     condition=l["Month"] == "January",
        ...     include_totals=True,
        ...     levels=[l["Month"], l["City"], l["Product"]],
        ... )
                                     Purchase price contributors.COUNT
        Month   City       Product
        Total                                 10.00                  3
        January                               10.00                  3
                London                        10.00                  2
                           Burger             10.00                  1
                           Ice cream          10.00                  1
                Manchester                    10.00                  1
                           Ice cream          10.00                  1

    """
    return SingleValueTableMeasure(
        _column_name=column.name,
        _table_name=column._table_name,
        _column_data_type=column.data_type,
        _levels=levels,
    )
