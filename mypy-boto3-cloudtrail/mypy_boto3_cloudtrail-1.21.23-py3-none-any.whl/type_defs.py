"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import AddTagsRequestRequestTypeDef

    data: AddTagsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EventDataStoreStatusType,
    InsightTypeType,
    LookupAttributeKeyType,
    QueryStatusType,
    ReadWriteTypeType,
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
    "AddTagsRequestRequestTypeDef",
    "AdvancedEventSelectorTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CancelQueryRequestRequestTypeDef",
    "CancelQueryResponseTypeDef",
    "CreateEventDataStoreRequestRequestTypeDef",
    "CreateEventDataStoreResponseTypeDef",
    "CreateTrailRequestRequestTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceTypeDef",
    "DeleteEventDataStoreRequestRequestTypeDef",
    "DeleteTrailRequestRequestTypeDef",
    "DescribeQueryRequestRequestTypeDef",
    "DescribeQueryResponseTypeDef",
    "DescribeTrailsRequestRequestTypeDef",
    "DescribeTrailsResponseTypeDef",
    "EventDataStoreTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetEventDataStoreRequestRequestTypeDef",
    "GetEventDataStoreResponseTypeDef",
    "GetEventSelectorsRequestRequestTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetInsightSelectorsRequestRequestTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetQueryResultsRequestRequestTypeDef",
    "GetQueryResultsResponseTypeDef",
    "GetTrailRequestRequestTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusRequestRequestTypeDef",
    "GetTrailStatusResponseTypeDef",
    "InsightSelectorTypeDef",
    "ListEventDataStoresRequestRequestTypeDef",
    "ListEventDataStoresResponseTypeDef",
    "ListPublicKeysRequestRequestTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListQueriesRequestRequestTypeDef",
    "ListQueriesResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "ListTrailsRequestRequestTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupAttributeTypeDef",
    "LookupEventsRequestRequestTypeDef",
    "LookupEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublicKeyTypeDef",
    "PutEventSelectorsRequestRequestTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "PutInsightSelectorsRequestRequestTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "QueryStatisticsForDescribeQueryTypeDef",
    "QueryStatisticsTypeDef",
    "QueryTypeDef",
    "RemoveTagsRequestRequestTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreEventDataStoreRequestRequestTypeDef",
    "RestoreEventDataStoreResponseTypeDef",
    "StartLoggingRequestRequestTypeDef",
    "StartQueryRequestRequestTypeDef",
    "StartQueryResponseTypeDef",
    "StopLoggingRequestRequestTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateEventDataStoreRequestRequestTypeDef",
    "UpdateEventDataStoreResponseTypeDef",
    "UpdateTrailRequestRequestTypeDef",
    "UpdateTrailResponseTypeDef",
)

AddTagsRequestRequestTypeDef = TypedDict(
    "AddTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence["TagTypeDef"],
    },
)

AdvancedEventSelectorTypeDef = TypedDict(
    "AdvancedEventSelectorTypeDef",
    {
        "FieldSelectors": Sequence["AdvancedFieldSelectorTypeDef"],
        "Name": NotRequired[str],
    },
)

AdvancedFieldSelectorTypeDef = TypedDict(
    "AdvancedFieldSelectorTypeDef",
    {
        "Field": str,
        "Equals": NotRequired[Sequence[str]],
        "StartsWith": NotRequired[Sequence[str]],
        "EndsWith": NotRequired[Sequence[str]],
        "NotEquals": NotRequired[Sequence[str]],
        "NotStartsWith": NotRequired[Sequence[str]],
        "NotEndsWith": NotRequired[Sequence[str]],
    },
)

CancelQueryRequestRequestTypeDef = TypedDict(
    "CancelQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
    },
)

CancelQueryResponseTypeDef = TypedDict(
    "CancelQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryStatus": QueryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventDataStoreRequestRequestTypeDef = TypedDict(
    "CreateEventDataStoreRequestRequestTypeDef",
    {
        "Name": str,
        "AdvancedEventSelectors": NotRequired[Sequence["AdvancedEventSelectorTypeDef"]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "TerminationProtectionEnabled": NotRequired[bool],
        "TagsList": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateEventDataStoreResponseTypeDef = TypedDict(
    "CreateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "TagsList": List["TagTypeDef"],
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrailRequestRequestTypeDef = TypedDict(
    "CreateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "EnableLogFileValidation": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "IsOrganizationTrail": NotRequired[bool],
        "TagsList": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTrailResponseTypeDef = TypedDict(
    "CreateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef",
    {
        "Type": NotRequired[str],
        "Values": NotRequired[List[str]],
    },
)

DeleteEventDataStoreRequestRequestTypeDef = TypedDict(
    "DeleteEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

DeleteTrailRequestRequestTypeDef = TypedDict(
    "DeleteTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeQueryRequestRequestTypeDef = TypedDict(
    "DescribeQueryRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
    },
)

DescribeQueryResponseTypeDef = TypedDict(
    "DescribeQueryResponseTypeDef",
    {
        "QueryId": str,
        "QueryString": str,
        "QueryStatus": QueryStatusType,
        "QueryStatistics": "QueryStatisticsForDescribeQueryTypeDef",
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrailsRequestRequestTypeDef = TypedDict(
    "DescribeTrailsRequestRequestTypeDef",
    {
        "trailNameList": NotRequired[Sequence[str]],
        "includeShadowTrails": NotRequired[bool],
    },
)

DescribeTrailsResponseTypeDef = TypedDict(
    "DescribeTrailsResponseTypeDef",
    {
        "trailList": List["TrailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventDataStoreTypeDef = TypedDict(
    "EventDataStoreTypeDef",
    {
        "EventDataStoreArn": NotRequired[str],
        "Name": NotRequired[str],
        "TerminationProtectionEnabled": NotRequired[bool],
        "Status": NotRequired[EventDataStoreStatusType],
        "AdvancedEventSelectors": NotRequired[List["AdvancedEventSelectorTypeDef"]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

EventSelectorTypeDef = TypedDict(
    "EventSelectorTypeDef",
    {
        "ReadWriteType": NotRequired[ReadWriteTypeType],
        "IncludeManagementEvents": NotRequired[bool],
        "DataResources": NotRequired[List["DataResourceTypeDef"]],
        "ExcludeManagementEventSources": NotRequired[List[str]],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": NotRequired[str],
        "EventName": NotRequired[str],
        "ReadOnly": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "EventSource": NotRequired[str],
        "Username": NotRequired[str],
        "Resources": NotRequired[List["ResourceTypeDef"]],
        "CloudTrailEvent": NotRequired[str],
    },
)

GetEventDataStoreRequestRequestTypeDef = TypedDict(
    "GetEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

GetEventDataStoreResponseTypeDef = TypedDict(
    "GetEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventSelectorsRequestRequestTypeDef = TypedDict(
    "GetEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetEventSelectorsResponseTypeDef = TypedDict(
    "GetEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInsightSelectorsRequestRequestTypeDef = TypedDict(
    "GetInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
    },
)

GetInsightSelectorsResponseTypeDef = TypedDict(
    "GetInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsRequestRequestTypeDef = TypedDict(
    "GetQueryResultsRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "QueryId": str,
        "NextToken": NotRequired[str],
        "MaxQueryResults": NotRequired[int],
    },
)

GetQueryResultsResponseTypeDef = TypedDict(
    "GetQueryResultsResponseTypeDef",
    {
        "QueryStatus": QueryStatusType,
        "QueryStatistics": "QueryStatisticsTypeDef",
        "QueryResultRows": List[List[Dict[str, str]]],
        "NextToken": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailRequestRequestTypeDef = TypedDict(
    "GetTrailRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailResponseTypeDef = TypedDict(
    "GetTrailResponseTypeDef",
    {
        "Trail": "TrailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrailStatusRequestRequestTypeDef = TypedDict(
    "GetTrailStatusRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTrailStatusResponseTypeDef = TypedDict(
    "GetTrailStatusResponseTypeDef",
    {
        "IsLogging": bool,
        "LatestDeliveryError": str,
        "LatestNotificationError": str,
        "LatestDeliveryTime": datetime,
        "LatestNotificationTime": datetime,
        "StartLoggingTime": datetime,
        "StopLoggingTime": datetime,
        "LatestCloudWatchLogsDeliveryError": str,
        "LatestCloudWatchLogsDeliveryTime": datetime,
        "LatestDigestDeliveryTime": datetime,
        "LatestDigestDeliveryError": str,
        "LatestDeliveryAttemptTime": str,
        "LatestNotificationAttemptTime": str,
        "LatestNotificationAttemptSucceeded": str,
        "LatestDeliveryAttemptSucceeded": str,
        "TimeLoggingStarted": str,
        "TimeLoggingStopped": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InsightSelectorTypeDef = TypedDict(
    "InsightSelectorTypeDef",
    {
        "InsightType": NotRequired[InsightTypeType],
    },
)

ListEventDataStoresRequestRequestTypeDef = TypedDict(
    "ListEventDataStoresRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEventDataStoresResponseTypeDef = TypedDict(
    "ListEventDataStoresResponseTypeDef",
    {
        "EventDataStores": List["EventDataStoreTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPublicKeysRequestRequestTypeDef = TypedDict(
    "ListPublicKeysRequestRequestTypeDef",
    {
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "NextToken": NotRequired[str],
    },
)

ListPublicKeysResponseTypeDef = TypedDict(
    "ListPublicKeysResponseTypeDef",
    {
        "PublicKeyList": List["PublicKeyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueriesRequestRequestTypeDef = TypedDict(
    "ListQueriesRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "QueryStatus": NotRequired[QueryStatusType],
    },
)

ListQueriesResponseTypeDef = TypedDict(
    "ListQueriesResponseTypeDef",
    {
        "Queries": List["QueryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "ResourceIdList": Sequence[str],
        "NextToken": NotRequired[str],
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "ResourceTagList": List["ResourceTagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrailsRequestRequestTypeDef = TypedDict(
    "ListTrailsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

ListTrailsResponseTypeDef = TypedDict(
    "ListTrailsResponseTypeDef",
    {
        "Trails": List["TrailInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LookupAttributeTypeDef = TypedDict(
    "LookupAttributeTypeDef",
    {
        "AttributeKey": LookupAttributeKeyType,
        "AttributeValue": str,
    },
)

LookupEventsRequestRequestTypeDef = TypedDict(
    "LookupEventsRequestRequestTypeDef",
    {
        "LookupAttributes": NotRequired[Sequence["LookupAttributeTypeDef"]],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "EventCategory": NotRequired[Literal["insight"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

LookupEventsResponseTypeDef = TypedDict(
    "LookupEventsResponseTypeDef",
    {
        "Events": List["EventTypeDef"],
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

PublicKeyTypeDef = TypedDict(
    "PublicKeyTypeDef",
    {
        "Value": NotRequired[bytes],
        "ValidityStartTime": NotRequired[datetime],
        "ValidityEndTime": NotRequired[datetime],
        "Fingerprint": NotRequired[str],
    },
)

PutEventSelectorsRequestRequestTypeDef = TypedDict(
    "PutEventSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "EventSelectors": NotRequired[Sequence["EventSelectorTypeDef"]],
        "AdvancedEventSelectors": NotRequired[Sequence["AdvancedEventSelectorTypeDef"]],
    },
)

PutEventSelectorsResponseTypeDef = TypedDict(
    "PutEventSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "EventSelectors": List["EventSelectorTypeDef"],
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutInsightSelectorsRequestRequestTypeDef = TypedDict(
    "PutInsightSelectorsRequestRequestTypeDef",
    {
        "TrailName": str,
        "InsightSelectors": Sequence["InsightSelectorTypeDef"],
    },
)

PutInsightSelectorsResponseTypeDef = TypedDict(
    "PutInsightSelectorsResponseTypeDef",
    {
        "TrailARN": str,
        "InsightSelectors": List["InsightSelectorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QueryStatisticsForDescribeQueryTypeDef = TypedDict(
    "QueryStatisticsForDescribeQueryTypeDef",
    {
        "EventsMatched": NotRequired[int],
        "EventsScanned": NotRequired[int],
        "BytesScanned": NotRequired[int],
        "ExecutionTimeInMillis": NotRequired[int],
        "CreationTime": NotRequired[datetime],
    },
)

QueryStatisticsTypeDef = TypedDict(
    "QueryStatisticsTypeDef",
    {
        "ResultsCount": NotRequired[int],
        "TotalResultsCount": NotRequired[int],
        "BytesScanned": NotRequired[int],
    },
)

QueryTypeDef = TypedDict(
    "QueryTypeDef",
    {
        "QueryId": NotRequired[str],
        "QueryStatus": NotRequired[QueryStatusType],
        "CreationTime": NotRequired[datetime],
    },
)

RemoveTagsRequestRequestTypeDef = TypedDict(
    "RemoveTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagsList": Sequence["TagTypeDef"],
    },
)

ResourceTagTypeDef = TypedDict(
    "ResourceTagTypeDef",
    {
        "ResourceId": NotRequired[str],
        "TagsList": NotRequired[List["TagTypeDef"]],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceName": NotRequired[str],
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

RestoreEventDataStoreRequestRequestTypeDef = TypedDict(
    "RestoreEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
    },
)

RestoreEventDataStoreResponseTypeDef = TypedDict(
    "RestoreEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartLoggingRequestRequestTypeDef = TypedDict(
    "StartLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartQueryRequestRequestTypeDef = TypedDict(
    "StartQueryRequestRequestTypeDef",
    {
        "QueryStatement": str,
    },
)

StartQueryResponseTypeDef = TypedDict(
    "StartQueryResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopLoggingRequestRequestTypeDef = TypedDict(
    "StopLoggingRequestRequestTypeDef",
    {
        "Name": str,
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TrailInfoTypeDef = TypedDict(
    "TrailInfoTypeDef",
    {
        "TrailARN": NotRequired[str],
        "Name": NotRequired[str],
        "HomeRegion": NotRequired[str],
    },
)

TrailTypeDef = TypedDict(
    "TrailTypeDef",
    {
        "Name": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "SnsTopicARN": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "HomeRegion": NotRequired[str],
        "TrailARN": NotRequired[str],
        "LogFileValidationEnabled": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "HasCustomEventSelectors": NotRequired[bool],
        "HasInsightSelectors": NotRequired[bool],
        "IsOrganizationTrail": NotRequired[bool],
    },
)

UpdateEventDataStoreRequestRequestTypeDef = TypedDict(
    "UpdateEventDataStoreRequestRequestTypeDef",
    {
        "EventDataStore": str,
        "Name": NotRequired[str],
        "AdvancedEventSelectors": NotRequired[Sequence["AdvancedEventSelectorTypeDef"]],
        "MultiRegionEnabled": NotRequired[bool],
        "OrganizationEnabled": NotRequired[bool],
        "RetentionPeriod": NotRequired[int],
        "TerminationProtectionEnabled": NotRequired[bool],
    },
)

UpdateEventDataStoreResponseTypeDef = TypedDict(
    "UpdateEventDataStoreResponseTypeDef",
    {
        "EventDataStoreArn": str,
        "Name": str,
        "Status": EventDataStoreStatusType,
        "AdvancedEventSelectors": List["AdvancedEventSelectorTypeDef"],
        "MultiRegionEnabled": bool,
        "OrganizationEnabled": bool,
        "RetentionPeriod": int,
        "TerminationProtectionEnabled": bool,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrailRequestRequestTypeDef = TypedDict(
    "UpdateTrailRequestRequestTypeDef",
    {
        "Name": str,
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "SnsTopicName": NotRequired[str],
        "IncludeGlobalServiceEvents": NotRequired[bool],
        "IsMultiRegionTrail": NotRequired[bool],
        "EnableLogFileValidation": NotRequired[bool],
        "CloudWatchLogsLogGroupArn": NotRequired[str],
        "CloudWatchLogsRoleArn": NotRequired[str],
        "KmsKeyId": NotRequired[str],
        "IsOrganizationTrail": NotRequired[bool],
    },
)

UpdateTrailResponseTypeDef = TypedDict(
    "UpdateTrailResponseTypeDef",
    {
        "Name": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "SnsTopicName": str,
        "SnsTopicARN": str,
        "IncludeGlobalServiceEvents": bool,
        "IsMultiRegionTrail": bool,
        "TrailARN": str,
        "LogFileValidationEnabled": bool,
        "CloudWatchLogsLogGroupArn": str,
        "CloudWatchLogsRoleArn": str,
        "KmsKeyId": str,
        "IsOrganizationTrail": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
