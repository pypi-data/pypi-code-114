"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AccountHealthTypeDef

    data: AccountHealthTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AnomalySeverityType,
    AnomalyStatusType,
    AnomalyTypeType,
    CloudWatchMetricDataStatusCodeType,
    CloudWatchMetricsStatType,
    CostEstimationServiceResourceStateType,
    CostEstimationStatusType,
    EventClassType,
    EventDataSourceType,
    EventSourceOptInStatusType,
    InsightFeedbackOptionType,
    InsightSeverityType,
    InsightStatusType,
    InsightTypeType,
    LocaleType,
    OptInStatusType,
    OrganizationResourceCollectionTypeType,
    ResourceCollectionTypeType,
    ServiceNameType,
    UpdateResourceCollectionActionType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountHealthTypeDef",
    "AccountInsightHealthTypeDef",
    "AddNotificationChannelRequestRequestTypeDef",
    "AddNotificationChannelResponseTypeDef",
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    "AnomalyReportedTimeRangeTypeDef",
    "AnomalyResourceTypeDef",
    "AnomalySourceDetailsTypeDef",
    "AnomalySourceMetadataTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDataSummaryTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewRequestRequestTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyRequestRequestTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeEventSourcesConfigResponseTypeDef",
    "DescribeFeedbackRequestRequestTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "DescribeInsightRequestRequestTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeOrganizationHealthRequestRequestTypeDef",
    "DescribeOrganizationHealthResponseTypeDef",
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    "DescribeOrganizationOverviewResponseTypeDef",
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventSourcesConfigTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationRequestRequestTypeDef",
    "GetCostEstimationResponseTypeDef",
    "GetResourceCollectionRequestRequestTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightRequestRequestTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsRequestRequestTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsRequestRequestTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsRequestRequestTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListOrganizationInsightsRequestRequestTypeDef",
    "ListOrganizationInsightsResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    "PerformanceInsightsMetricQueryTypeDef",
    "PerformanceInsightsMetricsDetailTypeDef",
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    "PerformanceInsightsReferenceDataTypeDef",
    "PerformanceInsightsReferenceMetricTypeDef",
    "PerformanceInsightsReferenceScalarTypeDef",
    "PerformanceInsightsStatTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "ProactiveOrganizationInsightSummaryTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "ReactiveOrganizationInsightSummaryTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RecommendationRelatedEventTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelRequestRequestTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "ResponseMetadataTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsRequestRequestTypeDef",
    "SearchInsightsResponseTypeDef",
    "SearchOrganizationInsightsFiltersTypeDef",
    "SearchOrganizationInsightsRequestRequestTypeDef",
    "SearchOrganizationInsightsResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartCostEstimationRequestRequestTypeDef",
    "StartTimeRangeTypeDef",
    "TagCollectionFilterTypeDef",
    "TagCollectionTypeDef",
    "TagCostEstimationResourceCollectionFilterTypeDef",
    "TagHealthTypeDef",
    "TimestampMetricValuePairTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateResourceCollectionRequestRequestTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
    "UpdateServiceIntegrationRequestRequestTypeDef",
    "UpdateTagCollectionFilterTypeDef",
)

AccountHealthTypeDef = TypedDict(
    "AccountHealthTypeDef",
    {
        "AccountId": NotRequired[str],
        "Insight": NotRequired["AccountInsightHealthTypeDef"],
    },
)

AccountInsightHealthTypeDef = TypedDict(
    "AccountInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
    },
)

AddNotificationChannelRequestRequestTypeDef = TypedDict(
    "AddNotificationChannelRequestRequestTypeDef",
    {
        "Config": "NotificationChannelConfigTypeDef",
    },
)

AddNotificationChannelResponseTypeDef = TypedDict(
    "AddNotificationChannelResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AmazonCodeGuruProfilerIntegrationTypeDef = TypedDict(
    "AmazonCodeGuruProfilerIntegrationTypeDef",
    {
        "Status": NotRequired[EventSourceOptInStatusType],
    },
)

AnomalyReportedTimeRangeTypeDef = TypedDict(
    "AnomalyReportedTimeRangeTypeDef",
    {
        "OpenTime": datetime,
        "CloseTime": NotRequired[datetime],
    },
)

AnomalyResourceTypeDef = TypedDict(
    "AnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

AnomalySourceDetailsTypeDef = TypedDict(
    "AnomalySourceDetailsTypeDef",
    {
        "CloudWatchMetrics": NotRequired[List["CloudWatchMetricsDetailTypeDef"]],
        "PerformanceInsightsMetrics": NotRequired[List["PerformanceInsightsMetricsDetailTypeDef"]],
    },
)

AnomalySourceMetadataTypeDef = TypedDict(
    "AnomalySourceMetadataTypeDef",
    {
        "Source": NotRequired[str],
        "SourceResourceName": NotRequired[str],
        "SourceResourceType": NotRequired[str],
    },
)

AnomalyTimeRangeTypeDef = TypedDict(
    "AnomalyTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)

CloudFormationCollectionFilterTypeDef = TypedDict(
    "CloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)

CloudFormationCollectionTypeDef = TypedDict(
    "CloudFormationCollectionTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)

CloudFormationCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[List[str]],
    },
)

CloudFormationHealthTypeDef = TypedDict(
    "CloudFormationHealthTypeDef",
    {
        "StackName": NotRequired[str],
        "Insight": NotRequired["InsightHealthTypeDef"],
    },
)

CloudWatchMetricsDataSummaryTypeDef = TypedDict(
    "CloudWatchMetricsDataSummaryTypeDef",
    {
        "TimestampMetricValuePairList": NotRequired[List["TimestampMetricValuePairTypeDef"]],
        "StatusCode": NotRequired[CloudWatchMetricDataStatusCodeType],
    },
)

CloudWatchMetricsDetailTypeDef = TypedDict(
    "CloudWatchMetricsDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Dimensions": NotRequired[List["CloudWatchMetricsDimensionTypeDef"]],
        "Stat": NotRequired[CloudWatchMetricsStatType],
        "Unit": NotRequired[str],
        "Period": NotRequired[int],
        "MetricDataSummary": NotRequired["CloudWatchMetricsDataSummaryTypeDef"],
    },
)

CloudWatchMetricsDimensionTypeDef = TypedDict(
    "CloudWatchMetricsDimensionTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)

CostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "CostEstimationResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired[
            "CloudFormationCostEstimationResourceCollectionFilterTypeDef"
        ],
        "Tags": NotRequired[List["TagCostEstimationResourceCollectionFilterTypeDef"]],
    },
)

CostEstimationTimeRangeTypeDef = TypedDict(
    "CostEstimationTimeRangeTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

DescribeAccountHealthResponseTypeDef = TypedDict(
    "DescribeAccountHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountOverviewRequestRequestTypeDef = TypedDict(
    "DescribeAccountOverviewRequestRequestTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": NotRequired[Union[datetime, str]],
    },
)

DescribeAccountOverviewResponseTypeDef = TypedDict(
    "DescribeAccountOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "MeanTimeToRecoverInMilliseconds": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)

DescribeAnomalyResponseTypeDef = TypedDict(
    "DescribeAnomalyResponseTypeDef",
    {
        "ProactiveAnomaly": "ProactiveAnomalyTypeDef",
        "ReactiveAnomaly": "ReactiveAnomalyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEventSourcesConfigResponseTypeDef = TypedDict(
    "DescribeEventSourcesConfigResponseTypeDef",
    {
        "EventSources": "EventSourcesConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeFeedbackRequestRequestTypeDef",
    {
        "InsightId": NotRequired[str],
    },
)

DescribeFeedbackResponseTypeDef = TypedDict(
    "DescribeFeedbackResponseTypeDef",
    {
        "InsightFeedback": "InsightFeedbackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRequestRequestTypeDef = TypedDict(
    "DescribeInsightRequestRequestTypeDef",
    {
        "Id": str,
        "AccountId": NotRequired[str],
    },
)

DescribeInsightResponseTypeDef = TypedDict(
    "DescribeInsightResponseTypeDef",
    {
        "ProactiveInsight": "ProactiveInsightTypeDef",
        "ReactiveInsight": "ReactiveInsightTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationHealthRequestRequestTypeDef",
    {
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
    },
)

DescribeOrganizationHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationHealthResponseTypeDef",
    {
        "OpenReactiveInsights": int,
        "OpenProactiveInsights": int,
        "MetricsAnalyzed": int,
        "ResourceHours": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationOverviewRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationOverviewRequestRequestTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": NotRequired[Union[datetime, str]],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
    },
)

DescribeOrganizationOverviewResponseTypeDef = TypedDict(
    "DescribeOrganizationOverviewResponseTypeDef",
    {
        "ReactiveInsights": int,
        "ProactiveInsights": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthRequestRequestTypeDef",
    {
        "OrganizationResourceCollectionType": OrganizationResourceCollectionTypeType,
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeOrganizationResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeOrganizationResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
        "Service": List["ServiceHealthTypeDef"],
        "Account": List["AccountHealthTypeDef"],
        "NextToken": str,
        "Tags": List["TagHealthTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourceCollectionHealthRequestRequestTypeDef = TypedDict(
    "DescribeResourceCollectionHealthRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)

DescribeResourceCollectionHealthResponseTypeDef = TypedDict(
    "DescribeResourceCollectionHealthResponseTypeDef",
    {
        "CloudFormation": List["CloudFormationHealthTypeDef"],
        "Service": List["ServiceHealthTypeDef"],
        "NextToken": str,
        "Tags": List["TagHealthTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeServiceIntegrationResponseTypeDef = TypedDict(
    "DescribeServiceIntegrationResponseTypeDef",
    {
        "ServiceIntegration": "ServiceIntegrationConfigTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EndTimeRangeTypeDef = TypedDict(
    "EndTimeRangeTypeDef",
    {
        "FromTime": NotRequired[Union[datetime, str]],
        "ToTime": NotRequired[Union[datetime, str]],
    },
)

EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

EventSourcesConfigTypeDef = TypedDict(
    "EventSourcesConfigTypeDef",
    {
        "AmazonCodeGuruProfiler": NotRequired["AmazonCodeGuruProfilerIntegrationTypeDef"],
    },
)

EventTimeRangeTypeDef = TypedDict(
    "EventTimeRangeTypeDef",
    {
        "FromTime": Union[datetime, str],
        "ToTime": Union[datetime, str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "Id": NotRequired[str],
        "Time": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Name": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "EventClass": NotRequired[EventClassType],
        "Resources": NotRequired[List["EventResourceTypeDef"]],
    },
)

GetCostEstimationRequestRequestTypeDef = TypedDict(
    "GetCostEstimationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

GetCostEstimationResponseTypeDef = TypedDict(
    "GetCostEstimationResponseTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
        "Status": CostEstimationStatusType,
        "Costs": List["ServiceResourceCostTypeDef"],
        "TimeRange": "CostEstimationTimeRangeTypeDef",
        "TotalCost": float,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceCollectionRequestRequestTypeDef = TypedDict(
    "GetResourceCollectionRequestRequestTypeDef",
    {
        "ResourceCollectionType": ResourceCollectionTypeType,
        "NextToken": NotRequired[str],
    },
)

GetResourceCollectionResponseTypeDef = TypedDict(
    "GetResourceCollectionResponseTypeDef",
    {
        "ResourceCollection": "ResourceCollectionFilterTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightFeedbackTypeDef = TypedDict(
    "InsightFeedbackTypeDef",
    {
        "Id": NotRequired[str],
        "Feedback": NotRequired[InsightFeedbackOptionType],
    },
)

InsightHealthTypeDef = TypedDict(
    "InsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
        "MeanTimeToRecoverInMilliseconds": NotRequired[int],
    },
)

InsightTimeRangeTypeDef = TypedDict(
    "InsightTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)

ListAnomaliesForInsightRequestRequestTypeDef = TypedDict(
    "ListAnomaliesForInsightRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTimeRange": NotRequired["StartTimeRangeTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

ListAnomaliesForInsightResponseTypeDef = TypedDict(
    "ListAnomaliesForInsightResponseTypeDef",
    {
        "ProactiveAnomalies": List["ProactiveAnomalySummaryTypeDef"],
        "ReactiveAnomalies": List["ReactiveAnomalySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventsFiltersTypeDef = TypedDict(
    "ListEventsFiltersTypeDef",
    {
        "InsightId": NotRequired[str],
        "EventTimeRange": NotRequired["EventTimeRangeTypeDef"],
        "EventClass": NotRequired[EventClassType],
        "EventSource": NotRequired[str],
        "DataSource": NotRequired[EventDataSourceType],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
    },
)

ListEventsRequestRequestTypeDef = TypedDict(
    "ListEventsRequestRequestTypeDef",
    {
        "Filters": "ListEventsFiltersTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

ListEventsResponseTypeDef = TypedDict(
    "ListEventsResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "StartTimeRange": "StartTimeRangeTypeDef",
    },
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
        "EndTimeRange": "EndTimeRangeTypeDef",
    },
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef",
    {
        "Type": InsightTypeType,
    },
)

ListInsightsRequestRequestTypeDef = TypedDict(
    "ListInsightsRequestRequestTypeDef",
    {
        "StatusFilter": "ListInsightsStatusFilterTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInsightsResponseTypeDef = TypedDict(
    "ListInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": NotRequired["ListInsightsOngoingStatusFilterTypeDef"],
        "Closed": NotRequired["ListInsightsClosedStatusFilterTypeDef"],
        "Any": NotRequired["ListInsightsAnyStatusFilterTypeDef"],
    },
)

ListNotificationChannelsRequestRequestTypeDef = TypedDict(
    "ListNotificationChannelsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListNotificationChannelsResponseTypeDef = TypedDict(
    "ListNotificationChannelsResponseTypeDef",
    {
        "Channels": List["NotificationChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "ListOrganizationInsightsRequestRequestTypeDef",
    {
        "StatusFilter": "ListInsightsStatusFilterTypeDef",
        "MaxResults": NotRequired[int],
        "AccountIds": NotRequired[Sequence[str]],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

ListOrganizationInsightsResponseTypeDef = TypedDict(
    "ListOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveOrganizationInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveOrganizationInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "InsightId": str,
        "NextToken": NotRequired[str],
        "Locale": NotRequired[LocaleType],
        "AccountId": NotRequired[str],
    },
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "Recommendations": List["RecommendationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationChannelConfigTypeDef = TypedDict(
    "NotificationChannelConfigTypeDef",
    {
        "Sns": "SnsChannelConfigTypeDef",
    },
)

NotificationChannelTypeDef = TypedDict(
    "NotificationChannelTypeDef",
    {
        "Id": NotRequired[str],
        "Config": NotRequired["NotificationChannelConfigTypeDef"],
    },
)

OpsCenterIntegrationConfigTypeDef = TypedDict(
    "OpsCenterIntegrationConfigTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
    },
)

OpsCenterIntegrationTypeDef = TypedDict(
    "OpsCenterIntegrationTypeDef",
    {
        "OptInStatus": NotRequired[OptInStatusType],
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

PerformanceInsightsMetricDimensionGroupTypeDef = TypedDict(
    "PerformanceInsightsMetricDimensionGroupTypeDef",
    {
        "Group": NotRequired[str],
        "Dimensions": NotRequired[List[str]],
        "Limit": NotRequired[int],
    },
)

PerformanceInsightsMetricQueryTypeDef = TypedDict(
    "PerformanceInsightsMetricQueryTypeDef",
    {
        "Metric": NotRequired[str],
        "GroupBy": NotRequired["PerformanceInsightsMetricDimensionGroupTypeDef"],
        "Filter": NotRequired[Dict[str, str]],
    },
)

PerformanceInsightsMetricsDetailTypeDef = TypedDict(
    "PerformanceInsightsMetricsDetailTypeDef",
    {
        "MetricDisplayName": NotRequired[str],
        "Unit": NotRequired[str],
        "MetricQuery": NotRequired["PerformanceInsightsMetricQueryTypeDef"],
        "ReferenceData": NotRequired[List["PerformanceInsightsReferenceDataTypeDef"]],
        "StatsAtAnomaly": NotRequired[List["PerformanceInsightsStatTypeDef"]],
        "StatsAtBaseline": NotRequired[List["PerformanceInsightsStatTypeDef"]],
    },
)

PerformanceInsightsReferenceComparisonValuesTypeDef = TypedDict(
    "PerformanceInsightsReferenceComparisonValuesTypeDef",
    {
        "ReferenceScalar": NotRequired["PerformanceInsightsReferenceScalarTypeDef"],
        "ReferenceMetric": NotRequired["PerformanceInsightsReferenceMetricTypeDef"],
    },
)

PerformanceInsightsReferenceDataTypeDef = TypedDict(
    "PerformanceInsightsReferenceDataTypeDef",
    {
        "Name": NotRequired[str],
        "ComparisonValues": NotRequired["PerformanceInsightsReferenceComparisonValuesTypeDef"],
    },
)

PerformanceInsightsReferenceMetricTypeDef = TypedDict(
    "PerformanceInsightsReferenceMetricTypeDef",
    {
        "MetricQuery": NotRequired["PerformanceInsightsMetricQueryTypeDef"],
    },
)

PerformanceInsightsReferenceScalarTypeDef = TypedDict(
    "PerformanceInsightsReferenceScalarTypeDef",
    {
        "Value": NotRequired[float],
    },
)

PerformanceInsightsStatTypeDef = TypedDict(
    "PerformanceInsightsStatTypeDef",
    {
        "Type": NotRequired[str],
        "Value": NotRequired[float],
    },
)

PredictionTimeRangeTypeDef = TypedDict(
    "PredictionTimeRangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": NotRequired[datetime],
    },
)

ProactiveAnomalySummaryTypeDef = TypedDict(
    "ProactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired["AnomalyTimeRangeTypeDef"],
        "AnomalyReportedTimeRange": NotRequired["AnomalyReportedTimeRangeTypeDef"],
        "PredictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "SourceDetails": NotRequired["AnomalySourceDetailsTypeDef"],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired["AnomalySourceMetadataTypeDef"],
        "AnomalyResources": NotRequired[List["AnomalyResourceTypeDef"]],
    },
)

ProactiveAnomalyTypeDef = TypedDict(
    "ProactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "UpdateTime": NotRequired[datetime],
        "AnomalyTimeRange": NotRequired["AnomalyTimeRangeTypeDef"],
        "AnomalyReportedTimeRange": NotRequired["AnomalyReportedTimeRangeTypeDef"],
        "PredictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "SourceDetails": NotRequired["AnomalySourceDetailsTypeDef"],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "Limit": NotRequired[float],
        "SourceMetadata": NotRequired["AnomalySourceMetadataTypeDef"],
        "AnomalyResources": NotRequired[List["AnomalyResourceTypeDef"]],
    },
)

ProactiveInsightSummaryTypeDef = TypedDict(
    "ProactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "PredictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)

ProactiveInsightTypeDef = TypedDict(
    "ProactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "PredictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ProactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ProactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "PredictionTimeRange": NotRequired["PredictionTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
    },
)

PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "InsightFeedback": NotRequired["InsightFeedbackTypeDef"],
    },
)

ReactiveAnomalySummaryTypeDef = TypedDict(
    "ReactiveAnomalySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired["AnomalyTimeRangeTypeDef"],
        "AnomalyReportedTimeRange": NotRequired["AnomalyReportedTimeRangeTypeDef"],
        "SourceDetails": NotRequired["AnomalySourceDetailsTypeDef"],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List["AnomalyResourceTypeDef"]],
    },
)

ReactiveAnomalyTypeDef = TypedDict(
    "ReactiveAnomalyTypeDef",
    {
        "Id": NotRequired[str],
        "Severity": NotRequired[AnomalySeverityType],
        "Status": NotRequired[AnomalyStatusType],
        "AnomalyTimeRange": NotRequired["AnomalyTimeRangeTypeDef"],
        "AnomalyReportedTimeRange": NotRequired["AnomalyReportedTimeRangeTypeDef"],
        "SourceDetails": NotRequired["AnomalySourceDetailsTypeDef"],
        "AssociatedInsightId": NotRequired[str],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "Type": NotRequired[AnomalyTypeType],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CausalAnomalyId": NotRequired[str],
        "AnomalyResources": NotRequired[List["AnomalyResourceTypeDef"]],
    },
)

ReactiveInsightSummaryTypeDef = TypedDict(
    "ReactiveInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
        "AssociatedResourceArns": NotRequired[List[str]],
    },
)

ReactiveInsightTypeDef = TypedDict(
    "ReactiveInsightTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "SsmOpsItemId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ReactiveOrganizationInsightSummaryTypeDef = TypedDict(
    "ReactiveOrganizationInsightSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "AccountId": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "Name": NotRequired[str],
        "Severity": NotRequired[InsightSeverityType],
        "Status": NotRequired[InsightStatusType],
        "InsightTimeRange": NotRequired["InsightTimeRangeTypeDef"],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
    },
)

RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

RecommendationRelatedAnomalySourceDetailTypeDef = TypedDict(
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    {
        "CloudWatchMetrics": NotRequired[
            List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"]
        ],
    },
)

RecommendationRelatedAnomalyTypeDef = TypedDict(
    "RecommendationRelatedAnomalyTypeDef",
    {
        "Resources": NotRequired[List["RecommendationRelatedAnomalyResourceTypeDef"]],
        "SourceDetails": NotRequired[List["RecommendationRelatedAnomalySourceDetailTypeDef"]],
        "AnomalyId": NotRequired[str],
    },
)

RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef = TypedDict(
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    {
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)

RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[str],
    },
)

RecommendationRelatedEventTypeDef = TypedDict(
    "RecommendationRelatedEventTypeDef",
    {
        "Name": NotRequired[str],
        "Resources": NotRequired[List["RecommendationRelatedEventResourceTypeDef"]],
    },
)

RecommendationTypeDef = TypedDict(
    "RecommendationTypeDef",
    {
        "Description": NotRequired[str],
        "Link": NotRequired[str],
        "Name": NotRequired[str],
        "Reason": NotRequired[str],
        "RelatedEvents": NotRequired[List["RecommendationRelatedEventTypeDef"]],
        "RelatedAnomalies": NotRequired[List["RecommendationRelatedAnomalyTypeDef"]],
        "Category": NotRequired[str],
    },
)

RemoveNotificationChannelRequestRequestTypeDef = TypedDict(
    "RemoveNotificationChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

ResourceCollectionFilterTypeDef = TypedDict(
    "ResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired["CloudFormationCollectionFilterTypeDef"],
        "Tags": NotRequired[List["TagCollectionFilterTypeDef"]],
    },
)

ResourceCollectionTypeDef = TypedDict(
    "ResourceCollectionTypeDef",
    {
        "CloudFormation": NotRequired["CloudFormationCollectionTypeDef"],
        "Tags": NotRequired[List["TagCollectionTypeDef"]],
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

SearchInsightsFiltersTypeDef = TypedDict(
    "SearchInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
    },
)

SearchInsightsRequestRequestTypeDef = TypedDict(
    "SearchInsightsRequestRequestTypeDef",
    {
        "StartTimeRange": "StartTimeRangeTypeDef",
        "Type": InsightTypeType,
        "Filters": NotRequired["SearchInsightsFiltersTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchInsightsResponseTypeDef = TypedDict(
    "SearchInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchOrganizationInsightsFiltersTypeDef = TypedDict(
    "SearchOrganizationInsightsFiltersTypeDef",
    {
        "Severities": NotRequired[Sequence[InsightSeverityType]],
        "Statuses": NotRequired[Sequence[InsightStatusType]],
        "ResourceCollection": NotRequired["ResourceCollectionTypeDef"],
        "ServiceCollection": NotRequired["ServiceCollectionTypeDef"],
    },
)

SearchOrganizationInsightsRequestRequestTypeDef = TypedDict(
    "SearchOrganizationInsightsRequestRequestTypeDef",
    {
        "AccountIds": Sequence[str],
        "StartTimeRange": "StartTimeRangeTypeDef",
        "Type": InsightTypeType,
        "Filters": NotRequired["SearchOrganizationInsightsFiltersTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchOrganizationInsightsResponseTypeDef = TypedDict(
    "SearchOrganizationInsightsResponseTypeDef",
    {
        "ProactiveInsights": List["ProactiveInsightSummaryTypeDef"],
        "ReactiveInsights": List["ReactiveInsightSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceCollectionTypeDef = TypedDict(
    "ServiceCollectionTypeDef",
    {
        "ServiceNames": NotRequired[List[ServiceNameType]],
    },
)

ServiceHealthTypeDef = TypedDict(
    "ServiceHealthTypeDef",
    {
        "ServiceName": NotRequired[ServiceNameType],
        "Insight": NotRequired["ServiceInsightHealthTypeDef"],
    },
)

ServiceInsightHealthTypeDef = TypedDict(
    "ServiceInsightHealthTypeDef",
    {
        "OpenProactiveInsights": NotRequired[int],
        "OpenReactiveInsights": NotRequired[int],
    },
)

ServiceIntegrationConfigTypeDef = TypedDict(
    "ServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired["OpsCenterIntegrationTypeDef"],
    },
)

ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": NotRequired[str],
        "State": NotRequired[CostEstimationServiceResourceStateType],
        "Count": NotRequired[int],
        "UnitCost": NotRequired[float],
        "Cost": NotRequired[float],
    },
)

SnsChannelConfigTypeDef = TypedDict(
    "SnsChannelConfigTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)

StartCostEstimationRequestRequestTypeDef = TypedDict(
    "StartCostEstimationRequestRequestTypeDef",
    {
        "ResourceCollection": "CostEstimationResourceCollectionFilterTypeDef",
        "ClientToken": NotRequired[str],
    },
)

StartTimeRangeTypeDef = TypedDict(
    "StartTimeRangeTypeDef",
    {
        "FromTime": NotRequired[Union[datetime, str]],
        "ToTime": NotRequired[Union[datetime, str]],
    },
)

TagCollectionFilterTypeDef = TypedDict(
    "TagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagCollectionTypeDef = TypedDict(
    "TagCollectionTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagCostEstimationResourceCollectionFilterTypeDef = TypedDict(
    "TagCostEstimationResourceCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": List[str],
    },
)

TagHealthTypeDef = TypedDict(
    "TagHealthTypeDef",
    {
        "AppBoundaryKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "Insight": NotRequired["InsightHealthTypeDef"],
    },
)

TimestampMetricValuePairTypeDef = TypedDict(
    "TimestampMetricValuePairTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "MetricValue": NotRequired[float],
    },
)

UpdateCloudFormationCollectionFilterTypeDef = TypedDict(
    "UpdateCloudFormationCollectionFilterTypeDef",
    {
        "StackNames": NotRequired[Sequence[str]],
    },
)

UpdateEventSourcesConfigRequestRequestTypeDef = TypedDict(
    "UpdateEventSourcesConfigRequestRequestTypeDef",
    {
        "EventSources": NotRequired["EventSourcesConfigTypeDef"],
    },
)

UpdateResourceCollectionFilterTypeDef = TypedDict(
    "UpdateResourceCollectionFilterTypeDef",
    {
        "CloudFormation": NotRequired["UpdateCloudFormationCollectionFilterTypeDef"],
        "Tags": NotRequired[Sequence["UpdateTagCollectionFilterTypeDef"]],
    },
)

UpdateResourceCollectionRequestRequestTypeDef = TypedDict(
    "UpdateResourceCollectionRequestRequestTypeDef",
    {
        "Action": UpdateResourceCollectionActionType,
        "ResourceCollection": "UpdateResourceCollectionFilterTypeDef",
    },
)

UpdateServiceIntegrationConfigTypeDef = TypedDict(
    "UpdateServiceIntegrationConfigTypeDef",
    {
        "OpsCenter": NotRequired["OpsCenterIntegrationConfigTypeDef"],
    },
)

UpdateServiceIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateServiceIntegrationRequestRequestTypeDef",
    {
        "ServiceIntegration": "UpdateServiceIntegrationConfigTypeDef",
    },
)

UpdateTagCollectionFilterTypeDef = TypedDict(
    "UpdateTagCollectionFilterTypeDef",
    {
        "AppBoundaryKey": str,
        "TagValues": Sequence[str],
    },
)
