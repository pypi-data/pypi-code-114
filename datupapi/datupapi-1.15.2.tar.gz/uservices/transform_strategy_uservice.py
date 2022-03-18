import os
import pandas as pd
import sys

from datupapi.extract.io import IO
from datupapi.prepare.format import Format
from datupapi.transform.forecasting import Forecasting


def main():
    io = IO(config_file='config.yml', logfile='data_forecasting', log_path='output/logs')
    fmt = Format(config_file='config.yml', logfile='data_prepare', log_path='output/logs')
    fcst = Forecasting(config_file='config.yml', logfile='data_forecasting', log_path='output/logs')

    io.logger.debug('Forecasting strategy starting...')
    df_fcst = io.download_csv(q_name='Qfcst', datalake_path=fcst.results_path, date_cols=['Date'])
    if fcst.use_location:
        df_strgy = pd.DataFrame()
        for location in df_fcst['Location'].unique():
            df_strgy_tmp = df_fcst.loc[df_fcst['Location'] == location]
            df_strgy_tmp = fcst.make_forecast_strategy(df_strgy_tmp, item_col='Item', use_location=fcst.use_location)
            df_strgy = pd.concat([df_strgy, df_strgy_tmp]).drop_duplicates()
    else:
        df_strgy = fcst.make_forecast_strategy(df_fcst, item_col='Item', use_location=fcst.use_location)
    if fcst.items_metadata:
        df_meta = io.download_csv(q_name='Qmeta', datalake_path=fcst.results_path)
        if fcst.use_location:
            df_strgy = fmt.concat_item_metadata_with_location(df_strgy, df_meta, item_col='Item',
                                                              location_col='Location')
        else:
            df_strgy = fmt.concat_item_metadata(df_strgy, df_meta, item_col='Item')
    io.upload_csv(df_strgy, q_name='Qstrgy', datalake_path=fcst.results_path)
    io.populate_dbtable(df_strgy,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblStrategy',
                        db_type=io.get_secret()['engine'])
    io.logger.debug('Forecasting strategy completed...')
    io.upload_log()

if __name__ == '__main__':
    main()
    sys.exit(0)