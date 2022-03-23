"""
Type annotations for rds-data service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_rds_data/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_rds_data.type_defs import ArrayValueTypeDef

    data: ArrayValueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import DecimalReturnTypeType, TypeHintType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayValueTypeDef",
    "BatchExecuteStatementRequestRequestTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "BeginTransactionRequestRequestTypeDef",
    "BeginTransactionResponseTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionRequestRequestTypeDef",
    "CommitTransactionResponseTypeDef",
    "ExecuteSqlRequestRequestTypeDef",
    "ExecuteSqlResponseTypeDef",
    "ExecuteStatementRequestRequestTypeDef",
    "ExecuteStatementResponseTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "ResponseMetadataTypeDef",
    "ResultFrameTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionRequestRequestTypeDef",
    "RollbackTransactionResponseTypeDef",
    "SqlParameterTypeDef",
    "SqlStatementResultTypeDef",
    "StructValueTypeDef",
    "UpdateResultTypeDef",
    "ValueTypeDef",
)

ArrayValueTypeDef = TypedDict(
    "ArrayValueTypeDef",
    {
        "arrayValues": NotRequired[Sequence[Dict[str, Any]]],
        "booleanValues": NotRequired[Sequence[bool]],
        "doubleValues": NotRequired[Sequence[float]],
        "longValues": NotRequired[Sequence[int]],
        "stringValues": NotRequired[Sequence[str]],
    },
)

BatchExecuteStatementRequestRequestTypeDef = TypedDict(
    "BatchExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "database": NotRequired[str],
        "parameterSets": NotRequired[Sequence[Sequence["SqlParameterTypeDef"]]],
        "schema": NotRequired[str],
        "transactionId": NotRequired[str],
    },
)

BatchExecuteStatementResponseTypeDef = TypedDict(
    "BatchExecuteStatementResponseTypeDef",
    {
        "updateResults": List["UpdateResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BeginTransactionRequestRequestTypeDef = TypedDict(
    "BeginTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)

BeginTransactionResponseTypeDef = TypedDict(
    "BeginTransactionResponseTypeDef",
    {
        "transactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "arrayBaseColumnType": NotRequired[int],
        "isAutoIncrement": NotRequired[bool],
        "isCaseSensitive": NotRequired[bool],
        "isCurrency": NotRequired[bool],
        "isSigned": NotRequired[bool],
        "label": NotRequired[str],
        "name": NotRequired[str],
        "nullable": NotRequired[int],
        "precision": NotRequired[int],
        "scale": NotRequired[int],
        "schemaName": NotRequired[str],
        "tableName": NotRequired[str],
        "type": NotRequired[int],
        "typeName": NotRequired[str],
    },
)

CommitTransactionRequestRequestTypeDef = TypedDict(
    "CommitTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

CommitTransactionResponseTypeDef = TypedDict(
    "CommitTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteSqlRequestRequestTypeDef = TypedDict(
    "ExecuteSqlRequestRequestTypeDef",
    {
        "awsSecretStoreArn": str,
        "dbClusterOrInstanceArn": str,
        "sqlStatements": str,
        "database": NotRequired[str],
        "schema": NotRequired[str],
    },
)

ExecuteSqlResponseTypeDef = TypedDict(
    "ExecuteSqlResponseTypeDef",
    {
        "sqlStatementResults": List["SqlStatementResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteStatementRequestRequestTypeDef = TypedDict(
    "ExecuteStatementRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "sql": str,
        "continueAfterTimeout": NotRequired[bool],
        "database": NotRequired[str],
        "includeResultMetadata": NotRequired[bool],
        "parameters": NotRequired[Sequence["SqlParameterTypeDef"]],
        "resultSetOptions": NotRequired["ResultSetOptionsTypeDef"],
        "schema": NotRequired[str],
        "transactionId": NotRequired[str],
    },
)

ExecuteStatementResponseTypeDef = TypedDict(
    "ExecuteStatementResponseTypeDef",
    {
        "columnMetadata": List["ColumnMetadataTypeDef"],
        "generatedFields": List["FieldTypeDef"],
        "numberOfRecordsUpdated": int,
        "records": List[List["FieldTypeDef"]],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FieldTypeDef = TypedDict(
    "FieldTypeDef",
    {
        "arrayValue": NotRequired["ArrayValueTypeDef"],
        "blobValue": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "isNull": NotRequired[bool],
        "longValue": NotRequired[int],
        "stringValue": NotRequired[str],
    },
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "values": NotRequired[List["ValueTypeDef"]],
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

ResultFrameTypeDef = TypedDict(
    "ResultFrameTypeDef",
    {
        "records": NotRequired[List["RecordTypeDef"]],
        "resultSetMetadata": NotRequired["ResultSetMetadataTypeDef"],
    },
)

ResultSetMetadataTypeDef = TypedDict(
    "ResultSetMetadataTypeDef",
    {
        "columnCount": NotRequired[int],
        "columnMetadata": NotRequired[List["ColumnMetadataTypeDef"]],
    },
)

ResultSetOptionsTypeDef = TypedDict(
    "ResultSetOptionsTypeDef",
    {
        "decimalReturnType": NotRequired[DecimalReturnTypeType],
    },
)

RollbackTransactionRequestRequestTypeDef = TypedDict(
    "RollbackTransactionRequestRequestTypeDef",
    {
        "resourceArn": str,
        "secretArn": str,
        "transactionId": str,
    },
)

RollbackTransactionResponseTypeDef = TypedDict(
    "RollbackTransactionResponseTypeDef",
    {
        "transactionStatus": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SqlParameterTypeDef = TypedDict(
    "SqlParameterTypeDef",
    {
        "name": NotRequired[str],
        "typeHint": NotRequired[TypeHintType],
        "value": NotRequired["FieldTypeDef"],
    },
)

SqlStatementResultTypeDef = TypedDict(
    "SqlStatementResultTypeDef",
    {
        "numberOfRecordsUpdated": NotRequired[int],
        "resultFrame": NotRequired["ResultFrameTypeDef"],
    },
)

StructValueTypeDef = TypedDict(
    "StructValueTypeDef",
    {
        "attributes": NotRequired[List[Dict[str, Any]]],
    },
)

UpdateResultTypeDef = TypedDict(
    "UpdateResultTypeDef",
    {
        "generatedFields": NotRequired[List["FieldTypeDef"]],
    },
)

ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "arrayValues": NotRequired[List[Dict[str, Any]]],
        "bigIntValue": NotRequired[int],
        "bitValue": NotRequired[bool],
        "blobValue": NotRequired[bytes],
        "doubleValue": NotRequired[float],
        "intValue": NotRequired[int],
        "isNull": NotRequired[bool],
        "realValue": NotRequired[float],
        "stringValue": NotRequired[str],
        "structValue": NotRequired[Dict[str, Any]],
    },
)
