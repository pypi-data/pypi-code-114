import pandas as pd
import click
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from typing import List, Dict

class SplitWords(BaseEstimator, TransformerMixin):
    #the constructor
    '''setting the add_bedrooms_per_room to True helps us check if the hyperparameter is useful'''
    def __init__(self, word_columns: str, separators: List[str]= [",", "/", ";", ":", "(", ")"]):
        self.word_columns = word_columns
        self.separators = separators

    #estimator method
    def fit(self, X, y = None):
        return self

    #transfprmation
    def transform(self, X, y = None) -> pd.DataFrame:
        for sep in self.separators:
            X.loc[:, self.word_columns] = X.loc[:, self.word_columns].map(lambda x: " ".join(x.split(sep)))
        X.loc[:, self.word_columns] = X.loc[:, self.word_columns].map(lambda x: " ".join(x.split()))
        return X.loc[:, self.word_columns]

class AutomatedKMeans(BaseEstimator, TransformerMixin):
    #the constructor
    '''setting the add_bedrooms_per_room to True helps us check if the hyperparameter is useful'''
    def __init__(self, clusters_range: List[int]):
        self.clusters_range = clusters_range
        self.kmeans = {}
        click.echo(f"Building kmeans for following number of clusters: {self.clusters_range}")
        for cluster in self.clusters_range:
            self.kmeans[cluster] = KMeans(cluster, random_state=64)
        self.best_kmeans = None

    def _best_clusters_by_silhouette_score(self, silouhettes_scores: Dict[int, float]) -> int:
        best_clusters = 0
        _best_score = 0
        for k, v in silouhettes_scores.items():
            if v >= _best_score:
                best_clusters = k
                _best_score = v
        return best_clusters

    #estimator method
    def fit(self, X, y = None):
        silhouette_scores = {}
        for k, v in self.kmeans.items():
            if pd.api.types.is_sparse(X):
                X = X.toarray()
            predicted = v.fit_predict(X)
            silhouette_scores[k] = silhouette_score(X, predicted)
        
        self._appropriate_n_cluster = self._best_clusters_by_silhouette_score(silhouette_scores)
        click.echo(f"Found {self._appropriate_n_cluster} clusters")
        self.best_kmeans = self.kmeans[self._appropriate_n_cluster]
        return self

    #transfprmation
    def predict(self, X) -> pd.DataFrame:
        if pd.api.types.is_sparse(X):
            X = X.toarray()

        return self.best_kmeans.predict(X)


