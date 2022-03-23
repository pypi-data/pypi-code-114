"""
Type annotations for databrew service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_databrew/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_databrew.type_defs import AllowedStatisticsTypeDef

    data: AllowedStatisticsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AnalyticsModeType,
    CompressionFormatType,
    EncryptionModeType,
    InputFormatType,
    JobRunStateType,
    JobTypeType,
    LogSubscriptionType,
    OrderType,
    OutputFormatType,
    ParameterTypeType,
    SampleModeType,
    SampleTypeType,
    SessionStatusType,
    SourceType,
    ThresholdTypeType,
    ThresholdUnitType,
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
    "AllowedStatisticsTypeDef",
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    "BatchDeleteRecipeVersionResponseTypeDef",
    "ColumnSelectorTypeDef",
    "ColumnStatisticsConfigurationTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobRequestRequestTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobRequestRequestTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeRequestRequestTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateRulesetRequestRequestTypeDef",
    "CreateRulesetResponseTypeDef",
    "CreateScheduleRequestRequestTypeDef",
    "CreateScheduleResponseTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DataCatalogOutputTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatabaseOutputTypeDef",
    "DatabaseTableOutputOptionsTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobRequestRequestTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionRequestRequestTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteRulesetRequestRequestTypeDef",
    "DeleteRulesetResponseTypeDef",
    "DeleteScheduleRequestRequestTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeJobRequestRequestTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunRequestRequestTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeRecipeRequestRequestTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeRulesetRequestRequestTypeDef",
    "DescribeRulesetResponseTypeDef",
    "DescribeScheduleRequestRequestTypeDef",
    "DescribeScheduleResponseTypeDef",
    "EntityDetectorConfigurationTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListJobRunsRequestRequestTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsRequestRequestTypeDef",
    "ListJobsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListRecipeVersionsRequestRequestTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesRequestRequestTypeDef",
    "ListRecipesResponseTypeDef",
    "ListRulesetsRequestRequestTypeDef",
    "ListRulesetsResponseTypeDef",
    "ListSchedulesRequestRequestTypeDef",
    "ListSchedulesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetadataTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathOptionsTypeDef",
    "ProfileConfigurationTypeDef",
    "ProjectTypeDef",
    "PublishRecipeRequestRequestTypeDef",
    "PublishRecipeResponseTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadataTypeDef",
    "RuleTypeDef",
    "RulesetItemTypeDef",
    "S3LocationTypeDef",
    "S3TableOutputOptionsTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "SendProjectSessionActionRequestRequestTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunRequestRequestTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionRequestRequestTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StatisticOverrideTypeDef",
    "StatisticsConfigurationTypeDef",
    "StopJobRunRequestRequestTypeDef",
    "StopJobRunResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThresholdTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDatasetRequestRequestTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobRequestRequestTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobRequestRequestTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeRequestRequestTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateRulesetRequestRequestTypeDef",
    "UpdateRulesetResponseTypeDef",
    "UpdateScheduleRequestRequestTypeDef",
    "UpdateScheduleResponseTypeDef",
    "ValidationConfigurationTypeDef",
    "ViewFrameTypeDef",
)

AllowedStatisticsTypeDef = TypedDict(
    "AllowedStatisticsTypeDef",
    {
        "Statistics": Sequence[str],
    },
)

BatchDeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "BatchDeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersions": Sequence[str],
    },
)

BatchDeleteRecipeVersionResponseTypeDef = TypedDict(
    "BatchDeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "Errors": List["RecipeVersionErrorDetailTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnSelectorTypeDef = TypedDict(
    "ColumnSelectorTypeDef",
    {
        "Regex": NotRequired[str],
        "Name": NotRequired[str],
    },
)

ColumnStatisticsConfigurationTypeDef = TypedDict(
    "ColumnStatisticsConfigurationTypeDef",
    {
        "Statistics": "StatisticsConfigurationTypeDef",
        "Selectors": NotRequired[Sequence["ColumnSelectorTypeDef"]],
    },
)

ConditionExpressionTypeDef = TypedDict(
    "ConditionExpressionTypeDef",
    {
        "Condition": str,
        "TargetColumn": str,
        "Value": NotRequired[str],
    },
)

CreateDatasetRequestRequestTypeDef = TypedDict(
    "CreateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired["FormatOptionsTypeDef"],
        "PathOptions": NotRequired["PathOptionsTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProfileJobRequestRequestTypeDef = TypedDict(
    "CreateProfileJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Configuration": NotRequired["ProfileConfigurationTypeDef"],
        "ValidationConfigurations": NotRequired[Sequence["ValidationConfigurationTypeDef"]],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired["JobSampleTypeDef"],
    },
)

CreateProfileJobResponseTypeDef = TypedDict(
    "CreateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "DatasetName": str,
        "Name": str,
        "RecipeName": str,
        "RoleArn": str,
        "Sample": NotRequired["SampleTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateProjectResponseTypeDef = TypedDict(
    "CreateProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecipeJobRequestRequestTypeDef = TypedDict(
    "CreateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence["OutputTypeDef"]],
        "DataCatalogOutputs": NotRequired[Sequence["DataCatalogOutputTypeDef"]],
        "DatabaseOutputs": NotRequired[Sequence["DatabaseOutputTypeDef"]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired["RecipeReferenceTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "Timeout": NotRequired[int],
    },
)

CreateRecipeJobResponseTypeDef = TypedDict(
    "CreateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecipeRequestRequestTypeDef = TypedDict(
    "CreateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Steps": Sequence["RecipeStepTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRecipeResponseTypeDef = TypedDict(
    "CreateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRulesetRequestRequestTypeDef = TypedDict(
    "CreateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "Rules": Sequence["RuleTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRulesetResponseTypeDef = TypedDict(
    "CreateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScheduleRequestRequestTypeDef = TypedDict(
    "CreateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateScheduleResponseTypeDef = TypedDict(
    "CreateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CsvOptionsTypeDef = TypedDict(
    "CsvOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
        "HeaderRow": NotRequired[bool],
    },
)

CsvOutputOptionsTypeDef = TypedDict(
    "CsvOutputOptionsTypeDef",
    {
        "Delimiter": NotRequired[str],
    },
)

DataCatalogInputDefinitionTypeDef = TypedDict(
    "DataCatalogInputDefinitionTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TempDirectory": NotRequired["S3LocationTypeDef"],
    },
)

DataCatalogOutputTypeDef = TypedDict(
    "DataCatalogOutputTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "S3Options": NotRequired["S3TableOutputOptionsTypeDef"],
        "DatabaseOptions": NotRequired["DatabaseTableOutputOptionsTypeDef"],
        "Overwrite": NotRequired[bool],
    },
)

DatabaseInputDefinitionTypeDef = TypedDict(
    "DatabaseInputDefinitionTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseTableName": NotRequired[str],
        "TempDirectory": NotRequired["S3LocationTypeDef"],
        "QueryString": NotRequired[str],
    },
)

DatabaseOutputTypeDef = TypedDict(
    "DatabaseOutputTypeDef",
    {
        "GlueConnectionName": str,
        "DatabaseOptions": "DatabaseTableOutputOptionsTypeDef",
        "DatabaseOutputMode": NotRequired[Literal["NEW_TABLE"]],
    },
)

DatabaseTableOutputOptionsTypeDef = TypedDict(
    "DatabaseTableOutputOptionsTypeDef",
    {
        "TableName": str,
        "TempDirectory": NotRequired["S3LocationTypeDef"],
    },
)

DatasetParameterTypeDef = TypedDict(
    "DatasetParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterTypeType,
        "DatetimeOptions": NotRequired["DatetimeOptionsTypeDef"],
        "CreateColumn": NotRequired[bool],
        "Filter": NotRequired["FilterExpressionTypeDef"],
    },
)

DatasetTypeDef = TypedDict(
    "DatasetTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired["FormatOptionsTypeDef"],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "Source": NotRequired[SourceType],
        "PathOptions": NotRequired["PathOptionsTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "ResourceArn": NotRequired[str],
    },
)

DatetimeOptionsTypeDef = TypedDict(
    "DatetimeOptionsTypeDef",
    {
        "Format": str,
        "TimezoneOffset": NotRequired[str],
        "LocaleCode": NotRequired[str],
    },
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDatasetResponseTypeDef = TypedDict(
    "DeleteDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteJobRequestRequestTypeDef = TypedDict(
    "DeleteJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteJobResponseTypeDef = TypedDict(
    "DeleteJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteProjectResponseTypeDef = TypedDict(
    "DeleteProjectResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRecipeVersionRequestRequestTypeDef = TypedDict(
    "DeleteRecipeVersionRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
    },
)

DeleteRecipeVersionResponseTypeDef = TypedDict(
    "DeleteRecipeVersionResponseTypeDef",
    {
        "Name": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRulesetRequestRequestTypeDef = TypedDict(
    "DeleteRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteRulesetResponseTypeDef = TypedDict(
    "DeleteRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteScheduleRequestRequestTypeDef = TypedDict(
    "DeleteScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScheduleResponseTypeDef = TypedDict(
    "DeleteScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "Name": str,
        "Format": InputFormatType,
        "FormatOptions": "FormatOptionsTypeDef",
        "Input": "InputTypeDef",
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Source": SourceType,
        "PathOptions": "PathOptionsTypeDef",
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRequestRequestTypeDef = TypedDict(
    "DescribeJobRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeJobResponseTypeDef = TypedDict(
    "DescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionModeType,
        "Name": str,
        "Type": JobTypeType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscriptionType,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "ProjectName": str,
        "ProfileConfiguration": "ProfileConfigurationTypeDef",
        "ValidationConfigurations": List["ValidationConfigurationTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeJobRunRequestRequestTypeDef = TypedDict(
    "DescribeJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

DescribeJobRunResponseTypeDef = TypedDict(
    "DescribeJobRunResponseTypeDef",
    {
        "Attempt": int,
        "CompletedOn": datetime,
        "DatasetName": str,
        "ErrorMessage": str,
        "ExecutionTime": int,
        "JobName": str,
        "ProfileConfiguration": "ProfileConfigurationTypeDef",
        "ValidationConfigurations": List["ValidationConfigurationTypeDef"],
        "RunId": str,
        "State": JobRunStateType,
        "LogSubscription": LogSubscriptionType,
        "LogGroupName": str,
        "Outputs": List["OutputTypeDef"],
        "DataCatalogOutputs": List["DataCatalogOutputTypeDef"],
        "DatabaseOutputs": List["DatabaseOutputTypeDef"],
        "RecipeReference": "RecipeReferenceTypeDef",
        "StartedBy": str,
        "StartedOn": datetime,
        "JobSample": "JobSampleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "LastModifiedDate": datetime,
        "LastModifiedBy": str,
        "Name": str,
        "RecipeName": str,
        "ResourceArn": str,
        "Sample": "SampleTypeDef",
        "RoleArn": str,
        "Tags": Dict[str, str],
        "SessionStatus": SessionStatusType,
        "OpenedBy": str,
        "OpenDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRecipeRequestRequestTypeDef = TypedDict(
    "DescribeRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)

DescribeRecipeResponseTypeDef = TypedDict(
    "DescribeRecipeResponseTypeDef",
    {
        "CreatedBy": str,
        "CreateDate": datetime,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ProjectName": str,
        "PublishedBy": str,
        "PublishedDate": datetime,
        "Description": str,
        "Name": str,
        "Steps": List["RecipeStepTypeDef"],
        "Tags": Dict[str, str],
        "ResourceArn": str,
        "RecipeVersion": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRulesetRequestRequestTypeDef = TypedDict(
    "DescribeRulesetRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeRulesetResponseTypeDef = TypedDict(
    "DescribeRulesetResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "TargetArn": str,
        "Rules": List["RuleTypeDef"],
        "CreateDate": datetime,
        "CreatedBy": str,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduleRequestRequestTypeDef = TypedDict(
    "DescribeScheduleRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "JobNames": List[str],
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "ResourceArn": str,
        "CronExpression": str,
        "Tags": Dict[str, str],
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EntityDetectorConfigurationTypeDef = TypedDict(
    "EntityDetectorConfigurationTypeDef",
    {
        "EntityTypes": Sequence[str],
        "AllowedStatistics": NotRequired[Sequence["AllowedStatisticsTypeDef"]],
    },
)

ExcelOptionsTypeDef = TypedDict(
    "ExcelOptionsTypeDef",
    {
        "SheetNames": NotRequired[Sequence[str]],
        "SheetIndexes": NotRequired[Sequence[int]],
        "HeaderRow": NotRequired[bool],
    },
)

FilesLimitTypeDef = TypedDict(
    "FilesLimitTypeDef",
    {
        "MaxFiles": int,
        "OrderedBy": NotRequired[Literal["LAST_MODIFIED_DATE"]],
        "Order": NotRequired[OrderType],
    },
)

FilterExpressionTypeDef = TypedDict(
    "FilterExpressionTypeDef",
    {
        "Expression": str,
        "ValuesMap": Mapping[str, str],
    },
)

FormatOptionsTypeDef = TypedDict(
    "FormatOptionsTypeDef",
    {
        "Json": NotRequired["JsonOptionsTypeDef"],
        "Excel": NotRequired["ExcelOptionsTypeDef"],
        "Csv": NotRequired["CsvOptionsTypeDef"],
    },
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "S3InputDefinition": NotRequired["S3LocationTypeDef"],
        "DataCatalogInputDefinition": NotRequired["DataCatalogInputDefinitionTypeDef"],
        "DatabaseInputDefinition": NotRequired["DatabaseInputDefinitionTypeDef"],
        "Metadata": NotRequired["MetadataTypeDef"],
    },
)

JobRunTypeDef = TypedDict(
    "JobRunTypeDef",
    {
        "Attempt": NotRequired[int],
        "CompletedOn": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "ExecutionTime": NotRequired[int],
        "JobName": NotRequired[str],
        "RunId": NotRequired[str],
        "State": NotRequired[JobRunStateType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "LogGroupName": NotRequired[str],
        "Outputs": NotRequired[List["OutputTypeDef"]],
        "DataCatalogOutputs": NotRequired[List["DataCatalogOutputTypeDef"]],
        "DatabaseOutputs": NotRequired[List["DatabaseOutputTypeDef"]],
        "RecipeReference": NotRequired["RecipeReferenceTypeDef"],
        "StartedBy": NotRequired[str],
        "StartedOn": NotRequired[datetime],
        "JobSample": NotRequired["JobSampleTypeDef"],
        "ValidationConfigurations": NotRequired[List["ValidationConfigurationTypeDef"]],
    },
)

JobSampleTypeDef = TypedDict(
    "JobSampleTypeDef",
    {
        "Mode": NotRequired[SampleModeType],
        "Size": NotRequired[int],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "DatasetName": NotRequired[str],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "Type": NotRequired[JobTypeType],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[List["OutputTypeDef"]],
        "DataCatalogOutputs": NotRequired[List["DataCatalogOutputTypeDef"]],
        "DatabaseOutputs": NotRequired[List["DatabaseOutputTypeDef"]],
        "ProjectName": NotRequired[str],
        "RecipeReference": NotRequired["RecipeReferenceTypeDef"],
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "Timeout": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "JobSample": NotRequired["JobSampleTypeDef"],
        "ValidationConfigurations": NotRequired[List["ValidationConfigurationTypeDef"]],
    },
)

JsonOptionsTypeDef = TypedDict(
    "JsonOptionsTypeDef",
    {
        "MultiLine": NotRequired[bool],
    },
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "Datasets": List["DatasetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobRunsRequestRequestTypeDef = TypedDict(
    "ListJobRunsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListJobRunsResponseTypeDef = TypedDict(
    "ListJobRunsResponseTypeDef",
    {
        "JobRuns": List["JobRunTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsRequestRequestTypeDef = TypedDict(
    "ListJobsRequestRequestTypeDef",
    {
        "DatasetName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ProjectName": NotRequired[str],
    },
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "Projects": List["ProjectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipeVersionsRequestRequestTypeDef = TypedDict(
    "ListRecipeVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRecipeVersionsResponseTypeDef = TypedDict(
    "ListRecipeVersionsResponseTypeDef",
    {
        "NextToken": str,
        "Recipes": List["RecipeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecipesRequestRequestTypeDef = TypedDict(
    "ListRecipesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "RecipeVersion": NotRequired[str],
    },
)

ListRecipesResponseTypeDef = TypedDict(
    "ListRecipesResponseTypeDef",
    {
        "Recipes": List["RecipeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRulesetsRequestRequestTypeDef = TypedDict(
    "ListRulesetsRequestRequestTypeDef",
    {
        "TargetArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRulesetsResponseTypeDef = TypedDict(
    "ListRulesetsResponseTypeDef",
    {
        "Rulesets": List["RulesetItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchedulesRequestRequestTypeDef = TypedDict(
    "ListSchedulesRequestRequestTypeDef",
    {
        "JobName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSchedulesResponseTypeDef = TypedDict(
    "ListSchedulesResponseTypeDef",
    {
        "Schedules": List["ScheduleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetadataTypeDef = TypedDict(
    "MetadataTypeDef",
    {
        "SourceArn": NotRequired[str],
    },
)

OutputFormatOptionsTypeDef = TypedDict(
    "OutputFormatOptionsTypeDef",
    {
        "Csv": NotRequired["CsvOutputOptionsTypeDef"],
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Location": "S3LocationTypeDef",
        "CompressionFormat": NotRequired[CompressionFormatType],
        "Format": NotRequired[OutputFormatType],
        "PartitionColumns": NotRequired[Sequence[str]],
        "Overwrite": NotRequired[bool],
        "FormatOptions": NotRequired["OutputFormatOptionsTypeDef"],
        "MaxOutputFiles": NotRequired[int],
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

PathOptionsTypeDef = TypedDict(
    "PathOptionsTypeDef",
    {
        "LastModifiedDateCondition": NotRequired["FilterExpressionTypeDef"],
        "FilesLimit": NotRequired["FilesLimitTypeDef"],
        "Parameters": NotRequired[Mapping[str, "DatasetParameterTypeDef"]],
    },
)

ProfileConfigurationTypeDef = TypedDict(
    "ProfileConfigurationTypeDef",
    {
        "DatasetStatisticsConfiguration": NotRequired["StatisticsConfigurationTypeDef"],
        "ProfileColumns": NotRequired[Sequence["ColumnSelectorTypeDef"]],
        "ColumnStatisticsConfigurations": NotRequired[
            Sequence["ColumnStatisticsConfigurationTypeDef"]
        ],
        "EntityDetectorConfiguration": NotRequired["EntityDetectorConfigurationTypeDef"],
    },
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "Name": str,
        "RecipeName": str,
        "AccountId": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "CreatedBy": NotRequired[str],
        "DatasetName": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Sample": NotRequired["SampleTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
        "RoleArn": NotRequired[str],
        "OpenedBy": NotRequired[str],
        "OpenDate": NotRequired[datetime],
    },
)

PublishRecipeRequestRequestTypeDef = TypedDict(
    "PublishRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)

PublishRecipeResponseTypeDef = TypedDict(
    "PublishRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecipeActionTypeDef = TypedDict(
    "RecipeActionTypeDef",
    {
        "Operation": str,
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

RecipeReferenceTypeDef = TypedDict(
    "RecipeReferenceTypeDef",
    {
        "Name": str,
        "RecipeVersion": NotRequired[str],
    },
)

RecipeStepTypeDef = TypedDict(
    "RecipeStepTypeDef",
    {
        "Action": "RecipeActionTypeDef",
        "ConditionExpressions": NotRequired[Sequence["ConditionExpressionTypeDef"]],
    },
)

RecipeTypeDef = TypedDict(
    "RecipeTypeDef",
    {
        "Name": str,
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ProjectName": NotRequired[str],
        "PublishedBy": NotRequired[str],
        "PublishedDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Steps": NotRequired[List["RecipeStepTypeDef"]],
        "Tags": NotRequired[Dict[str, str]],
        "RecipeVersion": NotRequired[str],
    },
)

RecipeVersionErrorDetailTypeDef = TypedDict(
    "RecipeVersionErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "RecipeVersion": NotRequired[str],
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

RuleTypeDef = TypedDict(
    "RuleTypeDef",
    {
        "Name": str,
        "CheckExpression": str,
        "Disabled": NotRequired[bool],
        "SubstitutionMap": NotRequired[Mapping[str, str]],
        "Threshold": NotRequired["ThresholdTypeDef"],
        "ColumnSelectors": NotRequired[Sequence["ColumnSelectorTypeDef"]],
    },
)

RulesetItemTypeDef = TypedDict(
    "RulesetItemTypeDef",
    {
        "Name": str,
        "TargetArn": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "Description": NotRequired[str],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "RuleCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": str,
        "Key": NotRequired[str],
        "BucketOwner": NotRequired[str],
    },
)

S3TableOutputOptionsTypeDef = TypedDict(
    "S3TableOutputOptionsTypeDef",
    {
        "Location": "S3LocationTypeDef",
    },
)

SampleTypeDef = TypedDict(
    "SampleTypeDef",
    {
        "Type": SampleTypeType,
        "Size": NotRequired[int],
    },
)

ScheduleTypeDef = TypedDict(
    "ScheduleTypeDef",
    {
        "Name": str,
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "JobNames": NotRequired[List[str]],
        "LastModifiedBy": NotRequired[str],
        "LastModifiedDate": NotRequired[datetime],
        "ResourceArn": NotRequired[str],
        "CronExpression": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

SendProjectSessionActionRequestRequestTypeDef = TypedDict(
    "SendProjectSessionActionRequestRequestTypeDef",
    {
        "Name": str,
        "Preview": NotRequired[bool],
        "RecipeStep": NotRequired["RecipeStepTypeDef"],
        "StepIndex": NotRequired[int],
        "ClientSessionId": NotRequired[str],
        "ViewFrame": NotRequired["ViewFrameTypeDef"],
    },
)

SendProjectSessionActionResponseTypeDef = TypedDict(
    "SendProjectSessionActionResponseTypeDef",
    {
        "Result": str,
        "Name": str,
        "ActionId": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartJobRunRequestRequestTypeDef = TypedDict(
    "StartJobRunRequestRequestTypeDef",
    {
        "Name": str,
    },
)

StartJobRunResponseTypeDef = TypedDict(
    "StartJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartProjectSessionRequestRequestTypeDef = TypedDict(
    "StartProjectSessionRequestRequestTypeDef",
    {
        "Name": str,
        "AssumeControl": NotRequired[bool],
    },
)

StartProjectSessionResponseTypeDef = TypedDict(
    "StartProjectSessionResponseTypeDef",
    {
        "Name": str,
        "ClientSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StatisticOverrideTypeDef = TypedDict(
    "StatisticOverrideTypeDef",
    {
        "Statistic": str,
        "Parameters": Mapping[str, str],
    },
)

StatisticsConfigurationTypeDef = TypedDict(
    "StatisticsConfigurationTypeDef",
    {
        "IncludedStatistics": NotRequired[Sequence[str]],
        "Overrides": NotRequired[Sequence["StatisticOverrideTypeDef"]],
    },
)

StopJobRunRequestRequestTypeDef = TypedDict(
    "StopJobRunRequestRequestTypeDef",
    {
        "Name": str,
        "RunId": str,
    },
)

StopJobRunResponseTypeDef = TypedDict(
    "StopJobRunResponseTypeDef",
    {
        "RunId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef",
    {
        "Value": float,
        "Type": NotRequired[ThresholdTypeType],
        "Unit": NotRequired[ThresholdUnitType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDatasetRequestRequestTypeDef = TypedDict(
    "UpdateDatasetRequestRequestTypeDef",
    {
        "Name": str,
        "Input": "InputTypeDef",
        "Format": NotRequired[InputFormatType],
        "FormatOptions": NotRequired["FormatOptionsTypeDef"],
        "PathOptions": NotRequired["PathOptionsTypeDef"],
    },
)

UpdateDatasetResponseTypeDef = TypedDict(
    "UpdateDatasetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProfileJobRequestRequestTypeDef = TypedDict(
    "UpdateProfileJobRequestRequestTypeDef",
    {
        "Name": str,
        "OutputLocation": "S3LocationTypeDef",
        "RoleArn": str,
        "Configuration": NotRequired["ProfileConfigurationTypeDef"],
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "ValidationConfigurations": NotRequired[Sequence["ValidationConfigurationTypeDef"]],
        "Timeout": NotRequired[int],
        "JobSample": NotRequired["JobSampleTypeDef"],
    },
)

UpdateProfileJobResponseTypeDef = TypedDict(
    "UpdateProfileJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "RoleArn": str,
        "Name": str,
        "Sample": NotRequired["SampleTypeDef"],
    },
)

UpdateProjectResponseTypeDef = TypedDict(
    "UpdateProjectResponseTypeDef",
    {
        "LastModifiedDate": datetime,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecipeJobRequestRequestTypeDef = TypedDict(
    "UpdateRecipeJobRequestRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "EncryptionKeyArn": NotRequired[str],
        "EncryptionMode": NotRequired[EncryptionModeType],
        "LogSubscription": NotRequired[LogSubscriptionType],
        "MaxCapacity": NotRequired[int],
        "MaxRetries": NotRequired[int],
        "Outputs": NotRequired[Sequence["OutputTypeDef"]],
        "DataCatalogOutputs": NotRequired[Sequence["DataCatalogOutputTypeDef"]],
        "DatabaseOutputs": NotRequired[Sequence["DatabaseOutputTypeDef"]],
        "Timeout": NotRequired[int],
    },
)

UpdateRecipeJobResponseTypeDef = TypedDict(
    "UpdateRecipeJobResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRecipeRequestRequestTypeDef = TypedDict(
    "UpdateRecipeRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Steps": NotRequired[Sequence["RecipeStepTypeDef"]],
    },
)

UpdateRecipeResponseTypeDef = TypedDict(
    "UpdateRecipeResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRulesetRequestRequestTypeDef = TypedDict(
    "UpdateRulesetRequestRequestTypeDef",
    {
        "Name": str,
        "Rules": Sequence["RuleTypeDef"],
        "Description": NotRequired[str],
    },
)

UpdateRulesetResponseTypeDef = TypedDict(
    "UpdateRulesetResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScheduleRequestRequestTypeDef = TypedDict(
    "UpdateScheduleRequestRequestTypeDef",
    {
        "CronExpression": str,
        "Name": str,
        "JobNames": NotRequired[Sequence[str]],
    },
)

UpdateScheduleResponseTypeDef = TypedDict(
    "UpdateScheduleResponseTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidationConfigurationTypeDef = TypedDict(
    "ValidationConfigurationTypeDef",
    {
        "RulesetArn": str,
        "ValidationMode": NotRequired[Literal["CHECK_ALL"]],
    },
)

ViewFrameTypeDef = TypedDict(
    "ViewFrameTypeDef",
    {
        "StartColumnIndex": int,
        "ColumnRange": NotRequired[int],
        "HiddenColumns": NotRequired[Sequence[str]],
        "StartRowIndex": NotRequired[int],
        "RowRange": NotRequired[int],
        "Analytics": NotRequired[AnalyticsModeType],
    },
)
