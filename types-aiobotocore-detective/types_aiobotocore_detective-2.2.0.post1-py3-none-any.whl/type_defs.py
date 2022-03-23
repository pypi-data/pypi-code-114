"""
Type annotations for detective service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_detective/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_detective.type_defs import AcceptInvitationRequestRequestTypeDef

    data: AcceptInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import InvitationTypeType, MemberDisabledReasonType, MemberStatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptInvitationRequestRequestTypeDef",
    "AccountTypeDef",
    "AdministratorTypeDef",
    "CreateGraphRequestRequestTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersRequestRequestTypeDef",
    "CreateMembersResponseTypeDef",
    "DeleteGraphRequestRequestTypeDef",
    "DeleteMembersRequestRequestTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DisassociateMembershipRequestRequestTypeDef",
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    "GetMembersRequestRequestTypeDef",
    "GetMembersResponseTypeDef",
    "GraphTypeDef",
    "ListGraphsRequestRequestTypeDef",
    "ListGraphsResponseTypeDef",
    "ListInvitationsRequestRequestTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersRequestRequestTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberDetailTypeDef",
    "RejectInvitationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "StartMonitoringMemberRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UnprocessedAccountTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
)

AcceptInvitationRequestRequestTypeDef = TypedDict(
    "AcceptInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AccountId": str,
        "EmailAddress": str,
    },
)

AdministratorTypeDef = TypedDict(
    "AdministratorTypeDef",
    {
        "AccountId": NotRequired[str],
        "GraphArn": NotRequired[str],
        "DelegationTime": NotRequired[datetime],
    },
)

CreateGraphRequestRequestTypeDef = TypedDict(
    "CreateGraphRequestRequestTypeDef",
    {
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateGraphResponseTypeDef = TypedDict(
    "CreateGraphResponseTypeDef",
    {
        "GraphArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMembersRequestRequestTypeDef = TypedDict(
    "CreateMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "Accounts": Sequence["AccountTypeDef"],
        "Message": NotRequired[str],
        "DisableEmailNotification": NotRequired[bool],
    },
)

CreateMembersResponseTypeDef = TypedDict(
    "CreateMembersResponseTypeDef",
    {
        "Members": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGraphRequestRequestTypeDef = TypedDict(
    "DeleteGraphRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DeleteMembersRequestRequestTypeDef = TypedDict(
    "DeleteMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": Sequence[str],
    },
)

DeleteMembersResponseTypeDef = TypedDict(
    "DeleteMembersResponseTypeDef",
    {
        "AccountIds": List[str],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {
        "AutoEnable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateMembershipRequestRequestTypeDef = TypedDict(
    "DisassociateMembershipRequestRequestTypeDef",
    {
        "GraphArn": str,
    },
)

EnableOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "EnableOrganizationAdminAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetMembersRequestRequestTypeDef = TypedDict(
    "GetMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountIds": Sequence[str],
    },
)

GetMembersResponseTypeDef = TypedDict(
    "GetMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "UnprocessedAccounts": List["UnprocessedAccountTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GraphTypeDef = TypedDict(
    "GraphTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)

ListGraphsRequestRequestTypeDef = TypedDict(
    "ListGraphsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGraphsResponseTypeDef = TypedDict(
    "ListGraphsResponseTypeDef",
    {
        "GraphList": List["GraphTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInvitationsRequestRequestTypeDef = TypedDict(
    "ListInvitationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {
        "Invitations": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersRequestRequestTypeDef = TypedDict(
    "ListMembersRequestRequestTypeDef",
    {
        "GraphArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef",
    {
        "MemberDetails": List["MemberDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationAdminAccountsRequestRequestTypeDef = TypedDict(
    "ListOrganizationAdminAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {
        "Administrators": List["AdministratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberDetailTypeDef = TypedDict(
    "MemberDetailTypeDef",
    {
        "AccountId": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GraphArn": NotRequired[str],
        "MasterId": NotRequired[str],
        "AdministratorId": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "DisabledReason": NotRequired[MemberDisabledReasonType],
        "InvitedTime": NotRequired[datetime],
        "UpdatedTime": NotRequired[datetime],
        "VolumeUsageInBytes": NotRequired[int],
        "VolumeUsageUpdatedTime": NotRequired[datetime],
        "PercentOfGraphUtilization": NotRequired[float],
        "PercentOfGraphUtilizationUpdatedTime": NotRequired[datetime],
        "InvitationType": NotRequired[InvitationTypeType],
    },
)

RejectInvitationRequestRequestTypeDef = TypedDict(
    "RejectInvitationRequestRequestTypeDef",
    {
        "GraphArn": str,
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

StartMonitoringMemberRequestRequestTypeDef = TypedDict(
    "StartMonitoringMemberRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AccountId": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {
        "AccountId": NotRequired[str],
        "Reason": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateOrganizationConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationConfigurationRequestRequestTypeDef",
    {
        "GraphArn": str,
        "AutoEnable": NotRequired[bool],
    },
)
