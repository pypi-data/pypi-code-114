"""
Type annotations for ssm-contacts service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_ssm_contacts/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_ssm_contacts.type_defs import AcceptPageRequestRequestTypeDef

    data: AcceptPageRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AcceptCodeValidationType,
    AcceptTypeType,
    ActivationStatusType,
    ChannelTypeType,
    ContactTypeType,
    ReceiptTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptPageRequestRequestTypeDef",
    "ActivateContactChannelRequestRequestTypeDef",
    "ChannelTargetInfoTypeDef",
    "ContactChannelAddressTypeDef",
    "ContactChannelTypeDef",
    "ContactTargetInfoTypeDef",
    "ContactTypeDef",
    "CreateContactChannelRequestRequestTypeDef",
    "CreateContactChannelResultTypeDef",
    "CreateContactRequestRequestTypeDef",
    "CreateContactResultTypeDef",
    "DeactivateContactChannelRequestRequestTypeDef",
    "DeleteContactChannelRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DescribeEngagementRequestRequestTypeDef",
    "DescribeEngagementResultTypeDef",
    "DescribePageRequestRequestTypeDef",
    "DescribePageResultTypeDef",
    "EngagementTypeDef",
    "GetContactChannelRequestRequestTypeDef",
    "GetContactChannelResultTypeDef",
    "GetContactPolicyRequestRequestTypeDef",
    "GetContactPolicyResultTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetContactResultTypeDef",
    "ListContactChannelsRequestRequestTypeDef",
    "ListContactChannelsResultTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListContactsResultTypeDef",
    "ListEngagementsRequestRequestTypeDef",
    "ListEngagementsResultTypeDef",
    "ListPageReceiptsRequestRequestTypeDef",
    "ListPageReceiptsResultTypeDef",
    "ListPagesByContactRequestRequestTypeDef",
    "ListPagesByContactResultTypeDef",
    "ListPagesByEngagementRequestRequestTypeDef",
    "ListPagesByEngagementResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PlanTypeDef",
    "PutContactPolicyRequestRequestTypeDef",
    "ReceiptTypeDef",
    "ResponseMetadataTypeDef",
    "SendActivationCodeRequestRequestTypeDef",
    "StageTypeDef",
    "StartEngagementRequestRequestTypeDef",
    "StartEngagementResultTypeDef",
    "StopEngagementRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContactChannelRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
)

AcceptPageRequestRequestTypeDef = TypedDict(
    "AcceptPageRequestRequestTypeDef",
    {
        "PageId": str,
        "AcceptType": AcceptTypeType,
        "AcceptCode": str,
        "ContactChannelId": NotRequired[str],
        "Note": NotRequired[str],
        "AcceptCodeValidation": NotRequired[AcceptCodeValidationType],
    },
)

ActivateContactChannelRequestRequestTypeDef = TypedDict(
    "ActivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "ActivationCode": str,
    },
)

ChannelTargetInfoTypeDef = TypedDict(
    "ChannelTargetInfoTypeDef",
    {
        "ContactChannelId": str,
        "RetryIntervalInMinutes": NotRequired[int],
    },
)

ContactChannelAddressTypeDef = TypedDict(
    "ContactChannelAddressTypeDef",
    {
        "SimpleAddress": NotRequired[str],
    },
)

ContactChannelTypeDef = TypedDict(
    "ContactChannelTypeDef",
    {
        "ContactChannelArn": str,
        "ContactArn": str,
        "Name": str,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
        "Type": NotRequired[ChannelTypeType],
    },
)

ContactTargetInfoTypeDef = TypedDict(
    "ContactTargetInfoTypeDef",
    {
        "IsEssential": bool,
        "ContactId": NotRequired[str],
    },
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "Type": ContactTypeType,
        "DisplayName": NotRequired[str],
    },
)

CreateContactChannelRequestRequestTypeDef = TypedDict(
    "CreateContactChannelRequestRequestTypeDef",
    {
        "ContactId": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "DeferActivation": NotRequired[bool],
        "IdempotencyToken": NotRequired[str],
    },
)

CreateContactChannelResultTypeDef = TypedDict(
    "CreateContactChannelResultTypeDef",
    {
        "ContactChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactRequestRequestTypeDef = TypedDict(
    "CreateContactRequestRequestTypeDef",
    {
        "Alias": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
        "DisplayName": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "IdempotencyToken": NotRequired[str],
    },
)

CreateContactResultTypeDef = TypedDict(
    "CreateContactResultTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateContactChannelRequestRequestTypeDef = TypedDict(
    "DeactivateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactChannelRequestRequestTypeDef = TypedDict(
    "DeleteContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)

DescribeEngagementRequestRequestTypeDef = TypedDict(
    "DescribeEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
    },
)

DescribeEngagementResultTypeDef = TypedDict(
    "DescribeEngagementResultTypeDef",
    {
        "ContactArn": str,
        "EngagementArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "StartTime": datetime,
        "StopTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePageRequestRequestTypeDef = TypedDict(
    "DescribePageRequestRequestTypeDef",
    {
        "PageId": str,
    },
)

DescribePageResultTypeDef = TypedDict(
    "DescribePageResultTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": str,
        "PublicContent": str,
        "IncidentId": str,
        "SentTime": datetime,
        "ReadTime": datetime,
        "DeliveryTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EngagementTypeDef = TypedDict(
    "EngagementTypeDef",
    {
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "IncidentId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "StopTime": NotRequired[datetime],
    },
)

GetContactChannelRequestRequestTypeDef = TypedDict(
    "GetContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

GetContactChannelResultTypeDef = TypedDict(
    "GetContactChannelResultTypeDef",
    {
        "ContactArn": str,
        "ContactChannelArn": str,
        "Name": str,
        "Type": ChannelTypeType,
        "DeliveryAddress": "ContactChannelAddressTypeDef",
        "ActivationStatus": ActivationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactPolicyRequestRequestTypeDef = TypedDict(
    "GetContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
    },
)

GetContactPolicyResultTypeDef = TypedDict(
    "GetContactPolicyResultTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactId": str,
    },
)

GetContactResultTypeDef = TypedDict(
    "GetContactResultTypeDef",
    {
        "ContactArn": str,
        "Alias": str,
        "DisplayName": str,
        "Type": ContactTypeType,
        "Plan": "PlanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactChannelsRequestRequestTypeDef = TypedDict(
    "ListContactChannelsRequestRequestTypeDef",
    {
        "ContactId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListContactChannelsResultTypeDef = TypedDict(
    "ListContactChannelsResultTypeDef",
    {
        "NextToken": str,
        "ContactChannels": List["ContactChannelTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContactsRequestRequestTypeDef = TypedDict(
    "ListContactsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "AliasPrefix": NotRequired[str],
        "Type": NotRequired[ContactTypeType],
    },
)

ListContactsResultTypeDef = TypedDict(
    "ListContactsResultTypeDef",
    {
        "NextToken": str,
        "Contacts": List["ContactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngagementsRequestRequestTypeDef = TypedDict(
    "ListEngagementsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncidentId": NotRequired[str],
        "TimeRangeValue": NotRequired["TimeRangeTypeDef"],
    },
)

ListEngagementsResultTypeDef = TypedDict(
    "ListEngagementsResultTypeDef",
    {
        "NextToken": str,
        "Engagements": List["EngagementTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPageReceiptsRequestRequestTypeDef = TypedDict(
    "ListPageReceiptsRequestRequestTypeDef",
    {
        "PageId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPageReceiptsResultTypeDef = TypedDict(
    "ListPageReceiptsResultTypeDef",
    {
        "NextToken": str,
        "Receipts": List["ReceiptTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPagesByContactRequestRequestTypeDef = TypedDict(
    "ListPagesByContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPagesByContactResultTypeDef = TypedDict(
    "ListPagesByContactResultTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPagesByEngagementRequestRequestTypeDef = TypedDict(
    "ListPagesByEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPagesByEngagementResultTypeDef = TypedDict(
    "ListPagesByEngagementResultTypeDef",
    {
        "NextToken": str,
        "Pages": List["PageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {
        "PageArn": str,
        "EngagementArn": str,
        "ContactArn": str,
        "Sender": str,
        "IncidentId": NotRequired[str],
        "SentTime": NotRequired[datetime],
        "DeliveryTime": NotRequired[datetime],
        "ReadTime": NotRequired[datetime],
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

PlanTypeDef = TypedDict(
    "PlanTypeDef",
    {
        "Stages": Sequence["StageTypeDef"],
    },
)

PutContactPolicyRequestRequestTypeDef = TypedDict(
    "PutContactPolicyRequestRequestTypeDef",
    {
        "ContactArn": str,
        "Policy": str,
    },
)

ReceiptTypeDef = TypedDict(
    "ReceiptTypeDef",
    {
        "ReceiptType": ReceiptTypeType,
        "ReceiptTime": datetime,
        "ContactChannelArn": NotRequired[str],
        "ReceiptInfo": NotRequired[str],
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

SendActivationCodeRequestRequestTypeDef = TypedDict(
    "SendActivationCodeRequestRequestTypeDef",
    {
        "ContactChannelId": str,
    },
)

StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "DurationInMinutes": int,
        "Targets": Sequence["TargetTypeDef"],
    },
)

StartEngagementRequestRequestTypeDef = TypedDict(
    "StartEngagementRequestRequestTypeDef",
    {
        "ContactId": str,
        "Sender": str,
        "Subject": str,
        "Content": str,
        "PublicSubject": NotRequired[str],
        "PublicContent": NotRequired[str],
        "IncidentId": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
    },
)

StartEngagementResultTypeDef = TypedDict(
    "StartEngagementResultTypeDef",
    {
        "EngagementArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopEngagementRequestRequestTypeDef = TypedDict(
    "StopEngagementRequestRequestTypeDef",
    {
        "EngagementId": str,
        "Reason": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "ChannelTargetInfo": NotRequired["ChannelTargetInfoTypeDef"],
        "ContactTargetInfo": NotRequired["ContactTargetInfoTypeDef"],
    },
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateContactChannelRequestRequestTypeDef = TypedDict(
    "UpdateContactChannelRequestRequestTypeDef",
    {
        "ContactChannelId": str,
        "Name": NotRequired[str],
        "DeliveryAddress": NotRequired["ContactChannelAddressTypeDef"],
    },
)

UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "ContactId": str,
        "DisplayName": NotRequired[str],
        "Plan": NotRequired["PlanTypeDef"],
    },
)
