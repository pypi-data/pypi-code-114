import numpy as np
import pandas as pd
import pytest

from datupapi.prepare.cleanse import Cleanse

class TestCleanMetadata(object):

    def test_camel_vowels_specialchars_removal(self):
        clns = Cleanse(config_file='datupapi/config.yml', logfile='test_data_prepare', log_path='output/logs')
        data = [[1, 0 , 1, 0], [0, 1, 0, 1]]
        metadata = ['María ñaÑez', 'Dämmerung', 'rosalía#', 'Víctor-Doom']
        clean_metadata = ['Maria Nanez', 'Dammerung', 'Rosalia', 'Victordoom']
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=metadata)
        df_out = clns.clean_metadata(df)
        actual = list(df_out.columns)
        expected = clean_metadata
        msg = (f'Cleanse.clean_metadata returned {actual} instead of {expected}')
        assert actual == expected, msg


class TestCleanData(object):

    def test_clean_categorical_data(self):
        clns = Cleanse(config_file='datupapi/config.yml', logfile='test_data_prepare', log_path='output/logs')
        data = [['Mar[ía', 'rosalía.', 'ñañez$', 25, 785.988],
                ['Jürgen', 'J.', 'Köhler', -5, 0.21]]
        clean_data = [['Maria', 'Rosalia', 'Nanez', 25, 785.988],
                      ['Jurgen', 'J', 'Kohler', -5, 0.21]]
        df = pd.DataFrame(data=data, index=range(0, len(data)), columns=['First Name', 'Middle Name', 'Surname', 'Age', 'Income'])
        df_clean = pd.DataFrame(data=clean_data, index=range(0, len(clean_data)), columns=['First Name', 'Middle Name', 'Surname', 'Age', 'Income'])
        df_out = clns.clean_data(df)
        print(df_out)
        print(df_clean)
        actual = df_out.equals(df_clean)
        expected = True
        msg = (f'Cleanse.clean_data returned {actual} instead of {expected}')
        assert actual is expected, msg



