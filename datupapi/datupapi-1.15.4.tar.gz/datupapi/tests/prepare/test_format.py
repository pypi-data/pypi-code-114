import numpy as np
import pandas as pd
import pytest

from datupapi.prepare.format import Format


class TestParseWeekToDate(object):

    def test_week_column_data_type(self):
        fmt = Format(config_file='datupapi/config.yml', logfile='test_data_prepare', log_path='output/logs')
        data = [['2017.08'], ['2018-12'], [2019.52], ['2020/04'], ['202118']]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Week'])
        df_out = fmt.parse_week_to_date(df, week_col='Week', date_col='Date')
        actual = isinstance(df_out['Week'], object)
        expected = True
        msg = (f'Format.parse_week_to_date returned {actual} data type instead of {expected}')
        assert actual is expected, msg

class TestPivotDatesVsSku(object):

    def test_dates_skus_size(self):
        fmt = Format(config_file='datupapi/config.yml', logfile='test_data_prepare', log_path='output/logs')
        data = [['2019-02-03', 1234, 16],
                ['2020-03-25', 9874, 20],
                ['2020-07-02', 7896, 78],
                ['2020-08-16', 1598, '14'],
                ['2020-08-16', 7896, 1000.47]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Date', 'Sku', 'Qty'])
        df_out = fmt.pivot_dates_vs_sku(df, date_col='Date', sku_col='Sku', qty_col='Qty')
        actual_dates = df['Date'].nunique()
        expected_dates = df_out.shape[0]
        msg_dates = (f'Format.pivot_dates_vs_sku returned {actual_dates} dates, instead of {expected_dates}')
        assert actual_dates is expected_dates, msg
        actual_skus = df['Sku'].nunique()
        expected_skus = df_out.shape[1]
        msg_skus = (f'Format.pivot_dates_vs_sku returned {actual_skus} SKUs, instead of {expected_skus}')
        assert actual_skus is expected_skus, msg_skus

class TestActiveSku(object):

    def test_active_sku_quantity(self):
        fmt = Format(config_file='datupapi/config.yml', logfile='test_data_prepare', log_path='output/logs')
        data = [[0, 1234, 0],
                [0, 1234, 0],
                [0, 1234, 0],
                [0, 0, 12],
                [0, 0, 15]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Date', 'Sku1', 'Sku2'])
        df_out = fmt.get_active_sku(df, min_periods=2, ascending=True)
        actual = len(df.columns)
        expected = len(df_out.columns)
        msg = (f'Format.get_active_sku returned {actual} skus for both input and output datasets')
        assert actual > expected

