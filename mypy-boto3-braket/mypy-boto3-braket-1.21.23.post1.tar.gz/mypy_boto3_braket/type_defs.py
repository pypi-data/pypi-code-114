"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs.html)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import AlgorithmSpecificationTypeDef

    data: AlgorithmSpecificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    CancellationStatusType,
    CompressionTypeType,
    DeviceStatusType,
    DeviceTypeType,
    InstanceTypeType,
    JobEventTypeType,
    JobPrimaryStatusType,
    QuantumTaskStatusType,
    SearchJobsFilterOperatorType,
    SearchQuantumTasksFilterOperatorType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlgorithmSpecificationTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CancelJobResponseTypeDef",
    "CancelQuantumTaskRequestRequestTypeDef",
    "CancelQuantumTaskResponseTypeDef",
    "ContainerImageTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateQuantumTaskRequestRequestTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "DataSourceTypeDef",
    "DeviceConfigTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetQuantumTaskRequestRequestTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "InputFileConfigTypeDef",
    "InstanceConfigTypeDef",
    "JobCheckpointConfigTypeDef",
    "JobEventDetailsTypeDef",
    "JobOutputDataConfigTypeDef",
    "JobStoppingConditionTypeDef",
    "JobSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceTypeDef",
    "ScriptModeConfigTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesRequestRequestTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchJobsFilterTypeDef",
    "SearchJobsRequestRequestTypeDef",
    "SearchJobsResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksRequestRequestTypeDef",
    "SearchQuantumTasksResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
)

AlgorithmSpecificationTypeDef = TypedDict(
    "AlgorithmSpecificationTypeDef",
    {
        "containerImage": NotRequired["ContainerImageTypeDef"],
        "scriptModeConfig": NotRequired["ScriptModeConfigTypeDef"],
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "jobArn": str,
    },
)

CancelJobResponseTypeDef = TypedDict(
    "CancelJobResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelQuantumTaskRequestRequestTypeDef = TypedDict(
    "CancelQuantumTaskRequestRequestTypeDef",
    {
        "clientToken": str,
        "quantumTaskArn": str,
    },
)

CancelQuantumTaskResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseTypeDef",
    {
        "cancellationStatus": CancellationStatusType,
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef",
    {
        "uri": str,
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "algorithmSpecification": "AlgorithmSpecificationTypeDef",
        "clientToken": str,
        "deviceConfig": "DeviceConfigTypeDef",
        "instanceConfig": "InstanceConfigTypeDef",
        "jobName": str,
        "outputDataConfig": "JobOutputDataConfigTypeDef",
        "roleArn": str,
        "checkpointConfig": NotRequired["JobCheckpointConfigTypeDef"],
        "hyperParameters": NotRequired[Mapping[str, str]],
        "inputDataConfig": NotRequired[Sequence["InputFileConfigTypeDef"]],
        "stoppingCondition": NotRequired["JobStoppingConditionTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "jobArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQuantumTaskRequestRequestTypeDef = TypedDict(
    "CreateQuantumTaskRequestRequestTypeDef",
    {
        "action": str,
        "clientToken": str,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3KeyPrefix": str,
        "shots": int,
        "deviceParameters": NotRequired[str],
        "jobToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateQuantumTaskResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseTypeDef",
    {
        "quantumTaskArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef",
    {
        "s3DataSource": "S3DataSourceTypeDef",
    },
)

DeviceConfigTypeDef = TypedDict(
    "DeviceConfigTypeDef",
    {
        "device": str,
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "deviceArn": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "deviceArn": str,
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatusType,
        "deviceType": DeviceTypeType,
        "providerName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "jobArn": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "algorithmSpecification": "AlgorithmSpecificationTypeDef",
        "billableDuration": int,
        "checkpointConfig": "JobCheckpointConfigTypeDef",
        "createdAt": datetime,
        "deviceConfig": "DeviceConfigTypeDef",
        "endedAt": datetime,
        "events": List["JobEventDetailsTypeDef"],
        "failureReason": str,
        "hyperParameters": Dict[str, str],
        "inputDataConfig": List["InputFileConfigTypeDef"],
        "instanceConfig": "InstanceConfigTypeDef",
        "jobArn": str,
        "jobName": str,
        "outputDataConfig": "JobOutputDataConfigTypeDef",
        "roleArn": str,
        "startedAt": datetime,
        "status": JobPrimaryStatusType,
        "stoppingCondition": "JobStoppingConditionTypeDef",
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQuantumTaskRequestRequestTypeDef = TypedDict(
    "GetQuantumTaskRequestRequestTypeDef",
    {
        "quantumTaskArn": str,
    },
)

GetQuantumTaskResponseTypeDef = TypedDict(
    "GetQuantumTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "endedAt": datetime,
        "failureReason": str,
        "jobArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputFileConfigTypeDef = TypedDict(
    "InputFileConfigTypeDef",
    {
        "channelName": str,
        "dataSource": "DataSourceTypeDef",
        "contentType": NotRequired[str],
    },
)

InstanceConfigTypeDef = TypedDict(
    "InstanceConfigTypeDef",
    {
        "instanceType": InstanceTypeType,
        "volumeSizeInGb": int,
    },
)

JobCheckpointConfigTypeDef = TypedDict(
    "JobCheckpointConfigTypeDef",
    {
        "s3Uri": str,
        "localPath": NotRequired[str],
    },
)

JobEventDetailsTypeDef = TypedDict(
    "JobEventDetailsTypeDef",
    {
        "eventType": NotRequired[JobEventTypeType],
        "message": NotRequired[str],
        "timeOfEvent": NotRequired[datetime],
    },
)

JobOutputDataConfigTypeDef = TypedDict(
    "JobOutputDataConfigTypeDef",
    {
        "s3Path": str,
        "kmsKeyId": NotRequired[str],
    },
)

JobStoppingConditionTypeDef = TypedDict(
    "JobStoppingConditionTypeDef",
    {
        "maxRuntimeInSeconds": NotRequired[int],
    },
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "createdAt": datetime,
        "device": str,
        "jobArn": str,
        "jobName": str,
        "status": JobPrimaryStatusType,
        "endedAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

QuantumTaskSummaryTypeDef = TypedDict(
    "QuantumTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatusType,
        "endedAt": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
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

S3DataSourceTypeDef = TypedDict(
    "S3DataSourceTypeDef",
    {
        "s3Uri": str,
    },
)

ScriptModeConfigTypeDef = TypedDict(
    "ScriptModeConfigTypeDef",
    {
        "entryPoint": str,
        "s3Uri": str,
        "compressionType": NotRequired[CompressionTypeType],
    },
)

SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef",
    {
        "name": str,
        "values": Sequence[str],
    },
)

SearchDevicesRequestRequestTypeDef = TypedDict(
    "SearchDevicesRequestRequestTypeDef",
    {
        "filters": Sequence["SearchDevicesFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {
        "devices": List["DeviceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchJobsFilterTypeDef = TypedDict(
    "SearchJobsFilterTypeDef",
    {
        "name": str,
        "operator": SearchJobsFilterOperatorType,
        "values": Sequence[str],
    },
)

SearchJobsRequestRequestTypeDef = TypedDict(
    "SearchJobsRequestRequestTypeDef",
    {
        "filters": Sequence["SearchJobsFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

SearchJobsResponseTypeDef = TypedDict(
    "SearchJobsResponseTypeDef",
    {
        "jobs": List["JobSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {
        "name": str,
        "operator": SearchQuantumTasksFilterOperatorType,
        "values": Sequence[str],
    },
)

SearchQuantumTasksRequestRequestTypeDef = TypedDict(
    "SearchQuantumTasksRequestRequestTypeDef",
    {
        "filters": Sequence["SearchQuantumTasksFilterTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

SearchQuantumTasksResponseTypeDef = TypedDict(
    "SearchQuantumTasksResponseTypeDef",
    {
        "nextToken": str,
        "quantumTasks": List["QuantumTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
