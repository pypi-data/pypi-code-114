"""
Type annotations for ebs service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ebs/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ebs.type_defs import BlockTypeDef

    data: BlockTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import StatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BlockTypeDef",
    "ChangedBlockTypeDef",
    "CompleteSnapshotRequestRequestTypeDef",
    "CompleteSnapshotResponseTypeDef",
    "GetSnapshotBlockRequestRequestTypeDef",
    "GetSnapshotBlockResponseTypeDef",
    "ListChangedBlocksRequestRequestTypeDef",
    "ListChangedBlocksResponseTypeDef",
    "ListSnapshotBlocksRequestRequestTypeDef",
    "ListSnapshotBlocksResponseTypeDef",
    "PutSnapshotBlockRequestRequestTypeDef",
    "PutSnapshotBlockResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartSnapshotRequestRequestTypeDef",
    "StartSnapshotResponseTypeDef",
    "TagTypeDef",
)

BlockTypeDef = TypedDict(
    "BlockTypeDef",
    {
        "BlockIndex": NotRequired[int],
        "BlockToken": NotRequired[str],
    },
)

ChangedBlockTypeDef = TypedDict(
    "ChangedBlockTypeDef",
    {
        "BlockIndex": NotRequired[int],
        "FirstBlockToken": NotRequired[str],
        "SecondBlockToken": NotRequired[str],
    },
)

CompleteSnapshotRequestRequestTypeDef = TypedDict(
    "CompleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "ChangedBlocksCount": int,
        "Checksum": NotRequired[str],
        "ChecksumAlgorithm": NotRequired[Literal["SHA256"]],
        "ChecksumAggregationMethod": NotRequired[Literal["LINEAR"]],
    },
)

CompleteSnapshotResponseTypeDef = TypedDict(
    "CompleteSnapshotResponseTypeDef",
    {
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotBlockRequestRequestTypeDef = TypedDict(
    "GetSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockToken": str,
    },
)

GetSnapshotBlockResponseTypeDef = TypedDict(
    "GetSnapshotBlockResponseTypeDef",
    {
        "DataLength": int,
        "BlockData": StreamingBody,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChangedBlocksRequestRequestTypeDef = TypedDict(
    "ListChangedBlocksRequestRequestTypeDef",
    {
        "SecondSnapshotId": str,
        "FirstSnapshotId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartingBlockIndex": NotRequired[int],
    },
)

ListChangedBlocksResponseTypeDef = TypedDict(
    "ListChangedBlocksResponseTypeDef",
    {
        "ChangedBlocks": List["ChangedBlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSnapshotBlocksRequestRequestTypeDef = TypedDict(
    "ListSnapshotBlocksRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartingBlockIndex": NotRequired[int],
    },
)

ListSnapshotBlocksResponseTypeDef = TypedDict(
    "ListSnapshotBlocksResponseTypeDef",
    {
        "Blocks": List["BlockTypeDef"],
        "ExpiryTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSnapshotBlockRequestRequestTypeDef = TypedDict(
    "PutSnapshotBlockRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "BlockIndex": int,
        "BlockData": Union[bytes, IO[bytes], StreamingBody],
        "DataLength": int,
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "Progress": NotRequired[int],
    },
)

PutSnapshotBlockResponseTypeDef = TypedDict(
    "PutSnapshotBlockResponseTypeDef",
    {
        "Checksum": str,
        "ChecksumAlgorithm": Literal["SHA256"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

StartSnapshotRequestRequestTypeDef = TypedDict(
    "StartSnapshotRequestRequestTypeDef",
    {
        "VolumeSize": int,
        "ParentSnapshotId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Encrypted": NotRequired[bool],
        "KmsKeyArn": NotRequired[str],
        "Timeout": NotRequired[int],
    },
)

StartSnapshotResponseTypeDef = TypedDict(
    "StartSnapshotResponseTypeDef",
    {
        "Description": str,
        "SnapshotId": str,
        "OwnerId": str,
        "Status": StatusType,
        "StartTime": datetime,
        "VolumeSize": int,
        "BlockSize": int,
        "Tags": List["TagTypeDef"],
        "ParentSnapshotId": str,
        "KmsKeyArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)
