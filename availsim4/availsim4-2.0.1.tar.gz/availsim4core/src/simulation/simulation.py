# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List

from availsim4core.src.context.context import Context
from availsim4core.src.results.results import Results


class SimulationType:
    MONTE_CARLO = "MONTE_CARLO"
    QUASI_MONTE_CARLO = "QUASI_MONTE_CARLO"
    SPLITTING_MONTE_CARLO = "SPLITTING_MONTE_CARLO"


class Simulation:
    """
    Defines a simulation that will be triggered by the Sensitivity Analysis.
    When a simulation is ran, it returns a ResultSimulation.
    """

    def run(self, context: Context) -> Results:
        """
        Run a simulation against a given Component tree by calling multiple Discrete event Simulations.
        """
        pass

    def get_list_of_diagnosis(self) -> List[str]:
        """
        Get a simulation's list of diagnosis for the exporter
        """
        pass
