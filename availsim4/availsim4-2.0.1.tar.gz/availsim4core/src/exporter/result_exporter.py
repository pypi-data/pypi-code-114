# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import pandas

from openpyxl import load_workbook
from availsim4core.src.analysis import Analysis
from availsim4core.src.context.context import Context
from availsim4core.src.results.results import Results


class ResultExporter:
    """
    Interface to define the exporter api for each .
    """

    OUTPUT_FILE_TEMPLATE = '{}simulation_result_{}_{}.xlsx'

    @classmethod
    def export(cls,
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
        pass

    @classmethod
    def open_workbook(cls,
                      output_file):
        """
        Function checking if the output file already exists and returning a writer
        :param output_file: name of the output file
        :return writer: object allowing to write sheets into an excel file using dataframe as the source of data
        """

        try:
            preexisting_data = load_workbook(output_file)
        except FileNotFoundError:
            preexisting_data = None

        writer = pandas.ExcelWriter(output_file, engine='openpyxl')

        if preexisting_data is not None:
            writer.book = preexisting_data

        return writer