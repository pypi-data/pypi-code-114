"""
Type annotations for dynamodbstreams service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_dynamodbstreams/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_dynamodbstreams.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from typing_extensions import NotRequired

from .literals import (
    KeyTypeType,
    OperationTypeType,
    ShardIteratorTypeType,
    StreamStatusType,
    StreamViewTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "GetShardIteratorOutputTypeDef",
    "IdentityTypeDef",
    "KeySchemaElementTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListStreamsOutputTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "SequenceNumberRangeTypeDef",
    "ShardTypeDef",
    "StreamDescriptionTypeDef",
    "StreamRecordTypeDef",
    "StreamTypeDef",
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[str],
        "B": NotRequired[bytes],
        "SS": NotRequired[List[str]],
        "NS": NotRequired[List[str]],
        "BS": NotRequired[List[bytes]],
        "M": NotRequired[Dict[str, Dict[str, Any]]],
        "L": NotRequired[List[Dict[str, Any]]],
        "NULL": NotRequired[bool],
        "BOOL": NotRequired[bool],
    },
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamArn": str,
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
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetShardIteratorInputRequestTypeDef = TypedDict(
    "GetShardIteratorInputRequestTypeDef",
    {
        "StreamArn": str,
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
        "SequenceNumber": NotRequired[str],
    },
)

GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "Type": NotRequired[str],
    },
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "AttributeName": str,
        "KeyType": KeyTypeType,
    },
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "TableName": NotRequired[str],
        "Limit": NotRequired[int],
        "ExclusiveStartStreamArn": NotRequired[str],
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "Streams": List["StreamTypeDef"],
        "LastEvaluatedStreamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "eventID": NotRequired[str],
        "eventName": NotRequired[OperationTypeType],
        "eventVersion": NotRequired[str],
        "eventSource": NotRequired[str],
        "awsRegion": NotRequired[str],
        "dynamodb": NotRequired["StreamRecordTypeDef"],
        "userIdentity": NotRequired["IdentityTypeDef"],
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
        "StartingSequenceNumber": NotRequired[str],
        "EndingSequenceNumber": NotRequired[str],
    },
)

ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "ShardId": NotRequired[str],
        "SequenceNumberRange": NotRequired["SequenceNumberRangeTypeDef"],
        "ParentShardId": NotRequired[str],
    },
)

StreamDescriptionTypeDef = TypedDict(
    "StreamDescriptionTypeDef",
    {
        "StreamArn": NotRequired[str],
        "StreamLabel": NotRequired[str],
        "StreamStatus": NotRequired[StreamStatusType],
        "StreamViewType": NotRequired[StreamViewTypeType],
        "CreationRequestDateTime": NotRequired[datetime],
        "TableName": NotRequired[str],
        "KeySchema": NotRequired[List["KeySchemaElementTypeDef"]],
        "Shards": NotRequired[List["ShardTypeDef"]],
        "LastEvaluatedShardId": NotRequired[str],
    },
)

StreamRecordTypeDef = TypedDict(
    "StreamRecordTypeDef",
    {
        "ApproximateCreationDateTime": NotRequired[datetime],
        "Keys": NotRequired[Dict[str, "AttributeValueTypeDef"]],
        "NewImage": NotRequired[Dict[str, "AttributeValueTypeDef"]],
        "OldImage": NotRequired[Dict[str, "AttributeValueTypeDef"]],
        "SequenceNumber": NotRequired[str],
        "SizeBytes": NotRequired[int],
        "StreamViewType": NotRequired[StreamViewTypeType],
    },
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "StreamArn": NotRequired[str],
        "TableName": NotRequired[str],
        "StreamLabel": NotRequired[str],
    },
)
