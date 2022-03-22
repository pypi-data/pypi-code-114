"""
Type annotations for lookoutvision service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import CreateDatasetRequestRequestTypeDef

    data: CreateDatasetRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    DatasetStatusType,
    ModelHostingStatusType,
    ModelPackagingJobStatusType,
    ModelStatusType,
    TargetPlatformArchType,
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
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateModelResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeModelPackagingJobRequestRequestTypeDef",
    "DescribeModelPackagingJobResponseTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DetectAnomaliesRequestRequestTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "DetectAnomalyResultTypeDef",
    "GreengrassConfigurationTypeDef",
    "GreengrassOutputDetailsTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ListDatasetEntriesRequestRequestTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListModelPackagingJobsRequestRequestTypeDef",
    "ListModelPackagingJobsResponseTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ListModelsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPackagingConfigurationTypeDef",
    "ModelPackagingDescriptionTypeDef",
    "ModelPackagingJobMetadataTypeDef",
    "ModelPackagingOutputDetailsTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "StartModelPackagingJobRequestRequestTypeDef",
    "StartModelPackagingJobResponseTypeDef",
    "StartModelRequestRequestTypeDef",
    "StartModelResponseTypeDef",
    "StopModelRequestRequestTypeDef",
    "StopModelResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetEntriesRequestRequestTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "DatasetSource": NotRequired["DatasetSourceTypeDef"],
        "ClientToken": NotRequired[str],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetMetadata": "DatasetMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "OutputConfig": "OutputConfigTypeDef",
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ModelMetadata": "ModelMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ClientToken": NotRequired[str],
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "ProjectMetadata": "ProjectMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatasetDescriptionTypeDef = TypedDict(
    "DatasetDescriptionTypeDef",
    {
        "ProjectName": NotRequired[str],
        "DatasetType": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
        "ImageStats": NotRequired["DatasetImageStatsTypeDef"],
    },
)

DatasetGroundTruthManifestTypeDef = TypedDict(
    "DatasetGroundTruthManifestTypeDef",
    {
        "S3Object": NotRequired["InputS3ObjectTypeDef"],
    },
)

DatasetImageStatsTypeDef = TypedDict(
    "DatasetImageStatsTypeDef",
    {
        "Total": NotRequired[int],
        "Labeled": NotRequired[int],
        "Normal": NotRequired[int],
        "Anomaly": NotRequired[int],
    },
)

DatasetMetadataTypeDef = TypedDict(
    "DatasetMetadataTypeDef",
    {
        "DatasetType": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Status": NotRequired[DatasetStatusType],
        "StatusMessage": NotRequired[str],
    },
)

DatasetSourceTypeDef = TypedDict(
    "DatasetSourceTypeDef",
    {
        "GroundTruthManifest": NotRequired["DatasetGroundTruthManifestTypeDef"],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "ClientToken": NotRequired[str],
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "ClientToken": NotRequired[str],
    },
)

DeleteModelResponseTypeDef = TypedDict(
    "DeleteModelResponseTypeDef",
    {
        "ModelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ClientToken": NotRequired[str],
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "ProjectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetDescription": "DatasetDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelPackagingJobRequestRequestTypeDef = TypedDict(
    "DescribeModelPackagingJobRequestRequestTypeDef",
    {
        "ProjectName": str,
        "JobName": str,
    },
)

DescribeModelPackagingJobResponseTypeDef = TypedDict(
    "DescribeModelPackagingJobResponseTypeDef",
    {
        "ModelPackagingDescription": "ModelPackagingDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeModelRequestRequestTypeDef = TypedDict(
    "DescribeModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
    },
)

DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef",
    {
        "ModelDescription": "ModelDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "ProjectName": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "ProjectDescription": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomaliesRequestRequestTypeDef = TypedDict(
    "DetectAnomaliesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "ContentType": str,
    },
)

DetectAnomaliesResponseTypeDef = TypedDict(
    "DetectAnomaliesResponseTypeDef",
    {
        "DetectAnomalyResult": "DetectAnomalyResultTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetectAnomalyResultTypeDef = TypedDict(
    "DetectAnomalyResultTypeDef",
    {
        "Source": NotRequired["ImageSourceTypeDef"],
        "IsAnomalous": NotRequired[bool],
        "Confidence": NotRequired[float],
    },
)

GreengrassConfigurationTypeDef = TypedDict(
    "GreengrassConfigurationTypeDef",
    {
        "S3OutputLocation": "S3LocationTypeDef",
        "ComponentName": str,
        "CompilerOptions": NotRequired[str],
        "TargetDevice": NotRequired[Literal["jetson_xavier"]],
        "TargetPlatform": NotRequired["TargetPlatformTypeDef"],
        "ComponentVersion": NotRequired[str],
        "ComponentDescription": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

GreengrassOutputDetailsTypeDef = TypedDict(
    "GreengrassOutputDetailsTypeDef",
    {
        "ComponentVersionArn": NotRequired[str],
        "ComponentName": NotRequired[str],
        "ComponentVersion": NotRequired[str],
    },
)

ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "Type": NotRequired[str],
    },
)

InputS3ObjectTypeDef = TypedDict(
    "InputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
        "VersionId": NotRequired[str],
    },
)

ListDatasetEntriesRequestRequestTypeDef = TypedDict(
    "ListDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Labeled": NotRequired[bool],
        "AnomalyClass": NotRequired[str],
        "BeforeCreationDate": NotRequired[Union[datetime, str]],
        "AfterCreationDate": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "SourceRefContains": NotRequired[str],
    },
)

ListDatasetEntriesResponseTypeDef = TypedDict(
    "ListDatasetEntriesResponseTypeDef",
    {
        "DatasetEntries": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelPackagingJobsRequestRequestTypeDef = TypedDict(
    "ListModelPackagingJobsRequestRequestTypeDef",
    {
        "ProjectName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListModelPackagingJobsResponseTypeDef = TypedDict(
    "ListModelPackagingJobsResponseTypeDef",
    {
        "ModelPackagingJobs": List["ModelPackagingJobMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListModelsRequestRequestTypeDef = TypedDict(
    "ListModelsRequestRequestTypeDef",
    {
        "ProjectName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {
        "Models": List["ModelMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List["ProjectMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModelDescriptionTypeDef = TypedDict(
    "ModelDescriptionTypeDef",
    {
        "ModelVersion": NotRequired[str],
        "ModelArn": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Description": NotRequired[str],
        "Status": NotRequired[ModelStatusType],
        "StatusMessage": NotRequired[str],
        "Performance": NotRequired["ModelPerformanceTypeDef"],
        "OutputConfig": NotRequired["OutputConfigTypeDef"],
        "EvaluationManifest": NotRequired["OutputS3ObjectTypeDef"],
        "EvaluationResult": NotRequired["OutputS3ObjectTypeDef"],
        "EvaluationEndTimestamp": NotRequired[datetime],
        "KmsKeyId": NotRequired[str],
    },
)

ModelMetadataTypeDef = TypedDict(
    "ModelMetadataTypeDef",
    {
        "CreationTimestamp": NotRequired[datetime],
        "ModelVersion": NotRequired[str],
        "ModelArn": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[ModelStatusType],
        "StatusMessage": NotRequired[str],
        "Performance": NotRequired["ModelPerformanceTypeDef"],
    },
)

ModelPackagingConfigurationTypeDef = TypedDict(
    "ModelPackagingConfigurationTypeDef",
    {
        "Greengrass": "GreengrassConfigurationTypeDef",
    },
)

ModelPackagingDescriptionTypeDef = TypedDict(
    "ModelPackagingDescriptionTypeDef",
    {
        "JobName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "ModelPackagingConfiguration": NotRequired["ModelPackagingConfigurationTypeDef"],
        "ModelPackagingJobDescription": NotRequired[str],
        "ModelPackagingMethod": NotRequired[str],
        "ModelPackagingOutputDetails": NotRequired["ModelPackagingOutputDetailsTypeDef"],
        "Status": NotRequired[ModelPackagingJobStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ModelPackagingJobMetadataTypeDef = TypedDict(
    "ModelPackagingJobMetadataTypeDef",
    {
        "JobName": NotRequired[str],
        "ProjectName": NotRequired[str],
        "ModelVersion": NotRequired[str],
        "ModelPackagingJobDescription": NotRequired[str],
        "ModelPackagingMethod": NotRequired[str],
        "Status": NotRequired[ModelPackagingJobStatusType],
        "StatusMessage": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ModelPackagingOutputDetailsTypeDef = TypedDict(
    "ModelPackagingOutputDetailsTypeDef",
    {
        "Greengrass": NotRequired["GreengrassOutputDetailsTypeDef"],
    },
)

ModelPerformanceTypeDef = TypedDict(
    "ModelPerformanceTypeDef",
    {
        "F1Score": NotRequired[float],
        "Recall": NotRequired[float],
        "Precision": NotRequired[float],
    },
)

OutputConfigTypeDef = TypedDict(
    "OutputConfigTypeDef",
    {
        "S3Location": "S3LocationTypeDef",
    },
)

OutputS3ObjectTypeDef = TypedDict(
    "OutputS3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
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

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "ProjectName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "Datasets": NotRequired[List["DatasetMetadataTypeDef"]],
    },
)

ProjectMetadataTypeDef = TypedDict(
    "ProjectMetadataTypeDef",
    {
        "ProjectArn": NotRequired[str],
        "ProjectName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Prefix": NotRequired[str],
    },
)

StartModelPackagingJobRequestRequestTypeDef = TypedDict(
    "StartModelPackagingJobRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "Configuration": "ModelPackagingConfigurationTypeDef",
        "JobName": NotRequired[str],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

StartModelPackagingJobResponseTypeDef = TypedDict(
    "StartModelPackagingJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartModelRequestRequestTypeDef = TypedDict(
    "StartModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "MinInferenceUnits": int,
        "ClientToken": NotRequired[str],
    },
)

StartModelResponseTypeDef = TypedDict(
    "StartModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopModelRequestRequestTypeDef = TypedDict(
    "StopModelRequestRequestTypeDef",
    {
        "ProjectName": str,
        "ModelVersion": str,
        "ClientToken": NotRequired[str],
    },
)

StopModelResponseTypeDef = TypedDict(
    "StopModelResponseTypeDef",
    {
        "Status": ModelHostingStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetPlatformTypeDef = TypedDict(
    "TargetPlatformTypeDef",
    {
        "Os": Literal["LINUX"],
        "Arch": TargetPlatformArchType,
        "Accelerator": Literal["NVIDIA"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDatasetEntriesRequestRequestTypeDef = TypedDict(
    "UpdateDatasetEntriesRequestRequestTypeDef",
    {
        "ProjectName": str,
        "DatasetType": str,
        "Changes": Union[bytes, IO[bytes], StreamingBody],
        "ClientToken": NotRequired[str],
    },
)

UpdateDatasetEntriesResponseTypeDef = TypedDict(
    "UpdateDatasetEntriesResponseTypeDef",
    {
        "Status": DatasetStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
