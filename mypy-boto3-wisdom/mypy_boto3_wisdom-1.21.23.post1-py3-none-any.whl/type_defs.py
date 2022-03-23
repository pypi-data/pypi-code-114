"""
Type annotations for wisdom service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wisdom/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wisdom.type_defs import AppIntegrationsConfigurationTypeDef

    data: AppIntegrationsConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AssistantStatusType,
    ContentStatusType,
    KnowledgeBaseStatusType,
    KnowledgeBaseTypeType,
    RelevanceLevelType,
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
    "AppIntegrationsConfigurationTypeDef",
    "AssistantAssociationDataTypeDef",
    "AssistantAssociationInputDataTypeDef",
    "AssistantAssociationOutputDataTypeDef",
    "AssistantAssociationSummaryTypeDef",
    "AssistantDataTypeDef",
    "AssistantSummaryTypeDef",
    "ContentDataTypeDef",
    "ContentReferenceTypeDef",
    "ContentSummaryTypeDef",
    "CreateAssistantAssociationRequestRequestTypeDef",
    "CreateAssistantAssociationResponseTypeDef",
    "CreateAssistantRequestRequestTypeDef",
    "CreateAssistantResponseTypeDef",
    "CreateContentRequestRequestTypeDef",
    "CreateContentResponseTypeDef",
    "CreateKnowledgeBaseRequestRequestTypeDef",
    "CreateKnowledgeBaseResponseTypeDef",
    "CreateSessionRequestRequestTypeDef",
    "CreateSessionResponseTypeDef",
    "DeleteAssistantAssociationRequestRequestTypeDef",
    "DeleteAssistantRequestRequestTypeDef",
    "DeleteContentRequestRequestTypeDef",
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    "DocumentTextTypeDef",
    "DocumentTypeDef",
    "FilterTypeDef",
    "GetAssistantAssociationRequestRequestTypeDef",
    "GetAssistantAssociationResponseTypeDef",
    "GetAssistantRequestRequestTypeDef",
    "GetAssistantResponseTypeDef",
    "GetContentRequestRequestTypeDef",
    "GetContentResponseTypeDef",
    "GetContentSummaryRequestRequestTypeDef",
    "GetContentSummaryResponseTypeDef",
    "GetKnowledgeBaseRequestRequestTypeDef",
    "GetKnowledgeBaseResponseTypeDef",
    "GetRecommendationsRequestRequestTypeDef",
    "GetRecommendationsResponseTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "HighlightTypeDef",
    "KnowledgeBaseAssociationDataTypeDef",
    "KnowledgeBaseDataTypeDef",
    "KnowledgeBaseSummaryTypeDef",
    "ListAssistantAssociationsRequestRequestTypeDef",
    "ListAssistantAssociationsResponseTypeDef",
    "ListAssistantsRequestRequestTypeDef",
    "ListAssistantsResponseTypeDef",
    "ListContentsRequestRequestTypeDef",
    "ListContentsResponseTypeDef",
    "ListKnowledgeBasesRequestRequestTypeDef",
    "ListKnowledgeBasesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NotifyRecommendationsReceivedErrorTypeDef",
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    "NotifyRecommendationsReceivedResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryAssistantRequestRequestTypeDef",
    "QueryAssistantResponseTypeDef",
    "RecommendationDataTypeDef",
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "RenderingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "ResultDataTypeDef",
    "SearchContentRequestRequestTypeDef",
    "SearchContentResponseTypeDef",
    "SearchExpressionTypeDef",
    "SearchSessionsRequestRequestTypeDef",
    "SearchSessionsResponseTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "SessionDataTypeDef",
    "SessionSummaryTypeDef",
    "SourceConfigurationTypeDef",
    "StartContentUploadRequestRequestTypeDef",
    "StartContentUploadResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateContentRequestRequestTypeDef",
    "UpdateContentResponseTypeDef",
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
)

AppIntegrationsConfigurationTypeDef = TypedDict(
    "AppIntegrationsConfigurationTypeDef",
    {
        "appIntegrationArn": str,
        "objectFields": Sequence[str],
    },
)

AssistantAssociationDataTypeDef = TypedDict(
    "AssistantAssociationDataTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": "AssistantAssociationOutputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": NotRequired[Dict[str, str]],
    },
)

AssistantAssociationInputDataTypeDef = TypedDict(
    "AssistantAssociationInputDataTypeDef",
    {
        "knowledgeBaseId": NotRequired[str],
    },
)

AssistantAssociationOutputDataTypeDef = TypedDict(
    "AssistantAssociationOutputDataTypeDef",
    {
        "knowledgeBaseAssociation": NotRequired["KnowledgeBaseAssociationDataTypeDef"],
    },
)

AssistantAssociationSummaryTypeDef = TypedDict(
    "AssistantAssociationSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantAssociationArn": str,
        "assistantAssociationId": str,
        "assistantId": str,
        "associationData": "AssistantAssociationOutputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
        "tags": NotRequired[Dict[str, str]],
    },
)

AssistantDataTypeDef = TypedDict(
    "AssistantDataTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "tags": NotRequired[Dict[str, str]],
    },
)

AssistantSummaryTypeDef = TypedDict(
    "AssistantSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "name": str,
        "status": AssistantStatusType,
        "type": Literal["AGENT"],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "tags": NotRequired[Dict[str, str]],
    },
)

ContentDataTypeDef = TypedDict(
    "ContentDataTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
        "url": str,
        "urlExpiry": datetime,
        "linkOutUri": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ContentReferenceTypeDef = TypedDict(
    "ContentReferenceTypeDef",
    {
        "contentArn": NotRequired[str],
        "contentId": NotRequired[str],
        "knowledgeBaseArn": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
    },
)

ContentSummaryTypeDef = TypedDict(
    "ContentSummaryTypeDef",
    {
        "contentArn": str,
        "contentId": str,
        "contentType": str,
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "metadata": Dict[str, str],
        "name": str,
        "revisionId": str,
        "status": ContentStatusType,
        "title": str,
        "tags": NotRequired[Dict[str, str]],
    },
)

CreateAssistantAssociationRequestRequestTypeDef = TypedDict(
    "CreateAssistantAssociationRequestRequestTypeDef",
    {
        "assistantId": str,
        "association": "AssistantAssociationInputDataTypeDef",
        "associationType": Literal["KNOWLEDGE_BASE"],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssistantAssociationResponseTypeDef = TypedDict(
    "CreateAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": "AssistantAssociationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssistantRequestRequestTypeDef = TypedDict(
    "CreateAssistantRequestRequestTypeDef",
    {
        "name": str,
        "type": Literal["AGENT"],
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssistantResponseTypeDef = TypedDict(
    "CreateAssistantResponseTypeDef",
    {
        "assistant": "AssistantDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContentRequestRequestTypeDef = TypedDict(
    "CreateContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "name": str,
        "uploadId": str,
        "clientToken": NotRequired[str],
        "metadata": NotRequired[Mapping[str, str]],
        "overrideLinkOutUri": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "title": NotRequired[str],
    },
)

CreateContentResponseTypeDef = TypedDict(
    "CreateContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "CreateKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "renderingConfiguration": NotRequired["RenderingConfigurationTypeDef"],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "sourceConfiguration": NotRequired["SourceConfigurationTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateKnowledgeBaseResponseTypeDef = TypedDict(
    "CreateKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSessionRequestRequestTypeDef = TypedDict(
    "CreateSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "name": str,
        "clientToken": NotRequired[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateSessionResponseTypeDef = TypedDict(
    "CreateSessionResponseTypeDef",
    {
        "session": "SessionDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAssistantAssociationRequestRequestTypeDef = TypedDict(
    "DeleteAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

DeleteAssistantRequestRequestTypeDef = TypedDict(
    "DeleteAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

DeleteContentRequestRequestTypeDef = TypedDict(
    "DeleteContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

DeleteKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "DeleteKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

DocumentTextTypeDef = TypedDict(
    "DocumentTextTypeDef",
    {
        "highlights": NotRequired[List["HighlightTypeDef"]],
        "text": NotRequired[str],
    },
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "contentReference": "ContentReferenceTypeDef",
        "excerpt": NotRequired["DocumentTextTypeDef"],
        "title": NotRequired["DocumentTextTypeDef"],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "field": Literal["NAME"],
        "operator": Literal["EQUALS"],
        "value": str,
    },
)

GetAssistantAssociationRequestRequestTypeDef = TypedDict(
    "GetAssistantAssociationRequestRequestTypeDef",
    {
        "assistantAssociationId": str,
        "assistantId": str,
    },
)

GetAssistantAssociationResponseTypeDef = TypedDict(
    "GetAssistantAssociationResponseTypeDef",
    {
        "assistantAssociation": "AssistantAssociationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssistantRequestRequestTypeDef = TypedDict(
    "GetAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
    },
)

GetAssistantResponseTypeDef = TypedDict(
    "GetAssistantResponseTypeDef",
    {
        "assistant": "AssistantDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentRequestRequestTypeDef = TypedDict(
    "GetContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetContentResponseTypeDef = TypedDict(
    "GetContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContentSummaryRequestRequestTypeDef = TypedDict(
    "GetContentSummaryRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
    },
)

GetContentSummaryResponseTypeDef = TypedDict(
    "GetContentSummaryResponseTypeDef",
    {
        "contentSummary": "ContentSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetKnowledgeBaseRequestRequestTypeDef = TypedDict(
    "GetKnowledgeBaseRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

GetKnowledgeBaseResponseTypeDef = TypedDict(
    "GetKnowledgeBaseResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecommendationsRequestRequestTypeDef = TypedDict(
    "GetRecommendationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
        "maxResults": NotRequired[int],
        "waitTimeSeconds": NotRequired[int],
    },
)

GetRecommendationsResponseTypeDef = TypedDict(
    "GetRecommendationsResponseTypeDef",
    {
        "recommendations": List["RecommendationDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "assistantId": str,
        "sessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "session": "SessionDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "beginOffsetInclusive": NotRequired[int],
        "endOffsetExclusive": NotRequired[int],
    },
)

KnowledgeBaseAssociationDataTypeDef = TypedDict(
    "KnowledgeBaseAssociationDataTypeDef",
    {
        "knowledgeBaseArn": NotRequired[str],
        "knowledgeBaseId": NotRequired[str],
    },
)

KnowledgeBaseDataTypeDef = TypedDict(
    "KnowledgeBaseDataTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "description": NotRequired[str],
        "lastContentModificationTime": NotRequired[datetime],
        "renderingConfiguration": NotRequired["RenderingConfigurationTypeDef"],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "sourceConfiguration": NotRequired["SourceConfigurationTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

KnowledgeBaseSummaryTypeDef = TypedDict(
    "KnowledgeBaseSummaryTypeDef",
    {
        "knowledgeBaseArn": str,
        "knowledgeBaseId": str,
        "knowledgeBaseType": KnowledgeBaseTypeType,
        "name": str,
        "status": KnowledgeBaseStatusType,
        "description": NotRequired[str],
        "renderingConfiguration": NotRequired["RenderingConfigurationTypeDef"],
        "serverSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "sourceConfiguration": NotRequired["SourceConfigurationTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

ListAssistantAssociationsRequestRequestTypeDef = TypedDict(
    "ListAssistantAssociationsRequestRequestTypeDef",
    {
        "assistantId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAssistantAssociationsResponseTypeDef = TypedDict(
    "ListAssistantAssociationsResponseTypeDef",
    {
        "assistantAssociationSummaries": List["AssistantAssociationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssistantsRequestRequestTypeDef = TypedDict(
    "ListAssistantsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListAssistantsResponseTypeDef = TypedDict(
    "ListAssistantsResponseTypeDef",
    {
        "assistantSummaries": List["AssistantSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListContentsRequestRequestTypeDef = TypedDict(
    "ListContentsRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListContentsResponseTypeDef = TypedDict(
    "ListContentsResponseTypeDef",
    {
        "contentSummaries": List["ContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListKnowledgeBasesRequestRequestTypeDef = TypedDict(
    "ListKnowledgeBasesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListKnowledgeBasesResponseTypeDef = TypedDict(
    "ListKnowledgeBasesResponseTypeDef",
    {
        "knowledgeBaseSummaries": List["KnowledgeBaseSummaryTypeDef"],
        "nextToken": str,
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
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotifyRecommendationsReceivedErrorTypeDef = TypedDict(
    "NotifyRecommendationsReceivedErrorTypeDef",
    {
        "message": NotRequired[str],
        "recommendationId": NotRequired[str],
    },
)

NotifyRecommendationsReceivedRequestRequestTypeDef = TypedDict(
    "NotifyRecommendationsReceivedRequestRequestTypeDef",
    {
        "assistantId": str,
        "recommendationIds": Sequence[str],
        "sessionId": str,
    },
)

NotifyRecommendationsReceivedResponseTypeDef = TypedDict(
    "NotifyRecommendationsReceivedResponseTypeDef",
    {
        "errors": List["NotifyRecommendationsReceivedErrorTypeDef"],
        "recommendationIds": List[str],
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

QueryAssistantRequestRequestTypeDef = TypedDict(
    "QueryAssistantRequestRequestTypeDef",
    {
        "assistantId": str,
        "queryText": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

QueryAssistantResponseTypeDef = TypedDict(
    "QueryAssistantResponseTypeDef",
    {
        "nextToken": str,
        "results": List["ResultDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecommendationDataTypeDef = TypedDict(
    "RecommendationDataTypeDef",
    {
        "document": "DocumentTypeDef",
        "recommendationId": str,
        "relevanceLevel": NotRequired[RelevanceLevelType],
        "relevanceScore": NotRequired[float],
    },
)

RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
    },
)

RenderingConfigurationTypeDef = TypedDict(
    "RenderingConfigurationTypeDef",
    {
        "templateUri": NotRequired[str],
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

ResultDataTypeDef = TypedDict(
    "ResultDataTypeDef",
    {
        "document": "DocumentTypeDef",
        "resultId": str,
        "relevanceScore": NotRequired[float],
    },
)

SearchContentRequestRequestTypeDef = TypedDict(
    "SearchContentRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "searchExpression": "SearchExpressionTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

SearchContentResponseTypeDef = TypedDict(
    "SearchContentResponseTypeDef",
    {
        "contentSummaries": List["ContentSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchExpressionTypeDef = TypedDict(
    "SearchExpressionTypeDef",
    {
        "filters": Sequence["FilterTypeDef"],
    },
)

SearchSessionsRequestRequestTypeDef = TypedDict(
    "SearchSessionsRequestRequestTypeDef",
    {
        "assistantId": str,
        "searchExpression": "SearchExpressionTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

SearchSessionsResponseTypeDef = TypedDict(
    "SearchSessionsResponseTypeDef",
    {
        "nextToken": str,
        "sessionSummaries": List["SessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "kmsKeyId": NotRequired[str],
    },
)

SessionDataTypeDef = TypedDict(
    "SessionDataTypeDef",
    {
        "name": str,
        "sessionArn": str,
        "sessionId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

SessionSummaryTypeDef = TypedDict(
    "SessionSummaryTypeDef",
    {
        "assistantArn": str,
        "assistantId": str,
        "sessionArn": str,
        "sessionId": str,
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "appIntegrations": NotRequired["AppIntegrationsConfigurationTypeDef"],
    },
)

StartContentUploadRequestRequestTypeDef = TypedDict(
    "StartContentUploadRequestRequestTypeDef",
    {
        "contentType": str,
        "knowledgeBaseId": str,
    },
)

StartContentUploadResponseTypeDef = TypedDict(
    "StartContentUploadResponseTypeDef",
    {
        "headersToInclude": Dict[str, str],
        "uploadId": str,
        "url": str,
        "urlExpiry": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateContentRequestRequestTypeDef = TypedDict(
    "UpdateContentRequestRequestTypeDef",
    {
        "contentId": str,
        "knowledgeBaseId": str,
        "metadata": NotRequired[Mapping[str, str]],
        "overrideLinkOutUri": NotRequired[str],
        "removeOverrideLinkOutUri": NotRequired[bool],
        "revisionId": NotRequired[str],
        "title": NotRequired[str],
        "uploadId": NotRequired[str],
    },
)

UpdateContentResponseTypeDef = TypedDict(
    "UpdateContentResponseTypeDef",
    {
        "content": "ContentDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef",
    {
        "knowledgeBaseId": str,
        "templateUri": str,
    },
)

UpdateKnowledgeBaseTemplateUriResponseTypeDef = TypedDict(
    "UpdateKnowledgeBaseTemplateUriResponseTypeDef",
    {
        "knowledgeBase": "KnowledgeBaseDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
