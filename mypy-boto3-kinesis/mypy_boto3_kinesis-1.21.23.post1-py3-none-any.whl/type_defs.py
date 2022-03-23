"""
Type annotations for kinesis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import AddTagsToStreamInputRequestTypeDef

    data: AddTagsToStreamInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ConsumerStatusType,
    EncryptionTypeType,
    MetricsNameType,
    ShardFilterTypeType,
    ShardIteratorTypeType,
    StreamModeType,
    StreamStatusType,
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
    "AddTagsToStreamInputRequestTypeDef",
    "ChildShardTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "CreateStreamInputRequestTypeDef",
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DeregisterStreamConsumerInputRequestTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerInputRequestTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "DescribeStreamSummaryInputRequestTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "DisableEnhancedMonitoringInputRequestTypeDef",
    "EnableEnhancedMonitoringInputRequestTypeDef",
    "EnhancedMetricsTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "GetShardIteratorOutputTypeDef",
    "HashKeyRangeTypeDef",
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListShardsInputRequestTypeDef",
    "ListShardsOutputTypeDef",
    "ListStreamConsumersInputRequestTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "MergeShardsInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordOutputTypeDef",
    "PutRecordsInputRequestTypeDef",
    "PutRecordsOutputTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "PutRecordsResultEntryTypeDef",
    "RecordTypeDef",
    "RegisterStreamConsumerInputRequestTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "RemoveTagsFromStreamInputRequestTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardFilterTypeDef",
    "ShardTypeDef",
    "SplitShardInputRequestTypeDef",
    "StartStreamEncryptionInputRequestTypeDef",
    "StartingPositionTypeDef",
    "StopStreamEncryptionInputRequestTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "StreamDescriptionTypeDef",
    "StreamModeDetailsTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "SubscribeToShardEventTypeDef",
    "SubscribeToShardInputRequestTypeDef",
    "SubscribeToShardOutputTypeDef",
    "TagTypeDef",
    "UpdateShardCountInputRequestTypeDef",
    "UpdateShardCountOutputTypeDef",
    "UpdateStreamModeInputRequestTypeDef",
    "WaiterConfigTypeDef",
)

AddTagsToStreamInputRequestTypeDef = TypedDict(
    "AddTagsToStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "Tags": Mapping[str, str],
    },
)

ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {
        "ShardId": str,
        "ParentShards": List[str],
        "HashKeyRange": "HashKeyRangeTypeDef",
    },
)

ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)

ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
    },
)

CreateStreamInputRequestTypeDef = TypedDict(
    "CreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardCount": NotRequired[int],
        "StreamModeDetails": NotRequired["StreamModeDetailsTypeDef"],
    },
)

DecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "EnforceConsumerDeletion": NotRequired[bool],
    },
)

DeregisterStreamConsumerInputRequestTypeDef = TypedDict(
    "DeregisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": NotRequired[str],
        "ConsumerName": NotRequired[str],
        "ConsumerARN": NotRequired[str],
    },
)

DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "ShardLimit": int,
        "OpenShardCount": int,
        "OnDemandStreamCount": int,
        "OnDemandStreamCountLimit": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamConsumerInputRequestTypeDef = TypedDict(
    "DescribeStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": NotRequired[str],
        "ConsumerName": NotRequired[str],
        "ConsumerARN": NotRequired[str],
    },
)

DescribeStreamConsumerOutputTypeDef = TypedDict(
    "DescribeStreamConsumerOutputTypeDef",
    {
        "ConsumerDescription": "ConsumerDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "Limit": NotRequired[int],
        "ExclusiveStartShardId": NotRequired[str],
    },
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamDescription": "StreamDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStreamSummaryInputRequestTypeDef = TypedDict(
    "DescribeStreamSummaryInputRequestTypeDef",
    {
        "StreamName": str,
    },
)

DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {
        "StreamDescriptionSummary": "StreamDescriptionSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "DisableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": Sequence[MetricsNameType],
    },
)

EnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "EnableEnhancedMonitoringInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardLevelMetrics": Sequence[MetricsNameType],
    },
)

EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": NotRequired[List[MetricsNameType]],
    },
)

EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsNameType],
        "DesiredShardLevelMetrics": List[MetricsNameType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecordsInputRequestTypeDef = TypedDict(
    "GetRecordsInputRequestTypeDef",
    {
        "ShardIterator": str,
        "Limit": NotRequired[int],
    },
)

GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List["ChildShardTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetShardIteratorInputRequestTypeDef = TypedDict(
    "GetShardIteratorInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
        "StartingSequenceNumber": NotRequired[str],
        "Timestamp": NotRequired[Union[datetime, str]],
    },
)

GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef",
    {
        "StartingHashKey": str,
        "EndingHashKey": str,
    },
)

IncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "StreamName": str,
        "RetentionPeriodHours": int,
    },
)

InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSOptInRequiredTypeDef = TypedDict(
    "KMSOptInRequiredTypeDef",
    {
        "message": NotRequired[str],
    },
)

KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

ListShardsInputRequestTypeDef = TypedDict(
    "ListShardsInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "NextToken": NotRequired[str],
        "ExclusiveStartShardId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StreamCreationTimestamp": NotRequired[Union[datetime, str]],
        "ShardFilter": NotRequired["ShardFilterTypeDef"],
    },
)

ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef",
    {
        "Shards": List["ShardTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamConsumersInputRequestTypeDef = TypedDict(
    "ListStreamConsumersInputRequestTypeDef",
    {
        "StreamARN": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StreamCreationTimestamp": NotRequired[Union[datetime, str]],
    },
)

ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {
        "Consumers": List["ConsumerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "ExclusiveStartStreamName": NotRequired[str],
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ExclusiveStartTagKey": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "HasMoreTags": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeShardsInputRequestTypeDef = TypedDict(
    "MergeShardsInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
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

PutRecordInputRequestTypeDef = TypedDict(
    "PutRecordInputRequestTypeDef",
    {
        "StreamName": str,
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
        "ExplicitHashKey": NotRequired[str],
        "SequenceNumberForOrdering": NotRequired[str],
    },
)

PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "ShardId": str,
        "SequenceNumber": str,
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordsInputRequestTypeDef = TypedDict(
    "PutRecordsInputRequestTypeDef",
    {
        "Records": Sequence["PutRecordsRequestEntryTypeDef"],
        "StreamName": str,
    },
)

PutRecordsOutputTypeDef = TypedDict(
    "PutRecordsOutputTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List["PutRecordsResultEntryTypeDef"],
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordsRequestEntryTypeDef = TypedDict(
    "PutRecordsRequestEntryTypeDef",
    {
        "Data": Union[bytes, IO[bytes], StreamingBody],
        "PartitionKey": str,
        "ExplicitHashKey": NotRequired[str],
    },
)

PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {
        "SequenceNumber": NotRequired[str],
        "ShardId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "SequenceNumber": str,
        "Data": bytes,
        "PartitionKey": str,
        "ApproximateArrivalTimestamp": NotRequired[datetime],
        "EncryptionType": NotRequired[EncryptionTypeType],
    },
)

RegisterStreamConsumerInputRequestTypeDef = TypedDict(
    "RegisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
    },
)

RegisterStreamConsumerOutputTypeDef = TypedDict(
    "RegisterStreamConsumerOutputTypeDef",
    {
        "Consumer": "ConsumerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "RemoveTagsFromStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "TagKeys": Sequence[str],
    },
)

ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)

ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": NotRequired[str],
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

SequenceNumberRangeTypeDef = TypedDict(
    "SequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": str,
        "EndingSequenceNumber": NotRequired[str],
    },
)

ShardFilterTypeDef = TypedDict(
    "ShardFilterTypeDef",
    {
        "Type": ShardFilterTypeType,
        "ShardId": NotRequired[str],
        "Timestamp": NotRequired[Union[datetime, str]],
    },
)

ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": "HashKeyRangeTypeDef",
        "SequenceNumberRange": "SequenceNumberRangeTypeDef",
        "ParentShardId": NotRequired[str],
        "AdjacentParentShardId": NotRequired[str],
    },
)

SplitShardInputRequestTypeDef = TypedDict(
    "SplitShardInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardToSplit": str,
        "NewStartingHashKey": str,
    },
)

StartStreamEncryptionInputRequestTypeDef = TypedDict(
    "StartStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

StartingPositionTypeDef = TypedDict(
    "StartingPositionTypeDef",
    {
        "Type": ShardIteratorTypeType,
        "SequenceNumber": NotRequired[str],
        "Timestamp": NotRequired[Union[datetime, str]],
    },
)

StopStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopStreamEncryptionInputRequestTypeDef",
    {
        "StreamName": str,
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
    },
)

StreamDescriptionSummaryTypeDef = TypedDict(
    "StreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "OpenShardCount": int,
        "StreamModeDetails": NotRequired["StreamModeDetailsTypeDef"],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KeyId": NotRequired[str],
        "ConsumerCount": NotRequired[int],
    },
)

StreamDescriptionTypeDef = TypedDict(
    "StreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "Shards": List["ShardTypeDef"],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List["EnhancedMetricsTypeDef"],
        "StreamModeDetails": NotRequired["StreamModeDetailsTypeDef"],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KeyId": NotRequired[str],
    },
)

StreamModeDetailsTypeDef = TypedDict(
    "StreamModeDetailsTypeDef",
    {
        "StreamMode": StreamModeType,
    },
)

SubscribeToShardEventStreamTypeDef = TypedDict(
    "SubscribeToShardEventStreamTypeDef",
    {
        "SubscribeToShardEvent": "SubscribeToShardEventTypeDef",
        "ResourceNotFoundException": NotRequired["ResourceNotFoundExceptionTypeDef"],
        "ResourceInUseException": NotRequired["ResourceInUseExceptionTypeDef"],
        "KMSDisabledException": NotRequired["KMSDisabledExceptionTypeDef"],
        "KMSInvalidStateException": NotRequired["KMSInvalidStateExceptionTypeDef"],
        "KMSAccessDeniedException": NotRequired["KMSAccessDeniedExceptionTypeDef"],
        "KMSNotFoundException": NotRequired["KMSNotFoundExceptionTypeDef"],
        "KMSOptInRequired": NotRequired["KMSOptInRequiredTypeDef"],
        "KMSThrottlingException": NotRequired["KMSThrottlingExceptionTypeDef"],
        "InternalFailureException": NotRequired["InternalFailureExceptionTypeDef"],
    },
)

SubscribeToShardEventTypeDef = TypedDict(
    "SubscribeToShardEventTypeDef",
    {
        "Records": List["RecordTypeDef"],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
        "ChildShards": NotRequired[List["ChildShardTypeDef"]],
    },
)

SubscribeToShardInputRequestTypeDef = TypedDict(
    "SubscribeToShardInputRequestTypeDef",
    {
        "ConsumerARN": str,
        "ShardId": str,
        "StartingPosition": "StartingPositionTypeDef",
    },
)

SubscribeToShardOutputTypeDef = TypedDict(
    "SubscribeToShardOutputTypeDef",
    {
        "EventStream": "SubscribeToShardEventStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

UpdateShardCountInputRequestTypeDef = TypedDict(
    "UpdateShardCountInputRequestTypeDef",
    {
        "StreamName": str,
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
    },
)

UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStreamModeInputRequestTypeDef = TypedDict(
    "UpdateStreamModeInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamModeDetails": "StreamModeDetailsTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
