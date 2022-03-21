# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import numpy
from numpy.random import weibull
from scipy.special import gamma
from availsim4core.src.context.system.probability_law.probability_law import ProbabilityLaw


class WeibullLaw(ProbabilityLaw):
    """
    Class used to generate values according to the Weibull law
    """

    def __init__(self,
                 parameters):
        super().__init__(self.__class__.__name__,
                         parameters,
                         is_failure_on_demand=False)

    def __eq__(self, other):
        if not isinstance(other, WeibullLaw):
            return NotImplemented
        return super().__eq__(other)

    def get_random_value(self):
        return self.parameters[0]*weibull(self.parameters[1])

    def get_quantile_value(self, quantile):
        return self.parameters[0]*(-numpy.log(1-quantile)**(1/self.parameters[1]))

    def get_mean_value(self):
        return self.parameters[0]*gamma(1+1/self.parameters[1])

    def get_variance_value(self):
        return self.parameters[0] ** 2 * (
            gamma(1 + 2 / self.parameters[1]) - gamma(1 + 1 / self.parameters[1]) ** 2
        )