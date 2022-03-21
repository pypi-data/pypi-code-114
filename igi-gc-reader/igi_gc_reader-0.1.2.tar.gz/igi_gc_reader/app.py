"""
Transform a GC lab Excel file to a format ready for p:IGI+/Metis import. 
"""
from os import stat
from igi_file_transformation_contract import (
    IFileTransformer,
    TransformationResult,
    Status,
    SuccessStatus,
    PLEASE_SUBMIT_MSG,
    IGINoSupportedSheetsException,
)
from typing import List, Optional
from collections import defaultdict
from argparse import ArgumentParser

from igi_gc_reader.reader.classification import GcFileClass
from igi_gc_reader.reader.gc_reader import IGcSheet, get_gc_sheets
from igi_gc_reader.writer import write_sheets
from igi_gc_reader.utils import gc_logger

SUPPORTED_FILE_CLASSES = [GcFileClass.One]
AUTO = "<AutoAssign>"


class GcFileTransformer(IFileTransformer):

    @property
    def title(self) -> str:
        return "GC File Transformation"

    @property
    def user_description(self) -> str:
        return "Upload a GC lab file to get an import file ready for p:IGI+ / Metis Transform."

    @property
    def accepts_file_extensions(self) -> List[str]:
        return ['.xlsx', '.xlsm', '.xls']

    def try_transform_file(self, in_path: str, out_path: str=AUTO) -> TransformationResult:
        """
        Transform GC lab file ready for p:IGI+/Transform import
        Returns: TransformationResult with path to transformed file and status
        """
        try:
            supported_sheets = get_supported_sheets(in_path)
            if (len(supported_sheets) == 0):  # if all sheets are not supported file class...
                err_msg = f"The structure of this file is not currently supported. {PLEASE_SUBMIT_MSG}"
                no_supported_sheets_err = IGINoSupportedSheetsException(err_msg)
                status = Status(success=False, igi_exception=no_supported_sheets_err)
                gc_logger.error(status.failure_message)
                return TransformationResult(status)
            out_path = self.transform_file(in_path, out_path, supported_sheets=supported_sheets)
        
        except Exception as e:  # could have a supported file class but still hit an error....
            status = Status(success=False, igi_exception=e)
            gc_logger.error(status.stack_trace)
            result = TransformationResult(status)
            return result

        result = TransformationResult(SuccessStatus, output_filepath=out_path)
        gc_logger.info(result)
        return result

    def transform_file(self, in_path: str, out_path: str = AUTO, **kwargs) -> str:
        """
        Transform GC lab file ready for p:IGI+/Transform import
        Returns: path to transformed file
        """        
        supported_sheets = kwargs.get("supported_sheets", get_supported_sheets(in_path))
        if out_path == AUTO:
            out_path = self.get_default_output_path(in_path)
        write_sheets(supported_sheets, out_path)
        return out_path

    def pick_and_transform_file(self) -> str:
        """
        Command line option to open file picker to select input file.
        Can also be used if you are using this lib within a Python script.
        For use in a web service use `transform_file` instead.
        """
        import tkinter.filedialog
        import tkinter as tk

        root = tk.Tk()  # to allow file selection dialog
        root.withdraw()  # hide root window
        input_path = tk.filedialog.askopenfilename(
            title="Select GC lab file (Excel)",
            filetypes=[("Excel files", ".xlsx .xls .xls*")],
        )
        return self.transform_file(input_path)

    @property
    def result_disclaimer(self) -> str:
        return (
            "Please check the output. We have tried to interpret the input file and "
            "assign data to appropriate indicators and units of measure. This is challenging "
            "because the headers do not always use the same names or appear in the same "
            "columns.\n\nIn the output file headers repeat in groups - one for each indicator "
            "(e.g., area, height, concentrations from area etc). If you check the first group "
            "after the context headers (well name, depth etc) the same indicators / uoms will "
            "be used for each property after."
        )

    @property
    def result_disclaimer_image_uri(self) -> Optional[str]:
        return "https://i.ibb.co/88vvsPs/disclaimer-example.png"


def get_supported_sheets(in_path: str) -> List[IGcSheet]:
    sheets_by_file_class = defaultdict(list)

    for sheet in get_gc_sheets(in_path):
        sheets_by_file_class[sheet.file_class].append(sheet)

    supported, unsupported = [], []
    for file_class in sheets_by_file_class.keys():  # i.e. if it's in supported classes
        if file_class in SUPPORTED_FILE_CLASSES:
            supported += sheets_by_file_class[file_class]
        else:
            unsupported += sheets_by_file_class[file_class]

    if len(supported) >= 1:
        if len(unsupported) == 0:
            names = [sh.sheet_name for sh in unsupported]
            gc_logger.info(f"Some unsupported sheets found: {names}")
        return supported
    return []


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "-i", dest="input_file_path", type=str, required=False, default=""
    )
    parser.add_argument(
        "-t", dest="use_try_func", type=str, required=False, default="n"
    )
    args = parser.parse_args()
    gc_transformer = GcFileTransformer()
    if not args.input_file_path:
        gc_transformer.pick_and_transform_file()
    else:
        if args.use_try_func.lower()[0] != "n":
            gc_transformer.try_transform_file(args.input_file_path)
        else:
            gc_transformer.transform_file(args.input_file_path)
