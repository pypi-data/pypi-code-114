"""
Type annotations for grafana service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_grafana/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_grafana.type_defs import AssertionAttributesTypeDef

    data: AssertionAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccountAccessTypeType,
    AuthenticationProviderTypesType,
    DataSourceTypeType,
    LicenseTypeType,
    PermissionTypeType,
    RoleType,
    SamlConfigurationStatusType,
    UpdateActionType,
    UserTypeType,
    WorkspaceStatusType,
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
    "AssertionAttributesTypeDef",
    "AssociateLicenseRequestRequestTypeDef",
    "AssociateLicenseResponseTypeDef",
    "AuthenticationDescriptionTypeDef",
    "AuthenticationSummaryTypeDef",
    "AwsSsoAuthenticationTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "DeleteWorkspaceResponseTypeDef",
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    "DescribeWorkspaceRequestRequestTypeDef",
    "DescribeWorkspaceResponseTypeDef",
    "DisassociateLicenseRequestRequestTypeDef",
    "DisassociateLicenseResponseTypeDef",
    "IdpMetadataTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionEntryTypeDef",
    "ResponseMetadataTypeDef",
    "RoleValuesTypeDef",
    "SamlAuthenticationTypeDef",
    "SamlConfigurationTypeDef",
    "UpdateErrorTypeDef",
    "UpdateInstructionTypeDef",
    "UpdatePermissionsRequestRequestTypeDef",
    "UpdatePermissionsResponseTypeDef",
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "UserTypeDef",
    "WorkspaceDescriptionTypeDef",
    "WorkspaceSummaryTypeDef",
)

AssertionAttributesTypeDef = TypedDict(
    "AssertionAttributesTypeDef",
    {
        "email": NotRequired[str],
        "groups": NotRequired[str],
        "login": NotRequired[str],
        "name": NotRequired[str],
        "org": NotRequired[str],
        "role": NotRequired[str],
    },
)

AssociateLicenseRequestRequestTypeDef = TypedDict(
    "AssociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)

AssociateLicenseResponseTypeDef = TypedDict(
    "AssociateLicenseResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthenticationDescriptionTypeDef = TypedDict(
    "AuthenticationDescriptionTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "awsSso": NotRequired["AwsSsoAuthenticationTypeDef"],
        "saml": NotRequired["SamlAuthenticationTypeDef"],
    },
)

AuthenticationSummaryTypeDef = TypedDict(
    "AuthenticationSummaryTypeDef",
    {
        "providers": List[AuthenticationProviderTypesType],
        "samlConfigurationStatus": NotRequired[SamlConfigurationStatusType],
    },
)

AwsSsoAuthenticationTypeDef = TypedDict(
    "AwsSsoAuthenticationTypeDef",
    {
        "ssoClientId": NotRequired[str],
    },
)

CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "accountAccessType": AccountAccessTypeType,
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "permissionType": PermissionTypeType,
        "clientToken": NotRequired[str],
        "organizationRoleName": NotRequired[str],
        "stackSetName": NotRequired[str],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DeleteWorkspaceResponseTypeDef = TypedDict(
    "DeleteWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "DescribeWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": "AuthenticationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

DescribeWorkspaceResponseTypeDef = TypedDict(
    "DescribeWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateLicenseRequestRequestTypeDef = TypedDict(
    "DisassociateLicenseRequestRequestTypeDef",
    {
        "licenseType": LicenseTypeType,
        "workspaceId": str,
    },
)

DisassociateLicenseResponseTypeDef = TypedDict(
    "DisassociateLicenseResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdpMetadataTypeDef = TypedDict(
    "IdpMetadataTypeDef",
    {
        "url": NotRequired[str],
        "xml": NotRequired[str],
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "workspaceId": str,
        "groupId": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "userId": NotRequired[str],
        "userType": NotRequired[UserTypeType],
    },
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "nextToken": str,
        "permissions": List["PermissionEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaces": List["WorkspaceSummaryTypeDef"],
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

PermissionEntryTypeDef = TypedDict(
    "PermissionEntryTypeDef",
    {
        "role": RoleType,
        "user": "UserTypeDef",
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

RoleValuesTypeDef = TypedDict(
    "RoleValuesTypeDef",
    {
        "admin": NotRequired[List[str]],
        "editor": NotRequired[List[str]],
    },
)

SamlAuthenticationTypeDef = TypedDict(
    "SamlAuthenticationTypeDef",
    {
        "status": SamlConfigurationStatusType,
        "configuration": NotRequired["SamlConfigurationTypeDef"],
    },
)

SamlConfigurationTypeDef = TypedDict(
    "SamlConfigurationTypeDef",
    {
        "idpMetadata": "IdpMetadataTypeDef",
        "allowedOrganizations": NotRequired[List[str]],
        "assertionAttributes": NotRequired["AssertionAttributesTypeDef"],
        "loginValidityDuration": NotRequired[int],
        "roleValues": NotRequired["RoleValuesTypeDef"],
    },
)

UpdateErrorTypeDef = TypedDict(
    "UpdateErrorTypeDef",
    {
        "causedBy": "UpdateInstructionTypeDef",
        "code": int,
        "message": str,
    },
)

UpdateInstructionTypeDef = TypedDict(
    "UpdateInstructionTypeDef",
    {
        "action": UpdateActionType,
        "role": RoleType,
        "users": Sequence["UserTypeDef"],
    },
)

UpdatePermissionsRequestRequestTypeDef = TypedDict(
    "UpdatePermissionsRequestRequestTypeDef",
    {
        "updateInstructionBatch": Sequence["UpdateInstructionTypeDef"],
        "workspaceId": str,
    },
)

UpdatePermissionsResponseTypeDef = TypedDict(
    "UpdatePermissionsResponseTypeDef",
    {
        "errors": List["UpdateErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkspaceAuthenticationRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationRequestRequestTypeDef",
    {
        "authenticationProviders": Sequence[AuthenticationProviderTypesType],
        "workspaceId": str,
        "samlConfiguration": NotRequired["SamlConfigurationTypeDef"],
    },
)

UpdateWorkspaceAuthenticationResponseTypeDef = TypedDict(
    "UpdateWorkspaceAuthenticationResponseTypeDef",
    {
        "authentication": "AuthenticationDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "organizationRoleName": NotRequired[str],
        "permissionType": NotRequired[PermissionTypeType],
        "stackSetName": NotRequired[str],
        "workspaceDataSources": NotRequired[Sequence[DataSourceTypeType]],
        "workspaceDescription": NotRequired[str],
        "workspaceName": NotRequired[str],
        "workspaceNotificationDestinations": NotRequired[Sequence[Literal["SNS"]]],
        "workspaceOrganizationalUnits": NotRequired[Sequence[str]],
        "workspaceRoleArn": NotRequired[str],
    },
)

UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "workspace": "WorkspaceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "id": str,
        "type": UserTypeType,
    },
)

WorkspaceDescriptionTypeDef = TypedDict(
    "WorkspaceDescriptionTypeDef",
    {
        "authentication": "AuthenticationSummaryTypeDef",
        "created": datetime,
        "dataSources": List[DataSourceTypeType],
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "accountAccessType": NotRequired[AccountAccessTypeType],
        "description": NotRequired[str],
        "freeTrialConsumed": NotRequired[bool],
        "freeTrialExpiration": NotRequired[datetime],
        "licenseExpiration": NotRequired[datetime],
        "licenseType": NotRequired[LicenseTypeType],
        "name": NotRequired[str],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
        "organizationRoleName": NotRequired[str],
        "organizationalUnits": NotRequired[List[str]],
        "permissionType": NotRequired[PermissionTypeType],
        "stackSetName": NotRequired[str],
        "workspaceRoleArn": NotRequired[str],
    },
)

WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "authentication": "AuthenticationSummaryTypeDef",
        "created": datetime,
        "endpoint": str,
        "grafanaVersion": str,
        "id": str,
        "modified": datetime,
        "status": WorkspaceStatusType,
        "description": NotRequired[str],
        "name": NotRequired[str],
        "notificationDestinations": NotRequired[List[Literal["SNS"]]],
    },
)
