"""Utility functions that are not specific to the context of the package."""

import string
from functools import lru_cache, partial
from math import copysign
from typing import Generator, Tuple, Union

from ._constants import DEFAULT_TOKEN_PAD_LENGTH

ALPHABET = string.ascii_uppercase

assert set(ALPHABET).isdisjoint(string.digits)


def copysign_int(magnitude_of: int, sign_of: Union[int, float]) -> int:
    """:py:class:`int` version of :py:function:`copysign`."""
    return int(copysign(magnitude_of, sign_of))


@lru_cache()
def convert_base(n: int, base: int) -> Tuple[int, ...]:
    """Returns the digits of a given number when written in a different base.

    Digits are returned in ascending order of significance. Thus, any first
    digit returned represents the _units_ place.

    Arguments:
        n: Number to perform base conversion on
        base: Base to use for conversion

    Returns:
        tuple of int

        These are the digits (as `int` values) of `n` expressed in the base
        `base`. Digits are placed in ascending order of significance, so the
        units-place value occupies position 0.

        If `n` is 0, then an empty tuple is returned. Otherwise, only 0s which
        are significant figures are included.

    Raises:
        ValueError: `base` is less than or equal to 0.
    """
    if base <= 0:
        raise ValueError(
            f"Base should be strictly greater than 0. Provided: {base}."
        )

    eff_base = copysign_int(magnitude_of=base, sign_of=n)
    dividend = n

    if dividend == 0:
        return ()

    # Invariants
    #   divmod(dividend_old, eff_base) == (dividend_new, mod)
    #   dividend_old == dividend_new * eff_base + mod
    (dividend, mod) = divmod(dividend, eff_base)
    return (mod,) + convert_base(dividend, base)


def token_gen(
    pad_length: int = DEFAULT_TOKEN_PAD_LENGTH,
) -> Generator[str, int, None]:
    """Readable token generator."""
    ALPHABET_LENGTH = len(ALPHABET)

    fmt_base = partial("{:>0{pad}}".format, pad=pad_length)

    token = "__invalid__"

    while True:
        decimal = yield token  # Give the `str`; receive the next `int`

        base = fmt_base(decimal)  # Each character should be in `string.digits`
        x = len(base) - pad_length

        prefix = (
            "".join(
                ALPHABET[i]
                for i in reversed(convert_base(x - 1, ALPHABET_LENGTH))
            )
            if x > 0
            else ""
        )

        token = f"{prefix}{base}"

    # pass
