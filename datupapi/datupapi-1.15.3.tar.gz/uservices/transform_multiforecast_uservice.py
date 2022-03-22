import os
import sys

import pandas as pd

from datupapi.extract.io import IO
from datupapi.transform.forecasting import Forecasting


def main():
    io = IO(config_file='config.yml', logfile='data_multiforecast', log_path='output/logs')
    fcst = Forecasting(config_file='config.yml', logfile='data_multiforecast', log_path='output/logs')

    io.logger.debug('Multiforecast starting...')
    model_type_ = 'tft'
    forecast_horizons_ = [1, 2, 5]

    df_fcst = fcst.concat_forecast_horizons(model_type=model_type_, forecast_horizons=forecast_horizons_)
    df_fcst_mo = fcst.concat_forecast_horizons_monthly(model_type=model_type_, forecast_horizons=forecast_horizons_)
    df_fcst['Date'] = pd.to_datetime(df_fcst['Date']).dt.date
    df_fcst_mo['Date'] = pd.to_datetime(df_fcst_mo['Date']).dt.date

    # Recompute Forecast Naive
    if fcst.use_location:
        df_mfcst = pd.DataFrame()
        for location in df_fcst['Location'].unique():
            df_fcst_tmp = df_fcst.loc[df_fcst['Location'] == location]
            df_fcst_tmp = fcst.compute_naive_forecast(df_fcst_tmp, num_periods=forecast_horizons_[2], naive_type='roll')
            df_mfcst = pd.concat([df_mfcst, df_fcst_tmp], axis='rows').drop_duplicates()
        df_mfcst_mo = pd.DataFrame()
        for location in df_fcst_mo['Location'].unique():
            df_fcst_mo_tmp = df_fcst_mo.loc[df_fcst_mo['Location'] == location]
            df_fcst_mo_tmp = fcst.compute_naive_forecast(df_fcst_mo_tmp, num_periods=3, naive_type='roll')
            df_mfcst_mo = pd.concat([df_mfcst_mo, df_fcst_mo_tmp], axis='rows').drop_duplicates()
    else:
        df_mfcst = fcst.compute_naive_forecast(df_fcst, num_periods=forecast_horizons_[2], naive_type='roll')
        df_mfcst_mo = fcst.compute_naive_forecast(df_fcst_mo, num_periods=3, naive_type='roll')

    # Fix to end of month date
    df_mfcst['Date'] = pd.to_datetime(df_mfcst['Date'])
    df_mfcst_mo['Date'] = pd.to_datetime(df_mfcst_mo['Date'])
    df_mfcst = df_mfcst.set_index('Date')
    df_mfcst_mo = df_mfcst_mo.set_index('Date')
    df_mfcst.index = df_mfcst.index.to_period('M').to_timestamp('M')
    df_mfcst_mo.index = df_mfcst_mo.index.to_period('M').to_timestamp('M')
    df_mfcst = df_mfcst.reset_index()
    df_mfcst_mo = df_mfcst_mo.reset_index()
    df_mfcst['Date'] = df_mfcst['Date'].dt.date
    df_mfcst_mo['Date'] = df_mfcst_mo['Date'].dt.date

    for horizon in forecast_horizons_:
        io.upload_csv(df_mfcst, q_name='Qmfcst',
                      datalake_path=os.path.join(fcst.multiforecast_path, model_type_ + str(horizon) + fcst.dataset_frequency.lower(), 'output'))
        io.upload_csv(df_mfcst_mo, q_name='Qmfcst-mo',
                      datalake_path=os.path.join(fcst.multiforecast_path, model_type_ + str(horizon) + fcst.dataset_frequency.lower(), 'output'))

    # io.populate_snowflake_table(df_mfcst,
    #                             dwh_account=io.get_secret()['account'],
    #                             dwh_name=io.get_secret()['warehouse'],
    #                             dwh_user=io.get_secret()['user'],
    #                             dwh_passwd=io.get_secret()['password'],
    #                             dwh_dbname=io.get_secret()['database'],
    #                             dwh_schema=io.get_secret()['schema'],
    #                             table_name='TblMultiforecast'
    #                             )
    # io.populate_dbtable(df_mfcst,
    #                     hostname=io.get_secret()['host'],
    #                     db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
    #                     db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
    #                     table_name='TblMultiforecast',
    #                     db_type=io.get_secret()['engine'])
    # io.populate_dbtable(df_mfcst_mo,
    #                     hostname=io.get_secret()['host'],
    #                     db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
    #                     db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
    #                     table_name='TblMultiforecastMonth',
    #                     db_type=io.get_secret()['engine'])
    io.logger.debug('Multiforecast completed...')
    io.upload_log()


if __name__ == '__main__':
    main()
    sys.exit(0)
