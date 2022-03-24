from unittest import TestCase
import pandas as pd

from my_portfolio_analysis.my_inv_analysis_xalpha import MyPortfolioAnalysis


class TestMyPortfolioAnalysis(TestCase):
    def setUp(self) -> None:
        master_data_df = pd.read_excel('./my_inv_record/Inv_Asset_Record.xlsx', sheet_name='MasterData', dtype='str')
        ex_record_df = pd.read_excel('./my_inv_record/Inv_Asset_Record.xlsx', sheet_name='E_TransRecord')
        in_record_df = pd.read_excel('./my_inv_record/Inv_Asset_Record.xlsx', sheet_name='I_TransRecord')
        self.my_portfolio_analysis = MyPortfolioAnalysis(master_data_df, ex_record_df, in_record_df)

    def test_get_my_inv_analysis(self):
        # result = self.my_portfolio_analysis.get_my_inv_analysis()
        # result.combsummary().to_excel('report.xlsx', index=0)
        pass

    def test_generate_analysis_and_month_end_closing_template(self):
        self.my_portfolio_analysis.generate_analysis_and_month_end_closing_template(period='2021/12')
