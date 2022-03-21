# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterComponentTreeExtended(ResultExporter):
    @classmethod
    def export(cls,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str: str):

        def component_tree_extended_export(component: Component, level=0):
            """
            Function recursively exploring the system in order to build a graphical representation of the system.
            This "extended" version of the tree exporter provides a detailed output. A simple version exists too.
            The function is called on the root component. Then if a component has children, it is called again for its
            children.
            """

            # Variable used to get the logic between the parent of the current component and the current component.
            # It is possible that a component has several parents if it's a "shared child".
            dict_of_children_logic = {}
            for parent in component.get_parents():
                dict_of_children_logic[parent.__repr__()] = parent.children_logic

            if level == 0:
                # if level ==0, then the current component is the root component, it has no parent,
                # only a "light" string is used to described the component
                ret = (f";" * (level) +
                       f"{component.name}_{component.local_id}_{component.global_id}; ROOT COMPONENT HAS NO PARENT \n")
            else:
                # else, the current component has some parent(s),
                # a more detailed string is used, with logic applied by its parent(s)
                ret = (f";" * (level - 1) + f"logic = {dict_of_children_logic};"
                                            f"{component.name}_{component.local_id}_{component.global_id}; parents = {component.get_parents()} \n")

            if component.get_children():
                # if that component has children (then it is a Compound type), apply the same function to the children
                for child in component._children:
                    ret += component_tree_extended_export(child,level + 1)
            else:
                # else, the current component is a basic and has failure mode(s), those a printed
                ret += (f";" * (level + 1) +
                        f"failure mode = {component.failure_mode}\n")

            return ret

        output_file = cls.OUTPUT_FILE_TEMPLATE.format(output_folder, analysis.id, unique_output_file_identifier_str)
        writer = ResultExporter.open_workbook(output_file)

        tree_string = component_tree_extended_export(context.root_component)

        tree_dataframe = pandas.DataFrame([x.split(';') for x in tree_string.split('\n')])

        tree_dataframe.to_excel(writer, sheet_name='RESULTS_COMPONENT_TREE_EXTENDED', index=False)

        writer.save()