import pandas as pd
import pytest
import random

from datupapi.feateng.scale import Scale


class TestScaleDataset(object):

    def test_dataset_size(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = [[13, 201236, 78.96], [45, 1289751, -1.56], [68, -5263478, -78.5]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Age', 'PnL', 'Temp'])
        for scaler in ['minmax', 'robust', 'zscore']:
            df_out, _ = scl.scale_dataset(df, scaler=scaler)
            actual = df_out.shape
            expected = df.shape
            msg = (f'Scale.scale_dataset returned {actual} instead of {expected}')
            assert actual == expected, msg

    def test_dataset_boxcox_size(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = [[13, 201236, 78.96], [45, 1289751, 1.56], [68, 5263478, 0.1]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Age', 'PnL', 'Temp'])
        df_out, _ = scl.scale_dataset(df, scaler='boxcox')
        actual = df_out.shape
        expected = df.shape
        msg = (f'Scale.scale_dataset returned {actual} instead of {expected}')
        assert actual == expected, msg

    def test_minmax_bounds(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = [[13, 201236, 78.96], [45, 1289751, 1.56], [68, 5263478, 0.1]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Age', 'PnL', 'Temp'])
        df_out, _ = scl.scale_dataset(df, scaler='minmax')
        actual = (min(df_out.min(axis=1).values), max(df_out.max(axis=1).values))
        expected = (0.0, 1.0)
        msg = (f'Scale.scale_dataset returned {actual} instead of {expected}')
        assert actual == expected, msg

    def test_boxcox_bounds(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = [[13, 201236, 78.96], [45, 1289751, 1.56], [68, 5263478, 1]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Age', 'PnL', 'Temp'])
        df_out, _ = scl.scale_dataset(df, scaler='boxcox')
        actual_min = min(df_out.min(axis=1).values)
        actual_max = max(df_out.max(axis=1).values)
        expected_min = 0.0
        msg = (f'Scale.scale_dataset returned {actual_min} instead of {expected_min}')
        assert actual_max > 0 , msg
        msg = (f'Scale.scale_dataset returned {actual_max} instead of larger than 0')


class TestInverseScaleDataset(object):

    def test_dataset_size(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = [[13, 201236, 78.96], [45, 1289751, 1.56], [68, 5263478, 78.5]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Age', 'PnL', 'Temp'])
        for scaler in ['minmax', 'robust', 'zscore', 'boxcox']:
            df_out, scaler_obj = scl.scale_dataset(df, scaler=scaler)
            df_inv = scl.inverse_scale_dataset(df_out, scaler_obj=scaler_obj)
            actual = df_inv.shape
            expected = df.shape
            msg = (f'Scale.scale_dataset returned {actual} instead of {expected}')
            assert actual == expected, msg

class TestExtractFrequency(object):

    def test_min_frequency_value(self):
        scl = Scale(config_file='datupapi/config.yml', logfile='test_data_feateng', log_path='output/logs')
        data = random.sample(range(0, 888), 260)
        ts = pd.Series(data=data)
        actual = scl.extract_frequency(ts.values, frequency='W-SUN')
        nonexpected = 1
        msg = (f'Scale.extract_frequency returned {actual} equal or fewer than {nonexpected}')
        assert actual > nonexpected, msg