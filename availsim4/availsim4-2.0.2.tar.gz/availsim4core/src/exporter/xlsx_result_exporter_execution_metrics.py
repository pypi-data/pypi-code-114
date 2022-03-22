# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterExecutionMetrics(ResultExporter):
    """
    class used to export the results of a simulation into an output file
    This exporter is meant to provide a good "summary" of a simulation, not a light report like the exporter LightStudy
    """

    @classmethod
    def export(cls,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str: str):

        output_file = cls.OUTPUT_FILE_TEMPLATE.format(output_folder, analysis.id, unique_output_file_identifier_str)
        writer = ResultExporter.open_workbook(output_file)

        execution_metrics_dict = {"execution_time": execution_time}
        execution_metrics_dict['number_of_DES_simulations_executed'] = str(results.number_of_DES_simulations_executed)
        for key, statistics in results.execution_metrics_statistics.items():
            execution_metrics_dict[key + "_MEAN"] = statistics.mean
            execution_metrics_dict[key + "_MAX"] = statistics.max
            execution_metrics_dict[key + "_STD"] = statistics.std

        number_of_compound_components = 0
        number_of_basic_components = 0

        for component in context.root_component.to_set():
            if component.get_children():
                # if that component has children (then it is a Compound type)
                number_of_compound_components += 1
            else:
                number_of_basic_components += 1

        execution_metrics_dict["number_of_compound_components"] = number_of_compound_components
        execution_metrics_dict["number_of_basic_components"] = number_of_basic_components

        # exporting the execution time and other metric
        execution_metrics_dataframe = pandas.DataFrame(
            execution_metrics_dict,
            index=[0]) # TODO add the number of iteration? number of b events? number of components?
        execution_metrics_dataframe.to_excel(writer, sheet_name='RESULTS_EXECUTION_METRICS', index=False)

        writer.save()