import pandas as pd
import pytest

from datupapi.transform.ranking import Ranking


class TestRankABC(object):

    def test_items_rank_distribution(self):
        rnkg = Ranking(config_file='datupapi/config.yml', logfile="test_data_ranking", log_path='output/logs')
        data = [[123, 12, 0],
                [435, 12, 0],
                [456, 1, 0],
                [345, 0, 12],
                [12345, 0, 15]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Sku1', 'Sku2', 'Sku3'])
        df_out = rnkg.rank_abc(df, sku_col='Sku', rank_col='Margin')
        actual = len(df.columns)
        expected = df_out.loc[df_out['ABC'] == 'A', 'ABC'].count() +\
                   df_out.loc[df_out['ABC'] == 'B', 'ABC'].count() +\
                   df_out.loc[df_out['ABC'] == 'C', 'ABC'].count()
        msg = (f'Ranking.rank_abc returned {actual} instead of {expected}')
        assert actual == expected, msg


class TestRankFSN(object):

    def test_items_rank_distribution(self):
        rnkg = Ranking(config_file='datupapi/config.yml', logfile="test_data_ranking", log_path='output/logs')
        data = [[123, 12, 0],
                [435, 12, 0],
                [456, 1, 0],
                [345, 0, 12],
                [12345, 0, 15]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Sku1', 'Sku2', 'Sku3'])
        df_out = rnkg.rank_fsn(df, sku_col='Sku', rank_col='Volume')
        actual = len(df.columns)
        expected = df_out.loc[df_out['FSN'] == 'F', 'FSN'].count() +\
                   df_out.loc[df_out['FSN'] == 'S', 'FSN'].count() +\
                   df_out.loc[df_out['FSN'] == 'N', 'FSN'].count()
        msg = (f'Ranking.rank_fsn returned {actual} instead of {expected}')
        assert actual == expected, msg


class TestRankXYZ(object):

    def test_items_rank_distribution(self):
        rnkg = Ranking(config_file='datupapi/config.yml', logfile="test_data_ranking", log_path='output/logs')
        data = [[123, 12, 0],
                [435, 12, 0],
                [456, 1, 0],
                [345, 0, 12],
                [12345, 0, 15]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['Sku1', 'Sku2', 'Sku3'])
        df_out = rnkg.rank_xyz(df, sku_col='Sku', rank_col='Volume')
        actual = len(df.columns)
        expected = df_out.loc[df_out['XYZ'] == 'X', 'XYZ'].count() +\
                   df_out.loc[df_out['XYZ'] == 'Y', 'XYZ'].count() +\
                   df_out.loc[df_out['XYZ'] == 'Z', 'XYZ'].count()
        msg = (f'Ranking.rank_xyz returned {actual} instead of {expected}')
        assert actual == expected, msg