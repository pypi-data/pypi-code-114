"""
Type annotations for cloudwatch service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_cloudwatch/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AlarmTypeType,
    AnomalyDetectorStateValueType,
    AnomalyDetectorTypeType,
    ComparisonOperatorType,
    HistoryItemTypeType,
    MetricStreamOutputFormatType,
    ScanByType,
    StandardUnitType,
    StateValueType,
    StatisticType,
    StatusCodeType,
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
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteAlarmsInputRequestTypeDef",
    "DeleteAnomalyDetectorInputRequestTypeDef",
    "DeleteDashboardsInputRequestTypeDef",
    "DeleteInsightRulesInputRequestTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DeleteMetricStreamInputRequestTypeDef",
    "DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef",
    "DescribeAlarmHistoryInputRequestTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DescribeAlarmsForMetricInputRequestTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsInputRequestTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
    "DescribeInsightRulesInputRequestTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "DimensionFilterTypeDef",
    "DimensionTypeDef",
    "DisableAlarmActionsInputRequestTypeDef",
    "DisableInsightRulesInputRequestTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EnableAlarmActionsInputRequestTypeDef",
    "EnableInsightRulesInputRequestTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "GetDashboardInputRequestTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportInputRequestTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "GetMetricDataInputRequestTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetMetricStatisticsInputMetricGetStatisticsTypeDef",
    "GetMetricStatisticsInputRequestTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "GetMetricStreamInputRequestTypeDef",
    "GetMetricStreamOutputTypeDef",
    "GetMetricWidgetImageInputRequestTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsInputRequestTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListMetricStreamsInputRequestTypeDef",
    "ListMetricStreamsOutputTypeDef",
    "ListMetricsInputRequestTypeDef",
    "ListMetricsOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataResultTypeDef",
    "MetricDatumTypeDef",
    "MetricMathAnomalyDetectorTypeDef",
    "MetricStatTypeDef",
    "MetricStreamEntryTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricTypeDef",
    "PaginatorConfigTypeDef",
    "PartialFailureTypeDef",
    "PutAnomalyDetectorInputRequestTypeDef",
    "PutCompositeAlarmInputRequestTypeDef",
    "PutDashboardInputRequestTypeDef",
    "PutDashboardOutputTypeDef",
    "PutInsightRuleInputRequestTypeDef",
    "PutMetricAlarmInputMetricPutAlarmTypeDef",
    "PutMetricAlarmInputRequestTypeDef",
    "PutMetricDataInputRequestTypeDef",
    "PutMetricStreamInputRequestTypeDef",
    "PutMetricStreamOutputTypeDef",
    "RangeTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceResourceAlarmRequestTypeDef",
    "ServiceResourceMetricRequestTypeDef",
    "SetAlarmStateInputAlarmSetStateTypeDef",
    "SetAlarmStateInputRequestTypeDef",
    "SingleMetricAnomalyDetectorTypeDef",
    "StartMetricStreamsInputRequestTypeDef",
    "StatisticSetTypeDef",
    "StopMetricStreamsInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UntagResourceInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

AlarmHistoryItemTypeDef = TypedDict(
    "AlarmHistoryItemTypeDef",
    {
        "AlarmName": NotRequired[str],
        "AlarmType": NotRequired[AlarmTypeType],
        "Timestamp": NotRequired[datetime],
        "HistoryItemType": NotRequired[HistoryItemTypeType],
        "HistorySummary": NotRequired[str],
        "HistoryData": NotRequired[str],
    },
)

AnomalyDetectorConfigurationTypeDef = TypedDict(
    "AnomalyDetectorConfigurationTypeDef",
    {
        "ExcludedTimeRanges": NotRequired[List["RangeTypeDef"]],
        "MetricTimezone": NotRequired[str],
    },
)

AnomalyDetectorTypeDef = TypedDict(
    "AnomalyDetectorTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[List["DimensionTypeDef"]],
        "Stat": NotRequired[str],
        "Configuration": NotRequired["AnomalyDetectorConfigurationTypeDef"],
        "StateValue": NotRequired[AnomalyDetectorStateValueType],
        "SingleMetricAnomalyDetector": NotRequired["SingleMetricAnomalyDetectorTypeDef"],
        "MetricMathAnomalyDetector": NotRequired["MetricMathAnomalyDetectorTypeDef"],
    },
)

CompositeAlarmTypeDef = TypedDict(
    "CompositeAlarmTypeDef",
    {
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[List[str]],
        "AlarmArn": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[datetime],
        "AlarmDescription": NotRequired[str],
        "AlarmName": NotRequired[str],
        "AlarmRule": NotRequired[str],
        "InsufficientDataActions": NotRequired[List[str]],
        "OKActions": NotRequired[List[str]],
        "StateReason": NotRequired[str],
        "StateReasonData": NotRequired[str],
        "StateUpdatedTimestamp": NotRequired[datetime],
        "StateValue": NotRequired[StateValueType],
    },
)

DashboardEntryTypeDef = TypedDict(
    "DashboardEntryTypeDef",
    {
        "DashboardName": NotRequired[str],
        "DashboardArn": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "Size": NotRequired[int],
    },
)

DashboardValidationMessageTypeDef = TypedDict(
    "DashboardValidationMessageTypeDef",
    {
        "DataPath": NotRequired[str],
        "Message": NotRequired[str],
    },
)

DatapointTypeDef = TypedDict(
    "DatapointTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "SampleCount": NotRequired[float],
        "Average": NotRequired[float],
        "Sum": NotRequired[float],
        "Minimum": NotRequired[float],
        "Maximum": NotRequired[float],
        "Unit": NotRequired[StandardUnitType],
        "ExtendedStatistics": NotRequired[Dict[str, float]],
    },
)

DeleteAlarmsInputRequestTypeDef = TypedDict(
    "DeleteAlarmsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

DeleteAnomalyDetectorInputRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Stat": NotRequired[str],
        "SingleMetricAnomalyDetector": NotRequired["SingleMetricAnomalyDetectorTypeDef"],
        "MetricMathAnomalyDetector": NotRequired["MetricMathAnomalyDetectorTypeDef"],
    },
)

DeleteDashboardsInputRequestTypeDef = TypedDict(
    "DeleteDashboardsInputRequestTypeDef",
    {
        "DashboardNames": Sequence[str],
    },
)

DeleteInsightRulesInputRequestTypeDef = TypedDict(
    "DeleteInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

DeleteInsightRulesOutputTypeDef = TypedDict(
    "DeleteInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMetricStreamInputRequestTypeDef = TypedDict(
    "DeleteMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef = TypedDict(
    "DescribeAlarmHistoryInputAlarmDescribeHistoryTypeDef",
    {
        "AlarmTypes": NotRequired[Sequence[AlarmTypeType]],
        "HistoryItemType": NotRequired[HistoryItemTypeType],
        "StartDate": NotRequired[Union[datetime, str]],
        "EndDate": NotRequired[Union[datetime, str]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScanBy": NotRequired[ScanByType],
    },
)

DescribeAlarmHistoryInputRequestTypeDef = TypedDict(
    "DescribeAlarmHistoryInputRequestTypeDef",
    {
        "AlarmName": NotRequired[str],
        "AlarmTypes": NotRequired[Sequence[AlarmTypeType]],
        "HistoryItemType": NotRequired[HistoryItemTypeType],
        "StartDate": NotRequired[Union[datetime, str]],
        "EndDate": NotRequired[Union[datetime, str]],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScanBy": NotRequired[ScanByType],
    },
)

DescribeAlarmHistoryOutputTypeDef = TypedDict(
    "DescribeAlarmHistoryOutputTypeDef",
    {
        "AlarmHistoryItems": List["AlarmHistoryItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsForMetricInputRequestTypeDef = TypedDict(
    "DescribeAlarmsForMetricInputRequestTypeDef",
    {
        "MetricName": str,
        "Namespace": str,
        "Statistic": NotRequired[StatisticType],
        "ExtendedStatistic": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Period": NotRequired[int],
        "Unit": NotRequired[StandardUnitType],
    },
)

DescribeAlarmsForMetricOutputTypeDef = TypedDict(
    "DescribeAlarmsForMetricOutputTypeDef",
    {
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAlarmsInputRequestTypeDef = TypedDict(
    "DescribeAlarmsInputRequestTypeDef",
    {
        "AlarmNames": NotRequired[Sequence[str]],
        "AlarmNamePrefix": NotRequired[str],
        "AlarmTypes": NotRequired[Sequence[AlarmTypeType]],
        "ChildrenOfAlarmName": NotRequired[str],
        "ParentsOfAlarmName": NotRequired[str],
        "StateValue": NotRequired[StateValueType],
        "ActionPrefix": NotRequired[str],
        "MaxRecords": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAlarmsOutputTypeDef = TypedDict(
    "DescribeAlarmsOutputTypeDef",
    {
        "CompositeAlarms": List["CompositeAlarmTypeDef"],
        "MetricAlarms": List["MetricAlarmTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorsInputRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "AnomalyDetectorTypes": NotRequired[Sequence[AnomalyDetectorTypeType]],
    },
)

DescribeAnomalyDetectorsOutputTypeDef = TypedDict(
    "DescribeAnomalyDetectorsOutputTypeDef",
    {
        "AnomalyDetectors": List["AnomalyDetectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInsightRulesInputRequestTypeDef = TypedDict(
    "DescribeInsightRulesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeInsightRulesOutputTypeDef = TypedDict(
    "DescribeInsightRulesOutputTypeDef",
    {
        "NextToken": str,
        "InsightRules": List["InsightRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionFilterTypeDef = TypedDict(
    "DimensionFilterTypeDef",
    {
        "Name": str,
        "Value": NotRequired[str],
    },
)

DimensionTypeDef = TypedDict(
    "DimensionTypeDef",
    {
        "Name": str,
        "Value": str,
    },
)

DisableAlarmActionsInputRequestTypeDef = TypedDict(
    "DisableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

DisableInsightRulesInputRequestTypeDef = TypedDict(
    "DisableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

DisableInsightRulesOutputTypeDef = TypedDict(
    "DisableInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAlarmActionsInputRequestTypeDef = TypedDict(
    "EnableAlarmActionsInputRequestTypeDef",
    {
        "AlarmNames": Sequence[str],
    },
)

EnableInsightRulesInputRequestTypeDef = TypedDict(
    "EnableInsightRulesInputRequestTypeDef",
    {
        "RuleNames": Sequence[str],
    },
)

EnableInsightRulesOutputTypeDef = TypedDict(
    "EnableInsightRulesOutputTypeDef",
    {
        "Failures": List["PartialFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDashboardInputRequestTypeDef = TypedDict(
    "GetDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
    },
)

GetDashboardOutputTypeDef = TypedDict(
    "GetDashboardOutputTypeDef",
    {
        "DashboardArn": str,
        "DashboardBody": str,
        "DashboardName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightRuleReportInputRequestTypeDef = TypedDict(
    "GetInsightRuleReportInputRequestTypeDef",
    {
        "RuleName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
        "MaxContributorCount": NotRequired[int],
        "Metrics": NotRequired[Sequence[str]],
        "OrderBy": NotRequired[str],
    },
)

GetInsightRuleReportOutputTypeDef = TypedDict(
    "GetInsightRuleReportOutputTypeDef",
    {
        "KeyLabels": List[str],
        "AggregationStatistic": str,
        "AggregateValue": float,
        "ApproximateUniqueCount": int,
        "Contributors": List["InsightRuleContributorTypeDef"],
        "MetricDatapoints": List["InsightRuleMetricDatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricDataInputRequestTypeDef = TypedDict(
    "GetMetricDataInputRequestTypeDef",
    {
        "MetricDataQueries": Sequence["MetricDataQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "NextToken": NotRequired[str],
        "ScanBy": NotRequired[ScanByType],
        "MaxDatapoints": NotRequired[int],
        "LabelOptions": NotRequired["LabelOptionsTypeDef"],
    },
)

GetMetricDataOutputTypeDef = TypedDict(
    "GetMetricDataOutputTypeDef",
    {
        "MetricDataResults": List["MetricDataResultTypeDef"],
        "NextToken": str,
        "Messages": List["MessageDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricStatisticsInputMetricGetStatisticsTypeDef = TypedDict(
    "GetMetricStatisticsInputMetricGetStatisticsTypeDef",
    {
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Statistics": NotRequired[Sequence[StatisticType]],
        "ExtendedStatistics": NotRequired[Sequence[str]],
        "Unit": NotRequired[StandardUnitType],
    },
)

GetMetricStatisticsInputRequestTypeDef = TypedDict(
    "GetMetricStatisticsInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricName": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "Period": int,
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Statistics": NotRequired[Sequence[StatisticType]],
        "ExtendedStatistics": NotRequired[Sequence[str]],
        "Unit": NotRequired[StandardUnitType],
    },
)

GetMetricStatisticsOutputTypeDef = TypedDict(
    "GetMetricStatisticsOutputTypeDef",
    {
        "Label": str,
        "Datapoints": List["DatapointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricStreamInputRequestTypeDef = TypedDict(
    "GetMetricStreamInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetMetricStreamOutputTypeDef = TypedDict(
    "GetMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "Name": str,
        "IncludeFilters": List["MetricStreamFilterTypeDef"],
        "ExcludeFilters": List["MetricStreamFilterTypeDef"],
        "FirehoseArn": str,
        "RoleArn": str,
        "State": str,
        "CreationDate": datetime,
        "LastUpdateDate": datetime,
        "OutputFormat": MetricStreamOutputFormatType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMetricWidgetImageInputRequestTypeDef = TypedDict(
    "GetMetricWidgetImageInputRequestTypeDef",
    {
        "MetricWidget": str,
        "OutputFormat": NotRequired[str],
    },
)

GetMetricWidgetImageOutputTypeDef = TypedDict(
    "GetMetricWidgetImageOutputTypeDef",
    {
        "MetricWidgetImage": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightRuleContributorDatapointTypeDef = TypedDict(
    "InsightRuleContributorDatapointTypeDef",
    {
        "Timestamp": datetime,
        "ApproximateValue": float,
    },
)

InsightRuleContributorTypeDef = TypedDict(
    "InsightRuleContributorTypeDef",
    {
        "Keys": List[str],
        "ApproximateAggregateValue": float,
        "Datapoints": List["InsightRuleContributorDatapointTypeDef"],
    },
)

InsightRuleMetricDatapointTypeDef = TypedDict(
    "InsightRuleMetricDatapointTypeDef",
    {
        "Timestamp": datetime,
        "UniqueContributors": NotRequired[float],
        "MaxContributorValue": NotRequired[float],
        "SampleCount": NotRequired[float],
        "Average": NotRequired[float],
        "Sum": NotRequired[float],
        "Minimum": NotRequired[float],
        "Maximum": NotRequired[float],
    },
)

InsightRuleTypeDef = TypedDict(
    "InsightRuleTypeDef",
    {
        "Name": str,
        "State": str,
        "Schema": str,
        "Definition": str,
    },
)

LabelOptionsTypeDef = TypedDict(
    "LabelOptionsTypeDef",
    {
        "Timezone": NotRequired[str],
    },
)

ListDashboardsInputRequestTypeDef = TypedDict(
    "ListDashboardsInputRequestTypeDef",
    {
        "DashboardNamePrefix": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

ListDashboardsOutputTypeDef = TypedDict(
    "ListDashboardsOutputTypeDef",
    {
        "DashboardEntries": List["DashboardEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricStreamsInputRequestTypeDef = TypedDict(
    "ListMetricStreamsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMetricStreamsOutputTypeDef = TypedDict(
    "ListMetricStreamsOutputTypeDef",
    {
        "NextToken": str,
        "Entries": List["MetricStreamEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricsInputRequestTypeDef = TypedDict(
    "ListMetricsInputRequestTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "RecentlyActive": NotRequired[Literal["PT3H"]],
    },
)

ListMetricsOutputTypeDef = TypedDict(
    "ListMetricsOutputTypeDef",
    {
        "Metrics": List["MetricTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageDataTypeDef = TypedDict(
    "MessageDataTypeDef",
    {
        "Code": NotRequired[str],
        "Value": NotRequired[str],
    },
)

MetricAlarmTypeDef = TypedDict(
    "MetricAlarmTypeDef",
    {
        "AlarmName": NotRequired[str],
        "AlarmArn": NotRequired[str],
        "AlarmDescription": NotRequired[str],
        "AlarmConfigurationUpdatedTimestamp": NotRequired[datetime],
        "ActionsEnabled": NotRequired[bool],
        "OKActions": NotRequired[List[str]],
        "AlarmActions": NotRequired[List[str]],
        "InsufficientDataActions": NotRequired[List[str]],
        "StateValue": NotRequired[StateValueType],
        "StateReason": NotRequired[str],
        "StateReasonData": NotRequired[str],
        "StateUpdatedTimestamp": NotRequired[datetime],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Statistic": NotRequired[StatisticType],
        "ExtendedStatistic": NotRequired[str],
        "Dimensions": NotRequired[List["DimensionTypeDef"]],
        "Period": NotRequired[int],
        "Unit": NotRequired[StandardUnitType],
        "EvaluationPeriods": NotRequired[int],
        "DatapointsToAlarm": NotRequired[int],
        "Threshold": NotRequired[float],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "TreatMissingData": NotRequired[str],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "Metrics": NotRequired[List["MetricDataQueryTypeDef"]],
        "ThresholdMetricId": NotRequired[str],
    },
)

MetricDataQueryTypeDef = TypedDict(
    "MetricDataQueryTypeDef",
    {
        "Id": str,
        "MetricStat": NotRequired["MetricStatTypeDef"],
        "Expression": NotRequired[str],
        "Label": NotRequired[str],
        "ReturnData": NotRequired[bool],
        "Period": NotRequired[int],
        "AccountId": NotRequired[str],
    },
)

MetricDataResultTypeDef = TypedDict(
    "MetricDataResultTypeDef",
    {
        "Id": NotRequired[str],
        "Label": NotRequired[str],
        "Timestamps": NotRequired[List[datetime]],
        "Values": NotRequired[List[float]],
        "StatusCode": NotRequired[StatusCodeType],
        "Messages": NotRequired[List["MessageDataTypeDef"]],
    },
)

MetricDatumTypeDef = TypedDict(
    "MetricDatumTypeDef",
    {
        "MetricName": str,
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Timestamp": NotRequired[Union[datetime, str]],
        "Value": NotRequired[float],
        "StatisticValues": NotRequired["StatisticSetTypeDef"],
        "Values": NotRequired[Sequence[float]],
        "Counts": NotRequired[Sequence[float]],
        "Unit": NotRequired[StandardUnitType],
        "StorageResolution": NotRequired[int],
    },
)

MetricMathAnomalyDetectorTypeDef = TypedDict(
    "MetricMathAnomalyDetectorTypeDef",
    {
        "MetricDataQueries": NotRequired[Sequence["MetricDataQueryTypeDef"]],
    },
)

MetricStatTypeDef = TypedDict(
    "MetricStatTypeDef",
    {
        "Metric": "MetricTypeDef",
        "Period": int,
        "Stat": str,
        "Unit": NotRequired[StandardUnitType],
    },
)

MetricStreamEntryTypeDef = TypedDict(
    "MetricStreamEntryTypeDef",
    {
        "Arn": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "LastUpdateDate": NotRequired[datetime],
        "Name": NotRequired[str],
        "FirehoseArn": NotRequired[str],
        "State": NotRequired[str],
        "OutputFormat": NotRequired[MetricStreamOutputFormatType],
    },
)

MetricStreamFilterTypeDef = TypedDict(
    "MetricStreamFilterTypeDef",
    {
        "Namespace": NotRequired[str],
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
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

PartialFailureTypeDef = TypedDict(
    "PartialFailureTypeDef",
    {
        "FailureResource": NotRequired[str],
        "ExceptionType": NotRequired[str],
        "FailureCode": NotRequired[str],
        "FailureDescription": NotRequired[str],
    },
)

PutAnomalyDetectorInputRequestTypeDef = TypedDict(
    "PutAnomalyDetectorInputRequestTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Stat": NotRequired[str],
        "Configuration": NotRequired["AnomalyDetectorConfigurationTypeDef"],
        "SingleMetricAnomalyDetector": NotRequired["SingleMetricAnomalyDetectorTypeDef"],
        "MetricMathAnomalyDetector": NotRequired["MetricMathAnomalyDetectorTypeDef"],
    },
)

PutCompositeAlarmInputRequestTypeDef = TypedDict(
    "PutCompositeAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "AlarmRule": str,
        "ActionsEnabled": NotRequired[bool],
        "AlarmActions": NotRequired[Sequence[str]],
        "AlarmDescription": NotRequired[str],
        "InsufficientDataActions": NotRequired[Sequence[str]],
        "OKActions": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutDashboardInputRequestTypeDef = TypedDict(
    "PutDashboardInputRequestTypeDef",
    {
        "DashboardName": str,
        "DashboardBody": str,
    },
)

PutDashboardOutputTypeDef = TypedDict(
    "PutDashboardOutputTypeDef",
    {
        "DashboardValidationMessages": List["DashboardValidationMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInsightRuleInputRequestTypeDef = TypedDict(
    "PutInsightRuleInputRequestTypeDef",
    {
        "RuleName": str,
        "RuleDefinition": str,
        "RuleState": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutMetricAlarmInputMetricPutAlarmTypeDef = TypedDict(
    "PutMetricAlarmInputMetricPutAlarmTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
        "AlarmDescription": NotRequired[str],
        "ActionsEnabled": NotRequired[bool],
        "OKActions": NotRequired[Sequence[str]],
        "AlarmActions": NotRequired[Sequence[str]],
        "InsufficientDataActions": NotRequired[Sequence[str]],
        "Statistic": NotRequired[StatisticType],
        "ExtendedStatistic": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Period": NotRequired[int],
        "Unit": NotRequired[StandardUnitType],
        "DatapointsToAlarm": NotRequired[int],
        "Threshold": NotRequired[float],
        "TreatMissingData": NotRequired[str],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "Metrics": NotRequired[Sequence["MetricDataQueryTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ThresholdMetricId": NotRequired[str],
    },
)

PutMetricAlarmInputRequestTypeDef = TypedDict(
    "PutMetricAlarmInputRequestTypeDef",
    {
        "AlarmName": str,
        "EvaluationPeriods": int,
        "ComparisonOperator": ComparisonOperatorType,
        "AlarmDescription": NotRequired[str],
        "ActionsEnabled": NotRequired[bool],
        "OKActions": NotRequired[Sequence[str]],
        "AlarmActions": NotRequired[Sequence[str]],
        "InsufficientDataActions": NotRequired[Sequence[str]],
        "MetricName": NotRequired[str],
        "Namespace": NotRequired[str],
        "Statistic": NotRequired[StatisticType],
        "ExtendedStatistic": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Period": NotRequired[int],
        "Unit": NotRequired[StandardUnitType],
        "DatapointsToAlarm": NotRequired[int],
        "Threshold": NotRequired[float],
        "TreatMissingData": NotRequired[str],
        "EvaluateLowSampleCountPercentile": NotRequired[str],
        "Metrics": NotRequired[Sequence["MetricDataQueryTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ThresholdMetricId": NotRequired[str],
    },
)

PutMetricDataInputRequestTypeDef = TypedDict(
    "PutMetricDataInputRequestTypeDef",
    {
        "Namespace": str,
        "MetricData": Sequence["MetricDatumTypeDef"],
    },
)

PutMetricStreamInputRequestTypeDef = TypedDict(
    "PutMetricStreamInputRequestTypeDef",
    {
        "Name": str,
        "FirehoseArn": str,
        "RoleArn": str,
        "OutputFormat": MetricStreamOutputFormatType,
        "IncludeFilters": NotRequired[Sequence["MetricStreamFilterTypeDef"]],
        "ExcludeFilters": NotRequired[Sequence["MetricStreamFilterTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

PutMetricStreamOutputTypeDef = TypedDict(
    "PutMetricStreamOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RangeTypeDef = TypedDict(
    "RangeTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
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

ServiceResourceAlarmRequestTypeDef = TypedDict(
    "ServiceResourceAlarmRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceMetricRequestTypeDef = TypedDict(
    "ServiceResourceMetricRequestTypeDef",
    {
        "namespace": str,
        "name": str,
    },
)

SetAlarmStateInputAlarmSetStateTypeDef = TypedDict(
    "SetAlarmStateInputAlarmSetStateTypeDef",
    {
        "StateValue": StateValueType,
        "StateReason": str,
        "StateReasonData": NotRequired[str],
    },
)

SetAlarmStateInputRequestTypeDef = TypedDict(
    "SetAlarmStateInputRequestTypeDef",
    {
        "AlarmName": str,
        "StateValue": StateValueType,
        "StateReason": str,
        "StateReasonData": NotRequired[str],
    },
)

SingleMetricAnomalyDetectorTypeDef = TypedDict(
    "SingleMetricAnomalyDetectorTypeDef",
    {
        "Namespace": NotRequired[str],
        "MetricName": NotRequired[str],
        "Dimensions": NotRequired[Sequence["DimensionTypeDef"]],
        "Stat": NotRequired[str],
    },
)

StartMetricStreamsInputRequestTypeDef = TypedDict(
    "StartMetricStreamsInputRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)

StatisticSetTypeDef = TypedDict(
    "StatisticSetTypeDef",
    {
        "SampleCount": float,
        "Sum": float,
        "Minimum": float,
        "Maximum": float,
    },
)

StopMetricStreamsInputRequestTypeDef = TypedDict(
    "StopMetricStreamsInputRequestTypeDef",
    {
        "Names": Sequence[str],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
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

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
