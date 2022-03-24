"""
Kevin的标的池跟踪模块：tracker
"""
import os
import pandas as pd
import hbshare as hbs
import datetime
from hbshare.quant.Kevin.quant_room.MyUtil.data_loader import get_fund_nav_from_sql, get_trading_day_list
from hbshare.quant.Kevin.quant_room.MyUtil.util_func import cal_annual_return, cal_annual_volatility
import plotly.express as px
from plotly.offline import plot as plot_ly



# import numpy as np
# from datetime import datetime
#
# from Arbitrage_backtest import cal_annual_return, cal_annual_volatility, cal_sharpe_ratio, cal_max_drawdown
# import plotly
# from plotly.offline import plot as plot_ly
# import plotly.graph_objs as go
# import plotly.figure_factory as ff
#
# plotly.offline.init_notebook_mode(connected=True)


class FundTracker:
    def __init__(self, end_date, cf_path):
        self.end_date = end_date
        self.cf_path = cf_path
        self._load_data()

    @staticmethod
    def _load_benchmark(start_date, end_date, benchmark_id):
        sql_script = "SELECT JYRQ as TRADEDATE, ZQDM, SPJG as TCLOSE from funddb.ZSJY WHERE" \
                     " ZQDM = '{}' " \
                     "and JYRQ >= {} and JYRQ <= {}".format(benchmark_id, start_date, end_date)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        data = pd.DataFrame(res['data'])
        benchmark_df = data.set_index('TRADEDATE')['TCLOSE']

        return benchmark_df

    def _load_data(self):
        config_df = pd.read_excel(os.path.join(self.cf_path, "config.xlsx"), sheet_name=0)
        end_dt = datetime.datetime.strptime(self.end_date, '%Y%m%d')
        pre_date = (end_dt - datetime.timedelta(days=180)).strftime('%Y%m%d')
        trading_day_list = get_trading_day_list(pre_date, self.end_date, frequency="week")[-9:]

        return_dict = {}

        # 500指增
        fund_dict = config_df[config_df['二级分类'] == "500指增"].set_index('基金名称')['Fund_id'].to_dict()
        fund_nav = get_fund_nav_from_sql(pre_date, self.end_date, fund_dict).reindex(
            trading_day_list).dropna(axis=1)
        benchmark_series = self._load_benchmark(pre_date, self.end_date, '000905').reindex(
            trading_day_list).pct_change().dropna()
        return_df = fund_nav.pct_change().dropna().sub(benchmark_series, axis=0).sort_index()
        return_dict['500_alpha'] = return_df
        # 1000指增
        fund_dict = config_df[config_df['二级分类'] == "1000指增"].set_index('基金名称')['Fund_id'].to_dict()
        fund_nav = get_fund_nav_from_sql(pre_date, self.end_date, fund_dict).reindex(
            trading_day_list).dropna(axis=1)
        benchmark_series = self._load_benchmark(pre_date, self.end_date, '000852').reindex(
            trading_day_list).pct_change().dropna()
        return_df = fund_nav.pct_change().dropna().sub(benchmark_series, axis=0).sort_index()
        return_dict['1000_alpha'] = return_df
        # 量化多头
        fund_dict = config_df[config_df['策略大类'] == "量化多头"].set_index('基金名称')['Fund_id'].to_dict()
        fund_nav = get_fund_nav_from_sql(pre_date, self.end_date, fund_dict).reindex(
            trading_day_list).dropna(axis=1)
        benchmark_series = self._load_benchmark(pre_date, self.end_date, '000985').reindex(
            trading_day_list)
        fund_nav['benchmark'] = benchmark_series
        return_df = fund_nav.pct_change().dropna().sort_index()
        return_dict['all_market'] = return_df
        # 市场中性
        fund_dict = config_df[config_df['策略大类'] == "市场中性"].set_index('基金名称')['Fund_id'].to_dict()
        fund_nav = get_fund_nav_from_sql(pre_date, self.end_date, fund_dict).reindex(
            trading_day_list).dropna(axis=1)
        return_df = fund_nav.pct_change().dropna().sort_index()
        return_dict['market_neutral'] = return_df
        # 套利
        fund_dict = config_df[config_df['策略大类'] == "套利"].set_index('基金名称')['Fund_id'].to_dict()
        fund_nav = get_fund_nav_from_sql(pre_date, self.end_date, fund_dict).reindex(
            trading_day_list).dropna(axis=1)
        return_df = fund_nav.pct_change().dropna().sort_index()
        return_dict['market_neutral'] = return_df

        self.return_dict = return_dict

    def process_500_alpha(self, return_df):
        annual_return = return_df.apply(cal_annual_return, axis=0)
        annual_vol = return_df.apply(cal_annual_volatility, axis=0)
        df = pd.merge(annual_return.to_frame('超额年化收益'), annual_vol.to_frame('超额年化波动'),
                      left_index=True, right_index=True).round(4)
        abr_df = pd.read_excel(os.path.join(self.cf_path, "config.xlsx"), sheet_name=1, index_col=0)
        df['name'] = abr_df

        fig = px.scatter(df, x='超额年化波动', y='超额年化收益', text='name')
        fig.update_traces(
            textposition="top center",
            textfont={'color': '#bebebe', 'size': 14}
        )
        fig.update_layout(
            title_text="<b>收益风险比（过去8周）<b>",
            template='plotly_white',
            titlefont={'size': 24},
            width=1200,
            height=800,
            yaxis=dict(tickfont=dict(size=12), tickformat=',.1%', showgrid=True),
            xaxis=dict(showgrid=True, tickformat=',.1%'),
        )

        plot_ly(fig, filename='D:\\123.html', auto_open=False)

    def process_500_alpha_2(self, return_df):
        df = return_df.sort_index(ascending=False).iloc[:2].T.round(4)
        df.columns = ["current_week", "pre_week"]
        abr_df = pd.read_excel(os.path.join(self.cf_path, "config.xlsx"), sheet_name=1, index_col=0)
        df['name'] = abr_df

        fig = px.scatter(df, x='pre_week', y='current_week', text='name')
        fig.update_traces(
            textposition="top center",
            textfont={'color': '#bebebe', 'size': 14}
        )
        fig.update_layout(
            title_text="<b>过去两周超额表现<b>",
            template='plotly_white',
            titlefont={'size': 24},
            width=1200,
            height=800,
            yaxis=dict(tickfont=dict(size=12), tickformat=',.1%', showgrid=True),
            xaxis=dict(showgrid=True, tickformat=',.1%'),
        )

        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=df['pre_week'].median(),
                      x1=df['pre_week'].max(),
                      y0=df['current_week'].median(),
                      y1=df['current_week'].max(),
                      fillcolor="lightgray",
                      line=dict(color='red', width=2, dash='dot'),
                      opacity=0.2
                      )
        fig.add_shape(type="rect",
                      xref="x", yref="y",
                      x0=df['pre_week'].min(),
                      x1=df['pre_week'].median(),
                      y0=df['current_week'].min(),
                      y1=df['current_week'].median(),
                      fillcolor="lightgray",
                      line=dict(color='green', width=2, dash='dot'),
                      opacity=0.2
                      )

        plot_ly(fig, filename='D:\\456.html', auto_open=False)

    def run(self):
        return_dict = self.return_dict

        return_df = return_dict['500_alpha']

        # cum_return = (1 + return_df).cumprod() - 1
        # cum_return = cum_return.iloc[[0, 1, 3, 7]].T
        # cum_return.columns = ['上周', '近两周', '近四周', '近八周']


if __name__ == '__main__':
    FundTracker('20220311', 'D:\\量化产品跟踪\\tracker\\').run()