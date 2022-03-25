"Training module for classifier"
import dataclasses
from pathlib import Path
from typing import Any, List, Tuple

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from classifier import __version__ as classifier_version
from classifier.settings import ALGORITHM_DICT
from classifier.utils.config import Configuration
from classifier.utils.general import get_available_model_args


def train_dataset(dataset: pd.DataFrame, algorithm: str, out_dir: Path,
                  config: Configuration) -> Tuple[dict, np.ndarray]:
    """Train the model using a dataset

    Args:
        dataset (pd.DataFrame): Dataset containing features in the columns
            with one column named "class" which contains class labels or numbers
        algorithm (str): The algorithm name
        out_dir (Path): Path where to write dataset file
        config (Configuration): contains config

    Returns:
        model_dict (dict): A dictionary containing the name, model and label
                        encoder.
        test (np.ndarray): A test dataset which was not used during training
    """
    # Encode the labels
    labels = np.unique(dataset['class'].values).tolist()
    labels = dict(zip(range(len(labels)), labels))
    # Split the dataset,
    model, xcols, test = init_model_and_train(dataset,
                                              algorithm,
                                              out_dir,
                                              config)

    model_dict = {'app_algorithm': algorithm,
                  'model': model,
                  'labels': labels,
                  'names': xcols,
                  'version': classifier_version}
    return model_dict, test


def set_model_parameters(algorithm: str, algorithm_args: dict) -> Any:
    """ Set the model parameters

    Args:
        algorithm (str): internal name of the algorithm (model)
        algorithm_args (dict): Algorithm arguments

    Returns:
        model (Any): parametrized model
    """
    model_type = ALGORITHM_DICT[algorithm]
    model = model_type()
    model_algorithm_args = get_available_model_args(algorithm_args, model_type)
    model.set_params(**model_algorithm_args)
    return model


def get_algorithm_args(config: Configuration, dataset: pd.DataFrame) -> dict:
    """Fills the algorithm arg dict for the chosen algorithm

    Args:
        config (Configuration): Contains Configuration including algorithm
            name and some parameters
        dataset (pd.Dataframe): Dataset

    Returns:
        algorithm_args (dict): Contains specific model keyword and arguments
            for the model initialization
    """
    algorithm_name = config.app.algorithm
    algorithm_args = {}

    if algorithm_name == 'randomforest':
        # Random forest
        algorithm_args = dataclasses.asdict(config.randomforest)
    elif algorithm_name == 'xgboost' and len(dataset['class'].unique()) < 3:
        # xgboost
        algorithm_args['objective'] = 'binary:logistic'
    algorithm_args['n_jobs'] = config.app.threads
    return algorithm_args


def init_model_and_train(dataset: pd.DataFrame,
                         algorithm: str,
                         out_dir: Path,
                         config: Configuration) -> Tuple[
                             Any, List[str], pd.DataFrame]:
    """Set the model parameters and train it

    Args:
        dataset (Array) : The dataset for input in the model (array)
        algorithm (str): Internal name of the algorithm (model)
        out_dir (Path): The output directory
        config (Configuration): Contains config

    Returns:
        model (Any): Trained sklearn model
        xcols (List[str]): Names of bands
        test (pd.DataFrame): Test dataset

    """
    optimize = config.supervised.optimization.optimize
    optimize_iters = config.supervised.optimization.optimize_number
    test_size = config.accuracy.testfraction
    algorithm_args = {}
    train, test = train_test_split(dataset, test_size=test_size)
    xcols = [x for x in train.columns if 'class' not in x]
    x_train = train[xcols].values
    y_train = np.ravel(
        train[[x for x in train.columns if 'class' in x]].values)

    # Get the model/algorithm arguments
    algorithm_args = get_algorithm_args(config, dataset)

    # Create the model with the given params
    model = set_model_parameters(algorithm, algorithm_args)
    if optimize:
        try:
            model.parameter_matrix = {
                'max_features': config.supervised.optimization.max_features,
                'max_depth': config.supervised.optimization.max_depth,
                'max_leaf_nodes': config.supervised.optimization.max_leaf_nodes,
                'n_estimators': config.supervised.optimization.n_estimators}
            algorithm_args = model.random_optimise(
                x_train,
                y_train,
                out_dir,
                optimize_iters
            )
            model = set_model_parameters(algorithm, algorithm_args)
        except AttributeError as no_attribute:  # if there is no param. matrix
            raise AttributeError from no_attribute
    # y_train_encoded = sample_labels_encoder.transform(y_train)
    model.fit(x_train, y_train)
    return model, xcols, test
