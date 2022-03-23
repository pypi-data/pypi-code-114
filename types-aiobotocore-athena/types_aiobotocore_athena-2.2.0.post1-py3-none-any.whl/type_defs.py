"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_athena/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_athena.type_defs import AclConfigurationTypeDef

    data: AclConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ColumnNullableType,
    DataCatalogTypeType,
    EncryptionOptionType,
    QueryExecutionStateType,
    StatementTypeType,
    WorkGroupStateType,
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
    "AclConfigurationTypeDef",
    "AthenaErrorTypeDef",
    "BatchGetNamedQueryInputRequestTypeDef",
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetQueryExecutionInputRequestTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateDataCatalogInputRequestTypeDef",
    "CreateNamedQueryInputRequestTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "CreatePreparedStatementInputRequestTypeDef",
    "CreateWorkGroupInputRequestTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "DeleteDataCatalogInputRequestTypeDef",
    "DeleteNamedQueryInputRequestTypeDef",
    "DeletePreparedStatementInputRequestTypeDef",
    "DeleteWorkGroupInputRequestTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineVersionTypeDef",
    "GetDataCatalogInputRequestTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseInputRequestTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryInputRequestTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetPreparedStatementInputRequestTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionInputRequestTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsInputRequestTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetTableMetadataInputRequestTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupInputRequestTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ListDataCatalogsInputRequestTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesInputRequestTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsInputRequestTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListNamedQueriesInputRequestTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListPreparedStatementsInputRequestTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsInputRequestTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListTableMetadataInputRequestTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsInputRequestTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "ResponseMetadataTypeDef",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "StartQueryExecutionInputRequestTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "StopQueryExecutionInputRequestTypeDef",
    "TableMetadataTypeDef",
    "TagResourceInputRequestTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateDataCatalogInputRequestTypeDef",
    "UpdateNamedQueryInputRequestTypeDef",
    "UpdatePreparedStatementInputRequestTypeDef",
    "UpdateWorkGroupInputRequestTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)

AclConfigurationTypeDef = TypedDict(
    "AclConfigurationTypeDef",
    {
        "S3AclOption": Literal["BUCKET_OWNER_FULL_CONTROL"],
    },
)

AthenaErrorTypeDef = TypedDict(
    "AthenaErrorTypeDef",
    {
        "ErrorCategory": NotRequired[int],
        "ErrorType": NotRequired[int],
    },
)

BatchGetNamedQueryInputRequestTypeDef = TypedDict(
    "BatchGetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryIds": Sequence[str],
    },
)

BatchGetNamedQueryOutputTypeDef = TypedDict(
    "BatchGetNamedQueryOutputTypeDef",
    {
        "NamedQueries": List["NamedQueryTypeDef"],
        "UnprocessedNamedQueryIds": List["UnprocessedNamedQueryIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetQueryExecutionInputRequestTypeDef = TypedDict(
    "BatchGetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionIds": Sequence[str],
    },
)

BatchGetQueryExecutionOutputTypeDef = TypedDict(
    "BatchGetQueryExecutionOutputTypeDef",
    {
        "QueryExecutions": List["QueryExecutionTypeDef"],
        "UnprocessedQueryExecutionIds": List["UnprocessedQueryExecutionIdTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnInfoTypeDef = TypedDict(
    "ColumnInfoTypeDef",
    {
        "Name": str,
        "Type": str,
        "CatalogName": NotRequired[str],
        "SchemaName": NotRequired[str],
        "TableName": NotRequired[str],
        "Label": NotRequired[str],
        "Precision": NotRequired[int],
        "Scale": NotRequired[int],
        "Nullable": NotRequired[ColumnNullableType],
        "CaseSensitive": NotRequired[bool],
    },
)

ColumnTypeDef = TypedDict(
    "ColumnTypeDef",
    {
        "Name": str,
        "Type": NotRequired[str],
        "Comment": NotRequired[str],
    },
)

CreateDataCatalogInputRequestTypeDef = TypedDict(
    "CreateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateNamedQueryInputRequestTypeDef = TypedDict(
    "CreateNamedQueryInputRequestTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "WorkGroup": NotRequired[str],
    },
)

CreateNamedQueryOutputTypeDef = TypedDict(
    "CreateNamedQueryOutputTypeDef",
    {
        "NamedQueryId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePreparedStatementInputRequestTypeDef = TypedDict(
    "CreatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
        "Description": NotRequired[str],
    },
)

CreateWorkGroupInputRequestTypeDef = TypedDict(
    "CreateWorkGroupInputRequestTypeDef",
    {
        "Name": str,
        "Configuration": NotRequired["WorkGroupConfigurationTypeDef"],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef",
    {
        "CatalogName": NotRequired[str],
        "Type": NotRequired[DataCatalogTypeType],
    },
)

DataCatalogTypeDef = TypedDict(
    "DataCatalogTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Dict[str, str]],
    },
)

DatumTypeDef = TypedDict(
    "DatumTypeDef",
    {
        "VarCharValue": NotRequired[str],
    },
)

DeleteDataCatalogInputRequestTypeDef = TypedDict(
    "DeleteDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteNamedQueryInputRequestTypeDef = TypedDict(
    "DeleteNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

DeletePreparedStatementInputRequestTypeDef = TypedDict(
    "DeletePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

DeleteWorkGroupInputRequestTypeDef = TypedDict(
    "DeleteWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
        "RecursiveDeleteOption": NotRequired[bool],
    },
)

EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "EncryptionOption": EncryptionOptionType,
        "KmsKey": NotRequired[str],
    },
)

EngineVersionTypeDef = TypedDict(
    "EngineVersionTypeDef",
    {
        "SelectedEngineVersion": NotRequired[str],
        "EffectiveEngineVersion": NotRequired[str],
    },
)

GetDataCatalogInputRequestTypeDef = TypedDict(
    "GetDataCatalogInputRequestTypeDef",
    {
        "Name": str,
    },
)

GetDataCatalogOutputTypeDef = TypedDict(
    "GetDataCatalogOutputTypeDef",
    {
        "DataCatalog": "DataCatalogTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDatabaseInputRequestTypeDef = TypedDict(
    "GetDatabaseInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
    },
)

GetDatabaseOutputTypeDef = TypedDict(
    "GetDatabaseOutputTypeDef",
    {
        "Database": "DatabaseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamedQueryInputRequestTypeDef = TypedDict(
    "GetNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
    },
)

GetNamedQueryOutputTypeDef = TypedDict(
    "GetNamedQueryOutputTypeDef",
    {
        "NamedQuery": "NamedQueryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPreparedStatementInputRequestTypeDef = TypedDict(
    "GetPreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
    },
)

GetPreparedStatementOutputTypeDef = TypedDict(
    "GetPreparedStatementOutputTypeDef",
    {
        "PreparedStatement": "PreparedStatementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryExecutionInputRequestTypeDef = TypedDict(
    "GetQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

GetQueryExecutionOutputTypeDef = TypedDict(
    "GetQueryExecutionOutputTypeDef",
    {
        "QueryExecution": "QueryExecutionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetQueryResultsInputRequestTypeDef = TypedDict(
    "GetQueryResultsInputRequestTypeDef",
    {
        "QueryExecutionId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

GetQueryResultsOutputTypeDef = TypedDict(
    "GetQueryResultsOutputTypeDef",
    {
        "UpdateCount": int,
        "ResultSet": "ResultSetTypeDef",
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableMetadataInputRequestTypeDef = TypedDict(
    "GetTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "TableName": str,
    },
)

GetTableMetadataOutputTypeDef = TypedDict(
    "GetTableMetadataOutputTypeDef",
    {
        "TableMetadata": "TableMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkGroupInputRequestTypeDef = TypedDict(
    "GetWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
    },
)

GetWorkGroupOutputTypeDef = TypedDict(
    "GetWorkGroupOutputTypeDef",
    {
        "WorkGroup": "WorkGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataCatalogsInputRequestTypeDef = TypedDict(
    "ListDataCatalogsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataCatalogsOutputTypeDef = TypedDict(
    "ListDataCatalogsOutputTypeDef",
    {
        "DataCatalogsSummary": List["DataCatalogSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDatabasesInputRequestTypeDef = TypedDict(
    "ListDatabasesInputRequestTypeDef",
    {
        "CatalogName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDatabasesOutputTypeDef = TypedDict(
    "ListDatabasesOutputTypeDef",
    {
        "DatabaseList": List["DatabaseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEngineVersionsInputRequestTypeDef = TypedDict(
    "ListEngineVersionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEngineVersionsOutputTypeDef = TypedDict(
    "ListEngineVersionsOutputTypeDef",
    {
        "EngineVersions": List["EngineVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNamedQueriesInputRequestTypeDef = TypedDict(
    "ListNamedQueriesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)

ListNamedQueriesOutputTypeDef = TypedDict(
    "ListNamedQueriesOutputTypeDef",
    {
        "NamedQueryIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPreparedStatementsInputRequestTypeDef = TypedDict(
    "ListPreparedStatementsInputRequestTypeDef",
    {
        "WorkGroup": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPreparedStatementsOutputTypeDef = TypedDict(
    "ListPreparedStatementsOutputTypeDef",
    {
        "PreparedStatements": List["PreparedStatementSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueryExecutionsInputRequestTypeDef = TypedDict(
    "ListQueryExecutionsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WorkGroup": NotRequired[str],
    },
)

ListQueryExecutionsOutputTypeDef = TypedDict(
    "ListQueryExecutionsOutputTypeDef",
    {
        "QueryExecutionIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTableMetadataInputRequestTypeDef = TypedDict(
    "ListTableMetadataInputRequestTypeDef",
    {
        "CatalogName": str,
        "DatabaseName": str,
        "Expression": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTableMetadataOutputTypeDef = TypedDict(
    "ListTableMetadataOutputTypeDef",
    {
        "TableMetadataList": List["TableMetadataTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkGroupsInputRequestTypeDef = TypedDict(
    "ListWorkGroupsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWorkGroupsOutputTypeDef = TypedDict(
    "ListWorkGroupsOutputTypeDef",
    {
        "WorkGroups": List["WorkGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NamedQueryTypeDef = TypedDict(
    "NamedQueryTypeDef",
    {
        "Name": str,
        "Database": str,
        "QueryString": str,
        "Description": NotRequired[str],
        "NamedQueryId": NotRequired[str],
        "WorkGroup": NotRequired[str],
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

PreparedStatementSummaryTypeDef = TypedDict(
    "PreparedStatementSummaryTypeDef",
    {
        "StatementName": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)

PreparedStatementTypeDef = TypedDict(
    "PreparedStatementTypeDef",
    {
        "StatementName": NotRequired[str],
        "QueryStatement": NotRequired[str],
        "WorkGroupName": NotRequired[str],
        "Description": NotRequired[str],
        "LastModifiedTime": NotRequired[datetime],
    },
)

QueryExecutionContextTypeDef = TypedDict(
    "QueryExecutionContextTypeDef",
    {
        "Database": NotRequired[str],
        "Catalog": NotRequired[str],
    },
)

QueryExecutionStatisticsTypeDef = TypedDict(
    "QueryExecutionStatisticsTypeDef",
    {
        "EngineExecutionTimeInMillis": NotRequired[int],
        "DataScannedInBytes": NotRequired[int],
        "DataManifestLocation": NotRequired[str],
        "TotalExecutionTimeInMillis": NotRequired[int],
        "QueryQueueTimeInMillis": NotRequired[int],
        "QueryPlanningTimeInMillis": NotRequired[int],
        "ServiceProcessingTimeInMillis": NotRequired[int],
    },
)

QueryExecutionStatusTypeDef = TypedDict(
    "QueryExecutionStatusTypeDef",
    {
        "State": NotRequired[QueryExecutionStateType],
        "StateChangeReason": NotRequired[str],
        "SubmissionDateTime": NotRequired[datetime],
        "CompletionDateTime": NotRequired[datetime],
        "AthenaError": NotRequired["AthenaErrorTypeDef"],
    },
)

QueryExecutionTypeDef = TypedDict(
    "QueryExecutionTypeDef",
    {
        "QueryExecutionId": NotRequired[str],
        "Query": NotRequired[str],
        "StatementType": NotRequired[StatementTypeType],
        "ResultConfiguration": NotRequired["ResultConfigurationTypeDef"],
        "QueryExecutionContext": NotRequired["QueryExecutionContextTypeDef"],
        "Status": NotRequired["QueryExecutionStatusTypeDef"],
        "Statistics": NotRequired["QueryExecutionStatisticsTypeDef"],
        "WorkGroup": NotRequired[str],
        "EngineVersion": NotRequired["EngineVersionTypeDef"],
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

ResultConfigurationTypeDef = TypedDict(
    "ResultConfigurationTypeDef",
    {
        "OutputLocation": NotRequired[str],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "ExpectedBucketOwner": NotRequired[str],
        "AclConfiguration": NotRequired["AclConfigurationTypeDef"],
    },
)

ResultConfigurationUpdatesTypeDef = TypedDict(
    "ResultConfigurationUpdatesTypeDef",
    {
        "OutputLocation": NotRequired[str],
        "RemoveOutputLocation": NotRequired[bool],
        "EncryptionConfiguration": NotRequired["EncryptionConfigurationTypeDef"],
        "RemoveEncryptionConfiguration": NotRequired[bool],
        "ExpectedBucketOwner": NotRequired[str],
        "RemoveExpectedBucketOwner": NotRequired[bool],
        "AclConfiguration": NotRequired["AclConfigurationTypeDef"],
        "RemoveAclConfiguration": NotRequired[bool],
    },
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "ColumnInfo": NotRequired[List["ColumnInfoTypeDef"]],
    },
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "Rows": NotRequired[List["RowTypeDef"]],
        "ResultSetMetadata": NotRequired["ResultSetMetadataTypeDef"],
    },
)

RowTypeDef = TypedDict(
    "RowTypeDef",
    {
        "Data": NotRequired[List["DatumTypeDef"]],
    },
)

StartQueryExecutionInputRequestTypeDef = TypedDict(
    "StartQueryExecutionInputRequestTypeDef",
    {
        "QueryString": str,
        "ClientRequestToken": NotRequired[str],
        "QueryExecutionContext": NotRequired["QueryExecutionContextTypeDef"],
        "ResultConfiguration": NotRequired["ResultConfigurationTypeDef"],
        "WorkGroup": NotRequired[str],
    },
)

StartQueryExecutionOutputTypeDef = TypedDict(
    "StartQueryExecutionOutputTypeDef",
    {
        "QueryExecutionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopQueryExecutionInputRequestTypeDef = TypedDict(
    "StopQueryExecutionInputRequestTypeDef",
    {
        "QueryExecutionId": str,
    },
)

TableMetadataTypeDef = TypedDict(
    "TableMetadataTypeDef",
    {
        "Name": str,
        "CreateTime": NotRequired[datetime],
        "LastAccessTime": NotRequired[datetime],
        "TableType": NotRequired[str],
        "Columns": NotRequired[List["ColumnTypeDef"]],
        "PartitionKeys": NotRequired[List["ColumnTypeDef"]],
        "Parameters": NotRequired[Dict[str, str]],
    },
)

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UnprocessedNamedQueryIdTypeDef = TypedDict(
    "UnprocessedNamedQueryIdTypeDef",
    {
        "NamedQueryId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

UnprocessedQueryExecutionIdTypeDef = TypedDict(
    "UnprocessedQueryExecutionIdTypeDef",
    {
        "QueryExecutionId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDataCatalogInputRequestTypeDef = TypedDict(
    "UpdateDataCatalogInputRequestTypeDef",
    {
        "Name": str,
        "Type": DataCatalogTypeType,
        "Description": NotRequired[str],
        "Parameters": NotRequired[Mapping[str, str]],
    },
)

UpdateNamedQueryInputRequestTypeDef = TypedDict(
    "UpdateNamedQueryInputRequestTypeDef",
    {
        "NamedQueryId": str,
        "Name": str,
        "QueryString": str,
        "Description": NotRequired[str],
    },
)

UpdatePreparedStatementInputRequestTypeDef = TypedDict(
    "UpdatePreparedStatementInputRequestTypeDef",
    {
        "StatementName": str,
        "WorkGroup": str,
        "QueryStatement": str,
        "Description": NotRequired[str],
    },
)

UpdateWorkGroupInputRequestTypeDef = TypedDict(
    "UpdateWorkGroupInputRequestTypeDef",
    {
        "WorkGroup": str,
        "Description": NotRequired[str],
        "ConfigurationUpdates": NotRequired["WorkGroupConfigurationUpdatesTypeDef"],
        "State": NotRequired[WorkGroupStateType],
    },
)

WorkGroupConfigurationTypeDef = TypedDict(
    "WorkGroupConfigurationTypeDef",
    {
        "ResultConfiguration": NotRequired["ResultConfigurationTypeDef"],
        "EnforceWorkGroupConfiguration": NotRequired[bool],
        "PublishCloudWatchMetricsEnabled": NotRequired[bool],
        "BytesScannedCutoffPerQuery": NotRequired[int],
        "RequesterPaysEnabled": NotRequired[bool],
        "EngineVersion": NotRequired["EngineVersionTypeDef"],
    },
)

WorkGroupConfigurationUpdatesTypeDef = TypedDict(
    "WorkGroupConfigurationUpdatesTypeDef",
    {
        "EnforceWorkGroupConfiguration": NotRequired[bool],
        "ResultConfigurationUpdates": NotRequired["ResultConfigurationUpdatesTypeDef"],
        "PublishCloudWatchMetricsEnabled": NotRequired[bool],
        "BytesScannedCutoffPerQuery": NotRequired[int],
        "RemoveBytesScannedCutoffPerQuery": NotRequired[bool],
        "RequesterPaysEnabled": NotRequired[bool],
        "EngineVersion": NotRequired["EngineVersionTypeDef"],
    },
)

WorkGroupSummaryTypeDef = TypedDict(
    "WorkGroupSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "State": NotRequired[WorkGroupStateType],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "EngineVersion": NotRequired["EngineVersionTypeDef"],
    },
)

WorkGroupTypeDef = TypedDict(
    "WorkGroupTypeDef",
    {
        "Name": str,
        "State": NotRequired[WorkGroupStateType],
        "Configuration": NotRequired["WorkGroupConfigurationTypeDef"],
        "Description": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)
