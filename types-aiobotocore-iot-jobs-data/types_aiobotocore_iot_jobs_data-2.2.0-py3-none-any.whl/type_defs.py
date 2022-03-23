"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iot_jobs_data/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iot_jobs_data.type_defs import DescribeJobExecutionRequestRequestTypeDef

    data: DescribeJobExecutionRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping

from typing_extensions import NotRequired

from .literals import JobExecutionStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeJobExecutionRequestRequestTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsRequestRequestTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "StartNextPendingJobExecutionRequestRequestTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionRequestRequestTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)

DescribeJobExecutionRequestRequestTypeDef = TypedDict(
    "DescribeJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "includeJobDocument": NotRequired[bool],
        "executionNumber": NotRequired[int],
    },
)

DescribeJobExecutionResponseTypeDef = TypedDict(
    "DescribeJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPendingJobExecutionsRequestRequestTypeDef = TypedDict(
    "GetPendingJobExecutionsRequestRequestTypeDef",
    {
        "thingName": str,
    },
)

GetPendingJobExecutionsResponseTypeDef = TypedDict(
    "GetPendingJobExecutionsResponseTypeDef",
    {
        "inProgressJobs": List["JobExecutionSummaryTypeDef"],
        "queuedJobs": List["JobExecutionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

JobExecutionStateTypeDef = TypedDict(
    "JobExecutionStateTypeDef",
    {
        "status": NotRequired[JobExecutionStatusType],
        "statusDetails": NotRequired[Dict[str, str]],
        "versionNumber": NotRequired[int],
    },
)

JobExecutionSummaryTypeDef = TypedDict(
    "JobExecutionSummaryTypeDef",
    {
        "jobId": NotRequired[str],
        "queuedAt": NotRequired[int],
        "startedAt": NotRequired[int],
        "lastUpdatedAt": NotRequired[int],
        "versionNumber": NotRequired[int],
        "executionNumber": NotRequired[int],
    },
)

JobExecutionTypeDef = TypedDict(
    "JobExecutionTypeDef",
    {
        "jobId": NotRequired[str],
        "thingName": NotRequired[str],
        "status": NotRequired[JobExecutionStatusType],
        "statusDetails": NotRequired[Dict[str, str]],
        "queuedAt": NotRequired[int],
        "startedAt": NotRequired[int],
        "lastUpdatedAt": NotRequired[int],
        "approximateSecondsBeforeTimedOut": NotRequired[int],
        "versionNumber": NotRequired[int],
        "executionNumber": NotRequired[int],
        "jobDocument": NotRequired[str],
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

StartNextPendingJobExecutionRequestRequestTypeDef = TypedDict(
    "StartNextPendingJobExecutionRequestRequestTypeDef",
    {
        "thingName": str,
        "statusDetails": NotRequired[Mapping[str, str]],
        "stepTimeoutInMinutes": NotRequired[int],
    },
)

StartNextPendingJobExecutionResponseTypeDef = TypedDict(
    "StartNextPendingJobExecutionResponseTypeDef",
    {
        "execution": "JobExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJobExecutionRequestRequestTypeDef = TypedDict(
    "UpdateJobExecutionRequestRequestTypeDef",
    {
        "jobId": str,
        "thingName": str,
        "status": JobExecutionStatusType,
        "statusDetails": NotRequired[Mapping[str, str]],
        "stepTimeoutInMinutes": NotRequired[int],
        "expectedVersion": NotRequired[int],
        "includeJobExecutionState": NotRequired[bool],
        "includeJobDocument": NotRequired[bool],
        "executionNumber": NotRequired[int],
    },
)

UpdateJobExecutionResponseTypeDef = TypedDict(
    "UpdateJobExecutionResponseTypeDef",
    {
        "executionState": "JobExecutionStateTypeDef",
        "jobDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
