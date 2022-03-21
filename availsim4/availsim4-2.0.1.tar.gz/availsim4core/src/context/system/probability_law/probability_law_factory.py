# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List

from availsim4core.src.context.system.probability_law.deterministic_law import DeterministicLaw
from availsim4core.src.context.system.probability_law.exponential_law import ExponentialLaw
from availsim4core.src.context.system.probability_law.normal_law import NormalLaw
from availsim4core.src.context.system.probability_law.binomial_law import BinomialLaw
from availsim4core.src.context.system.probability_law.weibull_law import WeibullLaw


class ProbabilityLawFactoryError(Exception):
    pass


class ProbabilityLawFactory:

    @staticmethod
    def build(distribution_str,
              parameters: List[float]):

        if distribution_str in ["EXP", "EXPONENTIAL", "EXPONENTIALLAW", "EXPONENTIAL_LAW"]:
            return ExponentialLaw(parameters)
        elif distribution_str in ["NORMAL", "NORMALLAW", "NORMAL_LAW"]:
            return NormalLaw(parameters)
        elif distribution_str in ["FIX", "DETERMINISTIC", "DETERMINISTIC_LAW", "DETERMINISTICLAW"]:
            return DeterministicLaw(parameters)
        elif distribution_str in ["POFOD", "FOD","BINOMIAL", "BINOMIALLAW", "BINOMIAL_LAW"]:
            return BinomialLaw(parameters)
        elif distribution_str in ["WEIBULL", "WEIBULLLAW", "WEIBULL_LAW"]:
            return WeibullLaw(parameters)
        else:
            message_exception = f"wrong type of distribution function: {distribution_str}"
            import logging
            logging.exception(message_exception)
            raise ProbabilityLawFactoryError(message_exception)
