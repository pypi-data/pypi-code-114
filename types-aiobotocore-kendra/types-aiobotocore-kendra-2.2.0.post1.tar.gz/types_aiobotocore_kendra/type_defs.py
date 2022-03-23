"""
Type annotations for kendra service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kendra/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kendra.type_defs import AccessControlListConfigurationTypeDef

    data: AccessControlListConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ConditionOperatorType,
    ConfluenceAttachmentFieldNameType,
    ConfluenceBlogFieldNameType,
    ConfluencePageFieldNameType,
    ConfluenceSpaceFieldNameType,
    ConfluenceVersionType,
    ContentTypeType,
    DatabaseEngineTypeType,
    DataSourceStatusType,
    DataSourceSyncJobStatusType,
    DataSourceTypeType,
    DocumentAttributeValueTypeType,
    DocumentStatusType,
    EntityTypeType,
    ErrorCodeType,
    ExperienceStatusType,
    FaqFileFormatType,
    FaqStatusType,
    HighlightTypeType,
    IndexEditionType,
    IndexStatusType,
    IntervalType,
    KeyLocationType,
    MetricTypeType,
    ModeType,
    OrderType,
    PersonaType,
    PrincipalMappingStatusType,
    PrincipalTypeType,
    QueryIdentifiersEnclosingOptionType,
    QueryResultTypeType,
    QuerySuggestionsBlockListStatusType,
    QuerySuggestionsStatusType,
    ReadAccessTypeType,
    RelevanceTypeType,
    SalesforceChatterFeedIncludeFilterTypeType,
    SalesforceKnowledgeArticleStateType,
    SalesforceStandardObjectNameType,
    ScoreConfidenceType,
    ServiceNowAuthenticationTypeType,
    ServiceNowBuildVersionTypeType,
    SharePointVersionType,
    SlackEntityType,
    SortOrderType,
    ThesaurusStatusType,
    UserContextPolicyType,
    UserGroupResolutionModeType,
    WebCrawlerModeType,
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
    "AccessControlListConfigurationTypeDef",
    "AclConfigurationTypeDef",
    "AdditionalResultAttributeTypeDef",
    "AdditionalResultAttributeValueTypeDef",
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    "AssociateEntitiesToExperienceResponseTypeDef",
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    "AssociatePersonasToEntitiesResponseTypeDef",
    "AttributeFilterTypeDef",
    "AuthenticationConfigurationTypeDef",
    "BasicAuthenticationConfigurationTypeDef",
    "BatchDeleteDocumentRequestRequestTypeDef",
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    "BatchDeleteDocumentResponseTypeDef",
    "BatchGetDocumentStatusRequestRequestTypeDef",
    "BatchGetDocumentStatusResponseErrorTypeDef",
    "BatchGetDocumentStatusResponseTypeDef",
    "BatchPutDocumentRequestRequestTypeDef",
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    "BatchPutDocumentResponseTypeDef",
    "CapacityUnitsConfigurationTypeDef",
    "ClearQuerySuggestionsRequestRequestTypeDef",
    "ClickFeedbackTypeDef",
    "ColumnConfigurationTypeDef",
    "ConfluenceAttachmentConfigurationTypeDef",
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    "ConfluenceBlogConfigurationTypeDef",
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    "ConfluenceConfigurationTypeDef",
    "ConfluencePageConfigurationTypeDef",
    "ConfluencePageToIndexFieldMappingTypeDef",
    "ConfluenceSpaceConfigurationTypeDef",
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    "ConnectionConfigurationTypeDef",
    "ContentSourceConfigurationTypeDef",
    "CorrectionTypeDef",
    "CreateDataSourceRequestRequestTypeDef",
    "CreateDataSourceResponseTypeDef",
    "CreateExperienceRequestRequestTypeDef",
    "CreateExperienceResponseTypeDef",
    "CreateFaqRequestRequestTypeDef",
    "CreateFaqResponseTypeDef",
    "CreateIndexRequestRequestTypeDef",
    "CreateIndexResponseTypeDef",
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    "CreateThesaurusRequestRequestTypeDef",
    "CreateThesaurusResponseTypeDef",
    "CustomDocumentEnrichmentConfigurationTypeDef",
    "DataSourceConfigurationTypeDef",
    "DataSourceGroupTypeDef",
    "DataSourceSummaryTypeDef",
    "DataSourceSyncJobMetricTargetTypeDef",
    "DataSourceSyncJobMetricsTypeDef",
    "DataSourceSyncJobTypeDef",
    "DataSourceToIndexFieldMappingTypeDef",
    "DataSourceVpcConfigurationTypeDef",
    "DatabaseConfigurationTypeDef",
    "DeleteDataSourceRequestRequestTypeDef",
    "DeleteExperienceRequestRequestTypeDef",
    "DeleteFaqRequestRequestTypeDef",
    "DeleteIndexRequestRequestTypeDef",
    "DeletePrincipalMappingRequestRequestTypeDef",
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    "DeleteThesaurusRequestRequestTypeDef",
    "DescribeDataSourceRequestRequestTypeDef",
    "DescribeDataSourceResponseTypeDef",
    "DescribeExperienceRequestRequestTypeDef",
    "DescribeExperienceResponseTypeDef",
    "DescribeFaqRequestRequestTypeDef",
    "DescribeFaqResponseTypeDef",
    "DescribeIndexRequestRequestTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribePrincipalMappingRequestRequestTypeDef",
    "DescribePrincipalMappingResponseTypeDef",
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    "DescribeThesaurusRequestRequestTypeDef",
    "DescribeThesaurusResponseTypeDef",
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    "DocumentAttributeConditionTypeDef",
    "DocumentAttributeTargetTypeDef",
    "DocumentAttributeTypeDef",
    "DocumentAttributeValueCountPairTypeDef",
    "DocumentAttributeValueTypeDef",
    "DocumentInfoTypeDef",
    "DocumentMetadataConfigurationTypeDef",
    "DocumentRelevanceConfigurationTypeDef",
    "DocumentTypeDef",
    "DocumentsMetadataConfigurationTypeDef",
    "EntityConfigurationTypeDef",
    "EntityDisplayDataTypeDef",
    "EntityPersonaConfigurationTypeDef",
    "ExperienceConfigurationTypeDef",
    "ExperienceEndpointTypeDef",
    "ExperienceEntitiesSummaryTypeDef",
    "ExperiencesSummaryTypeDef",
    "FacetResultTypeDef",
    "FacetTypeDef",
    "FailedEntityTypeDef",
    "FaqStatisticsTypeDef",
    "FaqSummaryTypeDef",
    "FsxConfigurationTypeDef",
    "GetQuerySuggestionsRequestRequestTypeDef",
    "GetQuerySuggestionsResponseTypeDef",
    "GetSnapshotsRequestRequestTypeDef",
    "GetSnapshotsResponseTypeDef",
    "GoogleDriveConfigurationTypeDef",
    "GroupMembersTypeDef",
    "GroupOrderingIdSummaryTypeDef",
    "GroupSummaryTypeDef",
    "HierarchicalPrincipalTypeDef",
    "HighlightTypeDef",
    "HookConfigurationTypeDef",
    "IndexConfigurationSummaryTypeDef",
    "IndexStatisticsTypeDef",
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    "JsonTokenTypeConfigurationTypeDef",
    "JwtTokenTypeConfigurationTypeDef",
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    "ListDataSourceSyncJobsResponseTypeDef",
    "ListDataSourcesRequestRequestTypeDef",
    "ListDataSourcesResponseTypeDef",
    "ListEntityPersonasRequestRequestTypeDef",
    "ListEntityPersonasResponseTypeDef",
    "ListExperienceEntitiesRequestRequestTypeDef",
    "ListExperienceEntitiesResponseTypeDef",
    "ListExperiencesRequestRequestTypeDef",
    "ListExperiencesResponseTypeDef",
    "ListFaqsRequestRequestTypeDef",
    "ListFaqsResponseTypeDef",
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    "ListIndicesRequestRequestTypeDef",
    "ListIndicesResponseTypeDef",
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThesauriRequestRequestTypeDef",
    "ListThesauriResponseTypeDef",
    "MemberGroupTypeDef",
    "MemberUserTypeDef",
    "OneDriveConfigurationTypeDef",
    "OneDriveUsersTypeDef",
    "PersonasSummaryTypeDef",
    "PrincipalTypeDef",
    "ProxyConfigurationTypeDef",
    "PutPrincipalMappingRequestRequestTypeDef",
    "QueryRequestRequestTypeDef",
    "QueryResultItemTypeDef",
    "QueryResultTypeDef",
    "QuerySuggestionsBlockListSummaryTypeDef",
    "RelevanceFeedbackTypeDef",
    "RelevanceTypeDef",
    "ResponseMetadataTypeDef",
    "S3DataSourceConfigurationTypeDef",
    "S3PathTypeDef",
    "SalesforceChatterFeedConfigurationTypeDef",
    "SalesforceConfigurationTypeDef",
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    "SalesforceStandardObjectConfigurationTypeDef",
    "ScoreAttributesTypeDef",
    "SearchTypeDef",
    "SeedUrlConfigurationTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServiceNowConfigurationTypeDef",
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    "ServiceNowServiceCatalogConfigurationTypeDef",
    "SharePointConfigurationTypeDef",
    "SiteMapsConfigurationTypeDef",
    "SlackConfigurationTypeDef",
    "SortingConfigurationTypeDef",
    "SpellCorrectedQueryTypeDef",
    "SpellCorrectionConfigurationTypeDef",
    "SqlConfigurationTypeDef",
    "StartDataSourceSyncJobRequestRequestTypeDef",
    "StartDataSourceSyncJobResponseTypeDef",
    "StatusTypeDef",
    "StopDataSourceSyncJobRequestRequestTypeDef",
    "SubmitFeedbackRequestRequestTypeDef",
    "SuggestionHighlightTypeDef",
    "SuggestionTextWithHighlightsTypeDef",
    "SuggestionTypeDef",
    "SuggestionValueTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextDocumentStatisticsTypeDef",
    "TextWithHighlightsTypeDef",
    "ThesaurusSummaryTypeDef",
    "TimeRangeTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataSourceRequestRequestTypeDef",
    "UpdateExperienceRequestRequestTypeDef",
    "UpdateIndexRequestRequestTypeDef",
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    "UpdateThesaurusRequestRequestTypeDef",
    "UrlsTypeDef",
    "UserContextTypeDef",
    "UserGroupResolutionConfigurationTypeDef",
    "UserIdentityConfigurationTypeDef",
    "UserTokenConfigurationTypeDef",
    "WarningTypeDef",
    "WebCrawlerConfigurationTypeDef",
    "WorkDocsConfigurationTypeDef",
)

AccessControlListConfigurationTypeDef = TypedDict(
    "AccessControlListConfigurationTypeDef",
    {
        "KeyPath": NotRequired[str],
    },
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "AllowedGroupsColumnName": str,
    },
)

AdditionalResultAttributeTypeDef = TypedDict(
    "AdditionalResultAttributeTypeDef",
    {
        "Key": str,
        "ValueType": Literal["TEXT_WITH_HIGHLIGHTS_VALUE"],
        "Value": "AdditionalResultAttributeValueTypeDef",
    },
)

AdditionalResultAttributeValueTypeDef = TypedDict(
    "AdditionalResultAttributeValueTypeDef",
    {
        "TextWithHighlightsValue": NotRequired["TextWithHighlightsTypeDef"],
    },
)

AssociateEntitiesToExperienceRequestRequestTypeDef = TypedDict(
    "AssociateEntitiesToExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence["EntityConfigurationTypeDef"],
    },
)

AssociateEntitiesToExperienceResponseTypeDef = TypedDict(
    "AssociateEntitiesToExperienceResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePersonasToEntitiesRequestRequestTypeDef = TypedDict(
    "AssociatePersonasToEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Personas": Sequence["EntityPersonaConfigurationTypeDef"],
    },
)

AssociatePersonasToEntitiesResponseTypeDef = TypedDict(
    "AssociatePersonasToEntitiesResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeFilterTypeDef = TypedDict(
    "AttributeFilterTypeDef",
    {
        "AndAllFilters": NotRequired[Sequence[Dict[str, Any]]],
        "OrAllFilters": NotRequired[Sequence[Dict[str, Any]]],
        "NotFilter": NotRequired[Dict[str, Any]],
        "EqualsTo": NotRequired["DocumentAttributeTypeDef"],
        "ContainsAll": NotRequired["DocumentAttributeTypeDef"],
        "ContainsAny": NotRequired["DocumentAttributeTypeDef"],
        "GreaterThan": NotRequired["DocumentAttributeTypeDef"],
        "GreaterThanOrEquals": NotRequired["DocumentAttributeTypeDef"],
        "LessThan": NotRequired["DocumentAttributeTypeDef"],
        "LessThanOrEquals": NotRequired["DocumentAttributeTypeDef"],
    },
)

AuthenticationConfigurationTypeDef = TypedDict(
    "AuthenticationConfigurationTypeDef",
    {
        "BasicAuthentication": NotRequired[Sequence["BasicAuthenticationConfigurationTypeDef"]],
    },
)

BasicAuthenticationConfigurationTypeDef = TypedDict(
    "BasicAuthenticationConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": str,
    },
)

BatchDeleteDocumentRequestRequestTypeDef = TypedDict(
    "BatchDeleteDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentIdList": Sequence[str],
        "DataSourceSyncJobMetricTarget": NotRequired["DataSourceSyncJobMetricTargetTypeDef"],
    },
)

BatchDeleteDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchDeleteDocumentResponseFailedDocumentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

BatchDeleteDocumentResponseTypeDef = TypedDict(
    "BatchDeleteDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchDeleteDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDocumentStatusRequestRequestTypeDef = TypedDict(
    "BatchGetDocumentStatusRequestRequestTypeDef",
    {
        "IndexId": str,
        "DocumentInfoList": Sequence["DocumentInfoTypeDef"],
    },
)

BatchGetDocumentStatusResponseErrorTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseErrorTypeDef",
    {
        "DocumentId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

BatchGetDocumentStatusResponseTypeDef = TypedDict(
    "BatchGetDocumentStatusResponseTypeDef",
    {
        "Errors": List["BatchGetDocumentStatusResponseErrorTypeDef"],
        "DocumentStatusList": List["StatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPutDocumentRequestRequestTypeDef = TypedDict(
    "BatchPutDocumentRequestRequestTypeDef",
    {
        "IndexId": str,
        "Documents": Sequence["DocumentTypeDef"],
        "RoleArn": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            "CustomDocumentEnrichmentConfigurationTypeDef"
        ],
    },
)

BatchPutDocumentResponseFailedDocumentTypeDef = TypedDict(
    "BatchPutDocumentResponseFailedDocumentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

BatchPutDocumentResponseTypeDef = TypedDict(
    "BatchPutDocumentResponseTypeDef",
    {
        "FailedDocuments": List["BatchPutDocumentResponseFailedDocumentTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CapacityUnitsConfigurationTypeDef = TypedDict(
    "CapacityUnitsConfigurationTypeDef",
    {
        "StorageCapacityUnits": int,
        "QueryCapacityUnits": int,
    },
)

ClearQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "ClearQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

ClickFeedbackTypeDef = TypedDict(
    "ClickFeedbackTypeDef",
    {
        "ResultId": str,
        "ClickTime": Union[datetime, str],
    },
)

ColumnConfigurationTypeDef = TypedDict(
    "ColumnConfigurationTypeDef",
    {
        "DocumentIdColumnName": str,
        "DocumentDataColumnName": str,
        "ChangeDetectingColumns": Sequence[str],
        "DocumentTitleColumnName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

ConfluenceAttachmentConfigurationTypeDef = TypedDict(
    "ConfluenceAttachmentConfigurationTypeDef",
    {
        "CrawlAttachments": NotRequired[bool],
        "AttachmentFieldMappings": NotRequired[
            Sequence["ConfluenceAttachmentToIndexFieldMappingTypeDef"]
        ],
    },
)

ConfluenceAttachmentToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceAttachmentToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceAttachmentFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)

ConfluenceBlogConfigurationTypeDef = TypedDict(
    "ConfluenceBlogConfigurationTypeDef",
    {
        "BlogFieldMappings": NotRequired[Sequence["ConfluenceBlogToIndexFieldMappingTypeDef"]],
    },
)

ConfluenceBlogToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceBlogToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceBlogFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)

ConfluenceConfigurationTypeDef = TypedDict(
    "ConfluenceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "Version": ConfluenceVersionType,
        "SpaceConfiguration": NotRequired["ConfluenceSpaceConfigurationTypeDef"],
        "PageConfiguration": NotRequired["ConfluencePageConfigurationTypeDef"],
        "BlogConfiguration": NotRequired["ConfluenceBlogConfigurationTypeDef"],
        "AttachmentConfiguration": NotRequired["ConfluenceAttachmentConfigurationTypeDef"],
        "VpcConfiguration": NotRequired["DataSourceVpcConfigurationTypeDef"],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
    },
)

ConfluencePageConfigurationTypeDef = TypedDict(
    "ConfluencePageConfigurationTypeDef",
    {
        "PageFieldMappings": NotRequired[Sequence["ConfluencePageToIndexFieldMappingTypeDef"]],
    },
)

ConfluencePageToIndexFieldMappingTypeDef = TypedDict(
    "ConfluencePageToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluencePageFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)

ConfluenceSpaceConfigurationTypeDef = TypedDict(
    "ConfluenceSpaceConfigurationTypeDef",
    {
        "CrawlPersonalSpaces": NotRequired[bool],
        "CrawlArchivedSpaces": NotRequired[bool],
        "IncludeSpaces": NotRequired[Sequence[str]],
        "ExcludeSpaces": NotRequired[Sequence[str]],
        "SpaceFieldMappings": NotRequired[Sequence["ConfluenceSpaceToIndexFieldMappingTypeDef"]],
    },
)

ConfluenceSpaceToIndexFieldMappingTypeDef = TypedDict(
    "ConfluenceSpaceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": NotRequired[ConfluenceSpaceFieldNameType],
        "DateFieldFormat": NotRequired[str],
        "IndexFieldName": NotRequired[str],
    },
)

ConnectionConfigurationTypeDef = TypedDict(
    "ConnectionConfigurationTypeDef",
    {
        "DatabaseHost": str,
        "DatabasePort": int,
        "DatabaseName": str,
        "TableName": str,
        "SecretArn": str,
    },
)

ContentSourceConfigurationTypeDef = TypedDict(
    "ContentSourceConfigurationTypeDef",
    {
        "DataSourceIds": NotRequired[Sequence[str]],
        "FaqIds": NotRequired[Sequence[str]],
        "DirectPutContent": NotRequired[bool],
    },
)

CorrectionTypeDef = TypedDict(
    "CorrectionTypeDef",
    {
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
        "Term": NotRequired[str],
        "CorrectedTerm": NotRequired[str],
    },
)

CreateDataSourceRequestRequestTypeDef = TypedDict(
    "CreateDataSourceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "Type": DataSourceTypeType,
        "Configuration": NotRequired["DataSourceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            "CustomDocumentEnrichmentConfigurationTypeDef"
        ],
    },
)

CreateDataSourceResponseTypeDef = TypedDict(
    "CreateDataSourceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateExperienceRequestRequestTypeDef = TypedDict(
    "CreateExperienceRequestRequestTypeDef",
    {
        "Name": str,
        "IndexId": str,
        "RoleArn": NotRequired[str],
        "Configuration": NotRequired["ExperienceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

CreateExperienceResponseTypeDef = TypedDict(
    "CreateExperienceResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFaqRequestRequestTypeDef = TypedDict(
    "CreateFaqRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "S3Path": "S3PathTypeDef",
        "RoleArn": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "FileFormat": NotRequired[FaqFileFormatType],
        "ClientToken": NotRequired[str],
        "LanguageCode": NotRequired[str],
    },
)

CreateFaqResponseTypeDef = TypedDict(
    "CreateFaqResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIndexRequestRequestTypeDef = TypedDict(
    "CreateIndexRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "Edition": NotRequired[IndexEditionType],
        "ServerSideEncryptionConfiguration": NotRequired[
            "ServerSideEncryptionConfigurationTypeDef"
        ],
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "UserTokenConfigurations": NotRequired[Sequence["UserTokenConfigurationTypeDef"]],
        "UserContextPolicy": NotRequired[UserContextPolicyType],
        "UserGroupResolutionConfiguration": NotRequired["UserGroupResolutionConfigurationTypeDef"],
    },
)

CreateIndexResponseTypeDef = TypedDict(
    "CreateIndexResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "SourceS3Path": "S3PathTypeDef",
        "RoleArn": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "CreateQuerySuggestionsBlockListResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateThesaurusRequestRequestTypeDef = TypedDict(
    "CreateThesaurusRequestRequestTypeDef",
    {
        "IndexId": str,
        "Name": str,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateThesaurusResponseTypeDef = TypedDict(
    "CreateThesaurusResponseTypeDef",
    {
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "CustomDocumentEnrichmentConfigurationTypeDef",
    {
        "InlineConfigurations": NotRequired[
            Sequence["InlineCustomDocumentEnrichmentConfigurationTypeDef"]
        ],
        "PreExtractionHookConfiguration": NotRequired["HookConfigurationTypeDef"],
        "PostExtractionHookConfiguration": NotRequired["HookConfigurationTypeDef"],
        "RoleArn": NotRequired[str],
    },
)

DataSourceConfigurationTypeDef = TypedDict(
    "DataSourceConfigurationTypeDef",
    {
        "S3Configuration": NotRequired["S3DataSourceConfigurationTypeDef"],
        "SharePointConfiguration": NotRequired["SharePointConfigurationTypeDef"],
        "DatabaseConfiguration": NotRequired["DatabaseConfigurationTypeDef"],
        "SalesforceConfiguration": NotRequired["SalesforceConfigurationTypeDef"],
        "OneDriveConfiguration": NotRequired["OneDriveConfigurationTypeDef"],
        "ServiceNowConfiguration": NotRequired["ServiceNowConfigurationTypeDef"],
        "ConfluenceConfiguration": NotRequired["ConfluenceConfigurationTypeDef"],
        "GoogleDriveConfiguration": NotRequired["GoogleDriveConfigurationTypeDef"],
        "WebCrawlerConfiguration": NotRequired["WebCrawlerConfigurationTypeDef"],
        "WorkDocsConfiguration": NotRequired["WorkDocsConfigurationTypeDef"],
        "FsxConfiguration": NotRequired["FsxConfigurationTypeDef"],
        "SlackConfiguration": NotRequired["SlackConfigurationTypeDef"],
    },
)

DataSourceGroupTypeDef = TypedDict(
    "DataSourceGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": str,
    },
)

DataSourceSummaryTypeDef = TypedDict(
    "DataSourceSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[DataSourceTypeType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "Status": NotRequired[DataSourceStatusType],
        "LanguageCode": NotRequired[str],
    },
)

DataSourceSyncJobMetricTargetTypeDef = TypedDict(
    "DataSourceSyncJobMetricTargetTypeDef",
    {
        "DataSourceId": str,
        "DataSourceSyncJobId": NotRequired[str],
    },
)

DataSourceSyncJobMetricsTypeDef = TypedDict(
    "DataSourceSyncJobMetricsTypeDef",
    {
        "DocumentsAdded": NotRequired[str],
        "DocumentsModified": NotRequired[str],
        "DocumentsDeleted": NotRequired[str],
        "DocumentsFailed": NotRequired[str],
        "DocumentsScanned": NotRequired[str],
    },
)

DataSourceSyncJobTypeDef = TypedDict(
    "DataSourceSyncJobTypeDef",
    {
        "ExecutionId": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Status": NotRequired[DataSourceSyncJobStatusType],
        "ErrorMessage": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "DataSourceErrorCode": NotRequired[str],
        "Metrics": NotRequired["DataSourceSyncJobMetricsTypeDef"],
    },
)

DataSourceToIndexFieldMappingTypeDef = TypedDict(
    "DataSourceToIndexFieldMappingTypeDef",
    {
        "DataSourceFieldName": str,
        "IndexFieldName": str,
        "DateFieldFormat": NotRequired[str],
    },
)

DataSourceVpcConfigurationTypeDef = TypedDict(
    "DataSourceVpcConfigurationTypeDef",
    {
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)

DatabaseConfigurationTypeDef = TypedDict(
    "DatabaseConfigurationTypeDef",
    {
        "DatabaseEngineType": DatabaseEngineTypeType,
        "ConnectionConfiguration": "ConnectionConfigurationTypeDef",
        "ColumnConfiguration": "ColumnConfigurationTypeDef",
        "VpcConfiguration": NotRequired["DataSourceVpcConfigurationTypeDef"],
        "AclConfiguration": NotRequired["AclConfigurationTypeDef"],
        "SqlConfiguration": NotRequired["SqlConfigurationTypeDef"],
    },
)

DeleteDataSourceRequestRequestTypeDef = TypedDict(
    "DeleteDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteExperienceRequestRequestTypeDef = TypedDict(
    "DeleteExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteFaqRequestRequestTypeDef = TypedDict(
    "DeleteFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DeleteIndexRequestRequestTypeDef = TypedDict(
    "DeleteIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePrincipalMappingRequestRequestTypeDef = TypedDict(
    "DeletePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "DataSourceId": NotRequired[str],
        "OrderingId": NotRequired[int],
    },
)

DeleteQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DeleteQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DeleteThesaurusRequestRequestTypeDef = TypedDict(
    "DeleteThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeDataSourceRequestRequestTypeDef = TypedDict(
    "DescribeDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeDataSourceResponseTypeDef = TypedDict(
    "DescribeDataSourceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Type": DataSourceTypeType,
        "Configuration": "DataSourceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": DataSourceStatusType,
        "Schedule": str,
        "RoleArn": str,
        "ErrorMessage": str,
        "LanguageCode": str,
        "CustomDocumentEnrichmentConfiguration": "CustomDocumentEnrichmentConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExperienceRequestRequestTypeDef = TypedDict(
    "DescribeExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeExperienceResponseTypeDef = TypedDict(
    "DescribeExperienceResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Endpoints": List["ExperienceEndpointTypeDef"],
        "Configuration": "ExperienceConfigurationTypeDef",
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Description": str,
        "Status": ExperienceStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFaqRequestRequestTypeDef = TypedDict(
    "DescribeFaqRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeFaqResponseTypeDef = TypedDict(
    "DescribeFaqResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "S3Path": "S3PathTypeDef",
        "Status": FaqStatusType,
        "RoleArn": str,
        "ErrorMessage": str,
        "FileFormat": FaqFileFormatType,
        "LanguageCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIndexRequestRequestTypeDef = TypedDict(
    "DescribeIndexRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeIndexResponseTypeDef = TypedDict(
    "DescribeIndexResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Edition": IndexEditionType,
        "RoleArn": str,
        "ServerSideEncryptionConfiguration": "ServerSideEncryptionConfigurationTypeDef",
        "Status": IndexStatusType,
        "Description": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DocumentMetadataConfigurations": List["DocumentMetadataConfigurationTypeDef"],
        "IndexStatistics": "IndexStatisticsTypeDef",
        "ErrorMessage": str,
        "CapacityUnits": "CapacityUnitsConfigurationTypeDef",
        "UserTokenConfigurations": List["UserTokenConfigurationTypeDef"],
        "UserContextPolicy": UserContextPolicyType,
        "UserGroupResolutionConfiguration": "UserGroupResolutionConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrincipalMappingRequestRequestTypeDef = TypedDict(
    "DescribePrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "DataSourceId": NotRequired[str],
    },
)

DescribePrincipalMappingResponseTypeDef = TypedDict(
    "DescribePrincipalMappingResponseTypeDef",
    {
        "IndexId": str,
        "DataSourceId": str,
        "GroupId": str,
        "GroupOrderingIdSummaries": List["GroupOrderingIdSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
    },
)

DescribeQuerySuggestionsBlockListResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsBlockListResponseTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": QuerySuggestionsBlockListStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "SourceS3Path": "S3PathTypeDef",
        "ItemCount": int,
        "FileSizeBytes": int,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
    },
)

DescribeQuerySuggestionsConfigResponseTypeDef = TypedDict(
    "DescribeQuerySuggestionsConfigResponseTypeDef",
    {
        "Mode": ModeType,
        "Status": QuerySuggestionsStatusType,
        "QueryLogLookBackWindowInDays": int,
        "IncludeQueriesWithoutUserInformation": bool,
        "MinimumNumberOfQueryingUsers": int,
        "MinimumQueryCount": int,
        "LastSuggestionsBuildTime": datetime,
        "LastClearTime": datetime,
        "TotalSuggestionsCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeThesaurusRequestRequestTypeDef = TypedDict(
    "DescribeThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

DescribeThesaurusResponseTypeDef = TypedDict(
    "DescribeThesaurusResponseTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": str,
        "Description": str,
        "Status": ThesaurusStatusType,
        "ErrorMessage": str,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "RoleArn": str,
        "SourceS3Path": "S3PathTypeDef",
        "FileSizeBytes": int,
        "TermCount": int,
        "SynonymRuleCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateEntitiesFromExperienceRequestRequestTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityList": Sequence["EntityConfigurationTypeDef"],
    },
)

DisassociateEntitiesFromExperienceResponseTypeDef = TypedDict(
    "DisassociateEntitiesFromExperienceResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePersonasFromEntitiesRequestRequestTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "EntityIds": Sequence[str],
    },
)

DisassociatePersonasFromEntitiesResponseTypeDef = TypedDict(
    "DisassociatePersonasFromEntitiesResponseTypeDef",
    {
        "FailedEntityList": List["FailedEntityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DocumentAttributeConditionTypeDef = TypedDict(
    "DocumentAttributeConditionTypeDef",
    {
        "ConditionDocumentAttributeKey": str,
        "Operator": ConditionOperatorType,
        "ConditionOnValue": NotRequired["DocumentAttributeValueTypeDef"],
    },
)

DocumentAttributeTargetTypeDef = TypedDict(
    "DocumentAttributeTargetTypeDef",
    {
        "TargetDocumentAttributeKey": NotRequired[str],
        "TargetDocumentAttributeValueDeletion": NotRequired[bool],
        "TargetDocumentAttributeValue": NotRequired["DocumentAttributeValueTypeDef"],
    },
)

DocumentAttributeTypeDef = TypedDict(
    "DocumentAttributeTypeDef",
    {
        "Key": str,
        "Value": "DocumentAttributeValueTypeDef",
    },
)

DocumentAttributeValueCountPairTypeDef = TypedDict(
    "DocumentAttributeValueCountPairTypeDef",
    {
        "DocumentAttributeValue": NotRequired["DocumentAttributeValueTypeDef"],
        "Count": NotRequired[int],
    },
)

DocumentAttributeValueTypeDef = TypedDict(
    "DocumentAttributeValueTypeDef",
    {
        "StringValue": NotRequired[str],
        "StringListValue": NotRequired[Sequence[str]],
        "LongValue": NotRequired[int],
        "DateValue": NotRequired[Union[datetime, str]],
    },
)

DocumentInfoTypeDef = TypedDict(
    "DocumentInfoTypeDef",
    {
        "DocumentId": str,
        "Attributes": NotRequired[Sequence["DocumentAttributeTypeDef"]],
    },
)

DocumentMetadataConfigurationTypeDef = TypedDict(
    "DocumentMetadataConfigurationTypeDef",
    {
        "Name": str,
        "Type": DocumentAttributeValueTypeType,
        "Relevance": NotRequired["RelevanceTypeDef"],
        "Search": NotRequired["SearchTypeDef"],
    },
)

DocumentRelevanceConfigurationTypeDef = TypedDict(
    "DocumentRelevanceConfigurationTypeDef",
    {
        "Name": str,
        "Relevance": "RelevanceTypeDef",
    },
)

DocumentTypeDef = TypedDict(
    "DocumentTypeDef",
    {
        "Id": str,
        "Title": NotRequired[str],
        "Blob": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "S3Path": NotRequired["S3PathTypeDef"],
        "Attributes": NotRequired[Sequence["DocumentAttributeTypeDef"]],
        "AccessControlList": NotRequired[Sequence["PrincipalTypeDef"]],
        "HierarchicalAccessControlList": NotRequired[Sequence["HierarchicalPrincipalTypeDef"]],
        "ContentType": NotRequired[ContentTypeType],
    },
)

DocumentsMetadataConfigurationTypeDef = TypedDict(
    "DocumentsMetadataConfigurationTypeDef",
    {
        "S3Prefix": NotRequired[str],
    },
)

EntityConfigurationTypeDef = TypedDict(
    "EntityConfigurationTypeDef",
    {
        "EntityId": str,
        "EntityType": EntityTypeType,
    },
)

EntityDisplayDataTypeDef = TypedDict(
    "EntityDisplayDataTypeDef",
    {
        "UserName": NotRequired[str],
        "GroupName": NotRequired[str],
        "IdentifiedUserName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
    },
)

EntityPersonaConfigurationTypeDef = TypedDict(
    "EntityPersonaConfigurationTypeDef",
    {
        "EntityId": str,
        "Persona": PersonaType,
    },
)

ExperienceConfigurationTypeDef = TypedDict(
    "ExperienceConfigurationTypeDef",
    {
        "ContentSourceConfiguration": NotRequired["ContentSourceConfigurationTypeDef"],
        "UserIdentityConfiguration": NotRequired["UserIdentityConfigurationTypeDef"],
    },
)

ExperienceEndpointTypeDef = TypedDict(
    "ExperienceEndpointTypeDef",
    {
        "EndpointType": NotRequired[Literal["HOME"]],
        "Endpoint": NotRequired[str],
    },
)

ExperienceEntitiesSummaryTypeDef = TypedDict(
    "ExperienceEntitiesSummaryTypeDef",
    {
        "EntityId": NotRequired[str],
        "EntityType": NotRequired[EntityTypeType],
        "DisplayData": NotRequired["EntityDisplayDataTypeDef"],
    },
)

ExperiencesSummaryTypeDef = TypedDict(
    "ExperiencesSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "Status": NotRequired[ExperienceStatusType],
        "Endpoints": NotRequired[List["ExperienceEndpointTypeDef"]],
    },
)

FacetResultTypeDef = TypedDict(
    "FacetResultTypeDef",
    {
        "DocumentAttributeKey": NotRequired[str],
        "DocumentAttributeValueType": NotRequired[DocumentAttributeValueTypeType],
        "DocumentAttributeValueCountPairs": NotRequired[
            List["DocumentAttributeValueCountPairTypeDef"]
        ],
    },
)

FacetTypeDef = TypedDict(
    "FacetTypeDef",
    {
        "DocumentAttributeKey": NotRequired[str],
    },
)

FailedEntityTypeDef = TypedDict(
    "FailedEntityTypeDef",
    {
        "EntityId": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

FaqStatisticsTypeDef = TypedDict(
    "FaqStatisticsTypeDef",
    {
        "IndexedQuestionAnswersCount": int,
    },
)

FaqSummaryTypeDef = TypedDict(
    "FaqSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[FaqStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "FileFormat": NotRequired[FaqFileFormatType],
        "LanguageCode": NotRequired[str],
    },
)

FsxConfigurationTypeDef = TypedDict(
    "FsxConfigurationTypeDef",
    {
        "FileSystemId": str,
        "FileSystemType": Literal["WINDOWS"],
        "VpcConfiguration": "DataSourceVpcConfigurationTypeDef",
        "SecretArn": NotRequired[str],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

GetQuerySuggestionsRequestRequestTypeDef = TypedDict(
    "GetQuerySuggestionsRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": str,
        "MaxSuggestionsCount": NotRequired[int],
    },
)

GetQuerySuggestionsResponseTypeDef = TypedDict(
    "GetQuerySuggestionsResponseTypeDef",
    {
        "QuerySuggestionsId": str,
        "Suggestions": List["SuggestionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotsRequestRequestTypeDef = TypedDict(
    "GetSnapshotsRequestRequestTypeDef",
    {
        "IndexId": str,
        "Interval": IntervalType,
        "MetricType": MetricTypeType,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetSnapshotsResponseTypeDef = TypedDict(
    "GetSnapshotsResponseTypeDef",
    {
        "SnapShotTimeFilter": "TimeRangeTypeDef",
        "SnapshotsDataHeader": List[str],
        "SnapshotsData": List[List[str]],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GoogleDriveConfigurationTypeDef = TypedDict(
    "GoogleDriveConfigurationTypeDef",
    {
        "SecretArn": str,
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
        "ExcludeMimeTypes": NotRequired[Sequence[str]],
        "ExcludeUserAccounts": NotRequired[Sequence[str]],
        "ExcludeSharedDrives": NotRequired[Sequence[str]],
    },
)

GroupMembersTypeDef = TypedDict(
    "GroupMembersTypeDef",
    {
        "MemberGroups": NotRequired[Sequence["MemberGroupTypeDef"]],
        "MemberUsers": NotRequired[Sequence["MemberUserTypeDef"]],
        "S3PathforGroupMembers": NotRequired["S3PathTypeDef"],
    },
)

GroupOrderingIdSummaryTypeDef = TypedDict(
    "GroupOrderingIdSummaryTypeDef",
    {
        "Status": NotRequired[PrincipalMappingStatusType],
        "LastUpdatedAt": NotRequired[datetime],
        "ReceivedAt": NotRequired[datetime],
        "OrderingId": NotRequired[int],
        "FailureReason": NotRequired[str],
    },
)

GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupId": NotRequired[str],
        "OrderingId": NotRequired[int],
    },
)

HierarchicalPrincipalTypeDef = TypedDict(
    "HierarchicalPrincipalTypeDef",
    {
        "PrincipalList": Sequence["PrincipalTypeDef"],
    },
)

HighlightTypeDef = TypedDict(
    "HighlightTypeDef",
    {
        "BeginOffset": int,
        "EndOffset": int,
        "TopAnswer": NotRequired[bool],
        "Type": NotRequired[HighlightTypeType],
    },
)

HookConfigurationTypeDef = TypedDict(
    "HookConfigurationTypeDef",
    {
        "LambdaArn": str,
        "S3Bucket": str,
        "InvocationCondition": NotRequired["DocumentAttributeConditionTypeDef"],
    },
)

IndexConfigurationSummaryTypeDef = TypedDict(
    "IndexConfigurationSummaryTypeDef",
    {
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "Status": IndexStatusType,
        "Name": NotRequired[str],
        "Id": NotRequired[str],
        "Edition": NotRequired[IndexEditionType],
    },
)

IndexStatisticsTypeDef = TypedDict(
    "IndexStatisticsTypeDef",
    {
        "FaqStatistics": "FaqStatisticsTypeDef",
        "TextDocumentStatistics": "TextDocumentStatisticsTypeDef",
    },
)

InlineCustomDocumentEnrichmentConfigurationTypeDef = TypedDict(
    "InlineCustomDocumentEnrichmentConfigurationTypeDef",
    {
        "Condition": NotRequired["DocumentAttributeConditionTypeDef"],
        "Target": NotRequired["DocumentAttributeTargetTypeDef"],
        "DocumentContentDeletion": NotRequired[bool],
    },
)

JsonTokenTypeConfigurationTypeDef = TypedDict(
    "JsonTokenTypeConfigurationTypeDef",
    {
        "UserNameAttributeField": str,
        "GroupAttributeField": str,
    },
)

JwtTokenTypeConfigurationTypeDef = TypedDict(
    "JwtTokenTypeConfigurationTypeDef",
    {
        "KeyLocation": KeyLocationType,
        "URL": NotRequired[str],
        "SecretManagerArn": NotRequired[str],
        "UserNameAttributeField": NotRequired[str],
        "GroupAttributeField": NotRequired[str],
        "Issuer": NotRequired[str],
        "ClaimRegex": NotRequired[str],
    },
)

ListDataSourceSyncJobsRequestRequestTypeDef = TypedDict(
    "ListDataSourceSyncJobsRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StartTimeFilter": NotRequired["TimeRangeTypeDef"],
        "StatusFilter": NotRequired[DataSourceSyncJobStatusType],
    },
)

ListDataSourceSyncJobsResponseTypeDef = TypedDict(
    "ListDataSourceSyncJobsResponseTypeDef",
    {
        "History": List["DataSourceSyncJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataSourcesRequestRequestTypeDef = TypedDict(
    "ListDataSourcesRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataSourcesResponseTypeDef = TypedDict(
    "ListDataSourcesResponseTypeDef",
    {
        "SummaryItems": List["DataSourceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntityPersonasRequestRequestTypeDef = TypedDict(
    "ListEntityPersonasRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEntityPersonasResponseTypeDef = TypedDict(
    "ListEntityPersonasResponseTypeDef",
    {
        "SummaryItems": List["PersonasSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperienceEntitiesRequestRequestTypeDef = TypedDict(
    "ListExperienceEntitiesRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "NextToken": NotRequired[str],
    },
)

ListExperienceEntitiesResponseTypeDef = TypedDict(
    "ListExperienceEntitiesResponseTypeDef",
    {
        "SummaryItems": List["ExperienceEntitiesSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExperiencesRequestRequestTypeDef = TypedDict(
    "ListExperiencesRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListExperiencesResponseTypeDef = TypedDict(
    "ListExperiencesResponseTypeDef",
    {
        "SummaryItems": List["ExperiencesSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFaqsRequestRequestTypeDef = TypedDict(
    "ListFaqsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFaqsResponseTypeDef = TypedDict(
    "ListFaqsResponseTypeDef",
    {
        "NextToken": str,
        "FaqSummaryItems": List["FaqSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGroupsOlderThanOrderingIdRequestRequestTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdRequestRequestTypeDef",
    {
        "IndexId": str,
        "OrderingId": int,
        "DataSourceId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGroupsOlderThanOrderingIdResponseTypeDef = TypedDict(
    "ListGroupsOlderThanOrderingIdResponseTypeDef",
    {
        "GroupsSummaries": List["GroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIndicesRequestRequestTypeDef = TypedDict(
    "ListIndicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListIndicesResponseTypeDef = TypedDict(
    "ListIndicesResponseTypeDef",
    {
        "IndexConfigurationSummaryItems": List["IndexConfigurationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQuerySuggestionsBlockListsRequestRequestTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListQuerySuggestionsBlockListsResponseTypeDef = TypedDict(
    "ListQuerySuggestionsBlockListsResponseTypeDef",
    {
        "BlockListSummaryItems": List["QuerySuggestionsBlockListSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListThesauriRequestRequestTypeDef = TypedDict(
    "ListThesauriRequestRequestTypeDef",
    {
        "IndexId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListThesauriResponseTypeDef = TypedDict(
    "ListThesauriResponseTypeDef",
    {
        "NextToken": str,
        "ThesaurusSummaryItems": List["ThesaurusSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MemberGroupTypeDef = TypedDict(
    "MemberGroupTypeDef",
    {
        "GroupId": str,
        "DataSourceId": NotRequired[str],
    },
)

MemberUserTypeDef = TypedDict(
    "MemberUserTypeDef",
    {
        "UserId": str,
    },
)

OneDriveConfigurationTypeDef = TypedDict(
    "OneDriveConfigurationTypeDef",
    {
        "TenantDomain": str,
        "SecretArn": str,
        "OneDriveUsers": "OneDriveUsersTypeDef",
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
        "DisableLocalGroups": NotRequired[bool],
    },
)

OneDriveUsersTypeDef = TypedDict(
    "OneDriveUsersTypeDef",
    {
        "OneDriveUserList": NotRequired[Sequence[str]],
        "OneDriveUserS3Path": NotRequired["S3PathTypeDef"],
    },
)

PersonasSummaryTypeDef = TypedDict(
    "PersonasSummaryTypeDef",
    {
        "EntityId": NotRequired[str],
        "Persona": NotRequired[PersonaType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {
        "Name": str,
        "Type": PrincipalTypeType,
        "Access": ReadAccessTypeType,
        "DataSourceId": NotRequired[str],
    },
)

ProxyConfigurationTypeDef = TypedDict(
    "ProxyConfigurationTypeDef",
    {
        "Host": str,
        "Port": int,
        "Credentials": NotRequired[str],
    },
)

PutPrincipalMappingRequestRequestTypeDef = TypedDict(
    "PutPrincipalMappingRequestRequestTypeDef",
    {
        "IndexId": str,
        "GroupId": str,
        "GroupMembers": "GroupMembersTypeDef",
        "DataSourceId": NotRequired[str],
        "OrderingId": NotRequired[int],
        "RoleArn": NotRequired[str],
    },
)

QueryRequestRequestTypeDef = TypedDict(
    "QueryRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryText": NotRequired[str],
        "AttributeFilter": NotRequired["AttributeFilterTypeDef"],
        "Facets": NotRequired[Sequence["FacetTypeDef"]],
        "RequestedDocumentAttributes": NotRequired[Sequence[str]],
        "QueryResultTypeFilter": NotRequired[QueryResultTypeType],
        "DocumentRelevanceOverrideConfigurations": NotRequired[
            Sequence["DocumentRelevanceConfigurationTypeDef"]
        ],
        "PageNumber": NotRequired[int],
        "PageSize": NotRequired[int],
        "SortingConfiguration": NotRequired["SortingConfigurationTypeDef"],
        "UserContext": NotRequired["UserContextTypeDef"],
        "VisitorId": NotRequired[str],
        "SpellCorrectionConfiguration": NotRequired["SpellCorrectionConfigurationTypeDef"],
    },
)

QueryResultItemTypeDef = TypedDict(
    "QueryResultItemTypeDef",
    {
        "Id": NotRequired[str],
        "Type": NotRequired[QueryResultTypeType],
        "AdditionalAttributes": NotRequired[List["AdditionalResultAttributeTypeDef"]],
        "DocumentId": NotRequired[str],
        "DocumentTitle": NotRequired["TextWithHighlightsTypeDef"],
        "DocumentExcerpt": NotRequired["TextWithHighlightsTypeDef"],
        "DocumentURI": NotRequired[str],
        "DocumentAttributes": NotRequired[List["DocumentAttributeTypeDef"]],
        "ScoreAttributes": NotRequired["ScoreAttributesTypeDef"],
        "FeedbackToken": NotRequired[str],
    },
)

QueryResultTypeDef = TypedDict(
    "QueryResultTypeDef",
    {
        "QueryId": str,
        "ResultItems": List["QueryResultItemTypeDef"],
        "FacetResults": List["FacetResultTypeDef"],
        "TotalNumberOfResults": int,
        "Warnings": List["WarningTypeDef"],
        "SpellCorrectedQueries": List["SpellCorrectedQueryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

QuerySuggestionsBlockListSummaryTypeDef = TypedDict(
    "QuerySuggestionsBlockListSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[QuerySuggestionsBlockListStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
        "ItemCount": NotRequired[int],
    },
)

RelevanceFeedbackTypeDef = TypedDict(
    "RelevanceFeedbackTypeDef",
    {
        "ResultId": str,
        "RelevanceValue": RelevanceTypeType,
    },
)

RelevanceTypeDef = TypedDict(
    "RelevanceTypeDef",
    {
        "Freshness": NotRequired[bool],
        "Importance": NotRequired[int],
        "Duration": NotRequired[str],
        "RankOrder": NotRequired[OrderType],
        "ValueImportanceMap": NotRequired[Dict[str, int]],
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

S3DataSourceConfigurationTypeDef = TypedDict(
    "S3DataSourceConfigurationTypeDef",
    {
        "BucketName": str,
        "InclusionPrefixes": NotRequired[Sequence[str]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "DocumentsMetadataConfiguration": NotRequired["DocumentsMetadataConfigurationTypeDef"],
        "AccessControlListConfiguration": NotRequired["AccessControlListConfigurationTypeDef"],
    },
)

S3PathTypeDef = TypedDict(
    "S3PathTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

SalesforceChatterFeedConfigurationTypeDef = TypedDict(
    "SalesforceChatterFeedConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
        "IncludeFilterTypes": NotRequired[Sequence[SalesforceChatterFeedIncludeFilterTypeType]],
    },
)

SalesforceConfigurationTypeDef = TypedDict(
    "SalesforceConfigurationTypeDef",
    {
        "ServerUrl": str,
        "SecretArn": str,
        "StandardObjectConfigurations": NotRequired[
            Sequence["SalesforceStandardObjectConfigurationTypeDef"]
        ],
        "KnowledgeArticleConfiguration": NotRequired[
            "SalesforceKnowledgeArticleConfigurationTypeDef"
        ],
        "ChatterFeedConfiguration": NotRequired["SalesforceChatterFeedConfigurationTypeDef"],
        "CrawlAttachments": NotRequired[bool],
        "StandardObjectAttachmentConfiguration": NotRequired[
            "SalesforceStandardObjectAttachmentConfigurationTypeDef"
        ],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
    },
)

SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef",
    {
        "Name": str,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

SalesforceKnowledgeArticleConfigurationTypeDef = TypedDict(
    "SalesforceKnowledgeArticleConfigurationTypeDef",
    {
        "IncludedStates": Sequence[SalesforceKnowledgeArticleStateType],
        "StandardKnowledgeArticleTypeConfiguration": NotRequired[
            "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef"
        ],
        "CustomKnowledgeArticleTypeConfigurations": NotRequired[
            Sequence["SalesforceCustomKnowledgeArticleTypeConfigurationTypeDef"]
        ],
    },
)

SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef = TypedDict(
    "SalesforceStandardKnowledgeArticleTypeConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

SalesforceStandardObjectAttachmentConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectAttachmentConfigurationTypeDef",
    {
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

SalesforceStandardObjectConfigurationTypeDef = TypedDict(
    "SalesforceStandardObjectConfigurationTypeDef",
    {
        "Name": SalesforceStandardObjectNameType,
        "DocumentDataFieldName": str,
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

ScoreAttributesTypeDef = TypedDict(
    "ScoreAttributesTypeDef",
    {
        "ScoreConfidence": NotRequired[ScoreConfidenceType],
    },
)

SearchTypeDef = TypedDict(
    "SearchTypeDef",
    {
        "Facetable": NotRequired[bool],
        "Searchable": NotRequired[bool],
        "Displayable": NotRequired[bool],
        "Sortable": NotRequired[bool],
    },
)

SeedUrlConfigurationTypeDef = TypedDict(
    "SeedUrlConfigurationTypeDef",
    {
        "SeedUrls": Sequence[str],
        "WebCrawlerMode": NotRequired[WebCrawlerModeType],
    },
)

ServerSideEncryptionConfigurationTypeDef = TypedDict(
    "ServerSideEncryptionConfigurationTypeDef",
    {
        "KmsKeyId": NotRequired[str],
    },
)

ServiceNowConfigurationTypeDef = TypedDict(
    "ServiceNowConfigurationTypeDef",
    {
        "HostUrl": str,
        "SecretArn": str,
        "ServiceNowBuildVersion": ServiceNowBuildVersionTypeType,
        "KnowledgeArticleConfiguration": NotRequired[
            "ServiceNowKnowledgeArticleConfigurationTypeDef"
        ],
        "ServiceCatalogConfiguration": NotRequired["ServiceNowServiceCatalogConfigurationTypeDef"],
        "AuthenticationType": NotRequired[ServiceNowAuthenticationTypeType],
    },
)

ServiceNowKnowledgeArticleConfigurationTypeDef = TypedDict(
    "ServiceNowKnowledgeArticleConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
        "FilterQuery": NotRequired[str],
    },
)

ServiceNowServiceCatalogConfigurationTypeDef = TypedDict(
    "ServiceNowServiceCatalogConfigurationTypeDef",
    {
        "DocumentDataFieldName": str,
        "CrawlAttachments": NotRequired[bool],
        "IncludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "ExcludeAttachmentFilePatterns": NotRequired[Sequence[str]],
        "DocumentTitleFieldName": NotRequired[str],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

SharePointConfigurationTypeDef = TypedDict(
    "SharePointConfigurationTypeDef",
    {
        "SharePointVersion": SharePointVersionType,
        "Urls": Sequence[str],
        "SecretArn": str,
        "CrawlAttachments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "VpcConfiguration": NotRequired["DataSourceVpcConfigurationTypeDef"],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
        "DocumentTitleFieldName": NotRequired[str],
        "DisableLocalGroups": NotRequired[bool],
        "SslCertificateS3Path": NotRequired["S3PathTypeDef"],
    },
)

SiteMapsConfigurationTypeDef = TypedDict(
    "SiteMapsConfigurationTypeDef",
    {
        "SiteMaps": Sequence[str],
    },
)

SlackConfigurationTypeDef = TypedDict(
    "SlackConfigurationTypeDef",
    {
        "TeamId": str,
        "SecretArn": str,
        "SlackEntityList": Sequence[SlackEntityType],
        "SinceCrawlDate": str,
        "VpcConfiguration": NotRequired["DataSourceVpcConfigurationTypeDef"],
        "UseChangeLog": NotRequired[bool],
        "CrawlBotMessage": NotRequired[bool],
        "ExcludeArchived": NotRequired[bool],
        "LookBackPeriod": NotRequired[int],
        "PrivateChannelFilter": NotRequired[Sequence[str]],
        "PublicChannelFilter": NotRequired[Sequence[str]],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)

SortingConfigurationTypeDef = TypedDict(
    "SortingConfigurationTypeDef",
    {
        "DocumentAttributeKey": str,
        "SortOrder": SortOrderType,
    },
)

SpellCorrectedQueryTypeDef = TypedDict(
    "SpellCorrectedQueryTypeDef",
    {
        "SuggestedQueryText": NotRequired[str],
        "Corrections": NotRequired[List["CorrectionTypeDef"]],
    },
)

SpellCorrectionConfigurationTypeDef = TypedDict(
    "SpellCorrectionConfigurationTypeDef",
    {
        "IncludeQuerySpellCheckSuggestions": bool,
    },
)

SqlConfigurationTypeDef = TypedDict(
    "SqlConfigurationTypeDef",
    {
        "QueryIdentifiersEnclosingOption": NotRequired[QueryIdentifiersEnclosingOptionType],
    },
)

StartDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StartDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

StartDataSourceSyncJobResponseTypeDef = TypedDict(
    "StartDataSourceSyncJobResponseTypeDef",
    {
        "ExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "DocumentId": NotRequired[str],
        "DocumentStatus": NotRequired[DocumentStatusType],
        "FailureCode": NotRequired[str],
        "FailureReason": NotRequired[str],
    },
)

StopDataSourceSyncJobRequestRequestTypeDef = TypedDict(
    "StopDataSourceSyncJobRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
    },
)

SubmitFeedbackRequestRequestTypeDef = TypedDict(
    "SubmitFeedbackRequestRequestTypeDef",
    {
        "IndexId": str,
        "QueryId": str,
        "ClickFeedbackItems": NotRequired[Sequence["ClickFeedbackTypeDef"]],
        "RelevanceFeedbackItems": NotRequired[Sequence["RelevanceFeedbackTypeDef"]],
    },
)

SuggestionHighlightTypeDef = TypedDict(
    "SuggestionHighlightTypeDef",
    {
        "BeginOffset": NotRequired[int],
        "EndOffset": NotRequired[int],
    },
)

SuggestionTextWithHighlightsTypeDef = TypedDict(
    "SuggestionTextWithHighlightsTypeDef",
    {
        "Text": NotRequired[str],
        "Highlights": NotRequired[List["SuggestionHighlightTypeDef"]],
    },
)

SuggestionTypeDef = TypedDict(
    "SuggestionTypeDef",
    {
        "Id": NotRequired[str],
        "Value": NotRequired["SuggestionValueTypeDef"],
    },
)

SuggestionValueTypeDef = TypedDict(
    "SuggestionValueTypeDef",
    {
        "Text": NotRequired["SuggestionTextWithHighlightsTypeDef"],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
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

TextDocumentStatisticsTypeDef = TypedDict(
    "TextDocumentStatisticsTypeDef",
    {
        "IndexedTextDocumentsCount": int,
        "IndexedTextBytes": int,
    },
)

TextWithHighlightsTypeDef = TypedDict(
    "TextWithHighlightsTypeDef",
    {
        "Text": NotRequired[str],
        "Highlights": NotRequired[List["HighlightTypeDef"]],
    },
)

ThesaurusSummaryTypeDef = TypedDict(
    "ThesaurusSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ThesaurusStatusType],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDataSourceRequestRequestTypeDef = TypedDict(
    "UpdateDataSourceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "Configuration": NotRequired["DataSourceConfigurationTypeDef"],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "RoleArn": NotRequired[str],
        "LanguageCode": NotRequired[str],
        "CustomDocumentEnrichmentConfiguration": NotRequired[
            "CustomDocumentEnrichmentConfigurationTypeDef"
        ],
    },
)

UpdateExperienceRequestRequestTypeDef = TypedDict(
    "UpdateExperienceRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Configuration": NotRequired["ExperienceConfigurationTypeDef"],
        "Description": NotRequired[str],
    },
)

UpdateIndexRequestRequestTypeDef = TypedDict(
    "UpdateIndexRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Description": NotRequired[str],
        "DocumentMetadataConfigurationUpdates": NotRequired[
            Sequence["DocumentMetadataConfigurationTypeDef"]
        ],
        "CapacityUnits": NotRequired["CapacityUnitsConfigurationTypeDef"],
        "UserTokenConfigurations": NotRequired[Sequence["UserTokenConfigurationTypeDef"]],
        "UserContextPolicy": NotRequired[UserContextPolicyType],
        "UserGroupResolutionConfiguration": NotRequired["UserGroupResolutionConfigurationTypeDef"],
    },
)

UpdateQuerySuggestionsBlockListRequestRequestTypeDef = TypedDict(
    "UpdateQuerySuggestionsBlockListRequestRequestTypeDef",
    {
        "IndexId": str,
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SourceS3Path": NotRequired["S3PathTypeDef"],
        "RoleArn": NotRequired[str],
    },
)

UpdateQuerySuggestionsConfigRequestRequestTypeDef = TypedDict(
    "UpdateQuerySuggestionsConfigRequestRequestTypeDef",
    {
        "IndexId": str,
        "Mode": NotRequired[ModeType],
        "QueryLogLookBackWindowInDays": NotRequired[int],
        "IncludeQueriesWithoutUserInformation": NotRequired[bool],
        "MinimumNumberOfQueryingUsers": NotRequired[int],
        "MinimumQueryCount": NotRequired[int],
    },
)

UpdateThesaurusRequestRequestTypeDef = TypedDict(
    "UpdateThesaurusRequestRequestTypeDef",
    {
        "Id": str,
        "IndexId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SourceS3Path": NotRequired["S3PathTypeDef"],
    },
)

UrlsTypeDef = TypedDict(
    "UrlsTypeDef",
    {
        "SeedUrlConfiguration": NotRequired["SeedUrlConfigurationTypeDef"],
        "SiteMapsConfiguration": NotRequired["SiteMapsConfigurationTypeDef"],
    },
)

UserContextTypeDef = TypedDict(
    "UserContextTypeDef",
    {
        "Token": NotRequired[str],
        "UserId": NotRequired[str],
        "Groups": NotRequired[Sequence[str]],
        "DataSourceGroups": NotRequired[Sequence["DataSourceGroupTypeDef"]],
    },
)

UserGroupResolutionConfigurationTypeDef = TypedDict(
    "UserGroupResolutionConfigurationTypeDef",
    {
        "UserGroupResolutionMode": UserGroupResolutionModeType,
    },
)

UserIdentityConfigurationTypeDef = TypedDict(
    "UserIdentityConfigurationTypeDef",
    {
        "IdentityAttributeName": NotRequired[str],
    },
)

UserTokenConfigurationTypeDef = TypedDict(
    "UserTokenConfigurationTypeDef",
    {
        "JwtTokenTypeConfiguration": NotRequired["JwtTokenTypeConfigurationTypeDef"],
        "JsonTokenTypeConfiguration": NotRequired["JsonTokenTypeConfigurationTypeDef"],
    },
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Message": NotRequired[str],
        "Code": NotRequired[Literal["QUERY_LANGUAGE_INVALID_SYNTAX"]],
    },
)

WebCrawlerConfigurationTypeDef = TypedDict(
    "WebCrawlerConfigurationTypeDef",
    {
        "Urls": "UrlsTypeDef",
        "CrawlDepth": NotRequired[int],
        "MaxLinksPerPage": NotRequired[int],
        "MaxContentSizePerPageInMegaBytes": NotRequired[float],
        "MaxUrlsPerMinuteCrawlRate": NotRequired[int],
        "UrlInclusionPatterns": NotRequired[Sequence[str]],
        "UrlExclusionPatterns": NotRequired[Sequence[str]],
        "ProxyConfiguration": NotRequired["ProxyConfigurationTypeDef"],
        "AuthenticationConfiguration": NotRequired["AuthenticationConfigurationTypeDef"],
    },
)

WorkDocsConfigurationTypeDef = TypedDict(
    "WorkDocsConfigurationTypeDef",
    {
        "OrganizationId": str,
        "CrawlComments": NotRequired[bool],
        "UseChangeLog": NotRequired[bool],
        "InclusionPatterns": NotRequired[Sequence[str]],
        "ExclusionPatterns": NotRequired[Sequence[str]],
        "FieldMappings": NotRequired[Sequence["DataSourceToIndexFieldMappingTypeDef"]],
    },
)
