# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
import os
from _datetime import datetime

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.system.system_utils import SystemUtils
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.exporter.xlsx_result_exporter_component_listing import XLSXResultExporterListing
from availsim4core.src.exporter.xlsx_result_exporter_component_tree_extented import \
    XLSXResultExporterComponentTreeExtended
from availsim4core.src.exporter.xlsx_result_exporter_component_tree_simple import XLSXResultExporterComponentTreeSimple
from availsim4core.src.exporter.xlsx_result_exporter_connectivity import XLSXResultExporterConnectivityMatrix
from availsim4core.src.exporter.xlsx_result_exporter_execution_metrics import XLSXResultExporterExecutionMetrics
from availsim4core.src.exporter.xlsx_result_exporter_last_timeline import XLSXResultExporterLastTimeline
from availsim4core.src.exporter.xlsx_result_exporter_summary import XLSXResultExporterSummary
from availsim4core.src.exporter.xlsx_result_exporter_rca import XLSXResultExporterRCA
from availsim4core.src.exporter.xlsx_result_exporter_critical_failure_paths import XLSXResultsExporterCriticalFailurePaths
from availsim4core.src.results.results import Results


class DiagnosticType:
    DIAGNOSTIC_EXPORTER = {
        "EXECUTION_METRICS": XLSXResultExporterExecutionMetrics,
        "SUMMARY": XLSXResultExporterSummary,
        "LAST_TIMELINE": XLSXResultExporterLastTimeline,
        "RCA": XLSXResultExporterRCA,
        "COMPONENT_TREE_SIMPLE": XLSXResultExporterComponentTreeSimple,
        "COMPONENT_TREE_EXTENDED": XLSXResultExporterComponentTreeExtended,
        "CONNECTIVITY_MATRIX": XLSXResultExporterConnectivityMatrix,
        "COMPONENT_LISTING": XLSXResultExporterListing,
        "GRAPH" : None,
        "CRITICAL_FAILURE_PATHS": None,
    }


class AggregateExporter(ResultExporter):
    @classmethod
    def export(cls,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str = None):

        # create the output directory if needed
        os.makedirs(output_folder, exist_ok=True)

        if unique_output_file_identifier_str is None:
            unique_output_file_identifier_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        for diagnostic in analysis.simulation.get_list_of_diagnosis():
            logging.debug(f"Exporting {diagnostic}")

            if diagnostic == "GRAPH":
                # avoiding to import that module if it's not need because that module is a bit exotic
                from availsim4core.src.exporter.xlsx_result_exporter_graph import XLSXResultExporterGraph
                exporter = XLSXResultExporterGraph

            elif "CRITICAL_FAILURE_PATHS" in diagnostic:
                if SystemUtils.is_string_containing_parenthesis(diagnostic):
                    root_component_for_the_analysis = SystemUtils.extract_arguments_within_parenthesis(diagnostic)
                    logging.info(f"The diagnostic CRITICAL_FAILURE_PATHS is performed using the root component "
                                 f"{root_component_for_the_analysis} as provided with the argument {diagnostic}")
                else:
                    root_component_for_the_analysis = context.root_component.name
                    logging.info(f"The diagnostic CRITICAL_FAILURE_PATHS is performed using the root component "
                                 f"{root_component_for_the_analysis} as a default value because no speficic value was "
                                 f"provided with the argument {diagnostic}. This can be performed by adding the name of "
                                 f"the component which should be used as root between parenthesis, such as: "
                                 f"CRITICAL_FAILURE_PATHS(specific_component_name)")

                exporter = XLSXResultsExporterCriticalFailurePaths(root_component_for_the_analysis)

            else:
                exporter = DiagnosticType.DIAGNOSTIC_EXPORTER[diagnostic]

            exporter.export(context,
                            output_folder,
                            analysis,
                            results,
                            execution_time,
                            unique_output_file_identifier_str)


        # Default exporter export last in order to be sure previous exporters had the time to finish properly
        DiagnosticType.DIAGNOSTIC_EXPORTER["EXECUTION_METRICS"].export(context,
                                                                       output_folder,
                                                                       analysis,
                                                                       results,
                                                                       execution_time,
                                                                       unique_output_file_identifier_str)