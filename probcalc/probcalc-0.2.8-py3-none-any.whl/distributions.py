# probcalc - Calculate probabilities for distributions
# Copyright (C) 2022 D. Dyson (DoctorDalek1963)

# This program is licensed under GNU GPLv3, available here:
# <https://www.gnu.org/licenses/gpl-3.0.html>

"""This module contains classes for various probability distributions, and a convenience function."""

from __future__ import annotations

import abc
import math
from typing import Literal

from .utility import choose, round_sig_fig


class NonsenseError(Exception):
    """A simple error representing mathematical nonsense.

    This could be a probability that doesn't make sense, or getting more successes than trials, etc.
    """


class Bounds:
    """This is a simple little class to hold bounds for a :class:`Distribution` object."""

    lower: tuple[int | None, bool]
    """The lower of the two bounds.

    The first element of the tuple is the value of the bound itself. None means the
    natural bound of the distribution. This can be 0, negative infinity, or something
    else depending on the distribution.

    The second element of the tuple is whether the value bound of the should be included
    in probability calculations or not.
    """

    upper: tuple[int | None, bool]
    """The upper of the two bounds.

    The first element of the tuple is the value of the bound itself. None means the
    natural bound of the distribution. This can be the maximum number of trials,
    infinity, or something else depending on the distribution.

    The second element of the tuple is whether the value bound of the should be included
    in probability calculations or not.
    """

    def __init__(self):
        """Create a :class:`Bounds` object with default bounds.

        These default bounds are ``(None, False)``, meaning everything up to but
        not including the natural bounds of the distribution. We don't include it,
        because evaluating probability at something like infinity might not make
        sense all the time.
        """
        self.lower = (None, False)
        self.upper = (None, False)

    def __repr__(self) -> str:
        """Return a simple repr of the object, containing the value of the lower and upper bounds."""
        return f'{self.__class__.__module__}.{self.__class__.__name__}({self.lower}, {self.upper})'

    def __eq__(self, other):
        """Check equality.

        This dunder method has been implemented purely to allow distributions to throw
        errors when users attempt to combine inequality and equality logic operators.
        To check against that, though, we need to be able to check :class:`Bounds` equality.
        """
        if not isinstance(other, Bounds):
            return NotImplemented

        return self.lower == other.lower and self.upper == other.upper


class Distribution(abc.ABC):
    """This is an abstract superclass representing an arbitrary probability distribution.

    It implements logical comparison dunder methods and :meth:`calculate`, which allow
    it to be used easily in :func:`calculate_probability`.
    """

    accepts_floats: bool
    """This attribute is a flag for whether this distribution accepts floats, or only accepts ints.

    If it accepts floats, then it is continuous, if it doesn't, then it's discrete.

    .. note::
       All logical comparison dunder methods implemented here check against this flag and return
       ``NotImplemented`` if the user tries to compare a discrete distribution with a float.
    """

    negate_probability: bool
    """This attribute is a flag set by :meth:`__ne__` and used by :meth:`calculate` for the ``!=`` operator."""

    def __init__(self, *, accepts_floats: bool):
        """Create a :class:`Distribution` object with natural bounds and one flag.

        :param bool accepts_floats: Whether this distribution should accept floats
        """
        self.bounds = Bounds()
        self.accepts_floats = accepts_floats
        self.negate_probability = False

    def reset(self) -> None:
        """Reset the bounds of the distribution to be the default, and reset :attr:`negate_probability` flag."""
        self.bounds = Bounds()
        self.negate_probability = False

    @abc.abstractmethod
    def __repr__(self) -> str:
        """Return a simple repr of the distribution, normally the syntax used to construct it."""

    def __eq__(self, other):
        """Set the upper and lower bounds to ``other``, if possible.

        This method checks the bounds against the defaults to see if the user has
        previously compared this distribution with an inequality operator. If they
        have, then we raise an error.

        :raises NonsenseError: If the user has tried to mix inequality and equality comparison
        """
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        # If the bounds are already mutated, then we've mixed inequality and equality
        if self.bounds != Bounds():
            raise NonsenseError('Cannot have inequality and equality mixed together')

        self.bounds.upper = (other, True)
        self.bounds.lower = (other, True)
        return self

    def __ne__(self, other):
        """Set the upper and lower bounds to ``other``, if possible, and set :attr:`negate_probability`.

        See :meth:`__eq__`.

        :raises NonsenseError: If the user has tried to mix inequality and equality comparison
        """
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        # If the bounds are already mutated, then we've mixed inequality and equality
        if self.bounds != Bounds():
            raise NonsenseError('Cannot have inequality and equality mixed together')

        self.bounds.upper = (other, True)
        self.bounds.lower = (other, True)

        self.negate_probability = True
        return self

    def __lt__(self, other):
        """Set the upper bound and don't include this value."""
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        self.bounds.upper = (other, False)
        return self

    def __le__(self, other):
        """Set the upper bound and include this value."""
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        self.bounds.upper = (other, True)
        return self

    def __gt__(self, other):
        """Set the lower bound and don't include this value."""
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        self.bounds.lower = (other, False)
        return self

    def __ge__(self, other):
        """Set the lower bound and include this value."""
        if not (isinstance(other, int) or (self.accepts_floats and isinstance(other, float))):
            return NotImplemented

        self.bounds.lower = (other, True)
        return self

    def calculate(self, *, strict: bool = True) -> float:
        """Return the probability of a random variable from this distribution taking on a value within its bounds.

        .. warning:: If ``strict`` is False, then we get undefined behaviour. Beware.

        .. warning::
           This method should only really be used in scripts and things, because it can easily
           result in undefined behaviour when the :class:`Distribution` object is mutated
           between calls, which is often done with logical comparison operators.

           If you want a good way to calculate probability interactively, see :func:`calculate_probability`.

        :param bool strict: Whether to raise errors or just ignore them
        :returns float: The calculated probability
        """
        lower = self.bounds.lower
        upper = self.bounds.upper

        probability = 1.0

        if upper[0] is not None:
            probability = self.cdf(upper[0], strict=strict)

            if not upper[1]:
                probability -= self.pmf(upper[0], strict=strict)

        if lower[0] is not None:
            probability -= self.cdf(lower[0], strict=strict)

            if lower[1]:
                probability += self.pmf(lower[0], strict=strict)

        if probability < 0:
            raise NonsenseError("This inequality doesn't make sense")

        if self.negate_probability:
            probability = 1 - probability

        return round_sig_fig(probability, 10)

    @abc.abstractmethod
    def pmf(self, value: int, *, strict: bool = True) -> float:
        """Evaluate the PMF (probability mass function) of this distribution.

        This is the probability that a random variable distributed by this
        distribution takes on the given value.

        :param int value: The value to find the probability of
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The calculated probability

        :raises NonsenseError: If the value doesn't make sense in the context of the distribution
        """

    @abc.abstractmethod
    def cdf(self, value: int, *, strict: bool = True) -> float:
        """Evaluate the CDF (cumulative distribution function) of this distribution.

        This is the probability that a random variable distributed by this
        distribution takes on a value less than or equal to the given value.

        :param int value: The value to find the probability for
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The calculated probability

        :raises NonsenseError: If the value doesn't make sense in the context of the distribution
        """


class BinomialDistribution(Distribution):
    """This is a binomial distribution, used to model multiple independent, binary trials."""

    def __init__(self, number_of_trials: int, probability: float):
        """Construct a binomial distribution from a given number of trials and probability of success for each trial."""
        if not 0 <= probability <= 1:
            raise NonsenseError(f'Binomial probability must be between 0 and 1, not {probability}')

        super().__init__(accepts_floats=False)

        self._number_of_trials = number_of_trials
        self._probability = probability

    def __repr__(self) -> str:
        """Return a nice repr of the distribution."""
        return f'B({self._number_of_trials}, {self._probability})'

    def _choose(self, r: int) -> int:
        """Call :meth:`probcalc.utility.choose` with the instance number of trials and the provided value."""
        return choose(self._number_of_trials, r)

    def check_nonsense(self, successes: int, *, strict: bool) -> Literal[None, -1]:
        """Check if the given number of successes is nonsense.

        :param int successes: The number of successes to check
        :param bool strict: Whether to throw errors or just return -1
        :returns: None on success, -1 on fail
        :rtype: Literal[None, -1]

        :raises NonsenseError: If the number of successes is outside the valid range
        :raises NonsenseError: If the number of successes is not an integer
        """
        if successes < 0:
            if strict:
                raise NonsenseError(f'Cannot have negative number of successes ({successes})')

            return -1

        if successes > self._number_of_trials:
            if strict:
                raise NonsenseError(f'Cannot have more success ({successes}) than trials ({self._number_of_trials})')

            return -1

        if successes != int(successes):
            if strict:
                raise NonsenseError(f'Cannot ask probability of {successes} successes')

            return -1

        return None

    def pmf(self, successes: int, *, strict: bool = True) -> float:
        r"""Return the probability that we get a given number of successes.

        This method uses the formula :math:`\binom{n}{r} p^r q^{n - r}` where
        :math:`n` is the number of trials, :math:`r` is the number of successes,
        :math:`p` is the probability of each success, and :math:`q = 1 - p`.

        :param int successes: The number of successes to find the probability of
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The probability of getting exactly this many successes

        :raises NonsenseError: If the number of successes is outside the valid range
        :raises NonsenseError: If the number of successes is not an integer
        """
        if self.check_nonsense(successes, strict=strict) is not None:
            return 0

        return self._choose(successes) * (self._probability ** successes) * \
            ((1 - self._probability) ** (self._number_of_trials - successes))

    def cdf(self, successes: int, *, strict: bool = True) -> float:
        """Return the probability that we get less than or equal to the given number of successes.

        This method just sums :meth:`pmf` from 0 to the given number of successes.

        :param int successes: The number of successes to find the probability for
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The probability of getting less than or equal to this many successes

        :raises NonsenseError: If the number of successes is outside the valid range
        :raises NonsenseError: If the number of successes is not an integer
        """
        if self.check_nonsense(successes, strict=strict) is not None:
            return 0

        if successes == self._number_of_trials:
            return 1

        # mypy expects this sum to have ints for some reason, so we ignore it
        return sum(self.pmf(x) for x in range(successes + 1))  # type: ignore[misc]

    def calculate(self, *, strict: bool = True) -> float:
        """Check for nonsense in an edge case.

        This method overrides :meth:`Distribution.calculate`. See that method for documentation.
        """
        if self.bounds.lower == (self._number_of_trials, False):
            raise NonsenseError(f'Cannot have more successes (> {self._number_of_trials}) '
                                f'than trials ({self._number_of_trials})')

        return super().calculate(strict=strict)


class PoissonDistribution(Distribution):
    """This is a Poisson distribution, used to model independent events that happen at a constant average rate."""

    def __init__(self, rate: float):
        """Construct a Poisson distribution with the given average rate of event occurrence."""
        if rate < 0:
            raise NonsenseError(f'Cannot have negative rate in Poisson distribution ({rate})')

        super().__init__(accepts_floats=False)

        self._rate = rate

    def __repr__(self) -> str:
        """Return a nice repr of the distribution."""
        return f'Po({self._rate})'

    @staticmethod
    def check_nonsense(number: int, *, strict: bool = True) -> Literal[None, -1]:
        """Check if the given number of event occurrences is nonsense.

        :param int number: The number of occurrences to check
        :param bool strict: Whether to throw errors or just return -1
        :returns: None on success, -1 on fail
        :rtype: Literal[None, -1]

        :raises NonsenseError: If the number is negative
        :raises NonsenseError: If the number is not an integer
        """
        if number < 0:
            if strict:
                raise NonsenseError(f'Cannot have negative number of event occurrences ({number})')

            return -1

        if number != int(number):
            if strict:
                raise NonsenseError(f'Number of occurrences must be an integer, not {number}')

            return -1

        return None

    def pmf(self, number: int, *, strict: bool = True) -> float:
        r"""Return the probability that we get a given number of occurrences.

        This method uses the formula :math:`\frac{e^{-\lambda} \lambda^x}{x!}`,
        where :math:`x` is the number of occurrences and :math:`\lambda` is the
        rate of the distribution.

        :param int number: The number of occurrences to find the probability of
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The probability of getting exactly this many occurrences

        :raises NonsenseError: If the number of occurrences is negative
        :raises NonsenseError: If the number of occurrences is not an integer
        """
        if self.check_nonsense(number, strict=strict) is not None:
            return 0

        if number == 0:
            return math.exp(-self._rate)

        # This line is pure magic that I stole from the SciPy source code
        # https://github.com/scipy/scipy/blob/main/scipy/stats/_discrete_distns.py#L854-L860
        log_pmf = number * math.log(self._rate) - math.lgamma(number + 1) - self._rate
        return math.exp(log_pmf)

    def cdf(self, number: int, *, strict: bool = True) -> float:
        """Return the probability that we get less than or equal to the given number of occurrences.

        This method just sums :meth:`pmf` from 0 to the given number of occurrences.

        :param int number: The number of occurrences to find the probability for
        :param bool strict: Whether to throw errors for invalid input, or return 0
        :returns float: The probability of getting exactly this many occurrences

        :raises NonsenseError: If the number of occurrences is negative
        :raises NonsenseError: If the number of occurrences is not an integer
        """
        if self.check_nonsense(number, strict=strict) is not None:
            return 0

        return sum(self.pmf(x) for x in range(number + 1))  # type: ignore[misc]


class ProbabilityCalculator:
    """This class only exists to give the probability calculator a nice repr."""

    def __repr__(self) -> str:
        """Return a very simple repr of the calculator."""
        return 'P'

    def __call__(self, distribution: Distribution) -> float:
        """Return the probability of a random variable from this distribution taking on a value within its bounds.

        This function is just a convenient wrapper around :meth:`Distribution.calculate`.

        .. note::
           This function calls :meth:`Distribution.reset`, but :meth:`Distribution.calculate`
           doesn't on its own. Using the class method multiple times with different inputs can
           result in undefined behaviour. Use this wrapper for all interactive use.

        This function gets exported as ``P`` by ``__init__.py``, which lets the user do things like:

        :Example:

        >>> from probcalc import P, B
        >>> X = B(20, 0.5)
        >>> P(X > 6)
        0.9423408508
        >>> P(4 < X <= 12)
        0.8625030518

        :param Distribution distribution: The probability distribution that we're using to calculate the value
        :returns float: The calculated probability

        :raises NonsenseError: If the bounds of the distribution are invalid
        """
        try:
            probability = distribution.calculate(strict=True)

        except NonsenseError as e:
            raise e

        finally:
            distribution.reset()

        return probability
