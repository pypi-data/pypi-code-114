import argparse
import logging
import os
import tarfile
import urllib.request

import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit, train_test_split

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

args = parser.parse_args()
if args.saveFile:
    housing_path = os.path.join(args.saveFile, "data", "raw")
    datapath = os.path.join(args.saveFile, "data")
    os.mkdir(datapath)    
    path = os.path.join(args.saveFile, "data", "processed")
    os.mkdir(path)
else:
    datapath = "../data"
    os.mkdir(datapath)    
    path = "../data/processed"
    os.mkdir(path)
housing_url = download_root + "datasets/housing/housing.tgz"

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

if args.log_path:
    path = os.path.join(args.log_path, "/logs")
    os.mkdir(path)
    logfile = path + "/ingest_data.log"
else:
    path = "../logs"
    os.mkdir(path)
    logfile = path + "/ingest_data.log"

if args.no_console_log:
    consolelog = 0

logging.basicConfig(filename=logfile, level=loglevel)
logger = logging.getLogger("ingest_data.py")

if consolelog:
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def fetch_housing_data(housing_url=housing_url, housing_path=housing_path):
    os.makedirs(housing_path, exist_ok=True)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()
    logger.info("Dataset downloaded")


def load_housing_data(housing_path=housing_path):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


def income_cat_proportions(data):
    return data["income_cat"].value_counts() / len(data)


try:
    fetch_housing_data()

    housing = load_housing_data()

    housing["income_cat"] = pd.cut(
        housing["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )

    train_set, test_set = train_test_split(
        housing, test_size=0.2, random_state=42
    )

    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        strat_test_set = housing.loc[test_index]

    compare_props = pd.DataFrame(
        {
            "Overall": income_cat_proportions(housing),
            "Stratified": income_cat_proportions(strat_test_set),
            "Random": income_cat_proportions(test_set),
        }
    ).sort_index()
    compare_props["Rand. %error"] = (
        100 * compare_props["Random"] / compare_props["Overall"] - 100
    )
    compare_props["Strat. %error"] = (
        100 * compare_props["Stratified"] / compare_props["Overall"] - 100
    )
    logger.info("The probability values are\n %s" % (compare_props))

    if args.saveFile:
        strat_train_set.to_excel(args.saveFile + "/data/processed/train.xlsx")
        strat_test_set.to_excel(args.saveFile + "/data/processed/test.xlsx")
        print("Files created in", datapath)
    else:
        # print("else part")
        strat_train_set.to_excel("../data/processed/train.xlsx")
        strat_test_set.to_excel("../data/processed/test.xlsx")

    logger.info("Train and Test Data saved succesfully")
except Exception as e:
    logger.exception("Some error occurred:")
    logger.exception(e)
