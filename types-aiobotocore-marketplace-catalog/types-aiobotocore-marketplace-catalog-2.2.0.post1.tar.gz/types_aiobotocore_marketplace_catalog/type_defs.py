"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_marketplace_catalog.type_defs import CancelChangeSetRequestRequestTypeDef

    data: CancelChangeSetRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import ChangeStatusType, FailureCodeType, SortOrderType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelChangeSetRequestRequestTypeDef",
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "DescribeChangeSetRequestRequestTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityRequestRequestTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "ListChangeSetsRequestRequestTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SortTypeDef",
    "StartChangeSetRequestRequestTypeDef",
    "StartChangeSetResponseTypeDef",
)

CancelChangeSetRequestRequestTypeDef = TypedDict(
    "CancelChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

CancelChangeSetResponseTypeDef = TypedDict(
    "CancelChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChangeSetSummaryListItemTypeDef = TypedDict(
    "ChangeSetSummaryListItemTypeDef",
    {
        "ChangeSetId": NotRequired[str],
        "ChangeSetArn": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "StartTime": NotRequired[str],
        "EndTime": NotRequired[str],
        "Status": NotRequired[ChangeStatusType],
        "EntityIdList": NotRequired[List[str]],
        "FailureCode": NotRequired[FailureCodeType],
    },
)

ChangeSummaryTypeDef = TypedDict(
    "ChangeSummaryTypeDef",
    {
        "ChangeType": NotRequired[str],
        "Entity": NotRequired["EntityTypeDef"],
        "Details": NotRequired[str],
        "ErrorDetailList": NotRequired[List["ErrorDetailTypeDef"]],
        "ChangeName": NotRequired[str],
    },
)

ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "ChangeType": str,
        "Entity": "EntityTypeDef",
        "Details": str,
        "ChangeName": NotRequired[str],
    },
)

DescribeChangeSetRequestRequestTypeDef = TypedDict(
    "DescribeChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSetId": str,
    },
)

DescribeChangeSetResponseTypeDef = TypedDict(
    "DescribeChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ChangeSetName": str,
        "StartTime": str,
        "EndTime": str,
        "Status": ChangeStatusType,
        "FailureCode": FailureCodeType,
        "FailureDescription": str,
        "ChangeSet": List["ChangeSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEntityRequestRequestTypeDef = TypedDict(
    "DescribeEntityRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityId": str,
    },
)

DescribeEntityResponseTypeDef = TypedDict(
    "DescribeEntityResponseTypeDef",
    {
        "EntityType": str,
        "EntityIdentifier": str,
        "EntityArn": str,
        "LastModifiedDate": str,
        "Details": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "Name": NotRequired[str],
        "EntityType": NotRequired[str],
        "EntityId": NotRequired[str],
        "EntityArn": NotRequired[str],
        "LastModifiedDate": NotRequired[str],
        "Visibility": NotRequired[str],
    },
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Type": str,
        "Identifier": NotRequired[str],
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": NotRequired[str],
        "ValueList": NotRequired[Sequence[str]],
    },
)

ListChangeSetsRequestRequestTypeDef = TypedDict(
    "ListChangeSetsRequestRequestTypeDef",
    {
        "Catalog": str,
        "FilterList": NotRequired[Sequence["FilterTypeDef"]],
        "Sort": NotRequired["SortTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChangeSetsResponseTypeDef = TypedDict(
    "ListChangeSetsResponseTypeDef",
    {
        "ChangeSetSummaryList": List["ChangeSetSummaryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesRequestRequestTypeDef = TypedDict(
    "ListEntitiesRequestRequestTypeDef",
    {
        "Catalog": str,
        "EntityType": str,
        "FilterList": NotRequired[Sequence["FilterTypeDef"]],
        "Sort": NotRequired["SortTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "EntitySummaryList": List["EntitySummaryTypeDef"],
        "NextToken": str,
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

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "SortBy": NotRequired[str],
        "SortOrder": NotRequired[SortOrderType],
    },
)

StartChangeSetRequestRequestTypeDef = TypedDict(
    "StartChangeSetRequestRequestTypeDef",
    {
        "Catalog": str,
        "ChangeSet": Sequence["ChangeTypeDef"],
        "ChangeSetName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)

StartChangeSetResponseTypeDef = TypedDict(
    "StartChangeSetResponseTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
