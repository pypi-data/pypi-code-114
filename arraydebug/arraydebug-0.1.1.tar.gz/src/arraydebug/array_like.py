def array_like_info(array_like) -> str:
    """
    Return human-friendly debug info of the array_like object.
    :param array_like:
        The array_like object to look into, such as pandas.DataFrame.
    :return str: the string representation of the array_like object.

    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame(
    ...     np.arange(24).reshape(6, 4) + 1000,
    ...     index=pd.date_range("20130101", periods=6),
    ...     columns=list("ABCD"))
    >>> print(array_like_info(df))
    <DataFrame: shape=(6, 4), dtype=int64>
                   A     B     C     D
    2013-01-01  1000  1001  1002  1003
    2013-01-02  1004  1005  1006  1007
    2013-01-03  1008  1009  1010  1011
    2013-01-04  1012  1013  1014  1015
    2013-01-05  1016  1017  1018  1019
    2013-01-06  1020  1021  1022  1023
    """
    array = array_like.__array__()
    return f"""\
<{array_like.__class__.__name__}: shape={array.shape}, dtype={array.dtype}>
{array_like.__repr__()}"""
