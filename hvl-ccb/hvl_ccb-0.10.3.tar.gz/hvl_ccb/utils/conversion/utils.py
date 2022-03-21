#  Copyright (c) 2021-2022 ETH Zurich, SIS ID and HVL D-ITET
#

import logging

import numpy as np

from hvl_ccb.utils.validation import validate_number

logger = logging.getLogger(__name__)


def preserve_type(func):
    """
    This wrapper preserves the first order type of the input.
    Upto now the type of the data stored in a list, tuple, array or dict
    is not preserved.
    Integer will be converted to float!
    """

    def wrap(self, value, **kwargs):
        data_type = type(value)
        validate_number("value", value, (-np.inf, np.inf), logger=logger)

        if data_type == dict:
            keys = list(value.keys())
            value = list(value.values())

        value_func = np.asarray(value, dtype=float)

        value_func = func(self, value_func, **kwargs)

        if data_type == list:
            value = list(value_func)
        elif isinstance(value, tuple) and hasattr(value, "_fields"):
            value = data_type(*value_func)
        elif data_type == tuple:
            value = tuple(value_func)
        elif data_type in (int, float):
            value = float(value_func)
        elif data_type == dict:
            value = dict(zip(keys, list(value_func)))
        else:
            value = value_func
        return value

    return wrap
