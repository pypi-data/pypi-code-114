# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import Dict

from availsim4core.src.reader.xlsx.monte_carlo_reader import MonteCarloReader
from availsim4core.src.reader.xlsx.monte_carlo_reader import SimulationMonteCarloColumn
from availsim4core.src.simulation.quasi_monte_carlo import QuasiMonteCarlo


class QuasiMonteCarloReader(MonteCarloReader):
    """
    Specific reader for the Quasi-Monte Carlo simulation.
    """

    @classmethod
    def build(cls, simulation_parameters: Dict):
        return QuasiMonteCarlo(
            int(simulation_parameters[SimulationMonteCarloColumn.MINIMUM_NUMBER_OF_SIMULATION]),
            int(simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_NUMBER_OF_SIMULATION]),
            float(simulation_parameters[SimulationMonteCarloColumn.CONVERGENCE_MARGIN]),
            float(simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_EXECUTION_TIME]),
            int(simulation_parameters[SimulationMonteCarloColumn.SEED]),
            cls.extract_from_str_list(simulation_parameters[SimulationMonteCarloColumn.DIAGNOSTICS]),
            float(simulation_parameters[SimulationMonteCarloColumn.DURATION])
        )