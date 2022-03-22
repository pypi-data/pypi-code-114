# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
from datetime import datetime
from functools import partial
from multiprocessing import Pool

from availsim4core import configuration
from availsim4core.src.analysis import Analysis
from availsim4core.src.reader.xlsx.simulation_reader import SimulationReader
from availsim4core.src.reader.xlsx.system_template_reader import SystemTemplateReader
from availsim4core.src.runner.htcondor_runner import HTCondorRunner
from availsim4core.src.runner.local_runner import LocalRunner
from availsim4core.src.sensitivity_analysis.sensitivity_analysis import SensitivityAnalysis


def start(path_simulation: str,
          path_system: str,
          path_sensitivity_analysis: str,
          output_folder: str,
          HTCondor: bool = False,
          HTCondor_extra_argument: str = "",
          nb_processes: int = 1,
          custom_children_logic_path: str = None):
    """
    Starts the availsim simulation.
    If `HTCondor` is true it starts the software on the HTCondor cluster.
    """

    initial_simulation = SimulationReader.generate_simulation(path_simulation)

    initial_system_template = SystemTemplateReader.generate_system_template(path_system,
                                                                            custom_children_logic_path)

    analysis_list = [Analysis(0,
                              initial_system_template,
                              initial_simulation)]

    if path_sensitivity_analysis:
        # init the list of systems to be simulated

        sensitivity_analysis = SensitivityAnalysis(initial_simulation, initial_system_template)
        analysis_list = sensitivity_analysis.generate_analysis_list(path_sensitivity_analysis)

    if HTCondor:
        HTCondorRunner.run(output_folder,
                           analysis_list,
                           HTCondor_extra_argument)
    else:
        if nb_processes == 1:
            for analysis in analysis_list:
                LocalRunner.run(output_folder,
                                analysis)
        else:
            partial_function = partial(LocalRunner.run,
                                       output_folder)
            with Pool(processes=nb_processes) as pool:
                pool.map(partial_function, analysis_list)


def main():
    """
    Entry point of Availsim.
    """

    (simulation,
     system,
     sensitivity_analysis,
     output_folder,
     HTCondor,
     HTCondor_extra_argument,
     nb_processes,
     custom_children_logic_path) = configuration.init()

    logging.info(f"- Start simulating -")

    start_time = datetime.now()

    start(simulation,
          system,
          sensitivity_analysis,
          output_folder,
          HTCondor,
          HTCondor_extra_argument,
          nb_processes,
          custom_children_logic_path)

    execution_time = (datetime.now() - start_time).total_seconds()
    logging.info(f"Total Availsim execution time: {execution_time:.2f} s")
