from typing import List, Dict
import os


class DatasetInfo(object):

    def __init__(self, sql: str,
                 entity_key: str,
                 feature_names: List,
                 prediction_database: str,
                 prediction_table: str,
                 target_names: List = None,
                 legacy_data_conf: Dict = None):
        self.sql = sql
        self.entity_key = entity_key
        self.feature_names = feature_names
        self.target_names = target_names
        self.prediction_database = prediction_database
        self.prediction_table = prediction_table
        self.legacy_data_conf = legacy_data_conf

    @classmethod
    def from_dict(cls, rendered_dataset: Dict):
        if "type" in rendered_dataset and rendered_dataset["type"] == "VantageCatalogBody":
            return cls(sql=rendered_dataset.get("sql"),
                       entity_key=rendered_dataset.get("entityKey"),
                       feature_names=rendered_dataset.get("featureNames"),
                       target_names=rendered_dataset.get("targetNames"),
                       prediction_database=rendered_dataset.get("predictions").get("database"),
                       prediction_table=rendered_dataset.get("predictions").get("table"))
        else:
            # # set dict and legacy
            return cls(sql=None,
                       entity_key=None,
                       feature_names=None,
                       target_names=None,
                       prediction_database=None,
                       prediction_table=None,
                       legacy_data_conf=rendered_dataset)

    def is_legacy(self):
        return self.legacy_data_conf is None


class ModelContext(object):

    def __init__(self, hyperparams: Dict,
                 dataset_info: DatasetInfo,
                 artefact_output_path: str = None,
                 artefact_input_path: str = None):

        self.hyperparams = hyperparams
        self.artefact_output_path = artefact_output_path
        self.artefact_input_path = artefact_input_path
        self.dataset_info = dataset_info

    @property
    def artefact_output_path(self):
        return self.__artefact_output_path

    @artefact_output_path.setter
    def artefact_output_path(self, artefact_output_path):
        if artefact_output_path and not os.path.isdir(artefact_output_path):
            raise ValueError(f"artefact_output_path ({artefact_output_path}) does not exist")

        self.__artefact_output_path = artefact_output_path

    @property
    def artefact_input_path(self):
        return self.__artefact_input_path

    @artefact_input_path.setter
    def artefact_input_path(self, artefact_input_path):
        if artefact_input_path and not os.path.isdir(artefact_input_path):
            raise ValueError(f"artefact_input_path ({artefact_input_path}) does not exist")

        self.__artefact_input_path = artefact_input_path

