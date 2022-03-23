"""
Type annotations for workdocs service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workdocs/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_workdocs.type_defs import AbortDocumentVersionUploadRequestRequestTypeDef

    data: AbortDocumentVersionUploadRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ActivityTypeType,
    BooleanEnumTypeType,
    CommentStatusTypeType,
    CommentVisibilityTypeType,
    DocumentSourceTypeType,
    DocumentStatusTypeType,
    DocumentThumbnailTypeType,
    FolderContentTypeType,
    LocaleTypeType,
    OrderTypeType,
    PrincipalTypeType,
    ResourceSortTypeType,
    ResourceStateTypeType,
    ResourceTypeType,
    RolePermissionTypeType,
    RoleTypeType,
    ShareStatusTypeType,
    StorageTypeType,
    UserFilterTypeType,
    UserSortTypeType,
    UserStatusTypeType,
    UserTypeType,
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
    "AbortDocumentVersionUploadRequestRequestTypeDef",
    "ActivateUserRequestRequestTypeDef",
    "ActivateUserResponseTypeDef",
    "ActivityTypeDef",
    "AddResourcePermissionsRequestRequestTypeDef",
    "AddResourcePermissionsResponseTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "CreateCommentRequestRequestTypeDef",
    "CreateCommentResponseTypeDef",
    "CreateCustomMetadataRequestRequestTypeDef",
    "CreateFolderRequestRequestTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateLabelsRequestRequestTypeDef",
    "CreateNotificationSubscriptionRequestRequestTypeDef",
    "CreateNotificationSubscriptionResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeactivateUserRequestRequestTypeDef",
    "DeleteCommentRequestRequestTypeDef",
    "DeleteCustomMetadataRequestRequestTypeDef",
    "DeleteDocumentRequestRequestTypeDef",
    "DeleteFolderContentsRequestRequestTypeDef",
    "DeleteFolderRequestRequestTypeDef",
    "DeleteLabelsRequestRequestTypeDef",
    "DeleteNotificationSubscriptionRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DescribeActivitiesRequestRequestTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "DescribeCommentsRequestRequestTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DescribeDocumentVersionsRequestRequestTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DescribeFolderContentsRequestRequestTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "DescribeGroupsRequestRequestTypeDef",
    "DescribeGroupsResponseTypeDef",
    "DescribeNotificationSubscriptionsRequestRequestTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "DescribeResourcePermissionsRequestRequestTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "DescribeRootFoldersRequestRequestTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "DescribeUsersRequestRequestTypeDef",
    "DescribeUsersResponseTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentVersionMetadataTypeDef",
    "FolderMetadataTypeDef",
    "GetCurrentUserRequestRequestTypeDef",
    "GetCurrentUserResponseTypeDef",
    "GetDocumentPathRequestRequestTypeDef",
    "GetDocumentPathResponseTypeDef",
    "GetDocumentRequestRequestTypeDef",
    "GetDocumentResponseTypeDef",
    "GetDocumentVersionRequestRequestTypeDef",
    "GetDocumentVersionResponseTypeDef",
    "GetFolderPathRequestRequestTypeDef",
    "GetFolderPathResponseTypeDef",
    "GetFolderRequestRequestTypeDef",
    "GetFolderResponseTypeDef",
    "GetResourcesRequestRequestTypeDef",
    "GetResourcesResponseTypeDef",
    "GroupMetadataTypeDef",
    "InitiateDocumentVersionUploadRequestRequestTypeDef",
    "InitiateDocumentVersionUploadResponseTypeDef",
    "NotificationOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantsTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "RemoveAllResourcePermissionsRequestRequestTypeDef",
    "RemoveResourcePermissionRequestRequestTypeDef",
    "ResourceMetadataTypeDef",
    "ResourcePathComponentTypeDef",
    "ResourcePathTypeDef",
    "ResponseMetadataTypeDef",
    "SharePrincipalTypeDef",
    "ShareResultTypeDef",
    "StorageRuleTypeTypeDef",
    "SubscriptionTypeDef",
    "UpdateDocumentRequestRequestTypeDef",
    "UpdateDocumentVersionRequestRequestTypeDef",
    "UpdateFolderRequestRequestTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadMetadataTypeDef",
    "UserMetadataTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
)

AbortDocumentVersionUploadRequestRequestTypeDef = TypedDict(
    "AbortDocumentVersionUploadRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

ActivateUserRequestRequestTypeDef = TypedDict(
    "ActivateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

ActivateUserResponseTypeDef = TypedDict(
    "ActivateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": NotRequired[ActivityTypeType],
        "TimeStamp": NotRequired[datetime],
        "IsIndirectActivity": NotRequired[bool],
        "OrganizationId": NotRequired[str],
        "Initiator": NotRequired["UserMetadataTypeDef"],
        "Participants": NotRequired["ParticipantsTypeDef"],
        "ResourceMetadata": NotRequired["ResourceMetadataTypeDef"],
        "OriginalParent": NotRequired["ResourceMetadataTypeDef"],
        "CommentMetadata": NotRequired["CommentMetadataTypeDef"],
    },
)

AddResourcePermissionsRequestRequestTypeDef = TypedDict(
    "AddResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Principals": Sequence["SharePrincipalTypeDef"],
        "AuthenticationToken": NotRequired[str],
        "NotificationOptions": NotRequired["NotificationOptionsTypeDef"],
    },
)

AddResourcePermissionsResponseTypeDef = TypedDict(
    "AddResourcePermissionsResponseTypeDef",
    {
        "ShareResults": List["ShareResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CommentMetadataTypeDef = TypedDict(
    "CommentMetadataTypeDef",
    {
        "CommentId": NotRequired[str],
        "Contributor": NotRequired["UserTypeDef"],
        "CreatedTimestamp": NotRequired[datetime],
        "CommentStatus": NotRequired[CommentStatusTypeType],
        "RecipientId": NotRequired[str],
    },
)

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "CommentId": str,
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Text": NotRequired[str],
        "Contributor": NotRequired["UserTypeDef"],
        "CreatedTimestamp": NotRequired[datetime],
        "Status": NotRequired[CommentStatusTypeType],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "RecipientId": NotRequired[str],
    },
)

CreateCommentRequestRequestTypeDef = TypedDict(
    "CreateCommentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "Text": str,
        "AuthenticationToken": NotRequired[str],
        "ParentId": NotRequired[str],
        "ThreadId": NotRequired[str],
        "Visibility": NotRequired[CommentVisibilityTypeType],
        "NotifyCollaborators": NotRequired[bool],
    },
)

CreateCommentResponseTypeDef = TypedDict(
    "CreateCommentResponseTypeDef",
    {
        "Comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomMetadataRequestRequestTypeDef = TypedDict(
    "CreateCustomMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "CustomMetadata": Mapping[str, str],
        "AuthenticationToken": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

CreateFolderRequestRequestTypeDef = TypedDict(
    "CreateFolderRequestRequestTypeDef",
    {
        "ParentFolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
    },
)

CreateFolderResponseTypeDef = TypedDict(
    "CreateFolderResponseTypeDef",
    {
        "Metadata": "FolderMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLabelsRequestRequestTypeDef = TypedDict(
    "CreateLabelsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "Labels": Sequence[str],
        "AuthenticationToken": NotRequired[str],
    },
)

CreateNotificationSubscriptionRequestRequestTypeDef = TypedDict(
    "CreateNotificationSubscriptionRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Endpoint": str,
        "Protocol": Literal["HTTPS"],
        "SubscriptionType": Literal["ALL"],
    },
)

CreateNotificationSubscriptionResponseTypeDef = TypedDict(
    "CreateNotificationSubscriptionResponseTypeDef",
    {
        "Subscription": "SubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "Username": str,
        "GivenName": str,
        "Surname": str,
        "Password": str,
        "OrganizationId": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "TimeZoneId": NotRequired[str],
        "StorageRule": NotRequired["StorageRuleTypeTypeDef"],
        "AuthenticationToken": NotRequired[str],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeactivateUserRequestRequestTypeDef = TypedDict(
    "DeactivateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DeleteCommentRequestRequestTypeDef = TypedDict(
    "DeleteCommentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "CommentId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DeleteCustomMetadataRequestRequestTypeDef = TypedDict(
    "DeleteCustomMetadataRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "VersionId": NotRequired[str],
        "Keys": NotRequired[Sequence[str]],
        "DeleteAll": NotRequired[bool],
    },
)

DeleteDocumentRequestRequestTypeDef = TypedDict(
    "DeleteDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DeleteFolderContentsRequestRequestTypeDef = TypedDict(
    "DeleteFolderContentsRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DeleteFolderRequestRequestTypeDef = TypedDict(
    "DeleteFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DeleteLabelsRequestRequestTypeDef = TypedDict(
    "DeleteLabelsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "Labels": NotRequired[Sequence[str]],
        "DeleteAll": NotRequired[bool],
    },
)

DeleteNotificationSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteNotificationSubscriptionRequestRequestTypeDef",
    {
        "SubscriptionId": str,
        "OrganizationId": str,
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

DescribeActivitiesRequestRequestTypeDef = TypedDict(
    "DescribeActivitiesRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "OrganizationId": NotRequired[str],
        "ActivityTypes": NotRequired[str],
        "ResourceId": NotRequired[str],
        "UserId": NotRequired[str],
        "IncludeIndirectActivities": NotRequired[bool],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeActivitiesResponseTypeDef = TypedDict(
    "DescribeActivitiesResponseTypeDef",
    {
        "UserActivities": List["ActivityTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCommentsRequestRequestTypeDef = TypedDict(
    "DescribeCommentsRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeCommentsResponseTypeDef = TypedDict(
    "DescribeCommentsResponseTypeDef",
    {
        "Comments": List["CommentTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDocumentVersionsRequestRequestTypeDef = TypedDict(
    "DescribeDocumentVersionsRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
        "Include": NotRequired[str],
        "Fields": NotRequired[str],
    },
)

DescribeDocumentVersionsResponseTypeDef = TypedDict(
    "DescribeDocumentVersionsResponseTypeDef",
    {
        "DocumentVersions": List["DocumentVersionMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFolderContentsRequestRequestTypeDef = TypedDict(
    "DescribeFolderContentsRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Sort": NotRequired[ResourceSortTypeType],
        "Order": NotRequired[OrderTypeType],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
        "Type": NotRequired[FolderContentTypeType],
        "Include": NotRequired[str],
    },
)

DescribeFolderContentsResponseTypeDef = TypedDict(
    "DescribeFolderContentsResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGroupsRequestRequestTypeDef = TypedDict(
    "DescribeGroupsRequestRequestTypeDef",
    {
        "SearchQuery": str,
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeGroupsResponseTypeDef = TypedDict(
    "DescribeGroupsResponseTypeDef",
    {
        "Groups": List["GroupMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNotificationSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsRequestRequestTypeDef",
    {
        "OrganizationId": str,
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
    },
)

DescribeNotificationSubscriptionsResponseTypeDef = TypedDict(
    "DescribeNotificationSubscriptionsResponseTypeDef",
    {
        "Subscriptions": List["SubscriptionTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeResourcePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
        "PrincipalId": NotRequired[str],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeResourcePermissionsResponseTypeDef = TypedDict(
    "DescribeResourcePermissionsResponseTypeDef",
    {
        "Principals": List["PrincipalTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRootFoldersRequestRequestTypeDef = TypedDict(
    "DescribeRootFoldersRequestRequestTypeDef",
    {
        "AuthenticationToken": str,
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

DescribeRootFoldersResponseTypeDef = TypedDict(
    "DescribeRootFoldersResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUsersRequestRequestTypeDef = TypedDict(
    "DescribeUsersRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "UserIds": NotRequired[str],
        "Query": NotRequired[str],
        "Include": NotRequired[UserFilterTypeType],
        "Order": NotRequired[OrderTypeType],
        "Sort": NotRequired[UserSortTypeType],
        "Marker": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
    },
)

DescribeUsersResponseTypeDef = TypedDict(
    "DescribeUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "TotalNumberOfUsers": int,
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentMetadataTypeDef = TypedDict(
    "DocumentMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "CreatorId": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "LatestVersionMetadata": NotRequired["DocumentVersionMetadataTypeDef"],
        "ResourceState": NotRequired[ResourceStateTypeType],
        "Labels": NotRequired[List[str]],
    },
)

DocumentVersionMetadataTypeDef = TypedDict(
    "DocumentVersionMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ContentType": NotRequired[str],
        "Size": NotRequired[int],
        "Signature": NotRequired[str],
        "Status": NotRequired[DocumentStatusTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "ContentCreatedTimestamp": NotRequired[datetime],
        "ContentModifiedTimestamp": NotRequired[datetime],
        "CreatorId": NotRequired[str],
        "Thumbnail": NotRequired[Dict[DocumentThumbnailTypeType, str]],
        "Source": NotRequired[Dict[DocumentSourceTypeType, str]],
    },
)

FolderMetadataTypeDef = TypedDict(
    "FolderMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "CreatorId": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "ResourceState": NotRequired[ResourceStateTypeType],
        "Signature": NotRequired[str],
        "Labels": NotRequired[List[str]],
        "Size": NotRequired[int],
        "LatestVersionSize": NotRequired[int],
    },
)

GetCurrentUserRequestRequestTypeDef = TypedDict(
    "GetCurrentUserRequestRequestTypeDef",
    {
        "AuthenticationToken": str,
    },
)

GetCurrentUserResponseTypeDef = TypedDict(
    "GetCurrentUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDocumentPathRequestRequestTypeDef = TypedDict(
    "GetDocumentPathRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
        "Marker": NotRequired[str],
    },
)

GetDocumentPathResponseTypeDef = TypedDict(
    "GetDocumentPathResponseTypeDef",
    {
        "Path": "ResourcePathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDocumentRequestRequestTypeDef = TypedDict(
    "GetDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)

GetDocumentResponseTypeDef = TypedDict(
    "GetDocumentResponseTypeDef",
    {
        "Metadata": "DocumentMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDocumentVersionRequestRequestTypeDef = TypedDict(
    "GetDocumentVersionRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "Fields": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)

GetDocumentVersionResponseTypeDef = TypedDict(
    "GetDocumentVersionResponseTypeDef",
    {
        "Metadata": "DocumentVersionMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFolderPathRequestRequestTypeDef = TypedDict(
    "GetFolderPathRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Limit": NotRequired[int],
        "Fields": NotRequired[str],
        "Marker": NotRequired[str],
    },
)

GetFolderPathResponseTypeDef = TypedDict(
    "GetFolderPathResponseTypeDef",
    {
        "Path": "ResourcePathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFolderRequestRequestTypeDef = TypedDict(
    "GetFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "IncludeCustomMetadata": NotRequired[bool],
    },
)

GetFolderResponseTypeDef = TypedDict(
    "GetFolderResponseTypeDef",
    {
        "Metadata": "FolderMetadataTypeDef",
        "CustomMetadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcesRequestRequestTypeDef = TypedDict(
    "GetResourcesRequestRequestTypeDef",
    {
        "AuthenticationToken": NotRequired[str],
        "UserId": NotRequired[str],
        "CollectionType": NotRequired[Literal["SHARED_WITH_ME"]],
        "Limit": NotRequired[int],
        "Marker": NotRequired[str],
    },
)

GetResourcesResponseTypeDef = TypedDict(
    "GetResourcesResponseTypeDef",
    {
        "Folders": List["FolderMetadataTypeDef"],
        "Documents": List["DocumentMetadataTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GroupMetadataTypeDef = TypedDict(
    "GroupMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)

InitiateDocumentVersionUploadRequestRequestTypeDef = TypedDict(
    "InitiateDocumentVersionUploadRequestRequestTypeDef",
    {
        "ParentFolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "ContentCreatedTimestamp": NotRequired[Union[datetime, str]],
        "ContentModifiedTimestamp": NotRequired[Union[datetime, str]],
        "ContentType": NotRequired[str],
        "DocumentSizeInBytes": NotRequired[int],
    },
)

InitiateDocumentVersionUploadResponseTypeDef = TypedDict(
    "InitiateDocumentVersionUploadResponseTypeDef",
    {
        "Metadata": "DocumentMetadataTypeDef",
        "UploadMetadata": "UploadMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationOptionsTypeDef = TypedDict(
    "NotificationOptionsTypeDef",
    {
        "SendEmail": NotRequired[bool],
        "EmailMessage": NotRequired[str],
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

ParticipantsTypeDef = TypedDict(
    "ParticipantsTypeDef",
    {
        "Users": NotRequired[List["UserMetadataTypeDef"]],
        "Groups": NotRequired[List["GroupMetadataTypeDef"]],
    },
)

PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef",
    {
        "Role": NotRequired[RoleTypeType],
        "Type": NotRequired[RolePermissionTypeType],
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[PrincipalTypeType],
        "Roles": NotRequired[List["PermissionInfoTypeDef"]],
    },
)

RemoveAllResourcePermissionsRequestRequestTypeDef = TypedDict(
    "RemoveAllResourcePermissionsRequestRequestTypeDef",
    {
        "ResourceId": str,
        "AuthenticationToken": NotRequired[str],
    },
)

RemoveResourcePermissionRequestRequestTypeDef = TypedDict(
    "RemoveResourcePermissionRequestRequestTypeDef",
    {
        "ResourceId": str,
        "PrincipalId": str,
        "AuthenticationToken": NotRequired[str],
        "PrincipalType": NotRequired[PrincipalTypeType],
    },
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": NotRequired[ResourceTypeType],
        "Name": NotRequired[str],
        "OriginalName": NotRequired[str],
        "Id": NotRequired[str],
        "VersionId": NotRequired[str],
        "Owner": NotRequired["UserMetadataTypeDef"],
        "ParentId": NotRequired[str],
    },
)

ResourcePathComponentTypeDef = TypedDict(
    "ResourcePathComponentTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ResourcePathTypeDef = TypedDict(
    "ResourcePathTypeDef",
    {
        "Components": NotRequired[List["ResourcePathComponentTypeDef"]],
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

SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef",
    {
        "Id": str,
        "Type": PrincipalTypeType,
        "Role": RoleTypeType,
    },
)

ShareResultTypeDef = TypedDict(
    "ShareResultTypeDef",
    {
        "PrincipalId": NotRequired[str],
        "InviteePrincipalId": NotRequired[str],
        "Role": NotRequired[RoleTypeType],
        "Status": NotRequired[ShareStatusTypeType],
        "ShareId": NotRequired[str],
        "StatusMessage": NotRequired[str],
    },
)

StorageRuleTypeTypeDef = TypedDict(
    "StorageRuleTypeTypeDef",
    {
        "StorageAllocatedInBytes": NotRequired[int],
        "StorageType": NotRequired[StorageTypeType],
    },
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "SubscriptionId": NotRequired[str],
        "EndPoint": NotRequired[str],
        "Protocol": NotRequired[Literal["HTTPS"]],
    },
)

UpdateDocumentRequestRequestTypeDef = TypedDict(
    "UpdateDocumentRequestRequestTypeDef",
    {
        "DocumentId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "ResourceState": NotRequired[ResourceStateTypeType],
    },
)

UpdateDocumentVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentVersionRequestRequestTypeDef",
    {
        "DocumentId": str,
        "VersionId": str,
        "AuthenticationToken": NotRequired[str],
        "VersionStatus": NotRequired[Literal["ACTIVE"]],
    },
)

UpdateFolderRequestRequestTypeDef = TypedDict(
    "UpdateFolderRequestRequestTypeDef",
    {
        "FolderId": str,
        "AuthenticationToken": NotRequired[str],
        "Name": NotRequired[str],
        "ParentFolderId": NotRequired[str],
        "ResourceState": NotRequired[ResourceStateTypeType],
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "AuthenticationToken": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "Type": NotRequired[UserTypeType],
        "StorageRule": NotRequired["StorageRuleTypeTypeDef"],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "GrantPoweruserPrivileges": NotRequired[BooleanEnumTypeType],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "UploadUrl": NotRequired[str],
        "SignedHeaders": NotRequired[Dict[str, str]],
    },
)

UserMetadataTypeDef = TypedDict(
    "UserMetadataTypeDef",
    {
        "Id": NotRequired[str],
        "Username": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "EmailAddress": NotRequired[str],
    },
)

UserStorageMetadataTypeDef = TypedDict(
    "UserStorageMetadataTypeDef",
    {
        "StorageUtilizedInBytes": NotRequired[int],
        "StorageRule": NotRequired["StorageRuleTypeTypeDef"],
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": NotRequired[str],
        "Username": NotRequired[str],
        "EmailAddress": NotRequired[str],
        "GivenName": NotRequired[str],
        "Surname": NotRequired[str],
        "OrganizationId": NotRequired[str],
        "RootFolderId": NotRequired[str],
        "RecycleBinFolderId": NotRequired[str],
        "Status": NotRequired[UserStatusTypeType],
        "Type": NotRequired[UserTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "ModifiedTimestamp": NotRequired[datetime],
        "TimeZoneId": NotRequired[str],
        "Locale": NotRequired[LocaleTypeType],
        "Storage": NotRequired["UserStorageMetadataTypeDef"],
    },
)
