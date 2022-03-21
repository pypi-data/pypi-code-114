from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List
from dataclasses import dataclass, field

from igi_gc_reader.reader.excel_address import ExcelAddress, col_index_to_letter, col_letter_to_index
from igi_gc_reader.reader.excel_reader import IExcelReader


class GcFileClass(Enum):
    One = 1
    #Two = 2
    Unclassified = 99


@dataclass
class AnalysisSearchParams:
    start_col: str = 'AJ'   # lowest seen: AM
    end_col: str = 'BG'     # highest seen: BE
    start_row: int = 1      # rowest seen: 1
    end_row: int = 3        # highest seen: 3


# for some file formats the main data headers start in the first couple of rows
# so just detecting a value e.g. in BE1 isn't enough to classify - we need to know
# whether it is an analysis. examples of analysis I have seen are: "WHOLE OIL GC", 
# "AROMATIC GCMS", "SATURATE GCMS", "Saturate Biomarkers", "AROMATIC BIOMARKERS",
# "Hight Temp GC" and "Extract GC". + Saturate GCMSMS
treat_as_analysis_if_contains = ["gc", "saturate", "arom", "biom", "whole", 'msms']


def is_an_analysis(val: Any) -> bool:
    val = str(val).lower()
    return any(snippet in val for snippet in treat_as_analysis_if_contains)


@dataclass
class IClassification(ABC):
    file_class: GcFileClass
    analysis: str = field(default_factory=lambda: "")
    analysis_addr: str = field(default_factory=lambda: "")

    @abstractmethod
    def is_instance(self, xl_reader: IExcelReader) -> bool:
        pass


# TODO - (MAYBE) *** Future note for classifier ***
#        distinguishing characteristic of this file class seems to be 🤞 the repeating metadata
#        blocks at the top of each page - looking for any of 4 specific headers usually seen in 
#        left metadata column. This could be a useful test when implementing a better classifier!


class ClassificationOne(IClassification):
    file_class: GcFileClass = field(default=GcFileClass.One)

    def is_instance(self, xl_reader: IExcelReader) -> bool:
        start_col_idx = col_letter_to_index(AnalysisSearchParams.start_col)
        end_col_idx = col_letter_to_index(AnalysisSearchParams.end_col)
        for row in range(AnalysisSearchParams.start_row, AnalysisSearchParams.end_row + 1):
            for col_idx in range(start_col_idx, end_col_idx + 1):
                col = col_index_to_letter(col_idx)
                addr = ExcelAddress(f'{col}{row}')
                val = xl_reader.read_cell(addr)
                if is_an_analysis(val):
                    self.analysis = val
                    self.analysis_addr = addr.addr
                    return True
        return False


class NoClassification(IClassification):
    file_class: GcFileClass = field(default=GcFileClass.Unclassified)

    def is_instance(self, _: IExcelReader) -> bool:
        raise NotImplementedError("Rather than calling is_instance - use this class if you "
            "have tried all registered classifiers and found no matches")


registered_classifications: List[IClassification] = [
    ClassificationOne(GcFileClass.One),
    ]


def classify(xl_reader: IExcelReader) -> IClassification:
    for classification in registered_classifications:
        if classification.is_instance(xl_reader):
            return classification
    return NoClassification(file_class=GcFileClass.Unclassified)
