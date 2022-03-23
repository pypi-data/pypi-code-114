"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionRequestRequestTypeDef

    data: CreateSuiteDefinitionRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import StatusType, SuiteRunStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSuiteDefinitionRequestRequestTypeDef",
    "CreateSuiteDefinitionResponseTypeDef",
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    "DeviceUnderTestTypeDef",
    "GetEndpointRequestRequestTypeDef",
    "GetEndpointResponseTypeDef",
    "GetSuiteDefinitionRequestRequestTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "GetSuiteRunReportRequestRequestTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "GetSuiteRunRequestRequestTypeDef",
    "GetSuiteRunResponseTypeDef",
    "GroupResultTypeDef",
    "ListSuiteDefinitionsRequestRequestTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "ListSuiteRunsRequestRequestTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSuiteRunRequestRequestTypeDef",
    "StartSuiteRunResponseTypeDef",
    "StopSuiteRunRequestRequestTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestCaseRunTypeDef",
    "TestResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)

CreateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "CreateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionConfiguration": NotRequired["SuiteDefinitionConfigurationTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateSuiteDefinitionResponseTypeDef = TypedDict(
    "CreateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
    },
)

DeviceUnderTestTypeDef = TypedDict(
    "DeviceUnderTestTypeDef",
    {
        "thingArn": NotRequired[str],
        "certificateArn": NotRequired[str],
    },
)

GetEndpointRequestRequestTypeDef = TypedDict(
    "GetEndpointRequestRequestTypeDef",
    {
        "thingArn": NotRequired[str],
        "certificateArn": NotRequired[str],
    },
)

GetEndpointResponseTypeDef = TypedDict(
    "GetEndpointResponseTypeDef",
    {
        "endpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "GetSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": NotRequired[str],
    },
)

GetSuiteDefinitionResponseTypeDef = TypedDict(
    "GetSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionVersion": str,
        "latestVersion": str,
        "suiteDefinitionConfiguration": "SuiteDefinitionConfigurationTypeDef",
        "createdAt": datetime,
        "lastModifiedAt": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunReportRequestRequestTypeDef = TypedDict(
    "GetSuiteRunReportRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunReportResponseTypeDef = TypedDict(
    "GetSuiteRunReportResponseTypeDef",
    {
        "qualificationReportDownloadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSuiteRunRequestRequestTypeDef = TypedDict(
    "GetSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

GetSuiteRunResponseTypeDef = TypedDict(
    "GetSuiteRunResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": str,
        "suiteRunId": str,
        "suiteRunArn": str,
        "suiteRunConfiguration": "SuiteRunConfigurationTypeDef",
        "testResult": "TestResultTypeDef",
        "startTime": datetime,
        "endTime": datetime,
        "status": SuiteRunStatusType,
        "errorReason": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupResultTypeDef = TypedDict(
    "GroupResultTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
        "tests": NotRequired[List["TestCaseRunTypeDef"]],
    },
)

ListSuiteDefinitionsRequestRequestTypeDef = TypedDict(
    "ListSuiteDefinitionsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSuiteDefinitionsResponseTypeDef = TypedDict(
    "ListSuiteDefinitionsResponseTypeDef",
    {
        "suiteDefinitionInformationList": List["SuiteDefinitionInformationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSuiteRunsRequestRequestTypeDef = TypedDict(
    "ListSuiteRunsRequestRequestTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionVersion": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListSuiteRunsResponseTypeDef = TypedDict(
    "ListSuiteRunsResponseTypeDef",
    {
        "suiteRunsList": List["SuiteRunInformationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

StartSuiteRunRequestRequestTypeDef = TypedDict(
    "StartSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionVersion": NotRequired[str],
        "suiteRunConfiguration": NotRequired["SuiteRunConfigurationTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

StartSuiteRunResponseTypeDef = TypedDict(
    "StartSuiteRunResponseTypeDef",
    {
        "suiteRunId": str,
        "suiteRunArn": str,
        "createdAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopSuiteRunRequestRequestTypeDef = TypedDict(
    "StopSuiteRunRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteRunId": str,
    },
)

SuiteDefinitionConfigurationTypeDef = TypedDict(
    "SuiteDefinitionConfigurationTypeDef",
    {
        "suiteDefinitionName": NotRequired[str],
        "devices": NotRequired[Sequence["DeviceUnderTestTypeDef"]],
        "intendedForQualification": NotRequired[bool],
        "rootGroup": NotRequired[str],
        "devicePermissionRoleArn": NotRequired[str],
    },
)

SuiteDefinitionInformationTypeDef = TypedDict(
    "SuiteDefinitionInformationTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionName": NotRequired[str],
        "defaultDevices": NotRequired[List["DeviceUnderTestTypeDef"]],
        "intendedForQualification": NotRequired[bool],
        "createdAt": NotRequired[datetime],
    },
)

SuiteRunConfigurationTypeDef = TypedDict(
    "SuiteRunConfigurationTypeDef",
    {
        "primaryDevice": NotRequired["DeviceUnderTestTypeDef"],
        "selectedTestList": NotRequired[List[str]],
        "parallelRun": NotRequired[bool],
    },
)

SuiteRunInformationTypeDef = TypedDict(
    "SuiteRunInformationTypeDef",
    {
        "suiteDefinitionId": NotRequired[str],
        "suiteDefinitionVersion": NotRequired[str],
        "suiteDefinitionName": NotRequired[str],
        "suiteRunId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "startedAt": NotRequired[datetime],
        "endAt": NotRequired[datetime],
        "status": NotRequired[SuiteRunStatusType],
        "passed": NotRequired[int],
        "failed": NotRequired[int],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TestCaseRunTypeDef = TypedDict(
    "TestCaseRunTypeDef",
    {
        "testCaseRunId": NotRequired[str],
        "testCaseDefinitionId": NotRequired[str],
        "testCaseDefinitionName": NotRequired[str],
        "status": NotRequired[StatusType],
        "startTime": NotRequired[datetime],
        "endTime": NotRequired[datetime],
        "logUrl": NotRequired[str],
        "warnings": NotRequired[str],
        "failure": NotRequired[str],
    },
)

TestResultTypeDef = TypedDict(
    "TestResultTypeDef",
    {
        "groups": NotRequired[List["GroupResultTypeDef"]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateSuiteDefinitionRequestRequestTypeDef = TypedDict(
    "UpdateSuiteDefinitionRequestRequestTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionConfiguration": NotRequired["SuiteDefinitionConfigurationTypeDef"],
    },
)

UpdateSuiteDefinitionResponseTypeDef = TypedDict(
    "UpdateSuiteDefinitionResponseTypeDef",
    {
        "suiteDefinitionId": str,
        "suiteDefinitionArn": str,
        "suiteDefinitionName": str,
        "suiteDefinitionVersion": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
