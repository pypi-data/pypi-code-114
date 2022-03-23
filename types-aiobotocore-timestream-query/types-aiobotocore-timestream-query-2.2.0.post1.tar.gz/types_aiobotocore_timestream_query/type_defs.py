"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_timestream_query/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_timestream_query.type_defs import CancelQueryRequestRequestTypeDef

    data: CancelQueryRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    MeasureValueTypeType,
    S3EncryptionOptionType,
    ScalarMeasureValueTypeType,
    ScalarTypeType,
    ScheduledQueryRunStatusType,
    ScheduledQueryStateType,
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
    "CancelQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "ColumnInfoTypeDef",
    "CreateScheduledQueryRequestRequestTypeDef",
    "CreateScheduledQueryResponseTypeDef",
    "DatumTypeDef",
    "DeleteScheduledQueryRequestRequestTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeScheduledQueryRequestRequestTypeDef",
    "DescribeScheduledQueryResponseTypeDef",
    "DimensionMappingTypeDef",
    "EndpointTypeDef",
    "ErrorReportConfigurationTypeDef",
    "ErrorReportLocationTypeDef",
    "ExecuteScheduledQueryRequestRequestTypeDef",
    "ExecutionStatsTypeDef",
    "ListScheduledQueriesRequestRequestTypeDef",
    "ListScheduledQueriesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MixedMeasureMappingTypeDef",
    "MultiMeasureAttributeMappingTypeDef",
    "MultiMeasureMappingsTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterMappingTypeDef",
    "PrepareQueryRequestRequestTypeDef",
    "PrepareQueryResponseTypeDef",
    "QueryRequestRequestTypeDef",
    "QueryResponseTypeDef",
    "QueryStatusTypeDef",
    "ResponseMetadataTypeDef",
    "RowTypeDef",
    "S3ConfigurationTypeDef",
    "S3ReportLocationTypeDef",
    "ScheduleConfigurationTypeDef",
    "ScheduledQueryDescriptionTypeDef",
    "ScheduledQueryRunSummaryTypeDef",
    "ScheduledQueryTypeDef",
    "SelectColumnTypeDef",
    "SnsConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetDestinationTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TimestreamConfigurationTypeDef",
    "TimestreamDestinationTypeDef",
    "TypeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateScheduledQueryRequestRequestTypeDef",
)

CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "CancellationMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Type": Dict[str, Any],
        "Name": NotRequired[str],
    },
)

CreateScheduledQueryRequestRequestTypeDef = TypedDict(
    "CreateScheduledQueryRequestRequestTypeDef",
    {
        "Name": str,
        "QueryString": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "ScheduledQueryExecutionRoleArn": str,
        "ErrorReportConfiguration": "ErrorReportConfigurationTypeDef",
        "TargetConfiguration": NotRequired["TargetConfigurationTypeDef"],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "KmsKeyId": NotRequired[str],
    },
)

CreateScheduledQueryResponseTypeDef = TypedDict(
    "CreateScheduledQueryResponseTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "ScalarValue": NotRequired[str],
        "TimeSeriesValue": NotRequired[List[Dict[str, Any]]],
        "ArrayValue": NotRequired[List[Dict[str, Any]]],
        "RowValue": NotRequired[Dict[str, Any]],
        "NullValue": NotRequired[bool],
    },
)

DeleteScheduledQueryRequestRequestTypeDef = TypedDict(
    "DeleteScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
    },
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {
        "Endpoints": List["EndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledQueryRequestRequestTypeDef = TypedDict(
    "DescribeScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
    },
)

DescribeScheduledQueryResponseTypeDef = TypedDict(
    "DescribeScheduledQueryResponseTypeDef",
    {
        "ScheduledQuery": "ScheduledQueryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DimensionMappingTypeDef = TypedDict(
    "DimensionMappingTypeDef",
    {
        "Name": str,
        "DimensionValueType": Literal["VARCHAR"],
    },
)

EndpointTypeDef = TypedDict(
    "EndpointTypeDef",
    {
        "Address": str,
        "CachePeriodInMinutes": int,
    },
)

ErrorReportConfigurationTypeDef = TypedDict(
    "ErrorReportConfigurationTypeDef",
    {
        "S3Configuration": "S3ConfigurationTypeDef",
    },
)

ErrorReportLocationTypeDef = TypedDict(
    "ErrorReportLocationTypeDef",
    {
        "S3ReportLocation": NotRequired["S3ReportLocationTypeDef"],
    },
)

ExecuteScheduledQueryRequestRequestTypeDef = TypedDict(
    "ExecuteScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
        "InvocationTime": Union[datetime, str],
        "ClientToken": NotRequired[str],
    },
)

ExecutionStatsTypeDef = TypedDict(
    "ExecutionStatsTypeDef",
    {
        "ExecutionTimeInMillis": NotRequired[int],
        "DataWrites": NotRequired[int],
        "BytesMetered": NotRequired[int],
        "RecordsIngested": NotRequired[int],
        "QueryResultRows": NotRequired[int],
    },
)

ListScheduledQueriesRequestRequestTypeDef = TypedDict(
    "ListScheduledQueriesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListScheduledQueriesResponseTypeDef = TypedDict(
    "ListScheduledQueriesResponseTypeDef",
    {
        "ScheduledQueries": List["ScheduledQueryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "MaxResults": NotRequired[int],
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

MixedMeasureMappingTypeDef = TypedDict(
    "MixedMeasureMappingTypeDef",
    {
        "MeasureValueType": MeasureValueTypeType,
        "MeasureName": NotRequired[str],
        "SourceColumn": NotRequired[str],
        "TargetMeasureName": NotRequired[str],
        "MultiMeasureAttributeMappings": NotRequired[
            Sequence["MultiMeasureAttributeMappingTypeDef"]
        ],
    },
)

MultiMeasureAttributeMappingTypeDef = TypedDict(
    "MultiMeasureAttributeMappingTypeDef",
    {
        "SourceColumn": str,
        "MeasureValueType": ScalarMeasureValueTypeType,
        "TargetMultiMeasureAttributeName": NotRequired[str],
    },
)

MultiMeasureMappingsTypeDef = TypedDict(
    "MultiMeasureMappingsTypeDef",
    {
        "MultiMeasureAttributeMappings": Sequence["MultiMeasureAttributeMappingTypeDef"],
        "TargetMultiMeasureName": NotRequired[str],
    },
)

NotificationConfigurationTypeDef = TypedDict(
    "NotificationConfigurationTypeDef",
    {
        "SnsConfiguration": "SnsConfigurationTypeDef",
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

ParameterMappingTypeDef = TypedDict(
    "ParameterMappingTypeDef",
    {
        "Name": str,
        "Type": "TypeTypeDef",
    },
)

PrepareQueryRequestRequestTypeDef = TypedDict(
    "PrepareQueryRequestRequestTypeDef",
    {
        "QueryString": str,
        "ValidateOnly": NotRequired[bool],
    },
)

PrepareQueryResponseTypeDef = TypedDict(
    "PrepareQueryResponseTypeDef",
    {
        "QueryString": str,
        "Columns": List["SelectColumnTypeDef"],
        "Parameters": List["ParameterMappingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryRequestRequestTypeDef = TypedDict(
    "QueryRequestRequestTypeDef",
    {
        "QueryString": str,
        "ClientToken": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxRows": NotRequired[int],
    },
)

QueryResponseTypeDef = TypedDict(
    "QueryResponseTypeDef",
    {
        "QueryId": str,
        "NextToken": str,
        "Rows": List["RowTypeDef"],
        "ColumnInfo": List["ColumnInfoTypeDef"],
        "QueryStatus": "QueryStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStatusTypeDef = TypedDict(
    "QueryStatusTypeDef",
    {
        "ProgressPercentage": NotRequired[float],
        "CumulativeBytesScanned": NotRequired[int],
        "CumulativeBytesMetered": NotRequired[int],
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

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": List["DatumTypeDef"],
    },
)

S3ConfigurationTypeDef = TypedDict(
    "S3ConfigurationTypeDef",
    {
        "BucketName": str,
        "ObjectKeyPrefix": NotRequired[str],
        "EncryptionOption": NotRequired[S3EncryptionOptionType],
    },
)

S3ReportLocationTypeDef = TypedDict(
    "S3ReportLocationTypeDef",
    {
        "BucketName": NotRequired[str],
        "ObjectKey": NotRequired[str],
    },
)

ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "ScheduleExpression": str,
    },
)

ScheduledQueryDescriptionTypeDef = TypedDict(
    "ScheduledQueryDescriptionTypeDef",
    {
        "Arn": str,
        "Name": str,
        "QueryString": str,
        "State": ScheduledQueryStateType,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "NotificationConfiguration": "NotificationConfigurationTypeDef",
        "CreationTime": NotRequired[datetime],
        "PreviousInvocationTime": NotRequired[datetime],
        "NextInvocationTime": NotRequired[datetime],
        "TargetConfiguration": NotRequired["TargetConfigurationTypeDef"],
        "ScheduledQueryExecutionRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "ErrorReportConfiguration": NotRequired["ErrorReportConfigurationTypeDef"],
        "LastRunSummary": NotRequired["ScheduledQueryRunSummaryTypeDef"],
        "RecentlyFailedRuns": NotRequired[List["ScheduledQueryRunSummaryTypeDef"]],
    },
)

ScheduledQueryRunSummaryTypeDef = TypedDict(
    "ScheduledQueryRunSummaryTypeDef",
    {
        "InvocationTime": NotRequired[datetime],
        "TriggerTime": NotRequired[datetime],
        "RunStatus": NotRequired[ScheduledQueryRunStatusType],
        "ExecutionStats": NotRequired["ExecutionStatsTypeDef"],
        "ErrorReportLocation": NotRequired["ErrorReportLocationTypeDef"],
        "FailureReason": NotRequired[str],
    },
)

ScheduledQueryTypeDef = TypedDict(
    "ScheduledQueryTypeDef",
    {
        "Arn": str,
        "Name": str,
        "State": ScheduledQueryStateType,
        "CreationTime": NotRequired[datetime],
        "PreviousInvocationTime": NotRequired[datetime],
        "NextInvocationTime": NotRequired[datetime],
        "ErrorReportConfiguration": NotRequired["ErrorReportConfigurationTypeDef"],
        "TargetDestination": NotRequired["TargetDestinationTypeDef"],
        "LastRunStatus": NotRequired[ScheduledQueryRunStatusType],
    },
)

SelectColumnTypeDef = TypedDict(
    "SelectColumnTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired["TypeTypeDef"],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Aliased": NotRequired[bool],
    },
)

SnsConfigurationTypeDef = TypedDict(
    "SnsConfigurationTypeDef",
    {
        "TopicArn": str,
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

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TimestreamConfiguration": "TimestreamConfigurationTypeDef",
    },
)

TargetDestinationTypeDef = TypedDict(
    "TargetDestinationTypeDef",
    {
        "TimestreamDestination": NotRequired["TimestreamDestinationTypeDef"],
    },
)

TimeSeriesDataPointTypeDef = TypedDict(
    "TimeSeriesDataPointTypeDef",
    {
        "Time": str,
        "Value": "DatumTypeDef",
    },
)

TimestreamConfigurationTypeDef = TypedDict(
    "TimestreamConfigurationTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TimeColumn": str,
        "DimensionMappings": Sequence["DimensionMappingTypeDef"],
        "MultiMeasureMappings": NotRequired["MultiMeasureMappingsTypeDef"],
        "MixedMeasureMappings": NotRequired[Sequence["MixedMeasureMappingTypeDef"]],
        "MeasureNameColumn": NotRequired[str],
    },
)

TimestreamDestinationTypeDef = TypedDict(
    "TimestreamDestinationTypeDef",
    {
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
    },
)

TypeTypeDef = TypedDict(
    "TypeTypeDef",
    {
        "ScalarType": NotRequired[ScalarTypeType],
        "ArrayColumnInfo": NotRequired[Dict[str, Any]],
        "TimeSeriesMeasureValueColumnInfo": NotRequired[Dict[str, Any]],
        "RowColumnInfo": NotRequired[List[Dict[str, Any]]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateScheduledQueryRequestRequestTypeDef = TypedDict(
    "UpdateScheduledQueryRequestRequestTypeDef",
    {
        "ScheduledQueryArn": str,
        "State": ScheduledQueryStateType,
    },
)
