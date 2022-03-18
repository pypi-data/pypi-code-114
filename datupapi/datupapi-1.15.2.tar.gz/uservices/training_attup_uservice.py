import os
import pandas as pd
import sys
import time
import numpy as np
import gc
from tensorflow.keras import backend as K

from datupapi.extract.io import IO
from datupapi.training.attup import Attup
from datupapi.predict.forecast import Forecast


def main():
    DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_training', log_path='output/logs')
    trng =  Attup(config_file=DOCKER_CONFIG_PATH, logfile='data_training', log_path='output/logs')
    fcst =  Forecast(config_file=DOCKER_CONFIG_PATH, logfile='data_forecasting', log_path='output/logs')
    io.logger.debug('Data Attup training starting...')

    Qprep =  io.download_object_csv(datalake_path=trng.dataset_import_path[0])
    if trng.use_location:
        Qprep["item_id"]=Qprep.apply(lambda row: (str(row["item_id"])+"-"+str(row["location"])),axis=1)
        Qprep=Qprep[["timestamp","item_id","demand"]]
     
    data_date,_=trng.transform_to_matrix(Qprep, value=0)
    n_features=len(data_date.columns)-1
    for_loc=[]
    
    data_date=data_date.set_index("Date")
    data_date=data_date.reindex(sorted(data_date.columns), axis=1)
    data_date=fcst.reorder_impct_columns(data_date).reset_index() if len(trng.sku_impct)>0 else data_date.reset_index()
    data=trng.add_date_features(data_date)

    if len(trng.dataset_import_path)==2:
            Qfwd = io.download_object_csv(datalake_path=trng.dataset_import_path[1])
            data=trng.join_related_dataset(Qfwd, data_date, data)
    if len(trng.dataset_import_path)==3:
            if trng.dataset_import_path[1] !="":
                Qfwd = io.download_object_csv(datalake_path=trng.dataset_import_path[1])
                data=trng.join_related_dataset(Qfwd, data_date, data)
            Qfwd = io.download_object_csv(datalake_path=trng.dataset_import_path[2])
            Qfwd=Qfwd.drop_duplicates(subset="timestamp")
            Qfwd=Qfwd.set_index("timestamp")
            Qfwd.index=pd.to_datetime(Qfwd.index)
            data=pd.concat([data,Qfwd], axis=1)
    n_train=0
    models,data_train_list, scalers_list, n_features=trng.training(data, n_features, n_train)  
    predict, models, predictions=fcst.prediction(data,models,data_train_list, scalers_list,n_features, n_train)
    del models, scalers_list, data_train_list
    gc.collect()
    K.clear_session()

    data=data.iloc[:,:n_features]
    multip=[]
    
    for j in range(n_features):
        multip=np.append(multip,[9,6,3])
    multip=multip.reshape(n_features, 3)
    predict=fcst.intervals(data=data,predict=predict, n_features=n_features,predictions=predictions, mult=multip)
    predict=trng.add_dates(data_date,data, predict, n_features, for_loc)
    predict=trng.clean_negatives(predict)  


    forecast=predict[0]
    backtest=pd.DataFrame()
    for k in range(trng.backtests):
        backtest=pd.concat([backtest,predict[k+1]])
    if trng.use_location:
        backtest["location"]=backtest.apply(lambda row: row["item_id"].split("-")[1], axis=1)
        backtest["item_id"]=backtest.apply(lambda row: row["item_id"].split("-")[0], axis=1)
        columns=["item_id","location","timestamp", "target_value","backtestwindow_start_time","backtestwindow_end_time", "p5","p20","p40","p50","p60","p80","p95"]
        backtest=backtest[columns]
        forecast["location"]=forecast.apply(lambda row: row["item_id"].split("-")[1], axis=1)
        forecast["item_id"]=forecast.apply(lambda row: row["item_id"].split("-")[0], axis=1)
        columns=["item_id","location", "date", "p5","p20","p40","p50","p60","p80","p95"]
        forecast=forecast[columns]
    io.upload_csv(backtest,q_name='forecasted-values', datalake_path=trng.backtest_export_path)
    io.upload_csv(forecast,q_name='forecast', datalake_path=trng.forecast_export_path)    

    io.logger.debug('Data Attup training completed...')
    io.upload_log()
    # Microservice response
    response = {
        'ConfigFileUri': os.path.join('s3://', io.datalake, io.config_path, 'config.yml')
    }
    io.upload_json_file(message=response, json_name='training_response', datalake_path=io.response_path)


if __name__ == '__main__':
    main()
    sys.exit(0)