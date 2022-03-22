# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List


class ProbabilityLaw:
    """
    Distributive Function which is used to evaluate the failure and repair times.
    """
    __slots__ = 'name', 'parameters', 'is_failure_on_demand'

    def __init__(self,
                 name: str,
                 parameters: List[float],
                 is_failure_on_demand):
        self.name = name
        self.parameters = parameters
        self.is_failure_on_demand = is_failure_on_demand

    def __str__(self):
        return f"{self.name} -> {self.parameters}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.name == other.name and \
               self.parameters == other.parameters

    def get_random_value(self):
        pass

    def get_quantile_value(self, quantile):
        pass

    def get_mean_value(self):
        pass

    def get_variance_value(self):
        pass
