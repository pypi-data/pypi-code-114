"""
Type annotations for personalize-runtime service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_personalize_runtime/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_personalize_runtime.type_defs import GetPersonalizedRankingRequestRequestTypeDef

    data: GetPersonalizedRankingRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "GetPersonalizedRankingRequestRequestTypeDef",
    "GetPersonalizedRankingResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "PredictedItemTypeDef",
    "ResponseMetadataTypeDef",
)

GetPersonalizedRankingRequestRequestTypeDef = TypedDict(
    "GetPersonalizedRankingRequestRequestTypeDef",
    {
        "campaignArn": str,
        "inputList": Sequence[str],
        "userId": str,
        "context": NotRequired[Mapping[str, str]],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
    },
)

GetPersonalizedRankingResponseTypeDef = TypedDict(
    "GetPersonalizedRankingResponseTypeDef",
    {
        "personalizedRanking": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "campaignArn": NotRequired[str],
        "itemId": NotRequired[str],
        "userId": NotRequired[str],
        "numResults": NotRequired[int],
        "context": NotRequired[Mapping[str, str]],
        "filterArn": NotRequired[str],
        "filterValues": NotRequired[Mapping[str, str]],
        "recommenderArn": NotRequired[str],
    },
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "itemList": List["PredictedItemTypeDef"],
        "recommendationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedItemTypeDef = TypedDict(
    "PredictedItemTypeDef",
    {
        "itemId": NotRequired[str],
        "score": NotRequired[float],
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
