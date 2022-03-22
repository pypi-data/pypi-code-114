#----- 1st Mar 2022 -----------#
#----- ZhangLe ----------------#
#----- Feature Engineering-----#

import pandas as pd
from ds_common_tool import suite_data

def sg_long_term_feature_engineer(df_list, feature_columns, target_column):
  df = df_list[0]
  brent_df = df_list[1]
  gas_df = df_list[2]
  weather_df = df_list[3]
  if (df.shape[0] < 100) or (df.shape[1] < 4):
    print('please check usep dataframe shape')
    return None
  if (brent_df.shape[0] < 100) or (brent_df.shape[1] < 6):
    print('please check brent dataframe shape')
    return None
  if (gas_df.shape[0] < 100) or (gas_df.shape[1] < 5):
    print('please check gas future dataframe shape')
    return None
  if (weather_df.shape[0] < 100) or (weather_df.shape[1] < 7):
    print('please check weather future dataframe shape')
    return None
  new_df = suite_data.add_period_to_time(df, 'DATE', 'PERIOD', 30)
  new_df.set_index('DATE', inplace=True)
  new_df = suite_data.remove_outlier(new_df, 'USEP', n_outlier=0.25)
  new_df = new_df.resample('D').mean()
  new_df = suite_data.get_n_rolling(new_df, 'USEP', n=30, method='mean')
  brent_data   = suite_data.read_data_external(brent_df, new_df, 'Date', 5)
  gas_data     = suite_data.read_data_external(gas_df, new_df, 'DATE', 5)
  weather_data = suite_data.read_data_external(weather_df, new_df, 'DATE', 5)
  all_data = suite_data.merge_dfs(df_list = [new_df, brent_data, gas_data, weather_data], on_column = 'DATE')
  df1 = all_data[['DATE', 'RNGC1']]
  df2 = all_data[['DATE', 'Close/Last']]
  df3 = all_data[['DATE', 'humidity']]
  df1 = suite_data.shift_row(df1, target_columns='RNGC1', shift_n_list = [-30])
  df2 = suite_data.shift_row(df2, target_columns='Close/Last', shift_n_list = [-30])
  df3 = suite_data.shift_row(df3, target_columns='humidity', shift_n_list = [-30])
  all_data = suite_data.merge_dfs(df_list = [all_data, 
                                             df1[['DATE', 'RNGC1_-30']], 
                                             df2[['DATE', 'Close/Last_-30']], 
                                             df3[['DATE', 'humidity_-30']]], on_column = 'DATE')
  all_data = all_data[feature_columns]
  all_data = suite_data.get_trend_mean(all_data, date_column_name = 'DATE')
  all_data = suite_data.switch_y_column(all_data, column_name=target_column)
  if (all_data.shape[0] < 100) or (all_data.shape[1] < 80):
    print('please check data processing function... data_shape is now :', all_data.shape)
  return all_data


def sg_short_term_feature_engineer(df_list, targetvariable = 'USEP', no_of_period = 12, divideby =10):
    df_usep = df_list[0]
    df_adv = df_list[1]
    df_usep['DATE'] = pd.to_datetime(df_usep['DATE'])
    df_adv['DATE'] = pd.to_datetime(df_adv['DATE'])
    df_adv = df_adv.groupby(['DATE', 'PERIOD']).max().reset_index()
    df_adv['DAYOFWEEK'] = df_adv.DATE.map(lambda x:x.dayofweek+1)
    merged_df = df_adv.merge(df_usep, on=['DATE', 'PERIOD'], how='left').fillna(0)
    if targetvariable == 'USEP':
      becomefeature = 'REG'
      merged_df = merged_df[['DATE','PERIOD', 'DEMAND', 'USEP', 'REG', 'DAYOFWEEK', 
                           'energy_shortfall_amt', 'reserve_shortfall_amt', 'regulation_shortfall_amt',
                           'abnormal_condition_type_Major Equipment Outage', 'abnormal_condition_type_Other',
                           'load_scenario_High', 'load_scenario_Low', 'load_scenario_Medium']]
    elif targetvariable == 'REG':
      becomefeature = 'USEP'
      merged_df = merged_df[['DATE','PERIOD', 'DEMAND', 'USEP', 'DAYOFWEEK', 
                           'energy_shortfall_amt', 'reserve_shortfall_amt', 'regulation_shortfall_amt',
                           'abnormal_condition_type_Major Equipment Outage', 'abnormal_condition_type_Other',
                           'load_scenario_High', 'load_scenario_Low', 'load_scenario_Medium']]
    merged_df.columns = ["DATE", "PERIOD", "DEMAND", "USEP", "REG", "DAYOFWEEK", "LOAD_SHORTFALL",
                         "RES_SHORTFALL", "REG_SHORTFALL", "ABNORMAL_OUTAGE", "ABNORMAL_OTHER", "PRICE_WARNING",
                         "PRICE_REVISION", "PROVISIONAL_PRICES"]
    merged_df['load_scenario_High'] = 0
    merged_df['load_scenario_Medium'] = 0
    merged_df['load_scenario_Low'] = 0
    merged_df = suite_data.add_period_to_time(merged_df, 'DATE', 'PERIOD', 30)
    merged_df = pd.get_dummies(merged_df, columns=['PERIOD','DAYOFWEEK'])
    merged_df['month'] = merged_df.DATE.map(lambda x:x.month)
    merged_df['day'] = merged_df.DATE.map(lambda x:x.day)
    for period in range(no_of_period + 1):
      merged_df['Value_prev' + str(period + 1)] = merged_df['REG'].shift(period + 1).fillna(method='bfill')
    merged_df['Value_max_12'] = merged_df['REG'].rolling(window=12, min_periods=1).max()
    merged_df['Value_min_12'] = merged_df['REG'].rolling(window=12, min_periods=1).min()
    merged_df['Value_mean_12'] = merged_df['REG'].rolling(window=12, min_periods=1).mean()
    merged_df['Value_std_12'] = merged_df['REG'].rolling(window=12, min_periods=1).std().fillna(method='bfill')
    merged_df['Value_mean_12_diff'] = merged_df['Value_mean_12'].diff(1).fillna(method='bfill')
    merged_df['DEMAND'] = merged_df['DEMAND']/2000
    merged_df[targetvariable] = merged_df[targetvariable]/divideby
    main_features = [targetvariable, becomefeature,'LOAD_SHORTFALL', 'RES_SHORTFALL',
       'REG_SHORTFALL', 'ABNORMAL_OUTAGE', 'ABNORMAL_OTHER', 'PRICE_WARNING',
       'PRICE_REVISION', 'PROVISIONAL_PRICES','DEMAND','DATE'] 
    merged_df[main_features]
    return merged_df

