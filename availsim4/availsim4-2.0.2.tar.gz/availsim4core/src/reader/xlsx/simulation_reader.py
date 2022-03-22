# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging

from availsim4core.src.context.system.system_utils import SystemUtils
from availsim4core.src.reader.xlsx.monte_carlo_reader import MonteCarloReader
from availsim4core.src.reader.xlsx.quasi_monte_carlo_reader import QuasiMonteCarloReader
from availsim4core.src.reader.xlsx.splitting_monte_carlo_reader import SplittingMonteCarloReader
from availsim4core.src.reader.xlsx.xlsx_reader import XLSXReader
from availsim4core.src.simulation.simulation import SimulationType
from availsim4core.src.statistics.critical_failure_paths import CriticalFailurePaths


class SimulationNotFoundError(Exception):
    pass

class DiagnosticNotFoundError(Exception):
    pass


class SimulationSheet:
    SHEET = "SIMULATION"
    TYPE = "SIMULATION_TYPE"


class SimulationReader(XLSXReader):

    @classmethod
    def generate_simulation(cls, simulation_file_path):
        """
        Generate a simulation based on the given XLSX file path.
        :param simulation_file_path: path to the XLSX file with the simulation configuration.
        """

        initial_simulation_dictionary = cls.read(simulation_file_path)

        simulation_parameters = initial_simulation_dictionary[SimulationSheet.SHEET][0]
        simulation_type = simulation_parameters[SimulationSheet.TYPE]
        logging.debug(f"Reading simulation = {simulation_type}")

        if SimulationType.MONTE_CARLO == simulation_type:    
            simulation = MonteCarloReader.build(simulation_parameters)
        elif SimulationType.QUASI_MONTE_CARLO == simulation_type:
            simulation = QuasiMonteCarloReader.build(simulation_parameters)
        elif SimulationType.SPLITTING_MONTE_CARLO == simulation_type:
            simulation = SplittingMonteCarloReader.build(simulation_parameters)
        else:
            message_exception = f"Simulation {simulation_type} not found"
            logging.exception(message_exception)
            raise SimulationNotFoundError(message_exception)

        for diagnostic in simulation.list_of_diagnosis:
            from availsim4core.src.exporter.aggregate_exporter import DiagnosticType
            if diagnostic not in DiagnosticType.DIAGNOSTIC_EXPORTER.keys():
                if "CRITICAL_FAILURE_PATHS" in diagnostic:
                    # the CRITICAL_FAILURE_PATHS diagnostic could have an argument between parenthesis such as:
                    # CRITICAL_FAILURE_PATHS(specific_component_name)
                    pass
                else:
                    message_exception = f"Diagnostic {diagnostic} not found in the predefined diagnosis"
                    logging.exception(message_exception)
                    raise DiagnosticNotFoundError(message_exception)

        return simulation
