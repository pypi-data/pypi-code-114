import argparse
import logging
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

housing_path = "../data/processed"
filename = "../artifacts/finalized_model.sav"
loglevel = logging.DEBUG
logfile = "../logs/score.log"
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
    help="Mention the path to open the model. "
    + "Default Value: the artifacts in project folder",
)
parser.add_argument(
    "-ll", "--log_level", help="Mention the log level. Default Value: DEBUG"
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

if args.folder_path:
    housing_path = os.path.join(args.folder_path, "data", "processed")
if args.model_directory_path:
    filename = args.model_directory_path + "/artifacts/finalized_model.sav"

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
    logfile = args.log_path + "/logs/score.log"

if args.no_console_log:
    consolelog = 0

logging.basicConfig(filename=logfile, level=loglevel)
logger = logging.getLogger("score.py")

if consolelog:
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


def eval_metrics(actual, pred):
    # compute relevant metrics
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


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


try:
    strat_train_set = pd.read_excel(housing_path + "/train.xlsx", engine='openpyxl')
    strat_test_set = pd.read_excel(housing_path + "/test.xlsx", engine='openpyxl')
    logger.info("Data successfully loaded!!")
    try:
        for set_ in (strat_train_set, strat_test_set):
            set_.drop("income_cat", axis=1, inplace=True)

        housing = strat_train_set.copy()
        housing = strat_train_set.drop("median_house_value", axis=1)
        housing_labels = strat_train_set["median_house_value"].copy()
        rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6

        housing_num = housing.drop("ocean_proximity", axis=1)
        num_pipeline = Pipeline(
            [
                ("imputer", SimpleImputer(strategy="median")),
                ("attribs_adder", CombinedAttributesAdder()),
                ("std_scaler", StandardScaler()),
            ]
        )

        num_attribs = list(housing_num)
        cat_attribs = ["ocean_proximity"]

        full_pipeline = ColumnTransformer(
            [
                ("num", num_pipeline, num_attribs),
                ("cat", OneHotEncoder(), cat_attribs),
            ]
        )

        housing_prepared = full_pipeline.fit_transform(housing)

        X_test = strat_test_set.drop("median_house_value", axis=1)
        y_test = strat_test_set["median_house_value"].copy()

        X_test_prepared = full_pipeline.transform(X_test)

        loaded_model = pickle.load(open(filename, "rb"))
        predicted = loaded_model.predict(X_test_prepared)
        result = loaded_model.score(X_test_prepared, y_test)
        print("  Score: ", result)

        (rmse, mae, r2) = eval_metrics(y_test, predicted)

        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)
        logger.info("  Score: %s" % result)
        logger.info("  RMSE: %s" % rmse)
        logger.info("  MAE: %s" % mae)
        logger.info("  R2: %s" % r2)
        logger.info("excecuted with no errors")
    except Exception as e:
        logger.exception("Error Occured")
        logger.exception(e)
except Exception as e:
    logger.exception("Data not loaded")
    logger.exception(e)
