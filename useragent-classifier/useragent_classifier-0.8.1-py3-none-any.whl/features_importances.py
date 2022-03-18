import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from dataclasses import dataclass
from typing import List, Union, Dict

@dataclass
class FeatureImportance:
    features_names: List[str]
    labels: List[int]
    X: Union[pd.DataFrame, np.ndarray]
    top_n_words: int

    def _get_features_importances_one_vs_all(self, labels: List[int]) -> pd.DataFrame:
        self.classifier = RandomForestClassifier()

        assert len(pd.Series(labels).unique()) <= 2

        self.classifier.fit(self.X, labels)
        importances = pd.DataFrame(self.classifier.feature_importances_).T
        importances.columns = self.features_names

        importances = importances.T
        importances.columns = ["importance_score"]

        importances = importances.sort_values(by="importance_score", ascending=False)
        importances = importances.head(self.top_n_words)

        return importances.importance_score
    
    def get_features_importances_one_vs_all(self) -> Dict[int, pd.DataFrame]:
        res = {}
        unique_labels = set(self.labels)
        for label in unique_labels:
            one_vs_all_labels = [int(x == label) for x in self.labels]
            
            res[label] = self._get_features_importances_one_vs_all(one_vs_all_labels)
        return res
    