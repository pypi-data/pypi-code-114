"""
Type annotations for codeguruprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.type_defs import AddNotificationChannelsRequestRequestTypeDef

    data: AddNotificationChannelsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AgentParameterFieldType,
    AggregationPeriodType,
    ComputePlatformType,
    FeedbackTypeType,
    MetadataFieldType,
    OrderByType,
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
    "AddNotificationChannelsRequestRequestTypeDef",
    "AddNotificationChannelsResponseTypeDef",
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "AnomalyInstanceTypeDef",
    "AnomalyTypeDef",
    "BatchGetFrameMetricDataRequestRequestTypeDef",
    "BatchGetFrameMetricDataResponseTypeDef",
    "ChannelTypeDef",
    "ConfigureAgentRequestRequestTypeDef",
    "ConfigureAgentResponseTypeDef",
    "CreateProfilingGroupRequestRequestTypeDef",
    "CreateProfilingGroupResponseTypeDef",
    "DeleteProfilingGroupRequestRequestTypeDef",
    "DescribeProfilingGroupRequestRequestTypeDef",
    "DescribeProfilingGroupResponseTypeDef",
    "FindingsReportSummaryTypeDef",
    "FrameMetricDatumTypeDef",
    "FrameMetricTypeDef",
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    "GetFindingsReportAccountSummaryResponseTypeDef",
    "GetNotificationConfigurationRequestRequestTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "ListFindingsReportsRequestRequestTypeDef",
    "ListFindingsReportsResponseTypeDef",
    "ListProfileTimesRequestRequestTypeDef",
    "ListProfileTimesResponseTypeDef",
    "ListProfilingGroupsRequestRequestTypeDef",
    "ListProfilingGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MatchTypeDef",
    "MetricTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PatternTypeDef",
    "PostAgentProfileRequestRequestTypeDef",
    "ProfileTimeTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "ProfilingStatusTypeDef",
    "PutPermissionRequestRequestTypeDef",
    "PutPermissionResponseTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "RemoveNotificationChannelResponseTypeDef",
    "RemovePermissionRequestRequestTypeDef",
    "RemovePermissionResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimestampStructureTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateProfilingGroupRequestRequestTypeDef",
    "UpdateProfilingGroupResponseTypeDef",
    "UserFeedbackTypeDef",
)

AddNotificationChannelsRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelsRequestRequestTypeDef",
    {
        "channels": Sequence["ChannelTypeDef"],
        "profilingGroupName": str,
    },
)

AddNotificationChannelsResponseTypeDef = TypedDict(
    "AddNotificationChannelsResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AgentConfigurationTypeDef = TypedDict(
    "AgentConfigurationTypeDef",
    {
        "periodInSeconds": int,
        "shouldProfile": bool,
        "agentParameters": NotRequired[Dict[AgentParameterFieldType, str]],
    },
)

AgentOrchestrationConfigTypeDef = TypedDict(
    "AgentOrchestrationConfigTypeDef",
    {
        "profilingEnabled": bool,
    },
)

AggregatedProfileTimeTypeDef = TypedDict(
    "AggregatedProfileTimeTypeDef",
    {
        "period": NotRequired[AggregationPeriodType],
        "start": NotRequired[datetime],
    },
)

AnomalyInstanceTypeDef = TypedDict(
    "AnomalyInstanceTypeDef",
    {
        "id": str,
        "startTime": datetime,
        "endTime": NotRequired[datetime],
        "userFeedback": NotRequired["UserFeedbackTypeDef"],
    },
)

AnomalyTypeDef = TypedDict(
    "AnomalyTypeDef",
    {
        "instances": List["AnomalyInstanceTypeDef"],
        "metric": "MetricTypeDef",
        "reason": str,
    },
)

BatchGetFrameMetricDataRequestRequestTypeDef = TypedDict(
    "BatchGetFrameMetricDataRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "endTime": NotRequired[Union[datetime, str]],
        "frameMetrics": NotRequired[Sequence["FrameMetricTypeDef"]],
        "period": NotRequired[str],
        "startTime": NotRequired[Union[datetime, str]],
        "targetResolution": NotRequired[AggregationPeriodType],
    },
)

BatchGetFrameMetricDataResponseTypeDef = TypedDict(
    "BatchGetFrameMetricDataResponseTypeDef",
    {
        "endTime": datetime,
        "endTimes": List["TimestampStructureTypeDef"],
        "frameMetricData": List["FrameMetricDatumTypeDef"],
        "resolution": AggregationPeriodType,
        "startTime": datetime,
        "unprocessedEndTimes": Dict[str, List["TimestampStructureTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "eventPublishers": Sequence[Literal["AnomalyDetection"]],
        "uri": str,
        "id": NotRequired[str],
    },
)

ConfigureAgentRequestRequestTypeDef = TypedDict(
    "ConfigureAgentRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "fleetInstanceId": NotRequired[str],
        "metadata": NotRequired[Mapping[MetadataFieldType, str]],
    },
)

ConfigureAgentResponseTypeDef = TypedDict(
    "ConfigureAgentResponseTypeDef",
    {
        "configuration": "AgentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProfilingGroupRequestRequestTypeDef = TypedDict(
    "CreateProfilingGroupRequestRequestTypeDef",
    {
        "clientToken": str,
        "profilingGroupName": str,
        "agentOrchestrationConfig": NotRequired["AgentOrchestrationConfigTypeDef"],
        "computePlatform": NotRequired[ComputePlatformType],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateProfilingGroupResponseTypeDef = TypedDict(
    "CreateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProfilingGroupRequestRequestTypeDef = TypedDict(
    "DeleteProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupRequestRequestTypeDef = TypedDict(
    "DescribeProfilingGroupRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

DescribeProfilingGroupResponseTypeDef = TypedDict(
    "DescribeProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FindingsReportSummaryTypeDef = TypedDict(
    "FindingsReportSummaryTypeDef",
    {
        "id": NotRequired[str],
        "profileEndTime": NotRequired[datetime],
        "profileStartTime": NotRequired[datetime],
        "profilingGroupName": NotRequired[str],
        "totalNumberOfFindings": NotRequired[int],
    },
)

FrameMetricDatumTypeDef = TypedDict(
    "FrameMetricDatumTypeDef",
    {
        "frameMetric": "FrameMetricTypeDef",
        "values": List[float],
    },
)

FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {
        "frameName": str,
        "threadStates": Sequence[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

GetFindingsReportAccountSummaryRequestRequestTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryRequestRequestTypeDef",
    {
        "dailyReportsOnly": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetFindingsReportAccountSummaryResponseTypeDef = TypedDict(
    "GetFindingsReportAccountSummaryResponseTypeDef",
    {
        "nextToken": str,
        "reportSummaries": List["FindingsReportSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNotificationConfigurationRequestRequestTypeDef = TypedDict(
    "GetNotificationConfigurationRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetNotificationConfigurationResponseTypeDef = TypedDict(
    "GetNotificationConfigurationResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "profilingGroupName": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "profilingGroupName": str,
        "accept": NotRequired[str],
        "endTime": NotRequired[Union[datetime, str]],
        "maxDepth": NotRequired[int],
        "period": NotRequired[str],
        "startTime": NotRequired[Union[datetime, str]],
    },
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "contentEncoding": str,
        "contentType": str,
        "profile": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
        "locale": NotRequired[str],
    },
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "anomalies": List["AnomalyTypeDef"],
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "recommendations": List["RecommendationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFindingsReportsRequestRequestTypeDef = TypedDict(
    "ListFindingsReportsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
        "dailyReportsOnly": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListFindingsReportsResponseTypeDef = TypedDict(
    "ListFindingsReportsResponseTypeDef",
    {
        "findingsReportSummaries": List["FindingsReportSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfileTimesRequestRequestTypeDef = TypedDict(
    "ListProfileTimesRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "period": AggregationPeriodType,
        "profilingGroupName": str,
        "startTime": Union[datetime, str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
    },
)

ListProfileTimesResponseTypeDef = TypedDict(
    "ListProfileTimesResponseTypeDef",
    {
        "nextToken": str,
        "profileTimes": List["ProfileTimeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProfilingGroupsRequestRequestTypeDef = TypedDict(
    "ListProfilingGroupsRequestRequestTypeDef",
    {
        "includeDescription": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListProfilingGroupsResponseTypeDef = TypedDict(
    "ListProfilingGroupsResponseTypeDef",
    {
        "nextToken": str,
        "profilingGroupNames": List[str],
        "profilingGroups": List["ProfilingGroupDescriptionTypeDef"],
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

MatchTypeDef = TypedDict(
    "MatchTypeDef",
    {
        "frameAddress": NotRequired[str],
        "targetFramesIndex": NotRequired[int],
        "thresholdBreachValue": NotRequired[float],
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "frameName": str,
        "threadStates": List[str],
        "type": Literal["AggregatedRelativeTotalTime"],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "channels": NotRequired[List["ChannelTypeDef"]],
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

PatternTypeDef = TypedDict(
    "PatternTypeDef",
    {
        "countersToAggregate": NotRequired[List[str]],
        "description": NotRequired[str],
        "id": NotRequired[str],
        "name": NotRequired[str],
        "resolutionSteps": NotRequired[str],
        "targetFrames": NotRequired[List[List[str]]],
        "thresholdPercent": NotRequired[float],
    },
)

PostAgentProfileRequestRequestTypeDef = TypedDict(
    "PostAgentProfileRequestRequestTypeDef",
    {
        "agentProfile": Union[bytes, IO[bytes], StreamingBody],
        "contentType": str,
        "profilingGroupName": str,
        "profileToken": NotRequired[str],
    },
)

ProfileTimeTypeDef = TypedDict(
    "ProfileTimeTypeDef",
    {
        "start": NotRequired[datetime],
    },
)

ProfilingGroupDescriptionTypeDef = TypedDict(
    "ProfilingGroupDescriptionTypeDef",
    {
        "agentOrchestrationConfig": NotRequired["AgentOrchestrationConfigTypeDef"],
        "arn": NotRequired[str],
        "computePlatform": NotRequired[ComputePlatformType],
        "createdAt": NotRequired[datetime],
        "name": NotRequired[str],
        "profilingStatus": NotRequired["ProfilingStatusTypeDef"],
        "tags": NotRequired[Dict[str, str]],
        "updatedAt": NotRequired[datetime],
    },
)

ProfilingStatusTypeDef = TypedDict(
    "ProfilingStatusTypeDef",
    {
        "latestAgentOrchestratedAt": NotRequired[datetime],
        "latestAgentProfileReportedAt": NotRequired[datetime],
        "latestAggregatedProfile": NotRequired["AggregatedProfileTimeTypeDef"],
    },
)

PutPermissionRequestRequestTypeDef = TypedDict(
    "PutPermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "principals": Sequence[str],
        "profilingGroupName": str,
        "revisionId": NotRequired[str],
    },
)

PutPermissionResponseTypeDef = TypedDict(
    "PutPermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "allMatchesCount": int,
        "allMatchesSum": float,
        "endTime": datetime,
        "pattern": "PatternTypeDef",
        "startTime": datetime,
        "topMatches": List["MatchTypeDef"],
    },
)

RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "channelId": str,
        "profilingGroupName": str,
    },
)

RemoveNotificationChannelResponseTypeDef = TypedDict(
    "RemoveNotificationChannelResponseTypeDef",
    {
        "notificationConfiguration": "NotificationConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemovePermissionRequestRequestTypeDef = TypedDict(
    "RemovePermissionRequestRequestTypeDef",
    {
        "actionGroup": Literal["agentPermissions"],
        "profilingGroupName": str,
        "revisionId": str,
    },
)

RemovePermissionResponseTypeDef = TypedDict(
    "RemovePermissionResponseTypeDef",
    {
        "policy": str,
        "revisionId": str,
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

SubmitFeedbackRequestRequestTypeDef = TypedDict(
    "SubmitFeedbackRequestRequestTypeDef",
    {
        "anomalyInstanceId": str,
        "profilingGroupName": str,
        "type": FeedbackTypeType,
        "comment": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TimestampStructureTypeDef = TypedDict(
    "TimestampStructureTypeDef",
    {
        "value": datetime,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateProfilingGroupRequestRequestTypeDef = TypedDict(
    "UpdateProfilingGroupRequestRequestTypeDef",
    {
        "agentOrchestrationConfig": "AgentOrchestrationConfigTypeDef",
        "profilingGroupName": str,
    },
)

UpdateProfilingGroupResponseTypeDef = TypedDict(
    "UpdateProfilingGroupResponseTypeDef",
    {
        "profilingGroup": "ProfilingGroupDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserFeedbackTypeDef = TypedDict(
    "UserFeedbackTypeDef",
    {
        "type": FeedbackTypeType,
    },
)
