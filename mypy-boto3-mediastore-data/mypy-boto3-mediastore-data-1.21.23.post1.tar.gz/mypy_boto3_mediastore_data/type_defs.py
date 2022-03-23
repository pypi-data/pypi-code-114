"""
Type annotations for mediastore-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import DeleteObjectRequestRequestTypeDef

    data: DeleteObjectRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import ItemTypeType, UploadAvailabilityType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteObjectRequestRequestTypeDef",
    "DescribeObjectRequestRequestTypeDef",
    "DescribeObjectResponseTypeDef",
    "GetObjectRequestRequestTypeDef",
    "GetObjectResponseTypeDef",
    "ItemTypeDef",
    "ListItemsRequestRequestTypeDef",
    "ListItemsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectRequestRequestTypeDef",
    "PutObjectResponseTypeDef",
    "ResponseMetadataTypeDef",
)

DeleteObjectRequestRequestTypeDef = TypedDict(
    "DeleteObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectRequestRequestTypeDef = TypedDict(
    "DescribeObjectRequestRequestTypeDef",
    {
        "Path": str,
    },
)

DescribeObjectResponseTypeDef = TypedDict(
    "DescribeObjectResponseTypeDef",
    {
        "ETag": str,
        "ContentType": str,
        "ContentLength": int,
        "CacheControl": str,
        "LastModified": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetObjectRequestRequestTypeDef = TypedDict(
    "GetObjectRequestRequestTypeDef",
    {
        "Path": str,
        "Range": NotRequired[str],
    },
)

GetObjectResponseTypeDef = TypedDict(
    "GetObjectResponseTypeDef",
    {
        "Body": StreamingBody,
        "CacheControl": str,
        "ContentRange": str,
        "ContentLength": int,
        "ContentType": str,
        "ETag": str,
        "LastModified": datetime,
        "StatusCode": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": NotRequired[str],
        "Type": NotRequired[ItemTypeType],
        "ETag": NotRequired[str],
        "LastModified": NotRequired[datetime],
        "ContentType": NotRequired[str],
        "ContentLength": NotRequired[int],
    },
)

ListItemsRequestRequestTypeDef = TypedDict(
    "ListItemsRequestRequestTypeDef",
    {
        "Path": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListItemsResponseTypeDef = TypedDict(
    "ListItemsResponseTypeDef",
    {
        "Items": List["ItemTypeDef"],
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

PutObjectRequestRequestTypeDef = TypedDict(
    "PutObjectRequestRequestTypeDef",
    {
        "Body": Union[bytes, IO[bytes], StreamingBody],
        "Path": str,
        "ContentType": NotRequired[str],
        "CacheControl": NotRequired[str],
        "StorageClass": NotRequired[Literal["TEMPORAL"]],
        "UploadAvailability": NotRequired[UploadAvailabilityType],
    },
)

PutObjectResponseTypeDef = TypedDict(
    "PutObjectResponseTypeDef",
    {
        "ContentSHA256": str,
        "ETag": str,
        "StorageClass": Literal["TEMPORAL"],
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
