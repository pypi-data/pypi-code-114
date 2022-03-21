import pandas as pd
from datetime import datetime, timedelta
import copy

input_columns = ['出清前_直调负荷(MW)', '出清前_地方电厂发电总加(MW)', '出清前_联络线受电负荷(MW)', '出清前_风电总加(MW)',
                '出清前_光伏总加(MW)', '出清前_试验机组总加(MW)', '出清前_自备机组总加(MW)', '日期', '时期']

def judge_input_error(input_json):
  inputs = pd.DataFrame(input_json["data"]["ndarray"])
  inputs.columns = input_columns
  print("预测接口输入数据:",inputs)
  return inputs,input_json

def add_timestamp(df_gongxu_predict):
  index_list = []
  for count, i in enumerate(df_gongxu_predict['时期']):
    index_list.append(datetime.strptime(df_gongxu_predict.loc[count, '日期'], '%Y-%m-%d') + timedelta(minutes=15 * i))
  df_gongxu_predict.index = index_list
  df_gongxu_predict = df_gongxu_predict.sort_index()
  return df_gongxu_predict

def pred_feature_engineer_shandong(ori_json):
  input_columns = ['出清前_直调负荷(MW)', '出清前_地方电厂发电总加(MW)', '出清前_联络线受电负荷(MW)', '出清前_风电总加(MW)',
                '出清前_光伏总加(MW)', '出清前_试验机组总加(MW)', '出清前_自备机组总加(MW)', '日期', '时期']
  ori_json['data']['ndarray']
  model_data = copy.deepcopy(ori_json['data']['ndarray'])
  model_data = pd.DataFrame(model_data)
  model_data.columns = input_columns
  inputs, ori_json = judge_input_error(ori_json, input_columns)
  model_data['时期'] = [i for i in range(96)]
  data = add_timestamp(model_data)
  data['出清前_竞价空间1'] = (data['出清前_直调负荷(MW)'] - data['出清前_联络线受电负荷(MW)'] - data['出清前_风电总加(MW)']
                         - data['出清前_光伏总加(MW)'] - data['出清前_地方电厂发电总加(MW)']
                         - data['出清前_试验机组总加(MW)'] - data['出清前_自备机组总加(MW)'])
  data['出清前_竞价空间2'] = (data['出清前_直调负荷(MW)'] - data['出清前_联络线受电负荷(MW)'] - data['出清前_风电总加(MW)']
                         - data['出清前_光伏总加(MW)'] - data['出清前_地方电厂发电总加(MW)'])
  data['出清前_新能源预测'] = data['出清前_风电总加(MW)'] + data['出清前_光伏总加(MW)']
  data['hour']=data['时期']//4
  data['time']=data['时期']
  data['出清前_竞价空间1_max']=data['出清前_竞价空间1'].max()
  data['出清前_竞价空间1_min'] = data['出清前_竞价空间1'].min()
  data['出清前_竞价空间1_mean'] = data['出清前_竞价空间1'].mean()
  return data

def shandong_feature_engineer(df_shandong, feature_columns, label_column):
  data = df_shandong.copy()
  data['index'] = pd.to_datetime(data['index'], infer_datetime_format = True)
  data['时期'] = data['index'].apply(lambda x: x.hour * 4 + x.minute // 15)
  data['出清前_竞价空间1'] = (data['出清前_直调负荷(MW)'] - data['出清前_联络线受电负荷(MW)'] - data['出清前_风电总加(MW)']
                         - data['出清前_光伏总加(MW)'] - data['出清前_地方电厂发电总加(MW)']
                         - data['出清前_试验机组总加(MW)'] - data['出清前_自备机组总加(MW)'])
  data['出清前_竞价空间2'] = (data['出清前_直调负荷(MW)'] - data['出清前_联络线受电负荷(MW)'] - data['出清前_风电总加(MW)']
                         - data['出清前_光伏总加(MW)'] - data['出清前_地方电厂发电总加(MW)'])
  data['出清前_新能源预测'] = data['出清前_风电总加(MW)'] + data['出清前_光伏总加(MW)']
  data['hour']=data['时期']//4
  data['time']=data['时期']
  data['出清前_竞价空间1_max']=data['出清前_竞价空间1'].max()
  data['出清前_竞价空间1_min'] = data['出清前_竞价空间1'].min()
  data['出清前_竞价空间1_mean'] = data['出清前_竞价空间1'].mean()
  mask = data[feature_columns + [label_column]].notna().all(axis=1).values
  data = data.loc[mask]
  data.set_index('index', inplace = True)
  return data