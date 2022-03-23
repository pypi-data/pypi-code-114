"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutmetrics/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_lookoutmetrics.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AggregationFunctionType,
    AlertStatusType,
    AlertTypeType,
    AnomalyDetectionTaskStatusType,
    AnomalyDetectorFailureTypeType,
    AnomalyDetectorStatusType,
    CSVFileCompressionType,
    FrequencyType,
    JsonFileCompressionType,
    RelationshipTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    "AlertSummaryTypeDef",
    "AlertTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AnomalyGroupTypeDef",
    "AppFlowConfigTypeDef",
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    "CloudWatchConfigTypeDef",
    "ContributionMatrixTypeDef",
    "CreateAlertRequestRequestTypeDef",
    "CreateAlertResponseTypeDef",
    "CreateAnomalyDetectorRequestRequestTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateMetricSetRequestRequestTypeDef",
    "CreateMetricSetResponseTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    "DeleteAlertRequestRequestTypeDef",
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    "DescribeAlertRequestRequestTypeDef",
    "DescribeAlertResponseTypeDef",
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "DescribeMetricSetRequestRequestTypeDef",
    "DescribeMetricSetResponseTypeDef",
    "DimensionContributionTypeDef",
    "DimensionNameValueTypeDef",
    "DimensionValueContributionTypeDef",
    "ExecutionStatusTypeDef",
    "FileFormatDescriptorTypeDef",
    "GetAnomalyGroupRequestRequestTypeDef",
    "GetAnomalyGroupResponseTypeDef",
    "GetFeedbackRequestRequestTypeDef",
    "GetFeedbackResponseTypeDef",
    "GetSampleDataRequestRequestTypeDef",
    "GetSampleDataResponseTypeDef",
    "InterMetricImpactDetailsTypeDef",
    "ItemizedMetricStatsTypeDef",
    "JsonFormatDescriptorTypeDef",
    "LambdaConfigurationTypeDef",
    "ListAlertsRequestRequestTypeDef",
    "ListAlertsResponseTypeDef",
    "ListAnomalyDetectorsRequestRequestTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    "ListAnomalyGroupSummariesResponseTypeDef",
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    "ListMetricSetsRequestRequestTypeDef",
    "ListMetricSetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSetSummaryTypeDef",
    "MetricSourceTypeDef",
    "MetricTypeDef",
    "PutFeedbackRequestRequestTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "ResponseMetadataTypeDef",
    "S3SourceConfigTypeDef",
    "SNSConfigurationTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "TimeSeriesTypeDef",
    "TimestampColumnTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    "UpdateAnomalyDetectorResponseTypeDef",
    "UpdateMetricSetRequestRequestTypeDef",
    "UpdateMetricSetResponseTypeDef",
    "VpcConfigurationTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "SNSConfiguration": NotRequired["SNSConfigurationTypeDef"],
        "LambdaConfiguration": NotRequired["LambdaConfigurationTypeDef"],
    },
)

ActivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "ActivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

AlertSummaryTypeDef = TypedDict(
    "AlertSummaryTypeDef",
    {
        "AlertArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "AlertName": NotRequired[str],
        "AlertSensitivityThreshold": NotRequired[int],
        "AlertType": NotRequired[AlertTypeType],
        "AlertStatus": NotRequired[AlertStatusType],
        "LastModificationTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)

AlertTypeDef = TypedDict(
    "AlertTypeDef",
    {
        "Action": NotRequired["ActionTypeDef"],
        "AlertDescription": NotRequired[str],
        "AlertArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "AlertName": NotRequired[str],
        "AlertSensitivityThreshold": NotRequired[int],
        "AlertType": NotRequired[AlertTypeType],
        "AlertStatus": NotRequired[AlertStatusType],
        "LastModificationTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)

AnomalyDetectorConfigSummaryTypeDef = TypedDict(
    "AnomalyDetectorConfigSummaryTypeDef",
    {
        "AnomalyDetectorFrequency": NotRequired[FrequencyType],
    },
)

AnomalyDetectorConfigTypeDef = TypedDict(
    "AnomalyDetectorConfigTypeDef",
    {
        "AnomalyDetectorFrequency": NotRequired[FrequencyType],
    },
)

AnomalyDetectorSummaryTypeDef = TypedDict(
    "AnomalyDetectorSummaryTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "AnomalyDetectorName": NotRequired[str],
        "AnomalyDetectorDescription": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
        "Status": NotRequired[AnomalyDetectorStatusType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

AnomalyGroupStatisticsTypeDef = TypedDict(
    "AnomalyGroupStatisticsTypeDef",
    {
        "EvaluationStartDate": NotRequired[str],
        "TotalCount": NotRequired[int],
        "ItemizedMetricStatsList": NotRequired[List["ItemizedMetricStatsTypeDef"]],
    },
)

AnomalyGroupSummaryTypeDef = TypedDict(
    "AnomalyGroupSummaryTypeDef",
    {
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "AnomalyGroupScore": NotRequired[float],
        "PrimaryMetricName": NotRequired[str],
    },
)

AnomalyGroupTimeSeriesFeedbackTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": str,
        "IsAnomaly": bool,
    },
)

AnomalyGroupTimeSeriesTypeDef = TypedDict(
    "AnomalyGroupTimeSeriesTypeDef",
    {
        "AnomalyGroupId": str,
        "TimeSeriesId": NotRequired[str],
    },
)

AnomalyGroupTypeDef = TypedDict(
    "AnomalyGroupTypeDef",
    {
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "AnomalyGroupScore": NotRequired[float],
        "PrimaryMetricName": NotRequired[str],
        "MetricLevelImpactList": NotRequired[List["MetricLevelImpactTypeDef"]],
    },
)

AppFlowConfigTypeDef = TypedDict(
    "AppFlowConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "FlowName": NotRequired[str],
    },
)

BackTestAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "BackTestAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

CloudWatchConfigTypeDef = TypedDict(
    "CloudWatchConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
    },
)

ContributionMatrixTypeDef = TypedDict(
    "ContributionMatrixTypeDef",
    {
        "DimensionContributionList": NotRequired[List["DimensionContributionTypeDef"]],
    },
)

CreateAlertRequestRequestTypeDef = TypedDict(
    "CreateAlertRequestRequestTypeDef",
    {
        "AlertName": str,
        "AlertSensitivityThreshold": int,
        "AnomalyDetectorArn": str,
        "Action": "ActionTypeDef",
        "AlertDescription": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAlertResponseTypeDef = TypedDict(
    "CreateAlertResponseTypeDef",
    {
        "AlertArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "CreateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorName": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigTypeDef",
        "AnomalyDetectorDescription": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAnomalyDetectorResponseTypeDef = TypedDict(
    "CreateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMetricSetRequestRequestTypeDef = TypedDict(
    "CreateMetricSetRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricList": Sequence["MetricTypeDef"],
        "MetricSource": "MetricSourceTypeDef",
        "MetricSetDescription": NotRequired[str],
        "Offset": NotRequired[int],
        "TimestampColumn": NotRequired["TimestampColumnTypeDef"],
        "DimensionList": NotRequired[Sequence[str]],
        "MetricSetFrequency": NotRequired[FrequencyType],
        "Timezone": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateMetricSetResponseTypeDef = TypedDict(
    "CreateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvFormatDescriptorTypeDef = TypedDict(
    "CsvFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[CSVFileCompressionType],
        "Charset": NotRequired[str],
        "ContainsHeader": NotRequired[bool],
        "Delimiter": NotRequired[str],
        "HeaderList": NotRequired[Sequence[str]],
        "QuoteSymbol": NotRequired[str],
    },
)

DeactivateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeactivateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DeleteAlertRequestRequestTypeDef = TypedDict(
    "DeleteAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DeleteAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DeleteAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAlertRequestRequestTypeDef = TypedDict(
    "DescribeAlertRequestRequestTypeDef",
    {
        "AlertArn": str,
    },
)

DescribeAlertResponseTypeDef = TypedDict(
    "DescribeAlertResponseTypeDef",
    {
        "Alert": "AlertTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectionExecutionsRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "Timestamp": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeAnomalyDetectionExecutionsResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    {
        "ExecutionList": List["ExecutionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "DescribeAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
    },
)

DescribeAnomalyDetectorResponseTypeDef = TypedDict(
    "DescribeAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyDetectorName": str,
        "AnomalyDetectorDescription": str,
        "AnomalyDetectorConfig": "AnomalyDetectorConfigSummaryTypeDef",
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Status": AnomalyDetectorStatusType,
        "FailureReason": str,
        "KmsKeyArn": str,
        "FailureType": AnomalyDetectorFailureTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricSetRequestRequestTypeDef = TypedDict(
    "DescribeMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
    },
)

DescribeMetricSetResponseTypeDef = TypedDict(
    "DescribeMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "AnomalyDetectorArn": str,
        "MetricSetName": str,
        "MetricSetDescription": str,
        "CreationTime": datetime,
        "LastModificationTime": datetime,
        "Offset": int,
        "MetricList": List["MetricTypeDef"],
        "TimestampColumn": "TimestampColumnTypeDef",
        "DimensionList": List[str],
        "MetricSetFrequency": FrequencyType,
        "Timezone": str,
        "MetricSource": "MetricSourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionContributionTypeDef = TypedDict(
    "DimensionContributionTypeDef",
    {
        "DimensionName": NotRequired[str],
        "DimensionValueContributionList": NotRequired[List["DimensionValueContributionTypeDef"]],
    },
)

DimensionNameValueTypeDef = TypedDict(
    "DimensionNameValueTypeDef",
    {
        "DimensionName": str,
        "DimensionValue": str,
    },
)

DimensionValueContributionTypeDef = TypedDict(
    "DimensionValueContributionTypeDef",
    {
        "DimensionValue": NotRequired[str],
        "ContributionScore": NotRequired[float],
    },
)

ExecutionStatusTypeDef = TypedDict(
    "ExecutionStatusTypeDef",
    {
        "Timestamp": NotRequired[str],
        "Status": NotRequired[AnomalyDetectionTaskStatusType],
        "FailureReason": NotRequired[str],
    },
)

FileFormatDescriptorTypeDef = TypedDict(
    "FileFormatDescriptorTypeDef",
    {
        "CsvFormatDescriptor": NotRequired["CsvFormatDescriptorTypeDef"],
        "JsonFormatDescriptor": NotRequired["JsonFormatDescriptorTypeDef"],
    },
)

GetAnomalyGroupRequestRequestTypeDef = TypedDict(
    "GetAnomalyGroupRequestRequestTypeDef",
    {
        "AnomalyGroupId": str,
        "AnomalyDetectorArn": str,
    },
)

GetAnomalyGroupResponseTypeDef = TypedDict(
    "GetAnomalyGroupResponseTypeDef",
    {
        "AnomalyGroup": "AnomalyGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFeedbackRequestRequestTypeDef = TypedDict(
    "GetFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetFeedbackResponseTypeDef = TypedDict(
    "GetFeedbackResponseTypeDef",
    {
        "AnomalyGroupTimeSeriesFeedback": List["TimeSeriesFeedbackTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSampleDataRequestRequestTypeDef = TypedDict(
    "GetSampleDataRequestRequestTypeDef",
    {
        "S3SourceConfig": NotRequired["SampleDataS3SourceConfigTypeDef"],
    },
)

GetSampleDataResponseTypeDef = TypedDict(
    "GetSampleDataResponseTypeDef",
    {
        "HeaderValues": List[str],
        "SampleRows": List[List[str]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterMetricImpactDetailsTypeDef = TypedDict(
    "InterMetricImpactDetailsTypeDef",
    {
        "MetricName": NotRequired[str],
        "AnomalyGroupId": NotRequired[str],
        "RelationshipType": NotRequired[RelationshipTypeType],
        "ContributionPercentage": NotRequired[float],
    },
)

ItemizedMetricStatsTypeDef = TypedDict(
    "ItemizedMetricStatsTypeDef",
    {
        "MetricName": NotRequired[str],
        "OccurrenceCount": NotRequired[int],
    },
)

JsonFormatDescriptorTypeDef = TypedDict(
    "JsonFormatDescriptorTypeDef",
    {
        "FileCompression": NotRequired[JsonFileCompressionType],
        "Charset": NotRequired[str],
    },
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "RoleArn": str,
        "LambdaArn": str,
    },
)

ListAlertsRequestRequestTypeDef = TypedDict(
    "ListAlertsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAlertsResponseTypeDef = TypedDict(
    "ListAlertsResponseTypeDef",
    {
        "AlertSummaryList": List["AlertSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyDetectorsRequestRequestTypeDef = TypedDict(
    "ListAnomalyDetectorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAnomalyDetectorsResponseTypeDef = TypedDict(
    "ListAnomalyDetectorsResponseTypeDef",
    {
        "AnomalyDetectorSummaryList": List["AnomalyDetectorSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyGroupRelatedMetricsRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "RelationshipTypeFilter": NotRequired[RelationshipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAnomalyGroupRelatedMetricsResponseTypeDef = TypedDict(
    "ListAnomalyGroupRelatedMetricsResponseTypeDef",
    {
        "InterMetricImpactList": List["InterMetricImpactDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyGroupSummariesRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupSummariesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "SensitivityThreshold": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAnomalyGroupSummariesResponseTypeDef = TypedDict(
    "ListAnomalyGroupSummariesResponseTypeDef",
    {
        "AnomalyGroupSummaryList": List["AnomalyGroupSummaryTypeDef"],
        "AnomalyGroupStatistics": "AnomalyGroupStatisticsTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAnomalyGroupTimeSeriesRequestRequestTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupId": str,
        "MetricName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAnomalyGroupTimeSeriesResponseTypeDef = TypedDict(
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    {
        "AnomalyGroupId": str,
        "MetricName": str,
        "TimestampList": List[str],
        "NextToken": str,
        "TimeSeriesList": List["TimeSeriesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMetricSetsRequestRequestTypeDef = TypedDict(
    "ListMetricSetsRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMetricSetsResponseTypeDef = TypedDict(
    "ListMetricSetsResponseTypeDef",
    {
        "MetricSetSummaryList": List["MetricSetSummaryTypeDef"],
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

MetricLevelImpactTypeDef = TypedDict(
    "MetricLevelImpactTypeDef",
    {
        "MetricName": NotRequired[str],
        "NumTimeSeries": NotRequired[int],
        "ContributionMatrix": NotRequired["ContributionMatrixTypeDef"],
    },
)

MetricSetSummaryTypeDef = TypedDict(
    "MetricSetSummaryTypeDef",
    {
        "MetricSetArn": NotRequired[str],
        "AnomalyDetectorArn": NotRequired[str],
        "MetricSetDescription": NotRequired[str],
        "MetricSetName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastModificationTime": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
    },
)

MetricSourceTypeDef = TypedDict(
    "MetricSourceTypeDef",
    {
        "S3SourceConfig": NotRequired["S3SourceConfigTypeDef"],
        "AppFlowConfig": NotRequired["AppFlowConfigTypeDef"],
        "CloudWatchConfig": NotRequired["CloudWatchConfigTypeDef"],
        "RDSSourceConfig": NotRequired["RDSSourceConfigTypeDef"],
        "RedshiftSourceConfig": NotRequired["RedshiftSourceConfigTypeDef"],
    },
)

MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {
        "MetricName": str,
        "AggregationFunction": AggregationFunctionType,
        "Namespace": NotRequired[str],
    },
)

PutFeedbackRequestRequestTypeDef = TypedDict(
    "PutFeedbackRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "AnomalyGroupTimeSeriesFeedback": "AnomalyGroupTimeSeriesFeedbackTypeDef",
    },
)

RDSSourceConfigTypeDef = TypedDict(
    "RDSSourceConfigTypeDef",
    {
        "DBInstanceIdentifier": NotRequired[str],
        "DatabaseHost": NotRequired[str],
        "DatabasePort": NotRequired[int],
        "SecretManagerArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
    },
)

RedshiftSourceConfigTypeDef = TypedDict(
    "RedshiftSourceConfigTypeDef",
    {
        "ClusterIdentifier": NotRequired[str],
        "DatabaseHost": NotRequired[str],
        "DatabasePort": NotRequired[int],
        "SecretManagerArn": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "VpcConfiguration": NotRequired["VpcConfigurationTypeDef"],
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

S3SourceConfigTypeDef = TypedDict(
    "S3SourceConfigTypeDef",
    {
        "RoleArn": NotRequired[str],
        "TemplatedPathList": NotRequired[Sequence[str]],
        "HistoricalDataPathList": NotRequired[Sequence[str]],
        "FileFormatDescriptor": NotRequired["FileFormatDescriptorTypeDef"],
    },
)

SNSConfigurationTypeDef = TypedDict(
    "SNSConfigurationTypeDef",
    {
        "RoleArn": str,
        "SnsTopicArn": str,
    },
)

SampleDataS3SourceConfigTypeDef = TypedDict(
    "SampleDataS3SourceConfigTypeDef",
    {
        "RoleArn": str,
        "FileFormatDescriptor": "FileFormatDescriptorTypeDef",
        "TemplatedPathList": NotRequired[Sequence[str]],
        "HistoricalDataPathList": NotRequired[Sequence[str]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TimeSeriesFeedbackTypeDef = TypedDict(
    "TimeSeriesFeedbackTypeDef",
    {
        "TimeSeriesId": NotRequired[str],
        "IsAnomaly": NotRequired[bool],
    },
)

TimeSeriesTypeDef = TypedDict(
    "TimeSeriesTypeDef",
    {
        "TimeSeriesId": str,
        "DimensionList": List["DimensionNameValueTypeDef"],
        "MetricValueList": List[float],
    },
)

TimestampColumnTypeDef = TypedDict(
    "TimestampColumnTypeDef",
    {
        "ColumnName": NotRequired[str],
        "ColumnFormat": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAnomalyDetectorRequestRequestTypeDef = TypedDict(
    "UpdateAnomalyDetectorRequestRequestTypeDef",
    {
        "AnomalyDetectorArn": str,
        "KmsKeyArn": NotRequired[str],
        "AnomalyDetectorDescription": NotRequired[str],
        "AnomalyDetectorConfig": NotRequired["AnomalyDetectorConfigTypeDef"],
    },
)

UpdateAnomalyDetectorResponseTypeDef = TypedDict(
    "UpdateAnomalyDetectorResponseTypeDef",
    {
        "AnomalyDetectorArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMetricSetRequestRequestTypeDef = TypedDict(
    "UpdateMetricSetRequestRequestTypeDef",
    {
        "MetricSetArn": str,
        "MetricSetDescription": NotRequired[str],
        "MetricList": NotRequired[Sequence["MetricTypeDef"]],
        "Offset": NotRequired[int],
        "TimestampColumn": NotRequired["TimestampColumnTypeDef"],
        "DimensionList": NotRequired[Sequence[str]],
        "MetricSetFrequency": NotRequired[FrequencyType],
        "MetricSource": NotRequired["MetricSourceTypeDef"],
    },
)

UpdateMetricSetResponseTypeDef = TypedDict(
    "UpdateMetricSetResponseTypeDef",
    {
        "MetricSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcConfigurationTypeDef = TypedDict(
    "VpcConfigurationTypeDef",
    {
        "SubnetIdList": Sequence[str],
        "SecurityGroupIdList": Sequence[str],
    },
)
