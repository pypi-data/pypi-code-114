

from enum import Enum
from ds_common_tool.suite_base import PriceForecastBase
from ds_common_tool import suite_feature_engineer_sg, suite_model, suite_data
import numpy as np
from datetime import datetime, timedelta

class Message(Enum):
  USE_DF_FETCH_MESSAGE = 'use df_fetch(df_name: string, data_path: string) to add dataframe into the df_list.'
  USE_DF_REMOVE_MESSAGE = 'use df_remove(df_name: string) to remove the dataframe from the df_list.'
  USE_DF_CHECK_MESSAGE = 'use df_display_all() to list all dataframe in the df_list.'
  USE_CHECK_DF_VALID_MESSAGE = 'use check_df_valid(df_name_list: string[]) to check if the dataframe loaded is valid for the training.'

class PriceForecastSGLong(PriceForecastBase):
  def __init__(self, case_name, env = 'localtest', log_level = 0):
    super().__init__(case_name, env)
    self.target_column = 'mean_30'
    self.model_type = 'lstm'
    self.log_level = log_level
    self.check_df_name_list = []
    self.display_hint(log_level, msg = [Message.USE_DF_FETCH_MESSAGE, Message.USE_DF_CHECK_MESSAGE])
  
  # ------------------------------- loading in data [add, check, remove]----------------------------
  def df_fetch(self, path_pre, log_level = 0):
    super().df_fetch(df_name = 'df', data_path = path_pre + 'USEP/USEP-2022.csv')
    super().df_fetch(df_name = 'brent_df', data_path = path_pre + 'BrentPrice.csv')
    super().df_fetch(df_name = 'gas_df', data_path = path_pre + 'future/Gas_Future.csv')
    super().df_fetch(df_name = 'weather_df', data_path = path_pre + 'weather/sg_weather.csv')
    self.check_df_name_list = self.df_dist.keys()
    self.display_hint(log_level, msg = [Message.USE_DF_CHECK_MESSAGE])

  def df_display_all(self, log_level = 0):
    super().df_display_all()
    self.check_df_name_list = self.df_dist.keys()
    self.display_hint(log_level, msg = [Message.USE_DF_FETCH_MESSAGE, Message.USE_DF_REMOVE_MESSAGE])

  def df_remove(self, df_name, log_level = 0):
    super().df_remove(df_name)
    self.check_df_name_list = self.df_dist.keys()
    self.display_hint(log_level, msg = [Message.USE_DF_CHECK_MESSAGE])

  # ----- feature engineer ------
  def check_df_valid(self, df_name_list = [], log_level = 0):
    self.check_df_name_list = df_name_list
    for name in df_name_list:
      if name not in self.df_dist.keys():
        print('dataFrame required: ', name)
        self.display_hint(log_level, msg = [Message.USE_DF_FETCH_MESSAGE, Message.USE_DF_REMOVE_MESSAGE])
        return False
    return True
  
  def feature_engineer(self, feature_columns, target_column = 'mean_30', log_level = 0):
    self.target_column = target_column
    self.feature_columns = feature_columns
    df_l = []
    for df_name in self.check_df_name_list:
      df_l.append(self.df_dist[df_name])
    try:
      self.train_df = suite_feature_engineer_sg.sg_long_term_feature_engineer(df_list = df_l, 
                                                                            feature_columns = self.feature_columns, 
                                                                            target_column = self.target_column)
      print(self.train_df.shape)
      print(self.train_df.columns)
    except:
      self.display_hint(log_level, msg = [Message.USE_CHECK_DF_VALID_MESSAGE])
  
  def check_train_df(self):
    print(self.train_df)
  
  # ------  train model ---------------
  def train_model(self, start_index = '', end_index = '', model_path = ''):
    self.model_path = super().generate_model_path(model_path)
    self.model = suite_model.model_with_data_split(df = self.train_df.copy(), 
                                                   label_column = self.target_column, 
                                                   column_set_index = 'DATE',
                                                   train_start = start_index, 
                                                   train_end = end_index,
                                                   look_back = 30, 
                                                   look_forward = 30, 
                                                   print_model_summary = False,
                                                   epochs = 500, patience = 10,
                                                   early_stop = True, 
                                                   save_model = True, model_path = model_path + 'sg_long_lstm.hdf5',
                                                   save_weight = False, checkpoint_path = './checkpoint', show_loss = True,
                                                   enable_optuna = True, epochs_each_try = 8, n_trials = 5,
                                                   model_name = 'lstm')
    print('----- Completed traning -----')
  
  def get_model(self):
    return self.model
  
  # ----- predict ----- -------------------------------
  def predict(self, path_pre, model_path, feature_columns, start_index):
    self.df_fetch(path_pre)
    self.feature_engineer(feature_columns, target_column = 'mean_30')
    start_d = (datetime.strptime(start_index, '%Y-%m-%d') - timedelta(days = 31)).strftime('%Y-%m-%d')
    end_d = (datetime.strptime(start_index, '%Y-%m-%d') + timedelta(days = 30)).strftime('%Y-%m-%d')
    self.predict_df = suite_data.predict_data_for_nn(df = self.train_df.copy(), 
                                                     target_column = 'mean_30', 
                                                     start_index = start_d,
                                                     end_index = end_d,
                                                     look_back = 30, 
                                                     date_column = 'DATE')
    self.model = suite_model.load_model_by_type(model_path = model_path + 'sg_long_lstm.hdf5', model_type = 'lstm')
    pred_result = suite_model.predict_result(predict_data_list = [self.predict_df], 
                                            model_path=[self.model], 
                                            model_type=['lstm'], 
                                            divideby = [1])
    self.predict_result = np.array(pred_result[0])
  
  def display_predict(self):
    print(self.predict_result)
  
  def get_predict(self):
    print(self.predict_result)

  # -------- support function -------------------
  def display_hint(self, log_level = 0, msg = []):
    self.log_level = log_level
    if self.log_level == 1:
      for item in Message:
        if item in msg:
          print(item.value)
