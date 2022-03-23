"""
Type annotations for organizations service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_organizations/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_organizations.type_defs import AcceptHandshakeRequestRequestTypeDef

    data: AcceptHandshakeRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountJoinedMethodType,
    AccountStatusType,
    ActionTypeType,
    ChildTypeType,
    CreateAccountFailureReasonType,
    CreateAccountStateType,
    EffectivePolicyTypeType,
    HandshakePartyTypeType,
    HandshakeResourceTypeType,
    HandshakeStateType,
    IAMUserAccessToBillingType,
    OrganizationFeatureSetType,
    ParentTypeType,
    PolicyTypeStatusType,
    PolicyTypeType,
    TargetTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptHandshakeRequestRequestTypeDef",
    "AcceptHandshakeResponseTypeDef",
    "AccountTypeDef",
    "AttachPolicyRequestRequestTypeDef",
    "CancelHandshakeRequestRequestTypeDef",
    "CancelHandshakeResponseTypeDef",
    "ChildTypeDef",
    "CreateAccountRequestRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAccountStatusTypeDef",
    "CreateGovCloudAccountRequestRequestTypeDef",
    "CreateGovCloudAccountResponseTypeDef",
    "CreateOrganizationRequestRequestTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateOrganizationalUnitRequestRequestTypeDef",
    "CreateOrganizationalUnitResponseTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreatePolicyResponseTypeDef",
    "DeclineHandshakeRequestRequestTypeDef",
    "DeclineHandshakeResponseTypeDef",
    "DelegatedAdministratorTypeDef",
    "DelegatedServiceTypeDef",
    "DeleteOrganizationalUnitRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeregisterDelegatedAdministratorRequestRequestTypeDef",
    "DescribeAccountRequestRequestTypeDef",
    "DescribeAccountResponseTypeDef",
    "DescribeCreateAccountStatusRequestRequestTypeDef",
    "DescribeCreateAccountStatusResponseTypeDef",
    "DescribeEffectivePolicyRequestRequestTypeDef",
    "DescribeEffectivePolicyResponseTypeDef",
    "DescribeHandshakeRequestRequestTypeDef",
    "DescribeHandshakeResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeOrganizationalUnitRequestRequestTypeDef",
    "DescribeOrganizationalUnitResponseTypeDef",
    "DescribePolicyRequestRequestTypeDef",
    "DescribePolicyResponseTypeDef",
    "DetachPolicyRequestRequestTypeDef",
    "DisableAWSServiceAccessRequestRequestTypeDef",
    "DisablePolicyTypeRequestRequestTypeDef",
    "DisablePolicyTypeResponseTypeDef",
    "EffectivePolicyTypeDef",
    "EnableAWSServiceAccessRequestRequestTypeDef",
    "EnableAllFeaturesResponseTypeDef",
    "EnablePolicyTypeRequestRequestTypeDef",
    "EnablePolicyTypeResponseTypeDef",
    "EnabledServicePrincipalTypeDef",
    "HandshakeFilterTypeDef",
    "HandshakePartyTypeDef",
    "HandshakeResourceTypeDef",
    "HandshakeTypeDef",
    "InviteAccountToOrganizationRequestRequestTypeDef",
    "InviteAccountToOrganizationResponseTypeDef",
    "ListAWSServiceAccessForOrganizationRequestRequestTypeDef",
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    "ListAccountsForParentRequestRequestTypeDef",
    "ListAccountsForParentResponseTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListChildrenRequestRequestTypeDef",
    "ListChildrenResponseTypeDef",
    "ListCreateAccountStatusRequestRequestTypeDef",
    "ListCreateAccountStatusResponseTypeDef",
    "ListDelegatedAdministratorsRequestRequestTypeDef",
    "ListDelegatedAdministratorsResponseTypeDef",
    "ListDelegatedServicesForAccountRequestRequestTypeDef",
    "ListDelegatedServicesForAccountResponseTypeDef",
    "ListHandshakesForAccountRequestRequestTypeDef",
    "ListHandshakesForAccountResponseTypeDef",
    "ListHandshakesForOrganizationRequestRequestTypeDef",
    "ListHandshakesForOrganizationResponseTypeDef",
    "ListOrganizationalUnitsForParentRequestRequestTypeDef",
    "ListOrganizationalUnitsForParentResponseTypeDef",
    "ListParentsRequestRequestTypeDef",
    "ListParentsResponseTypeDef",
    "ListPoliciesForTargetRequestRequestTypeDef",
    "ListPoliciesForTargetResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListRootsRequestRequestTypeDef",
    "ListRootsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForPolicyRequestRequestTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "MoveAccountRequestRequestTypeDef",
    "OrganizationTypeDef",
    "OrganizationalUnitTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTargetSummaryTypeDef",
    "PolicyTypeDef",
    "PolicyTypeSummaryTypeDef",
    "RegisterDelegatedAdministratorRequestRequestTypeDef",
    "RemoveAccountFromOrganizationRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RootTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateOrganizationalUnitRequestRequestTypeDef",
    "UpdateOrganizationalUnitResponseTypeDef",
    "UpdatePolicyRequestRequestTypeDef",
    "UpdatePolicyResponseTypeDef",
)

AcceptHandshakeRequestRequestTypeDef = TypedDict(
    "AcceptHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

AcceptHandshakeResponseTypeDef = TypedDict(
    "AcceptHandshakeResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AccountStatusType],
        "JoinedMethod": NotRequired[AccountJoinedMethodType],
        "JoinedTimestamp": NotRequired[datetime],
    },
)

AttachPolicyRequestRequestTypeDef = TypedDict(
    "AttachPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)

CancelHandshakeRequestRequestTypeDef = TypedDict(
    "CancelHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

CancelHandshakeResponseTypeDef = TypedDict(
    "CancelHandshakeResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChildTypeDef = TypedDict(
    "ChildTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ChildTypeType],
    },
)

CreateAccountRequestRequestTypeDef = TypedDict(
    "CreateAccountRequestRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
        "RoleName": NotRequired[str],
        "IamUserAccessToBilling": NotRequired[IAMUserAccessToBillingType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccountStatusTypeDef = TypedDict(
    "CreateAccountStatusTypeDef",
    {
        "Id": NotRequired[str],
        "AccountName": NotRequired[str],
        "State": NotRequired[CreateAccountStateType],
        "RequestedTimestamp": NotRequired[datetime],
        "CompletedTimestamp": NotRequired[datetime],
        "AccountId": NotRequired[str],
        "GovCloudAccountId": NotRequired[str],
        "FailureReason": NotRequired[CreateAccountFailureReasonType],
    },
)

CreateGovCloudAccountRequestRequestTypeDef = TypedDict(
    "CreateGovCloudAccountRequestRequestTypeDef",
    {
        "Email": str,
        "AccountName": str,
        "RoleName": NotRequired[str],
        "IamUserAccessToBilling": NotRequired[IAMUserAccessToBillingType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGovCloudAccountResponseTypeDef = TypedDict(
    "CreateGovCloudAccountResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOrganizationRequestRequestTypeDef = TypedDict(
    "CreateOrganizationRequestRequestTypeDef",
    {
        "FeatureSet": NotRequired[OrganizationFeatureSetType],
    },
)

CreateOrganizationResponseTypeDef = TypedDict(
    "CreateOrganizationResponseTypeDef",
    {
        "Organization": "OrganizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "CreateOrganizationalUnitRequestRequestTypeDef",
    {
        "ParentId": str,
        "Name": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateOrganizationalUnitResponseTypeDef = TypedDict(
    "CreateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePolicyRequestRequestTypeDef = TypedDict(
    "CreatePolicyRequestRequestTypeDef",
    {
        "Content": str,
        "Description": str,
        "Name": str,
        "Type": PolicyTypeType,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeclineHandshakeRequestRequestTypeDef = TypedDict(
    "DeclineHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

DeclineHandshakeResponseTypeDef = TypedDict(
    "DeclineHandshakeResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DelegatedAdministratorTypeDef = TypedDict(
    "DelegatedAdministratorTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Email": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[AccountStatusType],
        "JoinedMethod": NotRequired[AccountJoinedMethodType],
        "JoinedTimestamp": NotRequired[datetime],
        "DelegationEnabledDate": NotRequired[datetime],
    },
)

DelegatedServiceTypeDef = TypedDict(
    "DelegatedServiceTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "DelegationEnabledDate": NotRequired[datetime],
    },
)

DeleteOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "DeleteOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

DeregisterDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "DeregisterDelegatedAdministratorRequestRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)

DescribeAccountRequestRequestTypeDef = TypedDict(
    "DescribeAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DescribeAccountResponseTypeDef = TypedDict(
    "DescribeAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCreateAccountStatusRequestRequestTypeDef = TypedDict(
    "DescribeCreateAccountStatusRequestRequestTypeDef",
    {
        "CreateAccountRequestId": str,
    },
)

DescribeCreateAccountStatusResponseTypeDef = TypedDict(
    "DescribeCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatus": "CreateAccountStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEffectivePolicyRequestRequestTypeDef = TypedDict(
    "DescribeEffectivePolicyRequestRequestTypeDef",
    {
        "PolicyType": EffectivePolicyTypeType,
        "TargetId": NotRequired[str],
    },
)

DescribeEffectivePolicyResponseTypeDef = TypedDict(
    "DescribeEffectivePolicyResponseTypeDef",
    {
        "EffectivePolicy": "EffectivePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHandshakeRequestRequestTypeDef = TypedDict(
    "DescribeHandshakeRequestRequestTypeDef",
    {
        "HandshakeId": str,
    },
)

DescribeHandshakeResponseTypeDef = TypedDict(
    "DescribeHandshakeResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationResponseTypeDef = TypedDict(
    "DescribeOrganizationResponseTypeDef",
    {
        "Organization": "OrganizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "DescribeOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
    },
)

DescribeOrganizationalUnitResponseTypeDef = TypedDict(
    "DescribeOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePolicyRequestRequestTypeDef = TypedDict(
    "DescribePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
    },
)

DescribePolicyResponseTypeDef = TypedDict(
    "DescribePolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetachPolicyRequestRequestTypeDef = TypedDict(
    "DetachPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "TargetId": str,
    },
)

DisableAWSServiceAccessRequestRequestTypeDef = TypedDict(
    "DisableAWSServiceAccessRequestRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)

DisablePolicyTypeRequestRequestTypeDef = TypedDict(
    "DisablePolicyTypeRequestRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)

DisablePolicyTypeResponseTypeDef = TypedDict(
    "DisablePolicyTypeResponseTypeDef",
    {
        "Root": "RootTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EffectivePolicyTypeDef = TypedDict(
    "EffectivePolicyTypeDef",
    {
        "PolicyContent": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "TargetId": NotRequired[str],
        "PolicyType": NotRequired[EffectivePolicyTypeType],
    },
)

EnableAWSServiceAccessRequestRequestTypeDef = TypedDict(
    "EnableAWSServiceAccessRequestRequestTypeDef",
    {
        "ServicePrincipal": str,
    },
)

EnableAllFeaturesResponseTypeDef = TypedDict(
    "EnableAllFeaturesResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnablePolicyTypeRequestRequestTypeDef = TypedDict(
    "EnablePolicyTypeRequestRequestTypeDef",
    {
        "RootId": str,
        "PolicyType": PolicyTypeType,
    },
)

EnablePolicyTypeResponseTypeDef = TypedDict(
    "EnablePolicyTypeResponseTypeDef",
    {
        "Root": "RootTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnabledServicePrincipalTypeDef = TypedDict(
    "EnabledServicePrincipalTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "DateEnabled": NotRequired[datetime],
    },
)

HandshakeFilterTypeDef = TypedDict(
    "HandshakeFilterTypeDef",
    {
        "ActionType": NotRequired[ActionTypeType],
        "ParentHandshakeId": NotRequired[str],
    },
)

HandshakePartyTypeDef = TypedDict(
    "HandshakePartyTypeDef",
    {
        "Id": str,
        "Type": HandshakePartyTypeType,
    },
)

HandshakeResourceTypeDef = TypedDict(
    "HandshakeResourceTypeDef",
    {
        "Value": NotRequired[str],
        "Type": NotRequired[HandshakeResourceTypeType],
        "Resources": NotRequired[List[Dict[str, Any]]],
    },
)

HandshakeTypeDef = TypedDict(
    "HandshakeTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Parties": NotRequired[List["HandshakePartyTypeDef"]],
        "State": NotRequired[HandshakeStateType],
        "RequestedTimestamp": NotRequired[datetime],
        "ExpirationTimestamp": NotRequired[datetime],
        "Action": NotRequired[ActionTypeType],
        "Resources": NotRequired[List["HandshakeResourceTypeDef"]],
    },
)

InviteAccountToOrganizationRequestRequestTypeDef = TypedDict(
    "InviteAccountToOrganizationRequestRequestTypeDef",
    {
        "Target": "HandshakePartyTypeDef",
        "Notes": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

InviteAccountToOrganizationResponseTypeDef = TypedDict(
    "InviteAccountToOrganizationResponseTypeDef",
    {
        "Handshake": "HandshakeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAWSServiceAccessForOrganizationRequestRequestTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAWSServiceAccessForOrganizationResponseTypeDef = TypedDict(
    "ListAWSServiceAccessForOrganizationResponseTypeDef",
    {
        "EnabledServicePrincipals": List["EnabledServicePrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsForParentRequestRequestTypeDef = TypedDict(
    "ListAccountsForParentRequestRequestTypeDef",
    {
        "ParentId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAccountsForParentResponseTypeDef = TypedDict(
    "ListAccountsForParentResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChildrenRequestRequestTypeDef = TypedDict(
    "ListChildrenRequestRequestTypeDef",
    {
        "ParentId": str,
        "ChildType": ChildTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListChildrenResponseTypeDef = TypedDict(
    "ListChildrenResponseTypeDef",
    {
        "Children": List["ChildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCreateAccountStatusRequestRequestTypeDef = TypedDict(
    "ListCreateAccountStatusRequestRequestTypeDef",
    {
        "States": NotRequired[Sequence[CreateAccountStateType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCreateAccountStatusResponseTypeDef = TypedDict(
    "ListCreateAccountStatusResponseTypeDef",
    {
        "CreateAccountStatuses": List["CreateAccountStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDelegatedAdministratorsRequestRequestTypeDef = TypedDict(
    "ListDelegatedAdministratorsRequestRequestTypeDef",
    {
        "ServicePrincipal": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDelegatedAdministratorsResponseTypeDef = TypedDict(
    "ListDelegatedAdministratorsResponseTypeDef",
    {
        "DelegatedAdministrators": List["DelegatedAdministratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDelegatedServicesForAccountRequestRequestTypeDef = TypedDict(
    "ListDelegatedServicesForAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDelegatedServicesForAccountResponseTypeDef = TypedDict(
    "ListDelegatedServicesForAccountResponseTypeDef",
    {
        "DelegatedServices": List["DelegatedServiceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHandshakesForAccountRequestRequestTypeDef = TypedDict(
    "ListHandshakesForAccountRequestRequestTypeDef",
    {
        "Filter": NotRequired["HandshakeFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHandshakesForAccountResponseTypeDef = TypedDict(
    "ListHandshakesForAccountResponseTypeDef",
    {
        "Handshakes": List["HandshakeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHandshakesForOrganizationRequestRequestTypeDef = TypedDict(
    "ListHandshakesForOrganizationRequestRequestTypeDef",
    {
        "Filter": NotRequired["HandshakeFilterTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListHandshakesForOrganizationResponseTypeDef = TypedDict(
    "ListHandshakesForOrganizationResponseTypeDef",
    {
        "Handshakes": List["HandshakeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOrganizationalUnitsForParentRequestRequestTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentRequestRequestTypeDef",
    {
        "ParentId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListOrganizationalUnitsForParentResponseTypeDef = TypedDict(
    "ListOrganizationalUnitsForParentResponseTypeDef",
    {
        "OrganizationalUnits": List["OrganizationalUnitTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListParentsRequestRequestTypeDef = TypedDict(
    "ListParentsRequestRequestTypeDef",
    {
        "ChildId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListParentsResponseTypeDef = TypedDict(
    "ListParentsResponseTypeDef",
    {
        "Parents": List["ParentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesForTargetRequestRequestTypeDef = TypedDict(
    "ListPoliciesForTargetRequestRequestTypeDef",
    {
        "TargetId": str,
        "Filter": PolicyTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPoliciesForTargetResponseTypeDef = TypedDict(
    "ListPoliciesForTargetResponseTypeDef",
    {
        "Policies": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "Filter": PolicyTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "Policies": List["PolicySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRootsRequestRequestTypeDef = TypedDict(
    "ListRootsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRootsResponseTypeDef = TypedDict(
    "ListRootsResponseTypeDef",
    {
        "Roots": List["RootTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTargetsForPolicyRequestRequestTypeDef = TypedDict(
    "ListTargetsForPolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTargetsForPolicyResponseTypeDef = TypedDict(
    "ListTargetsForPolicyResponseTypeDef",
    {
        "Targets": List["PolicyTargetSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MoveAccountRequestRequestTypeDef = TypedDict(
    "MoveAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "SourceParentId": str,
        "DestinationParentId": str,
    },
)

OrganizationTypeDef = TypedDict(
    "OrganizationTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "FeatureSet": NotRequired[OrganizationFeatureSetType],
        "MasterAccountArn": NotRequired[str],
        "MasterAccountId": NotRequired[str],
        "MasterAccountEmail": NotRequired[str],
        "AvailablePolicyTypes": NotRequired[List["PolicyTypeSummaryTypeDef"]],
    },
)

OrganizationalUnitTypeDef = TypedDict(
    "OrganizationalUnitTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
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

ParentTypeDef = TypedDict(
    "ParentTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[ParentTypeType],
    },
)

PolicySummaryTypeDef = TypedDict(
    "PolicySummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[PolicyTypeType],
        "AwsManaged": NotRequired[bool],
    },
)

PolicyTargetSummaryTypeDef = TypedDict(
    "PolicyTargetSummaryTypeDef",
    {
        "TargetId": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[TargetTypeType],
    },
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicySummary": NotRequired["PolicySummaryTypeDef"],
        "Content": NotRequired[str],
    },
)

PolicyTypeSummaryTypeDef = TypedDict(
    "PolicyTypeSummaryTypeDef",
    {
        "Type": NotRequired[PolicyTypeType],
        "Status": NotRequired[PolicyTypeStatusType],
    },
)

RegisterDelegatedAdministratorRequestRequestTypeDef = TypedDict(
    "RegisterDelegatedAdministratorRequestRequestTypeDef",
    {
        "AccountId": str,
        "ServicePrincipal": str,
    },
)

RemoveAccountFromOrganizationRequestRequestTypeDef = TypedDict(
    "RemoveAccountFromOrganizationRequestRequestTypeDef",
    {
        "AccountId": str,
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

RootTypeDef = TypedDict(
    "RootTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "PolicyTypes": NotRequired[List["PolicyTypeSummaryTypeDef"]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceId": str,
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
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

UpdateOrganizationalUnitRequestRequestTypeDef = TypedDict(
    "UpdateOrganizationalUnitRequestRequestTypeDef",
    {
        "OrganizationalUnitId": str,
        "Name": NotRequired[str],
    },
)

UpdateOrganizationalUnitResponseTypeDef = TypedDict(
    "UpdateOrganizationalUnitResponseTypeDef",
    {
        "OrganizationalUnit": "OrganizationalUnitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePolicyRequestRequestTypeDef = TypedDict(
    "UpdatePolicyRequestRequestTypeDef",
    {
        "PolicyId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Content": NotRequired[str],
    },
)

UpdatePolicyResponseTypeDef = TypedDict(
    "UpdatePolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
