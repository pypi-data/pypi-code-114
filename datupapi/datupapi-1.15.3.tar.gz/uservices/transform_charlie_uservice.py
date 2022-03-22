import os
import pandas as pd
import sys

from datupapi.extract.io import IO
from datupapi.transform.backtesting import Backtesting
from datupapi.prepare.format import Format


def main():
    io = IO(config_file='config.yml', logfile='data_backtesting', log_path='output/logs')
    bckt = Backtesting(config_file='config.yml', logfile='data_backtesting', log_path='output/logs')
    fmt = Format(config_file='config.yml', logfile='data_backtesting', log_path='output/logs')

    try:
        backtest = bckt.backtest_ids[2]
        io.logger.debug('Backtesting charlie starting...')
        df = io.download_all_objects_csv(datalake_path=os.path.join(bckt.backtest_export_path,'forecasted-values'))
        df = bckt.format_backtests_export(df)
        if bckt.use_location:
            df_back = pd.DataFrame()
            for location in df['Location'].unique():
                df_back_tmp = df.loc[df['Location'] == location]
                df_back_tmp = bckt.create_backtest_dataset(df_back_tmp, backtest_name=backtest)
                df_back_tmp = bckt.compute_bias(df_back_tmp)
                df_back_tmp = bckt.compute_tracking_bias(df_back_tmp)
                df_back_tmp = bckt.compute_tracked_bias(df_back_tmp)
                df_back_tmp = bckt.compute_tracked_bias_forecast(df_back_tmp)
                df_back_tmp = bckt.compute_tracked_bias_error(df_back_tmp, error_types=bckt.error_ids)
                df_back = pd.concat([df_back, df_back_tmp], axis='rows').drop_duplicates()
                backtest_cols = ['Date', 'Week', 'Item', 'Location', 'Target',
                                 'SuggestedForecast', 'SuggestedInterval', 'ForecastPoint']
        else:
            df_back = bckt.create_backtest_dataset(df, backtest_name=backtest)
            df_back = bckt.compute_bias(df_back)
            df_back = bckt.compute_tracking_bias(df_back)
            df_back = bckt.compute_tracked_bias(df_back)
            df_back = bckt.compute_tracked_bias_forecast(df_back)
            df_back = bckt.compute_tracked_bias_error(df_back, error_types=bckt.error_ids)
            backtest_cols = ['Date', 'Week', 'Item', 'Target',
                             'SuggestedForecast', 'SuggestedInterval', 'ForecastPoint']

        df_back = fmt.reorder_cols(df_back, first_cols=backtest_cols)
        io.upload_csv(df_back, q_name='Qback' + '-' + backtest, datalake_path=bckt.results_path)
        io.logger.debug('Backtesting charlie completed...')
        io.upload_log()
    except IndexError:
        raise
        print(f'Got to enter to error handling: {err}')


if __name__ == '__main__':
    main()
    sys.exit(0)