"""
Type annotations for codeguru-reviewer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.type_defs import AssociateRepositoryRequestRequestTypeDef

    data: AssociateRepositoryRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AnalysisTypeType,
    EncryptionOptionType,
    JobStateType,
    ProviderTypeType,
    ReactionType,
    RecommendationCategoryType,
    RepositoryAssociationStateType,
    SeverityType,
    TypeType,
    VendorNameType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRepositoryRequestRequestTypeDef",
    "AssociateRepositoryResponseTypeDef",
    "BranchDiffSourceCodeTypeTypeDef",
    "CodeArtifactsTypeDef",
    "CodeCommitRepositoryTypeDef",
    "CodeReviewSummaryTypeDef",
    "CodeReviewTypeDef",
    "CodeReviewTypeTypeDef",
    "CommitDiffSourceCodeTypeTypeDef",
    "CreateCodeReviewRequestRequestTypeDef",
    "CreateCodeReviewResponseTypeDef",
    "DescribeCodeReviewRequestRequestTypeDef",
    "DescribeCodeReviewResponseTypeDef",
    "DescribeRecommendationFeedbackRequestRequestTypeDef",
    "DescribeRecommendationFeedbackResponseTypeDef",
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    "DescribeRepositoryAssociationResponseTypeDef",
    "DisassociateRepositoryRequestRequestTypeDef",
    "DisassociateRepositoryResponseTypeDef",
    "EventInfoTypeDef",
    "KMSKeyDetailsTypeDef",
    "ListCodeReviewsRequestRequestTypeDef",
    "ListCodeReviewsResponseTypeDef",
    "ListRecommendationFeedbackRequestRequestTypeDef",
    "ListRecommendationFeedbackResponseTypeDef",
    "ListRecommendationsRequestRequestTypeDef",
    "ListRecommendationsResponseTypeDef",
    "ListRepositoryAssociationsRequestRequestTypeDef",
    "ListRepositoryAssociationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsSummaryTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "PutRecommendationFeedbackRequestRequestTypeDef",
    "RecommendationFeedbackSummaryTypeDef",
    "RecommendationFeedbackTypeDef",
    "RecommendationSummaryTypeDef",
    "RepositoryAnalysisTypeDef",
    "RepositoryAssociationSummaryTypeDef",
    "RepositoryAssociationTypeDef",
    "RepositoryHeadSourceCodeTypeTypeDef",
    "RepositoryTypeDef",
    "RequestMetadataTypeDef",
    "ResponseMetadataTypeDef",
    "RuleMetadataTypeDef",
    "S3BucketRepositoryTypeDef",
    "S3RepositoryDetailsTypeDef",
    "S3RepositoryTypeDef",
    "SourceCodeTypeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThirdPartySourceRepositoryTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "WaiterConfigTypeDef",
)

AssociateRepositoryRequestRequestTypeDef = TypedDict(
    "AssociateRepositoryRequestRequestTypeDef",
    {
        "Repository": "RepositoryTypeDef",
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "KMSKeyDetails": NotRequired["KMSKeyDetailsTypeDef"],
    },
)

AssociateRepositoryResponseTypeDef = TypedDict(
    "AssociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BranchDiffSourceCodeTypeTypeDef = TypedDict(
    "BranchDiffSourceCodeTypeTypeDef",
    {
        "SourceBranchName": str,
        "DestinationBranchName": str,
    },
)

CodeArtifactsTypeDef = TypedDict(
    "CodeArtifactsTypeDef",
    {
        "SourceCodeArtifactsObjectKey": str,
        "BuildArtifactsObjectKey": NotRequired[str],
    },
)

CodeCommitRepositoryTypeDef = TypedDict(
    "CodeCommitRepositoryTypeDef",
    {
        "Name": str,
    },
)

CodeReviewSummaryTypeDef = TypedDict(
    "CodeReviewSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "CodeReviewArn": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[JobStateType],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "Type": NotRequired[TypeType],
        "PullRequestId": NotRequired[str],
        "MetricsSummary": NotRequired["MetricsSummaryTypeDef"],
        "SourceCodeType": NotRequired["SourceCodeTypeTypeDef"],
    },
)

CodeReviewTypeDef = TypedDict(
    "CodeReviewTypeDef",
    {
        "Name": NotRequired[str],
        "CodeReviewArn": NotRequired[str],
        "RepositoryName": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[JobStateType],
        "StateReason": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "Type": NotRequired[TypeType],
        "PullRequestId": NotRequired[str],
        "SourceCodeType": NotRequired["SourceCodeTypeTypeDef"],
        "AssociationArn": NotRequired[str],
        "Metrics": NotRequired["MetricsTypeDef"],
        "AnalysisTypes": NotRequired[List[AnalysisTypeType]],
    },
)

CodeReviewTypeTypeDef = TypedDict(
    "CodeReviewTypeTypeDef",
    {
        "RepositoryAnalysis": "RepositoryAnalysisTypeDef",
        "AnalysisTypes": NotRequired[Sequence[AnalysisTypeType]],
    },
)

CommitDiffSourceCodeTypeTypeDef = TypedDict(
    "CommitDiffSourceCodeTypeTypeDef",
    {
        "SourceCommit": NotRequired[str],
        "DestinationCommit": NotRequired[str],
        "MergeBaseCommit": NotRequired[str],
    },
)

CreateCodeReviewRequestRequestTypeDef = TypedDict(
    "CreateCodeReviewRequestRequestTypeDef",
    {
        "Name": str,
        "RepositoryAssociationArn": str,
        "Type": "CodeReviewTypeTypeDef",
        "ClientRequestToken": NotRequired[str],
    },
)

CreateCodeReviewResponseTypeDef = TypedDict(
    "CreateCodeReviewResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCodeReviewRequestRequestTypeDef = TypedDict(
    "DescribeCodeReviewRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
    },
)

DescribeCodeReviewResponseTypeDef = TypedDict(
    "DescribeCodeReviewResponseTypeDef",
    {
        "CodeReview": "CodeReviewTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "DescribeRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "UserId": NotRequired[str],
    },
)

DescribeRecommendationFeedbackResponseTypeDef = TypedDict(
    "DescribeRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedback": "RecommendationFeedbackTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoryAssociationRequestRequestTypeDef = TypedDict(
    "DescribeRepositoryAssociationRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

DescribeRepositoryAssociationResponseTypeDef = TypedDict(
    "DescribeRepositoryAssociationResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateRepositoryRequestRequestTypeDef = TypedDict(
    "DisassociateRepositoryRequestRequestTypeDef",
    {
        "AssociationArn": str,
    },
)

DisassociateRepositoryResponseTypeDef = TypedDict(
    "DisassociateRepositoryResponseTypeDef",
    {
        "RepositoryAssociation": "RepositoryAssociationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EventInfoTypeDef = TypedDict(
    "EventInfoTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[str],
    },
)

KMSKeyDetailsTypeDef = TypedDict(
    "KMSKeyDetailsTypeDef",
    {
        "KMSKeyId": NotRequired[str],
        "EncryptionOption": NotRequired[EncryptionOptionType],
    },
)

ListCodeReviewsRequestRequestTypeDef = TypedDict(
    "ListCodeReviewsRequestRequestTypeDef",
    {
        "Type": TypeType,
        "ProviderTypes": NotRequired[Sequence[ProviderTypeType]],
        "States": NotRequired[Sequence[JobStateType]],
        "RepositoryNames": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCodeReviewsResponseTypeDef = TypedDict(
    "ListCodeReviewsResponseTypeDef",
    {
        "CodeReviewSummaries": List["CodeReviewSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "ListRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "UserIds": NotRequired[Sequence[str]],
        "RecommendationIds": NotRequired[Sequence[str]],
    },
)

ListRecommendationFeedbackResponseTypeDef = TypedDict(
    "ListRecommendationFeedbackResponseTypeDef",
    {
        "RecommendationFeedbackSummaries": List["RecommendationFeedbackSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecommendationsRequestRequestTypeDef = TypedDict(
    "ListRecommendationsRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListRecommendationsResponseTypeDef = TypedDict(
    "ListRecommendationsResponseTypeDef",
    {
        "RecommendationSummaries": List["RecommendationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoryAssociationsRequestRequestTypeDef = TypedDict(
    "ListRepositoryAssociationsRequestRequestTypeDef",
    {
        "ProviderTypes": NotRequired[Sequence[ProviderTypeType]],
        "States": NotRequired[Sequence[RepositoryAssociationStateType]],
        "Names": NotRequired[Sequence[str]],
        "Owners": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRepositoryAssociationsResponseTypeDef = TypedDict(
    "ListRepositoryAssociationsResponseTypeDef",
    {
        "RepositoryAssociationSummaries": List["RepositoryAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricsSummaryTypeDef = TypedDict(
    "MetricsSummaryTypeDef",
    {
        "MeteredLinesOfCodeCount": NotRequired[int],
        "FindingsCount": NotRequired[int],
    },
)

MetricsTypeDef = TypedDict(
    "MetricsTypeDef",
    {
        "MeteredLinesOfCodeCount": NotRequired[int],
        "FindingsCount": NotRequired[int],
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

PutRecommendationFeedbackRequestRequestTypeDef = TypedDict(
    "PutRecommendationFeedbackRequestRequestTypeDef",
    {
        "CodeReviewArn": str,
        "RecommendationId": str,
        "Reactions": Sequence[ReactionType],
    },
)

RecommendationFeedbackSummaryTypeDef = TypedDict(
    "RecommendationFeedbackSummaryTypeDef",
    {
        "RecommendationId": NotRequired[str],
        "Reactions": NotRequired[List[ReactionType]],
        "UserId": NotRequired[str],
    },
)

RecommendationFeedbackTypeDef = TypedDict(
    "RecommendationFeedbackTypeDef",
    {
        "CodeReviewArn": NotRequired[str],
        "RecommendationId": NotRequired[str],
        "Reactions": NotRequired[List[ReactionType]],
        "UserId": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "LastUpdatedTimeStamp": NotRequired[datetime],
    },
)

RecommendationSummaryTypeDef = TypedDict(
    "RecommendationSummaryTypeDef",
    {
        "FilePath": NotRequired[str],
        "RecommendationId": NotRequired[str],
        "StartLine": NotRequired[int],
        "EndLine": NotRequired[int],
        "Description": NotRequired[str],
        "RecommendationCategory": NotRequired[RecommendationCategoryType],
        "RuleMetadata": NotRequired["RuleMetadataTypeDef"],
        "Severity": NotRequired[SeverityType],
    },
)

RepositoryAnalysisTypeDef = TypedDict(
    "RepositoryAnalysisTypeDef",
    {
        "RepositoryHead": NotRequired["RepositoryHeadSourceCodeTypeTypeDef"],
        "SourceCodeType": NotRequired["SourceCodeTypeTypeDef"],
    },
)

RepositoryAssociationSummaryTypeDef = TypedDict(
    "RepositoryAssociationSummaryTypeDef",
    {
        "AssociationArn": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "AssociationId": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[RepositoryAssociationStateType],
    },
)

RepositoryAssociationTypeDef = TypedDict(
    "RepositoryAssociationTypeDef",
    {
        "AssociationId": NotRequired[str],
        "AssociationArn": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "Name": NotRequired[str],
        "Owner": NotRequired[str],
        "ProviderType": NotRequired[ProviderTypeType],
        "State": NotRequired[RepositoryAssociationStateType],
        "StateReason": NotRequired[str],
        "LastUpdatedTimeStamp": NotRequired[datetime],
        "CreatedTimeStamp": NotRequired[datetime],
        "KMSKeyDetails": NotRequired["KMSKeyDetailsTypeDef"],
        "S3RepositoryDetails": NotRequired["S3RepositoryDetailsTypeDef"],
    },
)

RepositoryHeadSourceCodeTypeTypeDef = TypedDict(
    "RepositoryHeadSourceCodeTypeTypeDef",
    {
        "BranchName": str,
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "CodeCommit": NotRequired["CodeCommitRepositoryTypeDef"],
        "Bitbucket": NotRequired["ThirdPartySourceRepositoryTypeDef"],
        "GitHubEnterpriseServer": NotRequired["ThirdPartySourceRepositoryTypeDef"],
        "S3Bucket": NotRequired["S3RepositoryTypeDef"],
    },
)

RequestMetadataTypeDef = TypedDict(
    "RequestMetadataTypeDef",
    {
        "RequestId": NotRequired[str],
        "Requester": NotRequired[str],
        "EventInfo": NotRequired["EventInfoTypeDef"],
        "VendorName": NotRequired[VendorNameType],
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

RuleMetadataTypeDef = TypedDict(
    "RuleMetadataTypeDef",
    {
        "RuleId": NotRequired[str],
        "RuleName": NotRequired[str],
        "ShortDescription": NotRequired[str],
        "LongDescription": NotRequired[str],
        "RuleTags": NotRequired[List[str]],
    },
)

S3BucketRepositoryTypeDef = TypedDict(
    "S3BucketRepositoryTypeDef",
    {
        "Name": str,
        "Details": NotRequired["S3RepositoryDetailsTypeDef"],
    },
)

S3RepositoryDetailsTypeDef = TypedDict(
    "S3RepositoryDetailsTypeDef",
    {
        "BucketName": NotRequired[str],
        "CodeArtifacts": NotRequired["CodeArtifactsTypeDef"],
    },
)

S3RepositoryTypeDef = TypedDict(
    "S3RepositoryTypeDef",
    {
        "Name": str,
        "BucketName": str,
    },
)

SourceCodeTypeTypeDef = TypedDict(
    "SourceCodeTypeTypeDef",
    {
        "CommitDiff": NotRequired["CommitDiffSourceCodeTypeTypeDef"],
        "RepositoryHead": NotRequired["RepositoryHeadSourceCodeTypeTypeDef"],
        "BranchDiff": NotRequired["BranchDiffSourceCodeTypeTypeDef"],
        "S3BucketRepository": NotRequired["S3BucketRepositoryTypeDef"],
        "RequestMetadata": NotRequired["RequestMetadataTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "Tags": Mapping[str, str],
    },
)

ThirdPartySourceRepositoryTypeDef = TypedDict(
    "ThirdPartySourceRepositoryTypeDef",
    {
        "Name": str,
        "ConnectionArn": str,
        "Owner": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "TagKeys": Sequence[str],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
