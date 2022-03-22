# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterListing(ResultExporter):

    @staticmethod
    def component_listing_export(root_component: Component):
        """
        Function exploring the system in order to build a list of components in the system.
        """

        ret = ""

        for component in root_component.to_set():

            if component.get_children():
                # if that component has children (then it is a Compound type), apply the same function to the children
                ret += f"{component.name};{component.local_id};{component.global_id}; compound;" \
                       f" -; -; -; {[x.name for x in component.list_of_mru_trigger]}\n"
            else:
                # else, the current component is a basic and has failure mode(s), those a printed
                ret += f"{component.name};{component.local_id};{component.global_id}; basic;" \
                       f"{component.failure_mode.name}; " \
                       f"{component.failure_mode.failure.type_of_failure}; " \
                       f"{[x.name for x in component.list_of_mru_group]}; " \
                       f"{[x.name for x in component.list_of_mru_trigger]}\n"

        return ret

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

        tree_string = cls.component_listing_export(context.root_component)

        tree_dataframe = pandas.DataFrame([x.split(';') for x in tree_string.split('\n')],columns=[
            "COMPONENT_NAME", "local_id", "global_id", "COMPONENT_TYPE",
            "FAILURE_MODE_NAME", "TYPE_OF_FAILURE",
            "IN_MRU", "TRIGGER_MRU"
        ])

        tree_dataframe.to_excel(writer, sheet_name='RESULTS_COMPONENT_LISTING', index=False)

        writer.save()