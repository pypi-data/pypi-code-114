"""Holds miscellaneous functions for the entire package

Disclaimer:
    All rights reserved, Blizzard is the intellectual property owner of Battle.net and any data
    retrieved from this API.
"""

from typing import Tuple, Optional, Union


def currency_convertor(value: int) -> Tuple[int, int, int]:
    """Returns the value into gold, silver and copper values

    Args:
        value (int): the value to be converted

    Returns:
        tuple: gold, silver and copper values
    """
    if value < 0:
        raise ValueError("Value must be zero or a positive value")

    return value // 10000, (value % 10000) // 100, value % 100


def slugify(value: str) -> str:
    """Returns the 'slugified' string

    Args:
        value (str): the string to be converted into a slug

    Returns:
        str: the slug of :value:
    """
    return value.lower().replace("'", "").replace(" ", "-")


def localize(locale: Optional[str] = None) -> Union[None, str]:
    """Returns the standardized locale

    Args:
        locale (str): the locality to be standardized

    Returns:
        str: the locale in the format of "<lang>_<COUNTRY>"

    Raise:
        TypeError: when locale is not a string
        ValueError: when the lang and country are not in the given lists
    """
    if not locale:
        return None

    if not isinstance(locale, str):
        raise TypeError("Locale must be a string")

    if locale[:2].lower() not in (
        "en",
        "es",
        "pt",
        "fr",
        "ru",
        "de",
        "it",
        "ko",
        "zh",
    ):
        raise ValueError("Invalid language bnet")

    if locale[-2:].lower() not in (
        "us",
        "mx",
        "br",
        "gb",
        "es",
        "fr",
        "ru",
        "de",
        "pt",
        "it",
        "kr",
        "tw",
        "cn",
    ):
        raise ValueError("Invalid country bnet")

    return f"{locale[:2].lower()}_{locale[-2:].upper()}"
