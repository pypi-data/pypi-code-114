"""
Type annotations for pricing service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_pricing/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_pricing.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "DescribeServicesRequestRequestTypeDef",
    "DescribeServicesResponseTypeDef",
    "FilterTypeDef",
    "GetAttributeValuesRequestRequestTypeDef",
    "GetAttributeValuesResponseTypeDef",
    "GetProductsRequestRequestTypeDef",
    "GetProductsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceTypeDef",
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": NotRequired[str],
    },
)

DescribeServicesRequestRequestTypeDef = TypedDict(
    "DescribeServicesRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "FormatVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {
        "Services": List["ServiceTypeDef"],
        "FormatVersion": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Type": Literal["TERM_MATCH"],
        "Field": str,
        "Value": str,
    },
)

GetAttributeValuesRequestRequestTypeDef = TypedDict(
    "GetAttributeValuesRequestRequestTypeDef",
    {
        "ServiceCode": str,
        "AttributeName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetAttributeValuesResponseTypeDef = TypedDict(
    "GetAttributeValuesResponseTypeDef",
    {
        "AttributeValues": List["AttributeValueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProductsRequestRequestTypeDef = TypedDict(
    "GetProductsRequestRequestTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "FormatVersion": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetProductsResponseTypeDef = TypedDict(
    "GetProductsResponseTypeDef",
    {
        "FormatVersion": str,
        "PriceList": List[str],
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

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ServiceCode": NotRequired[str],
        "AttributeNames": NotRequired[List[str]],
    },
)
