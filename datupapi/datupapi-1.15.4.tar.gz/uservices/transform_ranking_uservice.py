import os
import sys
import dateutil.relativedelta

import pandas as pd
from datetime import datetime
from datupapi.extract.io import IO
from datupapi.prepare.format import Format
from datupapi.transform.ranking import Ranking
from pandas.tseries.offsets import MonthEnd


def main():
    #DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    DOCKER_CONFIG_PATH = os.path.join('./', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_ranking', log_path='output/logs')
    fmt = Format(config_file=DOCKER_CONFIG_PATH, logfile='data_ranking', log_path='output/logs')
    rnkg = Ranking(config_file=DOCKER_CONFIG_PATH, logfile='data_ranking', log_path='output/logs')

    io.logger.debug('Items ranking starting...')
    df = io.download_csv(q_name='Qprep', datalake_path=rnkg.results_path)
    df_sales = io.download_csv(q_name='Qprep-sales', datalake_path=rnkg.results_path)

    lastdate = pd.to_datetime(str(df['timestamp'].max()), format='%Y-%m-%d')
    print(lastdate.strftime('%Y-%m-%d'))
    if fmt.dataset_frequency == 'M':
        if str(lastdate)[5:7] == '02':
            fecha_target = lastdate - dateutil.relativedelta.relativedelta(months=2)
            fecha_target = pd.to_datetime(fecha_target, format='%Y-%m-%d')+MonthEnd(1)
            fecha_target = fecha_target.strftime('%Y-%m-%d')

        else:
            fecha_target = lastdate - dateutil.relativedelta.relativedelta(months=2)
            fecha_target = pd.to_datetime(fecha_target, format='%Y-%m-%d')
            fecha_target = fecha_target.strftime('%Y-%m-%d')
        print(fecha_target)

    elif fmt.dataset_frequency == '2M':
        fecha_target = lastdate - dateutil.relativedelta.relativedelta(months=4)
        fecha_target = pd.to_datetime(fecha_target, format='%Y-%m-%d')
        fecha_target = fecha_target.strftime('%Y-%m-%d')
        print(fecha_target)

    elif fmt.dataset_frequency == 'Q':
        fecha_target = lastdate - dateutil.relativedelta.relativedelta(months=6)
        fecha_target = pd.to_datetime(fecha_target, format='%Y-%m-%d')
        fecha_target = fecha_target.strftime('%Y-%m-%d')
        print(fecha_target)

    elif fmt.dataset_frequency == 'W':
        fecha_target = lastdate - dateutil.relativedelta.relativedelta(months=3)
        fecha_target = pd.to_datetime(fecha_target, format='%Y-%m-%d')
        fecha_target = fecha_target.strftime('%Y-%m-%d')
        print(fecha_target)

    else:
        print('No se especifico frecuencia')

    df = df[df['timestamp'] >= fecha_target]
    df_sales = df_sales[df_sales['timestamp'] >= fecha_target]

    df = rnkg.format_ranking_dataset(df)
    df_sales = rnkg.format_ranking_dataset(df_sales)
    if rnkg.use_location:
        df_rank = pd.DataFrame()
        for location in df['Location'].unique():
            df_ = df.loc[df['Location'] == location]
            df_sales_ = df_sales.loc[df_sales['Location'] == location]
            df_ = fmt.pivot_dates_vs_items(df_, date_col='Date', item_col='Item', qty_col='Target')
            df_sales_ = fmt.pivot_dates_vs_items(df_sales_, date_col='Date', item_col='Item', qty_col='Target')
            df_abc = rnkg.rank_abc(df_sales_, item_col='Item', rank_col='Target', threshold=rnkg.abc_threshold)
            df_fsn = rnkg.rank_fsn(df_, item_col='Item', rank_col='Target', threshold=rnkg.fsn_threshold)
            df_xyz = rnkg.rank_xyz(df_, item_col='Item', rank_col='Target', threshold=rnkg.xyz_threshold)
            df_ = rnkg.concat_ranking(df_abc, df_fsn, df_xyz, item_col='Item')
            df_['Location'] = location
            df_rank = pd.concat([df_rank, df_], axis='rows').drop_duplicates()
    else:
        df = fmt.pivot_dates_vs_items(df, date_col='Date', item_col='Item', qty_col='Target')
        df_sales = fmt.pivot_dates_vs_items(df_sales, date_col='Date', item_col='Item', qty_col='Target')
        df_abc = rnkg.rank_abc(df_sales, item_col='Item', rank_col='Target', threshold=rnkg.abc_threshold)
        df_fsn = rnkg.rank_fsn(df, item_col='Item', rank_col='Target', threshold=rnkg.fsn_threshold)
        df_xyz = rnkg.rank_xyz(df, item_col='Item', rank_col='Target', threshold=rnkg.xyz_threshold)
        df_rank = rnkg.concat_ranking(df_abc, df_fsn, df_xyz, item_col='Item')
    if rnkg.items_metadata:
        df_meta = io.download_csv(q_name='Qmeta', datalake_path=rnkg.results_path)
        if rnkg.use_location:
            df_rank = fmt.concat_item_metadata_with_location(df_rank, df_meta, item_col='Item', location_col='Location')
        else:
            df_rank = fmt.concat_item_metadata(df_rank, df_meta, item_col='Item')
    '''io.upload_csv(df_rank, q_name='Qrank', datalake_path=rnkg.results_path)
    io.populate_dbtable(df_rank,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblRanking',
                        db_type=io.get_secret()['engine'])
    io.populate_snowflake_table(df_rank,
                                dwh_account=io.get_secret()['account'],
                                dwh_name=io.get_secret()['warehouse'],
                                dwh_user=io.get_secret()['user'],
                                dwh_passwd=io.get_secret()['password'],
                                dwh_dbname=io.get_secret()['database'],
                                dwh_schema=io.get_secret()['schema'],
                                table_name='TblRanking'
                                )'''
    io.logger.debug('Items ranking completed...')
    io.upload_log()


if __name__ == '__main__':
    main()
    sys.exit(0)
