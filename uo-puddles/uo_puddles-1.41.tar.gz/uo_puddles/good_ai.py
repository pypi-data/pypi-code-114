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
  assert column_name in table.columns.to_list(),f'Puddles says: column_name is unrecognized. Check spelling and case. Here are legal column names: {table.columns.to_list()}'

  return table[column_name].to_list()


def up_plot_against(table, column1, column2):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  assert column1 in table.columns, f'Puddles says: the first column is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
  assert column2 in table.columns, f'Puddles says: the second column is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'

  if len(set(table[column1].to_list()))>20:
    print(f'Puddles warning: {column1} has more than 20 unique values. Likely to not plot well.')
    
  pd.crosstab(table[column1], table[column2]).plot(kind='bar', figsize=[15,8], grid=True, logy=False)
  
  
def up_table_subset(table, column_name, condition, value):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  assert isinstance(condition, str), f'Puddles says: condition must be a string but is of type {type(condition)}'
  legal_conditions = {'equals':'==', 'not equals':'!=', '>':'>', '<':'<'}
  assert condition in legal_conditions.keys(), f'Puddles says: condition incorrect. Must be one of {list(legal_conditions.keys())}'
  assert column_name in table.columns, f'Puddles says: column_name is not legal. Check spelling and case. Here are legal columns: {table.columns.to_list()}'
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
  
  new_list = [x for x in a_list_of_numbers if x != np.nan]
  st_dev = np.std(new_list)
  return st_dev
  
def stats_please(*, table):
  assert isinstance(table, pd.core.frame.DataFrame), f'Puddles says: expecting a pandas dataframe but instead got a {type(table)}!'
  return table.describe(include='all').T
