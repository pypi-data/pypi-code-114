"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_machinelearning/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_machinelearning.type_defs import AddTagsInputRequestTypeDef

    data: AddTagsInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BatchPredictionFilterVariableType,
    DataSourceFilterVariableType,
    DetailsAttributesType,
    EntityStatusType,
    EvaluationFilterVariableType,
    MLModelFilterVariableType,
    MLModelTypeType,
    RealtimeEndpointStatusType,
    SortOrderType,
    TaggableResourceTypeType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddTagsInputRequestTypeDef",
    "AddTagsOutputTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionInputRequestTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSInputRequestTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftInputRequestTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3InputRequestTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationInputRequestTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelInputRequestTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointInputRequestTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionInputRequestTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceInputRequestTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationInputRequestTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelInputRequestTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointInputRequestTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsInputRequestTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsInputRequestTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesInputRequestTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsInputRequestTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsInputRequestTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsInputRequestTypeDef",
    "DescribeTagsOutputTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionInputRequestTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceInputRequestTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationInputRequestTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelInputRequestTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictInputRequestTypeDef",
    "PredictOutputTypeDef",
    "PredictionTypeDef",
    "RDSDataSpecTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RDSMetadataTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "RedshiftDataSpecTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "RedshiftMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSpecTypeDef",
    "TagTypeDef",
    "UpdateBatchPredictionInputRequestTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceInputRequestTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationInputRequestTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelInputRequestTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsInputRequestTypeDef = TypedDict(
    "AddTagsInputRequestTypeDef",
    {
        "Tags": Sequence["TagTypeDef"],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

AddTagsOutputTypeDef = TypedDict(
    "AddTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPredictionTypeDef = TypedDict(
    "BatchPredictionTypeDef",
    {
        "BatchPredictionId": NotRequired[str],
        "MLModelId": NotRequired[str],
        "BatchPredictionDataSourceId": NotRequired[str],
        "InputDataLocationS3": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "OutputUri": NotRequired[str],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
        "TotalRecordCount": NotRequired[int],
        "InvalidRecordCount": NotRequired[int],
    },
)

CreateBatchPredictionInputRequestTypeDef = TypedDict(
    "CreateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "OutputUri": str,
        "BatchPredictionName": NotRequired[str],
    },
)

CreateBatchPredictionOutputTypeDef = TypedDict(
    "CreateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromRDSInputRequestTypeDef = TypedDict(
    "CreateDataSourceFromRDSInputRequestTypeDef",
    {
        "DataSourceId": str,
        "RDSData": "RDSDataSpecTypeDef",
        "RoleARN": str,
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)

CreateDataSourceFromRDSOutputTypeDef = TypedDict(
    "CreateDataSourceFromRDSOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromRedshiftInputRequestTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "RedshiftDataSpecTypeDef",
        "RoleARN": str,
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)

CreateDataSourceFromRedshiftOutputTypeDef = TypedDict(
    "CreateDataSourceFromRedshiftOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataSourceFromS3InputRequestTypeDef = TypedDict(
    "CreateDataSourceFromS3InputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSpec": "S3DataSpecTypeDef",
        "DataSourceName": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
    },
)

CreateDataSourceFromS3OutputTypeDef = TypedDict(
    "CreateDataSourceFromS3OutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEvaluationInputRequestTypeDef = TypedDict(
    "CreateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "EvaluationName": NotRequired[str],
    },
)

CreateEvaluationOutputTypeDef = TypedDict(
    "CreateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMLModelInputRequestTypeDef = TypedDict(
    "CreateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "MLModelType": MLModelTypeType,
        "TrainingDataSourceId": str,
        "MLModelName": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "Recipe": NotRequired[str],
        "RecipeUri": NotRequired[str],
    },
)

CreateMLModelOutputTypeDef = TypedDict(
    "CreateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRealtimeEndpointInputRequestTypeDef = TypedDict(
    "CreateRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

CreateRealtimeEndpointOutputTypeDef = TypedDict(
    "CreateRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "DataSourceId": NotRequired[str],
        "DataLocationS3": NotRequired[str],
        "DataRearrangement": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "DataSizeInBytes": NotRequired[int],
        "NumberOfFiles": NotRequired[int],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "Message": NotRequired[str],
        "RedshiftMetadata": NotRequired["RedshiftMetadataTypeDef"],
        "RDSMetadata": NotRequired["RDSMetadataTypeDef"],
        "RoleARN": NotRequired[str],
        "ComputeStatistics": NotRequired[bool],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)

DeleteBatchPredictionInputRequestTypeDef = TypedDict(
    "DeleteBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)

DeleteBatchPredictionOutputTypeDef = TypedDict(
    "DeleteBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDataSourceInputRequestTypeDef = TypedDict(
    "DeleteDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
    },
)

DeleteDataSourceOutputTypeDef = TypedDict(
    "DeleteDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEvaluationInputRequestTypeDef = TypedDict(
    "DeleteEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)

DeleteEvaluationOutputTypeDef = TypedDict(
    "DeleteEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLModelInputRequestTypeDef = TypedDict(
    "DeleteMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteMLModelOutputTypeDef = TypedDict(
    "DeleteMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRealtimeEndpointInputRequestTypeDef = TypedDict(
    "DeleteRealtimeEndpointInputRequestTypeDef",
    {
        "MLModelId": str,
    },
)

DeleteRealtimeEndpointOutputTypeDef = TypedDict(
    "DeleteRealtimeEndpointOutputTypeDef",
    {
        "MLModelId": str,
        "RealtimeEndpointInfo": "RealtimeEndpointInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTagsInputRequestTypeDef = TypedDict(
    "DeleteTagsInputRequestTypeDef",
    {
        "TagKeys": Sequence[str],
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DeleteTagsOutputTypeDef = TypedDict(
    "DeleteTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBatchPredictionsInputRequestTypeDef = TypedDict(
    "DescribeBatchPredictionsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[BatchPredictionFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeBatchPredictionsOutputTypeDef = TypedDict(
    "DescribeBatchPredictionsOutputTypeDef",
    {
        "Results": List["BatchPredictionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDataSourcesInputRequestTypeDef = TypedDict(
    "DescribeDataSourcesInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[DataSourceFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeDataSourcesOutputTypeDef = TypedDict(
    "DescribeDataSourcesOutputTypeDef",
    {
        "Results": List["DataSourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEvaluationsInputRequestTypeDef = TypedDict(
    "DescribeEvaluationsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[EvaluationFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeEvaluationsOutputTypeDef = TypedDict(
    "DescribeEvaluationsOutputTypeDef",
    {
        "Results": List["EvaluationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMLModelsInputRequestTypeDef = TypedDict(
    "DescribeMLModelsInputRequestTypeDef",
    {
        "FilterVariable": NotRequired[MLModelFilterVariableType],
        "EQ": NotRequired[str],
        "GT": NotRequired[str],
        "LT": NotRequired[str],
        "GE": NotRequired[str],
        "LE": NotRequired[str],
        "NE": NotRequired[str],
        "Prefix": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
        "NextToken": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeMLModelsOutputTypeDef = TypedDict(
    "DescribeMLModelsOutputTypeDef",
    {
        "Results": List["MLModelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsInputRequestTypeDef = TypedDict(
    "DescribeTagsInputRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
    },
)

DescribeTagsOutputTypeDef = TypedDict(
    "DescribeTagsOutputTypeDef",
    {
        "ResourceId": str,
        "ResourceType": TaggableResourceTypeType,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "EvaluationId": NotRequired[str],
        "MLModelId": NotRequired[str],
        "EvaluationDataSourceId": NotRequired[str],
        "InputDataLocationS3": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "PerformanceMetrics": NotRequired["PerformanceMetricsTypeDef"],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)

GetBatchPredictionInputRequestTypeDef = TypedDict(
    "GetBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
    },
)

GetBatchPredictionOutputTypeDef = TypedDict(
    "GetBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "MLModelId": str,
        "BatchPredictionDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "OutputUri": str,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "TotalRecordCount": int,
        "InvalidRecordCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataSourceInputRequestTypeDef = TypedDict(
    "GetDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
        "Verbose": NotRequired[bool],
    },
)

GetDataSourceOutputTypeDef = TypedDict(
    "GetDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "DataLocationS3": str,
        "DataRearrangement": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "DataSizeInBytes": int,
        "NumberOfFiles": int,
        "Name": str,
        "Status": EntityStatusType,
        "LogUri": str,
        "Message": str,
        "RedshiftMetadata": "RedshiftMetadataTypeDef",
        "RDSMetadata": "RDSMetadataTypeDef",
        "RoleARN": str,
        "ComputeStatistics": bool,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "DataSourceSchema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEvaluationInputRequestTypeDef = TypedDict(
    "GetEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
    },
)

GetEvaluationOutputTypeDef = TypedDict(
    "GetEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "MLModelId": str,
        "EvaluationDataSourceId": str,
        "InputDataLocationS3": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "PerformanceMetrics": "PerformanceMetricsTypeDef",
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLModelInputRequestTypeDef = TypedDict(
    "GetMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "Verbose": NotRequired[bool],
    },
)

GetMLModelOutputTypeDef = TypedDict(
    "GetMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "TrainingDataSourceId": str,
        "CreatedByIamUser": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Name": str,
        "Status": EntityStatusType,
        "SizeInBytes": int,
        "EndpointInfo": "RealtimeEndpointInfoTypeDef",
        "TrainingParameters": Dict[str, str],
        "InputDataLocationS3": str,
        "MLModelType": MLModelTypeType,
        "ScoreThreshold": float,
        "ScoreThresholdLastUpdatedAt": datetime,
        "LogUri": str,
        "Message": str,
        "ComputeTime": int,
        "FinishedAt": datetime,
        "StartedAt": datetime,
        "Recipe": str,
        "Schema": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MLModelTypeDef = TypedDict(
    "MLModelTypeDef",
    {
        "MLModelId": NotRequired[str],
        "TrainingDataSourceId": NotRequired[str],
        "CreatedByIamUser": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "LastUpdatedAt": NotRequired[datetime],
        "Name": NotRequired[str],
        "Status": NotRequired[EntityStatusType],
        "SizeInBytes": NotRequired[int],
        "EndpointInfo": NotRequired["RealtimeEndpointInfoTypeDef"],
        "TrainingParameters": NotRequired[Dict[str, str]],
        "InputDataLocationS3": NotRequired[str],
        "Algorithm": NotRequired[Literal["sgd"]],
        "MLModelType": NotRequired[MLModelTypeType],
        "ScoreThreshold": NotRequired[float],
        "ScoreThresholdLastUpdatedAt": NotRequired[datetime],
        "Message": NotRequired[str],
        "ComputeTime": NotRequired[int],
        "FinishedAt": NotRequired[datetime],
        "StartedAt": NotRequired[datetime],
    },
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PerformanceMetricsTypeDef = TypedDict(
    "PerformanceMetricsTypeDef",
    {
        "Properties": NotRequired[Dict[str, str]],
    },
)

PredictInputRequestTypeDef = TypedDict(
    "PredictInputRequestTypeDef",
    {
        "MLModelId": str,
        "Record": Mapping[str, str],
        "PredictEndpoint": str,
    },
)

PredictOutputTypeDef = TypedDict(
    "PredictOutputTypeDef",
    {
        "Prediction": "PredictionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictionTypeDef = TypedDict(
    "PredictionTypeDef",
    {
        "predictedLabel": NotRequired[str],
        "predictedValue": NotRequired[float],
        "predictedScores": NotRequired[Dict[str, float]],
        "details": NotRequired[Dict[DetailsAttributesType, str]],
    },
)

RDSDataSpecTypeDef = TypedDict(
    "RDSDataSpecTypeDef",
    {
        "DatabaseInformation": "RDSDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RDSDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
        "ResourceRole": str,
        "ServiceRole": str,
        "SubnetId": str,
        "SecurityGroupIds": Sequence[str],
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaUri": NotRequired[str],
    },
)

RDSDatabaseCredentialsTypeDef = TypedDict(
    "RDSDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RDSDatabaseTypeDef = TypedDict(
    "RDSDatabaseTypeDef",
    {
        "InstanceIdentifier": str,
        "DatabaseName": str,
    },
)

RDSMetadataTypeDef = TypedDict(
    "RDSMetadataTypeDef",
    {
        "Database": NotRequired["RDSDatabaseTypeDef"],
        "DatabaseUserName": NotRequired[str],
        "SelectSqlQuery": NotRequired[str],
        "ResourceRole": NotRequired[str],
        "ServiceRole": NotRequired[str],
        "DataPipelineId": NotRequired[str],
    },
)

RealtimeEndpointInfoTypeDef = TypedDict(
    "RealtimeEndpointInfoTypeDef",
    {
        "PeakRequestsPerSecond": NotRequired[int],
        "CreatedAt": NotRequired[datetime],
        "EndpointUrl": NotRequired[str],
        "EndpointStatus": NotRequired[RealtimeEndpointStatusType],
    },
)

RedshiftDataSpecTypeDef = TypedDict(
    "RedshiftDataSpecTypeDef",
    {
        "DatabaseInformation": "RedshiftDatabaseTypeDef",
        "SelectSqlQuery": str,
        "DatabaseCredentials": "RedshiftDatabaseCredentialsTypeDef",
        "S3StagingLocation": str,
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaUri": NotRequired[str],
    },
)

RedshiftDatabaseCredentialsTypeDef = TypedDict(
    "RedshiftDatabaseCredentialsTypeDef",
    {
        "Username": str,
        "Password": str,
    },
)

RedshiftDatabaseTypeDef = TypedDict(
    "RedshiftDatabaseTypeDef",
    {
        "DatabaseName": str,
        "ClusterIdentifier": str,
    },
)

RedshiftMetadataTypeDef = TypedDict(
    "RedshiftMetadataTypeDef",
    {
        "RedshiftDatabase": NotRequired["RedshiftDatabaseTypeDef"],
        "DatabaseUserName": NotRequired[str],
        "SelectSqlQuery": NotRequired[str],
    },
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

S3DataSpecTypeDef = TypedDict(
    "S3DataSpecTypeDef",
    {
        "DataLocationS3": str,
        "DataRearrangement": NotRequired[str],
        "DataSchema": NotRequired[str],
        "DataSchemaLocationS3": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UpdateBatchPredictionInputRequestTypeDef = TypedDict(
    "UpdateBatchPredictionInputRequestTypeDef",
    {
        "BatchPredictionId": str,
        "BatchPredictionName": str,
    },
)

UpdateBatchPredictionOutputTypeDef = TypedDict(
    "UpdateBatchPredictionOutputTypeDef",
    {
        "BatchPredictionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDataSourceInputRequestTypeDef = TypedDict(
    "UpdateDataSourceInputRequestTypeDef",
    {
        "DataSourceId": str,
        "DataSourceName": str,
    },
)

UpdateDataSourceOutputTypeDef = TypedDict(
    "UpdateDataSourceOutputTypeDef",
    {
        "DataSourceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEvaluationInputRequestTypeDef = TypedDict(
    "UpdateEvaluationInputRequestTypeDef",
    {
        "EvaluationId": str,
        "EvaluationName": str,
    },
)

UpdateEvaluationOutputTypeDef = TypedDict(
    "UpdateEvaluationOutputTypeDef",
    {
        "EvaluationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMLModelInputRequestTypeDef = TypedDict(
    "UpdateMLModelInputRequestTypeDef",
    {
        "MLModelId": str,
        "MLModelName": NotRequired[str],
        "ScoreThreshold": NotRequired[float],
    },
)

UpdateMLModelOutputTypeDef = TypedDict(
    "UpdateMLModelOutputTypeDef",
    {
        "MLModelId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
