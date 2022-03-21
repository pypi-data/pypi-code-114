# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from availsim4core.src.reader.xlsx.monte_carlo_reader import MonteCarloReader
from availsim4core.src.reader.xlsx.monte_carlo_reader import SimulationMonteCarloColumn
from availsim4core.src.simulation.splitting_mc import SplittingMonteCarlo

class SimulationSplittingMonteCarloColumn:
    SYSTEM_ROOT_COMPONENT = "SYSTEM_ROOT_COMPONENT"


class SplittingMonteCarloReader(MonteCarloReader):
    """
    Specific reader for the MonteCarlo simulation.
    """

    @classmethod
    def build(cls, simulation_parameters):
        return SplittingMonteCarlo(
            simulation_parameters[SimulationMonteCarloColumn.MINIMUM_NUMBER_OF_SIMULATION],
            simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_NUMBER_OF_SIMULATION],
            simulation_parameters[SimulationMonteCarloColumn.CONVERGENCE_MARGIN],
            simulation_parameters[SimulationMonteCarloColumn.MAXIMUM_EXECUTION_TIME],
            simulation_parameters[SimulationMonteCarloColumn.SEED],
            cls.extract_from_str_list(simulation_parameters[SimulationMonteCarloColumn.DIAGNOSTICS]),
            simulation_parameters[SimulationMonteCarloColumn.DURATION], 
            cls.clean_cell_str_else_raise(simulation_parameters[SimulationSplittingMonteCarloColumn.SYSTEM_ROOT_COMPONENT],
                                          exception_message_hint='simulation file'))