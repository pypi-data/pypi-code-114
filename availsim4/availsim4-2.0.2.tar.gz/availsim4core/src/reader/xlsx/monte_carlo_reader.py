# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import Dict

from availsim4core.src.reader.xlsx.xlsx_reader import XLSXReader
from availsim4core.src.simulation.monte_carlo import MonteCarlo


class SimulationMonteCarloColumn:
    MINIMUM_NUMBER_OF_SIMULATION = "MIN_NUMBER_OF_SIMULATION"
    MAXIMUM_NUMBER_OF_SIMULATION = "MAX_NUMBER_OF_SIMULATION"
    CONVERGENCE_MARGIN = "CONVERGENCE_MARGIN"
    MAXIMUM_EXECUTION_TIME = "MAX_EXECUTION_TIME"
    SEED = "SEED"
    DIAGNOSTICS = "DIAGNOSTICS"
    DURATION = "SIMULATION_DURATION"


class MonteCarloReader(XLSXReader):
    """
    Specific reader for the MonteCarlo simulation.
    """

    @classmethod
    def build(cls, simulation_parameters: Dict):
        return MonteCarlo(
            int(simulation_parameters[SimulationMonteCarloColumn.MINIMUM_NUMBER_OF_SIMULATION]),
            int(simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_NUMBER_OF_SIMULATION]),
            float(simulation_parameters[SimulationMonteCarloColumn.CONVERGENCE_MARGIN]),
            float(simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_EXECUTION_TIME]),
            int(simulation_parameters[SimulationMonteCarloColumn.SEED]),
            cls.extract_from_str_list(simulation_parameters[SimulationMonteCarloColumn.DIAGNOSTICS]),
            float(simulation_parameters[SimulationMonteCarloColumn.DURATION])
        )