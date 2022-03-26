import numpy as np

ndarray_repr = np.ndarray.__repr__


def ndarray_info(array: np.ndarray) -> str:
    """Return human-friendly debug info of the ndarray.
    :param array np.ndarray: The array to look into.
    :return str: The string representation of the array.

    >>> arr = np.arange(3*4).reshape(3, 4)
    >>> print(ndarray_info(arr))
    <ndarray: shape=(3, 4), dtype=int64>
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])

    >>> arr = np.arange(10000).reshape(100,100)
    >>> print(ndarray_info(arr))
    <ndarray: shape=(100, 100), dtype=int64>
    array([[   0,    1,    2, ...,   97,   98,   99],
           [ 100,  101,  102, ...,  197,  198,  199],
           [ 200,  201,  202, ...,  297,  298,  299],
           ...,
           [9700, 9701, 9702, ..., 9797, 9798, 9799],
           [9800, 9801, 9802, ..., 9897, 9898, 9899],
           [9900, 9901, 9902, ..., 9997, 9998, 9999]])
    """
    attributes = [
        f"shape={array.shape}",
        f"dtype={array.dtype}",
    ]
    return f"""\
<{array.__class__.__name__}: {', '.join(attributes)}>
{array.__repr__()}"""

    r"""
    data = ndarray_repr(array)
    data = re.findall(r'\[.*\]', data, flags=re.MULTILINE | re.DOTALL)[0]
    attributes.append(f"data=\n      {data}")

    return f'''array({', '.join(attributes)})'''
    """
