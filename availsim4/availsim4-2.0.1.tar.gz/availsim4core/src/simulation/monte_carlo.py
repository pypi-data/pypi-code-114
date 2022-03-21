# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 


import copy
import logging
from datetime import datetime
from typing import List

from availsim4core.src.context.context import Context
from availsim4core.src.discrete_event_simulation.discrete_event_simulation import DiscreteEventSimulation
from availsim4core.src.results.simulation_results import SimulationResults
from availsim4core.src.simulation.simulation import Simulation, SimulationType


class MonteCarlo(Simulation):
    """
    Defines a MonteCarlo simulation that will be triggered by the Sensitivity Analysis.
    Attributes:
    - minimum_number_of_simulations: minimun number of call to discrete event simulation.
    - maximum_number_of_simulations: maximun number of call to discrete event simulation.
    - convergence_margin: Evaluate on the fly the appropriate number of simulation to run.
    - maximum_execution_time: used on the Cluster to stop the simulation after this period of time.
    - seed: Control the random generator to get different values over each simulation. Deterministic approach.
    - list_of_diagnosis: Defines the metrics to compute.
    - result_simulation: The ResultSimulation to return.
    Extends the simulation, by implementing the run() method.
    """
    SIMULATION_TYPE = SimulationType.MONTE_CARLO

    def __init__(self,
                 minimum_number_of_simulations: int,
                 maximum_number_of_simulations: int,
                 convergence_margin: float,
                 maximum_execution_time: float,
                 seed: int,
                 list_of_diagnosis: List[str],
                 duration_of_simulation: float):
        self.minimum_number_of_simulations = minimum_number_of_simulations
        self.maximum_number_of_simulations = maximum_number_of_simulations
        self.convergence_margin = convergence_margin
        self.maximum_execution_time = maximum_execution_time
        self.seed = seed
        self.list_of_diagnosis = list_of_diagnosis
        self.duration_of_simulation = duration_of_simulation

    def __str__(self):
        return f"{self.SIMULATION_TYPE}:: " \
               f"minimum_number_of_simulations: {self.minimum_number_of_simulations} - " \
               f"maximum_number_of_simulations: {self.maximum_number_of_simulations} - " \
               f"maximum_execution_time: {self.maximum_execution_time} - " \
               f"diagnostics: {self.list_of_diagnosis} - " \
               f"seed: {self.seed} - " \
               f"duration_of_simulation: {self.duration_of_simulation}"

    def __eq__(self, other):
        return self.minimum_number_of_simulations == other.minimum_number_of_simulations \
               and self.maximum_number_of_simulations == other.maximum_number_of_simulations \
               and self.convergence_margin == other.convergence_margin \
               and self.maximum_execution_time == other.maximum_execution_time \
               and self.seed == other.seed \
               and self.list_of_diagnosis == other.list_of_diagnosis \
               and self.duration_of_simulation == other.duration_of_simulation


    def update_statistics(self, simulation_results: SimulationResults, simulation_des, start_time, simulation_weight: float, recursion_depth):
        """
        Function called after each iteration of the Monte Carlo algorithm to update the statistics incrementally
        :param simulation_results:
        :param simulation_des:
        :param start_time:
        :param simulation_index:
        :return:
        """
        simulation_results.update_with_des_results(simulation_des.execution_metrics,
                                        simulation_des.context.timeline_record,
                                        simulation_weight)
        execution_time = (datetime.now() - start_time).total_seconds()
        # logging.info(f"DES simulation completed in: {execution_time:.2f} s; ")
        simulation_results.root_cause_analysis_record_list.extend(simulation_des.context.rca_manager.root_cause_analysis_record_list)
        if recursion_depth not in simulation_results.number_of_DES_simulations_executed:
            simulation_results.number_of_DES_simulations_executed[recursion_depth] = 0
        simulation_results.number_of_DES_simulations_executed[recursion_depth] += 1

    def run(self, context: Context):
        simulation_results = SimulationResults(self.maximum_number_of_simulations,
                                    self.duration_of_simulation)
        simulation_weight = 1/self.maximum_number_of_simulations

        for simulation_index in range(0, self.maximum_number_of_simulations):
            start_time = datetime.now()
            logging.info(f"Starting Monte Carlo simulation {simulation_index+1} / {self.maximum_number_of_simulations}")

            local_context = copy.deepcopy(context)
            # initialisation of a DES
            simulation_des = DiscreteEventSimulation(self.seed + simulation_index,
                                                     self.duration_of_simulation,
                                                     local_context, None, -1 , 0)

            # simulation
            _, _ = simulation_des.run()
            timeline_record = local_context.timeline_record

            # updating statistics
            self.update_statistics(simulation_results,
                                   simulation_des,
                                   start_time,
                                   simulation_weight,
                                   0)


        simulation_results.evaluate_result()
        simulation_results.last_simulation_timeline = timeline_record.record_list
        return simulation_results

    def get_list_of_diagnosis(self):
        return self.list_of_diagnosis
