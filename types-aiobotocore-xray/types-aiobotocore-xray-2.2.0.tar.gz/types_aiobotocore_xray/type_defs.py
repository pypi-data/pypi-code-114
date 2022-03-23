"""
Type annotations for xray service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_xray/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EncryptionStatusType,
    EncryptionTypeType,
    InsightStateType,
    SamplingStrategyNameType,
    TimeRangeTypeType,
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
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AnomalousServiceTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "BatchGetTracesRequestRequestTypeDef",
    "BatchGetTracesResultTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupResultTypeDef",
    "CreateSamplingRuleRequestRequestTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteSamplingRuleRequestRequestTypeDef",
    "DeleteSamplingRuleResultTypeDef",
    "EdgeStatisticsTypeDef",
    "EdgeTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "ErrorRootCauseTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultRootCauseEntityTypeDef",
    "FaultRootCauseServiceTypeDef",
    "FaultRootCauseTypeDef",
    "FaultStatisticsTypeDef",
    "ForecastStatisticsTypeDef",
    "GetEncryptionConfigResultTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResultTypeDef",
    "GetGroupsRequestRequestTypeDef",
    "GetGroupsResultTypeDef",
    "GetInsightEventsRequestRequestTypeDef",
    "GetInsightEventsResultTypeDef",
    "GetInsightImpactGraphRequestRequestTypeDef",
    "GetInsightImpactGraphResultTypeDef",
    "GetInsightRequestRequestTypeDef",
    "GetInsightResultTypeDef",
    "GetInsightSummariesRequestRequestTypeDef",
    "GetInsightSummariesResultTypeDef",
    "GetSamplingRulesRequestRequestTypeDef",
    "GetSamplingRulesResultTypeDef",
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsRequestRequestTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetServiceGraphRequestRequestTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphRequestRequestTypeDef",
    "GetTraceGraphResultTypeDef",
    "GetTraceSummariesRequestRequestTypeDef",
    "GetTraceSummariesResultTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "InsightEventTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsConfigurationTypeDef",
    "InstanceIdDetailTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutEncryptionConfigRequestRequestTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "PutTelemetryRecordsRequestRequestTypeDef",
    "PutTraceSegmentsRequestRequestTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "RequestImpactStatisticsTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TelemetryRecordTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateGroupResultTypeDef",
    "UpdateSamplingRuleRequestRequestTypeDef",
    "UpdateSamplingRuleResultTypeDef",
    "ValueWithServiceIdsTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)

AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {
        "NumberValue": NotRequired[float],
        "BooleanValue": NotRequired[bool],
        "StringValue": NotRequired[str],
    },
)

AnomalousServiceTypeDef = TypedDict(
    "AnomalousServiceTypeDef",
    {
        "ServiceId": NotRequired["ServiceIdTypeDef"],
    },
)

AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef",
    {
        "Name": NotRequired[str],
    },
)

BackendConnectionErrorsTypeDef = TypedDict(
    "BackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": NotRequired[int],
        "ConnectionRefusedCount": NotRequired[int],
        "HTTPCode4XXCount": NotRequired[int],
        "HTTPCode5XXCount": NotRequired[int],
        "UnknownHostCount": NotRequired[int],
        "OtherCount": NotRequired[int],
    },
)

BatchGetTracesRequestRequestTypeDef = TypedDict(
    "BatchGetTracesRequestRequestTypeDef",
    {
        "TraceIds": Sequence[str],
        "NextToken": NotRequired[str],
    },
)

BatchGetTracesResultTypeDef = TypedDict(
    "BatchGetTracesResultTypeDef",
    {
        "Traces": List["TraceTypeDef"],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired["InsightsConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGroupResultTypeDef = TypedDict(
    "CreateGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSamplingRuleRequestRequestTypeDef = TypedDict(
    "CreateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRule": "SamplingRuleTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSamplingRuleResultTypeDef = TypedDict(
    "CreateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
    },
)

DeleteSamplingRuleRequestRequestTypeDef = TypedDict(
    "DeleteSamplingRuleRequestRequestTypeDef",
    {
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
    },
)

DeleteSamplingRuleResultTypeDef = TypedDict(
    "DeleteSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EdgeStatisticsTypeDef = TypedDict(
    "EdgeStatisticsTypeDef",
    {
        "OkCount": NotRequired[int],
        "ErrorStatistics": NotRequired["ErrorStatisticsTypeDef"],
        "FaultStatistics": NotRequired["FaultStatisticsTypeDef"],
        "TotalCount": NotRequired[int],
        "TotalResponseTime": NotRequired[float],
    },
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "SummaryStatistics": NotRequired["EdgeStatisticsTypeDef"],
        "ResponseTimeHistogram": NotRequired[List["HistogramEntryTypeDef"]],
        "Aliases": NotRequired[List["AliasTypeDef"]],
    },
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[EncryptionStatusType],
        "Type": NotRequired[EncryptionTypeType],
    },
)

ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Exceptions": NotRequired[List["RootCauseExceptionTypeDef"]],
        "Remote": NotRequired[bool],
    },
)

ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List["ErrorRootCauseEntityTypeDef"]],
        "Inferred": NotRequired[bool],
    },
)

ErrorRootCauseTypeDef = TypedDict(
    "ErrorRootCauseTypeDef",
    {
        "Services": NotRequired[List["ErrorRootCauseServiceTypeDef"]],
        "ClientImpacting": NotRequired[bool],
    },
)

ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {
        "ThrottleCount": NotRequired[int],
        "OtherCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)

FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Exceptions": NotRequired[List["RootCauseExceptionTypeDef"]],
        "Remote": NotRequired[bool],
    },
)

FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List["FaultRootCauseEntityTypeDef"]],
        "Inferred": NotRequired[bool],
    },
)

FaultRootCauseTypeDef = TypedDict(
    "FaultRootCauseTypeDef",
    {
        "Services": NotRequired[List["FaultRootCauseServiceTypeDef"]],
        "ClientImpacting": NotRequired[bool],
    },
)

FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef",
    {
        "OtherCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)

ForecastStatisticsTypeDef = TypedDict(
    "ForecastStatisticsTypeDef",
    {
        "FaultCountHigh": NotRequired[int],
        "FaultCountLow": NotRequired[int],
    },
)

GetEncryptionConfigResultTypeDef = TypedDict(
    "GetEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
    },
)

GetGroupResultTypeDef = TypedDict(
    "GetGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupsRequestRequestTypeDef = TypedDict(
    "GetGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

GetGroupsResultTypeDef = TypedDict(
    "GetGroupsResultTypeDef",
    {
        "Groups": List["GroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightEventsRequestRequestTypeDef = TypedDict(
    "GetInsightEventsRequestRequestTypeDef",
    {
        "InsightId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetInsightEventsResultTypeDef = TypedDict(
    "GetInsightEventsResultTypeDef",
    {
        "InsightEvents": List["InsightEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightImpactGraphRequestRequestTypeDef = TypedDict(
    "GetInsightImpactGraphRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": NotRequired[str],
    },
)

GetInsightImpactGraphResultTypeDef = TypedDict(
    "GetInsightImpactGraphResultTypeDef",
    {
        "InsightId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceGraphStartTime": datetime,
        "ServiceGraphEndTime": datetime,
        "Services": List["InsightImpactGraphServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightRequestRequestTypeDef = TypedDict(
    "GetInsightRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)

GetInsightResultTypeDef = TypedDict(
    "GetInsightResultTypeDef",
    {
        "Insight": "InsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightSummariesRequestRequestTypeDef = TypedDict(
    "GetInsightSummariesRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "States": NotRequired[Sequence[InsightStateType]],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetInsightSummariesResultTypeDef = TypedDict(
    "GetInsightSummariesResultTypeDef",
    {
        "InsightSummaries": List["InsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingRulesRequestRequestTypeDef = TypedDict(
    "GetSamplingRulesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

GetSamplingRulesResultTypeDef = TypedDict(
    "GetSamplingRulesResultTypeDef",
    {
        "SamplingRuleRecords": List["SamplingRuleRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingStatisticSummariesRequestRequestTypeDef = TypedDict(
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

GetSamplingStatisticSummariesResultTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultTypeDef",
    {
        "SamplingStatisticSummaries": List["SamplingStatisticSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSamplingTargetsRequestRequestTypeDef = TypedDict(
    "GetSamplingTargetsRequestRequestTypeDef",
    {
        "SamplingStatisticsDocuments": Sequence["SamplingStatisticsDocumentTypeDef"],
    },
)

GetSamplingTargetsResultTypeDef = TypedDict(
    "GetSamplingTargetsResultTypeDef",
    {
        "SamplingTargetDocuments": List["SamplingTargetDocumentTypeDef"],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List["UnprocessedStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceGraphRequestRequestTypeDef = TypedDict(
    "GetServiceGraphRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

GetServiceGraphResultTypeDef = TypedDict(
    "GetServiceGraphResultTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List["ServiceTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTimeSeriesServiceStatisticsRequestRequestTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "EntitySelectorExpression": NotRequired[str],
        "Period": NotRequired[int],
        "ForecastStatistics": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)

GetTimeSeriesServiceStatisticsResultTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    {
        "TimeSeriesServiceStatistics": List["TimeSeriesServiceStatisticsTypeDef"],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTraceGraphRequestRequestTypeDef = TypedDict(
    "GetTraceGraphRequestRequestTypeDef",
    {
        "TraceIds": Sequence[str],
        "NextToken": NotRequired[str],
    },
)

GetTraceGraphResultTypeDef = TypedDict(
    "GetTraceGraphResultTypeDef",
    {
        "Services": List["ServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTraceSummariesRequestRequestTypeDef = TypedDict(
    "GetTraceSummariesRequestRequestTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "TimeRangeType": NotRequired[TimeRangeTypeType],
        "Sampling": NotRequired[bool],
        "SamplingStrategy": NotRequired["SamplingStrategyTypeDef"],
        "FilterExpression": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

GetTraceSummariesResultTypeDef = TypedDict(
    "GetTraceSummariesResultTypeDef",
    {
        "TraceSummaries": List["TraceSummaryTypeDef"],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired["InsightsConfigurationTypeDef"],
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired["InsightsConfigurationTypeDef"],
    },
)

HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef",
    {
        "Value": NotRequired[float],
        "Count": NotRequired[int],
    },
)

HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {
        "HttpURL": NotRequired[str],
        "HttpStatus": NotRequired[int],
        "HttpMethod": NotRequired[str],
        "UserAgent": NotRequired[str],
        "ClientIp": NotRequired[str],
    },
)

InsightEventTypeDef = TypedDict(
    "InsightEventTypeDef",
    {
        "Summary": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "ClientRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "RootCauseServiceRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "TopAnomalousServices": NotRequired[List["AnomalousServiceTypeDef"]],
    },
)

InsightImpactGraphEdgeTypeDef = TypedDict(
    "InsightImpactGraphEdgeTypeDef",
    {
        "ReferenceId": NotRequired[int],
    },
)

InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Edges": NotRequired[List["InsightImpactGraphEdgeTypeDef"]],
    },
)

InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "InsightId": NotRequired[str],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "RootCauseServiceId": NotRequired["ServiceIdTypeDef"],
        "Categories": NotRequired[List[Literal["FAULT"]]],
        "State": NotRequired[InsightStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Summary": NotRequired[str],
        "ClientRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "RootCauseServiceRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "TopAnomalousServices": NotRequired[List["AnomalousServiceTypeDef"]],
        "LastUpdateTime": NotRequired[datetime],
    },
)

InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightId": NotRequired[str],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "RootCauseServiceId": NotRequired["ServiceIdTypeDef"],
        "Categories": NotRequired[List[Literal["FAULT"]]],
        "State": NotRequired[InsightStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Summary": NotRequired[str],
        "ClientRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "RootCauseServiceRequestImpactStatistics": NotRequired["RequestImpactStatisticsTypeDef"],
        "TopAnomalousServices": NotRequired[List["AnomalousServiceTypeDef"]],
    },
)

InsightsConfigurationTypeDef = TypedDict(
    "InsightsConfigurationTypeDef",
    {
        "InsightsEnabled": NotRequired[bool],
        "NotificationsEnabled": NotRequired[bool],
    },
)

InstanceIdDetailTypeDef = TypedDict(
    "InstanceIdDetailTypeDef",
    {
        "Id": NotRequired[str],
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
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

PutEncryptionConfigRequestRequestTypeDef = TypedDict(
    "PutEncryptionConfigRequestRequestTypeDef",
    {
        "Type": EncryptionTypeType,
        "KeyId": NotRequired[str],
    },
)

PutEncryptionConfigResultTypeDef = TypedDict(
    "PutEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": "EncryptionConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutTelemetryRecordsRequestRequestTypeDef = TypedDict(
    "PutTelemetryRecordsRequestRequestTypeDef",
    {
        "TelemetryRecords": Sequence["TelemetryRecordTypeDef"],
        "EC2InstanceId": NotRequired[str],
        "Hostname": NotRequired[str],
        "ResourceARN": NotRequired[str],
    },
)

PutTraceSegmentsRequestRequestTypeDef = TypedDict(
    "PutTraceSegmentsRequestRequestTypeDef",
    {
        "TraceSegmentDocuments": Sequence[str],
    },
)

PutTraceSegmentsResultTypeDef = TypedDict(
    "PutTraceSegmentsResultTypeDef",
    {
        "UnprocessedTraceSegments": List["UnprocessedTraceSegmentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestImpactStatisticsTypeDef = TypedDict(
    "RequestImpactStatisticsTypeDef",
    {
        "FaultCount": NotRequired[int],
        "OkCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)

ResourceARNDetailTypeDef = TypedDict(
    "ResourceARNDetailTypeDef",
    {
        "ARN": NotRequired[str],
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

ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Coverage": NotRequired[float],
        "Remote": NotRequired[bool],
    },
)

ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List["ResponseTimeRootCauseEntityTypeDef"]],
        "Inferred": NotRequired[bool],
    },
)

ResponseTimeRootCauseTypeDef = TypedDict(
    "ResponseTimeRootCauseTypeDef",
    {
        "Services": NotRequired[List["ResponseTimeRootCauseServiceTypeDef"]],
        "ClientImpacting": NotRequired[bool],
    },
)

RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef",
    {
        "Name": NotRequired[str],
        "Message": NotRequired[str],
    },
)

SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {
        "SamplingRule": NotRequired["SamplingRuleTypeDef"],
        "CreatedAt": NotRequired[datetime],
        "ModifiedAt": NotRequired[datetime],
    },
)

SamplingRuleTypeDef = TypedDict(
    "SamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

SamplingRuleUpdateTypeDef = TypedDict(
    "SamplingRuleUpdateTypeDef",
    {
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Priority": NotRequired[int],
        "FixedRate": NotRequired[float],
        "ReservoirSize": NotRequired[int],
        "Host": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceType": NotRequired[str],
        "HTTPMethod": NotRequired[str],
        "URLPath": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)

SamplingStatisticSummaryTypeDef = TypedDict(
    "SamplingStatisticSummaryTypeDef",
    {
        "RuleName": NotRequired[str],
        "Timestamp": NotRequired[datetime],
        "RequestCount": NotRequired[int],
        "BorrowCount": NotRequired[int],
        "SampledCount": NotRequired[int],
    },
)

SamplingStatisticsDocumentTypeDef = TypedDict(
    "SamplingStatisticsDocumentTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": Union[datetime, str],
        "RequestCount": int,
        "SampledCount": int,
        "BorrowCount": NotRequired[int],
    },
)

SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {
        "Name": NotRequired[SamplingStrategyNameType],
        "Value": NotRequired[float],
    },
)

SamplingTargetDocumentTypeDef = TypedDict(
    "SamplingTargetDocumentTypeDef",
    {
        "RuleName": NotRequired[str],
        "FixedRate": NotRequired[float],
        "ReservoirQuota": NotRequired[int],
        "ReservoirQuotaTTL": NotRequired[datetime],
        "Interval": NotRequired[int],
    },
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "Id": NotRequired[str],
        "Document": NotRequired[str],
    },
)

ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

ServiceStatisticsTypeDef = TypedDict(
    "ServiceStatisticsTypeDef",
    {
        "OkCount": NotRequired[int],
        "ErrorStatistics": NotRequired["ErrorStatisticsTypeDef"],
        "FaultStatistics": NotRequired["FaultStatisticsTypeDef"],
        "TotalCount": NotRequired[int],
        "TotalResponseTime": NotRequired[float],
    },
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Root": NotRequired[bool],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
        "State": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Edges": NotRequired[List["EdgeTypeDef"]],
        "SummaryStatistics": NotRequired["ServiceStatisticsTypeDef"],
        "DurationHistogram": NotRequired[List["HistogramEntryTypeDef"]],
        "ResponseTimeHistogram": NotRequired[List["HistogramEntryTypeDef"]],
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

TelemetryRecordTypeDef = TypedDict(
    "TelemetryRecordTypeDef",
    {
        "Timestamp": Union[datetime, str],
        "SegmentsReceivedCount": NotRequired[int],
        "SegmentsSentCount": NotRequired[int],
        "SegmentsSpilloverCount": NotRequired[int],
        "SegmentsRejectedCount": NotRequired[int],
        "BackendConnectionErrors": NotRequired["BackendConnectionErrorsTypeDef"],
    },
)

TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "EdgeSummaryStatistics": NotRequired["EdgeStatisticsTypeDef"],
        "ServiceSummaryStatistics": NotRequired["ServiceStatisticsTypeDef"],
        "ServiceForecastStatistics": NotRequired["ForecastStatisticsTypeDef"],
        "ResponseTimeHistogram": NotRequired[List["HistogramEntryTypeDef"]],
    },
)

TraceSummaryTypeDef = TypedDict(
    "TraceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Duration": NotRequired[float],
        "ResponseTime": NotRequired[float],
        "HasFault": NotRequired[bool],
        "HasError": NotRequired[bool],
        "HasThrottle": NotRequired[bool],
        "IsPartial": NotRequired[bool],
        "Http": NotRequired["HttpTypeDef"],
        "Annotations": NotRequired[Dict[str, List["ValueWithServiceIdsTypeDef"]]],
        "Users": NotRequired[List["TraceUserTypeDef"]],
        "ServiceIds": NotRequired[List["ServiceIdTypeDef"]],
        "ResourceARNs": NotRequired[List["ResourceARNDetailTypeDef"]],
        "InstanceIds": NotRequired[List["InstanceIdDetailTypeDef"]],
        "AvailabilityZones": NotRequired[List["AvailabilityZoneDetailTypeDef"]],
        "EntryPoint": NotRequired["ServiceIdTypeDef"],
        "FaultRootCauses": NotRequired[List["FaultRootCauseTypeDef"]],
        "ErrorRootCauses": NotRequired[List["ErrorRootCauseTypeDef"]],
        "ResponseTimeRootCauses": NotRequired[List["ResponseTimeRootCauseTypeDef"]],
        "Revision": NotRequired[int],
        "MatchedEventTime": NotRequired[datetime],
    },
)

TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "Id": NotRequired[str],
        "Duration": NotRequired[float],
        "LimitExceeded": NotRequired[bool],
        "Segments": NotRequired[List["SegmentTypeDef"]],
    },
)

TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef",
    {
        "UserName": NotRequired[str],
        "ServiceIds": NotRequired[List["ServiceIdTypeDef"]],
    },
)

UnprocessedStatisticsTypeDef = TypedDict(
    "UnprocessedStatisticsTypeDef",
    {
        "RuleName": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)

UnprocessedTraceSegmentTypeDef = TypedDict(
    "UnprocessedTraceSegmentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired["InsightsConfigurationTypeDef"],
    },
)

UpdateGroupResultTypeDef = TypedDict(
    "UpdateGroupResultTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSamplingRuleRequestRequestTypeDef = TypedDict(
    "UpdateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRuleUpdate": "SamplingRuleUpdateTypeDef",
    },
)

UpdateSamplingRuleResultTypeDef = TypedDict(
    "UpdateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": "SamplingRuleRecordTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {
        "AnnotationValue": NotRequired["AnnotationValueTypeDef"],
        "ServiceIds": NotRequired[List["ServiceIdTypeDef"]],
    },
)
