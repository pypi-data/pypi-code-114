"""
Type annotations for marketplace-entitlement service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef

    data: EntitlementTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import GetEntitlementFilterNameType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EntitlementTypeDef",
    "EntitlementValueTypeDef",
    "GetEntitlementsRequestRequestTypeDef",
    "GetEntitlementsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
)

EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "ProductCode": NotRequired[str],
        "Dimension": NotRequired[str],
        "CustomerIdentifier": NotRequired[str],
        "Value": NotRequired["EntitlementValueTypeDef"],
        "ExpirationDate": NotRequired[datetime],
    },
)

EntitlementValueTypeDef = TypedDict(
    "EntitlementValueTypeDef",
    {
        "IntegerValue": NotRequired[int],
        "DoubleValue": NotRequired[float],
        "BooleanValue": NotRequired[bool],
        "StringValue": NotRequired[str],
    },
)

GetEntitlementsRequestRequestTypeDef = TypedDict(
    "GetEntitlementsRequestRequestTypeDef",
    {
        "ProductCode": str,
        "Filter": NotRequired[Mapping[GetEntitlementFilterNameType, Sequence[str]]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetEntitlementsResultTypeDef = TypedDict(
    "GetEntitlementsResultTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
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
