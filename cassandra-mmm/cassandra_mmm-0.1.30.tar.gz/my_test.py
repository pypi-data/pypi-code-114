#!/usr/bin/env python
# coding: utf-8

# In[1]:


from src.cassandra.data.dataProcessing.clean_and_format import create_data_columns
from cassandra.data.dataAnalysis.correlation import show_saturation_curves, show_relationship_between_variables
from src.cassandra.data.dataAnalysis.plot import show_target_vs_media_spent_graph, show_prediction_vs_actual_graph
from src.cassandra.data.dataProcessing.clean_and_format import create_dataset
from src.cassandra.data.dataProcessing.prophet import prophet
from cassandra.model.deepLearning import deepLearning
from src.cassandra.model.linear import linear
from cassandra.model.logLinear import logLinear
from cassandra.model.ridge import ridge
from cassandra.data.featureSelection.ols import ols
from cassandra.data.trasformations.trasformations import saturation, adstock
from cassandra.model.modelEvaluation.evaluation import show_coefficients
from cassandra.model.modelEvaluation.evaluation import show_nrmse, show_mape, show_rsquared
import pandas as pd
import nevergrad as ng
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# In[2]:
from src.cassandra.model.nestedModel import nestedModel, mainNestedModel

csv_data = create_dataset('D:/workspace_cassandra/mmm/spedire/dataset-spedire-20-02-22.csv',
                          subset_columns=['ordine_data', 'revenue', 'transazioni', 'google_search_spent',
                                          'google_performance_max_spent', 'google_display_spent',
                                          'fb_retargeting_spent', 'fb_prospecting_spent', 'bing_organico',
                                          'google_organico', 'referral', 'email_sessioni', 'Offerte', 'Sconti'])
#csv_data = create_data_columns(csv_data, 'ordine_data')

#print(csv_data['festivo'].unique())

# r_maggiore = csv_data.loc[csv_data['revenue'] > 17000]
# r_minore = csv_data.loc[csv_data['revenue'] < 2000]
# print(r_maggiore.index)
# print(r_minore.index)
#csv_data = csv_data.drop(csv_data[csv_data.ordine_data < '2021-09-11'].index)

#csv_data.drop(csv_data[(csv_data['revenue'] > 17000)].index, inplace=True)  # droppate 12 righe
#csv_data.drop(csv_data[(csv_data['revenue'] < 1500)].index, inplace=True)

df = prophet(csv_data, 'ordine_data', 'revenue', window_start='2021-05-01')
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 20)
pd.set_option("display.max_columns", 20)
# df['facebook_spent'] = df["fb_retargeting_spent"] + df["fb_prospecting_spent"]
df

# In[3]:


medias = [col for col in df.columns if 'spent' in col]
# medias.remove("fb_retargeting_spent")
# medias.remove("fb_prospecting_spent")

organic = ['Offerte','Sconti', 'trend', 'yearly', 'monthly', 'weekly', 'holidays', 'google_organico', 'email_sessioni']

seasonal_categorical = []

seasonal_numeric = ['yearly', 'monthly', 'weekly', 'holidays']


media_numeric = medias

general_categorical= ['Offerte']

general_numeric = ['google_organico', 'Sconti', 'trend']
#'bing_organico', 'google_organico', 'referral', 'email_sessioni'

# Aggregate variables in Numerical and Categorical
numerical = media_numeric + general_numeric + seasonal_numeric
categorical = seasonal_categorical + general_categorical

# Sum everything up in one array
all_features = categorical + numerical

df.fillna(0, inplace=True)

X = df[all_features]
y = df['revenue']

#X_predictor_columns = ['google_organico', 'bing_organico']
#y_predictor_columns = 'referral'

#new_df, nested_model = nestedModelPredictor(df, X_predictor_columns, y_predictor_columns)



#new_df, nested_model, result_predictor, model_predictor = mainNestedModel(df, X_predictor_columns, y_predictor_columns, all_features, 'revenue')
result, model = linear(df, X, y, 'revenue', 'name_model')

show_prediction_vs_actual_graph(df, 'ordine_data', 'revenue', 'prediction')
# show_saturation_curves(medias, df, 'revenue')
#
# # In[4]:
#
#
# # show_relationship_between_variables(df, 5)
#
#
# # In[5]:
#
#
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# df.corr()
#
# # In[6]:
#
#
# show_target_vs_media_spent_graph(df, 'ordine_data', 'revenue', medias)
#
# # In[7]:
#
#
# organic = ['Offerte', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'mon', 'tue',
#            'wed', 'thu', 'fri', 'sat', 'sun', 'festivo', 'google_organico']
#
# seasonal_categorical = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'mon',
#                         'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'festivo']
# # 'year_2020','year_2021','year_2022',
#
# media_numeric = medias
#
# general_categorical = ['Offerte']
#
# general_numeric = ['google_organico']
# # 'bing_organico', 'google_organico', 'referral', 'email_sessioni'
#
# # Aggregate variables in Numerical and Categorical
# numerical = media_numeric + general_numeric
# categorical = seasonal_categorical + general_categorical
#
# # Sum everything up in one array
# all_features = categorical + numerical
#
# df.fillna(0, inplace=True)
#
# X = df[all_features]
# y = df['revenue']
#
# result_ols, model_ols = ols(X, y)
#
# # **Regressione Lineare**
#
# # In[8]:
#
#
# result_linear, model_linear = linear(df, medias, organic, X, y, 'revenue', 'Linear', ['accuracy', 'nrmse', 'mape'])
#
# # In[9]:
#
#
# show_prediction_vs_actual_graph(result_linear, 'ordine_data', 'revenue', 'prediction')
#
# # In[10]:
#
#
# coeffs = show_coefficients(all_features, model_linear.named_steps['regression'], 'Linear')
#
# # In[11]:
#
#
# # coeffs
#
#
# # In[12]:
#
#
# model_linear.named_steps['regression'].intercept_
#
# # **Nevergrad**
#
# # In[13]:
#
#
# mape_array = []
#
#
# def build_model(b1, b2, b3, b4, b5, b30, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19,
#                 b20, b21, b22, b23, b24, b25, b26, b27, b28, b34, b0, google_search_spent_theta,
#                 google_search_spent_beta,
#                 google_performance_max_spent_theta, google_performance_max_spent_beta,
#                 google_display_spent_theta, google_display_spent_beta,
#                 # facebook_spent_theta, facebook_spent_beta):
#                 fb_retargeting_spent_theta, fb_retargeting_spent_beta,
#                 fb_prospecting_spent_theta, fb_prospecting_spent_beta):
#     # bing_spent_theta, bing_spent_beta):
#
#     x1 = df["google_search_spent"]
#     x2 = df["google_performance_max_spent"]
#     x3 = df["google_display_spent"]
#     # x4 = df["facebook_spent"]
#     x4 = df["fb_retargeting_spent"]
#     x5 = df["fb_prospecting_spent"]
#     # x29 = df["bing_spent"]
#     x30 = df["google_organico"]
#     # x31 = df["bing_organico"]
#     # x32 = df["referral"]
#     # x33 = df["email_sessioni"]
#     x6 = df["year_2020"]
#     x7 = df["year_2021"]
#     x8 = df["year_2022"]
#     x9 = df["mon"]
#     x10 = df["tue"]
#     x11 = df["wed"]
#     x12 = df["thu"]
#     x13 = df["fri"]
#     x14 = df["sat"]
#     x15 = df["sun"]
#     x16 = df["jan"]
#     x17 = df["feb"]
#     x18 = df["mar"]
#     x19 = df["apr"]
#     x20 = df["may"]
#     x21 = df["jun"]
#     x22 = df["jul"]
#     x23 = df["aug"]
#     x24 = df["sep"]
#     x25 = df["oct"]
#     x26 = df["nov"]
#     x27 = df["dec"]
#     x28 = df["Offerte"]
#     x34 = df["festivo"]
#
#     # ' Transform all media variables and set them in the new Dictionary
#     # ' Adstock first and Saturation second
#     x1 = saturation(adstock(x1, google_search_spent_theta), google_search_spent_beta)
#     x2 = saturation(adstock(x2, google_performance_max_spent_theta), google_performance_max_spent_beta)
#     x3 = saturation(adstock(x3, google_display_spent_theta), google_display_spent_beta)
#     x4 = saturation(adstock(x4, fb_retargeting_spent_theta), fb_retargeting_spent_beta)
#     x5 = saturation(adstock(x5, fb_prospecting_spent_theta), fb_prospecting_spent_beta)
#     # x29 = saturation(adstock(x29, bing_spent_theta), bing_spent_beta)
#
#     y_pred = b6 * x6 + b7 * x7 + b8 * x8 + b16 * x16 + b17 * x17 + b18 * x18 + b19 * x19 + b20 * x20 + b21 * x21 + b22 * x22 + b23 * x23 + b24 * x24 + b25 * x25 + b26 * x26 + b27 * x27 + b9 * x9 + b10 * x10 + b11 * x11 + b12 * x12 + b13 * x13 + b14 * x14 + b15 * x15 + b34 * x34 + b28 * x28 + b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4 + b5 * x5 + b30 * x30 + b0
#     # b30*x30 + b31*x31 + b32*x32 + b33*x33 +
#     result = df
#     result['google_search_spent'] = x1
#     result['google_performance_max_spent'] = x2
#     result['google_display_spent'] = x3
#     result['fb_retargeting_spent'] = x4
#     result['fb_prospecting_spent'] = x5
#
#     result['prediction'] = y_pred
#
#     nrmse_val = show_nrmse(result['revenue'], result['prediction'])
#     mape_val = show_mape(result['revenue'], result['prediction'])
#     rsquared_val = show_rsquared(result['revenue'], result['prediction'])
#
#     print(nrmse_val, mape_val, rsquared_val)
#
#     mape_array.append(mape_val)
#
#     return mape_val
#
#
# # In[14]:
#
#
# # ' Define the list of hyperparameters to optimize
# # ' List must be the same as the ones in the function's definition, same order recommended too
# instrum = ng.p.Instrumentation(
#     b1=ng.p.Scalar(lower=0),
#     b2=ng.p.Scalar(lower=0),
#     b3=ng.p.Scalar(lower=0),
#     b4=ng.p.Scalar(lower=0),
#     b5=ng.p.Scalar(lower=0),
#     # b29=ng.p.Scalar(lower=0),
#     b30=ng.p.Scalar(),
#     # b31=ng.p.Scalar(),
#     # b32=ng.p.Scalar(),
#     # b34=ng.p.Scalar(),
#     b6=ng.p.Scalar(),
#     b7=ng.p.Scalar(),
#     b8=ng.p.Scalar(),
#     b9=ng.p.Scalar(),
#     b10=ng.p.Scalar(),
#     b11=ng.p.Scalar(),
#     b12=ng.p.Scalar(),
#     b13=ng.p.Scalar(),
#     b14=ng.p.Scalar(),
#     b15=ng.p.Scalar(),
#     b16=ng.p.Scalar(),
#     b17=ng.p.Scalar(),
#     b18=ng.p.Scalar(),
#     b19=ng.p.Scalar(),
#     b20=ng.p.Scalar(),
#     b21=ng.p.Scalar(),
#     b22=ng.p.Scalar(),
#     b23=ng.p.Scalar(),
#     b24=ng.p.Scalar(),
#     b25=ng.p.Scalar(),
#     b26=ng.p.Scalar(),
#     b27=ng.p.Scalar(),
#     b28=ng.p.Scalar(),
#     b34=ng.p.Scalar(),
#     b0=ng.p.Scalar(),
#
#     google_search_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     google_search_spent_beta=ng.p.Scalar(lower=0, upper=1),
#
#     google_performance_max_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     google_performance_max_spent_beta=ng.p.Scalar(lower=0, upper=1),
#
#     google_display_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     google_display_spent_beta=ng.p.Scalar(lower=0, upper=1),
#
#     # facebook_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     # facebook_spent_beta=ng.p.Scalar(lower=0, upper=1)
#
#     fb_retargeting_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     fb_retargeting_spent_beta=ng.p.Scalar(lower=0, upper=1),
#
#     fb_prospecting_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     fb_prospecting_spent_beta=ng.p.Scalar(lower=0, upper=1),
#
#     # bing_spent_theta=ng.p.Scalar(lower=0, upper=1),
#     # bing_spent_beta=ng.p.Scalar(lower=0, upper=1)
# )
#
# # print(instrum)
# # ' Define an Optimizer (use NGOpt as default) and set budget as number of trials (recommended 2500+)
# optimizer = ng.optimizers.TwoPointsDE(parametrization=instrum, budget=5000)
# # print(optimizer)
#
# # ' Pass the function to minimize
# # ' Nevergrad will automatically map Hyperparams
# recommendation = optimizer.minimize(build_model)
#
# # ' Results of the optimization are inside the following variable
# recommendation.value
#
#
# # build_model(**recommendation.value[1])
# # ' Use the following code to directly use the optimized hyperparams to build you model
#
#
# # In[15]:
#
#
# def build_model(b1, b2, b3, b4, b5, b30, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19,
#                 b20, b21, b22, b23, b24, b25, b26, b27, b28, b34, b0, google_search_spent_theta,
#                 google_search_spent_beta,
#                 google_performance_max_spent_theta, google_performance_max_spent_beta,
#                 google_display_spent_theta, google_display_spent_beta,
#                 # facebook_spent_theta, facebook_spent_beta):
#                 fb_retargeting_spent_theta, fb_retargeting_spent_beta,
#                 fb_prospecting_spent_theta, fb_prospecting_spent_beta):
#     # bing_spent_theta, bing_spent_beta):
#
#     x1 = df["google_search_spent"]
#     x2 = df["google_performance_max_spent"]
#     x3 = df["google_display_spent"]
#     # x4 = df["facebook_spent"]
#     x4 = df["fb_retargeting_spent"]
#     x5 = df["fb_prospecting_spent"]
#     # x29 = df["bing_spent"]
#     x30 = df["google_organico"]
#     # x31 = df["bing_organico"]
#     # x32 = df["referral"]
#     # x33 = df["email_sessioni"]
#     x6 = df["year_2020"]
#     x7 = df["year_2021"]
#     x8 = df["year_2022"]
#     x9 = df["mon"]
#     x10 = df["tue"]
#     x11 = df["wed"]
#     x12 = df["thu"]
#     x13 = df["fri"]
#     x14 = df["sat"]
#     x15 = df["sun"]
#     x16 = df["jan"]
#     x17 = df["feb"]
#     x18 = df["mar"]
#     x19 = df["apr"]
#     x20 = df["may"]
#     x21 = df["jun"]
#     x22 = df["jul"]
#     x23 = df["aug"]
#     x24 = df["sep"]
#     x25 = df["oct"]
#     x26 = df["nov"]
#     x27 = df["dec"]
#     x28 = df["Offerte"]
#     x34 = df["festivo"]
#
#     # ' Transform all media variables and set them in the new Dictionary
#     # ' Adstock first and Saturation second
#     x1 = saturation(adstock(x1, google_search_spent_theta), google_search_spent_beta)
#     x2 = saturation(adstock(x2, google_performance_max_spent_theta), google_performance_max_spent_beta)
#     x3 = saturation(adstock(x3, google_display_spent_theta), google_display_spent_beta)
#     x4 = saturation(adstock(x4, fb_retargeting_spent_theta), fb_retargeting_spent_beta)
#     x5 = saturation(adstock(x5, fb_prospecting_spent_theta), fb_prospecting_spent_beta)
#     # x29 = saturation(adstock(x29, bing_spent_theta), bing_spent_beta)
#
#     y_pred = b6 * x6 + b7 * x7 + b8 * x8 + b16 * x16 + b17 * x17 + b18 * x18 + b19 * x19 + b20 * x20 + b21 * x21 + b22 * x22 + b23 * x23 + b24 * x24 + b25 * x25 + b26 * x26 + b27 * x27 + b9 * x9 + b10 * x10 + b11 * x11 + b12 * x12 + b13 * x13 + b14 * x14 + b15 * x15 + b34 * x34 + b28 * x28 + b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4 + b5 * x5 + b30 * x30 + b0
#     # b30*x30 + b31*x31 + b32*x32 + b33*x33 +
#     result = df
#     result['google_search_spent'] = x1
#     result['google_performance_max_spent'] = x2
#     result['google_display_spent'] = x3
#     result['fb_retargeting_spent'] = x4
#     result['fb_prospecting_spent'] = x5
#
#     result['prediction'] = y_pred
#
#     nrmse_val = show_nrmse(result['revenue'], result['prediction'])
#     mape_val = show_mape(result['revenue'], result['prediction'])
#     rsquared_val = show_rsquared(result['revenue'], result['prediction'])
#
#     print('NRMSE: ', nrmse_val, 'MAPE: ', mape_val, 'RSQUARED: ', rsquared_val)
#     return mape_val, result
#
#
# # In[16]:
#
#
# mape_val, result = build_model(**recommendation.value[1])
# print(mape_val)
#
# # In[17]:
#
#
# import plotly.express as px
# import plotly.graph_objects as go
#
# fig = go.Figure(
#     layout=dict(xaxis_title='Iterations', yaxis_title='mape', title='MAPE Trend', legend_title='Legend'))
# fig.add_trace(go.Scatter(y=mape_array))
#
# # In[18]:
#
#
# pd.set_option("display.max_rows", 20)
# pd.set_option("display.max_columns", 20)
# # result.to_csv('dataset-spedire-saturation-adstock.csv')
# result
#
# # In[21]:
#
#
# csv_data = result[['ordine_data', 'revenue', 'transazioni', 'google_search_spent', 'google_performance_max_spent',
#                    'google_display_spent', 'fb_retargeting_spent', 'fb_prospecting_spent', 'google_organico',
#                    'Offerte', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec',
#                    'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'festivo']]
#
# df = csv_data
# pd.set_option("display.max_rows", 20)
# pd.set_option("display.max_columns", 20)
# df
#
# # In[22]:
#
#
# pd.set_option("display.max_rows", None)
# pd.set_option("display.max_columns", None)
# df.corr()
#
# # In[23]:
#
#
# medias = [col for col in df.columns if 'spent' in col]
#
# # In[24]:
#
#
# organic = ['Offerte', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'mon', 'tue',
#            'wed', 'thu', 'fri', 'sat', 'sun', 'festivo', 'google_organico']
#
# seasonal_categorical = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec', 'mon',
#                         'tue', 'wed', 'thu', 'fri', 'sat', 'sun', 'festivo']
#
# media_numeric = medias
#
# general_categorical = ['Offerte']
#
# general_numeric = ['google_organico']
# # 'bing_organico', 'google_organico', 'referral', 'email_sessioni'
#
# # Aggregate variables in Numerical and Categorical
# numerical = media_numeric + general_numeric
# categorical = seasonal_categorical + general_categorical
#
# # Sum everything up in one array
# all_features = categorical + numerical
#
# df.fillna(0, inplace=True)
#
# X = df[all_features]
# y = df['revenue']
#
# result_ols, model_ols = ols(X, y)
#
# # In[25]:
#
#
# result_linear, model_linear = linear(df, medias, organic, X, y, 'revenue', 'Linear', ['accuracy', 'nrmse', 'mape'])
#
# # In[26]:
#
#
# show_prediction_vs_actual_graph(result_linear, 'ordine_data', 'revenue', 'prediction')
#
# # In[27]:
#
#
# coeffs = show_coefficients(all_features, model_linear.named_steps['regression'], 'Linear')
#
# # In[28]:
#
#
# model_linear.named_steps['regression'].intercept_
#
# # In[29]:
#
#
# mape_array = []
#
#
# def build_model(b1, b2, b3, b4, b5, b30, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19,
#                 b20, b21, b22, b23, b24, b25, b26, b27, b28, b34, b0):
#     x1 = df["google_search_spent"]
#     x2 = df["google_performance_max_spent"]
#     x3 = df["google_display_spent"]
#     # x4 = df["facebook_spent"]
#     x4 = df["fb_retargeting_spent"]
#     x5 = df["fb_prospecting_spent"]
#     # x29 = df["bing_spent"]
#     x30 = df["google_organico"]
#     # x31 = df["bing_organico"]
#     # x32 = df["referral"]
#     # x33 = df["email_sessioni"]
#     # x6 = df["year_2020"]
#     # x7 = df["year_2021"]
#     # x8 = df["year_2022"]
#     x9 = df["mon"]
#     x10 = df["tue"]
#     x11 = df["wed"]
#     x12 = df["thu"]
#     x13 = df["fri"]
#     x14 = df["sat"]
#     x15 = df["sun"]
#     x16 = df["jan"]
#     x17 = df["feb"]
#     x18 = df["mar"]
#     x19 = df["apr"]
#     x20 = df["may"]
#     x21 = df["jun"]
#     x22 = df["jul"]
#     x23 = df["aug"]
#     x24 = df["sep"]
#     x25 = df["oct"]
#     x26 = df["nov"]
#     x27 = df["dec"]
#     x28 = df["Offerte"]
#     x34 = df["festivo"]
#
#     y_pred = b16 * x16 + b17 * x17 + b18 * x18 + b19 * x19 + b20 * x20 + b21 * x21 + b22 * x22 + b23 * x23 + b24 * x24 + b25 * x25 + b26 * x26 + b27 * x27 + b9 * x9 + b10 * x10 + b11 * x11 + b12 * x12 + b13 * x13 + b14 * x14 + b15 * x15 + b34 * x34 + b28 * x28 + b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4 + b5 * x5 + b30 * x30 + b0
#     # b30*x30 + b31*x31 + b32*x32 + b33*x33 +
#     # b6*x6 + b7*x7 + b8*x8 +
#     result = df
#
#     result['prediction'] = y_pred
#
#     nrmse_val = show_nrmse(result['revenue'], result['prediction'])
#     mape_val = show_mape(result['revenue'], result['prediction'])
#     rsquared_val = show_rsquared(result['revenue'], result['prediction'])
#     print(nrmse_val, mape_val, rsquared_val)
#     mape_array.append(mape_val)
#
#     return mape_val
#
#
# # In[30]:
#
#
# # ' Define the list of hyperparameters to optimize
# # ' List must be the same as the ones in the function's definition, same order recommended too
# instrum = ng.p.Instrumentation(
#     b1=ng.p.Scalar(lower=0),
#     b2=ng.p.Scalar(lower=0),
#     b3=ng.p.Scalar(lower=0),
#     b4=ng.p.Scalar(lower=0),
#     b5=ng.p.Scalar(lower=0),
#     # b29=ng.p.Scalar(lower=0),
#     b30=ng.p.Scalar(),
#     # b31=ng.p.Scalar(),
#     # b32=ng.p.Scalar(),
#     # b34=ng.p.Scalar(),
#     # b6=ng.p.Scalar(),
#     # b7=ng.p.Scalar(),
#     # b8=ng.p.Scalar(),
#     b9=ng.p.Scalar(),
#     b10=ng.p.Scalar(),
#     b11=ng.p.Scalar(),
#     b12=ng.p.Scalar(),
#     b13=ng.p.Scalar(),
#     b14=ng.p.Scalar(),
#     b15=ng.p.Scalar(),
#     b16=ng.p.Scalar(),
#     b17=ng.p.Scalar(),
#     b18=ng.p.Scalar(),
#     b19=ng.p.Scalar(),
#     b20=ng.p.Scalar(),
#     b21=ng.p.Scalar(),
#     b22=ng.p.Scalar(),
#     b23=ng.p.Scalar(),
#     b24=ng.p.Scalar(),
#     b25=ng.p.Scalar(),
#     b26=ng.p.Scalar(),
#     b27=ng.p.Scalar(),
#     b28=ng.p.Scalar(),
#     b34=ng.p.Scalar(),
#     b0=ng.p.Scalar()
# )
#
# # print(instrum)
# # ' Define an Optimizer (use NGOpt as default) and set budget as number of trials (recommended 2500+)
# optimizer = ng.optimizers.TwoPointsDE(parametrization=instrum, budget=5000)
# # print(optimizer)
#
# # ' Pass the function to minimize
# # ' Nevergrad will automatically map Hyperparams
# recommendation = optimizer.minimize(build_model)
#
# # ' Results of the optimization are inside the following variable
# recommendation.value
#
#
# # build_model(**recommendation.value[1])
# # ' Use the following code to directly use the optimized hyperparams to build you model
#
#
# # In[31]:
#
#
# def build_model(b1, b2, b3, b4, b5, b30, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19,
#                 b20, b21, b22, b23, b24, b25, b26, b27, b28, b34, b0):
#     x1 = df["google_search_spent"]
#     x2 = df["google_performance_max_spent"]
#     x3 = df["google_display_spent"]
#     # x4 = df["facebook_spent"]
#     x4 = df["fb_retargeting_spent"]
#     x5 = df["fb_prospecting_spent"]
#     # x29 = df["bing_spent"]
#     x30 = df["google_organico"]
#     # x31 = df["bing_organico"]
#     # x32 = df["referral"]
#     # x33 = df["email_sessioni"]
#     # x6 = df["year_2020"]
#     # x7 = df["year_2021"]
#     # x8 = df["year_2022"]
#     x9 = df["mon"]
#     x10 = df["tue"]
#     x11 = df["wed"]
#     x12 = df["thu"]
#     x13 = df["fri"]
#     x14 = df["sat"]
#     x15 = df["sun"]
#     x16 = df["jan"]
#     x17 = df["feb"]
#     x18 = df["mar"]
#     x19 = df["apr"]
#     x20 = df["may"]
#     x21 = df["jun"]
#     x22 = df["jul"]
#     x23 = df["aug"]
#     x24 = df["sep"]
#     x25 = df["oct"]
#     x26 = df["nov"]
#     x27 = df["dec"]
#     x28 = df["Offerte"]
#     x34 = df["festivo"]
#
#     y_pred = b16 * x16 + b17 * x17 + b18 * x18 + b19 * x19 + b20 * x20 + b21 * x21 + b22 * x22 + b23 * x23 + b24 * x24 + b25 * x25 + b26 * x26 + b27 * x27 + b9 * x9 + b10 * x10 + b11 * x11 + b12 * x12 + b13 * x13 + b14 * x14 + b15 * x15 + b34 * x34 + b28 * x28 + b1 * x1 + b2 * x2 + b3 * x3 + b4 * x4 + b5 * x5 + b30 * x30 + b0
#     # b30*x30 + b31*x31 + b32*x32 + b33*x33 +
#     # b6*x6 + b7*x7 + b8*x8 +
#     result = df
#
#     result['prediction'] = y_pred
#
#     nrmse_val = show_nrmse(result['revenue'], result['prediction'])
#     mape_val = show_mape(result['revenue'], result['prediction'])
#     rsquared_val = show_rsquared(result['revenue'], result['prediction'])
#
#     print('NRMSE: ', nrmse_val, 'MAPE: ', mape_val, 'RSQUARED: ', rsquared_val)
#     return mape_val, result
#
#
# # In[32]:
#
#
# mape_val, result = build_model(**recommendation.value[1])
# print(mape_val)
#
# # In[33]:
#
#
# import plotly.express as px
# import plotly.graph_objects as go
#
# fig = go.Figure(
#     layout=dict(xaxis_title='Iterations', yaxis_title='mape', title='MAPE Trend', legend_title='Legend'))
# fig.add_trace(go.Scatter(y=mape_array))
#
# # In[34]:
#
#
# pd.set_option("display.max_rows", 20)
# pd.set_option("display.max_columns", 20)
# # result.to_csv('dataset-spedire-saturation-adstock-prediction.csv')
# result
#
# # In[35]:
#
#
# show_prediction_vs_actual_graph(result, 'ordine_data', 'revenue', 'prediction')
#
# # In[36]:
#
#
# recommendation.value[1]
#
# # In[37]:
#
#
# array_coefs = ['b16', 'b17', 'b18', 'b19', 'b20', 'b21', 'b22', 'b23', 'b24', 'b25', 'b26', 'b27', 'b9', 'b10',
#                'b11', 'b12', 'b13', 'b14', 'b15', 'b34', 'b28', 'b1', 'b2', 'b3', 'b4', 'b5', 'b30']
# new_coef = [recommendation.value[1].get(key) for key in array_coefs]
# new_intercept = recommendation.value[1].get('b0')
#
# # In[38]:
#
#
# X_train, X_test, y_train, y_test = train_test_split(X, y)
#
# reg = LinearRegression().fit(X_train, y_train)
#
# reg.coef_ = np.array(new_coef)
# reg.intercept_ = new_intercept
#
# # In[39]:
#
#
# coeffs = show_coefficients(all_features, reg, 'Linear Change')
#
# # In[41]:
#
#
# result['prediction'] = reg.predict(X)
#
# # In[42]:
#
#
# show_prediction_vs_actual_graph(result, 'ordine_data', 'revenue', 'prediction')
#
# # In[44]:
#
#
# result
#
#
# # **Budget Allocator**
#
# # In[45]:
#
#
# def myFunc(x, grad=[]):
#     data = {'jan': [x[0]], 'feb': [x[1]],
#             'mar': [x[2]], 'apr': [x[3]],
#             'may': [x[4]], 'jun': [x[5]], 'jul': [x[6]], 'aug': [x[7]], 'sep': [x[8]],
#             'oct': [x[9]], 'nov': [x[10]], 'dec': [x[11]], 'mon': [x[12]], 'tue': [x[13]],
#             'wed': [x[14]], 'thu': [x[15]], 'fri': [x[16]], 'sat': [x[17]], 'sun': [x[18]],
#             'festivo': [x[19]], 'Offerte': [x[20]],
#             'google_search_spent': [x[21]], 'google_performance_max_spent': [x[22]],
#             'google_display_spent': [x[23]], 'fb_retargeting_spent': [x[24]], 'fb_prospecting_spent': [x[25]],
#             'google_organico': [x[26]]
#             }
#     dic = pd.DataFrame.from_dict(data)
#
#     return reg.predict(dic)
#
#
# # In[46]:
#
#
# import nlopt
# from numpy import *
#
# opt = nlopt.opt(nlopt.GN_AGS, 27)
#
# opt.set_lower_bounds([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
# opt.set_upper_bounds([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 500, 500, 500, 500, 500, 1])
#
# opt.set_max_objective(myFunc)
# opt.add_inequality_constraint(lambda z, grad: sum(z) - 600, 1e-8)
#
# # rate of improvement, below which we are done
# opt.set_xtol_rel(1e-10)
# opt.set_maxeval(1000)
#
# # In[47]:
#
#
# arrayx = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 142.5, 40, 5, 30, 30, 1])
# # for x in arrayx:
# # print(x.dtype)
# y = opt.optimize(arrayx)
#
# # In[ ]:
#
#
# maxf = opt.last_optimum_value()
#
# print("optimum at ", x[24], x[25], x[26], x[27], x[28])
# print("maximum value = ", maxf)
# print("iterations = ", opt.get_numevals())
# print("result code = ", opt.last_optimize_result())
#
# # In[ ]:
#
#
# # In[ ]:




