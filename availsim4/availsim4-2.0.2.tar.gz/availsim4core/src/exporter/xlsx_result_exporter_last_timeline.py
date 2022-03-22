# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.exporter.result_exporter import ResultExporter
from availsim4core.src.results.results import Results


class XLSXResultExporterLastTimeline(ResultExporter):
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

        # convert the last timeline for the conversion into a pandas dataframe
        timeline_export = []
        for record in results.last_simulation_timeline:
            timeline_export.append(
                {"timestamp": record.timestamp,
                 "phase": record.phase.name,
                 "component": record.get_result_record_entry(),
                 "description": record.description}
            )
        timeline_export_dataframe = pandas.DataFrame(timeline_export)
        timeline_export_dataframe.to_excel(writer, sheet_name='RESULTS_LAST_TIMELINE', index=False)

        writer.save()