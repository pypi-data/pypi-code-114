"""
Type annotations for sagemaker-featurestore-runtime service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sagemaker_featurestore_runtime/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sagemaker_featurestore_runtime.type_defs import BatchGetRecordErrorTypeDef

    data: BatchGetRecordErrorTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchGetRecordErrorTypeDef",
    "BatchGetRecordIdentifierTypeDef",
    "BatchGetRecordRequestRequestTypeDef",
    "BatchGetRecordResponseTypeDef",
    "BatchGetRecordResultDetailTypeDef",
    "DeleteRecordRequestRequestTypeDef",
    "FeatureValueTypeDef",
    "GetRecordRequestRequestTypeDef",
    "GetRecordResponseTypeDef",
    "PutRecordRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
)

BatchGetRecordErrorTypeDef = TypedDict(
    "BatchGetRecordErrorTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
)

BatchGetRecordIdentifierTypeDef = TypedDict(
    "BatchGetRecordIdentifierTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifiersValueAsString": Sequence[str],
        "FeatureNames": NotRequired[Sequence[str]],
    },
)

BatchGetRecordRequestRequestTypeDef = TypedDict(
    "BatchGetRecordRequestRequestTypeDef",
    {
        "Identifiers": Sequence["BatchGetRecordIdentifierTypeDef"],
    },
)

BatchGetRecordResponseTypeDef = TypedDict(
    "BatchGetRecordResponseTypeDef",
    {
        "Records": List["BatchGetRecordResultDetailTypeDef"],
        "Errors": List["BatchGetRecordErrorTypeDef"],
        "UnprocessedIdentifiers": List["BatchGetRecordIdentifierTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRecordResultDetailTypeDef = TypedDict(
    "BatchGetRecordResultDetailTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "Record": List["FeatureValueTypeDef"],
    },
)

DeleteRecordRequestRequestTypeDef = TypedDict(
    "DeleteRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "EventTime": str,
    },
)

FeatureValueTypeDef = TypedDict(
    "FeatureValueTypeDef",
    {
        "FeatureName": str,
        "ValueAsString": str,
    },
)

GetRecordRequestRequestTypeDef = TypedDict(
    "GetRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "RecordIdentifierValueAsString": str,
        "FeatureNames": NotRequired[Sequence[str]],
    },
)

GetRecordResponseTypeDef = TypedDict(
    "GetRecordResponseTypeDef",
    {
        "Record": List["FeatureValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRecordRequestRequestTypeDef = TypedDict(
    "PutRecordRequestRequestTypeDef",
    {
        "FeatureGroupName": str,
        "Record": Sequence["FeatureValueTypeDef"],
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
