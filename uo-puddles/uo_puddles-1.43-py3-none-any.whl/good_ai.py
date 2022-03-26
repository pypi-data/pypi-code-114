from sklearn.base import BaseEstimator, TransformerMixin

from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer

from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score#, balanced_accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV

def hello():
  print('Welcome to AI for Good')

def up_lottery(student_list):
  random_students = random.sample(student_list, len(student_list))
  table_table = pd.DataFrame(columns=['Table'], index=random_students + ['Blank']*(20-len(student_list)))
  table_table['Table'] = [1]*4 + [2]*4 + [3]*4 + [4]*4 + [5]*4
  return table_table
  
  
def up_get_table(url):
  assert isinstance(url, str), f':Puddles says: Expecting url to be string but is {type(url)} instead.'
  try:
    df = pd.read_csv(url)
  except:
    assert False, f'Puddles says: url is not a legal web site for a table. If using GitHub, make sure to get raw version of file.'
  return df


def up_get_column(table, column_name):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: Expecting a table but instead got a {type(table)}!'
  assert column_name in table.columns.to_list(),f'Puddles says: column_name {column_name} is unrecognized. Check spelling and case. Here are legal column names: {table.columns.to_list()}'

  return table[column_name].to_list()

def up_show_color(rgb_triple):
  assert isinstance(rgb_triple, list) or isinstance(rgb_triple, tuple), f'Puddles says: expecting a list but got {rgb_triple}.'
  assert len(rgb_triple)==3, f'Puddles says: expecting 3 itmes in the list but got {rgb_triple}.'
  assert all([isinstance(x, int) for x in rgb_triple]), f'Puddles says: expecting 3 ints but got {rgb_triple}.'

  import matplotlib.pyplot as plt
  plt.imshow([[tuple(rgb_triple)]])
  
def up_plot_against(table, column1, column2):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  assert column1 in table.columns, f'Puddles says: the first column {column1} is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
  assert column2 in table.columns, f'Puddles says: the second column {column2} is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'

  if len(set(table[column1].to_list()))>20:
    print(f'Puddles warning: {column1} has more than 20 unique values. Likely to not plot well.')
    
  if len(set(table[column2].to_list()))>5:
    print(f'Puddles warning: {column2} has more than 5 unique values. Likely to not plot well.')
    
  pd.crosstab(table[column1], table[column2]).plot(kind='bar', figsize=[15,8], grid=True, logy=False)
  
  
def up_table_subset(table, column_name, condition, value):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  assert isinstance(condition, str), f'Puddles says: condition must be a string but is of type {type(condition)}'
  legal_conditions = {'equals':'==', 'not equals':'!=', '>':'>', '<':'<'}
  assert condition in legal_conditions.keys(), f'Puddles says: condition {condition} incorrect. Must be one of {list(legal_conditions.keys())}'
  assert column_name in table.columns, f'Puddles says: column_name {column_name} is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
  if 'equals' not in condition and isinstance(value, str):
    assert False, f'Puddles says: expecting value to be a number but is string instead'

  if 'equals' in condition and value not in table[column_name].to_list():
      print(f'Puddles warning: {value} does not appear in {column_name}')

  op = legal_conditions[condition]

  if isinstance(value,int) or isinstance(value,float):
    value = str(value)
  elif isinstance(value,str):
    value = f'"{value}"'
  else:
    assert False, f'Puddles says: tell Steve he has a bug with {value}'

  new_table = table.query(column_name + op + value)
  if len(new_table)==0:
    print(f'Puddles warning: resulting table is empty')

  return new_table

def up_st_dev(a_list_of_numbers):
  assert isinstance(a_list_of_numbers, list), f'Puddles says: expecting a list but instead got a {type(a_list_of_numbers)}!'
  assert all([not isinstance(x,str) for x in a_list_of_numbers]), f'Puddles says: expecting a list of numbers but list includes a string!'

  st_dev = np.nanstd(a_list_of_numbers)  #ignores nans
  return st_dev

def up_drop_column(table, column_name):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: Expecting a table but instead got a {type(table)}!'
  assert column_name in table.columns.to_list(),f'Puddles says: column_name {column_name} is unrecognized. Check spelling and case. Here are legal column names: {table.columns.to_list()}'

  return table.drop(columns=column_name)

def up_drop_nan_rows(table):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a table but instead got a {type(table)}!'

  dropped_table = table.dropna(axis=0)
  return dropped_table

def up_map_column(table, column_name, mapping_dict):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a table but instead got a {type(table)}!'
  assert column_name in table.columns, f'Puddles says: column_name {column_name} is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
  assert isinstance(mapping_dict, dict), f'Puddles says: expecting mapping_dict to be a dictionary but instead got a {type(mapping_dict)}!'

  column_values = table[column_name].to_list()
  mapping_keys = list(mapping_dict.keys())
  keys_unaccounted = set(mapping_keys).difference(set(column_values))
  if keys_unaccounted:
    print(f'Puddles warning: these keys {keys_unaccounted} do not match any values in the column {column_name}.')

  values_unaccounted = set(column_values).difference(set(mapping_keys))
  if values_unaccounted:
    print(f'Puddles warning: these values {values_unaccounted} are missing a mapping.')

  new_table = table.copy()
  new_table[column_name] = table[column_name].replace(mapping_dict)

  return new_table

def up_get_column_types(table):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a table but instead got a {type(table)}!'

  column_types = []
  for column in table.columns:
    col_list = up_get_column(table, column)
    unique = set(col_list)
    for item in col_list:
      if item==np.nan: continue
      d = type(item)
      if d==str and len(unique)<10:
        value = [column, d.__name__, unique]
      else:
        value = [column, d.__name__, '...']
      column_types.append(value)
      break
  return pd.DataFrame(column_types, columns=['Column', 'Type', 'Unique<10'])

def up_column_histogram(table, column_name):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a table but instead got a {type(table)}!'
  assert column_name in table.columns, f'Puddles says: column_name {column_name} is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
  assert all([not isinstance(x,str) for x in table[column_name]]), f'Puddles says: the column has string values. Can only plot numeric values.'
  
  table[column_name].plot(kind='hist', figsize=(15,8), grid=True, logy=True)
  
def up_clip_list(value_list, lower_boundary, upper_boundary):
  assert isinstance(value_list, list), f'Puddles says: Expecting a list but instead got a {type(value_list)}!'
  assert lower_boundary<upper_boundary, f'Puddles says: lower_boundary must be less than upper_boundary!'

  upper_clipped = 0
  lower_clipped = 0
  new_list = []
  for item in value_list:
    if item>upper_boundary:
      value = upper_boundary
      upper_clipped+=1
    elif item<lower_boundary:
      value = lower_boundary
      lower_clipped+=1
    else:
      value = item
    new_list.append(value)
  print(f'Lower items clipped: {lower_clipped}')
  print(f'Upper items clipped: {upper_clipped}')
  return new_list

def up_set_column(table, column_name, new_values):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: Expecting a table but instead got a {type(table)}!'
  assert column_name in table.columns.to_list(),f'Puddles says: column_name {column_name} is unrecognized. Check spelling and case. Here are legal column names: {table.columns.to_list()}'
  assert isinstance(new_values, list), f'Puddles says: Expecting a list but instead got a {type(new_values)}!'
  assert len(new_values)==len(table), f'Puddles says: length of list is {len(new_values)} but length of table is {len(table)}. Mismatch!'
  
  new_table = table.copy()
  new_table[column_name] = new_values
  return new_table

def up_write_table(table, file_name):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: Expecting a table but instead got a {type(table)}!'
  assert isinstance(file_name, str), f'Puddles says: Expecting file_name to be a string but got a {type(file_name)}!'

  if not file_name.endswith('.csv'): file_name += '.csv'
  table.to_csv(file_name, index=False)
  return None
  
def stats_please(*, table):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  return table.describe(include='all').T
