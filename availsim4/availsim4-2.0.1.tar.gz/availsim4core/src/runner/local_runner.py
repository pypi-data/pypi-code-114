# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
from datetime import datetime

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.phase.phase_manager import PhaseManager
from availsim4core.src.context.rca.rca_manager import RootCauseAnalysisManager
from availsim4core.src.context.system.component_tree.component_factory import ComponentFactory
from availsim4core.src.exporter.aggregate_exporter import AggregateExporter


class LocalRunner:
    """
    class used to run simulation on the local machine (where the code is called)
    """

    @staticmethod
    def run(output_folder,
            analysis: Analysis):
        start_time = datetime.now()
        logging.info(f"Starting Analysis {analysis.id}")

        component_factory = ComponentFactory(analysis.system_template)
        root_component = component_factory.build()

        # run a simulation on a given system
        context = Context(root_component,
                          PhaseManager(analysis.system_template.phase_set,
                                       analysis.system_template.phase_jump_trigger_set),
                          RootCauseAnalysisManager(analysis.system_template.root_cause_analysis_trigger_set,
                                                   root_component.to_set()))

        logging.debug(f"Simulation: {str(analysis.simulation)}")
        logging.info(f"System tree: \n{str(root_component)}")
        logging.debug(f"PhaseManager: {str(context.phase_manager)}")

        simulation_results = analysis.simulation.run(context)

        execution_time = (datetime.now() - start_time).total_seconds()
        logging.info(f"Analysis execution time = {execution_time:.2f} s")

        # export results
        AggregateExporter.export(context,
                                 output_folder,
                                 analysis,
                                 simulation_results,
                                 execution_time)
