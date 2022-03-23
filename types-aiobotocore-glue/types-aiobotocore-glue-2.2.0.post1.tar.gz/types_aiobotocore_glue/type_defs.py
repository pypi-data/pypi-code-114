"""
Type annotations for glue service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_glue/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_glue.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    BackfillErrorCodeType,
    BlueprintRunStateType,
    BlueprintStatusType,
    CatalogEncryptionModeType,
    CloudWatchEncryptionModeType,
    ColumnStatisticsTypeType,
    ComparatorType,
    CompatibilityType,
    ConnectionPropertyKeyType,
    ConnectionTypeType,
    CrawlerLineageSettingsType,
    CrawlerStateType,
    CrawlStateType,
    CsvHeaderOptionType,
    DataFormatType,
    DeleteBehaviorType,
    EnableHybridValuesType,
    ExistConditionType,
    JobBookmarksEncryptionModeType,
    JobRunStateType,
    LanguageType,
    LastCrawlStatusType,
    LogicalType,
    MLUserDataEncryptionModeStringType,
    NodeTypeType,
    PartitionIndexStatusType,
    PermissionType,
    PermissionTypeType,
    PrincipalTypeType,
    RecrawlBehaviorType,
    RegistryStatusType,
    ResourceShareTypeType,
    ResourceTypeType,
    S3EncryptionModeType,
    ScheduleStateType,
    SchemaStatusType,
    SchemaVersionStatusType,
    SortDirectionTypeType,
    SortType,
    TaskRunSortColumnTypeType,
    TaskStatusTypeType,
    TaskTypeType,
    TransformSortColumnTypeType,
    TransformStatusTypeType,
    TriggerStateType,
    TriggerTypeType,
    UpdateBehaviorType,
    WorkerTypeType,
    WorkflowRunStatusType,
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
    "ActionTypeDef",
    "AuditContextTypeDef",
    "BackfillErrorTypeDef",
    "BatchCreatePartitionRequestRequestTypeDef",
    "BatchCreatePartitionResponseTypeDef",
    "BatchDeleteConnectionRequestRequestTypeDef",
    "BatchDeleteConnectionResponseTypeDef",
    "BatchDeletePartitionRequestRequestTypeDef",
    "BatchDeletePartitionResponseTypeDef",
    "BatchDeleteTableRequestRequestTypeDef",
    "BatchDeleteTableResponseTypeDef",
    "BatchDeleteTableVersionRequestRequestTypeDef",
    "BatchDeleteTableVersionResponseTypeDef",
    "BatchGetBlueprintsRequestRequestTypeDef",
    "BatchGetBlueprintsResponseTypeDef",
    "BatchGetCrawlersRequestRequestTypeDef",
    "BatchGetCrawlersResponseTypeDef",
    "BatchGetDevEndpointsRequestRequestTypeDef",
    "BatchGetDevEndpointsResponseTypeDef",
    "BatchGetJobsRequestRequestTypeDef",
    "BatchGetJobsResponseTypeDef",
    "BatchGetPartitionRequestRequestTypeDef",
    "BatchGetPartitionResponseTypeDef",
    "BatchGetTriggersRequestRequestTypeDef",
    "BatchGetTriggersResponseTypeDef",
    "BatchGetWorkflowsRequestRequestTypeDef",
    "BatchGetWorkflowsResponseTypeDef",
    "BatchStopJobRunErrorTypeDef",
    "BatchStopJobRunRequestRequestTypeDef",
    "BatchStopJobRunResponseTypeDef",
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    "BatchUpdatePartitionFailureEntryTypeDef",
    "BatchUpdatePartitionRequestEntryTypeDef",
    "BatchUpdatePartitionRequestRequestTypeDef",
    "BatchUpdatePartitionResponseTypeDef",
    "BinaryColumnStatisticsDataTypeDef",
    "BlueprintDetailsTypeDef",
    "BlueprintRunTypeDef",
    "BlueprintTypeDef",
    "BooleanColumnStatisticsDataTypeDef",
    "CancelMLTaskRunRequestRequestTypeDef",
    "CancelMLTaskRunResponseTypeDef",
    "CatalogEntryTypeDef",
    "CatalogImportStatusTypeDef",
    "CatalogTargetTypeDef",
    "CheckSchemaVersionValidityInputRequestTypeDef",
    "CheckSchemaVersionValidityResponseTypeDef",
    "ClassifierTypeDef",
    "CloudWatchEncryptionTypeDef",
    "CodeGenEdgeTypeDef",
    "CodeGenNodeArgTypeDef",
    "CodeGenNodeTypeDef",
    "ColumnErrorTypeDef",
    "ColumnImportanceTypeDef",
    "ColumnRowFilterTypeDef",
    "ColumnStatisticsDataTypeDef",
    "ColumnStatisticsErrorTypeDef",
    "ColumnStatisticsTypeDef",
    "ColumnTypeDef",
    "ConditionTypeDef",
    "ConfusionMatrixTypeDef",
    "ConnectionInputTypeDef",
    "ConnectionPasswordEncryptionTypeDef",
    "ConnectionTypeDef",
    "ConnectionsListTypeDef",
    "CrawlTypeDef",
    "CrawlerMetricsTypeDef",
    "CrawlerNodeDetailsTypeDef",
    "CrawlerTargetsTypeDef",
    "CrawlerTypeDef",
    "CreateBlueprintRequestRequestTypeDef",
    "CreateBlueprintResponseTypeDef",
    "CreateClassifierRequestRequestTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateCrawlerRequestRequestTypeDef",
    "CreateCsvClassifierRequestTypeDef",
    "CreateDatabaseRequestRequestTypeDef",
    "CreateDevEndpointRequestRequestTypeDef",
    "CreateDevEndpointResponseTypeDef",
    "CreateGrokClassifierRequestTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJsonClassifierRequestTypeDef",
    "CreateMLTransformRequestRequestTypeDef",
    "CreateMLTransformResponseTypeDef",
    "CreatePartitionIndexRequestRequestTypeDef",
    "CreatePartitionRequestRequestTypeDef",
    "CreateRegistryInputRequestTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaInputRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateScriptRequestRequestTypeDef",
    "CreateScriptResponseTypeDef",
    "CreateSecurityConfigurationRequestRequestTypeDef",
    "CreateSecurityConfigurationResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTriggerRequestRequestTypeDef",
    "CreateTriggerResponseTypeDef",
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    "CreateWorkflowRequestRequestTypeDef",
    "CreateWorkflowResponseTypeDef",
    "CreateXMLClassifierRequestTypeDef",
    "CsvClassifierTypeDef",
    "DataCatalogEncryptionSettingsTypeDef",
    "DataLakePrincipalTypeDef",
    "DatabaseIdentifierTypeDef",
    "DatabaseInputTypeDef",
    "DatabaseTypeDef",
    "DateColumnStatisticsDataTypeDef",
    "DecimalColumnStatisticsDataTypeDef",
    "DecimalNumberTypeDef",
    "DeleteBlueprintRequestRequestTypeDef",
    "DeleteBlueprintResponseTypeDef",
    "DeleteClassifierRequestRequestTypeDef",
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteCrawlerRequestRequestTypeDef",
    "DeleteDatabaseRequestRequestTypeDef",
    "DeleteDevEndpointRequestRequestTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteMLTransformRequestRequestTypeDef",
    "DeleteMLTransformResponseTypeDef",
    "DeletePartitionIndexRequestRequestTypeDef",
    "DeletePartitionRequestRequestTypeDef",
    "DeleteRegistryInputRequestTypeDef",
    "DeleteRegistryResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSchemaInputRequestTypeDef",
    "DeleteSchemaResponseTypeDef",
    "DeleteSchemaVersionsInputRequestTypeDef",
    "DeleteSchemaVersionsResponseTypeDef",
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "DeleteTableVersionRequestRequestTypeDef",
    "DeleteTriggerRequestRequestTypeDef",
    "DeleteTriggerResponseTypeDef",
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    "DeleteWorkflowRequestRequestTypeDef",
    "DeleteWorkflowResponseTypeDef",
    "DeltaTargetTypeDef",
    "DevEndpointCustomLibrariesTypeDef",
    "DevEndpointTypeDef",
    "DoubleColumnStatisticsDataTypeDef",
    "DynamoDBTargetTypeDef",
    "EdgeTypeDef",
    "EncryptionAtRestTypeDef",
    "EncryptionConfigurationTypeDef",
    "ErrorDetailTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationMetricsTypeDef",
    "EventBatchingConditionTypeDef",
    "ExecutionPropertyTypeDef",
    "ExportLabelsTaskRunPropertiesTypeDef",
    "FindMatchesMetricsTypeDef",
    "FindMatchesParametersTypeDef",
    "FindMatchesTaskRunPropertiesTypeDef",
    "GetBlueprintRequestRequestTypeDef",
    "GetBlueprintResponseTypeDef",
    "GetBlueprintRunRequestRequestTypeDef",
    "GetBlueprintRunResponseTypeDef",
    "GetBlueprintRunsRequestRequestTypeDef",
    "GetBlueprintRunsResponseTypeDef",
    "GetCatalogImportStatusRequestRequestTypeDef",
    "GetCatalogImportStatusResponseTypeDef",
    "GetClassifierRequestRequestTypeDef",
    "GetClassifierResponseTypeDef",
    "GetClassifiersRequestRequestTypeDef",
    "GetClassifiersResponseTypeDef",
    "GetColumnStatisticsForPartitionRequestRequestTypeDef",
    "GetColumnStatisticsForPartitionResponseTypeDef",
    "GetColumnStatisticsForTableRequestRequestTypeDef",
    "GetColumnStatisticsForTableResponseTypeDef",
    "GetConnectionRequestRequestTypeDef",
    "GetConnectionResponseTypeDef",
    "GetConnectionsFilterTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCrawlerMetricsRequestRequestTypeDef",
    "GetCrawlerMetricsResponseTypeDef",
    "GetCrawlerRequestRequestTypeDef",
    "GetCrawlerResponseTypeDef",
    "GetCrawlersRequestRequestTypeDef",
    "GetCrawlersResponseTypeDef",
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    "GetDatabaseRequestRequestTypeDef",
    "GetDatabaseResponseTypeDef",
    "GetDatabasesRequestRequestTypeDef",
    "GetDatabasesResponseTypeDef",
    "GetDataflowGraphRequestRequestTypeDef",
    "GetDataflowGraphResponseTypeDef",
    "GetDevEndpointRequestRequestTypeDef",
    "GetDevEndpointResponseTypeDef",
    "GetDevEndpointsRequestRequestTypeDef",
    "GetDevEndpointsResponseTypeDef",
    "GetJobBookmarkRequestRequestTypeDef",
    "GetJobBookmarkResponseTypeDef",
    "GetJobRequestRequestTypeDef",
    "GetJobResponseTypeDef",
    "GetJobRunRequestRequestTypeDef",
    "GetJobRunResponseTypeDef",
    "GetJobRunsRequestRequestTypeDef",
    "GetJobRunsResponseTypeDef",
    "GetJobsRequestRequestTypeDef",
    "GetJobsResponseTypeDef",
    "GetMLTaskRunRequestRequestTypeDef",
    "GetMLTaskRunResponseTypeDef",
    "GetMLTaskRunsRequestRequestTypeDef",
    "GetMLTaskRunsResponseTypeDef",
    "GetMLTransformRequestRequestTypeDef",
    "GetMLTransformResponseTypeDef",
    "GetMLTransformsRequestRequestTypeDef",
    "GetMLTransformsResponseTypeDef",
    "GetMappingRequestRequestTypeDef",
    "GetMappingResponseTypeDef",
    "GetPartitionIndexesRequestRequestTypeDef",
    "GetPartitionIndexesResponseTypeDef",
    "GetPartitionRequestRequestTypeDef",
    "GetPartitionResponseTypeDef",
    "GetPartitionsRequestRequestTypeDef",
    "GetPartitionsResponseTypeDef",
    "GetPlanRequestRequestTypeDef",
    "GetPlanResponseTypeDef",
    "GetRegistryInputRequestTypeDef",
    "GetRegistryResponseTypeDef",
    "GetResourcePoliciesRequestRequestTypeDef",
    "GetResourcePoliciesResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSchemaByDefinitionInputRequestTypeDef",
    "GetSchemaByDefinitionResponseTypeDef",
    "GetSchemaInputRequestTypeDef",
    "GetSchemaResponseTypeDef",
    "GetSchemaVersionInputRequestTypeDef",
    "GetSchemaVersionResponseTypeDef",
    "GetSchemaVersionsDiffInputRequestTypeDef",
    "GetSchemaVersionsDiffResponseTypeDef",
    "GetSecurityConfigurationRequestRequestTypeDef",
    "GetSecurityConfigurationResponseTypeDef",
    "GetSecurityConfigurationsRequestRequestTypeDef",
    "GetSecurityConfigurationsResponseTypeDef",
    "GetTableRequestRequestTypeDef",
    "GetTableResponseTypeDef",
    "GetTableVersionRequestRequestTypeDef",
    "GetTableVersionResponseTypeDef",
    "GetTableVersionsRequestRequestTypeDef",
    "GetTableVersionsResponseTypeDef",
    "GetTablesRequestRequestTypeDef",
    "GetTablesResponseTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetTagsResponseTypeDef",
    "GetTriggerRequestRequestTypeDef",
    "GetTriggerResponseTypeDef",
    "GetTriggersRequestRequestTypeDef",
    "GetTriggersResponseTypeDef",
    "GetUnfilteredPartitionMetadataRequestRequestTypeDef",
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    "GetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    "GetUnfilteredTableMetadataRequestRequestTypeDef",
    "GetUnfilteredTableMetadataResponseTypeDef",
    "GetUserDefinedFunctionRequestRequestTypeDef",
    "GetUserDefinedFunctionResponseTypeDef",
    "GetUserDefinedFunctionsRequestRequestTypeDef",
    "GetUserDefinedFunctionsResponseTypeDef",
    "GetWorkflowRequestRequestTypeDef",
    "GetWorkflowResponseTypeDef",
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    "GetWorkflowRunPropertiesResponseTypeDef",
    "GetWorkflowRunRequestRequestTypeDef",
    "GetWorkflowRunResponseTypeDef",
    "GetWorkflowRunsRequestRequestTypeDef",
    "GetWorkflowRunsResponseTypeDef",
    "GluePolicyTypeDef",
    "GlueTableTypeDef",
    "GrokClassifierTypeDef",
    "ImportCatalogToGlueRequestRequestTypeDef",
    "ImportLabelsTaskRunPropertiesTypeDef",
    "JdbcTargetTypeDef",
    "JobBookmarkEntryTypeDef",
    "JobBookmarksEncryptionTypeDef",
    "JobCommandTypeDef",
    "JobNodeDetailsTypeDef",
    "JobRunTypeDef",
    "JobTypeDef",
    "JobUpdateTypeDef",
    "JsonClassifierTypeDef",
    "KeySchemaElementTypeDef",
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    "LakeFormationConfigurationTypeDef",
    "LastActiveDefinitionTypeDef",
    "LastCrawlInfoTypeDef",
    "LineageConfigurationTypeDef",
    "ListBlueprintsRequestRequestTypeDef",
    "ListBlueprintsResponseTypeDef",
    "ListCrawlersRequestRequestTypeDef",
    "ListCrawlersResponseTypeDef",
    "ListDevEndpointsRequestRequestTypeDef",
    "ListDevEndpointsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListMLTransformsRequestRequestTypeDef",
    "ListMLTransformsResponseTypeDef",
    "ListRegistriesInputRequestTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsInputRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasInputRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTriggersRequestRequestTypeDef",
    "ListTriggersResponseTypeDef",
    "ListWorkflowsRequestRequestTypeDef",
    "ListWorkflowsResponseTypeDef",
    "LocationTypeDef",
    "LongColumnStatisticsDataTypeDef",
    "MLTransformTypeDef",
    "MLUserDataEncryptionTypeDef",
    "MappingEntryTypeDef",
    "MetadataInfoTypeDef",
    "MetadataKeyValuePairTypeDef",
    "MongoDBTargetTypeDef",
    "NodeTypeDef",
    "NotificationPropertyTypeDef",
    "OrderTypeDef",
    "OtherMetadataValueListItemTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionErrorTypeDef",
    "PartitionIndexDescriptorTypeDef",
    "PartitionIndexTypeDef",
    "PartitionInputTypeDef",
    "PartitionTypeDef",
    "PartitionValueListTypeDef",
    "PhysicalConnectionRequirementsTypeDef",
    "PredecessorTypeDef",
    "PredicateTypeDef",
    "PrincipalPermissionsTypeDef",
    "PropertyPredicateTypeDef",
    "PutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSchemaVersionMetadataInputRequestTypeDef",
    "PutSchemaVersionMetadataResponseTypeDef",
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    "QuerySchemaVersionMetadataResponseTypeDef",
    "RecrawlPolicyTypeDef",
    "RegisterSchemaVersionInputRequestTypeDef",
    "RegisterSchemaVersionResponseTypeDef",
    "RegistryIdTypeDef",
    "RegistryListItemTypeDef",
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    "RemoveSchemaVersionMetadataResponseTypeDef",
    "ResetJobBookmarkRequestRequestTypeDef",
    "ResetJobBookmarkResponseTypeDef",
    "ResourceUriTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeWorkflowRunRequestRequestTypeDef",
    "ResumeWorkflowRunResponseTypeDef",
    "S3EncryptionTypeDef",
    "S3TargetTypeDef",
    "ScheduleTypeDef",
    "SchemaChangePolicyTypeDef",
    "SchemaColumnTypeDef",
    "SchemaIdTypeDef",
    "SchemaListItemTypeDef",
    "SchemaReferenceTypeDef",
    "SchemaVersionErrorItemTypeDef",
    "SchemaVersionListItemTypeDef",
    "SchemaVersionNumberTypeDef",
    "SearchTablesRequestRequestTypeDef",
    "SearchTablesResponseTypeDef",
    "SecurityConfigurationTypeDef",
    "SegmentTypeDef",
    "SerDeInfoTypeDef",
    "SkewedInfoTypeDef",
    "SortCriterionTypeDef",
    "StartBlueprintRunRequestRequestTypeDef",
    "StartBlueprintRunResponseTypeDef",
    "StartCrawlerRequestRequestTypeDef",
    "StartCrawlerScheduleRequestRequestTypeDef",
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    "StartExportLabelsTaskRunResponseTypeDef",
    "StartImportLabelsTaskRunRequestRequestTypeDef",
    "StartImportLabelsTaskRunResponseTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    "StartMLEvaluationTaskRunResponseTypeDef",
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    "StartTriggerRequestRequestTypeDef",
    "StartTriggerResponseTypeDef",
    "StartWorkflowRunRequestRequestTypeDef",
    "StartWorkflowRunResponseTypeDef",
    "StartingEventBatchConditionTypeDef",
    "StopCrawlerRequestRequestTypeDef",
    "StopCrawlerScheduleRequestRequestTypeDef",
    "StopTriggerRequestRequestTypeDef",
    "StopTriggerResponseTypeDef",
    "StopWorkflowRunRequestRequestTypeDef",
    "StorageDescriptorTypeDef",
    "StringColumnStatisticsDataTypeDef",
    "TableErrorTypeDef",
    "TableIdentifierTypeDef",
    "TableInputTypeDef",
    "TableTypeDef",
    "TableVersionErrorTypeDef",
    "TableVersionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TaskRunFilterCriteriaTypeDef",
    "TaskRunPropertiesTypeDef",
    "TaskRunSortCriteriaTypeDef",
    "TaskRunTypeDef",
    "TransformEncryptionTypeDef",
    "TransformFilterCriteriaTypeDef",
    "TransformParametersTypeDef",
    "TransformSortCriteriaTypeDef",
    "TriggerNodeDetailsTypeDef",
    "TriggerTypeDef",
    "TriggerUpdateTypeDef",
    "UnfilteredPartitionTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBlueprintRequestRequestTypeDef",
    "UpdateBlueprintResponseTypeDef",
    "UpdateClassifierRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    "UpdateColumnStatisticsForTableResponseTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateCrawlerRequestRequestTypeDef",
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    "UpdateCsvClassifierRequestTypeDef",
    "UpdateDatabaseRequestRequestTypeDef",
    "UpdateDevEndpointRequestRequestTypeDef",
    "UpdateGrokClassifierRequestTypeDef",
    "UpdateJobRequestRequestTypeDef",
    "UpdateJobResponseTypeDef",
    "UpdateJsonClassifierRequestTypeDef",
    "UpdateMLTransformRequestRequestTypeDef",
    "UpdateMLTransformResponseTypeDef",
    "UpdatePartitionRequestRequestTypeDef",
    "UpdateRegistryInputRequestTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaInputRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "UpdateTriggerRequestRequestTypeDef",
    "UpdateTriggerResponseTypeDef",
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    "UpdateWorkflowRequestRequestTypeDef",
    "UpdateWorkflowResponseTypeDef",
    "UpdateXMLClassifierRequestTypeDef",
    "UserDefinedFunctionInputTypeDef",
    "UserDefinedFunctionTypeDef",
    "WorkflowGraphTypeDef",
    "WorkflowRunStatisticsTypeDef",
    "WorkflowRunTypeDef",
    "WorkflowTypeDef",
    "XMLClassifierTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "JobName": NotRequired[str],
        "Arguments": NotRequired[Dict[str, str]],
        "Timeout": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "CrawlerName": NotRequired[str],
    },
)

AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": NotRequired[str],
    },
)

BackfillErrorTypeDef = TypedDict(
    "BackfillErrorTypeDef",
    {
        "Code": NotRequired[BackfillErrorCodeType],
        "Partitions": NotRequired[List["PartitionValueListTypeDef"]],
    },
)

BatchCreatePartitionRequestRequestTypeDef = TypedDict(
    "BatchCreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInputList": Sequence["PartitionInputTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchCreatePartitionResponseTypeDef = TypedDict(
    "BatchCreatePartitionResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteConnectionRequestRequestTypeDef = TypedDict(
    "BatchDeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionNameList": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

BatchDeleteConnectionResponseTypeDef = TypedDict(
    "BatchDeleteConnectionResponseTypeDef",
    {
        "Succeeded": List[str],
        "Errors": Dict[str, "ErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePartitionRequestRequestTypeDef = TypedDict(
    "BatchDeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToDelete": Sequence["PartitionValueListTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchDeletePartitionResponseTypeDef = TypedDict(
    "BatchDeletePartitionResponseTypeDef",
    {
        "Errors": List["PartitionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteTableRequestRequestTypeDef = TypedDict(
    "BatchDeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TablesToDelete": Sequence[str],
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)

BatchDeleteTableResponseTypeDef = TypedDict(
    "BatchDeleteTableResponseTypeDef",
    {
        "Errors": List["TableErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteTableVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionIds": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

BatchDeleteTableVersionResponseTypeDef = TypedDict(
    "BatchDeleteTableVersionResponseTypeDef",
    {
        "Errors": List["TableVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetBlueprintsRequestRequestTypeDef = TypedDict(
    "BatchGetBlueprintsRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "IncludeBlueprint": NotRequired[bool],
        "IncludeParameterSpec": NotRequired[bool],
    },
)

BatchGetBlueprintsResponseTypeDef = TypedDict(
    "BatchGetBlueprintsResponseTypeDef",
    {
        "Blueprints": List["BlueprintTypeDef"],
        "MissingBlueprints": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetCrawlersRequestRequestTypeDef = TypedDict(
    "BatchGetCrawlersRequestRequestTypeDef",
    {
        "CrawlerNames": Sequence[str],
    },
)

BatchGetCrawlersResponseTypeDef = TypedDict(
    "BatchGetCrawlersResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "CrawlersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetDevEndpointsRequestRequestTypeDef = TypedDict(
    "BatchGetDevEndpointsRequestRequestTypeDef",
    {
        "DevEndpointNames": Sequence[str],
    },
)

BatchGetDevEndpointsResponseTypeDef = TypedDict(
    "BatchGetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "DevEndpointsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetJobsRequestRequestTypeDef = TypedDict(
    "BatchGetJobsRequestRequestTypeDef",
    {
        "JobNames": Sequence[str],
    },
)

BatchGetJobsResponseTypeDef = TypedDict(
    "BatchGetJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "JobsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetPartitionRequestRequestTypeDef = TypedDict(
    "BatchGetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionsToGet": Sequence["PartitionValueListTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchGetPartitionResponseTypeDef = TypedDict(
    "BatchGetPartitionResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "UnprocessedKeys": List["PartitionValueListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetTriggersRequestRequestTypeDef = TypedDict(
    "BatchGetTriggersRequestRequestTypeDef",
    {
        "TriggerNames": Sequence[str],
    },
)

BatchGetTriggersResponseTypeDef = TypedDict(
    "BatchGetTriggersResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "TriggersNotFound": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetWorkflowsRequestRequestTypeDef = TypedDict(
    "BatchGetWorkflowsRequestRequestTypeDef",
    {
        "Names": Sequence[str],
        "IncludeGraph": NotRequired[bool],
    },
)

BatchGetWorkflowsResponseTypeDef = TypedDict(
    "BatchGetWorkflowsResponseTypeDef",
    {
        "Workflows": List["WorkflowTypeDef"],
        "MissingWorkflows": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunErrorTypeDef = TypedDict(
    "BatchStopJobRunErrorTypeDef",
    {
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
        "ErrorDetail": NotRequired["ErrorDetailTypeDef"],
    },
)

BatchStopJobRunRequestRequestTypeDef = TypedDict(
    "BatchStopJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "JobRunIds": Sequence[str],
    },
)

BatchStopJobRunResponseTypeDef = TypedDict(
    "BatchStopJobRunResponseTypeDef",
    {
        "SuccessfulSubmissions": List["BatchStopJobRunSuccessfulSubmissionTypeDef"],
        "Errors": List["BatchStopJobRunErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchStopJobRunSuccessfulSubmissionTypeDef = TypedDict(
    "BatchStopJobRunSuccessfulSubmissionTypeDef",
    {
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
    },
)

BatchUpdatePartitionFailureEntryTypeDef = TypedDict(
    "BatchUpdatePartitionFailureEntryTypeDef",
    {
        "PartitionValueList": NotRequired[List[str]],
        "ErrorDetail": NotRequired["ErrorDetailTypeDef"],
    },
)

BatchUpdatePartitionRequestEntryTypeDef = TypedDict(
    "BatchUpdatePartitionRequestEntryTypeDef",
    {
        "PartitionValueList": Sequence[str],
        "PartitionInput": "PartitionInputTypeDef",
    },
)

BatchUpdatePartitionRequestRequestTypeDef = TypedDict(
    "BatchUpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "Entries": Sequence["BatchUpdatePartitionRequestEntryTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchUpdatePartitionResponseTypeDef = TypedDict(
    "BatchUpdatePartitionResponseTypeDef",
    {
        "Errors": List["BatchUpdatePartitionFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BinaryColumnStatisticsDataTypeDef = TypedDict(
    "BinaryColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
    },
)

BlueprintDetailsTypeDef = TypedDict(
    "BlueprintDetailsTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "RunId": NotRequired[str],
    },
)

BlueprintRunTypeDef = TypedDict(
    "BlueprintRunTypeDef",
    {
        "BlueprintName": NotRequired[str],
        "RunId": NotRequired[str],
        "WorkflowName": NotRequired[str],
        "State": NotRequired[BlueprintRunStateType],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "RollbackErrorMessage": NotRequired[str],
        "Parameters": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "ParameterSpec": NotRequired[str],
        "BlueprintLocation": NotRequired[str],
        "BlueprintServiceLocation": NotRequired[str],
        "Status": NotRequired[BlueprintStatusType],
        "ErrorMessage": NotRequired[str],
        "LastActiveDefinition": NotRequired["LastActiveDefinitionTypeDef"],
    },
)

BooleanColumnStatisticsDataTypeDef = TypedDict(
    "BooleanColumnStatisticsDataTypeDef",
    {
        "NumberOfTrues": int,
        "NumberOfFalses": int,
        "NumberOfNulls": int,
    },
)

CancelMLTaskRunRequestRequestTypeDef = TypedDict(
    "CancelMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

CancelMLTaskRunResponseTypeDef = TypedDict(
    "CancelMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CatalogEntryTypeDef = TypedDict(
    "CatalogEntryTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
    },
)

CatalogImportStatusTypeDef = TypedDict(
    "CatalogImportStatusTypeDef",
    {
        "ImportCompleted": NotRequired[bool],
        "ImportTime": NotRequired[datetime],
        "ImportedBy": NotRequired[str],
    },
)

CatalogTargetTypeDef = TypedDict(
    "CatalogTargetTypeDef",
    {
        "DatabaseName": str,
        "Tables": List[str],
        "ConnectionName": NotRequired[str],
    },
)

CheckSchemaVersionValidityInputRequestTypeDef = TypedDict(
    "CheckSchemaVersionValidityInputRequestTypeDef",
    {
        "DataFormat": DataFormatType,
        "SchemaDefinition": str,
    },
)

CheckSchemaVersionValidityResponseTypeDef = TypedDict(
    "CheckSchemaVersionValidityResponseTypeDef",
    {
        "Valid": bool,
        "Error": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ClassifierTypeDef = TypedDict(
    "ClassifierTypeDef",
    {
        "GrokClassifier": NotRequired["GrokClassifierTypeDef"],
        "XMLClassifier": NotRequired["XMLClassifierTypeDef"],
        "JsonClassifier": NotRequired["JsonClassifierTypeDef"],
        "CsvClassifier": NotRequired["CsvClassifierTypeDef"],
    },
)

CloudWatchEncryptionTypeDef = TypedDict(
    "CloudWatchEncryptionTypeDef",
    {
        "CloudWatchEncryptionMode": NotRequired[CloudWatchEncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)

CodeGenEdgeTypeDef = TypedDict(
    "CodeGenEdgeTypeDef",
    {
        "Source": str,
        "Target": str,
        "TargetParameter": NotRequired[str],
    },
)

CodeGenNodeArgTypeDef = TypedDict(
    "CodeGenNodeArgTypeDef",
    {
        "Name": str,
        "Value": str,
        "Param": NotRequired[bool],
    },
)

CodeGenNodeTypeDef = TypedDict(
    "CodeGenNodeTypeDef",
    {
        "Id": str,
        "NodeType": str,
        "Args": Sequence["CodeGenNodeArgTypeDef"],
        "LineNumber": NotRequired[int],
    },
)

ColumnErrorTypeDef = TypedDict(
    "ColumnErrorTypeDef",
    {
        "ColumnName": NotRequired[str],
        "Error": NotRequired["ErrorDetailTypeDef"],
    },
)

ColumnImportanceTypeDef = TypedDict(
    "ColumnImportanceTypeDef",
    {
        "ColumnName": NotRequired[str],
        "Importance": NotRequired[float],
    },
)

ColumnRowFilterTypeDef = TypedDict(
    "ColumnRowFilterTypeDef",
    {
        "ColumnName": NotRequired[str],
        "RowFilterExpression": NotRequired[str],
    },
)

ColumnStatisticsDataTypeDef = TypedDict(
    "ColumnStatisticsDataTypeDef",
    {
        "Type": ColumnStatisticsTypeType,
        "BooleanColumnStatisticsData": NotRequired["BooleanColumnStatisticsDataTypeDef"],
        "DateColumnStatisticsData": NotRequired["DateColumnStatisticsDataTypeDef"],
        "DecimalColumnStatisticsData": NotRequired["DecimalColumnStatisticsDataTypeDef"],
        "DoubleColumnStatisticsData": NotRequired["DoubleColumnStatisticsDataTypeDef"],
        "LongColumnStatisticsData": NotRequired["LongColumnStatisticsDataTypeDef"],
        "StringColumnStatisticsData": NotRequired["StringColumnStatisticsDataTypeDef"],
        "BinaryColumnStatisticsData": NotRequired["BinaryColumnStatisticsDataTypeDef"],
    },
)

ColumnStatisticsErrorTypeDef = TypedDict(
    "ColumnStatisticsErrorTypeDef",
    {
        "ColumnStatistics": NotRequired["ColumnStatisticsTypeDef"],
        "Error": NotRequired["ErrorDetailTypeDef"],
    },
)

ColumnStatisticsTypeDef = TypedDict(
    "ColumnStatisticsTypeDef",
    {
        "ColumnName": str,
        "ColumnType": str,
        "AnalyzedTime": datetime,
        "StatisticsData": "ColumnStatisticsDataTypeDef",
    },
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

ConditionTypeDef = TypedDict(
    "ConditionTypeDef",
    {
        "LogicalOperator": NotRequired[Literal["EQUALS"]],
        "JobName": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "CrawlerName": NotRequired[str],
        "CrawlState": NotRequired[CrawlStateType],
    },
)

ConfusionMatrixTypeDef = TypedDict(
    "ConfusionMatrixTypeDef",
    {
        "NumTruePositives": NotRequired[int],
        "NumFalsePositives": NotRequired[int],
        "NumTrueNegatives": NotRequired[int],
        "NumFalseNegatives": NotRequired[int],
    },
)

ConnectionInputTypeDef = TypedDict(
    "ConnectionInputTypeDef",
    {
        "Name": str,
        "ConnectionType": ConnectionTypeType,
        "ConnectionProperties": Mapping[ConnectionPropertyKeyType, str],
        "Description": NotRequired[str],
        "MatchCriteria": NotRequired[Sequence[str]],
        "PhysicalConnectionRequirements": NotRequired["PhysicalConnectionRequirementsTypeDef"],
    },
)

ConnectionPasswordEncryptionTypeDef = TypedDict(
    "ConnectionPasswordEncryptionTypeDef",
    {
        "ReturnConnectionPasswordEncrypted": bool,
        "AwsKmsKeyId": NotRequired[str],
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ConnectionType": NotRequired[ConnectionTypeType],
        "MatchCriteria": NotRequired[List[str]],
        "ConnectionProperties": NotRequired[Dict[ConnectionPropertyKeyType, str]],
        "PhysicalConnectionRequirements": NotRequired["PhysicalConnectionRequirementsTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "LastUpdatedBy": NotRequired[str],
    },
)

ConnectionsListTypeDef = TypedDict(
    "ConnectionsListTypeDef",
    {
        "Connections": NotRequired[List[str]],
    },
)

CrawlTypeDef = TypedDict(
    "CrawlTypeDef",
    {
        "State": NotRequired[CrawlStateType],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ErrorMessage": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LogStream": NotRequired[str],
    },
)

CrawlerMetricsTypeDef = TypedDict(
    "CrawlerMetricsTypeDef",
    {
        "CrawlerName": NotRequired[str],
        "TimeLeftSeconds": NotRequired[float],
        "StillEstimating": NotRequired[bool],
        "LastRuntimeSeconds": NotRequired[float],
        "MedianRuntimeSeconds": NotRequired[float],
        "TablesCreated": NotRequired[int],
        "TablesUpdated": NotRequired[int],
        "TablesDeleted": NotRequired[int],
    },
)

CrawlerNodeDetailsTypeDef = TypedDict(
    "CrawlerNodeDetailsTypeDef",
    {
        "Crawls": NotRequired[List["CrawlTypeDef"]],
    },
)

CrawlerTargetsTypeDef = TypedDict(
    "CrawlerTargetsTypeDef",
    {
        "S3Targets": NotRequired[List["S3TargetTypeDef"]],
        "JdbcTargets": NotRequired[List["JdbcTargetTypeDef"]],
        "MongoDBTargets": NotRequired[List["MongoDBTargetTypeDef"]],
        "DynamoDBTargets": NotRequired[List["DynamoDBTargetTypeDef"]],
        "CatalogTargets": NotRequired[List["CatalogTargetTypeDef"]],
        "DeltaTargets": NotRequired[List["DeltaTargetTypeDef"]],
    },
)

CrawlerTypeDef = TypedDict(
    "CrawlerTypeDef",
    {
        "Name": NotRequired[str],
        "Role": NotRequired[str],
        "Targets": NotRequired["CrawlerTargetsTypeDef"],
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Classifiers": NotRequired[List[str]],
        "RecrawlPolicy": NotRequired["RecrawlPolicyTypeDef"],
        "SchemaChangePolicy": NotRequired["SchemaChangePolicyTypeDef"],
        "LineageConfiguration": NotRequired["LineageConfigurationTypeDef"],
        "State": NotRequired[CrawlerStateType],
        "TablePrefix": NotRequired[str],
        "Schedule": NotRequired["ScheduleTypeDef"],
        "CrawlElapsedTime": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "LastCrawl": NotRequired["LastCrawlInfoTypeDef"],
        "Version": NotRequired[int],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
        "LakeFormationConfiguration": NotRequired["LakeFormationConfigurationTypeDef"],
    },
)

CreateBlueprintRequestRequestTypeDef = TypedDict(
    "CreateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateBlueprintResponseTypeDef = TypedDict(
    "CreateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateClassifierRequestRequestTypeDef = TypedDict(
    "CreateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": NotRequired["CreateGrokClassifierRequestTypeDef"],
        "XMLClassifier": NotRequired["CreateXMLClassifierRequestTypeDef"],
        "JsonClassifier": NotRequired["CreateJsonClassifierRequestTypeDef"],
        "CsvClassifier": NotRequired["CreateCsvClassifierRequestTypeDef"],
    },
)

CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "ConnectionInput": "ConnectionInputTypeDef",
        "CatalogId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateCrawlerRequestRequestTypeDef = TypedDict(
    "CreateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Targets": "CrawlerTargetsTypeDef",
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Classifiers": NotRequired[Sequence[str]],
        "TablePrefix": NotRequired[str],
        "SchemaChangePolicy": NotRequired["SchemaChangePolicyTypeDef"],
        "RecrawlPolicy": NotRequired["RecrawlPolicyTypeDef"],
        "LineageConfiguration": NotRequired["LineageConfigurationTypeDef"],
        "LakeFormationConfiguration": NotRequired["LakeFormationConfigurationTypeDef"],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateCsvClassifierRequestTypeDef = TypedDict(
    "CreateCsvClassifierRequestTypeDef",
    {
        "Name": str,
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[Sequence[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
    },
)

CreateDatabaseRequestRequestTypeDef = TypedDict(
    "CreateDatabaseRequestRequestTypeDef",
    {
        "DatabaseInput": "DatabaseInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

CreateDevEndpointRequestRequestTypeDef = TypedDict(
    "CreateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "RoleArn": str,
        "SecurityGroupIds": NotRequired[Sequence[str]],
        "SubnetId": NotRequired[str],
        "PublicKey": NotRequired[str],
        "PublicKeys": NotRequired[Sequence[str]],
        "NumberOfNodes": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
        "SecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "Arguments": NotRequired[Mapping[str, str]],
    },
)

CreateDevEndpointResponseTypeDef = TypedDict(
    "CreateDevEndpointResponseTypeDef",
    {
        "EndpointName": str,
        "Status": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "RoleArn": str,
        "YarnEndpointAddress": str,
        "ZeppelinRemoteSparkInterpreterPort": int,
        "NumberOfNodes": int,
        "WorkerType": WorkerTypeType,
        "GlueVersion": str,
        "NumberOfWorkers": int,
        "AvailabilityZone": str,
        "VpcId": str,
        "ExtraPythonLibsS3Path": str,
        "ExtraJarsS3Path": str,
        "FailureReason": str,
        "SecurityConfiguration": str,
        "CreatedTimestamp": datetime,
        "Arguments": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGrokClassifierRequestTypeDef = TypedDict(
    "CreateGrokClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "GrokPattern": str,
        "CustomPatterns": NotRequired[str],
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "Name": str,
        "Role": str,
        "Command": "JobCommandTypeDef",
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "ExecutionProperty": NotRequired["ExecutionPropertyTypeDef"],
        "DefaultArguments": NotRequired[Mapping[str, str]],
        "NonOverridableArguments": NotRequired[Mapping[str, str]],
        "Connections": NotRequired["ConnectionsListTypeDef"],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "WorkerType": NotRequired[WorkerTypeType],
    },
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateJsonClassifierRequestTypeDef = TypedDict(
    "CreateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": str,
    },
)

CreateMLTransformRequestRequestTypeDef = TypedDict(
    "CreateMLTransformRequestRequestTypeDef",
    {
        "Name": str,
        "InputRecordTables": Sequence["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "Role": str,
        "Description": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "TransformEncryption": NotRequired["TransformEncryptionTypeDef"],
    },
)

CreateMLTransformResponseTypeDef = TypedDict(
    "CreateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePartitionIndexRequestRequestTypeDef = TypedDict(
    "CreatePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionIndex": "PartitionIndexTypeDef",
        "CatalogId": NotRequired[str],
    },
)

CreatePartitionRequestRequestTypeDef = TypedDict(
    "CreatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionInput": "PartitionInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

CreateRegistryInputRequestTypeDef = TypedDict(
    "CreateRegistryInputRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "RegistryArn": str,
        "RegistryName": str,
        "Description": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaInputRequestTypeDef = TypedDict(
    "CreateSchemaInputRequestTypeDef",
    {
        "SchemaName": str,
        "DataFormat": DataFormatType,
        "RegistryId": NotRequired["RegistryIdTypeDef"],
        "Compatibility": NotRequired[CompatibilityType],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
        "SchemaDefinition": NotRequired[str],
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "Tags": Dict[str, str],
        "SchemaVersionId": str,
        "SchemaVersionStatus": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptRequestRequestTypeDef = TypedDict(
    "CreateScriptRequestRequestTypeDef",
    {
        "DagNodes": NotRequired[Sequence["CodeGenNodeTypeDef"]],
        "DagEdges": NotRequired[Sequence["CodeGenEdgeTypeDef"]],
        "Language": NotRequired[LanguageType],
    },
)

CreateScriptResponseTypeDef = TypedDict(
    "CreateScriptResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "CreateSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
        "EncryptionConfiguration": "EncryptionConfigurationTypeDef",
    },
)

CreateSecurityConfigurationResponseTypeDef = TypedDict(
    "CreateSecurityConfigurationResponseTypeDef",
    {
        "Name": str,
        "CreatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
        "CatalogId": NotRequired[str],
        "PartitionIndexes": NotRequired[Sequence["PartitionIndexTypeDef"]],
        "TransactionId": NotRequired[str],
    },
)

CreateTriggerRequestRequestTypeDef = TypedDict(
    "CreateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "Type": TriggerTypeType,
        "Actions": Sequence["ActionTypeDef"],
        "WorkflowName": NotRequired[str],
        "Schedule": NotRequired[str],
        "Predicate": NotRequired["PredicateTypeDef"],
        "Description": NotRequired[str],
        "StartOnCreation": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
        "EventBatchingCondition": NotRequired["EventBatchingConditionTypeDef"],
    },
)

CreateTriggerResponseTypeDef = TypedDict(
    "CreateTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "CreateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

CreateWorkflowRequestRequestTypeDef = TypedDict(
    "CreateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Mapping[str, str]],
        "MaxConcurrentRuns": NotRequired[int],
    },
)

CreateWorkflowResponseTypeDef = TypedDict(
    "CreateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateXMLClassifierRequestTypeDef = TypedDict(
    "CreateXMLClassifierRequestTypeDef",
    {
        "Classification": str,
        "Name": str,
        "RowTag": NotRequired[str],
    },
)

CsvClassifierTypeDef = TypedDict(
    "CsvClassifierTypeDef",
    {
        "Name": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[List[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
    },
)

DataCatalogEncryptionSettingsTypeDef = TypedDict(
    "DataCatalogEncryptionSettingsTypeDef",
    {
        "EncryptionAtRest": NotRequired["EncryptionAtRestTypeDef"],
        "ConnectionPasswordEncryption": NotRequired["ConnectionPasswordEncryptionTypeDef"],
    },
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": NotRequired[str],
    },
)

DatabaseIdentifierTypeDef = TypedDict(
    "DatabaseIdentifierTypeDef",
    {
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
    },
)

DatabaseInputTypeDef = TypedDict(
    "DatabaseInputTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "LocationUri": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "CreateTableDefaultPermissions": NotRequired[Sequence["PrincipalPermissionsTypeDef"]],
        "TargetDatabase": NotRequired["DatabaseIdentifierTypeDef"],
    },
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "LocationUri": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "CreateTime": NotRequired[datetime],
        "CreateTableDefaultPermissions": NotRequired[List["PrincipalPermissionsTypeDef"]],
        "TargetDatabase": NotRequired["DatabaseIdentifierTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

DateColumnStatisticsDataTypeDef = TypedDict(
    "DateColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[datetime],
        "MaximumValue": NotRequired[datetime],
    },
)

DecimalColumnStatisticsDataTypeDef = TypedDict(
    "DecimalColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired["DecimalNumberTypeDef"],
        "MaximumValue": NotRequired["DecimalNumberTypeDef"],
    },
)

DecimalNumberTypeDef = TypedDict(
    "DecimalNumberTypeDef",
    {
        "UnscaledValue": bytes,
        "Scale": int,
    },
)

DeleteBlueprintRequestRequestTypeDef = TypedDict(
    "DeleteBlueprintRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteBlueprintResponseTypeDef = TypedDict(
    "DeleteBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteClassifierRequestRequestTypeDef = TypedDict(
    "DeleteClassifierRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "DeleteColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnName": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "DeleteColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnName": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "ConnectionName": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteCrawlerRequestRequestTypeDef = TypedDict(
    "DeleteCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDatabaseRequestRequestTypeDef = TypedDict(
    "DeleteDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteDevEndpointRequestRequestTypeDef = TypedDict(
    "DeleteDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMLTransformRequestRequestTypeDef = TypedDict(
    "DeleteMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

DeleteMLTransformResponseTypeDef = TypedDict(
    "DeleteMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePartitionIndexRequestRequestTypeDef = TypedDict(
    "DeletePartitionIndexRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "IndexName": str,
        "CatalogId": NotRequired[str],
    },
)

DeletePartitionRequestRequestTypeDef = TypedDict(
    "DeletePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

DeleteRegistryInputRequestTypeDef = TypedDict(
    "DeleteRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

DeleteRegistryResponseTypeDef = TypedDict(
    "DeleteRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Status": RegistryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "PolicyHashCondition": NotRequired[str],
        "ResourceArn": NotRequired[str],
    },
)

DeleteSchemaInputRequestTypeDef = TypedDict(
    "DeleteSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

DeleteSchemaResponseTypeDef = TypedDict(
    "DeleteSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "Status": SchemaStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSchemaVersionsInputRequestTypeDef = TypedDict(
    "DeleteSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "Versions": str,
    },
)

DeleteSchemaVersionsResponseTypeDef = TypedDict(
    "DeleteSchemaVersionsResponseTypeDef",
    {
        "SchemaVersionErrors": List["SchemaVersionErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)

DeleteTableVersionRequestRequestTypeDef = TypedDict(
    "DeleteTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "VersionId": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteTriggerRequestRequestTypeDef = TypedDict(
    "DeleteTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteTriggerResponseTypeDef = TypedDict(
    "DeleteTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "DeleteUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteWorkflowRequestRequestTypeDef = TypedDict(
    "DeleteWorkflowRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteWorkflowResponseTypeDef = TypedDict(
    "DeleteWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeltaTargetTypeDef = TypedDict(
    "DeltaTargetTypeDef",
    {
        "DeltaTables": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "WriteManifest": NotRequired[bool],
    },
)

DevEndpointCustomLibrariesTypeDef = TypedDict(
    "DevEndpointCustomLibrariesTypeDef",
    {
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
    },
)

DevEndpointTypeDef = TypedDict(
    "DevEndpointTypeDef",
    {
        "EndpointName": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SecurityGroupIds": NotRequired[List[str]],
        "SubnetId": NotRequired[str],
        "YarnEndpointAddress": NotRequired[str],
        "PrivateAddress": NotRequired[str],
        "ZeppelinRemoteSparkInterpreterPort": NotRequired[int],
        "PublicAddress": NotRequired[str],
        "Status": NotRequired[str],
        "WorkerType": NotRequired[WorkerTypeType],
        "GlueVersion": NotRequired[str],
        "NumberOfWorkers": NotRequired[int],
        "NumberOfNodes": NotRequired[int],
        "AvailabilityZone": NotRequired[str],
        "VpcId": NotRequired[str],
        "ExtraPythonLibsS3Path": NotRequired[str],
        "ExtraJarsS3Path": NotRequired[str],
        "FailureReason": NotRequired[str],
        "LastUpdateStatus": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastModifiedTimestamp": NotRequired[datetime],
        "PublicKey": NotRequired[str],
        "PublicKeys": NotRequired[List[str]],
        "SecurityConfiguration": NotRequired[str],
        "Arguments": NotRequired[Dict[str, str]],
    },
)

DoubleColumnStatisticsDataTypeDef = TypedDict(
    "DoubleColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[float],
        "MaximumValue": NotRequired[float],
    },
)

DynamoDBTargetTypeDef = TypedDict(
    "DynamoDBTargetTypeDef",
    {
        "Path": NotRequired[str],
        "scanAll": NotRequired[bool],
        "scanRate": NotRequired[float],
    },
)

EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "SourceId": NotRequired[str],
        "DestinationId": NotRequired[str],
    },
)

EncryptionAtRestTypeDef = TypedDict(
    "EncryptionAtRestTypeDef",
    {
        "CatalogEncryptionMode": CatalogEncryptionModeType,
        "SseAwsKmsKeyId": NotRequired[str],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "S3Encryption": NotRequired[Sequence["S3EncryptionTypeDef"]],
        "CloudWatchEncryption": NotRequired["CloudWatchEncryptionTypeDef"],
        "JobBookmarksEncryption": NotRequired["JobBookmarksEncryptionTypeDef"],
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

EvaluationMetricsTypeDef = TypedDict(
    "EvaluationMetricsTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
        "FindMatchesMetrics": NotRequired["FindMatchesMetricsTypeDef"],
    },
)

EventBatchingConditionTypeDef = TypedDict(
    "EventBatchingConditionTypeDef",
    {
        "BatchSize": int,
        "BatchWindow": NotRequired[int],
    },
)

ExecutionPropertyTypeDef = TypedDict(
    "ExecutionPropertyTypeDef",
    {
        "MaxConcurrentRuns": NotRequired[int],
    },
)

ExportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ExportLabelsTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": NotRequired[str],
    },
)

FindMatchesMetricsTypeDef = TypedDict(
    "FindMatchesMetricsTypeDef",
    {
        "AreaUnderPRCurve": NotRequired[float],
        "Precision": NotRequired[float],
        "Recall": NotRequired[float],
        "F1": NotRequired[float],
        "ConfusionMatrix": NotRequired["ConfusionMatrixTypeDef"],
        "ColumnImportances": NotRequired[List["ColumnImportanceTypeDef"]],
    },
)

FindMatchesParametersTypeDef = TypedDict(
    "FindMatchesParametersTypeDef",
    {
        "PrimaryKeyColumnName": NotRequired[str],
        "PrecisionRecallTradeoff": NotRequired[float],
        "AccuracyCostTradeoff": NotRequired[float],
        "EnforceProvidedLabels": NotRequired[bool],
    },
)

FindMatchesTaskRunPropertiesTypeDef = TypedDict(
    "FindMatchesTaskRunPropertiesTypeDef",
    {
        "JobId": NotRequired[str],
        "JobName": NotRequired[str],
        "JobRunId": NotRequired[str],
    },
)

GetBlueprintRequestRequestTypeDef = TypedDict(
    "GetBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeBlueprint": NotRequired[bool],
        "IncludeParameterSpec": NotRequired[bool],
    },
)

GetBlueprintResponseTypeDef = TypedDict(
    "GetBlueprintResponseTypeDef",
    {
        "Blueprint": "BlueprintTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintRunRequestRequestTypeDef = TypedDict(
    "GetBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RunId": str,
    },
)

GetBlueprintRunResponseTypeDef = TypedDict(
    "GetBlueprintRunResponseTypeDef",
    {
        "BlueprintRun": "BlueprintRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBlueprintRunsRequestRequestTypeDef = TypedDict(
    "GetBlueprintRunsRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetBlueprintRunsResponseTypeDef = TypedDict(
    "GetBlueprintRunsResponseTypeDef",
    {
        "BlueprintRuns": List["BlueprintRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCatalogImportStatusRequestRequestTypeDef = TypedDict(
    "GetCatalogImportStatusRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)

GetCatalogImportStatusResponseTypeDef = TypedDict(
    "GetCatalogImportStatusResponseTypeDef",
    {
        "ImportStatus": "CatalogImportStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifierRequestRequestTypeDef = TypedDict(
    "GetClassifierRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetClassifierResponseTypeDef = TypedDict(
    "GetClassifierResponseTypeDef",
    {
        "Classifier": "ClassifierTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetClassifiersRequestRequestTypeDef = TypedDict(
    "GetClassifiersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetClassifiersResponseTypeDef = TypedDict(
    "GetClassifiersResponseTypeDef",
    {
        "Classifiers": List["ClassifierTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnNames": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

GetColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "GetColumnStatisticsForPartitionResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "GetColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnNames": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

GetColumnStatisticsForTableResponseTypeDef = TypedDict(
    "GetColumnStatisticsForTableResponseTypeDef",
    {
        "ColumnStatisticsList": List["ColumnStatisticsTypeDef"],
        "Errors": List["ColumnErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionRequestRequestTypeDef = TypedDict(
    "GetConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
        "HidePassword": NotRequired[bool],
    },
)

GetConnectionResponseTypeDef = TypedDict(
    "GetConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionsFilterTypeDef = TypedDict(
    "GetConnectionsFilterTypeDef",
    {
        "MatchCriteria": NotRequired[Sequence[str]],
        "ConnectionType": NotRequired[ConnectionTypeType],
    },
)

GetConnectionsRequestRequestTypeDef = TypedDict(
    "GetConnectionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Filter": NotRequired["GetConnectionsFilterTypeDef"],
        "HidePassword": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "ConnectionList": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerMetricsRequestRequestTypeDef = TypedDict(
    "GetCrawlerMetricsRequestRequestTypeDef",
    {
        "CrawlerNameList": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetCrawlerMetricsResponseTypeDef = TypedDict(
    "GetCrawlerMetricsResponseTypeDef",
    {
        "CrawlerMetricsList": List["CrawlerMetricsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlerRequestRequestTypeDef = TypedDict(
    "GetCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetCrawlerResponseTypeDef = TypedDict(
    "GetCrawlerResponseTypeDef",
    {
        "Crawler": "CrawlerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCrawlersRequestRequestTypeDef = TypedDict(
    "GetCrawlersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetCrawlersResponseTypeDef = TypedDict(
    "GetCrawlersResponseTypeDef",
    {
        "Crawlers": List["CrawlerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)

GetDataCatalogEncryptionSettingsResponseTypeDef = TypedDict(
    "GetDataCatalogEncryptionSettingsResponseTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseRequestRequestTypeDef = TypedDict(
    "GetDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)

GetDatabaseResponseTypeDef = TypedDict(
    "GetDatabaseResponseTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabasesRequestRequestTypeDef = TypedDict(
    "GetDatabasesRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
    },
)

GetDatabasesResponseTypeDef = TypedDict(
    "GetDatabasesResponseTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDataflowGraphRequestRequestTypeDef = TypedDict(
    "GetDataflowGraphRequestRequestTypeDef",
    {
        "PythonScript": NotRequired[str],
    },
)

GetDataflowGraphResponseTypeDef = TypedDict(
    "GetDataflowGraphResponseTypeDef",
    {
        "DagNodes": List["CodeGenNodeTypeDef"],
        "DagEdges": List["CodeGenEdgeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointRequestRequestTypeDef = TypedDict(
    "GetDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
    },
)

GetDevEndpointResponseTypeDef = TypedDict(
    "GetDevEndpointResponseTypeDef",
    {
        "DevEndpoint": "DevEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevEndpointsRequestRequestTypeDef = TypedDict(
    "GetDevEndpointsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetDevEndpointsResponseTypeDef = TypedDict(
    "GetDevEndpointsResponseTypeDef",
    {
        "DevEndpoints": List["DevEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobBookmarkRequestRequestTypeDef = TypedDict(
    "GetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": NotRequired[str],
    },
)

GetJobBookmarkResponseTypeDef = TypedDict(
    "GetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRequestRequestTypeDef = TypedDict(
    "GetJobRequestRequestTypeDef",
    {
        "JobName": str,
    },
)

GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRunRequestRequestTypeDef = TypedDict(
    "GetJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": str,
        "PredecessorsIncluded": NotRequired[bool],
    },
)

GetJobRunResponseTypeDef = TypedDict(
    "GetJobRunResponseTypeDef",
    {
        "JobRun": "JobRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobRunsRequestRequestTypeDef = TypedDict(
    "GetJobRunsRequestRequestTypeDef",
    {
        "JobName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetJobRunsResponseTypeDef = TypedDict(
    "GetJobRunsResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetJobsRequestRequestTypeDef = TypedDict(
    "GetJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetJobsResponseTypeDef = TypedDict(
    "GetJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTaskRunRequestRequestTypeDef = TypedDict(
    "GetMLTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
    },
)

GetMLTaskRunResponseTypeDef = TypedDict(
    "GetMLTaskRunResponseTypeDef",
    {
        "TransformId": str,
        "TaskRunId": str,
        "Status": TaskStatusTypeType,
        "LogGroupName": str,
        "Properties": "TaskRunPropertiesTypeDef",
        "ErrorString": str,
        "StartedOn": datetime,
        "LastModifiedOn": datetime,
        "CompletedOn": datetime,
        "ExecutionTime": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTaskRunsRequestRequestTypeDef = TypedDict(
    "GetMLTaskRunsRequestRequestTypeDef",
    {
        "TransformId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired["TaskRunFilterCriteriaTypeDef"],
        "Sort": NotRequired["TaskRunSortCriteriaTypeDef"],
    },
)

GetMLTaskRunsResponseTypeDef = TypedDict(
    "GetMLTaskRunsResponseTypeDef",
    {
        "TaskRuns": List["TaskRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformRequestRequestTypeDef = TypedDict(
    "GetMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

GetMLTransformResponseTypeDef = TypedDict(
    "GetMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "Name": str,
        "Description": str,
        "Status": TransformStatusTypeType,
        "CreatedOn": datetime,
        "LastModifiedOn": datetime,
        "InputRecordTables": List["GlueTableTypeDef"],
        "Parameters": "TransformParametersTypeDef",
        "EvaluationMetrics": "EvaluationMetricsTypeDef",
        "LabelCount": int,
        "Schema": List["SchemaColumnTypeDef"],
        "Role": str,
        "GlueVersion": str,
        "MaxCapacity": float,
        "WorkerType": WorkerTypeType,
        "NumberOfWorkers": int,
        "Timeout": int,
        "MaxRetries": int,
        "TransformEncryption": "TransformEncryptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMLTransformsRequestRequestTypeDef = TypedDict(
    "GetMLTransformsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired["TransformFilterCriteriaTypeDef"],
        "Sort": NotRequired["TransformSortCriteriaTypeDef"],
    },
)

GetMLTransformsResponseTypeDef = TypedDict(
    "GetMLTransformsResponseTypeDef",
    {
        "Transforms": List["MLTransformTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMappingRequestRequestTypeDef = TypedDict(
    "GetMappingRequestRequestTypeDef",
    {
        "Source": "CatalogEntryTypeDef",
        "Sinks": NotRequired[Sequence["CatalogEntryTypeDef"]],
        "Location": NotRequired["LocationTypeDef"],
    },
)

GetMappingResponseTypeDef = TypedDict(
    "GetMappingResponseTypeDef",
    {
        "Mapping": List["MappingEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartitionIndexesRequestRequestTypeDef = TypedDict(
    "GetPartitionIndexesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)

GetPartitionIndexesResponseTypeDef = TypedDict(
    "GetPartitionIndexesResponseTypeDef",
    {
        "PartitionIndexDescriptorList": List["PartitionIndexDescriptorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartitionRequestRequestTypeDef = TypedDict(
    "GetPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

GetPartitionResponseTypeDef = TypedDict(
    "GetPartitionResponseTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartitionsRequestRequestTypeDef = TypedDict(
    "GetPartitionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "Segment": NotRequired["SegmentTypeDef"],
        "MaxResults": NotRequired[int],
        "ExcludeColumnSchema": NotRequired[bool],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[Union[datetime, str]],
    },
)

GetPartitionsResponseTypeDef = TypedDict(
    "GetPartitionsResponseTypeDef",
    {
        "Partitions": List["PartitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlanRequestRequestTypeDef = TypedDict(
    "GetPlanRequestRequestTypeDef",
    {
        "Mapping": Sequence["MappingEntryTypeDef"],
        "Source": "CatalogEntryTypeDef",
        "Sinks": NotRequired[Sequence["CatalogEntryTypeDef"]],
        "Location": NotRequired["LocationTypeDef"],
        "Language": NotRequired[LanguageType],
        "AdditionalPlanOptionsMap": NotRequired[Mapping[str, str]],
    },
)

GetPlanResponseTypeDef = TypedDict(
    "GetPlanResponseTypeDef",
    {
        "PythonScript": str,
        "ScalaCode": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryInputRequestTypeDef = TypedDict(
    "GetRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
    },
)

GetRegistryResponseTypeDef = TypedDict(
    "GetRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "Description": str,
        "Status": RegistryStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePoliciesRequestRequestTypeDef = TypedDict(
    "GetResourcePoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetResourcePoliciesResponseTypeDef = TypedDict(
    "GetResourcePoliciesResponseTypeDef",
    {
        "GetResourcePoliciesResponseList": List["GluePolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": NotRequired[str],
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyInJson": str,
        "PolicyHash": str,
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaByDefinitionInputRequestTypeDef = TypedDict(
    "GetSchemaByDefinitionInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

GetSchemaByDefinitionResponseTypeDef = TypedDict(
    "GetSchemaByDefinitionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaArn": str,
        "DataFormat": DataFormatType,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaInputRequestTypeDef = TypedDict(
    "GetSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
    },
)

GetSchemaResponseTypeDef = TypedDict(
    "GetSchemaResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "SchemaName": str,
        "SchemaArn": str,
        "Description": str,
        "DataFormat": DataFormatType,
        "Compatibility": CompatibilityType,
        "SchemaCheckpoint": int,
        "LatestSchemaVersion": int,
        "NextSchemaVersion": int,
        "SchemaStatus": SchemaStatusType,
        "CreatedTime": str,
        "UpdatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionInputRequestTypeDef = TypedDict(
    "GetSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": NotRequired["SchemaIdTypeDef"],
        "SchemaVersionId": NotRequired[str],
        "SchemaVersionNumber": NotRequired["SchemaVersionNumberTypeDef"],
    },
)

GetSchemaVersionResponseTypeDef = TypedDict(
    "GetSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "SchemaDefinition": str,
        "DataFormat": DataFormatType,
        "SchemaArn": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "CreatedTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSchemaVersionsDiffInputRequestTypeDef = TypedDict(
    "GetSchemaVersionsDiffInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "FirstSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SecondSchemaVersionNumber": "SchemaVersionNumberTypeDef",
        "SchemaDiffType": Literal["SYNTAX_DIFF"],
    },
)

GetSchemaVersionsDiffResponseTypeDef = TypedDict(
    "GetSchemaVersionsDiffResponseTypeDef",
    {
        "Diff": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetSecurityConfigurationResponseTypeDef = TypedDict(
    "GetSecurityConfigurationResponseTypeDef",
    {
        "SecurityConfiguration": "SecurityConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSecurityConfigurationsRequestRequestTypeDef = TypedDict(
    "GetSecurityConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetSecurityConfigurationsResponseTypeDef = TypedDict(
    "GetSecurityConfigurationsResponseTypeDef",
    {
        "SecurityConfigurations": List["SecurityConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[Union[datetime, str]],
    },
)

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableVersionRequestRequestTypeDef = TypedDict(
    "GetTableVersionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

GetTableVersionResponseTypeDef = TypedDict(
    "GetTableVersionResponseTypeDef",
    {
        "TableVersion": "TableVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableVersionsRequestRequestTypeDef = TypedDict(
    "GetTableVersionsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetTableVersionsResponseTypeDef = TypedDict(
    "GetTableVersionsResponseTypeDef",
    {
        "TableVersions": List["TableVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTablesRequestRequestTypeDef = TypedDict(
    "GetTablesRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[Union[datetime, str]],
    },
)

GetTablesResponseTypeDef = TypedDict(
    "GetTablesResponseTypeDef",
    {
        "TableList": List["TableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetTagsResponseTypeDef = TypedDict(
    "GetTagsResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggerRequestRequestTypeDef = TypedDict(
    "GetTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetTriggerResponseTypeDef = TypedDict(
    "GetTriggerResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTriggersRequestRequestTypeDef = TypedDict(
    "GetTriggersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "DependentJobName": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetTriggersResponseTypeDef = TypedDict(
    "GetTriggersResponseTypeDef",
    {
        "Triggers": List["TriggerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUnfilteredPartitionMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredPartitionMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "AuditContext": NotRequired["AuditContextTypeDef"],
    },
)

GetUnfilteredPartitionMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionMetadataResponseTypeDef",
    {
        "Partition": "PartitionTypeDef",
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUnfilteredPartitionsMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredPartitionsMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Expression": NotRequired[str],
        "AuditContext": NotRequired["AuditContextTypeDef"],
        "NextToken": NotRequired[str],
        "Segment": NotRequired["SegmentTypeDef"],
        "MaxResults": NotRequired[int],
    },
)

GetUnfilteredPartitionsMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredPartitionsMetadataResponseTypeDef",
    {
        "UnfilteredPartitions": List["UnfilteredPartitionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUnfilteredTableMetadataRequestRequestTypeDef = TypedDict(
    "GetUnfilteredTableMetadataRequestRequestTypeDef",
    {
        "CatalogId": str,
        "DatabaseName": str,
        "Name": str,
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "AuditContext": NotRequired["AuditContextTypeDef"],
    },
)

GetUnfilteredTableMetadataResponseTypeDef = TypedDict(
    "GetUnfilteredTableMetadataResponseTypeDef",
    {
        "Table": "TableTypeDef",
        "AuthorizedColumns": List[str],
        "IsRegisteredWithLakeFormation": bool,
        "CellFilters": List["ColumnRowFilterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "GetUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "CatalogId": NotRequired[str],
    },
)

GetUserDefinedFunctionResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionResponseTypeDef",
    {
        "UserDefinedFunction": "UserDefinedFunctionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserDefinedFunctionsRequestRequestTypeDef = TypedDict(
    "GetUserDefinedFunctionsRequestRequestTypeDef",
    {
        "Pattern": str,
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetUserDefinedFunctionsResponseTypeDef = TypedDict(
    "GetUserDefinedFunctionsResponseTypeDef",
    {
        "UserDefinedFunctions": List["UserDefinedFunctionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRequestRequestTypeDef = TypedDict(
    "GetWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeGraph": NotRequired[bool],
    },
)

GetWorkflowResponseTypeDef = TypedDict(
    "GetWorkflowResponseTypeDef",
    {
        "Workflow": "WorkflowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

GetWorkflowRunPropertiesResponseTypeDef = TypedDict(
    "GetWorkflowRunPropertiesResponseTypeDef",
    {
        "RunProperties": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "IncludeGraph": NotRequired[bool],
    },
)

GetWorkflowRunResponseTypeDef = TypedDict(
    "GetWorkflowRunResponseTypeDef",
    {
        "Run": "WorkflowRunTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkflowRunsRequestRequestTypeDef = TypedDict(
    "GetWorkflowRunsRequestRequestTypeDef",
    {
        "Name": str,
        "IncludeGraph": NotRequired[bool],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetWorkflowRunsResponseTypeDef = TypedDict(
    "GetWorkflowRunsResponseTypeDef",
    {
        "Runs": List["WorkflowRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GluePolicyTypeDef = TypedDict(
    "GluePolicyTypeDef",
    {
        "PolicyInJson": NotRequired[str],
        "PolicyHash": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
    },
)

GlueTableTypeDef = TypedDict(
    "GlueTableTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "ConnectionName": NotRequired[str],
    },
)

GrokClassifierTypeDef = TypedDict(
    "GrokClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "GrokPattern": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "CustomPatterns": NotRequired[str],
    },
)

ImportCatalogToGlueRequestRequestTypeDef = TypedDict(
    "ImportCatalogToGlueRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)

ImportLabelsTaskRunPropertiesTypeDef = TypedDict(
    "ImportLabelsTaskRunPropertiesTypeDef",
    {
        "InputS3Path": NotRequired[str],
        "Replace": NotRequired[bool],
    },
)

JdbcTargetTypeDef = TypedDict(
    "JdbcTargetTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "Path": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
    },
)

JobBookmarkEntryTypeDef = TypedDict(
    "JobBookmarkEntryTypeDef",
    {
        "JobName": NotRequired[str],
        "Version": NotRequired[int],
        "Run": NotRequired[int],
        "Attempt": NotRequired[int],
        "PreviousRunId": NotRequired[str],
        "RunId": NotRequired[str],
        "JobBookmark": NotRequired[str],
    },
)

JobBookmarksEncryptionTypeDef = TypedDict(
    "JobBookmarksEncryptionTypeDef",
    {
        "JobBookmarksEncryptionMode": NotRequired[JobBookmarksEncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)

JobCommandTypeDef = TypedDict(
    "JobCommandTypeDef",
    {
        "Name": NotRequired[str],
        "ScriptLocation": NotRequired[str],
        "PythonVersion": NotRequired[str],
    },
)

JobNodeDetailsTypeDef = TypedDict(
    "JobNodeDetailsTypeDef",
    {
        "JobRuns": NotRequired[List["JobRunTypeDef"]],
    },
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Id": NotRequired[str],
        "Attempt": NotRequired[int],
        "PreviousRunId": NotRequired[str],
        "TriggerName": NotRequired[str],
        "JobName": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "JobRunState": NotRequired[JobRunStateType],
        "Arguments": NotRequired[Dict[str, str]],
        "ErrorMessage": NotRequired[str],
        "PredecessorRuns": NotRequired[List["PredecessorTypeDef"]],
        "AllocatedCapacity": NotRequired[int],
        "ExecutionTime": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "LogGroupName": NotRequired[str],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "GlueVersion": NotRequired[str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "Role": NotRequired[str],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "ExecutionProperty": NotRequired["ExecutionPropertyTypeDef"],
        "Command": NotRequired["JobCommandTypeDef"],
        "DefaultArguments": NotRequired[Dict[str, str]],
        "NonOverridableArguments": NotRequired[Dict[str, str]],
        "Connections": NotRequired["ConnectionsListTypeDef"],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "GlueVersion": NotRequired[str],
    },
)

JobUpdateTypeDef = TypedDict(
    "JobUpdateTypeDef",
    {
        "Description": NotRequired[str],
        "LogUri": NotRequired[str],
        "Role": NotRequired[str],
        "ExecutionProperty": NotRequired["ExecutionPropertyTypeDef"],
        "Command": NotRequired["JobCommandTypeDef"],
        "DefaultArguments": NotRequired[Mapping[str, str]],
        "NonOverridableArguments": NotRequired[Mapping[str, str]],
        "Connections": NotRequired["ConnectionsListTypeDef"],
        "MaxRetries": NotRequired[int],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "GlueVersion": NotRequired[str],
    },
)

JsonClassifierTypeDef = TypedDict(
    "JsonClassifierTypeDef",
    {
        "Name": str,
        "JsonPath": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
    },
)

KeySchemaElementTypeDef = TypedDict(
    "KeySchemaElementTypeDef",
    {
        "Name": str,
        "Type": str,
    },
)

LabelingSetGenerationTaskRunPropertiesTypeDef = TypedDict(
    "LabelingSetGenerationTaskRunPropertiesTypeDef",
    {
        "OutputS3Path": NotRequired[str],
    },
)

LakeFormationConfigurationTypeDef = TypedDict(
    "LakeFormationConfigurationTypeDef",
    {
        "UseLakeFormationCredentials": NotRequired[bool],
        "AccountId": NotRequired[str],
    },
)

LastActiveDefinitionTypeDef = TypedDict(
    "LastActiveDefinitionTypeDef",
    {
        "Description": NotRequired[str],
        "LastModifiedOn": NotRequired[datetime],
        "ParameterSpec": NotRequired[str],
        "BlueprintLocation": NotRequired[str],
        "BlueprintServiceLocation": NotRequired[str],
    },
)

LastCrawlInfoTypeDef = TypedDict(
    "LastCrawlInfoTypeDef",
    {
        "Status": NotRequired[LastCrawlStatusType],
        "ErrorMessage": NotRequired[str],
        "LogGroup": NotRequired[str],
        "LogStream": NotRequired[str],
        "MessagePrefix": NotRequired[str],
        "StartTime": NotRequired[datetime],
    },
)

LineageConfigurationTypeDef = TypedDict(
    "LineageConfigurationTypeDef",
    {
        "CrawlerLineageSettings": NotRequired[CrawlerLineageSettingsType],
    },
)

ListBlueprintsRequestRequestTypeDef = TypedDict(
    "ListBlueprintsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListBlueprintsResponseTypeDef = TypedDict(
    "ListBlueprintsResponseTypeDef",
    {
        "Blueprints": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCrawlersRequestRequestTypeDef = TypedDict(
    "ListCrawlersRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListCrawlersResponseTypeDef = TypedDict(
    "ListCrawlersResponseTypeDef",
    {
        "CrawlerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDevEndpointsRequestRequestTypeDef = TypedDict(
    "ListDevEndpointsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListDevEndpointsResponseTypeDef = TypedDict(
    "ListDevEndpointsResponseTypeDef",
    {
        "DevEndpointNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "JobNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMLTransformsRequestRequestTypeDef = TypedDict(
    "ListMLTransformsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filter": NotRequired["TransformFilterCriteriaTypeDef"],
        "Sort": NotRequired["TransformSortCriteriaTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListMLTransformsResponseTypeDef = TypedDict(
    "ListMLTransformsResponseTypeDef",
    {
        "TransformIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesInputRequestTypeDef = TypedDict(
    "ListRegistriesInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "Registries": List["RegistryListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemaVersionsInputRequestTypeDef = TypedDict(
    "ListSchemaVersionsInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "Schemas": List["SchemaVersionListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasInputRequestTypeDef = TypedDict(
    "ListSchemasInputRequestTypeDef",
    {
        "RegistryId": NotRequired["RegistryIdTypeDef"],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "Schemas": List["SchemaListItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTriggersRequestRequestTypeDef = TypedDict(
    "ListTriggersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "DependentJobName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

ListTriggersResponseTypeDef = TypedDict(
    "ListTriggersResponseTypeDef",
    {
        "TriggerNames": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkflowsRequestRequestTypeDef = TypedDict(
    "ListWorkflowsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkflowsResponseTypeDef = TypedDict(
    "ListWorkflowsResponseTypeDef",
    {
        "Workflows": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Jdbc": NotRequired[Sequence["CodeGenNodeArgTypeDef"]],
        "S3": NotRequired[Sequence["CodeGenNodeArgTypeDef"]],
        "DynamoDB": NotRequired[Sequence["CodeGenNodeArgTypeDef"]],
    },
)

LongColumnStatisticsDataTypeDef = TypedDict(
    "LongColumnStatisticsDataTypeDef",
    {
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
        "MinimumValue": NotRequired[int],
        "MaximumValue": NotRequired[int],
    },
)

MLTransformTypeDef = TypedDict(
    "MLTransformTypeDef",
    {
        "TransformId": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[TransformStatusTypeType],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "InputRecordTables": NotRequired[List["GlueTableTypeDef"]],
        "Parameters": NotRequired["TransformParametersTypeDef"],
        "EvaluationMetrics": NotRequired["EvaluationMetricsTypeDef"],
        "LabelCount": NotRequired[int],
        "Schema": NotRequired[List["SchemaColumnTypeDef"]],
        "Role": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "TransformEncryption": NotRequired["TransformEncryptionTypeDef"],
    },
)

MLUserDataEncryptionTypeDef = TypedDict(
    "MLUserDataEncryptionTypeDef",
    {
        "MlUserDataEncryptionMode": MLUserDataEncryptionModeStringType,
        "KmsKeyId": NotRequired[str],
    },
)

MappingEntryTypeDef = TypedDict(
    "MappingEntryTypeDef",
    {
        "SourceTable": NotRequired[str],
        "SourcePath": NotRequired[str],
        "SourceType": NotRequired[str],
        "TargetTable": NotRequired[str],
        "TargetPath": NotRequired[str],
        "TargetType": NotRequired[str],
    },
)

MetadataInfoTypeDef = TypedDict(
    "MetadataInfoTypeDef",
    {
        "MetadataValue": NotRequired[str],
        "CreatedTime": NotRequired[str],
        "OtherMetadataValueList": NotRequired[List["OtherMetadataValueListItemTypeDef"]],
    },
)

MetadataKeyValuePairTypeDef = TypedDict(
    "MetadataKeyValuePairTypeDef",
    {
        "MetadataKey": NotRequired[str],
        "MetadataValue": NotRequired[str],
    },
)

MongoDBTargetTypeDef = TypedDict(
    "MongoDBTargetTypeDef",
    {
        "ConnectionName": NotRequired[str],
        "Path": NotRequired[str],
        "ScanAll": NotRequired[bool],
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "Type": NotRequired[NodeTypeType],
        "Name": NotRequired[str],
        "UniqueId": NotRequired[str],
        "TriggerDetails": NotRequired["TriggerNodeDetailsTypeDef"],
        "JobDetails": NotRequired["JobNodeDetailsTypeDef"],
        "CrawlerDetails": NotRequired["CrawlerNodeDetailsTypeDef"],
    },
)

NotificationPropertyTypeDef = TypedDict(
    "NotificationPropertyTypeDef",
    {
        "NotifyDelayAfter": NotRequired[int],
    },
)

OrderTypeDef = TypedDict(
    "OrderTypeDef",
    {
        "Column": str,
        "SortOrder": int,
    },
)

OtherMetadataValueListItemTypeDef = TypedDict(
    "OtherMetadataValueListItemTypeDef",
    {
        "MetadataValue": NotRequired[str],
        "CreatedTime": NotRequired[str],
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

PartitionErrorTypeDef = TypedDict(
    "PartitionErrorTypeDef",
    {
        "PartitionValues": NotRequired[List[str]],
        "ErrorDetail": NotRequired["ErrorDetailTypeDef"],
    },
)

PartitionIndexDescriptorTypeDef = TypedDict(
    "PartitionIndexDescriptorTypeDef",
    {
        "IndexName": str,
        "Keys": List["KeySchemaElementTypeDef"],
        "IndexStatus": PartitionIndexStatusType,
        "BackfillErrors": NotRequired[List["BackfillErrorTypeDef"]],
    },
)

PartitionIndexTypeDef = TypedDict(
    "PartitionIndexTypeDef",
    {
        "Keys": Sequence[str],
        "IndexName": str,
    },
)

PartitionInputTypeDef = TypedDict(
    "PartitionInputTypeDef",
    {
        "Values": NotRequired[Sequence[str]],
        "LastAccessTime": NotRequired[Union[datetime, str]],
        "StorageDescriptor": NotRequired["StorageDescriptorTypeDef"],
        "Parameters": NotRequired[Mapping[str, str]],
        "LastAnalyzedTime": NotRequired[Union[datetime, str]],
    },
)

PartitionTypeDef = TypedDict(
    "PartitionTypeDef",
    {
        "Values": NotRequired[List[str]],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "StorageDescriptor": NotRequired["StorageDescriptorTypeDef"],
        "Parameters": NotRequired[Dict[str, str]],
        "LastAnalyzedTime": NotRequired[datetime],
        "CatalogId": NotRequired[str],
    },
)

PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": Sequence[str],
    },
)

PhysicalConnectionRequirementsTypeDef = TypedDict(
    "PhysicalConnectionRequirementsTypeDef",
    {
        "SubnetId": NotRequired[str],
        "SecurityGroupIdList": NotRequired[Sequence[str]],
        "AvailabilityZone": NotRequired[str],
    },
)

PredecessorTypeDef = TypedDict(
    "PredecessorTypeDef",
    {
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
    },
)

PredicateTypeDef = TypedDict(
    "PredicateTypeDef",
    {
        "Logical": NotRequired[LogicalType],
        "Conditions": NotRequired[List["ConditionTypeDef"]],
    },
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": NotRequired["DataLakePrincipalTypeDef"],
        "Permissions": NotRequired[Sequence[PermissionType]],
    },
)

PropertyPredicateTypeDef = TypedDict(
    "PropertyPredicateTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
        "Comparator": NotRequired[ComparatorType],
    },
)

PutDataCatalogEncryptionSettingsRequestRequestTypeDef = TypedDict(
    "PutDataCatalogEncryptionSettingsRequestRequestTypeDef",
    {
        "DataCatalogEncryptionSettings": "DataCatalogEncryptionSettingsTypeDef",
        "CatalogId": NotRequired[str],
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyInJson": str,
        "ResourceArn": NotRequired[str],
        "PolicyHashCondition": NotRequired[str],
        "PolicyExistsCondition": NotRequired[ExistConditionType],
        "EnableHybrid": NotRequired[EnableHybridValuesType],
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "PolicyHash": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "PutSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
        "SchemaId": NotRequired["SchemaIdTypeDef"],
        "SchemaVersionNumber": NotRequired["SchemaVersionNumberTypeDef"],
        "SchemaVersionId": NotRequired[str],
    },
)

PutSchemaVersionMetadataResponseTypeDef = TypedDict(
    "PutSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutWorkflowRunPropertiesRequestRequestTypeDef = TypedDict(
    "PutWorkflowRunPropertiesRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "RunProperties": Mapping[str, str],
    },
)

QuerySchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "QuerySchemaVersionMetadataInputRequestTypeDef",
    {
        "SchemaId": NotRequired["SchemaIdTypeDef"],
        "SchemaVersionNumber": NotRequired["SchemaVersionNumberTypeDef"],
        "SchemaVersionId": NotRequired[str],
        "MetadataList": NotRequired[Sequence["MetadataKeyValuePairTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

QuerySchemaVersionMetadataResponseTypeDef = TypedDict(
    "QuerySchemaVersionMetadataResponseTypeDef",
    {
        "MetadataInfoMap": Dict[str, "MetadataInfoTypeDef"],
        "SchemaVersionId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecrawlPolicyTypeDef = TypedDict(
    "RecrawlPolicyTypeDef",
    {
        "RecrawlBehavior": NotRequired[RecrawlBehaviorType],
    },
)

RegisterSchemaVersionInputRequestTypeDef = TypedDict(
    "RegisterSchemaVersionInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaDefinition": str,
    },
)

RegisterSchemaVersionResponseTypeDef = TypedDict(
    "RegisterSchemaVersionResponseTypeDef",
    {
        "SchemaVersionId": str,
        "VersionNumber": int,
        "Status": SchemaVersionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistryIdTypeDef = TypedDict(
    "RegistryIdTypeDef",
    {
        "RegistryName": NotRequired[str],
        "RegistryArn": NotRequired[str],
    },
)

RegistryListItemTypeDef = TypedDict(
    "RegistryListItemTypeDef",
    {
        "RegistryName": NotRequired[str],
        "RegistryArn": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[RegistryStatusType],
        "CreatedTime": NotRequired[str],
        "UpdatedTime": NotRequired[str],
    },
)

RemoveSchemaVersionMetadataInputRequestTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataInputRequestTypeDef",
    {
        "MetadataKeyValue": "MetadataKeyValuePairTypeDef",
        "SchemaId": NotRequired["SchemaIdTypeDef"],
        "SchemaVersionNumber": NotRequired["SchemaVersionNumberTypeDef"],
        "SchemaVersionId": NotRequired[str],
    },
)

RemoveSchemaVersionMetadataResponseTypeDef = TypedDict(
    "RemoveSchemaVersionMetadataResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "LatestVersion": bool,
        "VersionNumber": int,
        "SchemaVersionId": str,
        "MetadataKey": str,
        "MetadataValue": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetJobBookmarkRequestRequestTypeDef = TypedDict(
    "ResetJobBookmarkRequestRequestTypeDef",
    {
        "JobName": str,
        "RunId": NotRequired[str],
    },
)

ResetJobBookmarkResponseTypeDef = TypedDict(
    "ResetJobBookmarkResponseTypeDef",
    {
        "JobBookmarkEntry": "JobBookmarkEntryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceUriTypeDef = TypedDict(
    "ResourceUriTypeDef",
    {
        "ResourceType": NotRequired[ResourceTypeType],
        "Uri": NotRequired[str],
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

ResumeWorkflowRunRequestRequestTypeDef = TypedDict(
    "ResumeWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
        "NodeIds": Sequence[str],
    },
)

ResumeWorkflowRunResponseTypeDef = TypedDict(
    "ResumeWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "NodeIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3EncryptionTypeDef = TypedDict(
    "S3EncryptionTypeDef",
    {
        "S3EncryptionMode": NotRequired[S3EncryptionModeType],
        "KmsKeyArn": NotRequired[str],
    },
)

S3TargetTypeDef = TypedDict(
    "S3TargetTypeDef",
    {
        "Path": NotRequired[str],
        "Exclusions": NotRequired[List[str]],
        "ConnectionName": NotRequired[str],
        "SampleSize": NotRequired[int],
        "EventQueueArn": NotRequired[str],
        "DlqEventQueueArn": NotRequired[str],
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "ScheduleExpression": NotRequired[str],
        "State": NotRequired[ScheduleStateType],
    },
)

SchemaChangePolicyTypeDef = TypedDict(
    "SchemaChangePolicyTypeDef",
    {
        "UpdateBehavior": NotRequired[UpdateBehaviorType],
        "DeleteBehavior": NotRequired[DeleteBehaviorType],
    },
)

SchemaColumnTypeDef = TypedDict(
    "SchemaColumnTypeDef",
    {
        "Name": NotRequired[str],
        "DataType": NotRequired[str],
    },
)

SchemaIdTypeDef = TypedDict(
    "SchemaIdTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "RegistryName": NotRequired[str],
    },
)

SchemaListItemTypeDef = TypedDict(
    "SchemaListItemTypeDef",
    {
        "RegistryName": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaArn": NotRequired[str],
        "Description": NotRequired[str],
        "SchemaStatus": NotRequired[SchemaStatusType],
        "CreatedTime": NotRequired[str],
        "UpdatedTime": NotRequired[str],
    },
)

SchemaReferenceTypeDef = TypedDict(
    "SchemaReferenceTypeDef",
    {
        "SchemaId": NotRequired["SchemaIdTypeDef"],
        "SchemaVersionId": NotRequired[str],
        "SchemaVersionNumber": NotRequired[int],
    },
)

SchemaVersionErrorItemTypeDef = TypedDict(
    "SchemaVersionErrorItemTypeDef",
    {
        "VersionNumber": NotRequired[int],
        "ErrorDetails": NotRequired["ErrorDetailsTypeDef"],
    },
)

SchemaVersionListItemTypeDef = TypedDict(
    "SchemaVersionListItemTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaVersionId": NotRequired[str],
        "VersionNumber": NotRequired[int],
        "Status": NotRequired[SchemaVersionStatusType],
        "CreatedTime": NotRequired[str],
    },
)

SchemaVersionNumberTypeDef = TypedDict(
    "SchemaVersionNumberTypeDef",
    {
        "LatestVersion": NotRequired[bool],
        "VersionNumber": NotRequired[int],
    },
)

SearchTablesRequestRequestTypeDef = TypedDict(
    "SearchTablesRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "Filters": NotRequired[Sequence["PropertyPredicateTypeDef"]],
        "SearchText": NotRequired[str],
        "SortCriteria": NotRequired[Sequence["SortCriterionTypeDef"]],
        "MaxResults": NotRequired[int],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
    },
)

SearchTablesResponseTypeDef = TypedDict(
    "SearchTablesResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityConfigurationTypeDef = TypedDict(
    "SecurityConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "CreatedTimeStamp": NotRequired[datetime],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
    },
)

SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "SegmentNumber": int,
        "TotalSegments": int,
    },
)

SerDeInfoTypeDef = TypedDict(
    "SerDeInfoTypeDef",
    {
        "Name": NotRequired[str],
        "SerializationLibrary": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

SkewedInfoTypeDef = TypedDict(
    "SkewedInfoTypeDef",
    {
        "SkewedColumnNames": NotRequired[Sequence[str]],
        "SkewedColumnValues": NotRequired[Sequence[str]],
        "SkewedColumnValueLocationMaps": NotRequired[Mapping[str, str]],
    },
)

SortCriterionTypeDef = TypedDict(
    "SortCriterionTypeDef",
    {
        "FieldName": NotRequired[str],
        "Sort": NotRequired[SortType],
    },
)

StartBlueprintRunRequestRequestTypeDef = TypedDict(
    "StartBlueprintRunRequestRequestTypeDef",
    {
        "BlueprintName": str,
        "RoleArn": str,
        "Parameters": NotRequired[str],
    },
)

StartBlueprintRunResponseTypeDef = TypedDict(
    "StartBlueprintRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartCrawlerRequestRequestTypeDef = TypedDict(
    "StartCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StartCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

StartExportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "StartExportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartExportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartExportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartImportLabelsTaskRunRequestRequestTypeDef = TypedDict(
    "StartImportLabelsTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "InputS3Path": str,
        "ReplaceAllLabels": NotRequired[bool],
    },
)

StartImportLabelsTaskRunResponseTypeDef = TypedDict(
    "StartImportLabelsTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "JobName": str,
        "JobRunId": NotRequired[str],
        "Arguments": NotRequired[Mapping[str, str]],
        "AllocatedCapacity": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxCapacity": NotRequired[float],
        "SecurityConfiguration": NotRequired[str],
        "NotificationProperty": NotRequired["NotificationPropertyTypeDef"],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "JobRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLEvaluationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLEvaluationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
    },
)

StartMLEvaluationTaskRunResponseTypeDef = TypedDict(
    "StartMLEvaluationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef",
    {
        "TransformId": str,
        "OutputS3Path": str,
    },
)

StartMLLabelingSetGenerationTaskRunResponseTypeDef = TypedDict(
    "StartMLLabelingSetGenerationTaskRunResponseTypeDef",
    {
        "TaskRunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTriggerRequestRequestTypeDef = TypedDict(
    "StartTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartTriggerResponseTypeDef = TypedDict(
    "StartTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartWorkflowRunRequestRequestTypeDef = TypedDict(
    "StartWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunProperties": NotRequired[Mapping[str, str]],
    },
)

StartWorkflowRunResponseTypeDef = TypedDict(
    "StartWorkflowRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartingEventBatchConditionTypeDef = TypedDict(
    "StartingEventBatchConditionTypeDef",
    {
        "BatchSize": NotRequired[int],
        "BatchWindow": NotRequired[int],
    },
)

StopCrawlerRequestRequestTypeDef = TypedDict(
    "StopCrawlerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "StopCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
    },
)

StopTriggerRequestRequestTypeDef = TypedDict(
    "StopTriggerRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StopTriggerResponseTypeDef = TypedDict(
    "StopTriggerResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopWorkflowRunRequestRequestTypeDef = TypedDict(
    "StopWorkflowRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StorageDescriptorTypeDef = TypedDict(
    "StorageDescriptorTypeDef",
    {
        "Columns": NotRequired[Sequence["ColumnTypeDef"]],
        "Location": NotRequired[str],
        "AdditionalLocations": NotRequired[Sequence[str]],
        "InputFormat": NotRequired[str],
        "OutputFormat": NotRequired[str],
        "Compressed": NotRequired[bool],
        "NumberOfBuckets": NotRequired[int],
        "SerdeInfo": NotRequired["SerDeInfoTypeDef"],
        "BucketColumns": NotRequired[Sequence[str]],
        "SortColumns": NotRequired[Sequence["OrderTypeDef"]],
        "Parameters": NotRequired[Mapping[str, str]],
        "SkewedInfo": NotRequired["SkewedInfoTypeDef"],
        "StoredAsSubDirectories": NotRequired[bool],
        "SchemaReference": NotRequired["SchemaReferenceTypeDef"],
    },
)

StringColumnStatisticsDataTypeDef = TypedDict(
    "StringColumnStatisticsDataTypeDef",
    {
        "MaximumLength": int,
        "AverageLength": float,
        "NumberOfNulls": int,
        "NumberOfDistinctValues": int,
    },
)

TableErrorTypeDef = TypedDict(
    "TableErrorTypeDef",
    {
        "TableName": NotRequired[str],
        "ErrorDetail": NotRequired["ErrorDetailTypeDef"],
    },
)

TableIdentifierTypeDef = TypedDict(
    "TableIdentifierTypeDef",
    {
        "CatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "Name": NotRequired[str],
    },
)

TableInputTypeDef = TypedDict(
    "TableInputTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "LastAccessTime": NotRequired[Union[datetime, str]],
        "LastAnalyzedTime": NotRequired[Union[datetime, str]],
        "Retention": NotRequired[int],
        "StorageDescriptor": NotRequired["StorageDescriptorTypeDef"],
        "PartitionKeys": NotRequired[Sequence["ColumnTypeDef"]],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "TableType": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "TargetTable": NotRequired["TableIdentifierTypeDef"],
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Name": str,
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Owner": NotRequired[str],
        "CreateTime": NotRequired[datetime],
        "UpdateTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "LastAnalyzedTime": NotRequired[datetime],
        "Retention": NotRequired[int],
        "StorageDescriptor": NotRequired["StorageDescriptorTypeDef"],
        "PartitionKeys": NotRequired[List["ColumnTypeDef"]],
        "ViewOriginalText": NotRequired[str],
        "ViewExpandedText": NotRequired[str],
        "TableType": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
        "CreatedBy": NotRequired[str],
        "IsRegisteredWithLakeFormation": NotRequired[bool],
        "TargetTable": NotRequired["TableIdentifierTypeDef"],
        "CatalogId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

TableVersionErrorTypeDef = TypedDict(
    "TableVersionErrorTypeDef",
    {
        "TableName": NotRequired[str],
        "VersionId": NotRequired[str],
        "ErrorDetail": NotRequired["ErrorDetailTypeDef"],
    },
)

TableVersionTypeDef = TypedDict(
    "TableVersionTypeDef",
    {
        "Table": NotRequired["TableTypeDef"],
        "VersionId": NotRequired[str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToAdd": Mapping[str, str],
    },
)

TaskRunFilterCriteriaTypeDef = TypedDict(
    "TaskRunFilterCriteriaTypeDef",
    {
        "TaskRunType": NotRequired[TaskTypeType],
        "Status": NotRequired[TaskStatusTypeType],
        "StartedBefore": NotRequired[Union[datetime, str]],
        "StartedAfter": NotRequired[Union[datetime, str]],
    },
)

TaskRunPropertiesTypeDef = TypedDict(
    "TaskRunPropertiesTypeDef",
    {
        "TaskType": NotRequired[TaskTypeType],
        "ImportLabelsTaskRunProperties": NotRequired["ImportLabelsTaskRunPropertiesTypeDef"],
        "ExportLabelsTaskRunProperties": NotRequired["ExportLabelsTaskRunPropertiesTypeDef"],
        "LabelingSetGenerationTaskRunProperties": NotRequired[
            "LabelingSetGenerationTaskRunPropertiesTypeDef"
        ],
        "FindMatchesTaskRunProperties": NotRequired["FindMatchesTaskRunPropertiesTypeDef"],
    },
)

TaskRunSortCriteriaTypeDef = TypedDict(
    "TaskRunSortCriteriaTypeDef",
    {
        "Column": TaskRunSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TaskRunTypeDef = TypedDict(
    "TaskRunTypeDef",
    {
        "TransformId": NotRequired[str],
        "TaskRunId": NotRequired[str],
        "Status": NotRequired[TaskStatusTypeType],
        "LogGroupName": NotRequired[str],
        "Properties": NotRequired["TaskRunPropertiesTypeDef"],
        "ErrorString": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "ExecutionTime": NotRequired[int],
    },
)

TransformEncryptionTypeDef = TypedDict(
    "TransformEncryptionTypeDef",
    {
        "MlUserDataEncryption": NotRequired["MLUserDataEncryptionTypeDef"],
        "TaskRunSecurityConfigurationName": NotRequired[str],
    },
)

TransformFilterCriteriaTypeDef = TypedDict(
    "TransformFilterCriteriaTypeDef",
    {
        "Name": NotRequired[str],
        "TransformType": NotRequired[Literal["FIND_MATCHES"]],
        "Status": NotRequired[TransformStatusTypeType],
        "GlueVersion": NotRequired[str],
        "CreatedBefore": NotRequired[Union[datetime, str]],
        "CreatedAfter": NotRequired[Union[datetime, str]],
        "LastModifiedBefore": NotRequired[Union[datetime, str]],
        "LastModifiedAfter": NotRequired[Union[datetime, str]],
        "Schema": NotRequired[Sequence["SchemaColumnTypeDef"]],
    },
)

TransformParametersTypeDef = TypedDict(
    "TransformParametersTypeDef",
    {
        "TransformType": Literal["FIND_MATCHES"],
        "FindMatchesParameters": NotRequired["FindMatchesParametersTypeDef"],
    },
)

TransformSortCriteriaTypeDef = TypedDict(
    "TransformSortCriteriaTypeDef",
    {
        "Column": TransformSortColumnTypeType,
        "SortDirection": SortDirectionTypeType,
    },
)

TriggerNodeDetailsTypeDef = TypedDict(
    "TriggerNodeDetailsTypeDef",
    {
        "Trigger": NotRequired["TriggerTypeDef"],
    },
)

TriggerTypeDef = TypedDict(
    "TriggerTypeDef",
    {
        "Name": NotRequired[str],
        "WorkflowName": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[TriggerTypeType],
        "State": NotRequired[TriggerStateType],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Actions": NotRequired[List["ActionTypeDef"]],
        "Predicate": NotRequired["PredicateTypeDef"],
        "EventBatchingCondition": NotRequired["EventBatchingConditionTypeDef"],
    },
)

TriggerUpdateTypeDef = TypedDict(
    "TriggerUpdateTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Schedule": NotRequired[str],
        "Actions": NotRequired[Sequence["ActionTypeDef"]],
        "Predicate": NotRequired["PredicateTypeDef"],
        "EventBatchingCondition": NotRequired["EventBatchingConditionTypeDef"],
    },
)

UnfilteredPartitionTypeDef = TypedDict(
    "UnfilteredPartitionTypeDef",
    {
        "Partition": NotRequired["PartitionTypeDef"],
        "AuthorizedColumns": NotRequired[List[str]],
        "IsRegisteredWithLakeFormation": NotRequired[bool],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagsToRemove": Sequence[str],
    },
)

UpdateBlueprintRequestRequestTypeDef = TypedDict(
    "UpdateBlueprintRequestRequestTypeDef",
    {
        "Name": str,
        "BlueprintLocation": str,
        "Description": NotRequired[str],
    },
)

UpdateBlueprintResponseTypeDef = TypedDict(
    "UpdateBlueprintResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateClassifierRequestRequestTypeDef = TypedDict(
    "UpdateClassifierRequestRequestTypeDef",
    {
        "GrokClassifier": NotRequired["UpdateGrokClassifierRequestTypeDef"],
        "XMLClassifier": NotRequired["UpdateXMLClassifierRequestTypeDef"],
        "JsonClassifier": NotRequired["UpdateJsonClassifierRequestTypeDef"],
        "CsvClassifier": NotRequired["UpdateCsvClassifierRequestTypeDef"],
    },
)

UpdateColumnStatisticsForPartitionRequestRequestTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValues": Sequence[str],
        "ColumnStatisticsList": Sequence["ColumnStatisticsTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

UpdateColumnStatisticsForPartitionResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForPartitionResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateColumnStatisticsForTableRequestRequestTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "ColumnStatisticsList": Sequence["ColumnStatisticsTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

UpdateColumnStatisticsForTableResponseTypeDef = TypedDict(
    "UpdateColumnStatisticsForTableResponseTypeDef",
    {
        "Errors": List["ColumnStatisticsErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "Name": str,
        "ConnectionInput": "ConnectionInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

UpdateCrawlerRequestRequestTypeDef = TypedDict(
    "UpdateCrawlerRequestRequestTypeDef",
    {
        "Name": str,
        "Role": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "Description": NotRequired[str],
        "Targets": NotRequired["CrawlerTargetsTypeDef"],
        "Schedule": NotRequired[str],
        "Classifiers": NotRequired[Sequence[str]],
        "TablePrefix": NotRequired[str],
        "SchemaChangePolicy": NotRequired["SchemaChangePolicyTypeDef"],
        "RecrawlPolicy": NotRequired["RecrawlPolicyTypeDef"],
        "LineageConfiguration": NotRequired["LineageConfigurationTypeDef"],
        "LakeFormationConfiguration": NotRequired["LakeFormationConfigurationTypeDef"],
        "Configuration": NotRequired[str],
        "CrawlerSecurityConfiguration": NotRequired[str],
    },
)

UpdateCrawlerScheduleRequestRequestTypeDef = TypedDict(
    "UpdateCrawlerScheduleRequestRequestTypeDef",
    {
        "CrawlerName": str,
        "Schedule": NotRequired[str],
    },
)

UpdateCsvClassifierRequestTypeDef = TypedDict(
    "UpdateCsvClassifierRequestTypeDef",
    {
        "Name": str,
        "Delimiter": NotRequired[str],
        "QuoteSymbol": NotRequired[str],
        "ContainsHeader": NotRequired[CsvHeaderOptionType],
        "Header": NotRequired[Sequence[str]],
        "DisableValueTrimming": NotRequired[bool],
        "AllowSingleColumn": NotRequired[bool],
    },
)

UpdateDatabaseRequestRequestTypeDef = TypedDict(
    "UpdateDatabaseRequestRequestTypeDef",
    {
        "Name": str,
        "DatabaseInput": "DatabaseInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

UpdateDevEndpointRequestRequestTypeDef = TypedDict(
    "UpdateDevEndpointRequestRequestTypeDef",
    {
        "EndpointName": str,
        "PublicKey": NotRequired[str],
        "AddPublicKeys": NotRequired[Sequence[str]],
        "DeletePublicKeys": NotRequired[Sequence[str]],
        "CustomLibraries": NotRequired["DevEndpointCustomLibrariesTypeDef"],
        "UpdateEtlLibraries": NotRequired[bool],
        "DeleteArguments": NotRequired[Sequence[str]],
        "AddArguments": NotRequired[Mapping[str, str]],
    },
)

UpdateGrokClassifierRequestTypeDef = TypedDict(
    "UpdateGrokClassifierRequestTypeDef",
    {
        "Name": str,
        "Classification": NotRequired[str],
        "GrokPattern": NotRequired[str],
        "CustomPatterns": NotRequired[str],
    },
)

UpdateJobRequestRequestTypeDef = TypedDict(
    "UpdateJobRequestRequestTypeDef",
    {
        "JobName": str,
        "JobUpdate": "JobUpdateTypeDef",
    },
)

UpdateJobResponseTypeDef = TypedDict(
    "UpdateJobResponseTypeDef",
    {
        "JobName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateJsonClassifierRequestTypeDef = TypedDict(
    "UpdateJsonClassifierRequestTypeDef",
    {
        "Name": str,
        "JsonPath": NotRequired[str],
    },
)

UpdateMLTransformRequestRequestTypeDef = TypedDict(
    "UpdateMLTransformRequestRequestTypeDef",
    {
        "TransformId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired["TransformParametersTypeDef"],
        "Role": NotRequired[str],
        "GlueVersion": NotRequired[str],
        "MaxCapacity": NotRequired[float],
        "WorkerType": NotRequired[WorkerTypeType],
        "NumberOfWorkers": NotRequired[int],
        "Timeout": NotRequired[int],
        "MaxRetries": NotRequired[int],
    },
)

UpdateMLTransformResponseTypeDef = TypedDict(
    "UpdateMLTransformResponseTypeDef",
    {
        "TransformId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePartitionRequestRequestTypeDef = TypedDict(
    "UpdatePartitionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "PartitionValueList": Sequence[str],
        "PartitionInput": "PartitionInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

UpdateRegistryInputRequestTypeDef = TypedDict(
    "UpdateRegistryInputRequestTypeDef",
    {
        "RegistryId": "RegistryIdTypeDef",
        "Description": str,
    },
)

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "RegistryName": str,
        "RegistryArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchemaInputRequestTypeDef = TypedDict(
    "UpdateSchemaInputRequestTypeDef",
    {
        "SchemaId": "SchemaIdTypeDef",
        "SchemaVersionNumber": NotRequired["SchemaVersionNumberTypeDef"],
        "Compatibility": NotRequired[CompatibilityType],
        "Description": NotRequired[str],
    },
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "SchemaArn": str,
        "SchemaName": str,
        "RegistryName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableInput": "TableInputTypeDef",
        "CatalogId": NotRequired[str],
        "SkipArchive": NotRequired[bool],
        "TransactionId": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)

UpdateTriggerRequestRequestTypeDef = TypedDict(
    "UpdateTriggerRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerUpdate": "TriggerUpdateTypeDef",
    },
)

UpdateTriggerResponseTypeDef = TypedDict(
    "UpdateTriggerResponseTypeDef",
    {
        "Trigger": "TriggerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserDefinedFunctionRequestRequestTypeDef = TypedDict(
    "UpdateUserDefinedFunctionRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "FunctionName": str,
        "FunctionInput": "UserDefinedFunctionInputTypeDef",
        "CatalogId": NotRequired[str],
    },
)

UpdateWorkflowRequestRequestTypeDef = TypedDict(
    "UpdateWorkflowRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Mapping[str, str]],
        "MaxConcurrentRuns": NotRequired[int],
    },
)

UpdateWorkflowResponseTypeDef = TypedDict(
    "UpdateWorkflowResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateXMLClassifierRequestTypeDef = TypedDict(
    "UpdateXMLClassifierRequestTypeDef",
    {
        "Name": str,
        "Classification": NotRequired[str],
        "RowTag": NotRequired[str],
    },
)

UserDefinedFunctionInputTypeDef = TypedDict(
    "UserDefinedFunctionInputTypeDef",
    {
        "FunctionName": NotRequired[str],
        "ClassName": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerType": NotRequired[PrincipalTypeType],
        "ResourceUris": NotRequired[Sequence["ResourceUriTypeDef"]],
    },
)

UserDefinedFunctionTypeDef = TypedDict(
    "UserDefinedFunctionTypeDef",
    {
        "FunctionName": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "ClassName": NotRequired[str],
        "OwnerName": NotRequired[str],
        "OwnerType": NotRequired[PrincipalTypeType],
        "CreateTime": NotRequired[datetime],
        "ResourceUris": NotRequired[List["ResourceUriTypeDef"]],
        "CatalogId": NotRequired[str],
    },
)

WorkflowGraphTypeDef = TypedDict(
    "WorkflowGraphTypeDef",
    {
        "Nodes": NotRequired[List["NodeTypeDef"]],
        "Edges": NotRequired[List["EdgeTypeDef"]],
    },
)

WorkflowRunStatisticsTypeDef = TypedDict(
    "WorkflowRunStatisticsTypeDef",
    {
        "TotalActions": NotRequired[int],
        "TimeoutActions": NotRequired[int],
        "FailedActions": NotRequired[int],
        "StoppedActions": NotRequired[int],
        "SucceededActions": NotRequired[int],
        "RunningActions": NotRequired[int],
    },
)

WorkflowRunTypeDef = TypedDict(
    "WorkflowRunTypeDef",
    {
        "Name": NotRequired[str],
        "WorkflowRunId": NotRequired[str],
        "PreviousRunId": NotRequired[str],
        "WorkflowRunProperties": NotRequired[Dict[str, str]],
        "StartedOn": NotRequired[datetime],
        "CompletedOn": NotRequired[datetime],
        "Status": NotRequired[WorkflowRunStatusType],
        "ErrorMessage": NotRequired[str],
        "Statistics": NotRequired["WorkflowRunStatisticsTypeDef"],
        "Graph": NotRequired["WorkflowGraphTypeDef"],
        "StartingEventBatchCondition": NotRequired["StartingEventBatchConditionTypeDef"],
    },
)

WorkflowTypeDef = TypedDict(
    "WorkflowTypeDef",
    {
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "DefaultRunProperties": NotRequired[Dict[str, str]],
        "CreatedOn": NotRequired[datetime],
        "LastModifiedOn": NotRequired[datetime],
        "LastRun": NotRequired["WorkflowRunTypeDef"],
        "Graph": NotRequired["WorkflowGraphTypeDef"],
        "MaxConcurrentRuns": NotRequired[int],
        "BlueprintDetails": NotRequired["BlueprintDetailsTypeDef"],
    },
)

XMLClassifierTypeDef = TypedDict(
    "XMLClassifierTypeDef",
    {
        "Name": str,
        "Classification": str,
        "CreationTime": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Version": NotRequired[int],
        "RowTag": NotRequired[str],
    },
)
