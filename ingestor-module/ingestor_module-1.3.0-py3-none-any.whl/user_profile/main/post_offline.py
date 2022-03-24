from ingestor.common.read_write_from_s3 import ConnectS3
from ingestor.common.constants import CSV_EXTENSION
from ingestor.user_profile.main.config import S3_BUCKET_NAME, S3_OBJECT_NAME, \
    TO_READ_FROM_S3, CLUSTERING_METHODS
from pandas import DataFrame

from ingestor.user_profile.network.plot_relations import PlotRelations
from ingestor.user_profile.preferences.relationship_extractor import \
    RelationshipExtractor

class PostOfflineMain:

    def __init__(
            self,
            s3_resource: None
    ):
        self.s3_resource = s3_resource

    def get_file_from_s3(
            self,
            filename: str
    ) -> DataFrame:
        """
        Method to return CSV read from s3
        :param filename: file to obtain
        :return: dataframe object pandas
        """
        return ConnectS3().read_csv_from_s3(
            bucket_name=S3_BUCKET_NAME,
            object_name=S3_OBJECT_NAME + filename + CSV_EXTENSION,
            resource=self.s3_resource
        )

    def get_feature_relations(
            self,
            data: DataFrame
    ) -> DataFrame:
        """
        Use the relationship extractor to for
        relationship dataframe object based on
        user's preferences
        :param data: dataframe object pandas
        :return: dataframe object pandas with each
        record representing a relationship between
        a user and a node type.
        """
        re = RelationshipExtractor(
            data=data
        )
        return re.controller()

    def plot_relations(
            self,
            data: DataFrame,
            relation_label: str,
            destination_prop_label: str,
            connection_object
    ):
        """
        Dump the relations obtained from the
        relationship extractor into the Graph Database.
        The method to create relationship is create
        relationship without upsert
        :return: None, the update is reflected in the
        graph network network state.
        """
        pr = PlotRelations(
            data=data,
            label=relation_label,
            connection_uri=connection_object
        )
        pr.controller(
            destination_prop_label=destination_prop_label
        )

    def drop_nan_features(
            self,
            data
    ):
        to_drop = []
        for feature in data.columns:
            if feature[len(feature) - 4:] == '_nan':
                to_drop.append(feature)
        return data.drop(columns=to_drop)

    def controller(
            self,
            connection_object
    ):
        """
        The driver function for the procedure of dumping
        relations into GraphDB
        :return: None, the update is reflected in the
        graph network network state.
        """
        for filename, file_meta in TO_READ_FROM_S3.items():
            data = self.get_file_from_s3(
                filename=filename
            )

            data = self.drop_nan_features(data)
            if len(data.columns) == 1:
                continue

            print(
                "Dumping user relations with ",
                filename, " preferences"
                )

            if filename not in CLUSTERING_METHODS:
                data = self.get_feature_relations(
                    data=data
                )
            self.plot_relations(
                data=data,
                relation_label=file_meta[0],
                destination_prop_label=file_meta[1],
                connection_object=connection_object
            )