import os
import pandas as pd
import sys
import time
import numpy as np
import gc
from tensorflow.keras import backend as K
import datetime
from datupapi.extract.io import IO
from datupapi.training.attup import Attup
from datupapi.predict.forecast import Forecast


def main():

    DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_sim', log_path='output/logs')
    trng =  Attup(config_file=DOCKER_CONFIG_PATH, logfile='data_sim', log_path='output/logs')
    fcst =  Forecast(config_file=DOCKER_CONFIG_PATH, logfile='data_sim', log_path='output/logs')

    io.logger.debug('Data Attup training starting...')

    if (len(trng.sku_impct)==0 or len(trng.items_simulation)==0):
        print("No items to simulate")
    else:
        Qprep = io.download_csv(q_name='Qprep', datalake_path=trng.results_path)
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
            Qfwd=Qfwd.drop(columns=["item_id","location"])
            Qfwd=Qfwd.drop_duplicates(subset="timestamp")
            Qfwd=Qfwd.set_index("timestamp")
            Qfwd.index=pd.to_datetime(Qfwd.index)
            data=pd.concat([data,Qfwd], axis=1)

    #items_simulation=["ethylene_oxide price"]
        items_simulation=trng.items_simulation
        mult=[0.7,0.9,1,1.1,1.3]
        simulation={}
        for k, item_sim in enumerate(items_simulation):
            data_cut=data.copy()
            data_cut[item_sim]=data_cut[item_sim].shift( periods=-trng.forecast_horizon)
            predict={}
            predict_f={}
            new_values={}
            intervals={}
            trng.backtests=0
            trng.input_window=trng.forecast_horizon
            fcst.input_window=fcst.forecast_horizon
            trng.epochs_attup=45
            n_features=1
            n_train=1

            for i in range(50):
                print(i)
                models,data_train_list, scalers_list, n_features=trng.training(data_cut, n_features, n_train)
                predict, ids, new_values=fcst.predict_with_simulation(data_cut,scalers_list, mult=mult, item_sim=item_sim, n_features=n_features, n_train=n_train)
                for j in range(len(mult)):
                    if i==0:
                        predict_f[j]=predict[j]
                        predict_f[j].insert(0, "item_id",ids , True)  
                    else:
                        predict_f[j][str(i)]=predict[j][0].values

            for l in range(len(mult)):
                intervals[l]=l
                intervals[l]=predict_f[l].iloc[:,1:].quantile([.05,0.2,0.4,0.5,0.6,0.8,0.95], axis=1).T
                intervals[l].columns=["Lo95", "Lo80","Lo60","Point","Up60","Up80","Up95"]
                intervals[l]["mean"]=predict_f[l].iloc[:,1:].mean(axis=1)
                intervals[l]["item_id"]=predict_f[l]["item_id"]
                intervals[l]["item_sim"]=item_sim
                intervals[l]["sim_values"]=sum(new_values[l])/len(new_values[l])
                predict[l]=intervals[l].mean().reset_index().set_index("index").T
                predict[l]["item_id"]=intervals[l]["item_id"].unique()
                predict[l]["item_sim"]=intervals[l]["item_sim"].unique()

            simulation[k]=pd.concat(predict, axis=0)
            simulation[k]["index"]=mult
            simulation[k]=simulation[k].set_index("index")

            df_fcst = io.download_csv(q_name='Qfcst', datalake_path=io.results_path, date_cols=['Date'])
            cut_date=datetime.datetime.strftime(pd.to_datetime(df_fcst.sort_values(by="Date").Date.unique()[-trng.forecast_horizon]), '%Y-%m-%d')
            df_fcst=df_fcst[df_fcst.Date>=cut_date]
            SugInt=df_fcst[df_fcst.Item==trng.sku_impct[0]].SuggestedInterval.unique()
            simulation[k]["SuggestedInterval"]=SugInt[0]
            #simulation[k]["OriginalSuggestedForecast"]=df_fcst[df_fcst.Item.isin(trng.sku_impct)].SuggestedForecast.mean()
            simulation[k]["SuggestedForecast"]=simulation[k][SugInt]

        simulation=pd.concat(simulation, axis=0)
        BackSugInt=df_fcst[df_fcst.Item==trng.sku_impct[0]].BackSuggestedInterval.unique()
        simulation["BackSuggestedInterval"]=BackSugInt[0]
        simulation["BackSuggestedForecast"]=simulation[BackSugInt]
        NextSugInt=df_fcst[df_fcst.Item==trng.sku_impct[0]].NextSuggestedInterval.unique()
        simulation["NextSuggestedInterval"]=NextSugInt[0]
        simulation["NextSuggestedForecast"]=simulation[NextSugInt]
        simulation=simulation.reset_index()
        simulation=simulation.drop(columns=["level_0"])
        simulation=simulation.rename(columns={"index":"PercentSimulation","sim_values":"ValueSimulation","item_sim":"ItemSimulation"})
        simulation=simulation[["item_id","ItemSimulation","PercentSimulation","ValueSimulation","SuggestedForecast","SuggestedInterval",'BackSuggestedForecast', 'BackSuggestedInterval','NextSuggestedForecast', 'NextSuggestedInterval']]
        io.upload_csv(simulation, q_name='Qsimulation', datalake_path=trng.results_path+"/simulation/"+trng.string_normalization(trng.sku_impct[0]))

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