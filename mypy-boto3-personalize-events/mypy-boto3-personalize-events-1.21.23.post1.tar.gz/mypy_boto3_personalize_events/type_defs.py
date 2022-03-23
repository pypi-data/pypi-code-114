"""
Type annotations for personalize-events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import EventTypeDef

    data: EventTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Sequence, Union

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EventTypeDef",
    "ItemTypeDef",
    "PutEventsRequestRequestTypeDef",
    "PutItemsRequestRequestTypeDef",
    "PutUsersRequestRequestTypeDef",
    "UserTypeDef",
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "eventType": str,
        "sentAt": Union[datetime, str],
        "eventId": NotRequired[str],
        "eventValue": NotRequired[float],
        "itemId": NotRequired[str],
        "properties": NotRequired[str],
        "recommendationId": NotRequired[str],
        "impression": NotRequired[Sequence[str]],
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "itemId": str,
        "properties": NotRequired[str],
    },
)

PutEventsRequestRequestTypeDef = TypedDict(
    "PutEventsRequestRequestTypeDef",
    {
        "trackingId": str,
        "sessionId": str,
        "eventList": Sequence["EventTypeDef"],
        "userId": NotRequired[str],
    },
)

PutItemsRequestRequestTypeDef = TypedDict(
    "PutItemsRequestRequestTypeDef",
    {
        "datasetArn": str,
        "items": Sequence["ItemTypeDef"],
    },
)

PutUsersRequestRequestTypeDef = TypedDict(
    "PutUsersRequestRequestTypeDef",
    {
        "datasetArn": str,
        "users": Sequence["UserTypeDef"],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "userId": str,
        "properties": NotRequired[str],
    },
)
