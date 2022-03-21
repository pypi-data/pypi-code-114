from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, ClassVar, DefaultDict, Dict, Iterator, List, Tuple, Set
from abc import ABC, abstractmethod
from enum import Enum
from functools import reduce

from igi_gc_reader.reader.excel_address import ExcelAddress, col_index_to_letter, col_letter_to_index
from igi_gc_reader.reader.excel_reader import IExcelReader, has_value
from igi_gc_reader.reader.classification import GcFileClass
from igi_gc_reader.utils import gc_logger


@dataclass
class GcPageData:
    """Can represent a single page or merged pages."""
    page_no: str
    headers: List[str] = field(default_factory=list)
    data_rows: List[List[Any]] = field(default_factory=list)

    def has_data(self) -> bool:
        return any(self.data_rows)


@dataclass  # type: ignore
class IGcPageReader(ABC):
    _xl_reader: IExcelReader

    @abstractmethod
    def get_pages(self) -> Iterator[GcPageData]:
        pass


class PagePhase(Enum):
    Seeking = 1
    InPageMetadata = 2
    BetweenMetadataAndHeaders = 3
    InPageHeaders = 4
    InPageData = 5


# TODO - (MAYBE) Consider changing to a pattern where 
#        we have an IPageState abstract class and a subclass for each state:

# IPageState(xl_reader, page_data):
#   def transition(row) -> phase  # switch to alt state if transition criteria is detected
#   def process(row)

# then just go through states for each row and call transition (and process if no transition)


# See readme.md at top level dir for overview of page handling logic
# --- ---------
@dataclass
class GcPageClassOneReader(IGcPageReader):
    _xl_reader: IExcelReader
    header_cols: List[str] = field(default_factory=list)  # assume data uses same cols for now
    expected_metadata_headers: ClassVar[Set[str]] = {'Company:', 'Well Name:', 'Depth:', 
                                                      'Sampling Point:'}
    page_start_col: ClassVar[str] = 'A'
    post_data_headers: ClassVar[Set[str]] = {  # use as an indicator to stop
        'Miscellaneous Ratios', 'Carbon Number Distribution', 'Parameter'}
    start_page_search_from_row: ClassVar[int] = 40
    max_cols: ClassVar[int] = 60  # look for headers in all columns up to this
    end_after_n_empty_rows: ClassVar[int] = 100
    n_empty_cols_for_row: ClassVar[int] = 10  # treat the row as empty if first n cols are
    max_rows: ClassVar[int] = 3000  # ensure an error doesn't lead to infinite loop!

    def get_pages(self) -> Iterator[GcPageData]:
        found_start = False  # not unique to each page (set once for all)
        page_no = 1
        consecutive_empty_rows = 0
        header_row_num = 0
        phase = PagePhase.Seeking
        current_page = GcPageData(str(page_no))
        header_col_to_values: DefaultDict[str, List[str]] = defaultdict(list)
        data_row_col_pair_to_value: Dict[Tuple[int, str], Any] = {}

        # 3 stopping conditions as of 05/07/2021:
        #   1) Hit >= n empty rows consecutively (after finding start of data pages)
        #      (n configured as ClassVar with {n_empty_cols_for_row})
        #   2) Detected a head for ignored data at end e.g. derived data. This is 
        #      a backup for in case there is not a large gap from end of last data page
        #      (configured as ClassVar: {post_data_headers})
        #   3) Fallback - set a max num rows just incase of a logical error or unexpected
        #      file format to prevent possible infinite loop.
        #      (max rows configured as ClassVar: {max_rows})
        for row in range(self.start_page_search_from_row, self.max_rows):  # end cond 3: max rows
            is_empty_row = self.is_empty_row(row)
            consecutive_empty_rows = consecutive_empty_rows + 1 if is_empty_row else 0

            if consecutive_empty_rows >= self.end_after_n_empty_rows and found_start:
                self.add_data_rows(current_page, data_row_col_pair_to_value)
                if current_page.has_data():
                    yield current_page
                return  # end cond 1: n consecutive empty rows

            # phase 1
            if phase == PagePhase.Seeking:
                if not is_empty_row and self.is_start_of_new_page(row):
                    found_start = True
                    phase = PagePhase.InPageMetadata

            # phase 2
            if phase == PagePhase.InPageMetadata:
                if is_empty_row:
                    phase = PagePhase.BetweenMetadataAndHeaders

            # phase 3
            if phase == PagePhase.BetweenMetadataAndHeaders:
                if not is_empty_row:
                    phase = PagePhase.InPageHeaders
                    header_row_num = 1

            # phase 4
            if phase == PagePhase.InPageHeaders:
                if header_row_num <= 2:
                    for col, val in self.get_col_value_pairs(row):
                        # handle header row 2 slight misalignment if needed...
                        col = self.adj_col_for_off_by_ones(header_row_num, 
                                                           header_col_to_values, col, val)
                        header_col_to_values[col].append(str(val))
                        if val in self.post_data_headers:
                            return  # end cond 2: into derived data (last data page already returned)
                    header_row_num += 1  
                else:
                    phase = PagePhase.InPageData

                    # add headers to current page (all values for each col to handle multi row)
                    for col, values in sorted(header_col_to_values.items(), 
                                              key=lambda kvp: col_letter_to_index(kvp[0])):
                        header = " ".join(values)
                        current_page.headers.append(header)

                    header_row_num = 0  # reset
                    header_col_to_values = defaultdict(list)  # reset

            # phase 5
            if phase == PagePhase.InPageData:
                is_new_page = self.is_start_of_new_page(row) 
                if is_empty_row or self.is_subheading(row):
                    continue
                if is_new_page:
                    if is_new_page:
                        phase = PagePhase.InPageMetadata
                    else:
                        phase = PagePhase.Seeking

                    self.add_data_rows(current_page, data_row_col_pair_to_value)

                    # return current page
                    yield current_page
                    page_no += 1
                    current_page = GcPageData(str(page_no))  # reset
                    data_row_col_pair_to_value = {}  # reset
                    continue

                for col, val in self.get_col_value_pairs(row):
                    data_row_col_pair_to_value[(row, col)] = val

    def is_empty_row(self, row: int):
        check_cols = [col_index_to_letter(i) for i in range(0, self.n_empty_cols_for_row)]
        return not any(has_value(self.read(col, row)) for col in check_cols)

    def read(self, col: str, row: int) -> Any:
        return self._xl_reader.read_cell(ExcelAddress(f"{col}{row}"))

    def is_start_of_new_page(self, row: int) -> bool:
        col_a_cleaned = str(self.read(col=self.page_start_col, row=row)).strip()
        return col_a_cleaned in self.expected_metadata_headers

    def is_subheading(self, row: int) -> bool:
        """
        Example subheadings seen in GCMSMS file provided by Paul: 
        `330.3®217.2: Internal Standard`. All examples seen only have a value in col A.
        """        
        col_value_pairs = self.get_col_value_pairs(row)
        col_A_has_value = next(col_value_pairs)[0] == 'A'
        any_other_values = any(col_value_pairs)  # any left after taking element above?
        return col_A_has_value and not any_other_values

    def get_col_value_pairs(self, row: int) -> Iterator[Tuple[str, Any]]:
        """
        Return all none empty values in row as col, value pairs.
        """
        for col_idx in range(self.max_cols):
            col = col_index_to_letter(col_idx)
            val = self.read(col, row)
            if has_value(val):
                yield col, val

    def add_data_rows(self, page: GcPageData, 
                      data_row_col_pair_to_value: Dict[Tuple[int, str], Any]) -> None:
        cols = set([c for _, c in data_row_col_pair_to_value.keys()])
        ordered_cols = sorted(cols, key=lambda col: col_letter_to_index(col))
        ordered_rows = sorted(set([r for r, _ in data_row_col_pair_to_value.keys()]))
        for r in ordered_rows:
            data_row = []
            for c in ordered_cols:
                # need to incl empties so that data lines up with headers
                # TODO: Still some risk of misalignment e.g. if one col has no values
                #       the trouble is that the header cols don't align with the values
                #       precisely (e.g. val is merged group starting one col before header col)
                #       If we get issue above could match val cols to head cols by proximity 😩
                val = data_row_col_pair_to_value.get((r, c))
                data_row.append(val)
            page.data_rows.append(data_row)

    def adj_col_for_off_by_ones(self, header_row_num, header_col_to_values, col, val):
        """
        Row 2 headers can sometimes align visually, but use a column that is off by
        one relative to the row above. If one header row 2 and the col with a value
        is not in the row 1 cols, assign to one +/- 1 col if found.
        """
        # handle off by one alignment issues i.e. col is +/- 1 on 2nd header row
        if header_row_num == 2:
            if col not in header_col_to_values:
                this_col_idx = col_letter_to_index(col)
                col_dist_pairs = [(c, abs(this_col_idx - col_letter_to_index(c)))
                                                  for c in header_col_to_values]
                off_by_ones = list(filter(lambda p: p[1] == 1, col_dist_pairs))
                if len(off_by_ones) == 1:
                    col = off_by_ones[0][0]  # correct column to match from row1
                if len(off_by_ones) > 1:
                    gc_logger.warning(f"Row 2 header {val} in col {col} does not align "
                         f"with row 1. Multiple row 1 matches were close: {off_by_ones}, "
                         f"left unchanged as it is not clear which it should join with.")
        return col
            

def get_page_reader(xl_reader: IExcelReader, file_class: GcFileClass) -> IGcPageReader:
    if file_class == GcFileClass.One:
        return GcPageClassOneReader(xl_reader)
    raise NotImplementedError()   


def merge_pages(pages: List[GcPageData]) -> GcPageData:

    def merge_two(p1: GcPageData, p2: GcPageData) -> GcPageData:
        if p1.headers != p2.headers:
            raise ValueError(f"Expected headers to be the same, but page {p2.page_no} has different "
                            f"headers.\nPage {p2.page_no}: {p2.headers}, first page: {p1.headers}.")
        p1.page_no += f",{p2.page_no}"
        p1.data_rows = p1.data_rows + p2.data_rows
        return p1

    return reduce(merge_two, pages)


def get_page_data(xl_reader: IExcelReader, file_class: GcFileClass) -> GcPageData:
    gc_logger.info("  getting page data...")
    page_reader = get_page_reader(xl_reader, file_class)
    pages = list(page_reader.get_pages())
    if not pages:
        raise StopIteration("No page data found for file.")
    gc_logger.info(f"  found {len(pages)} pages of GC data.")
    return merge_pages(pages)
