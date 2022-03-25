import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,8)

data=pd.read_csv('/content/dataset.csv')
data.drop('user_id',1,inplace=True)
data.dropna(inplace=True)
data.drop_duplicates( keep='last',inplace=True)

time_col=pd.to_datetime(data['event_time'])
time_co=pd.DataFrame(dict(time = time_col))
data['hour']=time_co['time'].dt.hour
data['weekdays']=time_co['time'].dt.weekday
data['year']=time_co['time'].dt.year

def total_cost_sales(X,Y):
  data_filtered=data.loc[(data['year']==Y)&(data['category_code']==X)]
  return data_filtered['price'].sum()

def probability_of_purchase(X,Y):
  data_filtered=data.loc[(data['brand']==X)&(data['price']>Y)]
  return len(data_filtered)/len(data)