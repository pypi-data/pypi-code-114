import os
import warnings
import pandas as pd
import featurewiz as FW
import numpy as np
import tensorflow as tf
import tensorboard as tb

import copy
from pathlib import Path
import warnings

import numpy as np
import pytorch_lightning as pl
from pytorch_lightning.callbacks import EarlyStopping, LearningRateMonitor, ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger
import torch

from pytorch_forecasting import Baseline, TemporalFusionTransformer, TimeSeriesDataSet, DeepAR, NBeats
from pytorch_forecasting.data import GroupNormalizer, EncoderNormalizer
from pytorch_forecasting.metrics import SMAPE, PoissonLoss, QuantileLoss, MASE, MAPE, MAE, NormalDistributionLoss
from pytorch_forecasting.models.temporal_fusion_transformer.tuning import optimize_hyperparameters

import os
import sys
import time
import gc
from tensorflow.keras import backend as K
from dateutil.relativedelta import relativedelta
from datetime import datetime

from datupapi.extract.io import IO
from datupapi.training.tft import Tft

def main():
    DOCKER_CONFIG_PATH = os.path.join('/opt/ml/processing/input', 'config.yml')
    io = IO(config_file=DOCKER_CONFIG_PATH, logfile='data_training', log_path='output/logs')
    trng =  Tft(config_file=DOCKER_CONFIG_PATH, logfile='data_training', log_path='output/logs')
    trng.n_iter_tft=1 
    data1, scalers,  Qprep, suffix, known, unknown, group_ids, test_data, n_features, item_location, categorical= trng.prepare_data(normalization=trng.normalization)

    #Training loop
    tf.io.gfile = tb.compat.tensorflow_stub.io.gfile
    predict={}
    aux2={}
    test_predictions={}
    for i in range(0,trng.backtests+1):
        print("Features: ", n_features)
        print("Unknown variables: ")
        print(*unknown, sep = ", ") 
        print("Forecast_horizon: ", trng.forecast_horizon)
        print("Input_window: ", trng.input_window)
        print("Backtest: ", i)
        training_cutoff = data1["time_idx"].max() - trng.forecast_horizon*i
        training=trng.create_training_dataset(data1=data1, training_cutoff=training_cutoff, group_ids=group_ids,max_encoder_length= trng.input_window, max_prediction_length=trng.forecast_horizon, unknown= unknown,known=known, categorical=categorical)
        # create validation set (predict=True) which means to predict the last max_prediction_length points in time
        # for each series
        validation = TimeSeriesDataSet.from_dataset(training, data1[data1.time_idx <= (data1["time_idx"].max() - trng.forecast_horizon*(i-1))], predict=True, stop_randomization=True) if i != 0 else None
        # create dataloaders for model
        train_dataloader = training.to_dataloader(train=True, batch_size=trng.batch_size_tft , num_workers=0)
        val_dataloader = validation.to_dataloader(train=False, batch_size=trng.batch_size_tft*10, num_workers=0) if i != 0 else None 
        print("Training cutoff: ", training_cutoff)
        #Baseline error
        if i != 0:
            actuals = torch.cat([y for x, (y, weight) in iter(val_dataloader)])
            baseline_predictions = Baseline().predict(val_dataloader)
            print("Baseline error: ",(actuals - baseline_predictions).abs().mean().item())
        for j in range(trng.n_iter_tft):
        # configure network and trainer
            early_stop_callback = EarlyStopping(monitor="val_loss", min_delta=1e-4, patience=10, verbose=False, mode="min") if i != 0 else None          
            lr_logger = LearningRateMonitor()  # log the learning rate
            logger = TensorBoardLogger("lightning_logs")  # logging results to a tensorboard
            checkpoint_callback_forecast = ModelCheckpoint(verbose=True, monitor="train_loss", mode="min" )
            checkpoint_callback = ModelCheckpoint(verbose=True, monitor="val_loss", mode="min" )
            callbacks=[ checkpoint_callback_forecast] if i == 0 else [lr_logger, early_stop_callback, checkpoint_callback]
            #trainer = trng.create_trainer(callbacks, logger, strategy="ddp_find_unused_parameters_false", accelerator="auto" )
            trainer = trng.create_trainer(callbacks, logger )


            #define TFT
            tft= trng.create_tft(training)

            #training
            torch.set_num_threads(10)
            if i != 0:
                trainer.fit(tft, train_dataloader=train_dataloader, val_dataloaders=val_dataloader )
            else:
                trainer.fit(tft, train_dataloaders=train_dataloader)
                
            best_model_path = trainer.checkpoint_callback.best_model_path
            best_tft = TemporalFusionTransformer.load_from_checkpoint(best_model_path)
            
            # raw predictions are a dictionary from which all kind of information including quantiles can be extracted
            if i != 0:
                # calcualte mean absolute error on validation set
                actuals = torch.cat([y[0] for x, y in iter(val_dataloader)])
                predictions = best_tft.predict(val_dataloader)
                print("Error: ",(actuals - predictions).abs().mean())
                raw_predictions, x = best_tft.predict(val_dataloader, mode="raw", return_x=True)
                del predictions, actuals
            else:
                raw_predictions, x = best_tft.predict(test_data, mode="raw", return_x=True)
            del x, best_tft, tft
            aux=pd.DataFrame(raw_predictions["prediction"].numpy().reshape(n_features*trng.forecast_horizon , 7))         
            a = aux.values
            a.sort(axis=1)  
            a = a[:, ::1]
            aux=pd.DataFrame(a, aux.index, aux.columns)    
            predict[i] = aux if j==0 else predict[i]+aux 
            del a, aux, raw_predictions, trainer
            gc.collect()
        #Find intervals
        predict[i]=predict[i]/trng.n_iter_tft
        predict[i].columns=["p5","p20","p40","p50","p60","p80","p95"]
        if trng.use_location:
            predict[i].insert(7, "item_id", np.repeat(item_location.item_id.values ,trng.forecast_horizon ))  
            predict[i].insert(8, "location", np.repeat(item_location.location.values ,trng.forecast_horizon )) 
        else: 
            predict[i].insert(7, "item_id", np.repeat(data1.item_id.unique(), trng.forecast_horizon))
        predict[i].insert(8, "time_idx", np.tile(np.arange(data1.time_idx.max()+1-trng.forecast_horizon*i,data1.time_idx.max()+1+trng.forecast_horizon*(1-i)), n_features))

    if trng.normalization:
      for i in range(0, trng.backtests+1):
        predict[i]=trng.rescale(scalers,predict[i])
      data1= trng.prepare_data(normalization=False)
      Qprep=data1[2]
      suffix=data1[3]
      data1=data1[0]

    predict=trng.add_dates(Qprep,data1, predict, suffix)
    predict=trng.clean_negatives(predict)
    forecast=predict[0]
 
    backtest=pd.DataFrame()
    for k in range(trng.backtests):
        backtest=pd.concat([backtest,predict[k+1]])
 
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