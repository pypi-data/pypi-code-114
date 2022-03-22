"""
Type annotations for chime-sdk-messaging service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_messaging/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_messaging.type_defs import AppInstanceUserMembershipSummaryTypeDef

    data: AppInstanceUserMembershipSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AllowNotificationsType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageStatusType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    ErrorCodeType,
    FallbackActionType,
    PushNotificationTypeType,
    SortOrderType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppInstanceUserMembershipSummaryTypeDef",
    "AssociateChannelFlowRequestRequestTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "ChannelAssociatedWithFlowSummaryTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelFlowCallbackRequestRequestTypeDef",
    "ChannelFlowCallbackResponseTypeDef",
    "ChannelFlowSummaryTypeDef",
    "ChannelFlowTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipPreferencesTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageCallbackTypeDef",
    "ChannelMessageStatusStructureTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelFlowRequestRequestTypeDef",
    "CreateChannelFlowResponseTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelFlowRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelFlowRequestRequestTypeDef",
    "DescribeChannelFlowResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociateChannelFlowRequestRequestTypeDef",
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    "GetChannelMembershipPreferencesResponseTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetChannelMessageStatusRequestRequestTypeDef",
    "GetChannelMessageStatusResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "IdentityTypeDef",
    "LambdaConfigurationTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelFlowsRequestRequestTypeDef",
    "ListChannelFlowsResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "MessagingSessionEndpointTypeDef",
    "ProcessorConfigurationTypeDef",
    "ProcessorTypeDef",
    "PushNotificationConfigurationTypeDef",
    "PushNotificationPreferencesTypeDef",
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    "PutChannelMembershipPreferencesResponseTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "ResponseMetadataTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "SendChannelMessageResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelFlowRequestRequestTypeDef",
    "UpdateChannelFlowResponseTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": NotRequired[ChannelMembershipTypeType],
        "ReadMarkerTimestamp": NotRequired[datetime],
    },
)

AssociateChannelFlowRequestRequestTypeDef = TypedDict(
    "AssociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": NotRequired["IdentityTypeDef"],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Members": NotRequired[List["IdentityTypeDef"]],
        "ChannelArn": NotRequired[str],
    },
)

BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

BatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
    },
)

BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": "BatchChannelMembershipsTypeDef",
        "Errors": List["BatchCreateChannelMembershipErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelAssociatedWithFlowSummaryTypeDef = TypedDict(
    "ChannelAssociatedWithFlowSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
    },
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
    },
)

ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired["IdentityTypeDef"],
    },
)

ChannelFlowCallbackRequestRequestTypeDef = TypedDict(
    "ChannelFlowCallbackRequestRequestTypeDef",
    {
        "CallbackId": str,
        "ChannelArn": str,
        "ChannelMessage": "ChannelMessageCallbackTypeDef",
        "DeleteResource": NotRequired[bool],
    },
)

ChannelFlowCallbackResponseTypeDef = TypedDict(
    "ChannelFlowCallbackResponseTypeDef",
    {
        "ChannelArn": str,
        "CallbackId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelFlowSummaryTypeDef = TypedDict(
    "ChannelFlowSummaryTypeDef",
    {
        "ChannelFlowArn": NotRequired[str],
        "Name": NotRequired[str],
        "Processors": NotRequired[List["ProcessorTypeDef"]],
    },
)

ChannelFlowTypeDef = TypedDict(
    "ChannelFlowTypeDef",
    {
        "ChannelFlowArn": NotRequired[str],
        "Processors": NotRequired[List["ProcessorTypeDef"]],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired["ChannelSummaryTypeDef"],
        "AppInstanceUserMembershipSummary": NotRequired["AppInstanceUserMembershipSummaryTypeDef"],
    },
)

ChannelMembershipPreferencesTypeDef = TypedDict(
    "ChannelMembershipPreferencesTypeDef",
    {
        "PushNotifications": NotRequired["PushNotificationPreferencesTypeDef"],
    },
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
    },
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": NotRequired["IdentityTypeDef"],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Member": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ChannelMessageCallbackTypeDef = TypedDict(
    "ChannelMessageCallbackTypeDef",
    {
        "MessageId": str,
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "PushNotification": NotRequired["PushNotificationConfigurationTypeDef"],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
    },
)

ChannelMessageStatusStructureTypeDef = TypedDict(
    "ChannelMessageStatusStructureTypeDef",
    {
        "Value": NotRequired[ChannelMessageStatusType],
        "Detail": NotRequired[str],
    },
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "Sender": NotRequired["IdentityTypeDef"],
        "Redacted": NotRequired[bool],
        "Status": NotRequired["ChannelMessageStatusStructureTypeDef"],
        "MessageAttributes": NotRequired[Dict[str, "MessageAttributeValueTypeDef"]],
    },
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Sender": NotRequired["IdentityTypeDef"],
        "Redacted": NotRequired[bool],
        "Persistence": NotRequired[ChannelMessagePersistenceTypeType],
        "Status": NotRequired["ChannelMessageStatusStructureTypeDef"],
        "MessageAttributes": NotRequired[Dict[str, "MessageAttributeValueTypeDef"]],
    },
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired["ChannelSummaryTypeDef"],
    },
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": NotRequired["IdentityTypeDef"],
    },
)

ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired["IdentityTypeDef"],
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "LastMessageTimestamp": NotRequired[datetime],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "CreatedBy": NotRequired["IdentityTypeDef"],
        "CreatedTimestamp": NotRequired[datetime],
        "LastMessageTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "ChannelFlowArn": NotRequired[str],
    },
)

CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelFlowRequestRequestTypeDef = TypedDict(
    "CreateChannelFlowRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Processors": Sequence["ProcessorTypeDef"],
        "Name": str,
        "ClientRequestToken": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateChannelFlowResponseTypeDef = TypedDict(
    "CreateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": str,
    },
)

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "ChimeBearer": str,
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelFlowRequestRequestTypeDef = TypedDict(
    "DeleteChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

DeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "DeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "DeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": "ChannelBanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelFlowRequestRequestTypeDef = TypedDict(
    "DescribeChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
    },
)

DescribeChannelFlowResponseTypeDef = TypedDict(
    "DescribeChannelFlowResponseTypeDef",
    {
        "ChannelFlow": "ChannelFlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": "ChannelModeratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateChannelFlowRequestRequestTypeDef = TypedDict(
    "DisassociateChannelFlowRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelFlowArn": str,
        "ChimeBearer": str,
    },
)

GetChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "GetChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
    },
)

GetChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "GetChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "Preferences": "ChannelMembershipPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelMessageRequestRequestTypeDef = TypedDict(
    "GetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": "ChannelMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelMessageStatusRequestRequestTypeDef = TypedDict(
    "GetChannelMessageStatusRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

GetChannelMessageStatusResponseTypeDef = TypedDict(
    "GetChannelMessageStatusResponseTypeDef",
    {
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": "MessagingSessionEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

LambdaConfigurationTypeDef = TypedDict(
    "LambdaConfigurationTypeDef",
    {
        "ResourceArn": str,
        "InvocationType": Literal["ASYNC"],
    },
)

ListChannelBansRequestRequestTypeDef = TypedDict(
    "ListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List["ChannelBanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelFlowsRequestRequestTypeDef = TypedDict(
    "ListChannelFlowsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelFlowsResponseTypeDef = TypedDict(
    "ListChannelFlowsResponseTypeDef",
    {
        "ChannelFlows": List["ChannelFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List["ChannelMembershipForAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List["ChannelMembershipSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMessagesRequestRequestTypeDef = TypedDict(
    "ListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "SortOrder": NotRequired[SortOrderType],
        "NotBefore": NotRequired[Union[datetime, str]],
        "NotAfter": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List["ChannelMessageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "ListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List["ChannelModeratorSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelsAssociatedWithChannelFlowResponseTypeDef = TypedDict(
    "ListChannelsAssociatedWithChannelFlowResponseTypeDef",
    {
        "Channels": List["ChannelAssociatedWithFlowSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChimeBearer": str,
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List["ChannelModeratedByAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "ChimeBearer": str,
        "Privacy": NotRequired[ChannelPrivacyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MessageAttributeValueTypeDef = TypedDict(
    "MessageAttributeValueTypeDef",
    {
        "StringValues": NotRequired[Sequence[str]],
    },
)

MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": NotRequired[str],
    },
)

ProcessorConfigurationTypeDef = TypedDict(
    "ProcessorConfigurationTypeDef",
    {
        "Lambda": "LambdaConfigurationTypeDef",
    },
)

ProcessorTypeDef = TypedDict(
    "ProcessorTypeDef",
    {
        "Name": str,
        "Configuration": "ProcessorConfigurationTypeDef",
        "ExecutionOrder": int,
        "FallbackAction": FallbackActionType,
    },
)

PushNotificationConfigurationTypeDef = TypedDict(
    "PushNotificationConfigurationTypeDef",
    {
        "Title": NotRequired[str],
        "Body": NotRequired[str],
        "Type": NotRequired[PushNotificationTypeType],
    },
)

PushNotificationPreferencesTypeDef = TypedDict(
    "PushNotificationPreferencesTypeDef",
    {
        "AllowNotifications": AllowNotificationsType,
        "FilterRule": NotRequired[str],
    },
)

PutChannelMembershipPreferencesRequestRequestTypeDef = TypedDict(
    "PutChannelMembershipPreferencesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": str,
        "Preferences": "ChannelMembershipPreferencesTypeDef",
    },
)

PutChannelMembershipPreferencesResponseTypeDef = TypedDict(
    "PutChannelMembershipPreferencesResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "Preferences": "ChannelMembershipPreferencesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactChannelMessageRequestRequestTypeDef = TypedDict(
    "RedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
    },
)

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
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

SendChannelMessageRequestRequestTypeDef = TypedDict(
    "SendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "ChimeBearer": str,
        "Metadata": NotRequired[str],
        "PushNotification": NotRequired["PushNotificationConfigurationTypeDef"],
        "MessageAttributes": NotRequired[Mapping[str, "MessageAttributeValueTypeDef"]],
    },
)

SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
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
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateChannelFlowRequestRequestTypeDef = TypedDict(
    "UpdateChannelFlowRequestRequestTypeDef",
    {
        "ChannelFlowArn": str,
        "Processors": Sequence["ProcessorTypeDef"],
        "Name": str,
    },
)

UpdateChannelFlowResponseTypeDef = TypedDict(
    "UpdateChannelFlowResponseTypeDef",
    {
        "ChannelFlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "UpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": str,
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)

UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Status": "ChannelMessageStatusStructureTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": str,
    },
)

UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Mode": ChannelModeType,
        "ChimeBearer": str,
        "Metadata": NotRequired[str],
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
