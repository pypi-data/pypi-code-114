# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterComponentTreeSimple(ResultExporter):
    @classmethod
    def export(cls,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str: str):

        def component_tree_simple_export(component: Component, level=0):
            """
            Function recursively exploring the system in order to build a graphical representation of the system.
            This "simple" version of the tree exporter provides a "light" output. A "extended" version exists too.
            The function is called on the root component. Then if a component has children, it is called again for its
            children.
            """

            # line printed in the output for the current component
            ret = (f";" * (level) +
                   f"{component.name}_{component.local_id}_{component.global_id}\n")

            # if that component has children (then it is a Compound type), apply the same function to the children
            if component.get_children():
                for child in component._children:
                    ret += component_tree_simple_export(child,level + 1)

            return ret

        output_file = cls.OUTPUT_FILE_TEMPLATE.format(output_folder, analysis.id, unique_output_file_identifier_str)
        writer = ResultExporter.open_workbook(output_file)

        tree_string = component_tree_simple_export(context.root_component)

        tree_dataframe = pandas.DataFrame([x.split(';') for x in tree_string.split('\n')])

        tree_dataframe.to_excel(writer, sheet_name='RESULTS_COMPONENT_TREE_SIMPLE', index=False)

        writer.save()

