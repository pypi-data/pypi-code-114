from offline_model_builder.user_profile.clustering.cluster_generator import ClusterGenerator
from offline_model_builder.common.read_write_s3 import ConnectS3
from offline_model_builder.user_profile.clustering.ensemble_controller import EnsembleController
from offline_model_builder.user_profile.clustering.evaluation.utils import EvaluationUtils
from offline_model_builder.user_profile.clustering.evaluation.constants import NON_FEATURES
from offline_model_builder.user_profile.constants import CUSTOMER_ID, BIRCH_ENSEMBLE_FEATURE, \
    CSV_EXTENSION


class ClusterFeaturesGenerator:

    @staticmethod
    def create_cluster_features(
            resource,
            s3_bucket_name,
            s3_object_name,
            user_profile
    ):

        cluster_generator = ClusterGenerator(
            data=user_profile
        )
        cluster_generator.controller()

        ensemble_controller = EnsembleController(
            data=cluster_generator.clusters
        )
        ensemble_controller.controller()

        eval_utils = EvaluationUtils(
            data=cluster_generator.clusters
        )
        eval_utils.retrieve_ensemble_results()
        eval_utils.merge_ensemble_results()
        NON_FEATURES.append(BIRCH_ENSEMBLE_FEATURE)
        for feature in NON_FEATURES:
            if feature == CUSTOMER_ID:
                continue
            rel = eval_utils.data[[CUSTOMER_ID, feature]]

            ConnectS3().write_csv_to_s3(
                bucket_name=s3_bucket_name,
                object_name=s3_object_name + feature + CSV_EXTENSION,
                df_to_upload=rel,
                resource=resource
            )
