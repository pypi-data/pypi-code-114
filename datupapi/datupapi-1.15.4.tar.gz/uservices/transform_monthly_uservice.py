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

    io.logger.debug('Forecasting monthly starting...')
    df_fcst = io.download_csv(q_name='Qfcst', datalake_path=fcst.results_path, date_cols=['Date'])
    resample_dict = {'Target': 'sum',
                     'SuggestedForecast': 'sum',
                     'SuggestedInterval': 'first',
                     'NextSuggestedForecast': 'sum',
                     'NextSuggestedInterval': 'first',
                     'BackSuggestedForecast': 'sum',
                     'BackSuggestedInterval': 'first',
                     'ForecastCollab': 'sum',
                     'ForecastNaive': 'sum',
                     'ForecastPoint': 'sum',
                     'ForecastLo95': 'sum',
                     'ForecastLo80': 'sum',
                     'ForecastLo60': 'sum',
                     'ForecastUp60': 'sum',
                     'ForecastUp80': 'sum',
                     'ForecastUp95': 'sum',
                     'Ranking': 'first'}
    resample_dict.update({e: 'mean' for e in fcst.error_ids})
    if fcst.use_location:
        #resample_dict.update({'Location': 'first'})
        df_fcst_resample = fmt.resample_dataset_with_location(df_fcst, date_col_='Date', item_col_='Item',
                                                              location_col_='Location',
                                                              frequency_=fcst.upsample_frequency,
                                                              agg_dict_=resample_dict)
    else:
        df_fcst_resample = fmt.resample_dataset(df_fcst, date_col='Date', item_col='Item',
                                                frequency=fcst.upsample_frequency,
                                                agg_dict=resample_dict)
    if fcst.items_metadata:
        df_meta = io.download_csv(q_name='Qmeta', datalake_path=fcst.results_path)
        if fcst.use_location:
            df_fcst_resample = fmt.concat_item_metadata_with_location(df_fcst_resample, df_meta, item_col='Item',
                                                                      location_col='Location')
        else:
            df_fcst_resample = fmt.concat_item_metadata(df_fcst_resample, df_meta, item_col='Item')

    # io.upload_csv(df_fcst_resample, q_name='Qfcst-upsample', datalake_path=fcst.results_path)
    # io.populate_dbtable(df_fcst_resample,
    #                     hostname=io.get_secret()['host'],
    #                     db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
    #                     db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
    #                     table_name='TblUpsample',
    #                     db_type=io.get_secret()['engine'])
    io.logger.debug('Forecasting monthly completed...')
    io.upload_log()


if __name__ == '__main__':
    main()
    sys.exit(0)