# Copyright (c) 2021, 2022 Paul Irofti <paul@irofti.net>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import logging
import os

import numpy as np
import pandas as pd
import yaml
from attrdict import AttrDict
from sklearn.base import BaseEstimator
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelBinarizer

from .grid_search import GridSearch
from .models import ModelsLoader
from .preprocessing.egonet import EgonetFeatures
from .preprocessing.rwalk import RwalkFeatures
from .preprocessing.transactions_to_graph import Transactions2Graph
from .voting import VotingClassifier


class GraphomalyEstimator(BaseEstimator):
    def __init__(
        self,
        config_file="graphomaly.yaml",
        nn_models=["AmlAE", "AmlVAE"],
        n_cpus=1,
        preds2trans=None,
        voting="average",
        datadir="results",
    ):
        self.config_file = config_file
        self.n_cpus = n_cpus
        self.nn_models = nn_models
        self.preds2trans = preds2trans
        self.voting = voting
        self.datadir = datadir
        self.labels_ = []

        self.models_list = []
        self.models = []
        self.models_name = []
        self.feature_names_in_ = []

        # tune
        self.best_estimators = {}
        self.best_labels_ = {}
        self.best_params = {}
        self.best_score_ = {}

        logging.basicConfig(level=logging.INFO)

        # Sanity checks
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Couldn't find {self.config_file}.")

        with open(self.config_file) as f:
            self.config = AttrDict(yaml.safe_load(f))

        self.get_models_list()

    def load(self):
        """Load the dataset specified by name.

        Parameters
        ----------
        config : AttrDict
            The object containing the setup.

        Returns
        -------
        pandas.DataFrame
            Training dataset.

        array-like of shape (n_samples, )
            The true labels for training dataset.

        pandas.DataFrame
            Test dataset.

        array-like of shape (n_samples, )
            The true labels for test dataset.

        array-like of shape (n_samples, )
            The ids for training dataset.

        pandas.DataFrame
            The raw dataset.
        """
        raise NotImplementedError("Must override load_dataset")

    def preprocess(self, X, y, type=None, **kwargs):
        """Apply preprocessing operations on raw dataset.

        Parameters
        ----------
        X: array-like of shape (n_samples, n_features)
            The raw training dataset consiting of transactions list or graph

        y: array-like of shape (n_samples, )
            The ground truth for training dataset.

        type: string
            Preprocessing steps required. Depending on the input, the possible
            preprocessing actions are:
            * transactions_to_features (TODO)
            * graph_to_features
            * transactions_to_graph_to_features

        Keyword Args: dictionary
            The keyword args contains a dictionary consisting of two entries
            * to_graph_args: dictionary
                Contains fit `kwargs` for `preprocessing.transactions_to_graph`
                module
            * to_feature_args: dictionary
                Available key values
                * algorithms: list, `'egonet'`, `'rwalk'`
                * algorithms_args: dictionary, '`ctor_args'` and `'fit_args'`
                    *ctor_args: dictionary
                        Represents arguments passed to the algorithm's constructor.
                    *fit_args: dictionary
                        Represents options passed to the fit method.

        Returns
        -------
        X: The preprocessed training dataset

        y: The preprocessed labels

        See also
        --------
        tests.test_synthetic_preprocessing : example of building and passing kwargs
        """
        G = None

        # if type == "transactions_to_features":
        if type == "graph_to_features":
            X = self._process_graph_to_features(X, **kwargs)
        elif type == "transactions_to_graph_to_features":
            to_graph_args = kwargs["to_graph_args"]
            to_features_args = kwargs["to_features_args"]

            t2g = Transactions2Graph()
            G = t2g.fit_transform(X, **to_graph_args)

            X = self._process_graph_to_features(G, **to_features_args)
        return X, y, G

    def _process_graph_to_features(self, G, **kwargs):
        algorithms = kwargs["graph_algorithms"]
        algorithms_args = kwargs["graph_algorithms_args"]

        all_features = []
        for i, algo in enumerate(algorithms):
            ctor_args = algorithms_args[i]["ctor_args"]
            fit_args = algorithms_args[i]["fit_args"]
            if algo == "egonet":
                ego = EgonetFeatures(**ctor_args)
                features = ego.fit_transform(G, **fit_args)
                features_names_in = ego.feature_names_in_
            elif algo == "rwalk":
                rwalk = RwalkFeatures(**ctor_args)
                features = rwalk.fit_transform(G, **fit_args)
                features_names_in = rwalk.feature_names_in_
            all_features.append(features)
            self.feature_names_in_.append(features_names_in)

        return np.concatenate(all_features, axis=1)

    def _get_params(self, algorithm, n_features):
        if algorithm not in self.config.models.models_kwargs:
            model_kwargs = {}
        else:
            model_kwargs = self.config.models.models_kwargs[algorithm]

        if algorithm not in self.config.models.fit_kwargs:
            fit_kwargs = {}
        else:
            fit_kwargs = self.config.models.fit_kwargs[algorithm]

        # Setting the correct number of decoder neurons after preprocessing.
        if "decoder_neurons" in model_kwargs:
            model_kwargs["decoder_neurons"][-1] = n_features

        if "input_dim" in model_kwargs:
            model_kwargs["input_dim"] = n_features

        if "contamination" in model_kwargs:
            model_kwargs["contamination"] = self.config.dataset.contamination

        return model_kwargs, fit_kwargs

    def get_models_list(self):
        if self.config.models.train_all:
            self.models_list = ModelsLoader.models
        else:
            self.models_list = self.config.models.subset

    def fit(self, X, y=None):
        self.tune(X, y)

        return self

    def predict(self, X, y=None, voting=None):
        self.labels_ = self.vote(X, y, voting)
        return self.labels_

    def vote(self, X, y=None, voting=None):
        if voting:
            self.voting = voting
        if self.known_best_estimator:
            estimators = [(i, j) for i, j in zip(self.models_list, self.models)]
        else:
            estimators = [(i, j) for i, j in zip(self.models_name, self.models)]
        eclf = VotingClassifier(estimators=estimators, voting=self.voting)
        y = eclf.fit_predict(X, y)
        return y

    def tune(self, X, y=None):
        for algorithm in self.models_list:
            # if algorithm == "AmlAE" or algorithm == "AmlVAE":
            #     continue  # autoencoders are not ready yet
            model_kwargs, fit_kwargs = self._get_params(algorithm, X.shape[1])
            clf = ModelsLoader.get(algorithm, **model_kwargs)
            if hasattr(clf, "save"):  # tf model detected
                clf_type = "tensorflow"
            else:
                clf_type = "sklearn"

            search = GridSearch(
                clf,
                fit_kwargs,
                n_cpus=self.n_cpus,
                datadir=self.datadir,
                clf_type=clf_type,
            )
            search.fit(X, y)

            if y is None:
                self.models_name.extend([algorithm])
                self.models.extend(search.estimators_)
                self.known_best_estimator = False
            else:
                self.best_params[algorithm] = search.best_params_
                self.best_estimators[algorithm] = search.best_estimator_
                self.best_labels_[algorithm] = search.labels_
                self.best_score_[algorithm] = search.best_score_
                self.known_best_estimator = True

                self.models.append(search.best_estimator_)

                logging.info(
                    f"Best params for {algorithm}[BA={search.best_score_}]: "
                    f"{search.best_params_}"
                )

        return self

    def encode_column(self, X, col, nletter, do_pca, nc=6):
        lb = LabelBinarizer()

        mat = lb.fit_transform(X[col].astype(str))
        X.drop(columns=[col], axis=1, inplace=True)

        if do_pca:
            pca = PCA(n_components=nc, copy=False)
            mat_pca = pca.fit_transform(mat)
            cols = [nletter + str(x) for x in range(nc)]
            X = pd.concat([X, pd.DataFrame(mat_pca, columns=cols)], axis=1)
        else:
            cols = [nletter + str(x) for x in range(mat.shape[1])]
            X = pd.concat([X, pd.DataFrame(mat, columns=cols)], axis=1)

        return X
