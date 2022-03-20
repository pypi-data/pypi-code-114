#!/usr/bin/env python
# coding: utf-8

# In[13]:


import argparse
import logging
import os
import pickle
import mlflow
import mlflow.sklearn


# In[14]:


import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


# In[15]:


# mlflow server --backend-store-uri mlruns/ --default-artifact-root artifacts/mlruns/ --host 0.0.0.0 --port 5000
remote_server_uri = "http://0.0.0.0:5000"  # set to the server URI
mlflow.set_tracking_uri(
    remote_server_uri
)  # or set the MLFLOW_TRACKING_URI in the env

exp_name = "Housing_value_prediction"
mlflow.set_experiment(exp_name)


# In[16]:


housing_path = "../data/processed"
filename = "../artifacts/finalized_model.sav"
loglevel = logging.DEBUG
logfile = "../logs/train.log"
consolelog = 1
parser = argparse.ArgumentParser()
parser.add_argument(
    "-f",
    "--folder_path",
    help="Mention the path to the data folder."
    + " Default Value: the data in project folder",
)
parser.add_argument(
    "-m",
    "--model_directory_path",
    help="Mention the directory to save the model. "
    + "Default Value: the artifacts in project folder",
)
parser.add_argument(
    "-ll", "--log_level", help="Mention the log level. Default Value: DEBUG ",
)
parser.add_argument(
    "-lp",
    "--log_path",
    help="Mention the path to save log file."
    + " Default Value: the logs in project folder",
)
parser.add_argument(
    "--no_console_log",
    help="Toggle whether or not to write logs to the console",
    action="store_true",
)


# In[17]:


args = parser.parse_args()


# In[18]:


if args.folder_path:
    housing_path = os.path.join(args.folder_path, "data", "processed")
if args.model_directory_path:
    path = os.path.join(args.log_path, "artifacts")
    os.mkdir(path)
    filename = path + "/finalized_model.sav"


# In[19]:


if args.log_level == "DEBUG":
    loglevel = logging.DEBUG
elif args.log_level == "INFO":
    loglevel = logging.INFO
elif args.log_level == "WARNING":
    loglevel = logging.WARNING
elif args.log_level == "ERROR":
    loglevel = logging.ERROR
elif args.log_level == "CRITICAL":
    loglevel = logging.CRITICAL


# In[20]:


if args.log_path:
    logfile = args.log_path + "/logs/train.log"


# In[21]:


if args.no_console_log:
    consolelog = 0


# In[22]:


logging.basicConfig(filename=logfile, level=loglevel)
logger = logging.getLogger("train.py")


# In[23]:


if consolelog:
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


# In[24]:


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room
    def fit(self, X, y=None):
        return self  # nothing else to do
    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[
                X,
                rooms_per_household,
                population_per_household,
                bedrooms_per_room,
            ]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


# In[ ]:




