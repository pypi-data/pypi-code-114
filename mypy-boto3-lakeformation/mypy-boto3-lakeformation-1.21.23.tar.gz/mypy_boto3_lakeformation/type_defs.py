"""
Type annotations for lakeformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lakeformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lakeformation.type_defs import AddLFTagsToResourceRequestRequestTypeDef

    data: AddLFTagsToResourceRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ComparisonOperatorType,
    DataLakeResourceTypeType,
    FieldNameStringType,
    OptimizerTypeType,
    PermissionType,
    PermissionTypeType,
    QueryStateStringType,
    ResourceShareTypeType,
    ResourceTypeType,
    TransactionStatusFilterType,
    TransactionStatusType,
    TransactionTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddLFTagsToResourceRequestRequestTypeDef",
    "AddLFTagsToResourceResponseTypeDef",
    "AddObjectInputTypeDef",
    "AuditContextTypeDef",
    "BatchGrantPermissionsRequestRequestTypeDef",
    "BatchGrantPermissionsResponseTypeDef",
    "BatchPermissionsFailureEntryTypeDef",
    "BatchPermissionsRequestEntryTypeDef",
    "BatchRevokePermissionsRequestRequestTypeDef",
    "BatchRevokePermissionsResponseTypeDef",
    "CancelTransactionRequestRequestTypeDef",
    "ColumnLFTagTypeDef",
    "ColumnWildcardTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CommitTransactionResponseTypeDef",
    "CreateDataCellsFilterRequestRequestTypeDef",
    "CreateLFTagRequestRequestTypeDef",
    "DataCellsFilterResourceTypeDef",
    "DataCellsFilterTypeDef",
    "DataLakePrincipalTypeDef",
    "DataLakeSettingsTypeDef",
    "DataLocationResourceTypeDef",
    "DatabaseResourceTypeDef",
    "DeleteDataCellsFilterRequestRequestTypeDef",
    "DeleteLFTagRequestRequestTypeDef",
    "DeleteObjectInputTypeDef",
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    "DeregisterResourceRequestRequestTypeDef",
    "DescribeResourceRequestRequestTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeTransactionRequestRequestTypeDef",
    "DescribeTransactionResponseTypeDef",
    "DetailsMapTypeDef",
    "ErrorDetailTypeDef",
    "ExecutionStatisticsTypeDef",
    "ExtendTransactionRequestRequestTypeDef",
    "FilterConditionTypeDef",
    "GetDataLakeSettingsRequestRequestTypeDef",
    "GetDataLakeSettingsResponseTypeDef",
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    "GetEffectivePermissionsForPathResponseTypeDef",
    "GetLFTagRequestRequestTypeDef",
    "GetLFTagResponseTypeDef",
    "GetQueryStateRequestRequestTypeDef",
    "GetQueryStateResponseTypeDef",
    "GetQueryStatisticsRequestRequestTypeDef",
    "GetQueryStatisticsResponseTypeDef",
    "GetResourceLFTagsRequestRequestTypeDef",
    "GetResourceLFTagsResponseTypeDef",
    "GetTableObjectsRequestRequestTypeDef",
    "GetTableObjectsResponseTypeDef",
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    "GetWorkUnitResultsRequestRequestTypeDef",
    "GetWorkUnitResultsResponseTypeDef",
    "GetWorkUnitsRequestRequestTypeDef",
    "GetWorkUnitsResponseTypeDef",
    "GrantPermissionsRequestRequestTypeDef",
    "LFTagErrorTypeDef",
    "LFTagKeyResourceTypeDef",
    "LFTagPairTypeDef",
    "LFTagPolicyResourceTypeDef",
    "LFTagTypeDef",
    "ListDataCellsFilterRequestRequestTypeDef",
    "ListDataCellsFilterResponseTypeDef",
    "ListLFTagsRequestRequestTypeDef",
    "ListLFTagsResponseTypeDef",
    "ListPermissionsRequestRequestTypeDef",
    "ListPermissionsResponseTypeDef",
    "ListResourcesRequestRequestTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTableStorageOptimizersRequestRequestTypeDef",
    "ListTableStorageOptimizersResponseTypeDef",
    "ListTransactionsRequestRequestTypeDef",
    "ListTransactionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionObjectsTypeDef",
    "PartitionValueListTypeDef",
    "PlanningStatisticsTypeDef",
    "PrincipalPermissionsTypeDef",
    "PrincipalResourcePermissionsTypeDef",
    "PutDataLakeSettingsRequestRequestTypeDef",
    "QueryPlanningContextTypeDef",
    "RegisterResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    "RemoveLFTagsFromResourceResponseTypeDef",
    "ResourceInfoTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "RevokePermissionsRequestRequestTypeDef",
    "RowFilterTypeDef",
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    "SearchDatabasesByLFTagsResponseTypeDef",
    "SearchTablesByLFTagsRequestRequestTypeDef",
    "SearchTablesByLFTagsResponseTypeDef",
    "StartQueryPlanningRequestRequestTypeDef",
    "StartQueryPlanningResponseTypeDef",
    "StartTransactionRequestRequestTypeDef",
    "StartTransactionResponseTypeDef",
    "StorageOptimizerTypeDef",
    "TableObjectTypeDef",
    "TableResourceTypeDef",
    "TableWithColumnsResourceTypeDef",
    "TaggedDatabaseTypeDef",
    "TaggedTableTypeDef",
    "TransactionDescriptionTypeDef",
    "UpdateLFTagRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateTableObjectsRequestRequestTypeDef",
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    "UpdateTableStorageOptimizerResponseTypeDef",
    "VirtualObjectTypeDef",
    "WorkUnitRangeTypeDef",
    "WriteOperationTypeDef",
)

AddLFTagsToResourceRequestRequestTypeDef = TypedDict(
    "AddLFTagsToResourceRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": Sequence["LFTagPairTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

AddLFTagsToResourceResponseTypeDef = TypedDict(
    "AddLFTagsToResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddObjectInputTypeDef = TypedDict(
    "AddObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": str,
        "Size": int,
        "PartitionValues": NotRequired[Sequence[str]],
    },
)

AuditContextTypeDef = TypedDict(
    "AuditContextTypeDef",
    {
        "AdditionalAuditContext": NotRequired[str],
    },
)

BatchGrantPermissionsRequestRequestTypeDef = TypedDict(
    "BatchGrantPermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence["BatchPermissionsRequestEntryTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchGrantPermissionsResponseTypeDef = TypedDict(
    "BatchGrantPermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchPermissionsFailureEntryTypeDef = TypedDict(
    "BatchPermissionsFailureEntryTypeDef",
    {
        "RequestEntry": NotRequired["BatchPermissionsRequestEntryTypeDef"],
        "Error": NotRequired["ErrorDetailTypeDef"],
    },
)

BatchPermissionsRequestEntryTypeDef = TypedDict(
    "BatchPermissionsRequestEntryTypeDef",
    {
        "Id": str,
        "Principal": NotRequired["DataLakePrincipalTypeDef"],
        "Resource": NotRequired["ResourceTypeDef"],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)

BatchRevokePermissionsRequestRequestTypeDef = TypedDict(
    "BatchRevokePermissionsRequestRequestTypeDef",
    {
        "Entries": Sequence["BatchPermissionsRequestEntryTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

BatchRevokePermissionsResponseTypeDef = TypedDict(
    "BatchRevokePermissionsResponseTypeDef",
    {
        "Failures": List["BatchPermissionsFailureEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelTransactionRequestRequestTypeDef = TypedDict(
    "CancelTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

ColumnLFTagTypeDef = TypedDict(
    "ColumnLFTagTypeDef",
    {
        "Name": NotRequired[str],
        "LFTags": NotRequired[List["LFTagPairTypeDef"]],
    },
)

ColumnWildcardTypeDef = TypedDict(
    "ColumnWildcardTypeDef",
    {
        "ExcludedColumnNames": NotRequired[Sequence[str]],
    },
)

CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "TransactionStatus": TransactionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDataCellsFilterRequestRequestTypeDef = TypedDict(
    "CreateDataCellsFilterRequestRequestTypeDef",
    {
        "TableData": "DataCellsFilterTypeDef",
    },
)

CreateLFTagRequestRequestTypeDef = TypedDict(
    "CreateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

DataCellsFilterResourceTypeDef = TypedDict(
    "DataCellsFilterResourceTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)

DataCellsFilterTypeDef = TypedDict(
    "DataCellsFilterTypeDef",
    {
        "TableCatalogId": str,
        "DatabaseName": str,
        "TableName": str,
        "Name": str,
        "RowFilter": NotRequired["RowFilterTypeDef"],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired["ColumnWildcardTypeDef"],
    },
)

DataLakePrincipalTypeDef = TypedDict(
    "DataLakePrincipalTypeDef",
    {
        "DataLakePrincipalIdentifier": NotRequired[str],
    },
)

DataLakeSettingsTypeDef = TypedDict(
    "DataLakeSettingsTypeDef",
    {
        "DataLakeAdmins": NotRequired[List["DataLakePrincipalTypeDef"]],
        "CreateDatabaseDefaultPermissions": NotRequired[List["PrincipalPermissionsTypeDef"]],
        "CreateTableDefaultPermissions": NotRequired[List["PrincipalPermissionsTypeDef"]],
        "TrustedResourceOwners": NotRequired[List[str]],
        "AllowExternalDataFiltering": NotRequired[bool],
        "ExternalDataFilteringAllowList": NotRequired[List["DataLakePrincipalTypeDef"]],
        "AuthorizedSessionTagValueList": NotRequired[List[str]],
    },
)

DataLocationResourceTypeDef = TypedDict(
    "DataLocationResourceTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
    },
)

DatabaseResourceTypeDef = TypedDict(
    "DatabaseResourceTypeDef",
    {
        "Name": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteDataCellsFilterRequestRequestTypeDef = TypedDict(
    "DeleteDataCellsFilterRequestRequestTypeDef",
    {
        "TableCatalogId": NotRequired[str],
        "DatabaseName": NotRequired[str],
        "TableName": NotRequired[str],
        "Name": NotRequired[str],
    },
)

DeleteLFTagRequestRequestTypeDef = TypedDict(
    "DeleteLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)

DeleteObjectInputTypeDef = TypedDict(
    "DeleteObjectInputTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
        "PartitionValues": NotRequired[Sequence[str]],
    },
)

DeleteObjectsOnCancelRequestRequestTypeDef = TypedDict(
    "DeleteObjectsOnCancelRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "TransactionId": str,
        "Objects": Sequence["VirtualObjectTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

DeregisterResourceRequestRequestTypeDef = TypedDict(
    "DeregisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceRequestRequestTypeDef = TypedDict(
    "DescribeResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceInfo": "ResourceInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransactionRequestRequestTypeDef = TypedDict(
    "DescribeTransactionRequestRequestTypeDef",
    {
        "TransactionId": str,
    },
)

DescribeTransactionResponseTypeDef = TypedDict(
    "DescribeTransactionResponseTypeDef",
    {
        "TransactionDescription": "TransactionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DetailsMapTypeDef = TypedDict(
    "DetailsMapTypeDef",
    {
        "ResourceShare": NotRequired[List[str]],
    },
)

ErrorDetailTypeDef = TypedDict(
    "ErrorDetailTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

ExecutionStatisticsTypeDef = TypedDict(
    "ExecutionStatisticsTypeDef",
    {
        "AverageExecutionTimeMillis": NotRequired[int],
        "DataScannedBytes": NotRequired[int],
        "WorkUnitsExecutedCount": NotRequired[int],
    },
)

ExtendTransactionRequestRequestTypeDef = TypedDict(
    "ExtendTransactionRequestRequestTypeDef",
    {
        "TransactionId": NotRequired[str],
    },
)

FilterConditionTypeDef = TypedDict(
    "FilterConditionTypeDef",
    {
        "Field": NotRequired[FieldNameStringType],
        "ComparisonOperator": NotRequired[ComparisonOperatorType],
        "StringValueList": NotRequired[Sequence[str]],
    },
)

GetDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "GetDataLakeSettingsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
    },
)

GetDataLakeSettingsResponseTypeDef = TypedDict(
    "GetDataLakeSettingsResponseTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEffectivePermissionsForPathRequestRequestTypeDef = TypedDict(
    "GetEffectivePermissionsForPathRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "CatalogId": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetEffectivePermissionsForPathResponseTypeDef = TypedDict(
    "GetEffectivePermissionsForPathResponseTypeDef",
    {
        "Permissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLFTagRequestRequestTypeDef = TypedDict(
    "GetLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
    },
)

GetLFTagResponseTypeDef = TypedDict(
    "GetLFTagResponseTypeDef",
    {
        "CatalogId": str,
        "TagKey": str,
        "TagValues": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryStateRequestRequestTypeDef = TypedDict(
    "GetQueryStateRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

GetQueryStateResponseTypeDef = TypedDict(
    "GetQueryStateResponseTypeDef",
    {
        "Error": str,
        "State": QueryStateStringType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryStatisticsRequestRequestTypeDef = TypedDict(
    "GetQueryStatisticsRequestRequestTypeDef",
    {
        "QueryId": str,
    },
)

GetQueryStatisticsResponseTypeDef = TypedDict(
    "GetQueryStatisticsResponseTypeDef",
    {
        "ExecutionStatistics": "ExecutionStatisticsTypeDef",
        "PlanningStatistics": "PlanningStatisticsTypeDef",
        "QuerySubmissionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceLFTagsRequestRequestTypeDef = TypedDict(
    "GetResourceLFTagsRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "CatalogId": NotRequired[str],
        "ShowAssignedLFTags": NotRequired[bool],
    },
)

GetResourceLFTagsResponseTypeDef = TypedDict(
    "GetResourceLFTagsResponseTypeDef",
    {
        "LFTagOnDatabase": List["LFTagPairTypeDef"],
        "LFTagsOnTable": List["LFTagPairTypeDef"],
        "LFTagsOnColumns": List["ColumnLFTagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableObjectsRequestRequestTypeDef = TypedDict(
    "GetTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
        "QueryAsOfTime": NotRequired[Union[datetime, str]],
        "PartitionPredicate": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetTableObjectsResponseTypeDef = TypedDict(
    "GetTableObjectsResponseTypeDef",
    {
        "Objects": List["PartitionObjectsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemporaryGluePartitionCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "Partition": "PartitionValueListTypeDef",
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired["AuditContextTypeDef"],
    },
)

GetTemporaryGluePartitionCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGluePartitionCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTemporaryGlueTableCredentialsRequestRequestTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsRequestRequestTypeDef",
    {
        "TableArn": str,
        "SupportedPermissionTypes": Sequence[PermissionTypeType],
        "Permissions": NotRequired[Sequence[PermissionType]],
        "DurationSeconds": NotRequired[int],
        "AuditContext": NotRequired["AuditContextTypeDef"],
    },
)

GetTemporaryGlueTableCredentialsResponseTypeDef = TypedDict(
    "GetTemporaryGlueTableCredentialsResponseTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkUnitResultsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitResultsRequestRequestTypeDef",
    {
        "QueryId": str,
        "WorkUnitId": int,
        "WorkUnitToken": str,
    },
)

GetWorkUnitResultsResponseTypeDef = TypedDict(
    "GetWorkUnitResultsResponseTypeDef",
    {
        "ResultStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkUnitsRequestRequestTypeDef = TypedDict(
    "GetWorkUnitsRequestRequestTypeDef",
    {
        "QueryId": str,
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[int],
    },
)

GetWorkUnitsResponseTypeDef = TypedDict(
    "GetWorkUnitsResponseTypeDef",
    {
        "NextToken": str,
        "QueryId": str,
        "WorkUnitRanges": List["WorkUnitRangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GrantPermissionsRequestRequestTypeDef = TypedDict(
    "GrantPermissionsRequestRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)

LFTagErrorTypeDef = TypedDict(
    "LFTagErrorTypeDef",
    {
        "LFTag": NotRequired["LFTagPairTypeDef"],
        "Error": NotRequired["ErrorDetailTypeDef"],
    },
)

LFTagKeyResourceTypeDef = TypedDict(
    "LFTagKeyResourceTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

LFTagPairTypeDef = TypedDict(
    "LFTagPairTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
        "CatalogId": NotRequired[str],
    },
)

LFTagPolicyResourceTypeDef = TypedDict(
    "LFTagPolicyResourceTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Expression": Sequence["LFTagTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

LFTagTypeDef = TypedDict(
    "LFTagTypeDef",
    {
        "TagKey": str,
        "TagValues": Sequence[str],
    },
)

ListDataCellsFilterRequestRequestTypeDef = TypedDict(
    "ListDataCellsFilterRequestRequestTypeDef",
    {
        "Table": NotRequired["TableResourceTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataCellsFilterResponseTypeDef = TypedDict(
    "ListDataCellsFilterResponseTypeDef",
    {
        "DataCellsFilters": List["DataCellsFilterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLFTagsRequestRequestTypeDef = TypedDict(
    "ListLFTagsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "ResourceShareType": NotRequired[ResourceShareTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListLFTagsResponseTypeDef = TypedDict(
    "ListLFTagsResponseTypeDef",
    {
        "LFTags": List["LFTagPairTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPermissionsRequestRequestTypeDef = TypedDict(
    "ListPermissionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "Principal": NotRequired["DataLakePrincipalTypeDef"],
        "ResourceType": NotRequired[DataLakeResourceTypeType],
        "Resource": NotRequired["ResourceTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "IncludeRelated": NotRequired[str],
    },
)

ListPermissionsResponseTypeDef = TypedDict(
    "ListPermissionsResponseTypeDef",
    {
        "PrincipalResourcePermissions": List["PrincipalResourcePermissionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListResourcesRequestRequestTypeDef = TypedDict(
    "ListResourcesRequestRequestTypeDef",
    {
        "FilterConditionList": NotRequired[Sequence["FilterConditionTypeDef"]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListResourcesResponseTypeDef = TypedDict(
    "ListResourcesResponseTypeDef",
    {
        "ResourceInfoList": List["ResourceInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTableStorageOptimizersRequestRequestTypeDef = TypedDict(
    "ListTableStorageOptimizersRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "CatalogId": NotRequired[str],
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTableStorageOptimizersResponseTypeDef = TypedDict(
    "ListTableStorageOptimizersResponseTypeDef",
    {
        "StorageOptimizerList": List["StorageOptimizerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTransactionsRequestRequestTypeDef = TypedDict(
    "ListTransactionsRequestRequestTypeDef",
    {
        "CatalogId": NotRequired[str],
        "StatusFilter": NotRequired[TransactionStatusFilterType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListTransactionsResponseTypeDef = TypedDict(
    "ListTransactionsResponseTypeDef",
    {
        "Transactions": List["TransactionDescriptionTypeDef"],
        "NextToken": str,
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

PartitionObjectsTypeDef = TypedDict(
    "PartitionObjectsTypeDef",
    {
        "PartitionValues": NotRequired[List[str]],
        "Objects": NotRequired[List["TableObjectTypeDef"]],
    },
)

PartitionValueListTypeDef = TypedDict(
    "PartitionValueListTypeDef",
    {
        "Values": Sequence[str],
    },
)

PlanningStatisticsTypeDef = TypedDict(
    "PlanningStatisticsTypeDef",
    {
        "EstimatedDataToScanBytes": NotRequired[int],
        "PlanningTimeMillis": NotRequired[int],
        "QueueTimeMillis": NotRequired[int],
        "WorkUnitsGeneratedCount": NotRequired[int],
    },
)

PrincipalPermissionsTypeDef = TypedDict(
    "PrincipalPermissionsTypeDef",
    {
        "Principal": NotRequired["DataLakePrincipalTypeDef"],
        "Permissions": NotRequired[List[PermissionType]],
    },
)

PrincipalResourcePermissionsTypeDef = TypedDict(
    "PrincipalResourcePermissionsTypeDef",
    {
        "Principal": NotRequired["DataLakePrincipalTypeDef"],
        "Resource": NotRequired["ResourceTypeDef"],
        "Permissions": NotRequired[List[PermissionType]],
        "PermissionsWithGrantOption": NotRequired[List[PermissionType]],
        "AdditionalDetails": NotRequired["DetailsMapTypeDef"],
    },
)

PutDataLakeSettingsRequestRequestTypeDef = TypedDict(
    "PutDataLakeSettingsRequestRequestTypeDef",
    {
        "DataLakeSettings": "DataLakeSettingsTypeDef",
        "CatalogId": NotRequired[str],
    },
)

QueryPlanningContextTypeDef = TypedDict(
    "QueryPlanningContextTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "QueryAsOfTime": NotRequired[Union[datetime, str]],
        "QueryParameters": NotRequired[Mapping[str, str]],
        "TransactionId": NotRequired[str],
    },
)

RegisterResourceRequestRequestTypeDef = TypedDict(
    "RegisterResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "UseServiceLinkedRole": NotRequired[bool],
        "RoleArn": NotRequired[str],
    },
)

RemoveLFTagsFromResourceRequestRequestTypeDef = TypedDict(
    "RemoveLFTagsFromResourceRequestRequestTypeDef",
    {
        "Resource": "ResourceTypeDef",
        "LFTags": Sequence["LFTagPairTypeDef"],
        "CatalogId": NotRequired[str],
    },
)

RemoveLFTagsFromResourceResponseTypeDef = TypedDict(
    "RemoveLFTagsFromResourceResponseTypeDef",
    {
        "Failures": List["LFTagErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "ResourceArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "LastModified": NotRequired[datetime],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Catalog": NotRequired[Mapping[str, Any]],
        "Database": NotRequired["DatabaseResourceTypeDef"],
        "Table": NotRequired["TableResourceTypeDef"],
        "TableWithColumns": NotRequired["TableWithColumnsResourceTypeDef"],
        "DataLocation": NotRequired["DataLocationResourceTypeDef"],
        "DataCellsFilter": NotRequired["DataCellsFilterResourceTypeDef"],
        "LFTag": NotRequired["LFTagKeyResourceTypeDef"],
        "LFTagPolicy": NotRequired["LFTagPolicyResourceTypeDef"],
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

RevokePermissionsRequestRequestTypeDef = TypedDict(
    "RevokePermissionsRequestRequestTypeDef",
    {
        "Principal": "DataLakePrincipalTypeDef",
        "Resource": "ResourceTypeDef",
        "Permissions": Sequence[PermissionType],
        "CatalogId": NotRequired[str],
        "PermissionsWithGrantOption": NotRequired[Sequence[PermissionType]],
    },
)

RowFilterTypeDef = TypedDict(
    "RowFilterTypeDef",
    {
        "FilterExpression": NotRequired[str],
        "AllRowsWildcard": NotRequired[Mapping[str, Any]],
    },
)

SearchDatabasesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchDatabasesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence["LFTagTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)

SearchDatabasesByLFTagsResponseTypeDef = TypedDict(
    "SearchDatabasesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "DatabaseList": List["TaggedDatabaseTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchTablesByLFTagsRequestRequestTypeDef = TypedDict(
    "SearchTablesByLFTagsRequestRequestTypeDef",
    {
        "Expression": Sequence["LFTagTypeDef"],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CatalogId": NotRequired[str],
    },
)

SearchTablesByLFTagsResponseTypeDef = TypedDict(
    "SearchTablesByLFTagsResponseTypeDef",
    {
        "NextToken": str,
        "TableList": List["TaggedTableTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartQueryPlanningRequestRequestTypeDef = TypedDict(
    "StartQueryPlanningRequestRequestTypeDef",
    {
        "QueryPlanningContext": "QueryPlanningContextTypeDef",
        "QueryString": str,
    },
)

StartQueryPlanningResponseTypeDef = TypedDict(
    "StartQueryPlanningResponseTypeDef",
    {
        "QueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartTransactionRequestRequestTypeDef = TypedDict(
    "StartTransactionRequestRequestTypeDef",
    {
        "TransactionType": NotRequired[TransactionTypeType],
    },
)

StartTransactionResponseTypeDef = TypedDict(
    "StartTransactionResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageOptimizerTypeDef = TypedDict(
    "StorageOptimizerTypeDef",
    {
        "StorageOptimizerType": NotRequired[OptimizerTypeType],
        "Config": NotRequired[Dict[str, str]],
        "ErrorMessage": NotRequired[str],
        "Warnings": NotRequired[str],
        "LastRunDetails": NotRequired[str],
    },
)

TableObjectTypeDef = TypedDict(
    "TableObjectTypeDef",
    {
        "Uri": NotRequired[str],
        "ETag": NotRequired[str],
        "Size": NotRequired[int],
    },
)

TableResourceTypeDef = TypedDict(
    "TableResourceTypeDef",
    {
        "DatabaseName": str,
        "CatalogId": NotRequired[str],
        "Name": NotRequired[str],
        "TableWildcard": NotRequired[Mapping[str, Any]],
    },
)

TableWithColumnsResourceTypeDef = TypedDict(
    "TableWithColumnsResourceTypeDef",
    {
        "DatabaseName": str,
        "Name": str,
        "CatalogId": NotRequired[str],
        "ColumnNames": NotRequired[Sequence[str]],
        "ColumnWildcard": NotRequired["ColumnWildcardTypeDef"],
    },
)

TaggedDatabaseTypeDef = TypedDict(
    "TaggedDatabaseTypeDef",
    {
        "Database": NotRequired["DatabaseResourceTypeDef"],
        "LFTags": NotRequired[List["LFTagPairTypeDef"]],
    },
)

TaggedTableTypeDef = TypedDict(
    "TaggedTableTypeDef",
    {
        "Table": NotRequired["TableResourceTypeDef"],
        "LFTagOnDatabase": NotRequired[List["LFTagPairTypeDef"]],
        "LFTagsOnTable": NotRequired[List["LFTagPairTypeDef"]],
        "LFTagsOnColumns": NotRequired[List["ColumnLFTagTypeDef"]],
    },
)

TransactionDescriptionTypeDef = TypedDict(
    "TransactionDescriptionTypeDef",
    {
        "TransactionId": NotRequired[str],
        "TransactionStatus": NotRequired[TransactionStatusType],
        "TransactionStartTime": NotRequired[datetime],
        "TransactionEndTime": NotRequired[datetime],
    },
)

UpdateLFTagRequestRequestTypeDef = TypedDict(
    "UpdateLFTagRequestRequestTypeDef",
    {
        "TagKey": str,
        "CatalogId": NotRequired[str],
        "TagValuesToDelete": NotRequired[Sequence[str]],
        "TagValuesToAdd": NotRequired[Sequence[str]],
    },
)

UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "RoleArn": str,
        "ResourceArn": str,
    },
)

UpdateTableObjectsRequestRequestTypeDef = TypedDict(
    "UpdateTableObjectsRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "WriteOperations": Sequence["WriteOperationTypeDef"],
        "CatalogId": NotRequired[str],
        "TransactionId": NotRequired[str],
    },
)

UpdateTableStorageOptimizerRequestRequestTypeDef = TypedDict(
    "UpdateTableStorageOptimizerRequestRequestTypeDef",
    {
        "DatabaseName": str,
        "TableName": str,
        "StorageOptimizerConfig": Mapping[OptimizerTypeType, Mapping[str, str]],
        "CatalogId": NotRequired[str],
    },
)

UpdateTableStorageOptimizerResponseTypeDef = TypedDict(
    "UpdateTableStorageOptimizerResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VirtualObjectTypeDef = TypedDict(
    "VirtualObjectTypeDef",
    {
        "Uri": str,
        "ETag": NotRequired[str],
    },
)

WorkUnitRangeTypeDef = TypedDict(
    "WorkUnitRangeTypeDef",
    {
        "WorkUnitIdMax": int,
        "WorkUnitIdMin": int,
        "WorkUnitToken": str,
    },
)

WriteOperationTypeDef = TypedDict(
    "WriteOperationTypeDef",
    {
        "AddObject": NotRequired["AddObjectInputTypeDef"],
        "DeleteObject": NotRequired["DeleteObjectInputTypeDef"],
    },
)
