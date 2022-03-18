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

class PriceForecastSGShort(PriceForecastBase):
  def __init__(self, case_name = 'short', env = 'localtest', log_level = 0):
    super().__init__(case_name, env)
    self.target_column = 'USEP'
    self.model_type = 'xgb'
    self.log_level = log_level
    self.check_df_name_list = []
    self.display_hint(log_level, msg = [Message.USE_DF_FETCH_MESSAGE, Message.USE_DF_CHECK_MESSAGE])
  
  # ------------------------------- loading in data [add, check, remove]----------------------------
  def df_fetch(self, path_pre, log_level = 0):
    super().df_fetch(df_name = 'usep-48', data_path = path_pre + 'USEP/USEP-REG-2022.csv')
    super().df_fetch(df_name = 'usep-advisory', data_path = path_pre + 'Other/advisory.csv')
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
  
  def feature_engineer(self, feature_columns = None, target_column = 'USEP', log_level = 0):
    self.target_column = target_column
    df_l = []
    for df_name in self.check_df_name_list:
      df_l.append(self.df_dist[df_name])
    try:
      self.train_df = suite_feature_engineer_sg.sg_short_term_feature_engineer(df_list = df_l, 
                                                                               targetvariable = self.target_column, 
                                                                               no_of_period = 12, 
                                                                               divideby = 10)
      print(self.train_df.shape)
      print(self.train_df.columns)
    except:
      self.display_hint(log_level, msg = [Message.USE_CHECK_DF_VALID_MESSAGE])
  
  def check_train_df(self):
    print(self.train_df)
  
  # ------  train model ---------------
  def train_model(self, start_index = '', end_index = '', model_path = '', n_trials = 10):
    super().generate_model_path(model_path)
    self.model = suite_model.xgb_with_optuna(df = self.train_df, 
                                             label_column = self.target_column, 
                                             column_set_index = 'DATE', start_index = start_index, end_index = end_index, 
                                             save_model = True, model_path = self.model_path, 
                                             enable_optuna = True, n_trials = n_trials)
    print('----- Completed traning -----')
  
  def get_model(self):
    return self.model
  
  # ----- predict ----- -------------------------------
  def predict(self, path_pre, model_path, feature_columns, start_index):
    self.df_fetch(path_pre)
    self.feature_engineer(feature_columns, target_column = 'mean_30')
    start_d = (datetime.strptime(start_index, '%Y-%m-%d') - timedelta(days = 31)).strftime('%Y-%m-%d')
    end_d = (datetime.strptime(start_index, '%Y-%m-%d') + timedelta(days = 30)).strftime('%Y-%m-%d')
    self.predict_df = suite_data.predict_data(df = self.predict_df, 
                                              target_column = 'USEP', 
                                              look_back = 48, 
                                              start_index = start_d, end_index = end_d,
                                              date_column = 'DATE')
    self.model = suite_model.load_model_by_type(model_path = model_path + 'sg_usep.pkl', model_type = 'xgb')
    pred_result = suite_model.predict_result(predict_data_list = [self.predict_df], 
                                            model_path=[self.model], 
                                            model_type=['xgb'],
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
