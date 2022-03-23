"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import AssociateKmsKeyRequestRequestTypeDef

    data: AssociateKmsKeyRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    DistributionType,
    ExportTaskStatusCodeType,
    OrderByType,
    QueryStatusType,
    StandardUnitType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateKmsKeyRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CreateExportTaskRequestRequestTypeDef",
    "CreateExportTaskResponseTypeDef",
    "CreateLogGroupRequestRequestTypeDef",
    "CreateLogStreamRequestRequestTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteLogGroupRequestRequestTypeDef",
    "DeleteLogStreamRequestRequestTypeDef",
    "DeleteMetricFilterRequestRequestTypeDef",
    "DeleteQueryDefinitionRequestRequestTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteRetentionPolicyRequestRequestTypeDef",
    "DeleteSubscriptionFilterRequestRequestTypeDef",
    "DescribeDestinationsRequestRequestTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeLogGroupsRequestRequestTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "DescribeLogStreamsRequestRequestTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "DescribeMetricFiltersRequestRequestTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "DescribeQueriesRequestRequestTypeDef",
    "DescribeQueriesResponseTypeDef",
    "DescribeQueryDefinitionsRequestRequestTypeDef",
    "DescribeQueryDefinitionsResponseTypeDef",
    "DescribeResourcePoliciesRequestRequestTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "DescribeSubscriptionFiltersRequestRequestTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "DestinationTypeDef",
    "DisassociateKmsKeyRequestRequestTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FilterLogEventsRequestRequestTypeDef",
    "FilterLogEventsResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetLogEventsRequestRequestTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsRequestRequestTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordRequestRequestTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "InputLogEventTypeDef",
    "ListTagsLogGroupRequestRequestTypeDef",
    "ListTagsLogGroupResponseTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "PutDestinationPolicyRequestRequestTypeDef",
    "PutDestinationRequestRequestTypeDef",
    "PutDestinationResponseTypeDef",
    "PutLogEventsRequestRequestTypeDef",
    "PutLogEventsResponseTypeDef",
    "PutMetricFilterRequestRequestTypeDef",
    "PutQueryDefinitionRequestRequestTypeDef",
    "PutQueryDefinitionResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutRetentionPolicyRequestRequestTypeDef",
    "PutSubscriptionFilterRequestRequestTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFieldTypeDef",
    "SearchedLogStreamTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopQueryRequestRequestTypeDef",
    "StopQueryResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "TagLogGroupRequestRequestTypeDef",
    "TestMetricFilterRequestRequestTypeDef",
    "TestMetricFilterResponseTypeDef",
    "UntagLogGroupRequestRequestTypeDef",
)

AssociateKmsKeyRequestRequestTypeDef = TypedDict(
    "AssociateKmsKeyRequestRequestTypeDef",
    {
        "logGroupName": str,
        "kmsKeyId": str,
    },
)

CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "taskId": str,
    },
)

CreateExportTaskRequestRequestTypeDef = TypedDict(
    "CreateExportTaskRequestRequestTypeDef",
    {
        "logGroupName": str,
        "fromTime": int,
        "to": int,
        "destination": str,
        "taskName": NotRequired[str],
        "logStreamNamePrefix": NotRequired[str],
        "destinationPrefix": NotRequired[str],
    },
)

CreateExportTaskResponseTypeDef = TypedDict(
    "CreateExportTaskResponseTypeDef",
    {
        "taskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLogGroupRequestRequestTypeDef = TypedDict(
    "CreateLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
        "kmsKeyId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateLogStreamRequestRequestTypeDef = TypedDict(
    "CreateLogStreamRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
    },
)

DeleteLogGroupRequestRequestTypeDef = TypedDict(
    "DeleteLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteLogStreamRequestRequestTypeDef = TypedDict(
    "DeleteLogStreamRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
    },
)

DeleteMetricFilterRequestRequestTypeDef = TypedDict(
    "DeleteMetricFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DeleteQueryDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteQueryDefinitionRequestRequestTypeDef",
    {
        "queryDefinitionId": str,
    },
)

DeleteQueryDefinitionResponseTypeDef = TypedDict(
    "DeleteQueryDefinitionResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "policyName": NotRequired[str],
    },
)

DeleteRetentionPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRetentionPolicyRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

DeleteSubscriptionFilterRequestRequestTypeDef = TypedDict(
    "DeleteSubscriptionFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
    },
)

DescribeDestinationsRequestRequestTypeDef = TypedDict(
    "DescribeDestinationsRequestRequestTypeDef",
    {
        "DestinationNamePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeDestinationsResponseTypeDef = TypedDict(
    "DescribeDestinationsResponseTypeDef",
    {
        "destinations": List["DestinationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "taskId": NotRequired[str],
        "statusCode": NotRequired[ExportTaskStatusCodeType],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeExportTasksResponseTypeDef = TypedDict(
    "DescribeExportTasksResponseTypeDef",
    {
        "exportTasks": List["ExportTaskTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLogGroupsRequestRequestTypeDef",
    {
        "logGroupNamePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeLogGroupsResponseTypeDef = TypedDict(
    "DescribeLogGroupsResponseTypeDef",
    {
        "logGroups": List["LogGroupTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLogStreamsRequestRequestTypeDef = TypedDict(
    "DescribeLogStreamsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamNamePrefix": NotRequired[str],
        "orderBy": NotRequired[OrderByType],
        "descending": NotRequired[bool],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeLogStreamsResponseTypeDef = TypedDict(
    "DescribeLogStreamsResponseTypeDef",
    {
        "logStreams": List["LogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMetricFiltersRequestRequestTypeDef = TypedDict(
    "DescribeMetricFiltersRequestRequestTypeDef",
    {
        "logGroupName": NotRequired[str],
        "filterNamePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
        "metricName": NotRequired[str],
        "metricNamespace": NotRequired[str],
    },
)

DescribeMetricFiltersResponseTypeDef = TypedDict(
    "DescribeMetricFiltersResponseTypeDef",
    {
        "metricFilters": List["MetricFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueriesRequestRequestTypeDef = TypedDict(
    "DescribeQueriesRequestRequestTypeDef",
    {
        "logGroupName": NotRequired[str],
        "status": NotRequired[QueryStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeQueriesResponseTypeDef = TypedDict(
    "DescribeQueriesResponseTypeDef",
    {
        "queries": List["QueryInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQueryDefinitionsRequestRequestTypeDef = TypedDict(
    "DescribeQueryDefinitionsRequestRequestTypeDef",
    {
        "queryDefinitionNamePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

DescribeQueryDefinitionsResponseTypeDef = TypedDict(
    "DescribeQueryDefinitionsResponseTypeDef",
    {
        "queryDefinitions": List["QueryDefinitionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePoliciesRequestRequestTypeDef = TypedDict(
    "DescribeResourcePoliciesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeResourcePoliciesResponseTypeDef = TypedDict(
    "DescribeResourcePoliciesResponseTypeDef",
    {
        "resourcePolicies": List["ResourcePolicyTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubscriptionFiltersRequestRequestTypeDef = TypedDict(
    "DescribeSubscriptionFiltersRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterNamePrefix": NotRequired[str],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
    },
)

DescribeSubscriptionFiltersResponseTypeDef = TypedDict(
    "DescribeSubscriptionFiltersResponseTypeDef",
    {
        "subscriptionFilters": List["SubscriptionFilterTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "destinationName": NotRequired[str],
        "targetArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "accessPolicy": NotRequired[str],
        "arn": NotRequired[str],
        "creationTime": NotRequired[int],
    },
)

DisassociateKmsKeyRequestRequestTypeDef = TypedDict(
    "DisassociateKmsKeyRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

ExportTaskExecutionInfoTypeDef = TypedDict(
    "ExportTaskExecutionInfoTypeDef",
    {
        "creationTime": NotRequired[int],
        "completionTime": NotRequired[int],
    },
)

ExportTaskStatusTypeDef = TypedDict(
    "ExportTaskStatusTypeDef",
    {
        "code": NotRequired[ExportTaskStatusCodeType],
        "message": NotRequired[str],
    },
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": NotRequired[str],
        "taskName": NotRequired[str],
        "logGroupName": NotRequired[str],
        "from": NotRequired[int],
        "to": NotRequired[int],
        "destination": NotRequired[str],
        "destinationPrefix": NotRequired[str],
        "status": NotRequired["ExportTaskStatusTypeDef"],
        "executionInfo": NotRequired["ExportTaskExecutionInfoTypeDef"],
    },
)

FilterLogEventsRequestRequestTypeDef = TypedDict(
    "FilterLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamNames": NotRequired[Sequence[str]],
        "logStreamNamePrefix": NotRequired[str],
        "startTime": NotRequired[int],
        "endTime": NotRequired[int],
        "filterPattern": NotRequired[str],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
        "interleaved": NotRequired[bool],
    },
)

FilterLogEventsResponseTypeDef = TypedDict(
    "FilterLogEventsResponseTypeDef",
    {
        "events": List["FilteredLogEventTypeDef"],
        "searchedLogStreams": List["SearchedLogStreamTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilteredLogEventTypeDef = TypedDict(
    "FilteredLogEventTypeDef",
    {
        "logStreamName": NotRequired[str],
        "timestamp": NotRequired[int],
        "message": NotRequired[str],
        "ingestionTime": NotRequired[int],
        "eventId": NotRequired[str],
    },
)

GetLogEventsRequestRequestTypeDef = TypedDict(
    "GetLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
        "startTime": NotRequired[int],
        "endTime": NotRequired[int],
        "nextToken": NotRequired[str],
        "limit": NotRequired[int],
        "startFromHead": NotRequired[bool],
    },
)

GetLogEventsResponseTypeDef = TypedDict(
    "GetLogEventsResponseTypeDef",
    {
        "events": List["OutputLogEventTypeDef"],
        "nextForwardToken": str,
        "nextBackwardToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogGroupFieldsRequestRequestTypeDef = TypedDict(
    "GetLogGroupFieldsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "time": NotRequired[int],
    },
)

GetLogGroupFieldsResponseTypeDef = TypedDict(
    "GetLogGroupFieldsResponseTypeDef",
    {
        "logGroupFields": List["LogGroupFieldTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogRecordRequestRequestTypeDef = TypedDict(
    "GetLogRecordRequestRequestTypeDef",
    {
        "logRecordPointer": str,
    },
)

GetLogRecordResponseTypeDef = TypedDict(
    "GetLogRecordResponseTypeDef",
    {
        "logRecord": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsRequestRequestTypeDef = TypedDict(
    "GetQueryResultsRequestRequestTypeDef",
    {
        "queryId": str,
    },
)

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "results": List[List["ResultFieldTypeDef"]],
        "statistics": "QueryStatisticsTypeDef",
        "status": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputLogEventTypeDef = TypedDict(
    "InputLogEventTypeDef",
    {
        "timestamp": int,
        "message": str,
    },
)

ListTagsLogGroupRequestRequestTypeDef = TypedDict(
    "ListTagsLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
    },
)

ListTagsLogGroupResponseTypeDef = TypedDict(
    "ListTagsLogGroupResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LogGroupFieldTypeDef = TypedDict(
    "LogGroupFieldTypeDef",
    {
        "name": NotRequired[str],
        "percent": NotRequired[int],
    },
)

LogGroupTypeDef = TypedDict(
    "LogGroupTypeDef",
    {
        "logGroupName": NotRequired[str],
        "creationTime": NotRequired[int],
        "retentionInDays": NotRequired[int],
        "metricFilterCount": NotRequired[int],
        "arn": NotRequired[str],
        "storedBytes": NotRequired[int],
        "kmsKeyId": NotRequired[str],
    },
)

LogStreamTypeDef = TypedDict(
    "LogStreamTypeDef",
    {
        "logStreamName": NotRequired[str],
        "creationTime": NotRequired[int],
        "firstEventTimestamp": NotRequired[int],
        "lastEventTimestamp": NotRequired[int],
        "lastIngestionTime": NotRequired[int],
        "uploadSequenceToken": NotRequired[str],
        "arn": NotRequired[str],
        "storedBytes": NotRequired[int],
    },
)

MetricFilterMatchRecordTypeDef = TypedDict(
    "MetricFilterMatchRecordTypeDef",
    {
        "eventNumber": NotRequired[int],
        "eventMessage": NotRequired[str],
        "extractedValues": NotRequired[Dict[str, str]],
    },
)

MetricFilterTypeDef = TypedDict(
    "MetricFilterTypeDef",
    {
        "filterName": NotRequired[str],
        "filterPattern": NotRequired[str],
        "metricTransformations": NotRequired[List["MetricTransformationTypeDef"]],
        "creationTime": NotRequired[int],
        "logGroupName": NotRequired[str],
    },
)

MetricTransformationTypeDef = TypedDict(
    "MetricTransformationTypeDef",
    {
        "metricName": str,
        "metricNamespace": str,
        "metricValue": str,
        "defaultValue": NotRequired[float],
        "dimensions": NotRequired[Dict[str, str]],
        "unit": NotRequired[StandardUnitType],
    },
)

OutputLogEventTypeDef = TypedDict(
    "OutputLogEventTypeDef",
    {
        "timestamp": NotRequired[int],
        "message": NotRequired[str],
        "ingestionTime": NotRequired[int],
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

PutDestinationPolicyRequestRequestTypeDef = TypedDict(
    "PutDestinationPolicyRequestRequestTypeDef",
    {
        "destinationName": str,
        "accessPolicy": str,
        "forceUpdate": NotRequired[bool],
    },
)

PutDestinationRequestRequestTypeDef = TypedDict(
    "PutDestinationRequestRequestTypeDef",
    {
        "destinationName": str,
        "targetArn": str,
        "roleArn": str,
    },
)

PutDestinationResponseTypeDef = TypedDict(
    "PutDestinationResponseTypeDef",
    {
        "destination": "DestinationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutLogEventsRequestRequestTypeDef = TypedDict(
    "PutLogEventsRequestRequestTypeDef",
    {
        "logGroupName": str,
        "logStreamName": str,
        "logEvents": Sequence["InputLogEventTypeDef"],
        "sequenceToken": NotRequired[str],
    },
)

PutLogEventsResponseTypeDef = TypedDict(
    "PutLogEventsResponseTypeDef",
    {
        "nextSequenceToken": str,
        "rejectedLogEventsInfo": "RejectedLogEventsInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutMetricFilterRequestRequestTypeDef = TypedDict(
    "PutMetricFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "metricTransformations": Sequence["MetricTransformationTypeDef"],
    },
)

PutQueryDefinitionRequestRequestTypeDef = TypedDict(
    "PutQueryDefinitionRequestRequestTypeDef",
    {
        "name": str,
        "queryString": str,
        "queryDefinitionId": NotRequired[str],
        "logGroupNames": NotRequired[Sequence[str]],
    },
)

PutQueryDefinitionResponseTypeDef = TypedDict(
    "PutQueryDefinitionResponseTypeDef",
    {
        "queryDefinitionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "policyName": NotRequired[str],
        "policyDocument": NotRequired[str],
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "resourcePolicy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionPolicyRequestRequestTypeDef = TypedDict(
    "PutRetentionPolicyRequestRequestTypeDef",
    {
        "logGroupName": str,
        "retentionInDays": int,
    },
)

PutSubscriptionFilterRequestRequestTypeDef = TypedDict(
    "PutSubscriptionFilterRequestRequestTypeDef",
    {
        "logGroupName": str,
        "filterName": str,
        "filterPattern": str,
        "destinationArn": str,
        "roleArn": NotRequired[str],
        "distribution": NotRequired[DistributionType],
    },
)

QueryDefinitionTypeDef = TypedDict(
    "QueryDefinitionTypeDef",
    {
        "queryDefinitionId": NotRequired[str],
        "name": NotRequired[str],
        "queryString": NotRequired[str],
        "lastModified": NotRequired[int],
        "logGroupNames": NotRequired[List[str]],
    },
)

QueryInfoTypeDef = TypedDict(
    "QueryInfoTypeDef",
    {
        "queryId": NotRequired[str],
        "queryString": NotRequired[str],
        "status": NotRequired[QueryStatusType],
        "createTime": NotRequired[int],
        "logGroupName": NotRequired[str],
    },
)

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "recordsMatched": NotRequired[float],
        "recordsScanned": NotRequired[float],
        "bytesScanned": NotRequired[float],
    },
)

RejectedLogEventsInfoTypeDef = TypedDict(
    "RejectedLogEventsInfoTypeDef",
    {
        "tooNewLogEventStartIndex": NotRequired[int],
        "tooOldLogEventEndIndex": NotRequired[int],
        "expiredLogEventEndIndex": NotRequired[int],
    },
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "policyName": NotRequired[str],
        "policyDocument": NotRequired[str],
        "lastUpdatedTime": NotRequired[int],
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

ResultFieldTypeDef = TypedDict(
    "ResultFieldTypeDef",
    {
        "field": NotRequired[str],
        "value": NotRequired[str],
    },
)

SearchedLogStreamTypeDef = TypedDict(
    "SearchedLogStreamTypeDef",
    {
        "logStreamName": NotRequired[str],
        "searchedCompletely": NotRequired[bool],
    },
)

StartQueryRequestRequestTypeDef = TypedDict(
    "StartQueryRequestRequestTypeDef",
    {
        "startTime": int,
        "endTime": int,
        "queryString": str,
        "logGroupName": NotRequired[str],
        "logGroupNames": NotRequired[Sequence[str]],
        "limit": NotRequired[int],
    },
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "queryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryRequestRequestTypeDef = TypedDict(
    "StopQueryRequestRequestTypeDef",
    {
        "queryId": str,
    },
)

StopQueryResponseTypeDef = TypedDict(
    "StopQueryResponseTypeDef",
    {
        "success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SubscriptionFilterTypeDef = TypedDict(
    "SubscriptionFilterTypeDef",
    {
        "filterName": NotRequired[str],
        "logGroupName": NotRequired[str],
        "filterPattern": NotRequired[str],
        "destinationArn": NotRequired[str],
        "roleArn": NotRequired[str],
        "distribution": NotRequired[DistributionType],
        "creationTime": NotRequired[int],
    },
)

TagLogGroupRequestRequestTypeDef = TypedDict(
    "TagLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
        "tags": Mapping[str, str],
    },
)

TestMetricFilterRequestRequestTypeDef = TypedDict(
    "TestMetricFilterRequestRequestTypeDef",
    {
        "filterPattern": str,
        "logEventMessages": Sequence[str],
    },
)

TestMetricFilterResponseTypeDef = TypedDict(
    "TestMetricFilterResponseTypeDef",
    {
        "matches": List["MetricFilterMatchRecordTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagLogGroupRequestRequestTypeDef = TypedDict(
    "UntagLogGroupRequestRequestTypeDef",
    {
        "logGroupName": str,
        "tags": Sequence[str],
    },
)
