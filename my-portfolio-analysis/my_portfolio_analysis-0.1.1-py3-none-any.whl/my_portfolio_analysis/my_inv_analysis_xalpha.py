import pandas as pd
import xalpha as xa
from xalpha.cons import yesterdayobj


class MyPortfolioAnalysis:
    def __init__(self, master_data_df: pd.DataFrame, ex_record_df: pd.DataFrame, in_record_df: pd.DataFrame):
        self.master_data = master_data_df
        self.ex_record_df = ex_record_df
        self.in_record_df = in_record_df

    def get_my_inv_analysis(self, type='open', totmoney=None):
        """
        生成上一交易日分析xalpha对象，可以使用.combsummary() 获取df
        :param type: open or fix
        :param totmoney:
        :return:
        """
        ex_record_df = self.ex_record_df[self.ex_record_df.date != 'tobedeleted']

        ex_record = xa.record(path=ex_record_df, fund_property=True)
        in_record = xa.irecord(path=self.in_record_df)

        if type == 'open':
            result = xa.mul(status=ex_record, istatus=in_record)
        elif type == 'fix':
            result = xa.mulfix(status=ex_record, istatus=in_record, totmoney=totmoney)
        return result

    def __generate_my_inv_month_end_closing(self, df_analysis, period, analysis_date):
        df_month_end_closing_template = df_analysis[df_analysis.基金名称 != '总计']
        df_month_end_closing_template = df_month_end_closing_template[['基金名称', '基金代码', '基金现值']]
        df_month_end_closing_template.rename(columns={'基金名称': '项目', '基金代码': '代码', '基金现值': '现值'}, inplace=True)
        master_data = self.master_data[self.master_data['Validation'] == 'Y']  # 删除所有不在用的投资项目
        non_fund_list = master_data.loc[master_data['code'].isna(), 'name']
        for name in non_fund_list:
            df_month_end_closing_template = df_month_end_closing_template.append({'项目': name}, ignore_index=True)

        type1_list = []
        type2_list = []
        type3_list = []
        for index, row in df_month_end_closing_template.iterrows():
            type1 = master_data.loc[master_data['name'] == row['项目'], 'type_1'].iloc[0]
            type1_list.append(type1)
            type2 = master_data.loc[master_data['name'] == row['项目'], 'type_2'].iloc[0]
            type2_list.append(type2)
            type3 = master_data.loc[master_data['name'] == row['项目'], 'type_3'].iloc[0]
            type3_list.append(type3)
        df_month_end_closing_template['分类1'] = type1_list
        df_month_end_closing_template['分类2'] = type2_list
        df_month_end_closing_template['分类3'] = type3_list
        df_month_end_closing_template['期间'] = period
        df_month_end_closing_template['记录日期'] = analysis_date
        df_month_end_closing_template = df_month_end_closing_template[
            ['期间', '记录日期', '项目', '代码', '分类1', '分类2', '分类3', '现值']]
        return df_month_end_closing_template

    def generate_analysis_and_month_end_closing_template(self, period, date=None):
        """
        生成我的投资月结模版
        :param period: YYYY/MM
        :param date: pd.to_datetime('YYYY-MM-DD')
        :return:
        """
        if date is None:
            date = yesterdayobj()
        sys_open = self.get_my_inv_analysis(type='open')
        df_analysis = sys_open.combsummary(date=date).sort_values(by="基金现值", ascending=False)
        df_analysis = df_analysis[df_analysis['基金现值'] != 0]
        df_month_end_closing_template = self.__generate_my_inv_month_end_closing(df_analysis, period=period,
                                                                                 analysis_date=date.strftime(
                                                                                     '%Y/%m/%d'))
        df_month_end_closing_template['现值'] = pd.to_numeric(df_month_end_closing_template['现值'], errors='coerce')
        return df_month_end_closing_template
