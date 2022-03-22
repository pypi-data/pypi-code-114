from dataclasses import dataclass, field
from typing import Iterator, Optional, DefaultDict, List, Any, Tuple
from collections import defaultdict
from igi_file_transformation_contract import IGIUserFriendlyException

from igi_gc_reader.reader.gc_page import GcPageData
from igi_gc_reader.utils import get_ordinal, gc_logger


class ColumnAlignmentException(IGIUserFriendlyException):
    pass


@dataclass
class TargetHeaders:
    a: str
    h: str
    ca: str
    ch: str


@dataclass
class SourceColumnNames:
    prop: str = field(default="")
    prop_desc: str = field(default="")
    a: str = field(default="")
    h: str = field(default="")
    ca: str = field(default="")
    ch: str = field(default="")
    ion: Optional[str] = field(default=None)

    def get_target_headers(self, prop_val: str, igi_analysis: str = "WO-GC") -> TargetHeaders:
        return TargetHeaders(
            a=f"{prop_val}[a].{igi_analysis}<count>",
            h=f"{prop_val}[h].{igi_analysis}<count>",
            ca=f"{prop_val}[ca].{igi_analysis}<{self.get_ca_uom()}>",
            ch=f"{prop_val}[ch].{igi_analysis}<{self.get_ch_uom()}>"
        )

    def get_ca_uom(self) -> str:
        return self.clean(self.ca, rmv=["area", "(", ")"])

    def get_ch_uom(self) -> str:
        return self.clean(self.ch, rmv=["height", "hght", "(", ")"])

    def clean(self, val: str, rmv: List[str]) -> str:
        val = val.lower()
        for rm in rmv:
            val = val.replace(rm, "")
        return val.strip()


Row = List[Any]


@dataclass
class SampleData:
    """Page data restructured as a single sample row."""
    page_data: GcPageData
    igi_analysis: str
    _col_head_to_values: DefaultDict[str, Row] = field(
        default_factory=lambda: defaultdict(list))
    _page_data_cols: SourceColumnNames = field(init=False)

    def __post_init__(self):
        heads = self.page_data.headers
        for row in self.page_data.data_rows:
            if len(heads) != len(row):
                msg_suffix = ""  # rows without the issue with have `None` added, in case this 
                                 # row is one of those, look for examples with more values
                if len(row) > len(heads):
                    row_with_most_values, idx = self._get_row_with_most_values()
                    nth_row = get_ordinal(idx+1)
                    msg_suffix = (f"Example row with more values ({nth_row} GC data row): \n"
                        f"{row_with_most_values}. You may need to unmerge cells to see this "
                        f"in the source spreadsheet, then remove redundant values to fix.")

                msg =(f"{len(heads)} header columns, not equal to {len(row)} values in row. "
                    f"This could be due to merged cells that contain multiple values. \n"
                    f"Headers: {heads} \n{msg_suffix}")
                raise ColumnAlignmentException(msg)
            for head, val in zip(heads, row):
                self._col_head_to_values[head].append(val)
        self._page_data_cols = self.interpret_columns()

    def get_headers(self) -> Iterator[Tuple[str, Optional[str]]]:
        cols = self._page_data_cols
        ions = self._col_head_to_values[cols.ion] if cols.ion else [
            None for _ in self._col_head_to_values[cols.prop]]
        for prop_value, prop_desc, ion in zip(self._col_head_to_values[cols.prop],
                                              self._col_head_to_values[cols.prop_desc],
                                              ions):
            use_prop = prop_value if prop_value else prop_desc
            target_headers = cols.get_target_headers(use_prop, self.igi_analysis)
            if self._page_data_cols.a:
                yield target_headers.a, ion
            if self._page_data_cols.h:
                yield target_headers.h, ion
            if self._page_data_cols.ca:
                yield target_headers.ca, ion
            if self._page_data_cols.ch:
                yield target_headers.ch, ion

    def get_sample_row(self) -> Iterator[str]:
        cols = self._page_data_cols
        d = self._col_head_to_values
        indicators_with_data = []
        if cols.a:
            indicators_with_data.append(d[cols.a])
        if cols.h:
            indicators_with_data.append(d[cols.h])
        if cols.ca:
            indicators_with_data.append(d[cols.ca])
        if cols.ch:
            indicators_with_data.append(d[cols.ch])

        for property in zip(*indicators_with_data):
            for indicator in property:
                yield indicator

    @property
    def n_header_rows(self) -> int:
        return 2 if self._page_data_cols.ion is not None else 1

    def interpret_columns(self) -> SourceColumnNames:
        """
        Used to decide how we interpret columns in the source data, which we use for
        the property, and which are assigned to each indicator.
        """
        cols = SourceColumnNames()
        heads = self.page_data.headers
        for head in heads:
            formatted_header = head.lower()
            if formatted_header == "ion":
                cols.ion = head
            elif formatted_header.startswith("peak"):
                cols.prop = head
            elif formatted_header.startswith("compound"):
                cols.prop_desc = head
            elif formatted_header.startswith("ret") and formatted_header.endswith("time"):
                continue
            elif formatted_header == "area" or ("area" in formatted_header and 
                                                "count" in formatted_header):
                cols.a = head
            elif formatted_header == "height" or ("ght" in formatted_header and 
                                                  "count" in formatted_header):
                cols.h = head
            elif "area" in formatted_header:
                # There can be multiple e.g. std and response factor corrected. Paul asked
                # for us to prefer std where both are given.
                # i.e. use if we don't have it already or if we do and existing is for resp fact
                if not cols.ca or ('RF' in cols.ca.upper() or 'RESP' in cols.ca.upper()):
                    cols.ca = head
            elif "ght" in formatted_header:  # seen "<uom> (Hght)", "<uom> (Height)" & "Hght%"
                # as above prefer std over resp fact if both are given
                if not cols.ch or ('RF' in cols.ch.upper() or 'RESP' in cols.ch.upper()):
                    cols.ch = head
            else:
                gc_logger.warning(f"Unexpected header found in page data: {head} - failed to assign")
        return cols

    def _get_row_with_most_values(self) -> Tuple[Row, int]:
        """
        All rows will have the same number of cols (None inserted to keep alignment). We 
        want to find an example of a row with the greatest number of values that are not
        None, ideally returning the first example of this i.e. lowest index.
        """
        idx_row_cnt_tuples = [(i, len(list(filter(None, r))))  # count truthy vals
                                          for i, r in enumerate(self.page_data.data_rows)]
        # sort by n_truthy_values, then by index, 1/n to invert so we can use lowest like idx
        idx_row_cnt_tuples.sort(key=lambda x: (1/(x[1]), x[0]))
        idx_with_most_values = idx_row_cnt_tuples[0][0]
        row_with_most_values = self.page_data.data_rows[idx_with_most_values]
        return row_with_most_values, idx_with_most_values