from typing import Literal

from atoti_core import is_temporal_type

from .._measures.date_shift import DateShift
from ..hierarchy import Hierarchy
from ..measure_description import MeasureDescription

_DateShiftMethod = Literal["exact", "previous", "next", "interpolate"]


def date_shift(
    measure: MeasureDescription,
    on: Hierarchy,
    *,
    offset: str,
    method: _DateShiftMethod = "exact",
) -> MeasureDescription:
    """Return a measure equal to the passed measure shifted to another date.

    Args:
        measure: The measure to shift.
        on: The hierarchy to shift on.
            Only hierarchies with a single level of type date (or datetime) are supported.
            If one of the member of the hierarchy is ``N/A`` their shifted value will always be ``None``.
        offset: The offset of the form ``xxDxxWxxMxxQxxY`` to shift by.
            Only the ``D``, ``W``, ``M``, ``Q``, and ``Y`` offset aliases are supported.
            Offset aliases have the `same meaning as Pandas' <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases>`__.
        method: Determine the value to use when there is no member at the shifted date:

            * ``exact``: ``None``.
            * ``previous``: Value at the previous existing date.
            * ``next``: Value at the next existing date.
            * ``interpolate``: Linear interpolation of the values at the previous and next existing dates:

    Example:
        >>> from datetime import date
        >>> df = pd.DataFrame(
        ...     columns=["Date", "Price"],
        ...     data=[
        ...         (date(2020, 1, 5), 15.0),
        ...         (date(2020, 2, 3), 10.0),
        ...         (date(2020, 3, 3), 21.0),
        ...         (date(2020, 4, 5), 9.0),
        ...     ],
        ... )
        >>> table = session.read_pandas(
        ...     df,
        ...     table_name="date_shift example",
        ... )
        >>> cube = session.create_cube(table)
        >>> h, l, m = cube.hierarchies, cube.levels, cube.measures
        >>> m["Exact"] = tt.date_shift(
        ...     m["Price.SUM"], on=h["Date"], offset="1M", method="exact"
        ... )
        >>> m["Previous"] = tt.date_shift(
        ...     m["Price.SUM"], on=h["Date"], offset="1M", method="previous"
        ... )
        >>> m["Next"] = tt.date_shift(
        ...     m["Price.SUM"], on=h["Date"], offset="1M", method="next"
        ... )
        >>> m["Interpolate"] = tt.date_shift(
        ...     m["Price.SUM"], on=h["Date"], offset="1M", method="interpolate"
        ... )
        >>> cube.query(
        ...     m["Price.SUM"],
        ...     m["Exact"],
        ...     m["Previous"],
        ...     m["Next"],
        ...     m["Interpolate"],
        ...     levels=[l["Date"]],
        ... )
                   Price.SUM  Exact Previous   Next Interpolate
        Date
        2020-01-05     15.00           10.00  21.00       10.76
        2020-02-03     10.00  21.00    21.00  21.00       21.00
        2020-03-03     21.00           21.00   9.00        9.73
        2020-04-05      9.00            9.00

        Explanations for :guilabel:`Interpolate`'s values:

        * ``10.76``: linear interpolation of ``2020-02-03``'s ``10`` and ``2020-03-03``'s ``21`` at ``2020-02-05``.
        * ``21.00``: no interpolation required since there is an exact match at ``2000-03-03``.
        * ``9.73``: linear interpolation of ``2020-03-03``'s ``21`` and ``2020-04-05``'s ``9`` for ``2020-04-03``.
        * ∅: no interpolation possible because there are no records after ``2020-04-05``.

    """
    if len(on.levels) > 1 or not is_temporal_type(
        next(iter(on.levels.values())).data_type.java_type
    ):
        raise ValueError(
            f"Invalid hierarchy {on.name}, only hierarchies with a single date level are supported."
        )
    return DateShift(
        _underlying_measure=measure,
        _level_coordinates=list(on.levels.values())[-1]._coordinates,
        _shift=offset,
        _method=method,
    )
