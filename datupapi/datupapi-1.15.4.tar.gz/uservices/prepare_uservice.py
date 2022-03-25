import os
import pandas as pd
import sys

from datupapi.extract.io import IO
from datupapi.prepare.cleanse import Cleanse
from datupapi.prepare.format import Format


def main():
    io = IO(config_file='config.yml', logfile='data_prepare', log_path='output/logs')
    clns = Cleanse(config_file='config.yml', logfile='data_prepare', log_path='output/logs')
    fmt = Format(config_file='config.yml', logfile='data_prepare', log_path='output/logs')

    io.logger.debug('Data preparation starting...')
    df = io.download_csv(q_name='Qraw',
                         datalake_path=fmt.results_path,
                         types={'Mes': str, 'Semana': str})
    df_items = io.download_csv(q_name='active-items',
                               datalake_path='dev/ramiro/as-is')
    df = clns.clean_metadata(df)
    df = fmt.parse_week_to_date(df,
                                week_col='Semana',
                                date_col='timestamp',
                                drop_cols=['Semana'])
    df = df.rename(columns={fmt.dataset_orig_cols[1]: 'item_id',
                            fmt.dataset_orig_cols[2]: 'demand'
                            }
                   )
    df_sales = df.rename(columns={fmt.dataset_orig_cols[1]: 'item_id',
                                  fmt.dataset_orig_cols[3]: 'demand'
                                  }
                         )
    df['demand'] = df['demand'].map(lambda x: 0 if x < 0 else x)
    df_sales['demand'] = df_sales['demand'].map(lambda x: 0 if x < 0 else x)
    df = pd.merge(df, df_items, on='item_id', how='inner') \
           .drop_duplicates() \
           .sort_values('timestamp', ascending=False)
    df_sales = pd.merge(df_sales, df_items, on='item_id', how='inner') \
                 .drop_duplicates() \
                 .sort_values('timestamp', ascending=False)
    df_meta = fmt.extract_item_metadata(df, item_col='item_id', metadata_cols=fmt.items_metadata)
    df = fmt.reorder_cols(df[['timestamp', 'item_id', 'demand']], first_cols=['timestamp', 'item_id', 'demand'])
    df_sales = fmt.reorder_cols(df_sales[['timestamp', 'item_id', 'demand']], first_cols=['timestamp', 'item_id', 'demand'])
    io.upload_csv(df, q_name='Qprep', datalake_path=fmt.results_path)
    io.upload_csv(df_sales, q_name='Qprep-sales', datalake_path=fmt.results_path)
    io.upload_csv(df_meta, q_name='Qmeta', datalake_path=fmt.results_path)
    io.populate_dbtable(df_meta,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'],
                        db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'],
                        port=io.get_secret()['port'],
                        table_name='TblItemMetadata',
                        db_type=io.get_secret()['engine'])
    io.logger.debug('Data preparation completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='prepare_response', datalake_path=io.response_path)

if __name__ == '__main__':
    main()
    sys.exit(0)
