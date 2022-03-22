# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterRCA(ResultExporter):
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

        rca_export = []
        for record in results.root_cause_analysis_record_list:
            rca_export.append({
                "analysis_id": record.simulation_id,
                "timestamp": record.timestamp, 
                "rca_component_trigger": record.rca_trigger_component,
                "rca_status_trigger": record.rca_trigger_status,
                "rca_phase_trigger": record.rca_trigger_phase,
                "rca_event_description": record.description,
                **record.component_statuses_dict
            })
        rca_export_dataframe = pandas.DataFrame(rca_export)
        rca_export_dataframe.to_excel(writer, sheet_name="RESULTS_ROOT_CAUSE_ANALYSIS", index=False)

        writer.save()