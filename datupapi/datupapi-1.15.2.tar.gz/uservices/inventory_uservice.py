import pandas as pd
import os
import sys

from datupapi.extract.io import IO
from datupapi.utils.utils import Utils
from datupapi.prepare.format import Format
from datupapi.inventory.stocks import Stocks

def main():
    DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_io', log_path='output/logs')
    fmt = Format(config_file=DOCKER_CONFIG_PATH, logfile='data_io', log_path='output/logs')
    stks = Stocks(config_file=DOCKER_CONFIG_PATH, logfile='data_io', log_path='output/logs')

    df_prep = io.download_csv(q_name='Qprep', datalake_path = io.results_path, date_cols=['timestamp'])
    df_fcst = io.download_csv(q_name='Qfcst', datalake_path = io.results_path, date_cols=['Date'])
    
    if stks.use_location:
        df_inv = io.download_csv(q_name='Qprep-invopt', datalake_path = io.results_path, types={'Item':str,'Location':str})
    else:
        df_inv = io.download_csv(q_name='Qprep-invopt', datalake_path = io.results_path, types={'Item':str})

    df_inv1 = stks.extract_sales_history(df_prep, df_inv, date_cols = 'timestamp', 
                                         location = stks.use_location).fillna(0)
    df_inv2 = stks.extract_forecast(df_prep, df_fcst, df_inv1, date_cols = 'Date', 
                                    location = stks.use_location, frequency_ = stks.dataset_frequency).fillna(0)

    df_inv2['Availability'] = df_inv2['Inventory'] + df_inv2['InTransit']
    df_inv2['SuggestedAvailability'] = df_inv2['Availability'] - df_inv2['SuggestedForecast']

    df_inv3 = stks.extract_avg_daily(df_prep, df_inv2, date_cols = 'timestamp', location = stks.use_location,
                                     months_= 4, frequency_ = stks.dataset_frequency).fillna(0)

    df_inv3['LeadTimeDemand'] = df_inv3['AvgLeadTime'] * df_inv3['AvgDailyUsage']

    df_inv4 = stks.extract_max_sales(df_prep, df_inv3, date_cols = 'timestamp', location = stks.use_location, 
                                months_ = 4 , frequency_ = stks.dataset_frequency).fillna(0)

    df_inv4['SecurityStock'] = ((df_inv4['MaxDailySales']*df_inv4['MaxLeadTime']) - (df_inv4['AvgDailyUsage']*df_inv4['AvgLeadTime'])).fillna(0)
    df_inv4['SecurityStock'] = df_inv4['SecurityStock'].fillna(0)
    df_inv4['SecurityStock'] = df_inv4['SecurityStock'].map(lambda x: 0 if x < 0 else x)
    df_inv4['SecurityStockDays'] = ((df_inv4['MaxDailySales']*df_inv4['MaxLeadTime']) - (df_inv4['AvgDailyUsage']*df_inv4['AvgLeadTime'])) / (df_inv4['AvgDailyUsage'])
    df_inv4['SecurityStockDays'] = df_inv4['SecurityStockDays'].fillna(0)
    df_inv4['SecurityStockDays'] = df_inv4['SecurityStockDays'].map(lambda x: 0 if x < 0 else x)
    df_inv4['ReorderPoint'] = (df_inv4['LeadTimeDemand'] + df_inv4['SecurityStock'])
    df_inv4['ReorderPoint'] = df_inv4['ReorderPoint'].map(lambda x: 0 if x < 0 else x)
    df_inv4['ReorderPointDays'] = (df_inv4['LeadTimeDemand'] + df_inv4['SecurityStock']) / (df_inv4['AvgDailyUsage'])
    df_inv4['ReorderPointDays'] = df_inv4['ReorderPointDays'].fillna(0)

    df_inv5 = stks.extract_stockout (df_prep, df_inv4)
    df_inv6 = stks.extract_sug_stockout (df_prep, df_inv5)

    df_inv6.drop(columns=['AvgLeadTime','MaxLeadTime','MaxDailySales'],inplace=True)

    names = {'SuggestedForecast':'Forecast',
            'SecurityStock':'SS','SecurityStockDays':'SSDays',
            'ReorderPoint':'ROP','ReorderPointDays':'ROPDays'}
            
    df_inv7 = df_inv6.rename(columns=names)
    
    io.populate_dbtable(df_inv7,
                            hostname=io.get_secret()['host'],
                            db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                            db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                            table_name='TblInventoryOpt',
                            db_type=io.get_secret()['engine'])
    
    io.upload_csv(df_inv7, q_name='Qinvopt', datalake_path=io.results_path)

    io.logger.debug('Results extract and prepare inventory completed...')
    io.upload_log()

    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='prepare_invopt_response', datalake_path=io.response_path)

if __name__ == '__main__':
    main()
    sys.exit(0)