"""
Type annotations for cloudsearchdomain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef

    data: BucketInfoTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import ContentTypeType, QueryParserType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BucketInfoTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "HitsTypeDef",
    "ResponseMetadataTypeDef",
    "SearchRequestRequestTypeDef",
    "SearchResponseTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestRequestRequestTypeDef",
    "SuggestResponseTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "UploadDocumentsRequestRequestTypeDef",
    "UploadDocumentsResponseTypeDef",
)

BucketInfoTypeDef = TypedDict(
    "BucketInfoTypeDef",
    {
        "buckets": NotRequired[List["BucketTypeDef"]],
    },
)

BucketTypeDef = TypedDict(
    "BucketTypeDef",
    {
        "value": NotRequired[str],
        "count": NotRequired[int],
    },
)

DocumentServiceWarningTypeDef = TypedDict(
    "DocumentServiceWarningTypeDef",
    {
        "message": NotRequired[str],
    },
)

FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": NotRequired[str],
        "max": NotRequired[str],
        "count": NotRequired[int],
        "missing": NotRequired[int],
        "sum": NotRequired[float],
        "sumOfSquares": NotRequired[float],
        "mean": NotRequired[str],
        "stddev": NotRequired[float],
    },
)

HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": NotRequired[str],
        "fields": NotRequired[Dict[str, List[str]]],
        "exprs": NotRequired[Dict[str, str]],
        "highlights": NotRequired[Dict[str, str]],
    },
)

HitsTypeDef = TypedDict(
    "HitsTypeDef",
    {
        "found": NotRequired[int],
        "start": NotRequired[int],
        "cursor": NotRequired[str],
        "hit": NotRequired[List["HitTypeDef"]],
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

SearchRequestRequestTypeDef = TypedDict(
    "SearchRequestRequestTypeDef",
    {
        "query": str,
        "cursor": NotRequired[str],
        "expr": NotRequired[str],
        "facet": NotRequired[str],
        "filterQuery": NotRequired[str],
        "highlight": NotRequired[str],
        "partial": NotRequired[bool],
        "queryOptions": NotRequired[str],
        "queryParser": NotRequired[QueryParserType],
        "returnFields": NotRequired[str],
        "size": NotRequired[int],
        "sort": NotRequired[str],
        "start": NotRequired[int],
        "stats": NotRequired[str],
    },
)

SearchResponseTypeDef = TypedDict(
    "SearchResponseTypeDef",
    {
        "status": "SearchStatusTypeDef",
        "hits": "HitsTypeDef",
        "facets": Dict[str, "BucketInfoTypeDef"],
        "stats": Dict[str, "FieldStatsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchStatusTypeDef = TypedDict(
    "SearchStatusTypeDef",
    {
        "timems": NotRequired[int],
        "rid": NotRequired[str],
    },
)

SuggestModelTypeDef = TypedDict(
    "SuggestModelTypeDef",
    {
        "query": NotRequired[str],
        "found": NotRequired[int],
        "suggestions": NotRequired[List["SuggestionMatchTypeDef"]],
    },
)

SuggestRequestRequestTypeDef = TypedDict(
    "SuggestRequestRequestTypeDef",
    {
        "query": str,
        "suggester": str,
        "size": NotRequired[int],
    },
)

SuggestResponseTypeDef = TypedDict(
    "SuggestResponseTypeDef",
    {
        "status": "SuggestStatusTypeDef",
        "suggest": "SuggestModelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SuggestStatusTypeDef = TypedDict(
    "SuggestStatusTypeDef",
    {
        "timems": NotRequired[int],
        "rid": NotRequired[str],
    },
)

SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef",
    {
        "suggestion": NotRequired[str],
        "score": NotRequired[int],
        "id": NotRequired[str],
    },
)

UploadDocumentsRequestRequestTypeDef = TypedDict(
    "UploadDocumentsRequestRequestTypeDef",
    {
        "documents": Union[bytes, IO[bytes], StreamingBody],
        "contentType": ContentTypeType,
    },
)

UploadDocumentsResponseTypeDef = TypedDict(
    "UploadDocumentsResponseTypeDef",
    {
        "status": str,
        "adds": int,
        "deletes": int,
        "warnings": List["DocumentServiceWarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
