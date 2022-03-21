from dataclasses import dataclass
from logging import exception
from typing import Iterator, Tuple, Union

from igi_gc_reader.reader.gc_page import GcPageData, get_page_data
from igi_gc_reader.reader.excel_reader import get_excel_reader, IExcelReader
from igi_gc_reader.reader.context_data import ContextData, get_context_data_reader
from igi_gc_reader.reader.classification import GcFileClass, classify
from igi_gc_reader.sample_data import IGIUserFriendlyException
from igi_gc_reader.utils import gc_logger
    

@dataclass(frozen=True)
class GcSheet:
    sheet_name: str
    analysis: str
    analysis_addr: str
    file_class: GcFileClass
    context_data: ContextData
    page_data: GcPageData

    def get_igi_analysis(self):
        """Map from raw analysis text in the sheet to the IGI analysis group."""
        return get_igi_analysis(self.analysis)


def get_igi_analysis(raw_analysis: str) -> str:
    """Map from raw analysis text in the sheet to the IGI analysis group."""
    cleaned = raw_analysis.lower()
    if "msms" in cleaned or "ms-ms" in cleaned:
        return "GCMS-MS"
    if "sat" in cleaned:
        return "Sat-GCMS" if "gcms" in cleaned or "bio" in cleaned else "Sat-GC"
    if "aro" in cleaned: 
        return "Arom-GCMS" if "gcms" in cleaned or "bio" in cleaned else "Arom-GC"
    if "wo" in cleaned or 'whole oil' in cleaned:
        return "WO-GCMS" if "gcms" in cleaned else "WO-GC"
    if "py" in cleaned: 
        return "Py-GC-Extr" if "ext" in cleaned else "Py-GC"
    if "ht" in cleaned or "high temp" in cleaned:
        return "HT-GC"
    if "te" in cleaned or "thermal" in cleaned:
        return "TE-GC"  # TODO - confirm whether "EXTRACT GC" should go to this or WO-GC
    if "gasol" in cleaned: 
        return "Gasol-GC"
    if "diam" in cleaned: 
        return "Diam-GCMS"
    if "pol" in cleaned: 
        return "Pol-GCMS"
    if "mrm" in cleaned: 
        return "MRM-GCMS"
    if "irms" in cleaned: 
        return "GC-IRMS"
    default = "WO-GC"
    gc_logger.warning(f"Failed to map analysis from: {raw_analysis}. Assigned to: {default}.")
    return default


@dataclass
class GcSheetError:
    sheet_name: str
    file_class: GcFileClass
    error: Exception


IGcSheet = Union[GcSheet, GcSheetError]


def build_gc_sheet(xl_reader: IExcelReader, sheet_name: str) -> GcSheet:

    def _get_analysis_and_class(xl_reader: IExcelReader) -> Tuple[GcFileClass, str, str]:
        """Returns tuple of class, analysis and analysis address"""
        result = classify(xl_reader)
        return result.file_class, result.analysis, result.analysis_addr

    gc_logger.info(f"Attempting to read sheet {sheet_name}...")
    file_class, analysis, analysis_addr = _get_analysis_and_class(xl_reader)
    context_data = get_context_data_reader(file_class, xl_reader).get_context_data()
    context_data.set_data_dict(xl_reader)
    page_data = get_page_data(xl_reader, file_class)
    return GcSheet(sheet_name, analysis, analysis_addr, file_class, context_data, page_data)


def get_gc_sheets(wb_path: str) -> Iterator[IGcSheet]:
    xl_reader = get_excel_reader(wb_path)
    for sheet in xl_reader.get_sheet_names():
        xl_reader.set_sheet(sheet)
        gc_sheet = None
        try:
            gc_sheet = build_gc_sheet(xl_reader, sheet)
            yield gc_sheet
        # ignoring these errors allows us to process workbooks with some but not all valid sheets
        except StopIteration as e:  # ignore if not page data
            gc_logger.info(f"  skipping sheet {sheet}: {e}")
        except NotImplementedError as e:  # ignore if not supported class type (handled elsewhere)
            gc_logger.info(f"  skipping sheet {sheet}: {e}")
        except IGIUserFriendlyException as e:  # proceed to next sheet but write error info
            gc_logger.error("  error in sheet {sheet}: {e}")
            cls = gc_sheet.file_class if gc_sheet is not None else GcFileClass.Unclassified
            yield GcSheetError(sheet_name=sheet, file_class=cls, error=e)
    xl_reader.close()
