# probcalc - Calculate probabilities for distributions
# Copyright (C) 2022 D. Dyson (DoctorDalek1963)

# This program is licensed under GNU GPLv3, available here:
# <https://www.gnu.org/licenses/gpl-3.0.html>

"""This is the top-level ``probcalc`` package, which contains all the subpackages and submodules of the project.

Here's a table of user-friendly aliases and the backend classes they refer to:

.. list-table::
   :widths: 20 70
   :header-rows: 1

   * - Alias
     - Class or function name
   * - P
     - :class:`probcalc.distributions.ProbabilityCalculator`
   * - B
     - :class:`probcalc.distributions.BinomialDistribution`
   * - Po
     - :class:`probcalc.distributions.PoissonDistribution`
"""

from . import distributions, utility
from .distributions import NonsenseError

P = distributions.ProbabilityCalculator()
B = distributions.BinomialDistribution
Po = distributions.PoissonDistribution

__all__ = ['P', 'B', 'Po', 'NonsenseError', 'distributions', 'utility']

__version__ = '0.2.8'
