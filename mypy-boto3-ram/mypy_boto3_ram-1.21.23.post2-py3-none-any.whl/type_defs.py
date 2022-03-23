"""
Type annotations for ram service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ram/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ram.type_defs import AcceptResourceShareInvitationRequestRequestTypeDef

    data: AcceptResourceShareInvitationRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ResourceOwnerType,
    ResourceRegionScopeFilterType,
    ResourceRegionScopeType,
    ResourceShareAssociationStatusType,
    ResourceShareAssociationTypeType,
    ResourceShareFeatureSetType,
    ResourceShareInvitationStatusType,
    ResourceShareStatusType,
    ResourceStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptResourceShareInvitationRequestRequestTypeDef",
    "AcceptResourceShareInvitationResponseTypeDef",
    "AssociateResourceSharePermissionRequestRequestTypeDef",
    "AssociateResourceSharePermissionResponseTypeDef",
    "AssociateResourceShareRequestRequestTypeDef",
    "AssociateResourceShareResponseTypeDef",
    "CreateResourceShareRequestRequestTypeDef",
    "CreateResourceShareResponseTypeDef",
    "DeleteResourceShareRequestRequestTypeDef",
    "DeleteResourceShareResponseTypeDef",
    "DisassociateResourceSharePermissionRequestRequestTypeDef",
    "DisassociateResourceSharePermissionResponseTypeDef",
    "DisassociateResourceShareRequestRequestTypeDef",
    "DisassociateResourceShareResponseTypeDef",
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    "GetPermissionRequestRequestTypeDef",
    "GetPermissionResponseTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourceShareAssociationsRequestRequestTypeDef",
    "GetResourceShareAssociationsResponseTypeDef",
    "GetResourceShareInvitationsRequestRequestTypeDef",
    "GetResourceShareInvitationsResponseTypeDef",
    "GetResourceSharesRequestRequestTypeDef",
    "GetResourceSharesResponseTypeDef",
    "ListPendingInvitationResourcesRequestRequestTypeDef",
    "ListPendingInvitationResourcesResponseTypeDef",
    "ListPermissionVersionsRequestRequestTypeDef",
    "ListPermissionVersionsResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListPrincipalsRequestRequestTypeDef",
    "ListPrincipalsResponseTypeDef",
    "ListResourceSharePermissionsRequestRequestTypeDef",
    "ListResourceSharePermissionsResponseTypeDef",
    "ListResourceTypesRequestRequestTypeDef",
    "ListResourceTypesResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PrincipalTypeDef",
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    "RejectResourceShareInvitationRequestRequestTypeDef",
    "RejectResourceShareInvitationResponseTypeDef",
    "ResourceShareAssociationTypeDef",
    "ResourceShareInvitationTypeDef",
    "ResourceSharePermissionDetailTypeDef",
    "ResourceSharePermissionSummaryTypeDef",
    "ResourceShareTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "ServiceNameAndResourceTypeTypeDef",
    "TagFilterTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateResourceShareRequestRequestTypeDef",
    "UpdateResourceShareResponseTypeDef",
)

AcceptResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "AcceptResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "clientToken": NotRequired[str],
    },
)

AcceptResourceShareInvitationResponseTypeDef = TypedDict(
    "AcceptResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "AssociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
        "replace": NotRequired[bool],
        "clientToken": NotRequired[str],
        "permissionVersion": NotRequired[int],
    },
)

AssociateResourceSharePermissionResponseTypeDef = TypedDict(
    "AssociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceShareRequestRequestTypeDef = TypedDict(
    "AssociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)

AssociateResourceShareResponseTypeDef = TypedDict(
    "AssociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateResourceShareRequestRequestTypeDef = TypedDict(
    "CreateResourceShareRequestRequestTypeDef",
    {
        "name": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "allowExternalPrincipals": NotRequired[bool],
        "clientToken": NotRequired[str],
        "permissionArns": NotRequired[Sequence[str]],
    },
)

CreateResourceShareResponseTypeDef = TypedDict(
    "CreateResourceShareResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourceShareRequestRequestTypeDef = TypedDict(
    "DeleteResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "clientToken": NotRequired[str],
    },
)

DeleteResourceShareResponseTypeDef = TypedDict(
    "DeleteResourceShareResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceSharePermissionRequestRequestTypeDef = TypedDict(
    "DisassociateResourceSharePermissionRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "permissionArn": str,
        "clientToken": NotRequired[str],
    },
)

DisassociateResourceSharePermissionResponseTypeDef = TypedDict(
    "DisassociateResourceSharePermissionResponseTypeDef",
    {
        "returnValue": bool,
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceShareRequestRequestTypeDef = TypedDict(
    "DisassociateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "resourceArns": NotRequired[Sequence[str]],
        "principals": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)

DisassociateResourceShareResponseTypeDef = TypedDict(
    "DisassociateResourceShareResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSharingWithAwsOrganizationResponseTypeDef = TypedDict(
    "EnableSharingWithAwsOrganizationResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPermissionRequestRequestTypeDef = TypedDict(
    "GetPermissionRequestRequestTypeDef",
    {
        "permissionArn": str,
        "permissionVersion": NotRequired[int],
    },
)

GetPermissionResponseTypeDef = TypedDict(
    "GetPermissionResponseTypeDef",
    {
        "permission": "ResourceSharePermissionDetailTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "resourceArns": Sequence[str],
        "principal": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "policies": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceShareAssociationsRequestRequestTypeDef = TypedDict(
    "GetResourceShareAssociationsRequestRequestTypeDef",
    {
        "associationType": ResourceShareAssociationTypeType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceArn": NotRequired[str],
        "principal": NotRequired[str],
        "associationStatus": NotRequired[ResourceShareAssociationStatusType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetResourceShareAssociationsResponseTypeDef = TypedDict(
    "GetResourceShareAssociationsResponseTypeDef",
    {
        "resourceShareAssociations": List["ResourceShareAssociationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceShareInvitationsRequestRequestTypeDef = TypedDict(
    "GetResourceShareInvitationsRequestRequestTypeDef",
    {
        "resourceShareInvitationArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetResourceShareInvitationsResponseTypeDef = TypedDict(
    "GetResourceShareInvitationsResponseTypeDef",
    {
        "resourceShareInvitations": List["ResourceShareInvitationTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceSharesRequestRequestTypeDef = TypedDict(
    "GetResourceSharesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceShareArns": NotRequired[Sequence[str]],
        "resourceShareStatus": NotRequired[ResourceShareStatusType],
        "name": NotRequired[str],
        "tagFilters": NotRequired[Sequence["TagFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "permissionArn": NotRequired[str],
    },
)

GetResourceSharesResponseTypeDef = TypedDict(
    "GetResourceSharesResponseTypeDef",
    {
        "resourceShares": List["ResourceShareTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPendingInvitationResourcesRequestRequestTypeDef = TypedDict(
    "ListPendingInvitationResourcesRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)

ListPendingInvitationResourcesResponseTypeDef = TypedDict(
    "ListPendingInvitationResourcesResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionVersionsRequestRequestTypeDef = TypedDict(
    "ListPermissionVersionsRequestRequestTypeDef",
    {
        "permissionArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPermissionVersionsResponseTypeDef = TypedDict(
    "ListPermissionVersionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "resourceType": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPrincipalsRequestRequestTypeDef = TypedDict(
    "ListPrincipalsRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "resourceArn": NotRequired[str],
        "principals": NotRequired[Sequence[str]],
        "resourceType": NotRequired[str],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPrincipalsResponseTypeDef = TypedDict(
    "ListPrincipalsResponseTypeDef",
    {
        "principals": List["PrincipalTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceSharePermissionsRequestRequestTypeDef = TypedDict(
    "ListResourceSharePermissionsRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListResourceSharePermissionsResponseTypeDef = TypedDict(
    "ListResourceSharePermissionsResponseTypeDef",
    {
        "permissions": List["ResourceSharePermissionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourceTypesRequestRequestTypeDef = TypedDict(
    "ListResourceTypesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)

ListResourceTypesResponseTypeDef = TypedDict(
    "ListResourceTypesResponseTypeDef",
    {
        "resourceTypes": List["ServiceNameAndResourceTypeTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "resourceOwner": ResourceOwnerType,
        "principal": NotRequired[str],
        "resourceType": NotRequired[str],
        "resourceArns": NotRequired[Sequence[str]],
        "resourceShareArns": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "resourceRegionScope": NotRequired[ResourceRegionScopeFilterType],
    },
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
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

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "id": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "external": NotRequired[bool],
    },
)

PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyRequestRequestTypeDef",
    {
        "resourceShareArn": str,
    },
)

PromoteResourceShareCreatedFromPolicyResponseTypeDef = TypedDict(
    "PromoteResourceShareCreatedFromPolicyResponseTypeDef",
    {
        "returnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectResourceShareInvitationRequestRequestTypeDef = TypedDict(
    "RejectResourceShareInvitationRequestRequestTypeDef",
    {
        "resourceShareInvitationArn": str,
        "clientToken": NotRequired[str],
    },
)

RejectResourceShareInvitationResponseTypeDef = TypedDict(
    "RejectResourceShareInvitationResponseTypeDef",
    {
        "resourceShareInvitation": "ResourceShareInvitationTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceShareAssociationTypeDef = TypedDict(
    "ResourceShareAssociationTypeDef",
    {
        "resourceShareArn": NotRequired[str],
        "resourceShareName": NotRequired[str],
        "associatedEntity": NotRequired[str],
        "associationType": NotRequired[ResourceShareAssociationTypeType],
        "status": NotRequired[ResourceShareAssociationStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "external": NotRequired[bool],
    },
)

ResourceShareInvitationTypeDef = TypedDict(
    "ResourceShareInvitationTypeDef",
    {
        "resourceShareInvitationArn": NotRequired[str],
        "resourceShareName": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "senderAccountId": NotRequired[str],
        "receiverAccountId": NotRequired[str],
        "invitationTimestamp": NotRequired[datetime],
        "status": NotRequired[ResourceShareInvitationStatusType],
        "resourceShareAssociations": NotRequired[List["ResourceShareAssociationTypeDef"]],
        "receiverArn": NotRequired[str],
    },
)

ResourceSharePermissionDetailTypeDef = TypedDict(
    "ResourceSharePermissionDetailTypeDef",
    {
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "defaultVersion": NotRequired[bool],
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
        "permission": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "isResourceTypeDefault": NotRequired[bool],
    },
)

ResourceSharePermissionSummaryTypeDef = TypedDict(
    "ResourceSharePermissionSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "version": NotRequired[str],
        "defaultVersion": NotRequired[bool],
        "name": NotRequired[str],
        "resourceType": NotRequired[str],
        "status": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "isResourceTypeDefault": NotRequired[bool],
    },
)

ResourceShareTypeDef = TypedDict(
    "ResourceShareTypeDef",
    {
        "resourceShareArn": NotRequired[str],
        "name": NotRequired[str],
        "owningAccountId": NotRequired[str],
        "allowExternalPrincipals": NotRequired[bool],
        "status": NotRequired[ResourceShareStatusType],
        "statusMessage": NotRequired[str],
        "tags": NotRequired[List["TagTypeDef"]],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "featureSet": NotRequired[ResourceShareFeatureSetType],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "arn": NotRequired[str],
        "type": NotRequired[str],
        "resourceShareArn": NotRequired[str],
        "resourceGroupArn": NotRequired[str],
        "status": NotRequired[ResourceStatusType],
        "statusMessage": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdatedTime": NotRequired[datetime],
        "resourceRegionScope": NotRequired[ResourceRegionScopeType],
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

ServiceNameAndResourceTypeTypeDef = TypedDict(
    "ServiceNameAndResourceTypeTypeDef",
    {
        "resourceType": NotRequired[str],
        "serviceName": NotRequired[str],
        "resourceRegionScope": NotRequired[ResourceRegionScopeType],
    },
)

TagFilterTypeDef = TypedDict(
    "TagFilterTypeDef",
    {
        "tagKey": NotRequired[str],
        "tagValues": NotRequired[Sequence[str]],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateResourceShareRequestRequestTypeDef = TypedDict(
    "UpdateResourceShareRequestRequestTypeDef",
    {
        "resourceShareArn": str,
        "name": NotRequired[str],
        "allowExternalPrincipals": NotRequired[bool],
        "clientToken": NotRequired[str],
    },
)

UpdateResourceShareResponseTypeDef = TypedDict(
    "UpdateResourceShareResponseTypeDef",
    {
        "resourceShare": "ResourceShareTypeDef",
        "clientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
