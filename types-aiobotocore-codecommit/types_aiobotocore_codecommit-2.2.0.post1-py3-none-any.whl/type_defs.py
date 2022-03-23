"""
Type annotations for codecommit service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_codecommit/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_codecommit.type_defs import ApprovalRuleEventMetadataTypeDef

    data: ApprovalRuleEventMetadataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ApprovalStateType,
    ChangeTypeEnumType,
    ConflictDetailLevelTypeEnumType,
    ConflictResolutionStrategyTypeEnumType,
    FileModeTypeEnumType,
    MergeOptionTypeEnumType,
    ObjectTypeEnumType,
    OrderEnumType,
    OverrideStatusType,
    PullRequestEventTypeType,
    PullRequestStatusEnumType,
    RelativeFileVersionEnumType,
    ReplacementTypeEnumType,
    RepositoryTriggerEventEnumType,
    SortByEnumType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalRuleEventMetadataTypeDef",
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    "ApprovalRuleTemplateTypeDef",
    "ApprovalRuleTypeDef",
    "ApprovalStateChangedEventMetadataTypeDef",
    "ApprovalTypeDef",
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    "BatchDescribeMergeConflictsErrorTypeDef",
    "BatchDescribeMergeConflictsInputRequestTypeDef",
    "BatchDescribeMergeConflictsOutputTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    "BatchGetCommitsErrorTypeDef",
    "BatchGetCommitsInputRequestTypeDef",
    "BatchGetCommitsOutputTypeDef",
    "BatchGetRepositoriesInputRequestTypeDef",
    "BatchGetRepositoriesOutputTypeDef",
    "BlobMetadataTypeDef",
    "BranchInfoTypeDef",
    "CommentTypeDef",
    "CommentsForComparedCommitTypeDef",
    "CommentsForPullRequestTypeDef",
    "CommitTypeDef",
    "ConflictMetadataTypeDef",
    "ConflictResolutionTypeDef",
    "ConflictTypeDef",
    "CreateApprovalRuleTemplateInputRequestTypeDef",
    "CreateApprovalRuleTemplateOutputTypeDef",
    "CreateBranchInputRequestTypeDef",
    "CreateCommitInputRequestTypeDef",
    "CreateCommitOutputTypeDef",
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    "CreatePullRequestApprovalRuleOutputTypeDef",
    "CreatePullRequestInputRequestTypeDef",
    "CreatePullRequestOutputTypeDef",
    "CreateRepositoryInputRequestTypeDef",
    "CreateRepositoryOutputTypeDef",
    "CreateUnreferencedMergeCommitInputRequestTypeDef",
    "CreateUnreferencedMergeCommitOutputTypeDef",
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    "DeleteApprovalRuleTemplateOutputTypeDef",
    "DeleteBranchInputRequestTypeDef",
    "DeleteBranchOutputTypeDef",
    "DeleteCommentContentInputRequestTypeDef",
    "DeleteCommentContentOutputTypeDef",
    "DeleteFileEntryTypeDef",
    "DeleteFileInputRequestTypeDef",
    "DeleteFileOutputTypeDef",
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    "DeletePullRequestApprovalRuleOutputTypeDef",
    "DeleteRepositoryInputRequestTypeDef",
    "DeleteRepositoryOutputTypeDef",
    "DescribeMergeConflictsInputRequestTypeDef",
    "DescribeMergeConflictsOutputTypeDef",
    "DescribePullRequestEventsInputRequestTypeDef",
    "DescribePullRequestEventsOutputTypeDef",
    "DifferenceTypeDef",
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    "EvaluationTypeDef",
    "FileMetadataTypeDef",
    "FileModesTypeDef",
    "FileSizesTypeDef",
    "FileTypeDef",
    "FolderTypeDef",
    "GetApprovalRuleTemplateInputRequestTypeDef",
    "GetApprovalRuleTemplateOutputTypeDef",
    "GetBlobInputRequestTypeDef",
    "GetBlobOutputTypeDef",
    "GetBranchInputRequestTypeDef",
    "GetBranchOutputTypeDef",
    "GetCommentInputRequestTypeDef",
    "GetCommentOutputTypeDef",
    "GetCommentReactionsInputRequestTypeDef",
    "GetCommentReactionsOutputTypeDef",
    "GetCommentsForComparedCommitInputRequestTypeDef",
    "GetCommentsForComparedCommitOutputTypeDef",
    "GetCommentsForPullRequestInputRequestTypeDef",
    "GetCommentsForPullRequestOutputTypeDef",
    "GetCommitInputRequestTypeDef",
    "GetCommitOutputTypeDef",
    "GetDifferencesInputRequestTypeDef",
    "GetDifferencesOutputTypeDef",
    "GetFileInputRequestTypeDef",
    "GetFileOutputTypeDef",
    "GetFolderInputRequestTypeDef",
    "GetFolderOutputTypeDef",
    "GetMergeCommitInputRequestTypeDef",
    "GetMergeCommitOutputTypeDef",
    "GetMergeConflictsInputRequestTypeDef",
    "GetMergeConflictsOutputTypeDef",
    "GetMergeOptionsInputRequestTypeDef",
    "GetMergeOptionsOutputTypeDef",
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    "GetPullRequestApprovalStatesOutputTypeDef",
    "GetPullRequestInputRequestTypeDef",
    "GetPullRequestOutputTypeDef",
    "GetPullRequestOverrideStateInputRequestTypeDef",
    "GetPullRequestOverrideStateOutputTypeDef",
    "GetRepositoryInputRequestTypeDef",
    "GetRepositoryOutputTypeDef",
    "GetRepositoryTriggersInputRequestTypeDef",
    "GetRepositoryTriggersOutputTypeDef",
    "IsBinaryFileTypeDef",
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    "ListApprovalRuleTemplatesOutputTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    "ListBranchesInputRequestTypeDef",
    "ListBranchesOutputTypeDef",
    "ListPullRequestsInputRequestTypeDef",
    "ListPullRequestsOutputTypeDef",
    "ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    "ListRepositoriesInputRequestTypeDef",
    "ListRepositoriesOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LocationTypeDef",
    "MergeBranchesByFastForwardInputRequestTypeDef",
    "MergeBranchesByFastForwardOutputTypeDef",
    "MergeBranchesBySquashInputRequestTypeDef",
    "MergeBranchesBySquashOutputTypeDef",
    "MergeBranchesByThreeWayInputRequestTypeDef",
    "MergeBranchesByThreeWayOutputTypeDef",
    "MergeHunkDetailTypeDef",
    "MergeHunkTypeDef",
    "MergeMetadataTypeDef",
    "MergeOperationsTypeDef",
    "MergePullRequestByFastForwardInputRequestTypeDef",
    "MergePullRequestByFastForwardOutputTypeDef",
    "MergePullRequestBySquashInputRequestTypeDef",
    "MergePullRequestBySquashOutputTypeDef",
    "MergePullRequestByThreeWayInputRequestTypeDef",
    "MergePullRequestByThreeWayOutputTypeDef",
    "ObjectTypesTypeDef",
    "OriginApprovalRuleTemplateTypeDef",
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PostCommentForComparedCommitInputRequestTypeDef",
    "PostCommentForComparedCommitOutputTypeDef",
    "PostCommentForPullRequestInputRequestTypeDef",
    "PostCommentForPullRequestOutputTypeDef",
    "PostCommentReplyInputRequestTypeDef",
    "PostCommentReplyOutputTypeDef",
    "PullRequestCreatedEventMetadataTypeDef",
    "PullRequestEventTypeDef",
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    "PullRequestStatusChangedEventMetadataTypeDef",
    "PullRequestTargetTypeDef",
    "PullRequestTypeDef",
    "PutCommentReactionInputRequestTypeDef",
    "PutFileEntryTypeDef",
    "PutFileInputRequestTypeDef",
    "PutFileOutputTypeDef",
    "PutRepositoryTriggersInputRequestTypeDef",
    "PutRepositoryTriggersOutputTypeDef",
    "ReactionForCommentTypeDef",
    "ReactionValueFormatsTypeDef",
    "ReplaceContentEntryTypeDef",
    "RepositoryMetadataTypeDef",
    "RepositoryNameIdPairTypeDef",
    "RepositoryTriggerExecutionFailureTypeDef",
    "RepositoryTriggerTypeDef",
    "ResponseMetadataTypeDef",
    "SetFileModeEntryTypeDef",
    "SourceFileSpecifierTypeDef",
    "SubModuleTypeDef",
    "SymbolicLinkTypeDef",
    "TagResourceInputRequestTypeDef",
    "TargetTypeDef",
    "TestRepositoryTriggersInputRequestTypeDef",
    "TestRepositoryTriggersOutputTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateApprovalRuleTemplateContentInputRequestTypeDef",
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    "UpdateCommentInputRequestTypeDef",
    "UpdateCommentOutputTypeDef",
    "UpdateDefaultBranchInputRequestTypeDef",
    "UpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    "UpdatePullRequestDescriptionOutputTypeDef",
    "UpdatePullRequestStatusInputRequestTypeDef",
    "UpdatePullRequestStatusOutputTypeDef",
    "UpdatePullRequestTitleInputRequestTypeDef",
    "UpdatePullRequestTitleOutputTypeDef",
    "UpdateRepositoryDescriptionInputRequestTypeDef",
    "UpdateRepositoryNameInputRequestTypeDef",
    "UserInfoTypeDef",
)

ApprovalRuleEventMetadataTypeDef = TypedDict(
    "ApprovalRuleEventMetadataTypeDef",
    {
        "approvalRuleName": NotRequired[str],
        "approvalRuleId": NotRequired[str],
        "approvalRuleContent": NotRequired[str],
    },
)

ApprovalRuleOverriddenEventMetadataTypeDef = TypedDict(
    "ApprovalRuleOverriddenEventMetadataTypeDef",
    {
        "revisionId": NotRequired[str],
        "overrideStatus": NotRequired[OverrideStatusType],
    },
)

ApprovalRuleTemplateTypeDef = TypedDict(
    "ApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": NotRequired[str],
        "approvalRuleTemplateName": NotRequired[str],
        "approvalRuleTemplateDescription": NotRequired[str],
        "approvalRuleTemplateContent": NotRequired[str],
        "ruleContentSha256": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "lastModifiedUser": NotRequired[str],
    },
)

ApprovalRuleTypeDef = TypedDict(
    "ApprovalRuleTypeDef",
    {
        "approvalRuleId": NotRequired[str],
        "approvalRuleName": NotRequired[str],
        "approvalRuleContent": NotRequired[str],
        "ruleContentSha256": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "lastModifiedUser": NotRequired[str],
        "originApprovalRuleTemplate": NotRequired["OriginApprovalRuleTemplateTypeDef"],
    },
)

ApprovalStateChangedEventMetadataTypeDef = TypedDict(
    "ApprovalStateChangedEventMetadataTypeDef",
    {
        "revisionId": NotRequired[str],
        "approvalStatus": NotRequired[ApprovalStateType],
    },
)

ApprovalTypeDef = TypedDict(
    "ApprovalTypeDef",
    {
        "userArn": NotRequired[str],
        "approvalState": NotRequired[ApprovalStateType],
    },
)

AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef = TypedDict(
    "AssociateApprovalRuleTemplateWithRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef",
    {
        "repositoryName": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": Sequence[str],
    },
)

BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef = TypedDict(
    "BatchAssociateApprovalRuleTemplateWithRepositoriesOutputTypeDef",
    {
        "associatedRepositoryNames": List[str],
        "errors": List["BatchAssociateApprovalRuleTemplateWithRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDescribeMergeConflictsErrorTypeDef = TypedDict(
    "BatchDescribeMergeConflictsErrorTypeDef",
    {
        "filePath": str,
        "exceptionName": str,
        "message": str,
    },
)

BatchDescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "BatchDescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "maxMergeHunks": NotRequired[int],
        "maxConflictFiles": NotRequired[int],
        "filePaths": NotRequired[Sequence[str]],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
    },
)

BatchDescribeMergeConflictsOutputTypeDef = TypedDict(
    "BatchDescribeMergeConflictsOutputTypeDef",
    {
        "conflicts": List["ConflictTypeDef"],
        "nextToken": str,
        "errors": List["BatchDescribeMergeConflictsErrorTypeDef"],
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef",
    {
        "repositoryName": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryNames": Sequence[str],
    },
)

BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef = TypedDict(
    "BatchDisassociateApprovalRuleTemplateFromRepositoriesOutputTypeDef",
    {
        "disassociatedRepositoryNames": List[str],
        "errors": List["BatchDisassociateApprovalRuleTemplateFromRepositoriesErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCommitsErrorTypeDef = TypedDict(
    "BatchGetCommitsErrorTypeDef",
    {
        "commitId": NotRequired[str],
        "errorCode": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

BatchGetCommitsInputRequestTypeDef = TypedDict(
    "BatchGetCommitsInputRequestTypeDef",
    {
        "commitIds": Sequence[str],
        "repositoryName": str,
    },
)

BatchGetCommitsOutputTypeDef = TypedDict(
    "BatchGetCommitsOutputTypeDef",
    {
        "commits": List["CommitTypeDef"],
        "errors": List["BatchGetCommitsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetRepositoriesInputRequestTypeDef = TypedDict(
    "BatchGetRepositoriesInputRequestTypeDef",
    {
        "repositoryNames": Sequence[str],
    },
)

BatchGetRepositoriesOutputTypeDef = TypedDict(
    "BatchGetRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryMetadataTypeDef"],
        "repositoriesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BlobMetadataTypeDef = TypedDict(
    "BlobMetadataTypeDef",
    {
        "blobId": NotRequired[str],
        "path": NotRequired[str],
        "mode": NotRequired[str],
    },
)

BranchInfoTypeDef = TypedDict(
    "BranchInfoTypeDef",
    {
        "branchName": NotRequired[str],
        "commitId": NotRequired[str],
    },
)

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "commentId": NotRequired[str],
        "content": NotRequired[str],
        "inReplyTo": NotRequired[str],
        "creationDate": NotRequired[datetime],
        "lastModifiedDate": NotRequired[datetime],
        "authorArn": NotRequired[str],
        "deleted": NotRequired[bool],
        "clientRequestToken": NotRequired[str],
        "callerReactions": NotRequired[List[str]],
        "reactionCounts": NotRequired[Dict[str, int]],
    },
)

CommentsForComparedCommitTypeDef = TypedDict(
    "CommentsForComparedCommitTypeDef",
    {
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "beforeBlobId": NotRequired[str],
        "afterBlobId": NotRequired[str],
        "location": NotRequired["LocationTypeDef"],
        "comments": NotRequired[List["CommentTypeDef"]],
    },
)

CommentsForPullRequestTypeDef = TypedDict(
    "CommentsForPullRequestTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "beforeBlobId": NotRequired[str],
        "afterBlobId": NotRequired[str],
        "location": NotRequired["LocationTypeDef"],
        "comments": NotRequired[List["CommentTypeDef"]],
    },
)

CommitTypeDef = TypedDict(
    "CommitTypeDef",
    {
        "commitId": NotRequired[str],
        "treeId": NotRequired[str],
        "parents": NotRequired[List[str]],
        "message": NotRequired[str],
        "author": NotRequired["UserInfoTypeDef"],
        "committer": NotRequired["UserInfoTypeDef"],
        "additionalData": NotRequired[str],
    },
)

ConflictMetadataTypeDef = TypedDict(
    "ConflictMetadataTypeDef",
    {
        "filePath": NotRequired[str],
        "fileSizes": NotRequired["FileSizesTypeDef"],
        "fileModes": NotRequired["FileModesTypeDef"],
        "objectTypes": NotRequired["ObjectTypesTypeDef"],
        "numberOfConflicts": NotRequired[int],
        "isBinaryFile": NotRequired["IsBinaryFileTypeDef"],
        "contentConflict": NotRequired[bool],
        "fileModeConflict": NotRequired[bool],
        "objectTypeConflict": NotRequired[bool],
        "mergeOperations": NotRequired["MergeOperationsTypeDef"],
    },
)

ConflictResolutionTypeDef = TypedDict(
    "ConflictResolutionTypeDef",
    {
        "replaceContents": NotRequired[Sequence["ReplaceContentEntryTypeDef"]],
        "deleteFiles": NotRequired[Sequence["DeleteFileEntryTypeDef"]],
        "setFileModes": NotRequired[Sequence["SetFileModeEntryTypeDef"]],
    },
)

ConflictTypeDef = TypedDict(
    "ConflictTypeDef",
    {
        "conflictMetadata": NotRequired["ConflictMetadataTypeDef"],
        "mergeHunks": NotRequired[List["MergeHunkTypeDef"]],
    },
)

CreateApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "CreateApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateContent": str,
        "approvalRuleTemplateDescription": NotRequired[str],
    },
)

CreateApprovalRuleTemplateOutputTypeDef = TypedDict(
    "CreateApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBranchInputRequestTypeDef = TypedDict(
    "CreateBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "commitId": str,
    },
)

CreateCommitInputRequestTypeDef = TypedDict(
    "CreateCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "parentCommitId": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "putFiles": NotRequired[Sequence["PutFileEntryTypeDef"]],
        "deleteFiles": NotRequired[Sequence["DeleteFileEntryTypeDef"]],
        "setFileModes": NotRequired[Sequence["SetFileModeEntryTypeDef"]],
    },
)

CreateCommitOutputTypeDef = TypedDict(
    "CreateCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "filesAdded": List["FileMetadataTypeDef"],
        "filesUpdated": List["FileMetadataTypeDef"],
        "filesDeleted": List["FileMetadataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "approvalRuleContent": str,
    },
)

CreatePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "CreatePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePullRequestInputRequestTypeDef = TypedDict(
    "CreatePullRequestInputRequestTypeDef",
    {
        "title": str,
        "targets": Sequence["TargetTypeDef"],
        "description": NotRequired[str],
        "clientRequestToken": NotRequired[str],
    },
)

CreatePullRequestOutputTypeDef = TypedDict(
    "CreatePullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryInputRequestTypeDef = TypedDict(
    "CreateRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryDescription": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateRepositoryOutputTypeDef = TypedDict(
    "CreateRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUnreferencedMergeCommitInputRequestTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

CreateUnreferencedMergeCommitOutputTypeDef = TypedDict(
    "CreateUnreferencedMergeCommitOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

DeleteApprovalRuleTemplateOutputTypeDef = TypedDict(
    "DeleteApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBranchInputRequestTypeDef = TypedDict(
    "DeleteBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
    },
)

DeleteBranchOutputTypeDef = TypedDict(
    "DeleteBranchOutputTypeDef",
    {
        "deletedBranch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCommentContentInputRequestTypeDef = TypedDict(
    "DeleteCommentContentInputRequestTypeDef",
    {
        "commentId": str,
    },
)

DeleteCommentContentOutputTypeDef = TypedDict(
    "DeleteCommentContentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFileEntryTypeDef = TypedDict(
    "DeleteFileEntryTypeDef",
    {
        "filePath": str,
    },
)

DeleteFileInputRequestTypeDef = TypedDict(
    "DeleteFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "filePath": str,
        "parentCommitId": str,
        "keepEmptyFolders": NotRequired[bool],
        "commitMessage": NotRequired[str],
        "name": NotRequired[str],
        "email": NotRequired[str],
    },
)

DeleteFileOutputTypeDef = TypedDict(
    "DeleteFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "filePath": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePullRequestApprovalRuleInputRequestTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
    },
)

DeletePullRequestApprovalRuleOutputTypeDef = TypedDict(
    "DeletePullRequestApprovalRuleOutputTypeDef",
    {
        "approvalRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryInputRequestTypeDef = TypedDict(
    "DeleteRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

DeleteRepositoryOutputTypeDef = TypedDict(
    "DeleteRepositoryOutputTypeDef",
    {
        "repositoryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMergeConflictsInputRequestTypeDef = TypedDict(
    "DescribeMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "filePath": str,
        "maxMergeHunks": NotRequired[int],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
    },
)

DescribeMergeConflictsOutputTypeDef = TypedDict(
    "DescribeMergeConflictsOutputTypeDef",
    {
        "conflictMetadata": "ConflictMetadataTypeDef",
        "mergeHunks": List["MergeHunkTypeDef"],
        "nextToken": str,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePullRequestEventsInputRequestTypeDef = TypedDict(
    "DescribePullRequestEventsInputRequestTypeDef",
    {
        "pullRequestId": str,
        "pullRequestEventType": NotRequired[PullRequestEventTypeType],
        "actorArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribePullRequestEventsOutputTypeDef = TypedDict(
    "DescribePullRequestEventsOutputTypeDef",
    {
        "pullRequestEvents": List["PullRequestEventTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DifferenceTypeDef = TypedDict(
    "DifferenceTypeDef",
    {
        "beforeBlob": NotRequired["BlobMetadataTypeDef"],
        "afterBlob": NotRequired["BlobMetadataTypeDef"],
        "changeType": NotRequired[ChangeTypeEnumType],
    },
)

DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef = TypedDict(
    "DisassociateApprovalRuleTemplateFromRepositoryInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "repositoryName": str,
    },
)

EvaluatePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

EvaluatePullRequestApprovalRulesOutputTypeDef = TypedDict(
    "EvaluatePullRequestApprovalRulesOutputTypeDef",
    {
        "evaluation": "EvaluationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EvaluationTypeDef = TypedDict(
    "EvaluationTypeDef",
    {
        "approved": NotRequired[bool],
        "overridden": NotRequired[bool],
        "approvalRulesSatisfied": NotRequired[List[str]],
        "approvalRulesNotSatisfied": NotRequired[List[str]],
    },
)

FileMetadataTypeDef = TypedDict(
    "FileMetadataTypeDef",
    {
        "absolutePath": NotRequired[str],
        "blobId": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)

FileModesTypeDef = TypedDict(
    "FileModesTypeDef",
    {
        "source": NotRequired[FileModeTypeEnumType],
        "destination": NotRequired[FileModeTypeEnumType],
        "base": NotRequired[FileModeTypeEnumType],
    },
)

FileSizesTypeDef = TypedDict(
    "FileSizesTypeDef",
    {
        "source": NotRequired[int],
        "destination": NotRequired[int],
        "base": NotRequired[int],
    },
)

FileTypeDef = TypedDict(
    "FileTypeDef",
    {
        "blobId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)

FolderTypeDef = TypedDict(
    "FolderTypeDef",
    {
        "treeId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
    },
)

GetApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "GetApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
    },
)

GetApprovalRuleTemplateOutputTypeDef = TypedDict(
    "GetApprovalRuleTemplateOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlobInputRequestTypeDef = TypedDict(
    "GetBlobInputRequestTypeDef",
    {
        "repositoryName": str,
        "blobId": str,
    },
)

GetBlobOutputTypeDef = TypedDict(
    "GetBlobOutputTypeDef",
    {
        "content": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBranchInputRequestTypeDef = TypedDict(
    "GetBranchInputRequestTypeDef",
    {
        "repositoryName": NotRequired[str],
        "branchName": NotRequired[str],
    },
)

GetBranchOutputTypeDef = TypedDict(
    "GetBranchOutputTypeDef",
    {
        "branch": "BranchInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentInputRequestTypeDef = TypedDict(
    "GetCommentInputRequestTypeDef",
    {
        "commentId": str,
    },
)

GetCommentOutputTypeDef = TypedDict(
    "GetCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentReactionsInputRequestTypeDef = TypedDict(
    "GetCommentReactionsInputRequestTypeDef",
    {
        "commentId": str,
        "reactionUserArn": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetCommentReactionsOutputTypeDef = TypedDict(
    "GetCommentReactionsOutputTypeDef",
    {
        "reactionsForComment": List["ReactionForCommentTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentsForComparedCommitInputRequestTypeDef = TypedDict(
    "GetCommentsForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "beforeCommitId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetCommentsForComparedCommitOutputTypeDef = TypedDict(
    "GetCommentsForComparedCommitOutputTypeDef",
    {
        "commentsForComparedCommitData": List["CommentsForComparedCommitTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommentsForPullRequestInputRequestTypeDef = TypedDict(
    "GetCommentsForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetCommentsForPullRequestOutputTypeDef = TypedDict(
    "GetCommentsForPullRequestOutputTypeDef",
    {
        "commentsForPullRequestData": List["CommentsForPullRequestTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCommitInputRequestTypeDef = TypedDict(
    "GetCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "commitId": str,
    },
)

GetCommitOutputTypeDef = TypedDict(
    "GetCommitOutputTypeDef",
    {
        "commit": "CommitTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDifferencesInputRequestTypeDef = TypedDict(
    "GetDifferencesInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitSpecifier": str,
        "beforeCommitSpecifier": NotRequired[str],
        "beforePath": NotRequired[str],
        "afterPath": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetDifferencesOutputTypeDef = TypedDict(
    "GetDifferencesOutputTypeDef",
    {
        "differences": List["DifferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFileInputRequestTypeDef = TypedDict(
    "GetFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "filePath": str,
        "commitSpecifier": NotRequired[str],
    },
)

GetFileOutputTypeDef = TypedDict(
    "GetFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
        "fileSize": int,
        "fileContent": bytes,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFolderInputRequestTypeDef = TypedDict(
    "GetFolderInputRequestTypeDef",
    {
        "repositoryName": str,
        "folderPath": str,
        "commitSpecifier": NotRequired[str],
    },
)

GetFolderOutputTypeDef = TypedDict(
    "GetFolderOutputTypeDef",
    {
        "commitId": str,
        "folderPath": str,
        "treeId": str,
        "subFolders": List["FolderTypeDef"],
        "files": List["FileTypeDef"],
        "symbolicLinks": List["SymbolicLinkTypeDef"],
        "subModules": List["SubModuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMergeCommitInputRequestTypeDef = TypedDict(
    "GetMergeCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
    },
)

GetMergeCommitOutputTypeDef = TypedDict(
    "GetMergeCommitOutputTypeDef",
    {
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "mergedCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMergeConflictsInputRequestTypeDef = TypedDict(
    "GetMergeConflictsInputRequestTypeDef",
    {
        "repositoryName": str,
        "destinationCommitSpecifier": str,
        "sourceCommitSpecifier": str,
        "mergeOption": MergeOptionTypeEnumType,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "maxConflictFiles": NotRequired[int],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "nextToken": NotRequired[str],
    },
)

GetMergeConflictsOutputTypeDef = TypedDict(
    "GetMergeConflictsOutputTypeDef",
    {
        "mergeable": bool,
        "destinationCommitId": str,
        "sourceCommitId": str,
        "baseCommitId": str,
        "conflictMetadataList": List["ConflictMetadataTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMergeOptionsInputRequestTypeDef = TypedDict(
    "GetMergeOptionsInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
    },
)

GetMergeOptionsOutputTypeDef = TypedDict(
    "GetMergeOptionsOutputTypeDef",
    {
        "mergeOptions": List[MergeOptionTypeEnumType],
        "sourceCommitId": str,
        "destinationCommitId": str,
        "baseCommitId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestApprovalStatesInputRequestTypeDef = TypedDict(
    "GetPullRequestApprovalStatesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestApprovalStatesOutputTypeDef = TypedDict(
    "GetPullRequestApprovalStatesOutputTypeDef",
    {
        "approvals": List["ApprovalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestInputRequestTypeDef = TypedDict(
    "GetPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
    },
)

GetPullRequestOutputTypeDef = TypedDict(
    "GetPullRequestOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPullRequestOverrideStateInputRequestTypeDef = TypedDict(
    "GetPullRequestOverrideStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
    },
)

GetPullRequestOverrideStateOutputTypeDef = TypedDict(
    "GetPullRequestOverrideStateOutputTypeDef",
    {
        "overridden": bool,
        "overrider": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryInputRequestTypeDef = TypedDict(
    "GetRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryOutputTypeDef = TypedDict(
    "GetRepositoryOutputTypeDef",
    {
        "repositoryMetadata": "RepositoryMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryTriggersInputRequestTypeDef = TypedDict(
    "GetRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
    },
)

GetRepositoryTriggersOutputTypeDef = TypedDict(
    "GetRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "triggers": List["RepositoryTriggerTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IsBinaryFileTypeDef = TypedDict(
    "IsBinaryFileTypeDef",
    {
        "source": NotRequired[bool],
        "destination": NotRequired[bool],
        "base": NotRequired[bool],
    },
)

ListApprovalRuleTemplatesInputRequestTypeDef = TypedDict(
    "ListApprovalRuleTemplatesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListApprovalRuleTemplatesOutputTypeDef = TypedDict(
    "ListApprovalRuleTemplatesOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryInputRequestTypeDef",
    {
        "repositoryName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef = TypedDict(
    "ListAssociatedApprovalRuleTemplatesForRepositoryOutputTypeDef",
    {
        "approvalRuleTemplateNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBranchesInputRequestTypeDef = TypedDict(
    "ListBranchesInputRequestTypeDef",
    {
        "repositoryName": str,
        "nextToken": NotRequired[str],
    },
)

ListBranchesOutputTypeDef = TypedDict(
    "ListBranchesOutputTypeDef",
    {
        "branches": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPullRequestsInputRequestTypeDef = TypedDict(
    "ListPullRequestsInputRequestTypeDef",
    {
        "repositoryName": str,
        "authorArn": NotRequired[str],
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPullRequestsOutputTypeDef = TypedDict(
    "ListPullRequestsOutputTypeDef",
    {
        "pullRequestIds": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListRepositoriesForApprovalRuleTemplateOutputTypeDef = TypedDict(
    "ListRepositoriesForApprovalRuleTemplateOutputTypeDef",
    {
        "repositoryNames": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInputRequestTypeDef = TypedDict(
    "ListRepositoriesInputRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "sortBy": NotRequired[SortByEnumType],
        "order": NotRequired[OrderEnumType],
    },
)

ListRepositoriesOutputTypeDef = TypedDict(
    "ListRepositoriesOutputTypeDef",
    {
        "repositories": List["RepositoryNameIdPairTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": Dict[str, str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "filePath": NotRequired[str],
        "filePosition": NotRequired[int],
        "relativeFileVersion": NotRequired[RelativeFileVersionEnumType],
    },
)

MergeBranchesByFastForwardInputRequestTypeDef = TypedDict(
    "MergeBranchesByFastForwardInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
    },
)

MergeBranchesByFastForwardOutputTypeDef = TypedDict(
    "MergeBranchesByFastForwardOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeBranchesBySquashInputRequestTypeDef = TypedDict(
    "MergeBranchesBySquashInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

MergeBranchesBySquashOutputTypeDef = TypedDict(
    "MergeBranchesBySquashOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeBranchesByThreeWayInputRequestTypeDef = TypedDict(
    "MergeBranchesByThreeWayInputRequestTypeDef",
    {
        "repositoryName": str,
        "sourceCommitSpecifier": str,
        "destinationCommitSpecifier": str,
        "targetBranch": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "commitMessage": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

MergeBranchesByThreeWayOutputTypeDef = TypedDict(
    "MergeBranchesByThreeWayOutputTypeDef",
    {
        "commitId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergeHunkDetailTypeDef = TypedDict(
    "MergeHunkDetailTypeDef",
    {
        "startLine": NotRequired[int],
        "endLine": NotRequired[int],
        "hunkContent": NotRequired[str],
    },
)

MergeHunkTypeDef = TypedDict(
    "MergeHunkTypeDef",
    {
        "isConflict": NotRequired[bool],
        "source": NotRequired["MergeHunkDetailTypeDef"],
        "destination": NotRequired["MergeHunkDetailTypeDef"],
        "base": NotRequired["MergeHunkDetailTypeDef"],
    },
)

MergeMetadataTypeDef = TypedDict(
    "MergeMetadataTypeDef",
    {
        "isMerged": NotRequired[bool],
        "mergedBy": NotRequired[str],
        "mergeCommitId": NotRequired[str],
        "mergeOption": NotRequired[MergeOptionTypeEnumType],
    },
)

MergeOperationsTypeDef = TypedDict(
    "MergeOperationsTypeDef",
    {
        "source": NotRequired[ChangeTypeEnumType],
        "destination": NotRequired[ChangeTypeEnumType],
    },
)

MergePullRequestByFastForwardInputRequestTypeDef = TypedDict(
    "MergePullRequestByFastForwardInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
    },
)

MergePullRequestByFastForwardOutputTypeDef = TypedDict(
    "MergePullRequestByFastForwardOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergePullRequestBySquashInputRequestTypeDef = TypedDict(
    "MergePullRequestBySquashInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "commitMessage": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

MergePullRequestBySquashOutputTypeDef = TypedDict(
    "MergePullRequestBySquashOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MergePullRequestByThreeWayInputRequestTypeDef = TypedDict(
    "MergePullRequestByThreeWayInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "sourceCommitId": NotRequired[str],
        "conflictDetailLevel": NotRequired[ConflictDetailLevelTypeEnumType],
        "conflictResolutionStrategy": NotRequired[ConflictResolutionStrategyTypeEnumType],
        "commitMessage": NotRequired[str],
        "authorName": NotRequired[str],
        "email": NotRequired[str],
        "keepEmptyFolders": NotRequired[bool],
        "conflictResolution": NotRequired["ConflictResolutionTypeDef"],
    },
)

MergePullRequestByThreeWayOutputTypeDef = TypedDict(
    "MergePullRequestByThreeWayOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ObjectTypesTypeDef = TypedDict(
    "ObjectTypesTypeDef",
    {
        "source": NotRequired[ObjectTypeEnumType],
        "destination": NotRequired[ObjectTypeEnumType],
        "base": NotRequired[ObjectTypeEnumType],
    },
)

OriginApprovalRuleTemplateTypeDef = TypedDict(
    "OriginApprovalRuleTemplateTypeDef",
    {
        "approvalRuleTemplateId": NotRequired[str],
        "approvalRuleTemplateName": NotRequired[str],
    },
)

OverridePullRequestApprovalRulesInputRequestTypeDef = TypedDict(
    "OverridePullRequestApprovalRulesInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "overrideStatus": OverrideStatusType,
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

PostCommentForComparedCommitInputRequestTypeDef = TypedDict(
    "PostCommentForComparedCommitInputRequestTypeDef",
    {
        "repositoryName": str,
        "afterCommitId": str,
        "content": str,
        "beforeCommitId": NotRequired[str],
        "location": NotRequired["LocationTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

PostCommentForComparedCommitOutputTypeDef = TypedDict(
    "PostCommentForComparedCommitOutputTypeDef",
    {
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PostCommentForPullRequestInputRequestTypeDef = TypedDict(
    "PostCommentForPullRequestInputRequestTypeDef",
    {
        "pullRequestId": str,
        "repositoryName": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "content": str,
        "location": NotRequired["LocationTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

PostCommentForPullRequestOutputTypeDef = TypedDict(
    "PostCommentForPullRequestOutputTypeDef",
    {
        "repositoryName": str,
        "pullRequestId": str,
        "beforeCommitId": str,
        "afterCommitId": str,
        "beforeBlobId": str,
        "afterBlobId": str,
        "location": "LocationTypeDef",
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PostCommentReplyInputRequestTypeDef = TypedDict(
    "PostCommentReplyInputRequestTypeDef",
    {
        "inReplyTo": str,
        "content": str,
        "clientRequestToken": NotRequired[str],
    },
)

PostCommentReplyOutputTypeDef = TypedDict(
    "PostCommentReplyOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PullRequestCreatedEventMetadataTypeDef = TypedDict(
    "PullRequestCreatedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "sourceCommitId": NotRequired[str],
        "destinationCommitId": NotRequired[str],
        "mergeBase": NotRequired[str],
    },
)

PullRequestEventTypeDef = TypedDict(
    "PullRequestEventTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "eventDate": NotRequired[datetime],
        "pullRequestEventType": NotRequired[PullRequestEventTypeType],
        "actorArn": NotRequired[str],
        "pullRequestCreatedEventMetadata": NotRequired["PullRequestCreatedEventMetadataTypeDef"],
        "pullRequestStatusChangedEventMetadata": NotRequired[
            "PullRequestStatusChangedEventMetadataTypeDef"
        ],
        "pullRequestSourceReferenceUpdatedEventMetadata": NotRequired[
            "PullRequestSourceReferenceUpdatedEventMetadataTypeDef"
        ],
        "pullRequestMergedStateChangedEventMetadata": NotRequired[
            "PullRequestMergedStateChangedEventMetadataTypeDef"
        ],
        "approvalRuleEventMetadata": NotRequired["ApprovalRuleEventMetadataTypeDef"],
        "approvalStateChangedEventMetadata": NotRequired[
            "ApprovalStateChangedEventMetadataTypeDef"
        ],
        "approvalRuleOverriddenEventMetadata": NotRequired[
            "ApprovalRuleOverriddenEventMetadataTypeDef"
        ],
    },
)

PullRequestMergedStateChangedEventMetadataTypeDef = TypedDict(
    "PullRequestMergedStateChangedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "destinationReference": NotRequired[str],
        "mergeMetadata": NotRequired["MergeMetadataTypeDef"],
    },
)

PullRequestSourceReferenceUpdatedEventMetadataTypeDef = TypedDict(
    "PullRequestSourceReferenceUpdatedEventMetadataTypeDef",
    {
        "repositoryName": NotRequired[str],
        "beforeCommitId": NotRequired[str],
        "afterCommitId": NotRequired[str],
        "mergeBase": NotRequired[str],
    },
)

PullRequestStatusChangedEventMetadataTypeDef = TypedDict(
    "PullRequestStatusChangedEventMetadataTypeDef",
    {
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
    },
)

PullRequestTargetTypeDef = TypedDict(
    "PullRequestTargetTypeDef",
    {
        "repositoryName": NotRequired[str],
        "sourceReference": NotRequired[str],
        "destinationReference": NotRequired[str],
        "destinationCommit": NotRequired[str],
        "sourceCommit": NotRequired[str],
        "mergeBase": NotRequired[str],
        "mergeMetadata": NotRequired["MergeMetadataTypeDef"],
    },
)

PullRequestTypeDef = TypedDict(
    "PullRequestTypeDef",
    {
        "pullRequestId": NotRequired[str],
        "title": NotRequired[str],
        "description": NotRequired[str],
        "lastActivityDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "pullRequestStatus": NotRequired[PullRequestStatusEnumType],
        "authorArn": NotRequired[str],
        "pullRequestTargets": NotRequired[List["PullRequestTargetTypeDef"]],
        "clientRequestToken": NotRequired[str],
        "revisionId": NotRequired[str],
        "approvalRules": NotRequired[List["ApprovalRuleTypeDef"]],
    },
)

PutCommentReactionInputRequestTypeDef = TypedDict(
    "PutCommentReactionInputRequestTypeDef",
    {
        "commentId": str,
        "reactionValue": str,
    },
)

PutFileEntryTypeDef = TypedDict(
    "PutFileEntryTypeDef",
    {
        "filePath": str,
        "fileMode": NotRequired[FileModeTypeEnumType],
        "fileContent": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "sourceFile": NotRequired["SourceFileSpecifierTypeDef"],
    },
)

PutFileInputRequestTypeDef = TypedDict(
    "PutFileInputRequestTypeDef",
    {
        "repositoryName": str,
        "branchName": str,
        "fileContent": Union[bytes, IO[bytes], StreamingBody],
        "filePath": str,
        "fileMode": NotRequired[FileModeTypeEnumType],
        "parentCommitId": NotRequired[str],
        "commitMessage": NotRequired[str],
        "name": NotRequired[str],
        "email": NotRequired[str],
    },
)

PutFileOutputTypeDef = TypedDict(
    "PutFileOutputTypeDef",
    {
        "commitId": str,
        "blobId": str,
        "treeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryTriggersInputRequestTypeDef = TypedDict(
    "PutRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": Sequence["RepositoryTriggerTypeDef"],
    },
)

PutRepositoryTriggersOutputTypeDef = TypedDict(
    "PutRepositoryTriggersOutputTypeDef",
    {
        "configurationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReactionForCommentTypeDef = TypedDict(
    "ReactionForCommentTypeDef",
    {
        "reaction": NotRequired["ReactionValueFormatsTypeDef"],
        "reactionUsers": NotRequired[List[str]],
        "reactionsFromDeletedUsersCount": NotRequired[int],
    },
)

ReactionValueFormatsTypeDef = TypedDict(
    "ReactionValueFormatsTypeDef",
    {
        "emoji": NotRequired[str],
        "shortCode": NotRequired[str],
        "unicode": NotRequired[str],
    },
)

ReplaceContentEntryTypeDef = TypedDict(
    "ReplaceContentEntryTypeDef",
    {
        "filePath": str,
        "replacementType": ReplacementTypeEnumType,
        "content": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)

RepositoryMetadataTypeDef = TypedDict(
    "RepositoryMetadataTypeDef",
    {
        "accountId": NotRequired[str],
        "repositoryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryDescription": NotRequired[str],
        "defaultBranch": NotRequired[str],
        "lastModifiedDate": NotRequired[datetime],
        "creationDate": NotRequired[datetime],
        "cloneUrlHttp": NotRequired[str],
        "cloneUrlSsh": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

RepositoryNameIdPairTypeDef = TypedDict(
    "RepositoryNameIdPairTypeDef",
    {
        "repositoryName": NotRequired[str],
        "repositoryId": NotRequired[str],
    },
)

RepositoryTriggerExecutionFailureTypeDef = TypedDict(
    "RepositoryTriggerExecutionFailureTypeDef",
    {
        "trigger": NotRequired[str],
        "failureMessage": NotRequired[str],
    },
)

RepositoryTriggerTypeDef = TypedDict(
    "RepositoryTriggerTypeDef",
    {
        "name": str,
        "destinationArn": str,
        "events": List[RepositoryTriggerEventEnumType],
        "customData": NotRequired[str],
        "branches": NotRequired[List[str]],
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

SetFileModeEntryTypeDef = TypedDict(
    "SetFileModeEntryTypeDef",
    {
        "filePath": str,
        "fileMode": FileModeTypeEnumType,
    },
)

SourceFileSpecifierTypeDef = TypedDict(
    "SourceFileSpecifierTypeDef",
    {
        "filePath": str,
        "isMove": NotRequired[bool],
    },
)

SubModuleTypeDef = TypedDict(
    "SubModuleTypeDef",
    {
        "commitId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
    },
)

SymbolicLinkTypeDef = TypedDict(
    "SymbolicLinkTypeDef",
    {
        "blobId": NotRequired[str],
        "absolutePath": NotRequired[str],
        "relativePath": NotRequired[str],
        "fileMode": NotRequired[FileModeTypeEnumType],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

TargetTypeDef = TypedDict(
    "TargetTypeDef",
    {
        "repositoryName": str,
        "sourceReference": str,
        "destinationReference": NotRequired[str],
    },
)

TestRepositoryTriggersInputRequestTypeDef = TypedDict(
    "TestRepositoryTriggersInputRequestTypeDef",
    {
        "repositoryName": str,
        "triggers": Sequence["RepositoryTriggerTypeDef"],
    },
)

TestRepositoryTriggersOutputTypeDef = TypedDict(
    "TestRepositoryTriggersOutputTypeDef",
    {
        "successfulExecutions": List[str],
        "failedExecutions": List["RepositoryTriggerExecutionFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateApprovalRuleTemplateContentInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "newRuleContent": str,
        "existingRuleContentSha256": NotRequired[str],
    },
)

UpdateApprovalRuleTemplateContentOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateContentOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionInputRequestTypeDef",
    {
        "approvalRuleTemplateName": str,
        "approvalRuleTemplateDescription": str,
    },
)

UpdateApprovalRuleTemplateDescriptionOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateDescriptionOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateApprovalRuleTemplateNameInputRequestTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameInputRequestTypeDef",
    {
        "oldApprovalRuleTemplateName": str,
        "newApprovalRuleTemplateName": str,
    },
)

UpdateApprovalRuleTemplateNameOutputTypeDef = TypedDict(
    "UpdateApprovalRuleTemplateNameOutputTypeDef",
    {
        "approvalRuleTemplate": "ApprovalRuleTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCommentInputRequestTypeDef = TypedDict(
    "UpdateCommentInputRequestTypeDef",
    {
        "commentId": str,
        "content": str,
    },
)

UpdateCommentOutputTypeDef = TypedDict(
    "UpdateCommentOutputTypeDef",
    {
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDefaultBranchInputRequestTypeDef = TypedDict(
    "UpdateDefaultBranchInputRequestTypeDef",
    {
        "repositoryName": str,
        "defaultBranchName": str,
    },
)

UpdatePullRequestApprovalRuleContentInputRequestTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentInputRequestTypeDef",
    {
        "pullRequestId": str,
        "approvalRuleName": str,
        "newRuleContent": str,
        "existingRuleContentSha256": NotRequired[str],
    },
)

UpdatePullRequestApprovalRuleContentOutputTypeDef = TypedDict(
    "UpdatePullRequestApprovalRuleContentOutputTypeDef",
    {
        "approvalRule": "ApprovalRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestApprovalStateInputRequestTypeDef = TypedDict(
    "UpdatePullRequestApprovalStateInputRequestTypeDef",
    {
        "pullRequestId": str,
        "revisionId": str,
        "approvalState": ApprovalStateType,
    },
)

UpdatePullRequestDescriptionInputRequestTypeDef = TypedDict(
    "UpdatePullRequestDescriptionInputRequestTypeDef",
    {
        "pullRequestId": str,
        "description": str,
    },
)

UpdatePullRequestDescriptionOutputTypeDef = TypedDict(
    "UpdatePullRequestDescriptionOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestStatusInputRequestTypeDef = TypedDict(
    "UpdatePullRequestStatusInputRequestTypeDef",
    {
        "pullRequestId": str,
        "pullRequestStatus": PullRequestStatusEnumType,
    },
)

UpdatePullRequestStatusOutputTypeDef = TypedDict(
    "UpdatePullRequestStatusOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePullRequestTitleInputRequestTypeDef = TypedDict(
    "UpdatePullRequestTitleInputRequestTypeDef",
    {
        "pullRequestId": str,
        "title": str,
    },
)

UpdatePullRequestTitleOutputTypeDef = TypedDict(
    "UpdatePullRequestTitleOutputTypeDef",
    {
        "pullRequest": "PullRequestTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRepositoryDescriptionInputRequestTypeDef = TypedDict(
    "UpdateRepositoryDescriptionInputRequestTypeDef",
    {
        "repositoryName": str,
        "repositoryDescription": NotRequired[str],
    },
)

UpdateRepositoryNameInputRequestTypeDef = TypedDict(
    "UpdateRepositoryNameInputRequestTypeDef",
    {
        "oldName": str,
        "newName": str,
    },
)

UserInfoTypeDef = TypedDict(
    "UserInfoTypeDef",
    {
        "name": NotRequired[str],
        "email": NotRequired[str],
        "date": NotRequired[str],
    },
)
