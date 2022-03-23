"""
Type annotations for iam service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    ContextKeyTypeEnumType,
    DeletionTaskStatusTypeType,
    EntityTypeType,
    PolicyEvaluationDecisionTypeType,
    PolicySourceTypeType,
    PolicyUsageTypeType,
    ReportStateTypeType,
    assignmentStatusTypeType,
    encodingTypeType,
    globalEndpointTokenVersionType,
    jobStatusTypeType,
    policyOwnerEntityTypeType,
    policyScopeTypeType,
    policyTypeType,
    sortKeyTypeType,
    statusTypeType,
    summaryKeyTypeType,
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
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    "AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef",
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    "AddUserToGroupRequestGroupAddUserTypeDef",
    "AddUserToGroupRequestRequestTypeDef",
    "AddUserToGroupRequestUserAddGroupTypeDef",
    "AttachGroupPolicyRequestGroupAttachPolicyTypeDef",
    "AttachGroupPolicyRequestPolicyAttachGroupTypeDef",
    "AttachGroupPolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestPolicyAttachRoleTypeDef",
    "AttachRolePolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestRoleAttachPolicyTypeDef",
    "AttachUserPolicyRequestPolicyAttachUserTypeDef",
    "AttachUserPolicyRequestRequestTypeDef",
    "AttachUserPolicyRequestUserAttachPolicyTypeDef",
    "AttachedPermissionsBoundaryResponseMetadataTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "ChangePasswordRequestServiceResourceChangePasswordTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyRequestRequestTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "CreateAccountAliasRequestRequestTypeDef",
    "CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef",
    "CreateGroupRequestGroupCreateTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupRequestServiceResourceCreateGroupTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateLoginProfileRequestLoginProfileCreateTypeDef",
    "CreateLoginProfileRequestRequestTypeDef",
    "CreateLoginProfileRequestUserCreateLoginProfileTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "CreateOpenIDConnectProviderRequestRequestTypeDef",
    "CreateOpenIDConnectProviderResponseTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreatePolicyRequestServiceResourceCreatePolicyTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionRequestPolicyCreateVersionTypeDef",
    "CreatePolicyVersionRequestRequestTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateRoleRequestRequestTypeDef",
    "CreateRoleRequestServiceResourceCreateRoleTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateSAMLProviderRequestRequestTypeDef",
    "CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "CreateServiceLinkedRoleRequestRequestTypeDef",
    "CreateServiceLinkedRoleResponseTypeDef",
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    "CreateServiceSpecificCredentialResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserRequestServiceResourceCreateUserTypeDef",
    "CreateUserRequestUserCreateTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVirtualMFADeviceRequestRequestTypeDef",
    "CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "DeactivateMFADeviceRequestRequestTypeDef",
    "DeleteAccessKeyRequestRequestTypeDef",
    "DeleteAccountAliasRequestRequestTypeDef",
    "DeleteGroupPolicyRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteLoginProfileRequestRequestTypeDef",
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeletePolicyVersionRequestRequestTypeDef",
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    "DeleteRolePolicyRequestRequestTypeDef",
    "DeleteRoleRequestRequestTypeDef",
    "DeleteSAMLProviderRequestRequestTypeDef",
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    "DeleteServerCertificateRequestRequestTypeDef",
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    "DeleteServiceLinkedRoleResponseTypeDef",
    "DeleteServiceSpecificCredentialRequestRequestTypeDef",
    "DeleteSigningCertificateRequestRequestTypeDef",
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    "DeleteUserPolicyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "DetachGroupPolicyRequestGroupDetachPolicyTypeDef",
    "DetachGroupPolicyRequestPolicyDetachGroupTypeDef",
    "DetachGroupPolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestPolicyDetachRoleTypeDef",
    "DetachRolePolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestRoleDetachPolicyTypeDef",
    "DetachUserPolicyRequestPolicyDetachUserTypeDef",
    "DetachUserPolicyRequestRequestTypeDef",
    "DetachUserPolicyRequestUserDetachPolicyTypeDef",
    "EnableMFADeviceRequestMfaDeviceAssociateTypeDef",
    "EnableMFADeviceRequestRequestTypeDef",
    "EnableMFADeviceRequestUserEnableMfaTypeDef",
    "EntityDetailsTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationResultTypeDef",
    "GenerateCredentialReportResponseTypeDef",
    "GenerateOrganizationsAccessReportRequestRequestTypeDef",
    "GenerateOrganizationsAccessReportResponseTypeDef",
    "GenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    "GetAccessKeyLastUsedResponseTypeDef",
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
    "GetAccountPasswordPolicyResponseTypeDef",
    "GetAccountSummaryResponseTypeDef",
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    "GetContextKeysForPolicyResponseTypeDef",
    "GetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    "GetCredentialReportResponseTypeDef",
    "GetGroupPolicyRequestRequestTypeDef",
    "GetGroupPolicyResponseTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupResponseTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetInstanceProfileResponseTypeDef",
    "GetLoginProfileRequestRequestTypeDef",
    "GetLoginProfileResponseTypeDef",
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    "GetOpenIDConnectProviderResponseTypeDef",
    "GetOrganizationsAccessReportRequestRequestTypeDef",
    "GetOrganizationsAccessReportResponseTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionRequestRequestTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRolePolicyRequestRequestTypeDef",
    "GetRolePolicyResponseTypeDef",
    "GetRoleRequestRequestTypeDef",
    "GetRoleResponseTypeDef",
    "GetSAMLProviderRequestRequestTypeDef",
    "GetSAMLProviderResponseTypeDef",
    "GetSSHPublicKeyRequestRequestTypeDef",
    "GetSSHPublicKeyResponseTypeDef",
    "GetServerCertificateRequestRequestTypeDef",
    "GetServerCertificateResponseTypeDef",
    "GetServiceLastAccessedDetailsRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "GetUserPolicyRequestRequestTypeDef",
    "GetUserPolicyResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GroupDetailTypeDef",
    "GroupPolicyRequestTypeDef",
    "GroupTypeDef",
    "InstanceProfileTypeDef",
    "ListAccessKeysRequestRequestTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesRequestRequestTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesRequestRequestTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesRequestRequestTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesRequestRequestTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "ListEntitiesForPolicyRequestRequestTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListGroupPoliciesRequestRequestTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListGroupsForUserRequestRequestTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListGroupsResponseTypeDef",
    "ListInstanceProfileTagsRequestRequestTypeDef",
    "ListInstanceProfileTagsResponseTypeDef",
    "ListInstanceProfilesForRoleRequestRequestTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "ListMFADeviceTagsRequestRequestTypeDef",
    "ListMFADeviceTagsResponseTypeDef",
    "ListMFADevicesRequestRequestTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListOpenIDConnectProviderTagsRequestRequestTypeDef",
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    "ListOpenIDConnectProvidersResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyTagsRequestRequestTypeDef",
    "ListPolicyTagsResponseTypeDef",
    "ListPolicyVersionsRequestRequestTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListRolePoliciesRequestRequestTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListRoleTagsRequestRequestTypeDef",
    "ListRoleTagsResponseTypeDef",
    "ListRolesRequestRequestTypeDef",
    "ListRolesResponseTypeDef",
    "ListSAMLProviderTagsRequestRequestTypeDef",
    "ListSAMLProviderTagsResponseTypeDef",
    "ListSAMLProvidersResponseTypeDef",
    "ListSSHPublicKeysRequestRequestTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ListServerCertificateTagsRequestRequestTypeDef",
    "ListServerCertificateTagsResponseTypeDef",
    "ListServerCertificatesRequestRequestTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    "ListServiceSpecificCredentialsResponseTypeDef",
    "ListSigningCertificatesRequestRequestTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "ListUserPoliciesRequestRequestTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "ListUserTagsRequestRequestTypeDef",
    "ListUserTagsResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListVirtualMFADevicesRequestRequestTypeDef",
    "ListVirtualMFADevicesResponseTypeDef",
    "LoginProfileTypeDef",
    "MFADeviceTypeDef",
    "ManagedPolicyDetailTypeDef",
    "OpenIDConnectProviderListEntryTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "PolicyDetailTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyTypeDef",
    "PolicyUserTypeDef",
    "PolicyVersionTypeDef",
    "PositionTypeDef",
    "PutGroupPolicyRequestGroupCreatePolicyTypeDef",
    "PutGroupPolicyRequestGroupPolicyPutTypeDef",
    "PutGroupPolicyRequestRequestTypeDef",
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    "PutRolePolicyRequestRequestTypeDef",
    "PutRolePolicyRequestRolePolicyPutTypeDef",
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    "PutUserPolicyRequestRequestTypeDef",
    "PutUserPolicyRequestUserCreatePolicyTypeDef",
    "PutUserPolicyRequestUserPolicyPutTypeDef",
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    "RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef",
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    "RemoveUserFromGroupRequestGroupRemoveUserTypeDef",
    "RemoveUserFromGroupRequestRequestTypeDef",
    "RemoveUserFromGroupRequestUserRemoveGroupTypeDef",
    "ResetServiceSpecificCredentialRequestRequestTypeDef",
    "ResetServiceSpecificCredentialResponseTypeDef",
    "ResourceSpecificResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResyncMFADeviceRequestMfaDeviceResyncTypeDef",
    "ResyncMFADeviceRequestRequestTypeDef",
    "RoleDetailTypeDef",
    "RoleLastUsedResponseMetadataTypeDef",
    "RoleLastUsedTypeDef",
    "RolePolicyRequestTypeDef",
    "RoleTypeDef",
    "RoleUsageTypeTypeDef",
    "SAMLProviderListEntryTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "SSHPublicKeyTypeDef",
    "ServerCertificateMetadataResponseMetadataTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ServerCertificateTypeDef",
    "ServiceLastAccessedTypeDef",
    "ServiceResourceAccessKeyPairRequestTypeDef",
    "ServiceResourceAccessKeyRequestTypeDef",
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    "ServiceResourceGroupPolicyRequestTypeDef",
    "ServiceResourceGroupRequestTypeDef",
    "ServiceResourceInstanceProfileRequestTypeDef",
    "ServiceResourceLoginProfileRequestTypeDef",
    "ServiceResourceMfaDeviceRequestTypeDef",
    "ServiceResourcePolicyRequestTypeDef",
    "ServiceResourcePolicyVersionRequestTypeDef",
    "ServiceResourceRolePolicyRequestTypeDef",
    "ServiceResourceRoleRequestTypeDef",
    "ServiceResourceSamlProviderRequestTypeDef",
    "ServiceResourceServerCertificateRequestTypeDef",
    "ServiceResourceSigningCertificateRequestTypeDef",
    "ServiceResourceUserPolicyRequestTypeDef",
    "ServiceResourceUserRequestTypeDef",
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    "SigningCertificateTypeDef",
    "SimulateCustomPolicyRequestRequestTypeDef",
    "SimulatePolicyResponseTypeDef",
    "SimulatePrincipalPolicyRequestRequestTypeDef",
    "StatementTypeDef",
    "TagInstanceProfileRequestRequestTypeDef",
    "TagMFADeviceRequestRequestTypeDef",
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    "TagPolicyRequestRequestTypeDef",
    "TagRoleRequestRequestTypeDef",
    "TagSAMLProviderRequestRequestTypeDef",
    "TagServerCertificateRequestRequestTypeDef",
    "TagTypeDef",
    "TagUserRequestRequestTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "UntagInstanceProfileRequestRequestTypeDef",
    "UntagMFADeviceRequestRequestTypeDef",
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    "UntagPolicyRequestRequestTypeDef",
    "UntagRoleRequestRequestTypeDef",
    "UntagSAMLProviderRequestRequestTypeDef",
    "UntagServerCertificateRequestRequestTypeDef",
    "UntagUserRequestRequestTypeDef",
    "UpdateAccessKeyRequestAccessKeyActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyDeactivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef",
    "UpdateAccessKeyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef",
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef",
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef",
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    "UpdateGroupRequestGroupUpdateTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoginProfileRequestLoginProfileUpdateTypeDef",
    "UpdateLoginProfileRequestRequestTypeDef",
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    "UpdateRoleDescriptionRequestRequestTypeDef",
    "UpdateRoleDescriptionResponseTypeDef",
    "UpdateRoleRequestRequestTypeDef",
    "UpdateSAMLProviderRequestRequestTypeDef",
    "UpdateSAMLProviderRequestSamlProviderUpdateTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    "UpdateServerCertificateRequestRequestTypeDef",
    "UpdateServerCertificateRequestServerCertificateUpdateTypeDef",
    "UpdateServiceSpecificCredentialRequestRequestTypeDef",
    "UpdateSigningCertificateRequestRequestTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateActivateTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserRequestUserUpdateTypeDef",
    "UploadSSHPublicKeyRequestRequestTypeDef",
    "UploadSSHPublicKeyResponseTypeDef",
    "UploadServerCertificateRequestRequestTypeDef",
    "UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "UploadSigningCertificateRequestRequestTypeDef",
    "UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "UserAccessKeyRequestTypeDef",
    "UserDetailTypeDef",
    "UserMfaDeviceRequestTypeDef",
    "UserPolicyRequestTypeDef",
    "UserResponseMetadataTypeDef",
    "UserSigningCertificateRequestTypeDef",
    "UserTypeDef",
    "VirtualMFADeviceTypeDef",
    "WaiterConfigTypeDef",
)

AccessDetailTypeDef = TypedDict(
    "AccessDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": NotRequired[str],
        "EntityPath": NotRequired[str],
        "LastAuthenticatedTime": NotRequired[datetime],
        "TotalAuthenticatedEntities": NotRequired[int],
    },
)

AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "LastUsedDate": datetime,
        "ServiceName": str,
        "Region": str,
    },
)

AccessKeyMetadataTypeDef = TypedDict(
    "AccessKeyMetadataTypeDef",
    {
        "UserName": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "Status": NotRequired[statusTypeType],
        "CreateDate": NotRequired[datetime],
    },
)

AccessKeyTypeDef = TypedDict(
    "AccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": statusTypeType,
        "SecretAccessKey": str,
        "CreateDate": NotRequired[datetime],
    },
)

AddClientIDToOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef",
    {
        "RoleName": str,
    },
)

AddRoleToInstanceProfileRequestRequestTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

AddUserToGroupRequestGroupAddUserTypeDef = TypedDict(
    "AddUserToGroupRequestGroupAddUserTypeDef",
    {
        "UserName": str,
    },
)

AddUserToGroupRequestRequestTypeDef = TypedDict(
    "AddUserToGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

AddUserToGroupRequestUserAddGroupTypeDef = TypedDict(
    "AddUserToGroupRequestUserAddGroupTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestGroupAttachPolicyTypeDef = TypedDict(
    "AttachGroupPolicyRequestGroupAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachGroupPolicyRequestPolicyAttachGroupTypeDef = TypedDict(
    "AttachGroupPolicyRequestPolicyAttachGroupTypeDef",
    {
        "GroupName": str,
    },
)

AttachGroupPolicyRequestRequestTypeDef = TypedDict(
    "AttachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestPolicyAttachRoleTypeDef = TypedDict(
    "AttachRolePolicyRequestPolicyAttachRoleTypeDef",
    {
        "RoleName": str,
    },
)

AttachRolePolicyRequestRequestTypeDef = TypedDict(
    "AttachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

AttachRolePolicyRequestRoleAttachPolicyTypeDef = TypedDict(
    "AttachRolePolicyRequestRoleAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestPolicyAttachUserTypeDef = TypedDict(
    "AttachUserPolicyRequestPolicyAttachUserTypeDef",
    {
        "UserName": str,
    },
)

AttachUserPolicyRequestRequestTypeDef = TypedDict(
    "AttachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

AttachUserPolicyRequestUserAttachPolicyTypeDef = TypedDict(
    "AttachUserPolicyRequestUserAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

AttachedPermissionsBoundaryResponseMetadataTypeDef = TypedDict(
    "AttachedPermissionsBoundaryResponseMetadataTypeDef",
    {
        "PermissionsBoundaryType": Literal["PermissionsBoundaryPolicy"],
        "PermissionsBoundaryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachedPermissionsBoundaryTypeDef = TypedDict(
    "AttachedPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryType": NotRequired[Literal["PermissionsBoundaryPolicy"]],
        "PermissionsBoundaryArn": NotRequired[str],
    },
)

AttachedPolicyTypeDef = TypedDict(
    "AttachedPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)

ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ChangePasswordRequestServiceResourceChangePasswordTypeDef = TypedDict(
    "ChangePasswordRequestServiceResourceChangePasswordTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)

ContextEntryTypeDef = TypedDict(
    "ContextEntryTypeDef",
    {
        "ContextKeyName": NotRequired[str],
        "ContextKeyValues": NotRequired[Sequence[str]],
        "ContextKeyType": NotRequired[ContextKeyTypeEnumType],
    },
)

CreateAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateAccessKeyRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
    },
)

CreateAccessKeyResponseTypeDef = TypedDict(
    "CreateAccessKeyResponseTypeDef",
    {
        "AccessKey": "AccessKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAccountAliasRequestRequestTypeDef = TypedDict(
    "CreateAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef = TypedDict(
    "CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef",
    {
        "AccountAlias": str,
    },
)

CreateGroupRequestGroupCreateTypeDef = TypedDict(
    "CreateGroupRequestGroupCreateTypeDef",
    {
        "Path": NotRequired[str],
    },
)

CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "Path": NotRequired[str],
    },
)

CreateGroupRequestServiceResourceCreateGroupTypeDef = TypedDict(
    "CreateGroupRequestServiceResourceCreateGroupTypeDef",
    {
        "GroupName": str,
        "Path": NotRequired[str],
    },
)

CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "CreateInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef = TypedDict(
    "CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef",
    {
        "InstanceProfileName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLoginProfileRequestLoginProfileCreateTypeDef = TypedDict(
    "CreateLoginProfileRequestLoginProfileCreateTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)

CreateLoginProfileRequestRequestTypeDef = TypedDict(
    "CreateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)

CreateLoginProfileRequestUserCreateLoginProfileTypeDef = TypedDict(
    "CreateLoginProfileRequestUserCreateLoginProfileTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)

CreateLoginProfileResponseTypeDef = TypedDict(
    "CreateLoginProfileResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "CreateOpenIDConnectProviderRequestRequestTypeDef",
    {
        "Url": str,
        "ThumbprintList": Sequence[str],
        "ClientIDList": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateOpenIDConnectProviderResponseTypeDef = TypedDict(
    "CreateOpenIDConnectProviderResponseTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePolicyRequestRequestTypeDef = TypedDict(
    "CreatePolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePolicyRequestServiceResourceCreatePolicyTypeDef = TypedDict(
    "CreatePolicyRequestServiceResourceCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
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

CreatePolicyVersionRequestPolicyCreateVersionTypeDef = TypedDict(
    "CreatePolicyVersionRequestPolicyCreateVersionTypeDef",
    {
        "PolicyDocument": str,
        "SetAsDefault": NotRequired[bool],
    },
)

CreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "CreatePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "PolicyDocument": str,
        "SetAsDefault": NotRequired[bool],
    },
)

CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoleRequestRequestTypeDef = TypedDict(
    "CreateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRoleRequestServiceResourceCreateRoleTypeDef = TypedDict(
    "CreateRoleRequestServiceResourceCreateRoleTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRoleResponseTypeDef = TypedDict(
    "CreateRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSAMLProviderRequestRequestTypeDef = TypedDict(
    "CreateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef = TypedDict(
    "CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSAMLProviderResponseTypeDef = TypedDict(
    "CreateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "CreateServiceLinkedRoleRequestRequestTypeDef",
    {
        "AWSServiceName": str,
        "Description": NotRequired[str],
        "CustomSuffix": NotRequired[str],
    },
)

CreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "CreateServiceLinkedRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
)

CreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "CreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserRequestServiceResourceCreateUserTypeDef = TypedDict(
    "CreateUserRequestServiceResourceCreateUserTypeDef",
    {
        "UserName": str,
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserRequestUserCreateTypeDef = TypedDict(
    "CreateUserRequestUserCreateTypeDef",
    {
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "CreateVirtualMFADeviceRequestRequestTypeDef",
    {
        "VirtualMFADeviceName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef = TypedDict(
    "CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef",
    {
        "VirtualMFADeviceName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateVirtualMFADeviceResponseTypeDef = TypedDict(
    "CreateVirtualMFADeviceResponseTypeDef",
    {
        "VirtualMFADevice": "VirtualMFADeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateMFADeviceRequestRequestTypeDef = TypedDict(
    "DeactivateMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
    },
)

DeleteAccessKeyRequestRequestTypeDef = TypedDict(
    "DeleteAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
        "UserName": NotRequired[str],
    },
)

DeleteAccountAliasRequestRequestTypeDef = TypedDict(
    "DeleteAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)

DeleteGroupPolicyRequestRequestTypeDef = TypedDict(
    "DeleteGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)

DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

DeleteLoginProfileRequestRequestTypeDef = TypedDict(
    "DeleteLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

DeletePolicyVersionRequestRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

DeleteRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteRolePolicyRequestRequestTypeDef = TypedDict(
    "DeleteRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

DeleteRoleRequestRequestTypeDef = TypedDict(
    "DeleteRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteSAMLProviderRequestRequestTypeDef = TypedDict(
    "DeleteSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

DeleteSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
    },
)

DeleteServerCertificateRequestRequestTypeDef = TypedDict(
    "DeleteServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

DeleteServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

DeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "DeleteServiceLinkedRoleResponseTypeDef",
    {
        "DeletionTaskId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "DeleteServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "UserName": NotRequired[str],
    },
)

DeleteSigningCertificateRequestRequestTypeDef = TypedDict(
    "DeleteSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "UserName": NotRequired[str],
    },
)

DeleteUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteUserPolicyRequestRequestTypeDef = TypedDict(
    "DeleteUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

DeleteVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
    },
)

DeletionTaskFailureReasonTypeTypeDef = TypedDict(
    "DeletionTaskFailureReasonTypeTypeDef",
    {
        "Reason": NotRequired[str],
        "RoleUsageList": NotRequired[List["RoleUsageTypeTypeDef"]],
    },
)

DetachGroupPolicyRequestGroupDetachPolicyTypeDef = TypedDict(
    "DetachGroupPolicyRequestGroupDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachGroupPolicyRequestPolicyDetachGroupTypeDef = TypedDict(
    "DetachGroupPolicyRequestPolicyDetachGroupTypeDef",
    {
        "GroupName": str,
    },
)

DetachGroupPolicyRequestRequestTypeDef = TypedDict(
    "DetachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestPolicyDetachRoleTypeDef = TypedDict(
    "DetachRolePolicyRequestPolicyDetachRoleTypeDef",
    {
        "RoleName": str,
    },
)

DetachRolePolicyRequestRequestTypeDef = TypedDict(
    "DetachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)

DetachRolePolicyRequestRoleDetachPolicyTypeDef = TypedDict(
    "DetachRolePolicyRequestRoleDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestPolicyDetachUserTypeDef = TypedDict(
    "DetachUserPolicyRequestPolicyDetachUserTypeDef",
    {
        "UserName": str,
    },
)

DetachUserPolicyRequestRequestTypeDef = TypedDict(
    "DetachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)

DetachUserPolicyRequestUserDetachPolicyTypeDef = TypedDict(
    "DetachUserPolicyRequestUserDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)

EnableMFADeviceRequestMfaDeviceAssociateTypeDef = TypedDict(
    "EnableMFADeviceRequestMfaDeviceAssociateTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestRequestTypeDef = TypedDict(
    "EnableMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EnableMFADeviceRequestUserEnableMfaTypeDef = TypedDict(
    "EnableMFADeviceRequestUserEnableMfaTypeDef",
    {
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

EntityDetailsTypeDef = TypedDict(
    "EntityDetailsTypeDef",
    {
        "EntityInfo": "EntityInfoTypeDef",
        "LastAuthenticated": NotRequired[datetime],
    },
)

EntityInfoTypeDef = TypedDict(
    "EntityInfoTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": policyOwnerEntityTypeType,
        "Id": str,
        "Path": NotRequired[str],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "Message": str,
        "Code": str,
    },
)

EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvalActionName": str,
        "EvalDecision": PolicyEvaluationDecisionTypeType,
        "EvalResourceName": NotRequired[str],
        "MatchedStatements": NotRequired[List["StatementTypeDef"]],
        "MissingContextValues": NotRequired[List[str]],
        "OrganizationsDecisionDetail": NotRequired["OrganizationsDecisionDetailTypeDef"],
        "PermissionsBoundaryDecisionDetail": NotRequired[
            "PermissionsBoundaryDecisionDetailTypeDef"
        ],
        "EvalDecisionDetails": NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]],
        "ResourceSpecificResults": NotRequired[List["ResourceSpecificResultTypeDef"]],
    },
)

GenerateCredentialReportResponseTypeDef = TypedDict(
    "GenerateCredentialReportResponseTypeDef",
    {
        "State": ReportStateTypeType,
        "Description": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportRequestRequestTypeDef",
    {
        "EntityPath": str,
        "OrganizationsPolicyId": NotRequired[str],
    },
)

GenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GenerateServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "Arn": str,
        "Granularity": NotRequired[AccessAdvisorUsageGranularityTypeType],
    },
)

GenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccessKeyLastUsedRequestRequestTypeDef = TypedDict(
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)

GetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "GetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": "AccessKeyLastUsedTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountAuthorizationDetailsRequestRequestTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    {
        "Filter": NotRequired[Sequence[EntityTypeType]],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List["UserDetailTypeDef"],
        "GroupDetailList": List["GroupDetailTypeDef"],
        "RoleDetailList": List["RoleDetailTypeDef"],
        "Policies": List["ManagedPolicyDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "GetAccountPasswordPolicyResponseTypeDef",
    {
        "PasswordPolicy": "PasswordPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSummaryResponseTypeDef = TypedDict(
    "GetAccountSummaryResponseTypeDef",
    {
        "SummaryMap": Dict[summaryKeyTypeType, int],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContextKeysForCustomPolicyRequestRequestTypeDef = TypedDict(
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": Sequence[str],
    },
)

GetContextKeysForPolicyResponseTypeDef = TypedDict(
    "GetContextKeysForPolicyResponseTypeDef",
    {
        "ContextKeyNames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContextKeysForPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "GetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
        "PolicyInputList": NotRequired[Sequence[str]],
    },
)

GetCredentialReportResponseTypeDef = TypedDict(
    "GetCredentialReportResponseTypeDef",
    {
        "Content": bytes,
        "ReportFormat": Literal["text/csv"],
        "GeneratedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)

GetGroupPolicyResponseTypeDef = TypedDict(
    "GetGroupPolicyResponseTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": "GroupTypeDef",
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)

GetInstanceProfileResponseTypeDef = TypedDict(
    "GetInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": "InstanceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLoginProfileRequestRequestTypeDef = TypedDict(
    "GetLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)

GetLoginProfileResponseTypeDef = TypedDict(
    "GetLoginProfileResponseTypeDef",
    {
        "LoginProfile": "LoginProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)

GetOpenIDConnectProviderResponseTypeDef = TypedDict(
    "GetOpenIDConnectProviderResponseTypeDef",
    {
        "Url": str,
        "ClientIDList": List[str],
        "ThumbprintList": List[str],
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "GetOrganizationsAccessReportRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "SortKey": NotRequired[sortKeyTypeType],
    },
)

GetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List["AccessDetailTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)

GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": "PolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPolicyVersionRequestRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

GetPolicyVersionResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseTypeDef",
    {
        "PolicyVersion": "PolicyVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRolePolicyRequestRequestTypeDef = TypedDict(
    "GetRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)

GetRolePolicyResponseTypeDef = TypedDict(
    "GetRolePolicyResponseTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoleRequestRequestTypeDef = TypedDict(
    "GetRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)

GetRoleResponseTypeDef = TypedDict(
    "GetRoleResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSAMLProviderRequestRequestTypeDef = TypedDict(
    "GetSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)

GetSAMLProviderResponseTypeDef = TypedDict(
    "GetSAMLProviderResponseTypeDef",
    {
        "SAMLMetadataDocument": str,
        "CreateDate": datetime,
        "ValidUntil": datetime,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "GetSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Encoding": encodingTypeType,
    },
)

GetSSHPublicKeyResponseTypeDef = TypedDict(
    "GetSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServerCertificateRequestRequestTypeDef = TypedDict(
    "GetServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)

GetServerCertificateResponseTypeDef = TypedDict(
    "GetServerCertificateResponseTypeDef",
    {
        "ServerCertificate": "ServerCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobType": AccessAdvisorUsageGranularityTypeType,
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List["ServiceLastAccessedTypeDef"],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    {
        "JobId": str,
        "ServiceNamespace": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": jobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List["EntityDetailsTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "Error": "ErrorDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    {
        "DeletionTaskId": str,
    },
)

GetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": DeletionTaskStatusTypeType,
        "Reason": "DeletionTaskFailureReasonTypeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserPolicyRequestRequestTypeDef = TypedDict(
    "GetUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)

GetUserPolicyResponseTypeDef = TypedDict(
    "GetUserPolicyResponseTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupDetailTypeDef = TypedDict(
    "GroupDetailTypeDef",
    {
        "Path": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "GroupPolicyList": NotRequired[List["PolicyDetailTypeDef"]],
        "AttachedManagedPolicies": NotRequired[List["AttachedPolicyTypeDef"]],
    },
)

GroupPolicyRequestTypeDef = TypedDict(
    "GroupPolicyRequestTypeDef",
    {
        "name": str,
    },
)

GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)

InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List["RoleTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ListAccessKeysRequestRequestTypeDef = TypedDict(
    "ListAccessKeysRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAccessKeysResponseTypeDef = TypedDict(
    "ListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List["AccessKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountAliasesRequestRequestTypeDef = TypedDict(
    "ListAccountAliasesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAccountAliasesResponseTypeDef = TypedDict(
    "ListAccountAliasesResponseTypeDef",
    {
        "AccountAliases": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttachedGroupPoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttachedRolePoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttachedUserPoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List["AttachedPolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesForPolicyRequestRequestTypeDef = TypedDict(
    "ListEntitiesForPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "EntityFilter": NotRequired[EntityTypeType],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List["PolicyGroupTypeDef"],
        "PolicyUsers": List["PolicyUserTypeDef"],
        "PolicyRoles": List["PolicyRoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupPoliciesRequestRequestTypeDef = TypedDict(
    "ListGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListGroupPoliciesResponseTypeDef = TypedDict(
    "ListGroupPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsForUserRequestRequestTypeDef = TypedDict(
    "ListGroupsForUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListGroupsForUserResponseTypeDef = TypedDict(
    "ListGroupsForUserResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List["GroupTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfileTagsRequestRequestTypeDef = TypedDict(
    "ListInstanceProfileTagsRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListInstanceProfileTagsResponseTypeDef = TypedDict(
    "ListInstanceProfileTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesForRoleRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesForRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "ListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListInstanceProfilesResponseTypeDef = TypedDict(
    "ListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List["InstanceProfileTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMFADeviceTagsRequestRequestTypeDef = TypedDict(
    "ListMFADeviceTagsRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListMFADeviceTagsResponseTypeDef = TypedDict(
    "ListMFADeviceTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMFADevicesRequestRequestTypeDef = TypedDict(
    "ListMFADevicesRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListMFADevicesResponseTypeDef = TypedDict(
    "ListMFADevicesResponseTypeDef",
    {
        "MFADevices": List["MFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpenIDConnectProviderTagsRequestRequestTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListOpenIDConnectProviderTagsResponseTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOpenIDConnectProvidersResponseTypeDef = TypedDict(
    "ListOpenIDConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List["OpenIDConnectProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesGrantingServiceAccessEntryTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    {
        "ServiceNamespace": NotRequired[str],
        "Policies": NotRequired[List["PolicyGrantingServiceAccessTypeDef"]],
    },
)

ListPoliciesGrantingServiceAccessRequestRequestTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    {
        "Arn": str,
        "ServiceNamespaces": Sequence[str],
        "Marker": NotRequired[str],
    },
)

ListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List["ListPoliciesGrantingServiceAccessEntryTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "Scope": NotRequired[policyScopeTypeType],
        "OnlyAttached": NotRequired[bool],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "Policies": List["PolicyTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyTagsRequestRequestTypeDef = TypedDict(
    "ListPolicyTagsRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListPolicyTagsResponseTypeDef = TypedDict(
    "ListPolicyTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListPolicyVersionsRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {
        "Versions": List["PolicyVersionTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRolePoliciesRequestRequestTypeDef = TypedDict(
    "ListRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListRolePoliciesResponseTypeDef = TypedDict(
    "ListRolePoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoleTagsRequestRequestTypeDef = TypedDict(
    "ListRoleTagsRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListRoleTagsResponseTypeDef = TypedDict(
    "ListRoleTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRolesRequestRequestTypeDef = TypedDict(
    "ListRolesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListRolesResponseTypeDef = TypedDict(
    "ListRolesResponseTypeDef",
    {
        "Roles": List["RoleTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSAMLProviderTagsRequestRequestTypeDef = TypedDict(
    "ListSAMLProviderTagsRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListSAMLProviderTagsResponseTypeDef = TypedDict(
    "ListSAMLProviderTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSAMLProvidersResponseTypeDef = TypedDict(
    "ListSAMLProvidersResponseTypeDef",
    {
        "SAMLProviderList": List["SAMLProviderListEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSSHPublicKeysRequestRequestTypeDef = TypedDict(
    "ListSSHPublicKeysRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListSSHPublicKeysResponseTypeDef = TypedDict(
    "ListSSHPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List["SSHPublicKeyMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServerCertificateTagsRequestRequestTypeDef = TypedDict(
    "ListServerCertificateTagsRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListServerCertificateTagsResponseTypeDef = TypedDict(
    "ListServerCertificateTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServerCertificatesRequestRequestTypeDef = TypedDict(
    "ListServerCertificatesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListServerCertificatesResponseTypeDef = TypedDict(
    "ListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List["ServerCertificateMetadataTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceSpecificCredentialsRequestRequestTypeDef = TypedDict(
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)

ListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "ListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List["ServiceSpecificCredentialMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSigningCertificatesRequestRequestTypeDef = TypedDict(
    "ListSigningCertificatesRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListSigningCertificatesResponseTypeDef = TypedDict(
    "ListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List["SigningCertificateTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserPoliciesRequestRequestTypeDef = TypedDict(
    "ListUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListUserPoliciesResponseTypeDef = TypedDict(
    "ListUserPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserTagsRequestRequestTypeDef = TypedDict(
    "ListUserTagsRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListUserTagsResponseTypeDef = TypedDict(
    "ListUserTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVirtualMFADevicesRequestRequestTypeDef = TypedDict(
    "ListVirtualMFADevicesRequestRequestTypeDef",
    {
        "AssignmentStatus": NotRequired[assignmentStatusTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)

ListVirtualMFADevicesResponseTypeDef = TypedDict(
    "ListVirtualMFADevicesResponseTypeDef",
    {
        "VirtualMFADevices": List["VirtualMFADeviceTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoginProfileTypeDef = TypedDict(
    "LoginProfileTypeDef",
    {
        "UserName": str,
        "CreateDate": datetime,
        "PasswordResetRequired": NotRequired[bool],
    },
)

MFADeviceTypeDef = TypedDict(
    "MFADeviceTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "EnableDate": datetime,
    },
)

ManagedPolicyDetailTypeDef = TypedDict(
    "ManagedPolicyDetailTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyId": NotRequired[str],
        "Arn": NotRequired[str],
        "Path": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "AttachmentCount": NotRequired[int],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "IsAttachable": NotRequired[bool],
        "Description": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "PolicyVersionList": NotRequired[List["PolicyVersionTypeDef"]],
    },
)

OpenIDConnectProviderListEntryTypeDef = TypedDict(
    "OpenIDConnectProviderListEntryTypeDef",
    {
        "Arn": NotRequired[str],
    },
)

OrganizationsDecisionDetailTypeDef = TypedDict(
    "OrganizationsDecisionDetailTypeDef",
    {
        "AllowedByOrganizations": NotRequired[bool],
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

PasswordPolicyTypeDef = TypedDict(
    "PasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "ExpirePasswords": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)

PermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "PermissionsBoundaryDecisionDetailTypeDef",
    {
        "AllowedByPermissionsBoundary": NotRequired[bool],
    },
)

PolicyDetailTypeDef = TypedDict(
    "PolicyDetailTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyDocument": NotRequired[str],
    },
)

PolicyGrantingServiceAccessTypeDef = TypedDict(
    "PolicyGrantingServiceAccessTypeDef",
    {
        "PolicyName": str,
        "PolicyType": policyTypeType,
        "PolicyArn": NotRequired[str],
        "EntityType": NotRequired[policyOwnerEntityTypeType],
        "EntityName": NotRequired[str],
    },
)

PolicyGroupTypeDef = TypedDict(
    "PolicyGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)

PolicyRoleTypeDef = TypedDict(
    "PolicyRoleTypeDef",
    {
        "RoleName": NotRequired[str],
        "RoleId": NotRequired[str],
    },
)

PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyId": NotRequired[str],
        "Arn": NotRequired[str],
        "Path": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "AttachmentCount": NotRequired[int],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "IsAttachable": NotRequired[bool],
        "Description": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

PolicyUserTypeDef = TypedDict(
    "PolicyUserTypeDef",
    {
        "UserName": NotRequired[str],
        "UserId": NotRequired[str],
    },
)

PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "Document": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "CreateDate": NotRequired[datetime],
    },
)

PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "Line": NotRequired[int],
        "Column": NotRequired[int],
    },
)

PutGroupPolicyRequestGroupCreatePolicyTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestGroupPolicyPutTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupPolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutGroupPolicyRequestRequestTypeDef = TypedDict(
    "PutGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
        "PermissionsBoundary": str,
    },
)

PutRolePolicyRequestRequestTypeDef = TypedDict(
    "PutRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutRolePolicyRequestRolePolicyPutTypeDef = TypedDict(
    "PutRolePolicyRequestRolePolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)

PutUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
        "PermissionsBoundary": str,
    },
)

PutUserPolicyRequestRequestTypeDef = TypedDict(
    "PutUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserCreatePolicyTypeDef = TypedDict(
    "PutUserPolicyRequestUserCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)

PutUserPolicyRequestUserPolicyPutTypeDef = TypedDict(
    "PutUserPolicyRequestUserPolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)

RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)

RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef",
    {
        "RoleName": str,
    },
)

RemoveRoleFromInstanceProfileRequestRequestTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)

RemoveUserFromGroupRequestGroupRemoveUserTypeDef = TypedDict(
    "RemoveUserFromGroupRequestGroupRemoveUserTypeDef",
    {
        "UserName": str,
    },
)

RemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "RemoveUserFromGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)

RemoveUserFromGroupRequestUserRemoveGroupTypeDef = TypedDict(
    "RemoveUserFromGroupRequestUserRemoveGroupTypeDef",
    {
        "GroupName": str,
    },
)

ResetServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "ResetServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "UserName": NotRequired[str],
    },
)

ResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": "ServiceSpecificCredentialTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceSpecificResultTypeDef = TypedDict(
    "ResourceSpecificResultTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": PolicyEvaluationDecisionTypeType,
        "MatchedStatements": NotRequired[List["StatementTypeDef"]],
        "MissingContextValues": NotRequired[List[str]],
        "EvalDecisionDetails": NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]],
        "PermissionsBoundaryDecisionDetail": NotRequired[
            "PermissionsBoundaryDecisionDetailTypeDef"
        ],
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

ResyncMFADeviceRequestMfaDeviceResyncTypeDef = TypedDict(
    "ResyncMFADeviceRequestMfaDeviceResyncTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

ResyncMFADeviceRequestRequestTypeDef = TypedDict(
    "ResyncMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)

RoleDetailTypeDef = TypedDict(
    "RoleDetailTypeDef",
    {
        "Path": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "AssumeRolePolicyDocument": NotRequired[str],
        "InstanceProfileList": NotRequired[List["InstanceProfileTypeDef"]],
        "RolePolicyList": NotRequired[List["PolicyDetailTypeDef"]],
        "AttachedManagedPolicies": NotRequired[List["AttachedPolicyTypeDef"]],
        "PermissionsBoundary": NotRequired["AttachedPermissionsBoundaryTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "RoleLastUsed": NotRequired["RoleLastUsedTypeDef"],
    },
)

RoleLastUsedResponseMetadataTypeDef = TypedDict(
    "RoleLastUsedResponseMetadataTypeDef",
    {
        "LastUsedDate": datetime,
        "Region": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RoleLastUsedTypeDef = TypedDict(
    "RoleLastUsedTypeDef",
    {
        "LastUsedDate": NotRequired[datetime],
        "Region": NotRequired[str],
    },
)

RolePolicyRequestTypeDef = TypedDict(
    "RolePolicyRequestTypeDef",
    {
        "name": str,
    },
)

RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": NotRequired[str],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired["AttachedPermissionsBoundaryTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
        "RoleLastUsed": NotRequired["RoleLastUsedTypeDef"],
    },
)

RoleUsageTypeTypeDef = TypedDict(
    "RoleUsageTypeTypeDef",
    {
        "Region": NotRequired[str],
        "Resources": NotRequired[List[str]],
    },
)

SAMLProviderListEntryTypeDef = TypedDict(
    "SAMLProviderListEntryTypeDef",
    {
        "Arn": NotRequired[str],
        "ValidUntil": NotRequired[datetime],
        "CreateDate": NotRequired[datetime],
    },
)

SSHPublicKeyMetadataTypeDef = TypedDict(
    "SSHPublicKeyMetadataTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
        "UploadDate": datetime,
    },
)

SSHPublicKeyTypeDef = TypedDict(
    "SSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": statusTypeType,
        "UploadDate": NotRequired[datetime],
    },
)

ServerCertificateMetadataResponseMetadataTypeDef = TypedDict(
    "ServerCertificateMetadataResponseMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": datetime,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerCertificateMetadataTypeDef = TypedDict(
    "ServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": NotRequired[datetime],
        "Expiration": NotRequired[datetime],
    },
)

ServerCertificateTypeDef = TypedDict(
    "ServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "CertificateBody": str,
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ServiceLastAccessedTypeDef = TypedDict(
    "ServiceLastAccessedTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "LastAuthenticated": NotRequired[datetime],
        "LastAuthenticatedEntity": NotRequired[str],
        "LastAuthenticatedRegion": NotRequired[str],
        "TotalAuthenticatedEntities": NotRequired[int],
        "TrackedActionsLastAccessed": NotRequired[List["TrackedActionLastAccessedTypeDef"]],
    },
)

ServiceResourceAccessKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyPairRequestTypeDef",
    {
        "user_name": str,
        "id": str,
        "secret": str,
    },
)

ServiceResourceAccessKeyRequestTypeDef = TypedDict(
    "ServiceResourceAccessKeyRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceAssumeRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceAssumeRolePolicyRequestTypeDef",
    {
        "role_name": str,
    },
)

ServiceResourceGroupPolicyRequestTypeDef = TypedDict(
    "ServiceResourceGroupPolicyRequestTypeDef",
    {
        "group_name": str,
        "name": str,
    },
)

ServiceResourceGroupRequestTypeDef = TypedDict(
    "ServiceResourceGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceInstanceProfileRequestTypeDef = TypedDict(
    "ServiceResourceInstanceProfileRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceLoginProfileRequestTypeDef = TypedDict(
    "ServiceResourceLoginProfileRequestTypeDef",
    {
        "user_name": str,
    },
)

ServiceResourceMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceMfaDeviceRequestTypeDef",
    {
        "user_name": str,
        "serial_number": str,
    },
)

ServiceResourcePolicyRequestTypeDef = TypedDict(
    "ServiceResourcePolicyRequestTypeDef",
    {
        "policy_arn": str,
    },
)

ServiceResourcePolicyVersionRequestTypeDef = TypedDict(
    "ServiceResourcePolicyVersionRequestTypeDef",
    {
        "arn": str,
        "version_id": str,
    },
)

ServiceResourceRolePolicyRequestTypeDef = TypedDict(
    "ServiceResourceRolePolicyRequestTypeDef",
    {
        "role_name": str,
        "name": str,
    },
)

ServiceResourceRoleRequestTypeDef = TypedDict(
    "ServiceResourceRoleRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSamlProviderRequestTypeDef = TypedDict(
    "ServiceResourceSamlProviderRequestTypeDef",
    {
        "arn": str,
    },
)

ServiceResourceServerCertificateRequestTypeDef = TypedDict(
    "ServiceResourceServerCertificateRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceSigningCertificateRequestTypeDef = TypedDict(
    "ServiceResourceSigningCertificateRequestTypeDef",
    {
        "user_name": str,
        "id": str,
    },
)

ServiceResourceUserPolicyRequestTypeDef = TypedDict(
    "ServiceResourceUserPolicyRequestTypeDef",
    {
        "user_name": str,
        "name": str,
    },
)

ServiceResourceUserRequestTypeDef = TypedDict(
    "ServiceResourceUserRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceVirtualMfaDeviceRequestTypeDef = TypedDict(
    "ServiceResourceVirtualMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

ServiceSpecificCredentialMetadataTypeDef = TypedDict(
    "ServiceSpecificCredentialMetadataTypeDef",
    {
        "UserName": str,
        "Status": statusTypeType,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
)

ServiceSpecificCredentialTypeDef = TypedDict(
    "ServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": statusTypeType,
    },
)

SetDefaultPolicyVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)

SetSecurityTokenServicePreferencesRequestRequestTypeDef = TypedDict(
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    {
        "GlobalEndpointTokenVersion": globalEndpointTokenVersionType,
    },
)

SigningCertificateTypeDef = TypedDict(
    "SigningCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": statusTypeType,
        "UploadDate": NotRequired[datetime],
    },
)

SimulateCustomPolicyRequestRequestTypeDef = TypedDict(
    "SimulateCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": Sequence[str],
        "ActionNames": Sequence[str],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence["ContextEntryTypeDef"]],
        "ResourceHandlingOption": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

SimulatePolicyResponseTypeDef = TypedDict(
    "SimulatePolicyResponseTypeDef",
    {
        "EvaluationResults": List["EvaluationResultTypeDef"],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SimulatePrincipalPolicyRequestRequestTypeDef = TypedDict(
    "SimulatePrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
        "ActionNames": Sequence[str],
        "PolicyInputList": NotRequired[Sequence[str]],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence["ContextEntryTypeDef"]],
        "ResourceHandlingOption": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "SourcePolicyId": NotRequired[str],
        "SourcePolicyType": NotRequired[PolicySourceTypeType],
        "StartPosition": NotRequired["PositionTypeDef"],
        "EndPosition": NotRequired["PositionTypeDef"],
    },
)

TagInstanceProfileRequestRequestTypeDef = TypedDict(
    "TagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagMFADeviceRequestRequestTypeDef = TypedDict(
    "TagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagPolicyRequestRequestTypeDef = TypedDict(
    "TagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagRoleRequestRequestTypeDef = TypedDict(
    "TagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagSAMLProviderRequestRequestTypeDef = TypedDict(
    "TagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagServerCertificateRequestRequestTypeDef = TypedDict(
    "TagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
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

TagUserRequestRequestTypeDef = TypedDict(
    "TagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TrackedActionLastAccessedTypeDef = TypedDict(
    "TrackedActionLastAccessedTypeDef",
    {
        "ActionName": NotRequired[str],
        "LastAccessedEntity": NotRequired[str],
        "LastAccessedTime": NotRequired[datetime],
        "LastAccessedRegion": NotRequired[str],
    },
)

UntagInstanceProfileRequestRequestTypeDef = TypedDict(
    "UntagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "TagKeys": Sequence[str],
    },
)

UntagMFADeviceRequestRequestTypeDef = TypedDict(
    "UntagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "TagKeys": Sequence[str],
    },
)

UntagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "TagKeys": Sequence[str],
    },
)

UntagPolicyRequestRequestTypeDef = TypedDict(
    "UntagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "TagKeys": Sequence[str],
    },
)

UntagRoleRequestRequestTypeDef = TypedDict(
    "UntagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "TagKeys": Sequence[str],
    },
)

UntagSAMLProviderRequestRequestTypeDef = TypedDict(
    "UntagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "TagKeys": Sequence[str],
    },
)

UntagServerCertificateRequestRequestTypeDef = TypedDict(
    "UntagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "TagKeys": Sequence[str],
    },
)

UntagUserRequestRequestTypeDef = TypedDict(
    "UntagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAccessKeyRequestAccessKeyActivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyActivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateAccessKeyRequestAccessKeyDeactivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyDeactivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateAccessKeyRequestAccessKeyPairActivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairActivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateAccessKeyRequestRequestTypeDef = TypedDict(
    "UpdateAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
        "Status": statusTypeType,
        "UserName": NotRequired[str],
    },
)

UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)

UpdateAccountPasswordPolicyRequestRequestTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)

UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)

UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef",
    {
        "PolicyDocument": str,
    },
)

UpdateAssumeRolePolicyRequestRequestTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyDocument": str,
    },
)

UpdateGroupRequestGroupUpdateTypeDef = TypedDict(
    "UpdateGroupRequestGroupUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewGroupName": NotRequired[str],
    },
)

UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "NewPath": NotRequired[str],
        "NewGroupName": NotRequired[str],
    },
)

UpdateLoginProfileRequestLoginProfileUpdateTypeDef = TypedDict(
    "UpdateLoginProfileRequestLoginProfileUpdateTypeDef",
    {
        "Password": NotRequired[str],
        "PasswordResetRequired": NotRequired[bool],
    },
)

UpdateLoginProfileRequestRequestTypeDef = TypedDict(
    "UpdateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": NotRequired[str],
        "PasswordResetRequired": NotRequired[bool],
    },
)

UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef = TypedDict(
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ThumbprintList": Sequence[str],
    },
)

UpdateRoleDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateRoleDescriptionRequestRequestTypeDef",
    {
        "RoleName": str,
        "Description": str,
    },
)

UpdateRoleDescriptionResponseTypeDef = TypedDict(
    "UpdateRoleDescriptionResponseTypeDef",
    {
        "Role": "RoleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRoleRequestRequestTypeDef = TypedDict(
    "UpdateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
    },
)

UpdateSAMLProviderRequestRequestTypeDef = TypedDict(
    "UpdateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "SAMLProviderArn": str,
    },
)

UpdateSAMLProviderRequestSamlProviderUpdateTypeDef = TypedDict(
    "UpdateSAMLProviderRequestSamlProviderUpdateTypeDef",
    {
        "SAMLMetadataDocument": str,
    },
)

UpdateSAMLProviderResponseTypeDef = TypedDict(
    "UpdateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": statusTypeType,
    },
)

UpdateServerCertificateRequestRequestTypeDef = TypedDict(
    "UpdateServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "NewPath": NotRequired[str],
        "NewServerCertificateName": NotRequired[str],
    },
)

UpdateServerCertificateRequestServerCertificateUpdateTypeDef = TypedDict(
    "UpdateServerCertificateRequestServerCertificateUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewServerCertificateName": NotRequired[str],
    },
)

UpdateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "UpdateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "Status": statusTypeType,
        "UserName": NotRequired[str],
    },
)

UpdateSigningCertificateRequestRequestTypeDef = TypedDict(
    "UpdateSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "Status": statusTypeType,
        "UserName": NotRequired[str],
    },
)

UpdateSigningCertificateRequestSigningCertificateActivateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateActivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef",
    {
        "Status": NotRequired[statusTypeType],
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "NewPath": NotRequired[str],
        "NewUserName": NotRequired[str],
    },
)

UpdateUserRequestUserUpdateTypeDef = TypedDict(
    "UpdateUserRequestUserUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewUserName": NotRequired[str],
    },
)

UploadSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UploadSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyBody": str,
    },
)

UploadSSHPublicKeyResponseTypeDef = TypedDict(
    "UploadSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": "SSHPublicKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadServerCertificateRequestRequestTypeDef = TypedDict(
    "UploadServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
        "Path": NotRequired[str],
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef = TypedDict(
    "UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
        "Path": NotRequired[str],
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

UploadServerCertificateResponseTypeDef = TypedDict(
    "UploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": "ServerCertificateMetadataTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadSigningCertificateRequestRequestTypeDef = TypedDict(
    "UploadSigningCertificateRequestRequestTypeDef",
    {
        "CertificateBody": str,
        "UserName": NotRequired[str],
    },
)

UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef = TypedDict(
    "UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef",
    {
        "CertificateBody": str,
        "UserName": NotRequired[str],
    },
)

UploadSigningCertificateResponseTypeDef = TypedDict(
    "UploadSigningCertificateResponseTypeDef",
    {
        "Certificate": "SigningCertificateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserAccessKeyRequestTypeDef = TypedDict(
    "UserAccessKeyRequestTypeDef",
    {
        "id": str,
    },
)

UserDetailTypeDef = TypedDict(
    "UserDetailTypeDef",
    {
        "Path": NotRequired[str],
        "UserName": NotRequired[str],
        "UserId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UserPolicyList": NotRequired[List["PolicyDetailTypeDef"]],
        "GroupList": NotRequired[List[str]],
        "AttachedManagedPolicies": NotRequired[List["AttachedPolicyTypeDef"]],
        "PermissionsBoundary": NotRequired["AttachedPermissionsBoundaryTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

UserMfaDeviceRequestTypeDef = TypedDict(
    "UserMfaDeviceRequestTypeDef",
    {
        "serial_number": str,
    },
)

UserPolicyRequestTypeDef = TypedDict(
    "UserPolicyRequestTypeDef",
    {
        "name": str,
    },
)

UserResponseMetadataTypeDef = TypedDict(
    "UserResponseMetadataTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": datetime,
        "PermissionsBoundary": "AttachedPermissionsBoundaryTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserSigningCertificateRequestTypeDef = TypedDict(
    "UserSigningCertificateRequestTypeDef",
    {
        "id": str,
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": NotRequired[datetime],
        "PermissionsBoundary": NotRequired["AttachedPermissionsBoundaryTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

VirtualMFADeviceTypeDef = TypedDict(
    "VirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": NotRequired[bytes],
        "QRCodePNG": NotRequired[bytes],
        "User": NotRequired["UserTypeDef"],
        "EnableDate": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
