#!/usr/bin/env python
# coding: utf-8

# In[28]:


import argparse
import logging
import os
import tarfile
import urllib.request
import mlflow
import mlflow.sklearn


# In[29]:


import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split


# In[30]:


# mlflow server --backend-store-uri mlruns/ --default-artifact-root artifacts/mlruns/ --host 0.0.0.0 --port 5000
remote_server_uri = "http://0.0.0.0:5000"  # set to the server URI
mlflow.set_tracking_uri(
    remote_server_uri
)  # or set the MLFLOW_TRACKING_URI in the env

exp_name = "Housing_value_prediction"
mlflow.set_experiment(exp_name)


# In[31]:


download_root = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
housing_path = os.path.join("../data", "raw")
loglevel = logging.DEBUG
logfile = "../logs/ingest_data.log"
consolelog = 1
parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--saveFile",
    help="Mention the path to save the files(raw,train,test)."
    + " Default Value: the data in project folder",
)
parser.add_argument(
    "-ll", "--log_level", help="Mention the log level. Default Value: DEBUG "
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


# In[32]:


args, unknown = parser.parse_known_args()
if args.saveFile:
    housing_path = os.path.join(args.saveFile, "data", "raw")
    datapath = os.path.join(args.saveFile, "data")
    os.mkdir(datapath)
    path = os.path.join(args.saveFile, "data/processed")
    os.mkdir(path)
housing_url = download_root + "datasets/housing/housing.tgz"


# In[33]:


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


# In[34]:


if args.log_path:
    path = os.path.join(args.log_path, "logs")
    os.mkdir(path)
    logfile = path + "/ingest_data.log"


# In[35]:


if args.no_console_log:
    consolelog = 0


# In[36]:


logging.basicConfig(filename=logfile, level=loglevel)
logger = logging.getLogger("ingest_data.py")


# In[37]:


if consolelog:
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


# In[38]:


def fetch_housing_data(housing_url=housing_url, housing_path=housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    logger.info("Dataset downloaded")


# In[39]:


def load_housing_data(housing_path=housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# In[40]:


def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)


# In[ ]:




