"""
Type annotations for synthetics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import ArtifactConfigInputTypeDef

    data: ArtifactConfigInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    CanaryRunStateReasonCodeType,
    CanaryRunStateType,
    CanaryStateType,
    EncryptionModeType,
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
    "ArtifactConfigInputTypeDef",
    "ArtifactConfigOutputTypeDef",
    "BaseScreenshotTypeDef",
    "CanaryCodeInputTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "CreateCanaryRequestRequestTypeDef",
    "CreateCanaryResponseTypeDef",
    "DeleteCanaryRequestRequestTypeDef",
    "DescribeCanariesLastRunRequestRequestTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesRequestRequestTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "GetCanaryRequestRequestTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsRequestRequestTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeVersionTypeDef",
    "S3EncryptionConfigTypeDef",
    "StartCanaryRequestRequestTypeDef",
    "StopCanaryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateCanaryRequestRequestTypeDef",
    "VisualReferenceInputTypeDef",
    "VisualReferenceOutputTypeDef",
    "VpcConfigInputTypeDef",
    "VpcConfigOutputTypeDef",
)

ArtifactConfigInputTypeDef = TypedDict(
    "ArtifactConfigInputTypeDef",
    {
        "S3Encryption": NotRequired["S3EncryptionConfigTypeDef"],
    },
)

ArtifactConfigOutputTypeDef = TypedDict(
    "ArtifactConfigOutputTypeDef",
    {
        "S3Encryption": NotRequired["S3EncryptionConfigTypeDef"],
    },
)

BaseScreenshotTypeDef = TypedDict(
    "BaseScreenshotTypeDef",
    {
        "ScreenshotName": str,
        "IgnoreCoordinates": NotRequired[List[str]],
    },
)

CanaryCodeInputTypeDef = TypedDict(
    "CanaryCodeInputTypeDef",
    {
        "Handler": str,
        "S3Bucket": NotRequired[str],
        "S3Key": NotRequired[str],
        "S3Version": NotRequired[str],
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

CanaryCodeOutputTypeDef = TypedDict(
    "CanaryCodeOutputTypeDef",
    {
        "SourceLocationArn": NotRequired[str],
        "Handler": NotRequired[str],
    },
)

CanaryLastRunTypeDef = TypedDict(
    "CanaryLastRunTypeDef",
    {
        "CanaryName": NotRequired[str],
        "LastRun": NotRequired["CanaryRunTypeDef"],
    },
)

CanaryRunConfigInputTypeDef = TypedDict(
    "CanaryRunConfigInputTypeDef",
    {
        "TimeoutInSeconds": NotRequired[int],
        "MemoryInMB": NotRequired[int],
        "ActiveTracing": NotRequired[bool],
        "EnvironmentVariables": NotRequired[Mapping[str, str]],
    },
)

CanaryRunConfigOutputTypeDef = TypedDict(
    "CanaryRunConfigOutputTypeDef",
    {
        "TimeoutInSeconds": NotRequired[int],
        "MemoryInMB": NotRequired[int],
        "ActiveTracing": NotRequired[bool],
    },
)

CanaryRunStatusTypeDef = TypedDict(
    "CanaryRunStatusTypeDef",
    {
        "State": NotRequired[CanaryRunStateType],
        "StateReason": NotRequired[str],
        "StateReasonCode": NotRequired[CanaryRunStateReasonCodeType],
    },
)

CanaryRunTimelineTypeDef = TypedDict(
    "CanaryRunTimelineTypeDef",
    {
        "Started": NotRequired[datetime],
        "Completed": NotRequired[datetime],
    },
)

CanaryRunTypeDef = TypedDict(
    "CanaryRunTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired["CanaryRunStatusTypeDef"],
        "Timeline": NotRequired["CanaryRunTimelineTypeDef"],
        "ArtifactS3Location": NotRequired[str],
    },
)

CanaryScheduleInputTypeDef = TypedDict(
    "CanaryScheduleInputTypeDef",
    {
        "Expression": str,
        "DurationInSeconds": NotRequired[int],
    },
)

CanaryScheduleOutputTypeDef = TypedDict(
    "CanaryScheduleOutputTypeDef",
    {
        "Expression": NotRequired[str],
        "DurationInSeconds": NotRequired[int],
    },
)

CanaryStatusTypeDef = TypedDict(
    "CanaryStatusTypeDef",
    {
        "State": NotRequired[CanaryStateType],
        "StateReason": NotRequired[str],
        "StateReasonCode": NotRequired[Literal["INVALID_PERMISSIONS"]],
    },
)

CanaryTimelineTypeDef = TypedDict(
    "CanaryTimelineTypeDef",
    {
        "Created": NotRequired[datetime],
        "LastModified": NotRequired[datetime],
        "LastStarted": NotRequired[datetime],
        "LastStopped": NotRequired[datetime],
    },
)

CanaryTypeDef = TypedDict(
    "CanaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Code": NotRequired["CanaryCodeOutputTypeDef"],
        "ExecutionRoleArn": NotRequired[str],
        "Schedule": NotRequired["CanaryScheduleOutputTypeDef"],
        "RunConfig": NotRequired["CanaryRunConfigOutputTypeDef"],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "Status": NotRequired["CanaryStatusTypeDef"],
        "Timeline": NotRequired["CanaryTimelineTypeDef"],
        "ArtifactS3Location": NotRequired[str],
        "EngineArn": NotRequired[str],
        "RuntimeVersion": NotRequired[str],
        "VpcConfig": NotRequired["VpcConfigOutputTypeDef"],
        "VisualReference": NotRequired["VisualReferenceOutputTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "ArtifactConfig": NotRequired["ArtifactConfigOutputTypeDef"],
    },
)

CreateCanaryRequestRequestTypeDef = TypedDict(
    "CreateCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "Code": "CanaryCodeInputTypeDef",
        "ArtifactS3Location": str,
        "ExecutionRoleArn": str,
        "Schedule": "CanaryScheduleInputTypeDef",
        "RuntimeVersion": str,
        "RunConfig": NotRequired["CanaryRunConfigInputTypeDef"],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "VpcConfig": NotRequired["VpcConfigInputTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "ArtifactConfig": NotRequired["ArtifactConfigInputTypeDef"],
    },
)

CreateCanaryResponseTypeDef = TypedDict(
    "CreateCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCanaryRequestRequestTypeDef = TypedDict(
    "DeleteCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeCanariesLastRunRequestRequestTypeDef = TypedDict(
    "DescribeCanariesLastRunRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Names": NotRequired[Sequence[str]],
    },
)

DescribeCanariesLastRunResponseTypeDef = TypedDict(
    "DescribeCanariesLastRunResponseTypeDef",
    {
        "CanariesLastRun": List["CanaryLastRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCanariesRequestRequestTypeDef = TypedDict(
    "DescribeCanariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Names": NotRequired[Sequence[str]],
    },
)

DescribeCanariesResponseTypeDef = TypedDict(
    "DescribeCanariesResponseTypeDef",
    {
        "Canaries": List["CanaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeVersionsRequestRequestTypeDef = TypedDict(
    "DescribeRuntimeVersionsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeRuntimeVersionsResponseTypeDef = TypedDict(
    "DescribeRuntimeVersionsResponseTypeDef",
    {
        "RuntimeVersions": List["RuntimeVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCanaryRequestRequestTypeDef = TypedDict(
    "GetCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetCanaryResponseTypeDef = TypedDict(
    "GetCanaryResponseTypeDef",
    {
        "Canary": "CanaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCanaryRunsRequestRequestTypeDef = TypedDict(
    "GetCanaryRunsRequestRequestTypeDef",
    {
        "Name": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetCanaryRunsResponseTypeDef = TypedDict(
    "GetCanaryRunsResponseTypeDef",
    {
        "CanaryRuns": List["CanaryRunTypeDef"],
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
        "Tags": Dict[str, str],
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

RuntimeVersionTypeDef = TypedDict(
    "RuntimeVersionTypeDef",
    {
        "VersionName": NotRequired[str],
        "Description": NotRequired[str],
        "ReleaseDate": NotRequired[datetime],
        "DeprecationDate": NotRequired[datetime],
    },
)

S3EncryptionConfigTypeDef = TypedDict(
    "S3EncryptionConfigTypeDef",
    {
        "EncryptionMode": NotRequired[EncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)

StartCanaryRequestRequestTypeDef = TypedDict(
    "StartCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopCanaryRequestRequestTypeDef = TypedDict(
    "StopCanaryRequestRequestTypeDef",
    {
        "Name": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateCanaryRequestRequestTypeDef = TypedDict(
    "UpdateCanaryRequestRequestTypeDef",
    {
        "Name": str,
        "Code": NotRequired["CanaryCodeInputTypeDef"],
        "ExecutionRoleArn": NotRequired[str],
        "RuntimeVersion": NotRequired[str],
        "Schedule": NotRequired["CanaryScheduleInputTypeDef"],
        "RunConfig": NotRequired["CanaryRunConfigInputTypeDef"],
        "SuccessRetentionPeriodInDays": NotRequired[int],
        "FailureRetentionPeriodInDays": NotRequired[int],
        "VpcConfig": NotRequired["VpcConfigInputTypeDef"],
        "VisualReference": NotRequired["VisualReferenceInputTypeDef"],
        "ArtifactS3Location": NotRequired[str],
        "ArtifactConfig": NotRequired["ArtifactConfigInputTypeDef"],
    },
)

VisualReferenceInputTypeDef = TypedDict(
    "VisualReferenceInputTypeDef",
    {
        "BaseCanaryRunId": str,
        "BaseScreenshots": NotRequired[Sequence["BaseScreenshotTypeDef"]],
    },
)

VisualReferenceOutputTypeDef = TypedDict(
    "VisualReferenceOutputTypeDef",
    {
        "BaseScreenshots": NotRequired[List["BaseScreenshotTypeDef"]],
        "BaseCanaryRunId": NotRequired[str],
    },
)

VpcConfigInputTypeDef = TypedDict(
    "VpcConfigInputTypeDef",
    {
        "SubnetIds": NotRequired[Sequence[str]],
        "SecurityGroupIds": NotRequired[Sequence[str]],
    },
)

VpcConfigOutputTypeDef = TypedDict(
    "VpcConfigOutputTypeDef",
    {
        "VpcId": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "SecurityGroupIds": NotRequired[List[str]],
    },
)
