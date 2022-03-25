import pandas as pd
import pytest

from datupapi.extract.io import IO


class TestExtractMSSQL(object):

    def test_dbtable_rows_size(self, hostname='181.143.64.93', db_user='tr_datup', db_passwd='USgRC1BAEK', db_name='TR_Datup', port='1433', table_name='TR_TAB_OLAP_HVentas_1'):
        io = IO(config_file='datupapi/config.yml', logfile="test_data_io", log_path='output/logs')
        actual = io.download_mssql(hostname=hostname, db_user=db_user, db_passwd=db_passwd, db_name=db_name, port=port, table_name=table_name).shape[0]
        unexpected = 0
        msg = (f'IO.extract_mssql returned {actual} instead of {unexpected + 1} or larger')
        assert actual is not unexpected, msg

class TestUploadCSV(object):

    def test_csv_upload(self, q_name='Q-test', datalake_path='in-proc/test'):
        io = IO(config_file='datupapi/config.yml', logfile="test_data_io", log_path='output/logs')
        df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
        actual = io.upload_csv(df=df, q_name=q_name, datalake_path=datalake_path)
        expected = True
        msg = (f'IO.upload_csv returned {actual} instead of {expected}')
        assert actual is expected, msg


class TestDownloadCSV(object):

    def test_csv_rows_size(self, q_name='Q-test', datalake_path='in-proc/test'):
        io = IO(config_file='datupapi/config.yml', logfile="test_data_io", log_path='output/logs')
        actual = io.download_csv(q_name=q_name, datalake_path=datalake_path).shape[0]
        unexpected = 0
        msg = (f'IO.download_csv returned {actual} instead of {unexpected + 1} or larger')
        assert actual is not unexpected, msg

class TestDownloadExcel(object):

    def test_excel_rows_size(self, q_name='Q-test.xlsx', sheet_name='Q-test', datalake_path='in-proc/test/Q-test'):
        io = IO(config_file='datupapi/config.yml', logfile="test_data_io", log_path='output/logs')
        actual = io.download_excel(q_name=q_name, sheet_name=sheet_name, datalake_path=datalake_path).shape[0]
        unexpected = 0
        msg = (f'IO.download_csv returned {actual} instead of {unexpected + 1} or larger')
        assert actual is not unexpected, msg





