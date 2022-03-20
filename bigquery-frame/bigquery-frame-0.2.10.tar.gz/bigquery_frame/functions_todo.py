from typing import Union

from bigquery_frame.dataframe import cols_to_str, Column
from bigquery_frame.functions import __str_to_col
from bigquery_frame import functions as f


def when(condition: Column, value: Column) -> Column:
    """Evaluates a list of conditions and returns one of multiple possible result expressions.
    If :func:`Column.otherwise` is not invoked, None is returned for unmatched conditions.

    :param condition: a boolean :class:`Column` expression.
    :param value: a :class:`Column` expression.
    :return:
    """
    # TODO


def hash(*cols: Union[str, Column]) -> Column:
    cols = __str_to_col(cols)
    return f.expr(f"FARM_FINGERPRINT(TO_JSON_STRING(STRUCT({cols_to_str(cols)})))")


def sort_array(col: Union[str, Column]) -> Column:
    col = __str_to_col(col)
    return f.expr(f"ARRAY(SELECT x FROM UNNEST({col}) AS x ORDER BY x)")
