"""
Type annotations for workspaces service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AccessPropertyValueType,
    ApplicationType,
    AssociationStatusType,
    ComputeType,
    ConnectionAliasStateType,
    ConnectionStateType,
    DedicatedTenancyModificationStateEnumType,
    DedicatedTenancySupportResultEnumType,
    ImageTypeType,
    ModificationResourceEnumType,
    ModificationStateEnumType,
    OperatingSystemTypeType,
    ReconnectEnumType,
    RunningModeType,
    TargetWorkspaceStateType,
    TenancyType,
    WorkspaceDirectoryStateType,
    WorkspaceDirectoryTypeType,
    WorkspaceImageIngestionProcessType,
    WorkspaceImageRequiredTenancyType,
    WorkspaceImageStateType,
    WorkspaceStateType,
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
    "AccountModificationTypeDef",
    "AssociateConnectionAliasRequestRequestTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "AssociateIpGroupsRequestRequestTypeDef",
    "AuthorizeIpRulesRequestRequestTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectClientAddInTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "CopyWorkspaceImageRequestRequestTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateConnectClientAddInRequestRequestTypeDef",
    "CreateConnectClientAddInResultTypeDef",
    "CreateConnectionAliasRequestRequestTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupRequestRequestTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateUpdatedWorkspaceImageRequestRequestTypeDef",
    "CreateUpdatedWorkspaceImageResultTypeDef",
    "CreateWorkspaceBundleRequestRequestTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspacesRequestRequestTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DeleteConnectClientAddInRequestRequestTypeDef",
    "DeleteConnectionAliasRequestRequestTypeDef",
    "DeleteIpGroupRequestRequestTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    "DeleteWorkspaceImageRequestRequestTypeDef",
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    "DescribeAccountModificationsRequestRequestTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeClientPropertiesRequestRequestTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectClientAddInsRequestRequestTypeDef",
    "DescribeConnectClientAddInsResultTypeDef",
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesRequestRequestTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeIpGroupsRequestRequestTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesRequestRequestTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "DisassociateConnectionAliasRequestRequestTypeDef",
    "DisassociateIpGroupsRequestRequestTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "ImportWorkspaceImageRequestRequestTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "IpRuleItemTypeDef",
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceRequestRequestTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "ModificationStateTypeDef",
    "ModifyAccountRequestRequestTypeDef",
    "ModifyClientPropertiesRequestRequestTypeDef",
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    "ModifyWorkspaceStateRequestRequestTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesRequestRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesRequestRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreWorkspaceRequestRequestTypeDef",
    "RevokeIpRulesRequestRequestTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesRequestRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesRequestRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesRequestRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "UpdateConnectClientAddInRequestRequestTypeDef",
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    "UpdateResultTypeDef",
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
)

AccountModificationTypeDef = TypedDict(
    "AccountModificationTypeDef",
    {
        "ModificationState": NotRequired[DedicatedTenancyModificationStateEnumType],
        "DedicatedTenancySupport": NotRequired[DedicatedTenancySupportResultEnumType],
        "DedicatedTenancyManagementCidrRange": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

AssociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "AssociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
        "ResourceId": str,
    },
)

AssociateConnectionAliasResultTypeDef = TypedDict(
    "AssociateConnectionAliasResultTypeDef",
    {
        "ConnectionIdentifier": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIpGroupsRequestRequestTypeDef = TypedDict(
    "AssociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": Sequence[str],
    },
)

AuthorizeIpRulesRequestRequestTypeDef = TypedDict(
    "AuthorizeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence["IpRuleItemTypeDef"],
    },
)

ClientPropertiesResultTypeDef = TypedDict(
    "ClientPropertiesResultTypeDef",
    {
        "ResourceId": NotRequired[str],
        "ClientProperties": NotRequired["ClientPropertiesTypeDef"],
    },
)

ClientPropertiesTypeDef = TypedDict(
    "ClientPropertiesTypeDef",
    {
        "ReconnectEnabled": NotRequired[ReconnectEnumType],
    },
)

ComputeTypeTypeDef = TypedDict(
    "ComputeTypeTypeDef",
    {
        "Name": NotRequired[ComputeType],
    },
)

ConnectClientAddInTypeDef = TypedDict(
    "ConnectClientAddInTypeDef",
    {
        "AddInId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "Name": NotRequired[str],
        "URL": NotRequired[str],
    },
)

ConnectionAliasAssociationTypeDef = TypedDict(
    "ConnectionAliasAssociationTypeDef",
    {
        "AssociationStatus": NotRequired[AssociationStatusType],
        "AssociatedAccountId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ConnectionIdentifier": NotRequired[str],
    },
)

ConnectionAliasPermissionTypeDef = TypedDict(
    "ConnectionAliasPermissionTypeDef",
    {
        "SharedAccountId": str,
        "AllowAssociation": bool,
    },
)

ConnectionAliasTypeDef = TypedDict(
    "ConnectionAliasTypeDef",
    {
        "ConnectionString": NotRequired[str],
        "AliasId": NotRequired[str],
        "State": NotRequired[ConnectionAliasStateType],
        "OwnerAccountId": NotRequired[str],
        "Associations": NotRequired[List["ConnectionAliasAssociationTypeDef"]],
    },
)

CopyWorkspaceImageRequestRequestTypeDef = TypedDict(
    "CopyWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CopyWorkspaceImageResultTypeDef = TypedDict(
    "CopyWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "CreateConnectClientAddInRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Name": str,
        "URL": str,
    },
)

CreateConnectClientAddInResultTypeDef = TypedDict(
    "CreateConnectClientAddInResultTypeDef",
    {
        "AddInId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionAliasRequestRequestTypeDef = TypedDict(
    "CreateConnectionAliasRequestRequestTypeDef",
    {
        "ConnectionString": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateConnectionAliasResultTypeDef = TypedDict(
    "CreateConnectionAliasResultTypeDef",
    {
        "AliasId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpGroupRequestRequestTypeDef = TypedDict(
    "CreateIpGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "GroupDesc": NotRequired[str],
        "UserRules": NotRequired[Sequence["IpRuleItemTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateIpGroupResultTypeDef = TypedDict(
    "CreateIpGroupResultTypeDef",
    {
        "GroupId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTagsRequestRequestTypeDef = TypedDict(
    "CreateTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

CreateUpdatedWorkspaceImageRequestRequestTypeDef = TypedDict(
    "CreateUpdatedWorkspaceImageRequestRequestTypeDef",
    {
        "Name": str,
        "Description": str,
        "SourceImageId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUpdatedWorkspaceImageResultTypeDef = TypedDict(
    "CreateUpdatedWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleName": str,
        "BundleDescription": str,
        "ImageId": str,
        "ComputeType": "ComputeTypeTypeDef",
        "UserStorage": "UserStorageTypeDef",
        "RootStorage": NotRequired["RootStorageTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWorkspaceBundleResultTypeDef = TypedDict(
    "CreateWorkspaceBundleResultTypeDef",
    {
        "WorkspaceBundle": "WorkspaceBundleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspacesRequestRequestTypeDef = TypedDict(
    "CreateWorkspacesRequestRequestTypeDef",
    {
        "Workspaces": Sequence["WorkspaceRequestTypeDef"],
    },
)

CreateWorkspacesResultTypeDef = TypedDict(
    "CreateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedCreateWorkspaceRequestTypeDef"],
        "PendingRequests": List["WorkspaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefaultWorkspaceCreationPropertiesTypeDef = TypedDict(
    "DefaultWorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": NotRequired[bool],
        "EnableInternetAccess": NotRequired[bool],
        "DefaultOu": NotRequired[str],
        "CustomSecurityGroupId": NotRequired[str],
        "UserEnabledAsLocalAdministrator": NotRequired[bool],
        "EnableMaintenanceMode": NotRequired[bool],
    },
)

DeleteConnectClientAddInRequestRequestTypeDef = TypedDict(
    "DeleteConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
    },
)

DeleteConnectionAliasRequestRequestTypeDef = TypedDict(
    "DeleteConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)

DeleteIpGroupRequestRequestTypeDef = TypedDict(
    "DeleteIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)

DeleteTagsRequestRequestTypeDef = TypedDict(
    "DeleteTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "TagKeys": Sequence[str],
    },
)

DeleteWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": NotRequired[str],
    },
)

DeleteWorkspaceImageRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)

DeregisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "DeregisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
    },
)

DescribeAccountModificationsRequestRequestTypeDef = TypedDict(
    "DescribeAccountModificationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)

DescribeAccountModificationsResultTypeDef = TypedDict(
    "DescribeAccountModificationsResultTypeDef",
    {
        "AccountModifications": List["AccountModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountResultTypeDef = TypedDict(
    "DescribeAccountResultTypeDef",
    {
        "DedicatedTenancySupport": DedicatedTenancySupportResultEnumType,
        "DedicatedTenancyManagementCidrRange": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientPropertiesRequestRequestTypeDef = TypedDict(
    "DescribeClientPropertiesRequestRequestTypeDef",
    {
        "ResourceIds": Sequence[str],
    },
)

DescribeClientPropertiesResultTypeDef = TypedDict(
    "DescribeClientPropertiesResultTypeDef",
    {
        "ClientPropertiesList": List["ClientPropertiesResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectClientAddInsRequestRequestTypeDef = TypedDict(
    "DescribeConnectClientAddInsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeConnectClientAddInsResultTypeDef = TypedDict(
    "DescribeConnectClientAddInsResultTypeDef",
    {
        "AddIns": List["ConnectClientAddInTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionAliasPermissionsRequestRequestTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsRequestRequestTypeDef",
    {
        "AliasId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeConnectionAliasPermissionsResultTypeDef = TypedDict(
    "DescribeConnectionAliasPermissionsResultTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermissions": List["ConnectionAliasPermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConnectionAliasesRequestRequestTypeDef = TypedDict(
    "DescribeConnectionAliasesRequestRequestTypeDef",
    {
        "AliasIds": NotRequired[Sequence[str]],
        "ResourceId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeConnectionAliasesResultTypeDef = TypedDict(
    "DescribeConnectionAliasesResultTypeDef",
    {
        "ConnectionAliases": List["ConnectionAliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpGroupsRequestRequestTypeDef = TypedDict(
    "DescribeIpGroupsRequestRequestTypeDef",
    {
        "GroupIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeIpGroupsResultTypeDef = TypedDict(
    "DescribeIpGroupsResultTypeDef",
    {
        "Result": List["WorkspacesIpGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "ResourceId": str,
    },
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceBundlesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceBundlesRequestRequestTypeDef",
    {
        "BundleIds": NotRequired[Sequence[str]],
        "Owner": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

DescribeWorkspaceBundlesResultTypeDef = TypedDict(
    "DescribeWorkspaceBundlesResultTypeDef",
    {
        "Bundles": List["WorkspaceBundleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceDirectoriesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesRequestRequestTypeDef",
    {
        "DirectoryIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeWorkspaceDirectoriesResultTypeDef = TypedDict(
    "DescribeWorkspaceDirectoriesResultTypeDef",
    {
        "Directories": List["WorkspaceDirectoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceImagePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsRequestRequestTypeDef",
    {
        "ImageId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeWorkspaceImagePermissionsResultTypeDef = TypedDict(
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    {
        "ImageId": str,
        "ImagePermissions": List["ImagePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceImagesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceImagesRequestRequestTypeDef",
    {
        "ImageIds": NotRequired[Sequence[str]],
        "ImageType": NotRequired[ImageTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

DescribeWorkspaceImagesResultTypeDef = TypedDict(
    "DescribeWorkspaceImagesResultTypeDef",
    {
        "Images": List["WorkspaceImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspaceSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

DescribeWorkspaceSnapshotsResultTypeDef = TypedDict(
    "DescribeWorkspaceSnapshotsResultTypeDef",
    {
        "RebuildSnapshots": List["SnapshotTypeDef"],
        "RestoreSnapshots": List["SnapshotTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesConnectionStatusRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusRequestRequestTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
    },
)

DescribeWorkspacesConnectionStatusResultTypeDef = TypedDict(
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    {
        "WorkspacesConnectionStatus": List["WorkspaceConnectionStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkspacesRequestRequestTypeDef = TypedDict(
    "DescribeWorkspacesRequestRequestTypeDef",
    {
        "WorkspaceIds": NotRequired[Sequence[str]],
        "DirectoryId": NotRequired[str],
        "UserName": NotRequired[str],
        "BundleId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeWorkspacesResultTypeDef = TypedDict(
    "DescribeWorkspacesResultTypeDef",
    {
        "Workspaces": List["WorkspaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateConnectionAliasRequestRequestTypeDef = TypedDict(
    "DisassociateConnectionAliasRequestRequestTypeDef",
    {
        "AliasId": str,
    },
)

DisassociateIpGroupsRequestRequestTypeDef = TypedDict(
    "DisassociateIpGroupsRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "GroupIds": Sequence[str],
    },
)

FailedCreateWorkspaceRequestTypeDef = TypedDict(
    "FailedCreateWorkspaceRequestTypeDef",
    {
        "WorkspaceRequest": NotRequired["WorkspaceRequestTypeDef"],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

FailedWorkspaceChangeRequestTypeDef = TypedDict(
    "FailedWorkspaceChangeRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

ImagePermissionTypeDef = TypedDict(
    "ImagePermissionTypeDef",
    {
        "SharedAccountId": NotRequired[str],
    },
)

ImportWorkspaceImageRequestRequestTypeDef = TypedDict(
    "ImportWorkspaceImageRequestRequestTypeDef",
    {
        "Ec2ImageId": str,
        "IngestionProcess": WorkspaceImageIngestionProcessType,
        "ImageName": str,
        "ImageDescription": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "Applications": NotRequired[Sequence[ApplicationType]],
    },
)

ImportWorkspaceImageResultTypeDef = TypedDict(
    "ImportWorkspaceImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IpRuleItemTypeDef = TypedDict(
    "IpRuleItemTypeDef",
    {
        "ipRule": NotRequired[str],
        "ruleDesc": NotRequired[str],
    },
)

ListAvailableManagementCidrRangesRequestRequestTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesRequestRequestTypeDef",
    {
        "ManagementCidrRangeConstraint": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAvailableManagementCidrRangesResultTypeDef = TypedDict(
    "ListAvailableManagementCidrRangesResultTypeDef",
    {
        "ManagementCidrRanges": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrateWorkspaceRequestRequestTypeDef = TypedDict(
    "MigrateWorkspaceRequestRequestTypeDef",
    {
        "SourceWorkspaceId": str,
        "BundleId": str,
    },
)

MigrateWorkspaceResultTypeDef = TypedDict(
    "MigrateWorkspaceResultTypeDef",
    {
        "SourceWorkspaceId": str,
        "TargetWorkspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModificationStateTypeDef = TypedDict(
    "ModificationStateTypeDef",
    {
        "Resource": NotRequired[ModificationResourceEnumType],
        "State": NotRequired[ModificationStateEnumType],
    },
)

ModifyAccountRequestRequestTypeDef = TypedDict(
    "ModifyAccountRequestRequestTypeDef",
    {
        "DedicatedTenancySupport": NotRequired[Literal["ENABLED"]],
        "DedicatedTenancyManagementCidrRange": NotRequired[str],
    },
)

ModifyClientPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyClientPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ClientProperties": "ClientPropertiesTypeDef",
    },
)

ModifySelfservicePermissionsRequestRequestTypeDef = TypedDict(
    "ModifySelfservicePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "SelfservicePermissions": "SelfservicePermissionsTypeDef",
    },
)

ModifyWorkspaceAccessPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceAccessPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceAccessProperties": "WorkspaceAccessPropertiesTypeDef",
    },
)

ModifyWorkspaceCreationPropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceCreationPropertiesRequestRequestTypeDef",
    {
        "ResourceId": str,
        "WorkspaceCreationProperties": "WorkspaceCreationPropertiesTypeDef",
    },
)

ModifyWorkspacePropertiesRequestRequestTypeDef = TypedDict(
    "ModifyWorkspacePropertiesRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceProperties": "WorkspacePropertiesTypeDef",
    },
)

ModifyWorkspaceStateRequestRequestTypeDef = TypedDict(
    "ModifyWorkspaceStateRequestRequestTypeDef",
    {
        "WorkspaceId": str,
        "WorkspaceState": TargetWorkspaceStateType,
    },
)

OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Type": NotRequired[OperatingSystemTypeType],
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

RebootRequestTypeDef = TypedDict(
    "RebootRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebootWorkspacesRequestRequestTypeDef = TypedDict(
    "RebootWorkspacesRequestRequestTypeDef",
    {
        "RebootWorkspaceRequests": Sequence["RebootRequestTypeDef"],
    },
)

RebootWorkspacesResultTypeDef = TypedDict(
    "RebootWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RebuildRequestTypeDef = TypedDict(
    "RebuildRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RebuildWorkspacesRequestRequestTypeDef = TypedDict(
    "RebuildWorkspacesRequestRequestTypeDef",
    {
        "RebuildWorkspaceRequests": Sequence["RebuildRequestTypeDef"],
    },
)

RebuildWorkspacesResultTypeDef = TypedDict(
    "RebuildWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterWorkspaceDirectoryRequestRequestTypeDef = TypedDict(
    "RegisterWorkspaceDirectoryRequestRequestTypeDef",
    {
        "DirectoryId": str,
        "EnableWorkDocs": bool,
        "SubnetIds": NotRequired[Sequence[str]],
        "EnableSelfService": NotRequired[bool],
        "Tenancy": NotRequired[TenancyType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
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

RestoreWorkspaceRequestRequestTypeDef = TypedDict(
    "RestoreWorkspaceRequestRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

RevokeIpRulesRequestRequestTypeDef = TypedDict(
    "RevokeIpRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence[str],
    },
)

RootStorageTypeDef = TypedDict(
    "RootStorageTypeDef",
    {
        "Capacity": NotRequired[str],
    },
)

SelfservicePermissionsTypeDef = TypedDict(
    "SelfservicePermissionsTypeDef",
    {
        "RestartWorkspace": NotRequired[ReconnectEnumType],
        "IncreaseVolumeSize": NotRequired[ReconnectEnumType],
        "ChangeComputeType": NotRequired[ReconnectEnumType],
        "SwitchRunningMode": NotRequired[ReconnectEnumType],
        "RebuildWorkspace": NotRequired[ReconnectEnumType],
    },
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "SnapshotTime": NotRequired[datetime],
    },
)

StartRequestTypeDef = TypedDict(
    "StartRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
    },
)

StartWorkspacesRequestRequestTypeDef = TypedDict(
    "StartWorkspacesRequestRequestTypeDef",
    {
        "StartWorkspaceRequests": Sequence["StartRequestTypeDef"],
    },
)

StartWorkspacesResultTypeDef = TypedDict(
    "StartWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopRequestTypeDef = TypedDict(
    "StopRequestTypeDef",
    {
        "WorkspaceId": NotRequired[str],
    },
)

StopWorkspacesRequestRequestTypeDef = TypedDict(
    "StopWorkspacesRequestRequestTypeDef",
    {
        "StopWorkspaceRequests": Sequence["StopRequestTypeDef"],
    },
)

StopWorkspacesResultTypeDef = TypedDict(
    "StopWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)

TerminateRequestTypeDef = TypedDict(
    "TerminateRequestTypeDef",
    {
        "WorkspaceId": str,
    },
)

TerminateWorkspacesRequestRequestTypeDef = TypedDict(
    "TerminateWorkspacesRequestRequestTypeDef",
    {
        "TerminateWorkspaceRequests": Sequence["TerminateRequestTypeDef"],
    },
)

TerminateWorkspacesResultTypeDef = TypedDict(
    "TerminateWorkspacesResultTypeDef",
    {
        "FailedRequests": List["FailedWorkspaceChangeRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectClientAddInRequestRequestTypeDef = TypedDict(
    "UpdateConnectClientAddInRequestRequestTypeDef",
    {
        "AddInId": str,
        "ResourceId": str,
        "Name": NotRequired[str],
        "URL": NotRequired[str],
    },
)

UpdateConnectionAliasPermissionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionAliasPermissionRequestRequestTypeDef",
    {
        "AliasId": str,
        "ConnectionAliasPermission": "ConnectionAliasPermissionTypeDef",
    },
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "UpdateAvailable": NotRequired[bool],
        "Description": NotRequired[str],
    },
)

UpdateRulesOfIpGroupRequestRequestTypeDef = TypedDict(
    "UpdateRulesOfIpGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "UserRules": Sequence["IpRuleItemTypeDef"],
    },
)

UpdateWorkspaceBundleRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceBundleRequestRequestTypeDef",
    {
        "BundleId": NotRequired[str],
        "ImageId": NotRequired[str],
    },
)

UpdateWorkspaceImagePermissionRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceImagePermissionRequestRequestTypeDef",
    {
        "ImageId": str,
        "AllowCopyImage": bool,
        "SharedAccountId": str,
    },
)

UserStorageTypeDef = TypedDict(
    "UserStorageTypeDef",
    {
        "Capacity": NotRequired[str],
    },
)

WorkspaceAccessPropertiesTypeDef = TypedDict(
    "WorkspaceAccessPropertiesTypeDef",
    {
        "DeviceTypeWindows": NotRequired[AccessPropertyValueType],
        "DeviceTypeOsx": NotRequired[AccessPropertyValueType],
        "DeviceTypeWeb": NotRequired[AccessPropertyValueType],
        "DeviceTypeIos": NotRequired[AccessPropertyValueType],
        "DeviceTypeAndroid": NotRequired[AccessPropertyValueType],
        "DeviceTypeChromeOs": NotRequired[AccessPropertyValueType],
        "DeviceTypeZeroClient": NotRequired[AccessPropertyValueType],
        "DeviceTypeLinux": NotRequired[AccessPropertyValueType],
    },
)

WorkspaceBundleTypeDef = TypedDict(
    "WorkspaceBundleTypeDef",
    {
        "BundleId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "Description": NotRequired[str],
        "ImageId": NotRequired[str],
        "RootStorage": NotRequired["RootStorageTypeDef"],
        "UserStorage": NotRequired["UserStorageTypeDef"],
        "ComputeType": NotRequired["ComputeTypeTypeDef"],
        "LastUpdatedTime": NotRequired[datetime],
        "CreationTime": NotRequired[datetime],
    },
)

WorkspaceConnectionStatusTypeDef = TypedDict(
    "WorkspaceConnectionStatusTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "ConnectionState": NotRequired[ConnectionStateType],
        "ConnectionStateCheckTimestamp": NotRequired[datetime],
        "LastKnownUserConnectionTimestamp": NotRequired[datetime],
    },
)

WorkspaceCreationPropertiesTypeDef = TypedDict(
    "WorkspaceCreationPropertiesTypeDef",
    {
        "EnableWorkDocs": NotRequired[bool],
        "EnableInternetAccess": NotRequired[bool],
        "DefaultOu": NotRequired[str],
        "CustomSecurityGroupId": NotRequired[str],
        "UserEnabledAsLocalAdministrator": NotRequired[bool],
        "EnableMaintenanceMode": NotRequired[bool],
    },
)

WorkspaceDirectoryTypeDef = TypedDict(
    "WorkspaceDirectoryTypeDef",
    {
        "DirectoryId": NotRequired[str],
        "Alias": NotRequired[str],
        "DirectoryName": NotRequired[str],
        "RegistrationCode": NotRequired[str],
        "SubnetIds": NotRequired[List[str]],
        "DnsIpAddresses": NotRequired[List[str]],
        "CustomerUserName": NotRequired[str],
        "IamRoleId": NotRequired[str],
        "DirectoryType": NotRequired[WorkspaceDirectoryTypeType],
        "WorkspaceSecurityGroupId": NotRequired[str],
        "State": NotRequired[WorkspaceDirectoryStateType],
        "WorkspaceCreationProperties": NotRequired["DefaultWorkspaceCreationPropertiesTypeDef"],
        "ipGroupIds": NotRequired[List[str]],
        "WorkspaceAccessProperties": NotRequired["WorkspaceAccessPropertiesTypeDef"],
        "Tenancy": NotRequired[TenancyType],
        "SelfservicePermissions": NotRequired["SelfservicePermissionsTypeDef"],
    },
)

WorkspaceImageTypeDef = TypedDict(
    "WorkspaceImageTypeDef",
    {
        "ImageId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "OperatingSystem": NotRequired["OperatingSystemTypeDef"],
        "State": NotRequired[WorkspaceImageStateType],
        "RequiredTenancy": NotRequired[WorkspaceImageRequiredTenancyType],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "Created": NotRequired[datetime],
        "OwnerAccountId": NotRequired[str],
        "Updates": NotRequired["UpdateResultTypeDef"],
    },
)

WorkspacePropertiesTypeDef = TypedDict(
    "WorkspacePropertiesTypeDef",
    {
        "RunningMode": NotRequired[RunningModeType],
        "RunningModeAutoStopTimeoutInMinutes": NotRequired[int],
        "RootVolumeSizeGib": NotRequired[int],
        "UserVolumeSizeGib": NotRequired[int],
        "ComputeTypeName": NotRequired[ComputeType],
    },
)

WorkspaceRequestTypeDef = TypedDict(
    "WorkspaceRequestTypeDef",
    {
        "DirectoryId": str,
        "UserName": str,
        "BundleId": str,
        "VolumeEncryptionKey": NotRequired[str],
        "UserVolumeEncryptionEnabled": NotRequired[bool],
        "RootVolumeEncryptionEnabled": NotRequired[bool],
        "WorkspaceProperties": NotRequired["WorkspacePropertiesTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

WorkspaceTypeDef = TypedDict(
    "WorkspaceTypeDef",
    {
        "WorkspaceId": NotRequired[str],
        "DirectoryId": NotRequired[str],
        "UserName": NotRequired[str],
        "IpAddress": NotRequired[str],
        "State": NotRequired[WorkspaceStateType],
        "BundleId": NotRequired[str],
        "SubnetId": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ComputerName": NotRequired[str],
        "VolumeEncryptionKey": NotRequired[str],
        "UserVolumeEncryptionEnabled": NotRequired[bool],
        "RootVolumeEncryptionEnabled": NotRequired[bool],
        "WorkspaceProperties": NotRequired["WorkspacePropertiesTypeDef"],
        "ModificationStates": NotRequired[List["ModificationStateTypeDef"]],
    },
)

WorkspacesIpGroupTypeDef = TypedDict(
    "WorkspacesIpGroupTypeDef",
    {
        "groupId": NotRequired[str],
        "groupName": NotRequired[str],
        "groupDesc": NotRequired[str],
        "userRules": NotRequired[List["IpRuleItemTypeDef"]],
    },
)
