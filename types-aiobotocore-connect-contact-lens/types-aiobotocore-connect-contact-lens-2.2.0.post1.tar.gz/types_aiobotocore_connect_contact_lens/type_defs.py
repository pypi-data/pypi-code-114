"""
Type annotations for connect-contact-lens service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_connect_contact_lens/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_connect_contact_lens.type_defs import CategoriesTypeDef

    data: CategoriesTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from typing_extensions import NotRequired

from .literals import SentimentValueType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CategoriesTypeDef",
    "CategoryDetailsTypeDef",
    "CharacterOffsetsTypeDef",
    "IssueDetectedTypeDef",
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    "PointOfInterestTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "ResponseMetadataTypeDef",
    "TranscriptTypeDef",
)

CategoriesTypeDef = TypedDict(
    "CategoriesTypeDef",
    {
        "MatchedCategories": List[str],
        "MatchedDetails": Dict[str, "CategoryDetailsTypeDef"],
    },
)

CategoryDetailsTypeDef = TypedDict(
    "CategoryDetailsTypeDef",
    {
        "PointsOfInterest": List["PointOfInterestTypeDef"],
    },
)

CharacterOffsetsTypeDef = TypedDict(
    "CharacterOffsetsTypeDef",
    {
        "BeginOffsetChar": int,
        "EndOffsetChar": int,
    },
)

IssueDetectedTypeDef = TypedDict(
    "IssueDetectedTypeDef",
    {
        "CharacterOffsets": "CharacterOffsetsTypeDef",
    },
)

ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ContactId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRealtimeContactAnalysisSegmentsResponseTypeDef = TypedDict(
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    {
        "Segments": List["RealtimeContactAnalysisSegmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PointOfInterestTypeDef = TypedDict(
    "PointOfInterestTypeDef",
    {
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
    },
)

RealtimeContactAnalysisSegmentTypeDef = TypedDict(
    "RealtimeContactAnalysisSegmentTypeDef",
    {
        "Transcript": NotRequired["TranscriptTypeDef"],
        "Categories": NotRequired["CategoriesTypeDef"],
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

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef",
    {
        "Id": str,
        "ParticipantId": str,
        "ParticipantRole": str,
        "Content": str,
        "BeginOffsetMillis": int,
        "EndOffsetMillis": int,
        "Sentiment": SentimentValueType,
        "IssuesDetected": NotRequired[List["IssueDetectedTypeDef"]],
    },
)
