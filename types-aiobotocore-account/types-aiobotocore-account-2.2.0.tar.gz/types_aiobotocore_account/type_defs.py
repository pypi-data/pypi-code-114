"""
Type annotations for account service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_account/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_account.type_defs import AlternateContactTypeDef

    data: AlternateContactTypeDef = {...}
    ```
"""
import sys
from typing import Dict

from typing_extensions import NotRequired

from .literals import AlternateContactTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlternateContactTypeDef",
    "DeleteAlternateContactRequestRequestTypeDef",
    "GetAlternateContactRequestRequestTypeDef",
    "GetAlternateContactResponseTypeDef",
    "PutAlternateContactRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
)

AlternateContactTypeDef = TypedDict(
    "AlternateContactTypeDef",
    {
        "AlternateContactType": NotRequired[AlternateContactTypeType],
        "EmailAddress": NotRequired[str],
        "Name": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "Title": NotRequired[str],
    },
)

DeleteAlternateContactRequestRequestTypeDef = TypedDict(
    "DeleteAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)

GetAlternateContactRequestRequestTypeDef = TypedDict(
    "GetAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "AccountId": NotRequired[str],
    },
)

GetAlternateContactResponseTypeDef = TypedDict(
    "GetAlternateContactResponseTypeDef",
    {
        "AlternateContact": "AlternateContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAlternateContactRequestRequestTypeDef = TypedDict(
    "PutAlternateContactRequestRequestTypeDef",
    {
        "AlternateContactType": AlternateContactTypeType,
        "EmailAddress": str,
        "Name": str,
        "PhoneNumber": str,
        "Title": str,
        "AccountId": NotRequired[str],
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
