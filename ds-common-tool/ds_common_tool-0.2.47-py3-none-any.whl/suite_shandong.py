from ds_common_tool.suite_base import PriceForecastBase
from ds_common_tool import suite_feature_engineer_tt, suite_model, suite_data
from datetime import datetime, timedelta


class PriceForecastShanDong(PriceForecastBase):
  def __init__(self, case_name = 'shandong', node_id = '', env = 'localtest', log_level = 0):
    super().__init__(case_name, env)
    self.node_id = node_id
    self.target_column = '日前_电价(元/MWh)'
    self.feature_columns = ['出清前_竞价空间1','hour','出清前_新能源预测','time','出清前_竞价空间1_max','出清前_竞价空间1_mean','出清前_竞价空间1_min']
    self.model_type = 'xgb'
    self.log_level = log_level
    self.check_df_name_list = []
  
  # ------------------------------- loading in data [add, check, remove]----------------------------
  def df_fetch(self, path_pre):
    super().df_fetch(df_name = 'shandong-zhangjiachan', data_path = path_pre + 'Other/shandong_zhangjiachan.csv')
    self.check_df_name_list = self.df_dist.keys()

  def df_display_all(self):
    super().df_display_all()
    self.check_df_name_list = self.df_dist.keys()

  def df_remove(self, df_name):
    super().df_remove(df_name)
    self.check_df_name_list = self.df_dist.keys()

  # ----- feature engineer ------
  def check_df_valid(self, df_name_list = []):
    self.check_df_name_list = df_name_list
    for name in df_name_list:
      if name not in self.df_dist.keys():
        print('dataFrame required: ', name)
        return False
    return True
  
  def feature_engineer(self):
    df_l = []
    for df_name in self.check_df_name_list:
      df_l.append(self.df_dist[df_name])
    try:
      data = suite_feature_engineer_tt.shandong_feature_engineer(df_shandong = df_l[0], 
                                                                          feature_columns = self.feature_columns, 
                                                                          label_column = self.target_column)
      self.train_df = data['2021-12-01 00:00:00' : '2022-02-28 23:45:00']
      print(self.train_df.shape)
      print(self.train_df.columns)
    except:
      pass
  
  def check_train_df(self):
    print(self.train_df)
  
  # ------  train model ---------------
  def train_model(self, start_index = '', end_index = '', model_path = '', n_trials = 10):
    self.model_path = super().generate_model_path(model_path)
    self.model = suite_model.xgb_with_optuna(df = self.train_df, 
                                             label_column = self.target_column, 
                                             column_set_index = 'DATE', start_index = start_index, end_index = end_index, 
                                             save_model = True, model_path = model_path + '.pkl', 
                                             enable_optuna = True, n_trials = n_trials)
    print('----- Completed traning -----')
  
  def get_model(self):
    return self.model
  
  # ----- predict ----- -------------------------------
  def predict(self, model_path, start_index, end_index = '', path_pre = ''):
    self.df_fetch(path_pre)
    self.feature_engineer()
    # start_d = (datetime.strptime(start_index, '%Y-%m-%d') - timedelta(days = 31)).strftime('%Y-%m-%d')
    # end_d = (datetime.strptime(start_index, '%Y-%m-%d') + timedelta(days = 30)).strftime('%Y-%m-%d')
    self.predict_df = suite_data.predict_data(df = self.predict_df, 
                                              target_column = self.target_column, 
                                              look_back = 96, 
                                              start_index = start_index, end_index = end_index,
                                              date_column = 'DATE')
    self.model = suite_model.load_model_by_type(model_path = self.model_path, model_type = 'xgb')
    pred_result = suite_model.predict_result(predict_data_list = [self.predict_df], 
                                            model_path=[self.model], 
                                            model_type=['xgb'],
                                            divideby = [1])
    self.predict_result = pred_result[0]
  
  def display_predict(self):
    print(self.predict_result)
  
  def get_predict(self):
    print(self.predict_result)
