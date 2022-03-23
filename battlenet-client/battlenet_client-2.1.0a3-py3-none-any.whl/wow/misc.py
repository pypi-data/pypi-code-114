"""Miscellaneous functions to support world of warcraft

Functions:
    currency_convertor
"""
from typing import Tuple


def currency_convertor(value: int) -> Tuple[int, int, int]:
    """Returns the value into gold, silver and copper

    Args:
        value (int/str): the value to be converted

    Returns:
        tuple: gold, silver and copper values
    """
    value = int(value)

    if value < 0:
        raise ValueError("Value cannot be negative")

    return value // 10000, (value % 10000) // 100, value % 100
