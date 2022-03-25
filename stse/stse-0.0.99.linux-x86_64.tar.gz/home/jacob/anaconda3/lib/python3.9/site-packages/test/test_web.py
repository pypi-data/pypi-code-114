import unittest
import pandas as pd

from stse import web, dataframes


class TestWeb(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = pd.DataFrame({
            'a': [1, 2, 3, 4],
            'b': ['a', 'b', 'c', 'd']
        })
        return super().setUpClass()
    
    def test_read_shreadsheet(self):
        # Test csv
        mock_file = dataframes.store_df(self.df, 'csv')
        pd.testing.assert_frame_equal(
            web.read_spreadsheet(mock_file), 
            self.df
        )
        mock_file.close()
        
        # Test excel
        mock_file = dataframes.store_df(self.df, 'xlsx')
        pd.testing.assert_frame_equal(
            web.read_spreadsheet(mock_file), 
            self.df
        )
        mock_file.close()
        
        # Test csv
        mock_file = dataframes.store_df(self.df, 'tsv')
        pd.testing.assert_frame_equal(
            web.read_spreadsheet(mock_file), 
            self.df
        )
        mock_file.close()


if __name__ == '__main__':
    unittest.main()
