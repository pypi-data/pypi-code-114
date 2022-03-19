
from typing import Callable


ASCII_EXTENDED = bytes(range(128, 255))
LOWER_ALPHABETS = b"abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABETS = LOWER_ALPHABETS + UPPER_ALPHABETS
DIGITS = b"0123456789"
LEGAL_SIGNS = b"~!@#$%^&()_+=-`;'.,}{[]"
ILLEGAL_SIGNS = b"\\/:*?\"<>|"
SIGNS = LEGAL_SIGNS + ILLEGAL_SIGNS
SPACE = b" "


def pattern(*args) -> Callable[[int, int, str], bool]:
    """
    This function creates another function that is accepted as `allowness` parameter of `patinput` function. The 
    accepted pattern is sum of all characters which are given as arguments of this method.  

    Returns:
        Callable[[int, int, str], bool]: A function that accepted as `allowness` parameter of `patinput` function
    """

    full = b""
    for arg in args:
        if isinstance(arg, bytes):
            full += arg
    return lambda char, position, string: char in list(full)


ALOW_NUMBERS = pattern(DIGITS)
ALOW_ALPHABETS = pattern(SPACE, ALPHABETS)
ALOW_NOSPACE = pattern(ALPHABETS, DIGITS, LEGAL_SIGNS)