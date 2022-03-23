"""
Type annotations for application-insights service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_application_insights/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_application_insights.type_defs import ApplicationComponentTypeDef

    data: ApplicationComponentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    CloudWatchEventSourceType,
    ConfigurationEventResourceTypeType,
    ConfigurationEventStatusType,
    DiscoveryTypeType,
    FeedbackValueType,
    LogFilterType,
    OsTypeType,
    SeverityLevelType,
    StatusType,
    TierType,
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
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateComponentRequestRequestTypeDef",
    "CreateLogPatternRequestRequestTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteComponentRequestRequestTypeDef",
    "DeleteLogPatternRequestRequestTypeDef",
    "DescribeApplicationRequestRequestTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationRequestRequestTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeComponentRequestRequestTypeDef",
    "DescribeComponentResponseTypeDef",
    "DescribeLogPatternRequestRequestTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "DescribeObservationRequestRequestTypeDef",
    "DescribeObservationResponseTypeDef",
    "DescribeProblemObservationsRequestRequestTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
    "DescribeProblemRequestRequestTypeDef",
    "DescribeProblemResponseTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListComponentsRequestRequestTypeDef",
    "ListComponentsResponseTypeDef",
    "ListConfigurationHistoryRequestRequestTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "ListLogPatternSetsRequestRequestTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "ListLogPatternsRequestRequestTypeDef",
    "ListLogPatternsResponseTypeDef",
    "ListProblemsRequestRequestTypeDef",
    "ListProblemsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateComponentConfigurationRequestRequestTypeDef",
    "UpdateComponentRequestRequestTypeDef",
    "UpdateLogPatternRequestRequestTypeDef",
    "UpdateLogPatternResponseTypeDef",
)

ApplicationComponentTypeDef = TypedDict(
    "ApplicationComponentTypeDef",
    {
        "ComponentName": NotRequired[str],
        "ComponentRemarks": NotRequired[str],
        "ResourceType": NotRequired[str],
        "OsType": NotRequired[OsTypeType],
        "Tier": NotRequired[TierType],
        "Monitor": NotRequired[bool],
        "DetectedWorkload": NotRequired[Dict[TierType, Dict[str, str]]],
    },
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "ResourceGroupName": NotRequired[str],
        "LifeCycle": NotRequired[str],
        "OpsItemSNSTopicArn": NotRequired[str],
        "OpsCenterEnabled": NotRequired[bool],
        "CWEMonitorEnabled": NotRequired[bool],
        "Remarks": NotRequired[str],
        "AutoConfigEnabled": NotRequired[bool],
        "DiscoveryType": NotRequired[DiscoveryTypeType],
    },
)

ConfigurationEventTypeDef = TypedDict(
    "ConfigurationEventTypeDef",
    {
        "MonitoredResourceARN": NotRequired[str],
        "EventStatus": NotRequired[ConfigurationEventStatusType],
        "EventResourceType": NotRequired[ConfigurationEventResourceTypeType],
        "EventTime": NotRequired[datetime],
        "EventDetail": NotRequired[str],
        "EventResourceName": NotRequired[str],
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": NotRequired[str],
        "OpsCenterEnabled": NotRequired[bool],
        "CWEMonitorEnabled": NotRequired[bool],
        "OpsItemSNSTopicArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "AutoConfigEnabled": NotRequired[bool],
        "AutoCreate": NotRequired[bool],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateComponentRequestRequestTypeDef = TypedDict(
    "CreateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "ResourceList": Sequence[str],
    },
)

CreateLogPatternRequestRequestTypeDef = TypedDict(
    "CreateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": str,
        "Rank": int,
    },
)

CreateLogPatternResponseTypeDef = TypedDict(
    "CreateLogPatternResponseTypeDef",
    {
        "LogPattern": "LogPatternTypeDef",
        "ResourceGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DeleteComponentRequestRequestTypeDef = TypedDict(
    "DeleteComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DeleteLogPatternRequestRequestTypeDef = TypedDict(
    "DeleteLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeApplicationRequestRequestTypeDef = TypedDict(
    "DescribeApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
    },
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRecommendationRequestRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "Tier": TierType,
    },
)

DescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    {
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentConfigurationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseTypeDef",
    {
        "Monitor": bool,
        "Tier": TierType,
        "ComponentConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeComponentRequestRequestTypeDef = TypedDict(
    "DescribeComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
    },
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {
        "ApplicationComponent": "ApplicationComponentTypeDef",
        "ResourceList": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogPatternRequestRequestTypeDef = TypedDict(
    "DescribeLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
    },
)

DescribeLogPatternResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeObservationRequestRequestTypeDef = TypedDict(
    "DescribeObservationRequestRequestTypeDef",
    {
        "ObservationId": str,
    },
)

DescribeObservationResponseTypeDef = TypedDict(
    "DescribeObservationResponseTypeDef",
    {
        "Observation": "ObservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemObservationsRequestRequestTypeDef = TypedDict(
    "DescribeProblemObservationsRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemObservationsResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseTypeDef",
    {
        "RelatedObservations": "RelatedObservationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProblemRequestRequestTypeDef = TypedDict(
    "DescribeProblemRequestRequestTypeDef",
    {
        "ProblemId": str,
    },
)

DescribeProblemResponseTypeDef = TypedDict(
    "DescribeProblemResponseTypeDef",
    {
        "Problem": "ProblemTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "ApplicationInfoList": List["ApplicationInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListComponentsRequestRequestTypeDef = TypedDict(
    "ListComponentsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {
        "ApplicationComponentList": List["ApplicationComponentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConfigurationHistoryRequestRequestTypeDef = TypedDict(
    "ListConfigurationHistoryRequestRequestTypeDef",
    {
        "ResourceGroupName": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "EventStatus": NotRequired[ConfigurationEventStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConfigurationHistoryResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseTypeDef",
    {
        "EventList": List["ConfigurationEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogPatternSetsRequestRequestTypeDef = TypedDict(
    "ListLogPatternSetsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLogPatternSetsResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatternSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLogPatternsRequestRequestTypeDef = TypedDict(
    "ListLogPatternsRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLogPatternsResponseTypeDef = TypedDict(
    "ListLogPatternsResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPatterns": List["LogPatternTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProblemsRequestRequestTypeDef = TypedDict(
    "ListProblemsRequestRequestTypeDef",
    {
        "ResourceGroupName": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ComponentName": NotRequired[str],
    },
)

ListProblemsResponseTypeDef = TypedDict(
    "ListProblemsResponseTypeDef",
    {
        "ProblemList": List["ProblemTypeDef"],
        "NextToken": str,
        "ResourceGroupName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {
        "PatternSetName": NotRequired[str],
        "PatternName": NotRequired[str],
        "Pattern": NotRequired[str],
        "Rank": NotRequired[int],
    },
)

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "Id": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "SourceType": NotRequired[str],
        "SourceARN": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LineTime": NotRequired[datetime],
        "LogText": NotRequired[str],
        "LogFilter": NotRequired[LogFilterType],
        "MetricNamespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Unit": NotRequired[str],
        "Value": NotRequired[float],
        "CloudWatchEventId": NotRequired[str],
        "CloudWatchEventSource": NotRequired[CloudWatchEventSourceType],
        "CloudWatchEventDetailType": NotRequired[str],
        "HealthEventArn": NotRequired[str],
        "HealthService": NotRequired[str],
        "HealthEventTypeCode": NotRequired[str],
        "HealthEventTypeCategory": NotRequired[str],
        "HealthEventDescription": NotRequired[str],
        "CodeDeployDeploymentId": NotRequired[str],
        "CodeDeployDeploymentGroup": NotRequired[str],
        "CodeDeployState": NotRequired[str],
        "CodeDeployApplication": NotRequired[str],
        "CodeDeployInstanceGroupId": NotRequired[str],
        "Ec2State": NotRequired[str],
        "RdsEventCategories": NotRequired[str],
        "RdsEventMessage": NotRequired[str],
        "S3EventName": NotRequired[str],
        "StatesExecutionArn": NotRequired[str],
        "StatesArn": NotRequired[str],
        "StatesStatus": NotRequired[str],
        "StatesInput": NotRequired[str],
        "EbsEvent": NotRequired[str],
        "EbsResult": NotRequired[str],
        "EbsCause": NotRequired[str],
        "EbsRequestId": NotRequired[str],
        "XRayFaultPercent": NotRequired[int],
        "XRayThrottlePercent": NotRequired[int],
        "XRayErrorPercent": NotRequired[int],
        "XRayRequestCount": NotRequired[int],
        "XRayRequestAverageLatency": NotRequired[int],
        "XRayNodeName": NotRequired[str],
        "XRayNodeType": NotRequired[str],
    },
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "Id": NotRequired[str],
        "Title": NotRequired[str],
        "Insights": NotRequired[str],
        "Status": NotRequired[StatusType],
        "AffectedResource": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "SeverityLevel": NotRequired[SeverityLevelType],
        "ResourceGroupName": NotRequired[str],
        "Feedback": NotRequired[Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValueType]],
        "RecurringCount": NotRequired[int],
        "LastRecurrenceTime": NotRequired[datetime],
    },
)

RelatedObservationsTypeDef = TypedDict(
    "RelatedObservationsTypeDef",
    {
        "ObservationList": NotRequired[List["ObservationTypeDef"]],
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "OpsCenterEnabled": NotRequired[bool],
        "CWEMonitorEnabled": NotRequired[bool],
        "OpsItemSNSTopicArn": NotRequired[str],
        "RemoveSNSTopic": NotRequired[bool],
        "AutoConfigEnabled": NotRequired[bool],
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "ApplicationInfo": "ApplicationInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateComponentConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateComponentConfigurationRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "Monitor": NotRequired[bool],
        "Tier": NotRequired[TierType],
        "ComponentConfiguration": NotRequired[str],
        "AutoConfigEnabled": NotRequired[bool],
    },
)

UpdateComponentRequestRequestTypeDef = TypedDict(
    "UpdateComponentRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "ComponentName": str,
        "NewComponentName": NotRequired[str],
        "ResourceList": NotRequired[Sequence[str]],
    },
)

UpdateLogPatternRequestRequestTypeDef = TypedDict(
    "UpdateLogPatternRequestRequestTypeDef",
    {
        "ResourceGroupName": str,
        "PatternSetName": str,
        "PatternName": str,
        "Pattern": NotRequired[str],
        "Rank": NotRequired[int],
    },
)

UpdateLogPatternResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseTypeDef",
    {
        "ResourceGroupName": str,
        "LogPattern": "LogPatternTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
