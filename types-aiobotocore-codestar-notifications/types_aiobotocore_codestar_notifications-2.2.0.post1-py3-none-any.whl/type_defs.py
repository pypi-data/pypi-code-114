"""
Type annotations for codestar-notifications service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_codestar_notifications/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_codestar_notifications.type_defs import CreateNotificationRuleRequestRequestTypeDef

    data: CreateNotificationRuleRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    DetailTypeType,
    ListEventTypesFilterNameType,
    ListNotificationRulesFilterNameType,
    ListTargetsFilterNameType,
    NotificationRuleStatusType,
    TargetStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateNotificationRuleRequestRequestTypeDef",
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleRequestRequestTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "DeleteTargetRequestRequestTypeDef",
    "DescribeNotificationRuleRequestRequestTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "EventTypeSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesRequestRequestTypeDef",
    "ListEventTypesResultTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesRequestRequestTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsRequestRequestTypeDef",
    "ListTargetsResultTypeDef",
    "NotificationRuleSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SubscribeRequestRequestTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagResourceResultTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UnsubscribeRequestRequestTypeDef",
    "UnsubscribeResultTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateNotificationRuleRequestRequestTypeDef",
)

CreateNotificationRuleRequestRequestTypeDef = TypedDict(
    "CreateNotificationRuleRequestRequestTypeDef",
    {
        "Name": str,
        "EventTypeIds": Sequence[str],
        "Resource": str,
        "Targets": Sequence["TargetTypeDef"],
        "DetailType": DetailTypeType,
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Status": NotRequired[NotificationRuleStatusType],
    },
)

CreateNotificationRuleResultTypeDef = TypedDict(
    "CreateNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNotificationRuleRequestRequestTypeDef = TypedDict(
    "DeleteNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DeleteNotificationRuleResultTypeDef = TypedDict(
    "DeleteNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTargetRequestRequestTypeDef = TypedDict(
    "DeleteTargetRequestRequestTypeDef",
    {
        "TargetAddress": str,
        "ForceUnsubscribeAll": NotRequired[bool],
    },
)

DescribeNotificationRuleRequestRequestTypeDef = TypedDict(
    "DescribeNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

DescribeNotificationRuleResultTypeDef = TypedDict(
    "DescribeNotificationRuleResultTypeDef",
    {
        "Arn": str,
        "Name": str,
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "Resource": str,
        "Targets": List["TargetSummaryTypeDef"],
        "DetailType": DetailTypeType,
        "CreatedBy": str,
        "Status": NotificationRuleStatusType,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {
        "EventTypeId": NotRequired[str],
        "ServiceName": NotRequired[str],
        "EventTypeName": NotRequired[str],
        "ResourceType": NotRequired[str],
    },
)

ListEventTypesFilterTypeDef = TypedDict(
    "ListEventTypesFilterTypeDef",
    {
        "Name": ListEventTypesFilterNameType,
        "Value": str,
    },
)

ListEventTypesRequestRequestTypeDef = TypedDict(
    "ListEventTypesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ListEventTypesFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEventTypesResultTypeDef = TypedDict(
    "ListEventTypesResultTypeDef",
    {
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNotificationRulesFilterTypeDef = TypedDict(
    "ListNotificationRulesFilterTypeDef",
    {
        "Name": ListNotificationRulesFilterNameType,
        "Value": str,
    },
)

ListNotificationRulesRequestRequestTypeDef = TypedDict(
    "ListNotificationRulesRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ListNotificationRulesFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListNotificationRulesResultTypeDef = TypedDict(
    "ListNotificationRulesResultTypeDef",
    {
        "NextToken": str,
        "NotificationRules": List["NotificationRuleSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "Arn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsFilterTypeDef = TypedDict(
    "ListTargetsFilterTypeDef",
    {
        "Name": ListTargetsFilterNameType,
        "Value": str,
    },
)

ListTargetsRequestRequestTypeDef = TypedDict(
    "ListTargetsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["ListTargetsFilterTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTargetsResultTypeDef = TypedDict(
    "ListTargetsResultTypeDef",
    {
        "Targets": List["TargetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationRuleSummaryTypeDef = TypedDict(
    "NotificationRuleSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
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

SubscribeRequestRequestTypeDef = TypedDict(
    "SubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "Target": "TargetTypeDef",
        "ClientRequestToken": NotRequired[str],
    },
)

SubscribeResultTypeDef = TypedDict(
    "SubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "Tags": Mapping[str, str],
    },
)

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {
        "TargetAddress": NotRequired[str],
        "TargetType": NotRequired[str],
        "TargetStatus": NotRequired[TargetStatusType],
    },
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "TargetType": NotRequired[str],
        "TargetAddress": NotRequired[str],
    },
)

UnsubscribeRequestRequestTypeDef = TypedDict(
    "UnsubscribeRequestRequestTypeDef",
    {
        "Arn": str,
        "TargetAddress": str,
    },
)

UnsubscribeResultTypeDef = TypedDict(
    "UnsubscribeResultTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateNotificationRuleRequestRequestTypeDef = TypedDict(
    "UpdateNotificationRuleRequestRequestTypeDef",
    {
        "Arn": str,
        "Name": NotRequired[str],
        "Status": NotRequired[NotificationRuleStatusType],
        "EventTypeIds": NotRequired[Sequence[str]],
        "Targets": NotRequired[Sequence["TargetTypeDef"]],
        "DetailType": NotRequired[DetailTypeType],
    },
)
