import argparse
import logging
import os
import pickle

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

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

args = parser.parse_args()


if args.folder_path:
    housing_path = os.path.join(args.folder_path, "data", "processed")

if args.model_directory_path:
    path = os.path.join(args.model_directory_path, "artifacts")
    os.mkdir(path)
    filename = path + "/finalized_model.sav"
else:
    path = "../artifacts"
    os.mkdir(path)
    filename = path + "/finalized_model.sav"

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
    logfile = args.log_path + "/logs/train.log"

if args.no_console_log:
    consolelog = 0

logging.basicConfig(filename=logfile, level=loglevel)
logger = logging.getLogger("train.py")

if consolelog:
    ch = logging.StreamHandler()
    ch.setLevel(loglevel)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  

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
        rooms_ix, bedrooms_ix, population_ix, households_ix = (
            3,
            4,
            5,
            6,
        )

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

        logger.info("Preprocessing Done")

        param_grid = [
            {"n_estimators": [3, 10, 30], "max_features": [2, 4, 6, 8],},
            {
                "bootstrap": [False],
                "n_estimators": [3, 10],
                "max_features": [2, 3, 4],
            },
        ]

        forest_reg = RandomForestRegressor()

        grid_search = GridSearchCV(
            forest_reg,
            param_grid,
            cv=5,
            scoring="neg_mean_squared_error",
            return_train_score=True,
        )

        grid_search.fit(housing_prepared, housing_labels)
        grid_search.best_params_
        cvres = grid_search.cv_results_
        for mean_score, params in zip(
            cvres["mean_test_score"], cvres["params"]
        ):
            logger.info(
                "random forest with grid search gave score \n %s for parameters %s"
                % (str(np.sqrt(-mean_score)), str(params))
            )
        final_model = grid_search.best_estimator_
        
        logger.info("model trained")
        os.makedirs(os.path.dirname(filename), exist_ok=True) #stack overflow
        pickle.dump(final_model, open(filename, "wb"))
        logger.info("model saved in " + filename)
    except Exception as e:
        logger.exception("Error Occured")
        logger.exception(e)
except Exception as e:
    logger.exception("Data not loaded")
    logger.exception(e)
