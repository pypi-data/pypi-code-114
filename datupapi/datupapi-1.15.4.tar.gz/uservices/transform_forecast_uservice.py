import os
import pandas as pd
import sys

from datupapi.extract.io import IO
from datupapi.prepare.format import Format
from datupapi.transform.ranking import Ranking
from datupapi.transform.backtesting import Backtesting
from datupapi.transform.forecasting import Forecasting


def main():
    io = IO(config_file='config.yml', logfile='data_forecasting', log_path='output/logs')
    fmt = Format(config_file='config.yml', logfile='data_prepare', log_path='output/logs')
    rnkg = Ranking(config_file='config.yml', logfile='data_ranking', log_path='output/logs')
    bckt = Backtesting(config_file='config.yml', logfile='data_backtesting', log_path='output/logs')
    fcst = Forecasting(config_file='config.yml', logfile='data_forecasting', log_path='output/logs')

    io.logger.debug('Forecasting starting...')
    df_rank = io.download_csv(q_name='Qrank', datalake_path=rnkg.results_path)
    df_fcst_all = io.download_all_objects_csv(datalake_path=fcst.forecast_export_path, date_cols=['date'])
    df_fcst_all = fcst.format_forecasts_export(df_fcst_all)
    df_bckt = bckt.concat_backtest_datasets(q_backtest='Qback',
                                            backtests_names=fcst.backtest_ids,
                                            datalake_path_=bckt.results_path)
    if fcst.use_location:
        df_fcst = pd.DataFrame()
        for location in df_bckt['Location'].unique():
            df_bckt_tmp = df_bckt.loc[df_bckt['Location'] == location]
            df_fcst_tmp = df_fcst_all.loc[df_fcst_all['Location'] == location]
            df_fcst_tmp = fcst.compute_errors_from_backtests(df_fcst_tmp, df_bckt_tmp, error_types=fcst.error_ids)
            df_fcst_tmp = fcst.compute_interval_per_backtests(df_fcst_tmp,
                                                              q_backtest='Qback',
                                                              backtest_names=fcst.backtest_ids,
                                                              datalake_path_=fcst.results_path,
                                                              use_location=fcst.use_location,
                                                              location=location)
            df_fcst_tmp = fcst.compute_suggested_interval(df_fcst_tmp, backtest_names=fcst.backtest_ids)
            df_fcst_tmp = fcst.compute_suggested_forecast(df_fcst_tmp, backtest_names=fcst.backtest_ids)
            df_fcst_tmp = fcst.concat_forecast_backtests(df_fcst_tmp, df_bckt_tmp, debug_cols=False)
            df_fcst_tmp = fcst.compute_next_suggested_interval_forecast(df_fcst_tmp)
            df_fcst_tmp = fcst.compute_back_suggested_interval_forecast(df_fcst_tmp)
            df_fcst_tmp = fcst.compute_naive_forecast(df_fcst_tmp)
            df_fcst = pd.concat([df_fcst, df_fcst_tmp], axis='rows').drop_duplicates()
            df_fcst['ForecastCollab'] = df_fcst['SuggestedForecast']
            forecast_cols = ['Date', 'Week', 'Item', 'Location', 'Target',
                             'SuggestedForecast', 'SuggestedInterval',
                             'NextSuggestedForecast', 'NextSuggestedInterval',
                             'BackSuggestedForecast', 'BackSuggestedInterval',
                             'ForecastCollab', 'ForecastNaive', 'ForecastPoint']
    else:
        df_fcst = fcst.compute_errors_from_backtests(df_fcst_all, df_bckt, error_types=fcst.error_ids)
        df_fcst = fcst.compute_interval_per_backtests(df_fcst,
                                                      q_backtest='Qback',
                                                      backtest_names=fcst.backtest_ids,
                                                      datalake_path_=fcst.results_path)
        df_fcst = fcst.compute_suggested_interval(df_fcst, backtest_names=fcst.backtest_ids)
        df_fcst = fcst.compute_suggested_forecast(df_fcst, backtest_names=fcst.backtest_ids)

        df_fcst = fcst.concat_forecast_backtests(df_fcst, df_bckt, debug_cols=False)
        df_fcst = fcst.compute_next_suggested_interval_forecast(df_fcst)
        df_fcst = fcst.compute_back_suggested_interval_forecast(df_fcst)
        df_fcst = fcst.compute_naive_forecast(df_fcst)
        df_fcst['ForecastCollab'] = df_fcst['SuggestedForecast']
        forecast_cols = ['Date', 'Week', 'Item', 'Target',
                         'SuggestedForecast', 'SuggestedInterval',
                         'NextSuggestedForecast', 'NextSuggestedInterval',
                         'BackSuggestedForecast', 'BackSuggestedInterval',
                         'ForecastCollab', 'ForecastNaive', 'ForecastPoint']
    if fcst.use_location:
        df_rank = df_rank.astype({'Item': str, 'Location': str, 'Ranking': str})
        df_fcst = df_fcst.astype({'Item': str, 'Location': str})
        df_fcst = pd.merge(df_fcst, df_rank[['Item', 'Location', 'Ranking']], on=['Item', 'Location'], how='left')
    else:
        df_rank = df_rank.astype({'Item': str, 'Ranking': str})
        df_fcst = df_fcst.astype({'Item': str})
        df_fcst = fcst.concat_forecast_ranking(df_fcst, df_rank)
    if fcst.items_metadata:
        df_meta = io.download_csv(q_name='Qmeta', datalake_path=fcst.results_path)
        if fcst.use_location:
            df_fcst = fmt.concat_item_metadata_with_location(df_fcst, df_meta, item_col='Item', location_col='Location')
        else:
            df_fcst = fmt.concat_item_metadata(df_fcst, df_meta, item_col='Item')
    df_fcst = fmt.reorder_cols(df_fcst, first_cols=forecast_cols)

    io.upload_csv(df_fcst, q_name='Qfcst', datalake_path=fcst.results_path)
    io.populate_dbtable(df_fcst,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblForecast',
                        db_type=io.get_secret()['engine'])
    io.logger.debug('Forecasting completed...')
    io.upload_log()


if __name__ == '__main__':
    main()
    sys.exit(0)
