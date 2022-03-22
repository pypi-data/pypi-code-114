"""
Type annotations for sdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
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
    "AttributeTypeDef",
    "BatchDeleteAttributesRequestRequestTypeDef",
    "BatchPutAttributesRequestRequestTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "DeletableItemTypeDef",
    "DeleteAttributesRequestRequestTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DomainMetadataRequestRequestTypeDef",
    "DomainMetadataResultTypeDef",
    "GetAttributesRequestRequestTypeDef",
    "GetAttributesResultTypeDef",
    "ItemTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PutAttributesRequestRequestTypeDef",
    "ReplaceableAttributeTypeDef",
    "ReplaceableItemTypeDef",
    "ResponseMetadataTypeDef",
    "SelectRequestRequestTypeDef",
    "SelectResultTypeDef",
    "UpdateConditionTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Name": str,
        "Value": str,
        "AlternateNameEncoding": NotRequired[str],
        "AlternateValueEncoding": NotRequired[str],
    },
)

BatchDeleteAttributesRequestRequestTypeDef = TypedDict(
    "BatchDeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": Sequence["DeletableItemTypeDef"],
    },
)

BatchPutAttributesRequestRequestTypeDef = TypedDict(
    "BatchPutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "Items": Sequence["ReplaceableItemTypeDef"],
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DeletableItemTypeDef = TypedDict(
    "DeletableItemTypeDef",
    {
        "Name": str,
        "Attributes": NotRequired[Sequence["AttributeTypeDef"]],
    },
)

DeleteAttributesRequestRequestTypeDef = TypedDict(
    "DeleteAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": NotRequired[Sequence["AttributeTypeDef"]],
        "Expected": NotRequired["UpdateConditionTypeDef"],
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataRequestRequestTypeDef = TypedDict(
    "DomainMetadataRequestRequestTypeDef",
    {
        "DomainName": str,
    },
)

DomainMetadataResultTypeDef = TypedDict(
    "DomainMetadataResultTypeDef",
    {
        "ItemCount": int,
        "ItemNamesSizeBytes": int,
        "AttributeNameCount": int,
        "AttributeNamesSizeBytes": int,
        "AttributeValueCount": int,
        "AttributeValuesSizeBytes": int,
        "Timestamp": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttributesRequestRequestTypeDef = TypedDict(
    "GetAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "AttributeNames": NotRequired[Sequence[str]],
        "ConsistentRead": NotRequired[bool],
    },
)

GetAttributesResultTypeDef = TypedDict(
    "GetAttributesResultTypeDef",
    {
        "Attributes": List["AttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": str,
        "Attributes": List["AttributeTypeDef"],
        "AlternateNameEncoding": NotRequired[str],
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "MaxNumberOfDomains": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "DomainNames": List[str],
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

PutAttributesRequestRequestTypeDef = TypedDict(
    "PutAttributesRequestRequestTypeDef",
    {
        "DomainName": str,
        "ItemName": str,
        "Attributes": Sequence["ReplaceableAttributeTypeDef"],
        "Expected": NotRequired["UpdateConditionTypeDef"],
    },
)

ReplaceableAttributeTypeDef = TypedDict(
    "ReplaceableAttributeTypeDef",
    {
        "Name": str,
        "Value": str,
        "Replace": NotRequired[bool],
    },
)

ReplaceableItemTypeDef = TypedDict(
    "ReplaceableItemTypeDef",
    {
        "Name": str,
        "Attributes": Sequence["ReplaceableAttributeTypeDef"],
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

SelectRequestRequestTypeDef = TypedDict(
    "SelectRequestRequestTypeDef",
    {
        "SelectExpression": str,
        "NextToken": NotRequired[str],
        "ConsistentRead": NotRequired[bool],
    },
)

SelectResultTypeDef = TypedDict(
    "SelectResultTypeDef",
    {
        "Items": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConditionTypeDef = TypedDict(
    "UpdateConditionTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[str],
        "Exists": NotRequired[bool],
    },
)
