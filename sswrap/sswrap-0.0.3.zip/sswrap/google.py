import os.path
from enum import Enum
from typing import List, Any, Dict, Optional, Union

import googleapiclient.discovery
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from sswrap.common import to_a1_range, from_a1_cell
from sswrap.exceptions import SswrapException
from sswrap.spreadsheet import Spreadsheet
from sswrap.worksheet import Worksheet

_DEFAULT_CREDENTIAL_PATH = "credentials.json"
_DEFAULT_TOKEN_PATH = "token.json"
_DEFAULT_WRITABLE = False
_DEFAULT_PREFETCH = True


def _prepare_spreadsheets_resource(*,
                                   credential_path: str = _DEFAULT_CREDENTIAL_PATH,
                                   token_path: str = _DEFAULT_TOKEN_PATH,
                                   writable: bool = _DEFAULT_WRITABLE) -> googleapiclient.discovery.Resource:
    """\
    Constructs a googleapiclient.discovery.Resource for interacting with Google Sheets API.

    See https://developers.google.com/sheets/api/reference/rest

    :param credential_path:
    :param token_path:
    :param writable:
    :return: Resource object for interacting with Google Sheets API
    """
    scopes: List[str]
    if writable:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    else:
        scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

    # Based on https://developers.google.com/sheets/api/quickstart/python
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, scopes)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential_path, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())
    if not creds:
        raise SswrapException("Failed to create a credential for Google Sheets API")
    return build("sheets", "v4", credentials=creds).spreadsheets()


class ValueRenderOption(Enum):
    """\
    See also https://developers.google.com/sheets/api/reference/rest/v4/ValueRenderOption
    """
    # Values will be calculated & formatted in the reply according to the cell's formatting.
    # Formatting is based on the spreadsheet's locale, not the requesting user's locale.
    # For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "$1.23".
    FORMATTED_VALUE = "FORMATTED_VALUE"

    # Values will be calculated, but not formatted in the reply.
    # For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return the number 1.23.
    UNFORMATTED_VALUE = "UNFORMATTED_VALUE"

    # Values will not be calculated. The reply will include the formulas.
    # For example, if A1 is 1.23 and A2 is =A1 and formatted as currency, then A2 would return "=A1".
    FORMULA = "FORMULA"

    def __str__(self):
        return self.value


class GoogleSpreadsheet(Spreadsheet):
    def __init__(self,
                 spreadsheet_id: str,
                 *,
                 credential_path: str = _DEFAULT_CREDENTIAL_PATH,
                 token_path: str = _DEFAULT_TOKEN_PATH,
                 writable: bool = _DEFAULT_WRITABLE,
                 value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE):
        super().__init__()
        self._spreadsheet_id = spreadsheet_id
        self._resource = _prepare_spreadsheets_resource(credential_path=credential_path,
                                                        token_path=token_path,
                                                        writable=writable)
        self._metadata = self._get_remote_metadata()
        self._sheet_title_to_index: Dict[str, int] = {
            sheet["properties"]["title"]: i for i, sheet in enumerate(self._metadata["sheets"])
        }
        self._value_render_option = value_render_option

    @property
    def metadata(self):
        return self._metadata

    def get_sheet_names(self) -> List[str]:
        return list(self._sheet_title_to_index.keys())

    def _get_remote_metadata(self):
        return self._resource.get(spreadsheetId=self._spreadsheet_id, fields=None).execute()

    def num_worksheets(self) -> int:
        return len(self._metadata.get('sheets', 0))

    def __getitem__(self, index_or_name: Union[int, str]) -> "GoogleWorksheet":
        if isinstance(index_or_name, str):
            index = self._sheet_title_to_index[index_or_name]
        else:
            index = index_or_name
        return GoogleWorksheet(self,
                               self._metadata.get("sheets", [])[index],
                               value_render_option=self._value_render_option)

    def __len__(self) -> int:
        return len(self._metadata.get('sheets', []))

    @property
    def resource(self):
        return self._resource

    @property
    def spreadsheet_id(self):
        return self._spreadsheet_id


class GoogleWorksheet(Worksheet):
    def __init__(self,
                 spreadsheet: "GoogleSpreadsheet",
                 metadata: Dict[str, Any],
                 *,
                 value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE):
        self._spreadsheet = spreadsheet
        self._metadata = metadata
        grid_properties = self._metadata["properties"]["gridProperties"]
        # 巨大なシートをまだ対象としてない
        row_count = grid_properties["rowCount"]
        col_count = grid_properties["columnCount"]
        # TODO: Implement non-cache initialization
        self._cache: Optional[List[List[Any]]] = self.fetch_remote_range(
            0, 0, row_count - 1, col_count - 1, value_render_option=value_render_option)

    @property
    def title(self):
        return self._metadata["properties"]["title"]

    @property
    def metadata(self):
        return self._metadata

    def fetch_remote_range(self,
                           start_row_index: int,
                           start_col_index: int,
                           end_row_index: int,
                           end_col_index: int,
                           *,
                           value_render_option: ValueRenderOption = ValueRenderOption.FORMATTED_VALUE)\
            -> List[List[Any]]:
        """\
        指定したリモート範囲を取得して返す。内部キャッシュを無視する。また内部キャッシュを更新しない
        """
        range_str = to_a1_range(start_row_index, start_col_index, end_row_index, end_col_index)
        result = self._spreadsheet.resource.values().get(spreadsheetId=self._spreadsheet.spreadsheet_id,
                                                         range="{}!{}".format(self.title, range_str),
                                                         valueRenderOption=value_render_option.value).execute()
        return result.get("values")

    def get_value(self, row_index: int, col_index: int) -> Any:
        return self._cache[row_index][col_index]

    def get_by_cell(self, cell: str) -> Any:
        row_index, col_index = from_a1_cell(cell)
        return self.get_value(row_index, col_index)

    def get_range_as_dict(self,
                          start_row_index: int,
                          start_col_index: int,
                          end_row_index: int,
                          end_col_index: int,
                          *,
                          name_map: Optional[Dict[str, str]] = None,
                          ignore_shorter_content: bool = True,
                          ignore_longer_content: bool = True)\
            -> List[Dict[str, Any]]:
        """\
        指定したリモート範囲の1行目をヘッダ行とみなし、辞書にして返す。
        辞書のキーはヘッダ行のそれぞれが文字列に変換されたものである。

        name_map がある場合、ヘッダに記載された名前をキーとしてname_mapを探索し、
        もし対応するvalueがあるなら、返却されるキーもその変換後の名前になる。

        ヘッダ行より長いデータ本体の行が存在した場合、ignore_longer_contentがTrueなら無視し、Falseなら例外を送出する
        """
        if end_row_index - start_row_index < 1:
            raise SswrapException("Row range not sufficient")
        assert self._cache
        rows = self._cache[start_row_index:end_row_index + 1]

        assert len(rows) > 1
        header_row = rows[0][start_col_index:end_col_index + 1]
        header_length = len(header_row)
        col_to_name: Dict[int, str] = {}
        if name_map is None:
            name_map = {}
        appeared = set()
        for i, org_header in enumerate(header_row):
            header = name_map.get(org_header, org_header)
            if header in appeared:
                header_str = f"\"{header}\"" if header == org_header else f"\"{header}\" (org: \"{org_header}\")"
                raise SswrapException(f"header {header_str} already appeared")
            col_to_name[i] = header
        ret = []
        for raw_i, row in enumerate(rows[1:]):
            row_index = start_row_index + raw_i + 1
            if header_length < len(row):
                if ignore_longer_content:
                    row = row[:header_length]
                else:
                    raise SswrapException(f"Too long content row at {row_index}")
            elif header_length > len(row):
                if ignore_shorter_content:
                    row = row + [None] * (header_length - len(row))
                else:
                    raise SswrapException(f"Too short content row at {row_index}")
            ret.append({col_to_name[col_i]: col for col_i, col in enumerate(row)})
        return ret


def _run_smoke_test():
    """\
    Runs a simple procedure demonstrating Google Sheets API.
    See also https://developers.google.com/sheets/api/quickstart/python
    """
    resource = _prepare_spreadsheets_resource()
    # This spreadsheet is maintained by Google, not by us.
    result = resource.values().get(spreadsheetId="1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
                                   range="Class Data!A2:E").execute()
    values = result.get("values", [])

    if not values:
        print("No data found.")
        return

    print("Name, Major:")
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print(f"{row[0]}, {row[4]}")


if __name__ == "__main__":
    print("Start running an embedded smoke test")
    _run_smoke_test()
