"""
Type annotations for codestar service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_codestar/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_codestar.type_defs import AssociateTeamMemberRequestRequestTypeDef

    data: AssociateTeamMemberRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateTeamMemberRequestRequestTypeDef",
    "AssociateTeamMemberResultTypeDef",
    "CodeCommitCodeDestinationTypeDef",
    "CodeDestinationTypeDef",
    "CodeSourceTypeDef",
    "CodeTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResultTypeDef",
    "CreateUserProfileRequestRequestTypeDef",
    "CreateUserProfileResultTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResultTypeDef",
    "DeleteUserProfileRequestRequestTypeDef",
    "DeleteUserProfileResultTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResultTypeDef",
    "DescribeUserProfileRequestRequestTypeDef",
    "DescribeUserProfileResultTypeDef",
    "DisassociateTeamMemberRequestRequestTypeDef",
    "GitHubCodeDestinationTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResultTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResultTypeDef",
    "ListTagsForProjectRequestRequestTypeDef",
    "ListTagsForProjectResultTypeDef",
    "ListTeamMembersRequestRequestTypeDef",
    "ListTeamMembersResultTypeDef",
    "ListUserProfilesRequestRequestTypeDef",
    "ListUserProfilesResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "S3LocationTypeDef",
    "TagProjectRequestRequestTypeDef",
    "TagProjectResultTypeDef",
    "TeamMemberTypeDef",
    "ToolchainSourceTypeDef",
    "ToolchainTypeDef",
    "UntagProjectRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateTeamMemberRequestRequestTypeDef",
    "UpdateTeamMemberResultTypeDef",
    "UpdateUserProfileRequestRequestTypeDef",
    "UpdateUserProfileResultTypeDef",
    "UserProfileSummaryTypeDef",
)

AssociateTeamMemberRequestRequestTypeDef = TypedDict(
    "AssociateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
        "projectRole": str,
        "clientRequestToken": NotRequired[str],
        "remoteAccessAllowed": NotRequired[bool],
    },
)

AssociateTeamMemberResultTypeDef = TypedDict(
    "AssociateTeamMemberResultTypeDef",
    {
        "clientRequestToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CodeCommitCodeDestinationTypeDef = TypedDict(
    "CodeCommitCodeDestinationTypeDef",
    {
        "name": str,
    },
)

CodeDestinationTypeDef = TypedDict(
    "CodeDestinationTypeDef",
    {
        "codeCommit": NotRequired["CodeCommitCodeDestinationTypeDef"],
        "gitHub": NotRequired["GitHubCodeDestinationTypeDef"],
    },
)

CodeSourceTypeDef = TypedDict(
    "CodeSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

CodeTypeDef = TypedDict(
    "CodeTypeDef",
    {
        "source": "CodeSourceTypeDef",
        "destination": "CodeDestinationTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": str,
        "id": str,
        "description": NotRequired[str],
        "clientRequestToken": NotRequired[str],
        "sourceCode": NotRequired[Sequence["CodeTypeDef"]],
        "toolchain": NotRequired["ToolchainTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "id": str,
        "arn": str,
        "clientRequestToken": str,
        "projectTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserProfileRequestRequestTypeDef = TypedDict(
    "CreateUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": NotRequired[str],
    },
)

CreateUserProfileResultTypeDef = TypedDict(
    "CreateUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "id": str,
        "clientRequestToken": NotRequired[str],
        "deleteStack": NotRequired[bool],
    },
)

DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef",
    {
        "stackId": str,
        "projectArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserProfileRequestRequestTypeDef = TypedDict(
    "DeleteUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
    },
)

DeleteUserProfileResultTypeDef = TypedDict(
    "DeleteUserProfileResultTypeDef",
    {
        "userArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": "ProjectStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUserProfileRequestRequestTypeDef = TypedDict(
    "DescribeUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
    },
)

DescribeUserProfileResultTypeDef = TypedDict(
    "DescribeUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTeamMemberRequestRequestTypeDef = TypedDict(
    "DisassociateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
    },
)

GitHubCodeDestinationTypeDef = TypedDict(
    "GitHubCodeDestinationTypeDef",
    {
        "name": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
        "description": NotRequired[str],
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListResourcesResultTypeDef = TypedDict(
    "ListResourcesResultTypeDef",
    {
        "resources": List["ResourceTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForProjectRequestRequestTypeDef = TypedDict(
    "ListTagsForProjectRequestRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTagsForProjectResultTypeDef = TypedDict(
    "ListTagsForProjectResultTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTeamMembersRequestRequestTypeDef = TypedDict(
    "ListTeamMembersRequestRequestTypeDef",
    {
        "projectId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTeamMembersResultTypeDef = TypedDict(
    "ListTeamMembersResultTypeDef",
    {
        "teamMembers": List["TeamMemberTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserProfilesRequestRequestTypeDef = TypedDict(
    "ListUserProfilesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListUserProfilesResultTypeDef = TypedDict(
    "ListUserProfilesResultTypeDef",
    {
        "userProfiles": List["UserProfileSummaryTypeDef"],
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

ProjectStatusTypeDef = TypedDict(
    "ProjectStatusTypeDef",
    {
        "state": str,
        "reason": NotRequired[str],
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectId": NotRequired[str],
        "projectArn": NotRequired[str],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": str,
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

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "bucketName": NotRequired[str],
        "bucketKey": NotRequired[str],
    },
)

TagProjectRequestRequestTypeDef = TypedDict(
    "TagProjectRequestRequestTypeDef",
    {
        "id": str,
        "tags": Mapping[str, str],
    },
)

TagProjectResultTypeDef = TypedDict(
    "TagProjectResultTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TeamMemberTypeDef = TypedDict(
    "TeamMemberTypeDef",
    {
        "userArn": str,
        "projectRole": str,
        "remoteAccessAllowed": NotRequired[bool],
    },
)

ToolchainSourceTypeDef = TypedDict(
    "ToolchainSourceTypeDef",
    {
        "s3": "S3LocationTypeDef",
    },
)

ToolchainTypeDef = TypedDict(
    "ToolchainTypeDef",
    {
        "source": "ToolchainSourceTypeDef",
        "roleArn": NotRequired[str],
        "stackParameters": NotRequired[Mapping[str, str]],
    },
)

UntagProjectRequestRequestTypeDef = TypedDict(
    "UntagProjectRequestRequestTypeDef",
    {
        "id": str,
        "tags": Sequence[str],
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "id": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)

UpdateTeamMemberRequestRequestTypeDef = TypedDict(
    "UpdateTeamMemberRequestRequestTypeDef",
    {
        "projectId": str,
        "userArn": str,
        "projectRole": NotRequired[str],
        "remoteAccessAllowed": NotRequired[bool],
    },
)

UpdateTeamMemberResultTypeDef = TypedDict(
    "UpdateTeamMemberResultTypeDef",
    {
        "userArn": str,
        "projectRole": str,
        "remoteAccessAllowed": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserProfileRequestRequestTypeDef = TypedDict(
    "UpdateUserProfileRequestRequestTypeDef",
    {
        "userArn": str,
        "displayName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "sshPublicKey": NotRequired[str],
    },
)

UpdateUserProfileResultTypeDef = TypedDict(
    "UpdateUserProfileResultTypeDef",
    {
        "userArn": str,
        "displayName": str,
        "emailAddress": str,
        "sshPublicKey": str,
        "createdTimestamp": datetime,
        "lastModifiedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserProfileSummaryTypeDef = TypedDict(
    "UserProfileSummaryTypeDef",
    {
        "userArn": NotRequired[str],
        "displayName": NotRequired[str],
        "emailAddress": NotRequired[str],
        "sshPublicKey": NotRequired[str],
    },
)
