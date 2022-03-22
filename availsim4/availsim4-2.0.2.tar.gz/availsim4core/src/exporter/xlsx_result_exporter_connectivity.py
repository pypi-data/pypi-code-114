# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterConnectivityMatrix(ResultExporter):
    @classmethod
    def export(cls,
               context: Context,
               output_folder: str,
               analysis: Analysis,
               results: Results,
               execution_time: float,
               unique_output_file_identifier_str: str):

        def connectivity_matrix_children_export(root: Component, level=0):
            """
            Function building a matrix with +1 recursively exploring the system in order to build a graphical representation of the system.
            This "extended" version of the tree exporter provides a detailed output. A simple version exists too.
            The function is called on the root component. Then if a component has children, it is called again for its
            children.
            """

            set_of_components = root.to_set()

            ret = ';'

            # header
            for icol, component_col in enumerate(set_of_components):
                ret += f"{component_col.name}_{component_col.local_id}_{component_col.global_id}; "
            ret += '\n'

            for irow, component_row in enumerate(set_of_components):

                # header row wise
                ret += f"{component_row.name}_{component_row.local_id}_{component_row.global_id}; "

                child_list = component_row.get_children()
                parent_list = component_row._parents

                for icol, component_col in enumerate(set_of_components):

                    if component_col in child_list:
                        ret+='1;'
                    elif component_col in parent_list:
                        ret+='-1;'
                    else:
                        ret+='0;'

                ret+='\n'

            return ret

        output_file = cls.OUTPUT_FILE_TEMPLATE.format(output_folder, analysis.id, unique_output_file_identifier_str)
        writer = ResultExporter.open_workbook(output_file)

        connectivity_matrix_string = connectivity_matrix_children_export(context.root_component)

        connectivity_matrix = pandas.DataFrame([x.split(';') for x in connectivity_matrix_string.split('\n')])

        connectivity_matrix.to_excel(writer, sheet_name='RESULTS_CONNECTIVITY_MATRIX', index=False)

        writer.save()