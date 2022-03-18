import pandas as pd
from enum import Enum
import subprocess
import sys

class ENV(Enum):
  LOCAL_TEST = 'localtest'
  EAP = 'eap'

class PriceForecastBase:
  def __init__(self, case_name, env):
     self.name = case_name
     self.env = env
     self.df_dist = {}
     self.feature_columns = []
     self.target_column = ''
     self.train_df = None
     self.predict_df = None
     self.model = None
     self.model_type = ''
     self.model_path = ''
     self.predict_result = []
    
  def generate_model_path(self, model_path = ''):
     if self.model_type in ['lstm', 'tcn', 'transformer']:
       self.model_path = model_path + '.hdf5'
     if self.model_type in ['xgb']:
       self.model_path = model_path + '.pkl'
     if self.model_type in ['linear']:
       self.model_path = model_path + '.sav'
  
  def get_model_path(self):
    return self.model_path

  def df_fetch(self, df_name, data_path):
    if self.env == ENV.EAP.value:
      self.install_lib('eapdataset')
      from eapdataset import  Dataset
      dataset = Dataset.get_by_name(df_name)
      df = dataset.to_pandas_dataframe(use_cached_result=False)
    if self.env == ENV.LOCAL_TEST.value:
      df = pd.read_csv(data_path, thousands=',')
    self.df_dist[df_name] = df
    self.check_df_name_list = self.df_dist.keys()
  
  def df_remove(self, df_name):
    self.df_dist.pop(df_name)
    self.check_df_name_list = self.df_dist.keys()
  
  def df_display_all(self):
    print(self.df_dist)
  
  def feature_engineer(self):
    self.train_df = self.df_dist[self.df_dist.keys()[0]]

  def train_model(self):
    pass

  def predict(self):
    pass

  def get_model(self):
    return self.model
  
  def get_predict(self):
    return self.predict_result
  
  def install_lib(self, package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
