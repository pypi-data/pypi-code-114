# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
import pandas as pd

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.results.results import Results
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.statistics.critical_failure_paths import CriticalFailurePaths


class XLSXResultsExporterCriticalFailurePaths(ResultExporter):

    def __init__(self, root_component_for_the_analysis: str):
        self.root_component_for_the_analysis = root_component_for_the_analysis

    def export(self,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str):
        f"""
        Exports results.
        :param context {Context} of the result to export.
        :param output_folder folder to export result.
        :param analysis {Analysis} the analysis which have been proceed.
        :param results {Results} the simulation results.
        :param execution_time time of the simulation.
        :param unique_output_file_identifier_str to uniquely identify group of output files. Currently the date/time at exporting is used as a label.
        """
        output_file = ResultExporter.OUTPUT_FILE_TEMPLATE.format(output_folder, analysis.id, unique_output_file_identifier_str)
        writer = ResultExporter.open_workbook(output_file)

        logging.info(f"Exporting the critical failure path from the node {self.root_component_for_the_analysis}")
        cfp = CriticalFailurePaths(context, self.root_component_for_the_analysis)
        critical_failure_paths_names = []
        for path in cfp.critical_failure_paths:
            path_names = []
            for component in path:
                #TODO add some information about the failure mode ? (blind, dectable etc ?) or forcing an additional
                # export with this information, like the list of component export ?
                path_names.append(
                    f"{component.name}_{component.local_id}_{component.global_id}"
                )
            critical_failure_paths_names.append(path_names)

        cfp_df = pd.DataFrame(critical_failure_paths_names)
        cfp_df.to_excel(writer, sheet_name='RESULTS_CRITICAL_FAILURE_PATHS', index=False)
        writer.save()
