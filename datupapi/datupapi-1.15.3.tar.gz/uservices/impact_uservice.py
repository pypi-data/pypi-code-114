import os
import pandas as pd
import sys
import time
import numpy as np
from datupapi.extract.io import IO
from datupapi.training.attup import Attup
from datupapi.predict.forecast import Forecast
from datupapi.feateng.relation import Relation

   

def main():

    DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='impact', log_path='output/logs')
    trng = Attup(config_file=DOCKER_CONFIG_PATH, logfile='impact', log_path='output/logs')
    fcst =  Forecast(config_file=DOCKER_CONFIG_PATH, logfile='impact', log_path='output/logs')
    rltn =  Relation(config_file=DOCKER_CONFIG_PATH, logfile='impact', log_path='output/logs')
    trng.save_last_epoch=True
    
    if trng.sku_impct == False:
        print("No SKUs found")
    else:
        Qprep = io.download_csv(q_name='Qprep', datalake_path=trng.results_path)
        table = str.maketrans(dict.fromkeys("()"))
        if all(item in Qprep.item_id.unique()  for item in trng.sku_impct):
            for item in trng.sku_impct:
                Qprep = io.download_csv(q_name='Qprep', datalake_path=trng.results_path)
                if trng.use_location:
                    Qprep["item_id"]=Qprep.apply(lambda row: (str(row["item_id"])+"-"+str(row["location"])),axis=1)
                    Qprep=Qprep[["timestamp","item_id","demand"]]
                data_date,_=trng.transform_to_matrix(Qprep, value=0)
                data_date=data_date.set_index("Date")
                impct_columns=[item]
                n_features=1
                reindex_col=impct_columns.copy()
                reindex_col.extend(data_date.columns[np.logical_not(data_date.columns.isin(impct_columns))])
                data_date = data_date.reindex(columns=reindex_col)
                data_date=data_date.reset_index()
                #data = data_date.iloc[:, 1:]
                data=trng.add_date_features(data_date)
                
                models,data_train_list, scalers_list, n_features=trng.training(data, n_features, n_train=1)
                df_importance_f= fcst.relative_importance(data)
                df_importance_f=df_importance_f.round(2)
                df_importance_f.columns=["Item",(trng.string_normalization(item.translate(table)))]
                #######
                correlation_matrix=rltn.correlation(data, list_columns=impct_columns)            
                #######
                data = data_date.iloc[:, 1:]
                _,data=trng.min_max_scaler(data)
                #data=data.drop(columns=["etileno cntp (cents per pound)","etileno cbp (cents per pound)","etileno cntp (us per metric ton)","etileno spa (cents per pound)","etileno spa (us per metric ton)"])
                Qcausal=rltn.causality(data,item)

                io.upload_csv(df_importance_f, q_name='Qimpct', datalake_path=trng.results_path+"/importancia/"+trng.string_normalization(item))
                io.upload_csv(correlation_matrix, q_name='Qcorrelation', datalake_path=trng.results_path+"/importancia/"+trng.string_normalization(item))
                io.upload_csv(Qcausal, q_name='Qcausal', datalake_path=trng.results_path+"/importancia/"+trng.string_normalization(item))
                
            io.populate_dbtable(df_importance_f,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblImpact',
                        db_type=io.get_secret()['engine'])
            io.populate_dbtable(correlation_matrix,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblCorrelation',
                        db_type=io.get_secret()['engine'])
            io.populate_dbtable(Qcausal,
                        hostname=io.get_secret()['host'],
                        db_user=io.get_secret()['username'], db_passwd=io.get_secret()['password'],
                        db_name=io.get_secret()['dbname'], port=io.get_secret()['port'],
                        table_name='TblCausality',
                        db_type=io.get_secret()['engine'])
        else:
            print("A sku doesn't belong to the dataset")
    io.logger.debug('Data Attup impact completed...')
    io.upload_log()

if __name__ == '__main__':
    main()
    sys.exit(0)