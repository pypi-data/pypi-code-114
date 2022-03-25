# probcalc - Calculate probabilities for distributions
# Copyright (C) 2022 D. Dyson (DoctorDalek1963)

# This program is licensed under GNU GPLv3, available here:
# <https://www.gnu.org/licenses/gpl-3.0.html>

"""A simple utility module to just provide helper functions for the maths."""

from functools import reduce
from math import exp, floor, log10, pi, sqrt
from operator import mul

# Compute constants at import time for slight speed increase
TWO_OVER_ROOT_PI = 2 / sqrt(pi)


def factorial(n: int) -> int:
    """Return the factorial of ``n``."""
    return reduce(mul, range(1, n + 1), 1)


def factorial_fraction(n: int) -> float:
    """Return ``1 / factorial(n)``, but without overflowing."""
    return reduce(lambda a, b: a / b, range(1, n + 1), 1.0)


def choose(n: int, r: int) -> int:
    r"""Return the number of ways to choose ``r`` items from ``n`` elements.

    This is often written as :math:`\binom{n}{r}` or :math:`^nC_r`.

    :param int n: The number of items to choose from
    :param int r: The number of items to be chosen
    :returns int: The number of ways to choose ``r`` from ``n``

    :raises ValueError: If ``r > n``
    """
    if r > n:
        raise ValueError(f'Cannot choose {r} items from only {n} elements')

    return factorial(n) // (factorial(r) * factorial(n - r))


def round_sig_fig(n: float, sig_fig: int) -> float:
    """Round ``n`` to a given number of significant figures.

    :Example:

    >>> round_sig_fig(0.123456789, 3)
    0.123
    >>> round_sig_fig(0.123456789, 6)
    0.123457
    >>> round_sig_fig(0.123456789, 9)
    0.123456789
    >>> round_sig_fig(0.0000123456789, 3)
    1.23e-05

    :param float n: The number to round
    :param int sig_fig: The number of significant figures to round to
    :returns float: The rounded number
    """
    # This code was taken from a comment on this SO answer: https://stackoverflow.com/a/3411435/12985838
    return n if n == 0 else round(n, -int(floor(log10(abs(n)))) + (sig_fig - 1))


def erf(x: float) -> float:
    r"""Return the error function evaluated at :math:`x`.

    The error function is defined as an integral which cannot be evaluated using analytical techniques
    (:math:`\text{erf}z=\frac{2}{\sqrt{\pi}}\int_0^z e^{-t^2}dt`). Rather than doing numeric integration,
     this method uses a numerical approximation found on the Wikipedia page.
    """
    if x == 0:
        return 0

    if x < 0:
        return -erf(-x)

    # Magic numbers taken from https://en.wikipedia.org/wiki/Error_function#Approximation_with_elementary_functions
    t = 1 / (1 + 0.3275911 * x)
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429

    return 1 - (
        a1 * t +
        a2 * t ** 2 +
        a3 * t ** 3 +
        a4 * t ** 4 +
        a5 * t ** 5
    ) * exp(-x ** 2)
