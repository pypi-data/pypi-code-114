import pyspark
from ruamel import yaml

import great_expectations as ge
from great_expectations import DataContext
from great_expectations.core import ExpectationSuite
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.data_context.util import file_relative_path
from great_expectations.validator.validator import Validator

context: DataContext = ge.get_context()

yaml = yaml.YAML(typ="safe")

spark_session: pyspark.sql.session.SparkSession = (
    ge.core.util.get_or_create_spark_application()
)

# create and load Expectation Suite
context.create_expectation_suite(
    expectation_suite_name="insert_your_expectation_suite_name_here"
)
suite: ExpectationSuite = context.get_expectation_suite(
    expectation_suite_name="insert_your_expectation_suite_name_here"
)

datasource_yaml = f"""
name: my_spark_datasource
class_name: Datasource
module_name: great_expectations.datasource
execution_engine:
    module_name: great_expectations.execution_engine
    class_name: SparkDFExecutionEngine
data_connectors:
    my_runtime_data_connector:
        class_name: RuntimeDataConnector
        batch_identifiers:
            - some_key_maybe_pipeline_stage
            - some_other_key_maybe_airflow_run_id
"""

context.add_datasource(**yaml.load(datasource_yaml))

# RuntimeBatchRequest with batch_data as Spark Dataframe
path_to_file: str = "some_path.csv"

# Please note this override is only to provide good UX for docs and tests.
path_to_file: str = file_relative_path(
    __file__, "data/yellow_tripdata_sample_2019-01.csv"
)

df: pyspark.sql.dataframe.DataFrame = spark_session.read.csv(path_to_file)
runtime_batch_request = RuntimeBatchRequest(
    datasource_name="my_spark_datasource",
    data_connector_name="my_runtime_data_connector",
    data_asset_name="insert_your_data_asset_name_here",
    runtime_parameters={"batch_data": df},
    batch_identifiers={
        "some_key_maybe_pipeline_stage": "ingestion step 1",
        "some_other_key_maybe_airflow_run_id": "run 18",
    },
)

# Please note this override is only to provide good UX for docs and tests.
path_to_file: str = file_relative_path(
    __file__, "data/yellow_tripdata_sample_2019-01.csv"
)

# RuntimeBatchRequest with path
runtime_batch_request = RuntimeBatchRequest(
    datasource_name="my_spark_datasource",
    data_connector_name="my_runtime_data_connector",
    data_asset_name="insert_your_data_asset_name_here",
    runtime_parameters={"path": path_to_file},
    batch_identifiers={
        "some_key_maybe_pipeline_stage": "ingestion step 1",
        "some_other_key_maybe_airflow_run_id": "run 18",
    },
)

# Constructing Validator by passing in RuntimeBatchRequest
my_validator: Validator = context.get_validator(
    batch_request=runtime_batch_request,
    expectation_suite=suite,  # OR
    # expectation_suite_name=suite_name
)
my_validator.head()

# Constructing Validator by passing in arguments
my_validator: Validator = context.get_validator(
    datasource_name="my_spark_datasource",
    data_connector_name="my_runtime_data_connector",
    data_asset_name="insert_your_data_asset_name_here",
    runtime_parameters={"path": path_to_file},
    batch_identifiers={
        "some_key_maybe_pipeline_stage": "ingestion step 1",
        "some_other_key_maybe_airflow_run_id": "run 18",
    },
    batch_spec_passthrough={
        "reader_method": "csv",
        "reader_options": {"delimiter": ",", "header": True},
    },
    expectation_suite=suite,  # OR
    # expectation_suite_name=suite_name
)
my_validator.head()
