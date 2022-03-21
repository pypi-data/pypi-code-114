# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import copy
import logging
from datetime import datetime

from availsim4core.src.context.context import Context
from availsim4core.src.discrete_event_simulation.discrete_event_simulation import DiscreteEventSimulation
from availsim4core.src.results.simulation_results import SimulationResults
from availsim4core.src.simulation.monte_carlo import MonteCarlo
from availsim4core.src.simulation.des_random_generator.quasi_monte_carlo_generator import QuasiMonteCarloGenerator

from availsim4core.src.context.system.component_tree.basic import Basic
from availsim4core.src.simulation.simulation import SimulationType


class QuasiMonteCarlo(MonteCarlo):
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
    SIMULATION_TYPE = SimulationType.QUASI_MONTE_CARLO


    def run(self, context: Context):
        simulation_results = SimulationResults(self.maximum_number_of_simulations,
                                               self.duration_of_simulation)

        basic_components = [component for component in context.root_component.to_set() if isinstance(component, Basic)]
        qp_sobol = QuasiMonteCarloGenerator(basic_components, self.duration_of_simulation)
        qp_sobol_samples = qp_sobol.generate_samples(self.seed, self.seed+self.maximum_number_of_simulations)
        simulation_weight = 1/self.maximum_number_of_simulations

        for simulation_index in range(0, self.maximum_number_of_simulations):
            start_time = datetime.now()
            logging.info(f"Starting Quasi-Monte Carlo simulation {simulation_index+1} / {self.maximum_number_of_simulations}")

            random_sequence = qp_sobol_samples[simulation_index]
            qp_sobol.set_ttfs_of_failure_modes(random_sequence)

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
