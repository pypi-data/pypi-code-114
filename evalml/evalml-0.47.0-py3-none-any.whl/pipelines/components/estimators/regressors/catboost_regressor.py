"""CatBoost Regressor, a regressor that uses gradient-boosting on decision trees. CatBoost is an open-source library and natively supports categorical features."""
import copy
import warnings

import pandas as pd
from skopt.space import Integer, Real

from evalml.model_family import ModelFamily
from evalml.pipelines.components.estimators import Estimator
from evalml.problem_types import ProblemTypes
from evalml.utils import import_or_raise, infer_feature_types


class CatBoostRegressor(Estimator):
    """CatBoost Regressor, a regressor that uses gradient-boosting on decision trees. CatBoost is an open-source library and natively supports categorical features.

    For more information, check out https://catboost.ai/

    Args:
        n_estimators (float): The maximum number of trees to build. Defaults to 10.
        eta (float): The learning rate. Defaults to 0.03.
        max_depth (int): The maximum tree depth for base learners. Defaults to 6.
        bootstrap_type (string): Defines the method for sampling the weights of objects. Available methods are 'Bayesian', 'Bernoulli', 'MVS'. Defaults to None.
        silent (boolean): Whether to use the "silent" logging mode. Defaults to True.
        allow_writing_files (boolean): Whether to allow writing snapshot files while training. Defaults to False.
        n_jobs (int or None): Number of jobs to run in parallel. -1 uses all processes. Defaults to -1.
        random_seed (int): Seed for the random number generator. Defaults to 0.
    """

    name = "CatBoost Regressor"
    hyperparameter_ranges = {
        "n_estimators": Integer(4, 100),
        "eta": Real(0.000001, 1),
        "max_depth": Integer(4, 10),
    }
    """{
        "n_estimators": Integer(4, 100),
        "eta": Real(0.000001, 1),
        "max_depth": Integer(4, 10),
    }"""
    model_family = ModelFamily.CATBOOST
    """ModelFamily.CATBOOST"""
    supported_problem_types = [
        ProblemTypes.REGRESSION,
        ProblemTypes.TIME_SERIES_REGRESSION,
    ]
    """[
        ProblemTypes.REGRESSION,
        ProblemTypes.TIME_SERIES_REGRESSION,
    ]"""

    def __init__(
        self,
        n_estimators=10,
        eta=0.03,
        max_depth=6,
        bootstrap_type=None,
        silent=False,
        allow_writing_files=False,
        random_seed=0,
        n_jobs=-1,
        **kwargs,
    ):
        parameters = {
            "n_estimators": n_estimators,
            "eta": eta,
            "max_depth": max_depth,
            "bootstrap_type": bootstrap_type,
            "silent": silent,
            "allow_writing_files": allow_writing_files,
        }
        if kwargs.get("thread_count", None) is not None:
            warnings.warn(
                "Parameter 'thread_count' will be ignored. To use parallel threads, use the 'n_jobs' parameter instead."
            )
        parameters.update(kwargs)

        cb_error_msg = (
            "catboost is not installed. Please install using `pip install catboost.`"
        )
        catboost = import_or_raise("catboost", error_msg=cb_error_msg)
        # catboost will choose an intelligent default for bootstrap_type, so only set if provided
        cb_parameters = copy.copy(parameters)
        if bootstrap_type is None:
            cb_parameters.pop("bootstrap_type")
        cb_parameters["thread_count"] = n_jobs
        cb_regressor = catboost.CatBoostRegressor(
            **cb_parameters, random_seed=random_seed
        )
        parameters["n_jobs"] = n_jobs
        super().__init__(
            parameters=parameters, component_obj=cb_regressor, random_seed=random_seed
        )

    def fit(self, X, y=None):
        """Fits CatBoost regressor component to data.

        Args:
            X (pd.DataFrame): The input training data of shape [n_samples, n_features].
            y (pd.Series): The target training data of length [n_samples].

        Returns:
            self
        """
        X = infer_feature_types(X)
        cat_cols = list(X.ww.select("category", return_schema=True).columns)
        self.input_feature_names = list(X.columns)
        X, y = super()._manage_woodwork(X, y)
        self._component_obj.fit(X, y, silent=True, cat_features=cat_cols)
        return self

    @property
    def feature_importance(self):
        """Feature importance of fitted CatBoost regressor."""
        return pd.Series(self._component_obj.get_feature_importance())
