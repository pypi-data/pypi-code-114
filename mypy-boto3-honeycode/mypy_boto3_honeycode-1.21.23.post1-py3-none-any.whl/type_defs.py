"""
Type annotations for honeycode service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs.html)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsRequestRequestTypeDef

    data: BatchCreateTableRowsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ErrorCodeType,
    FormatType,
    ImportDataCharacterEncodingType,
    TableDataImportJobStatusType,
    UpsertActionType,
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
    "BatchCreateTableRowsRequestRequestTypeDef",
    "BatchCreateTableRowsResultTypeDef",
    "BatchDeleteTableRowsRequestRequestTypeDef",
    "BatchDeleteTableRowsResultTypeDef",
    "BatchUpdateTableRowsRequestRequestTypeDef",
    "BatchUpdateTableRowsResultTypeDef",
    "BatchUpsertTableRowsRequestRequestTypeDef",
    "BatchUpsertTableRowsResultTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "CreateRowDataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobRequestRequestTypeDef",
    "DescribeTableDataImportJobResultTypeDef",
    "DestinationOptionsTypeDef",
    "FailedBatchItemTypeDef",
    "FilterTypeDef",
    "GetScreenDataRequestRequestTypeDef",
    "GetScreenDataResultTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportDataSourceTypeDef",
    "ImportJobSubmitterTypeDef",
    "ImportOptionsTypeDef",
    "InvokeScreenAutomationRequestRequestTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "ListTableColumnsRequestRequestTypeDef",
    "ListTableColumnsResultTypeDef",
    "ListTableRowsRequestRequestTypeDef",
    "ListTableRowsResultTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "QueryTableRowsRequestRequestTypeDef",
    "QueryTableRowsResultTypeDef",
    "ResponseMetadataTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "StartTableDataImportJobRequestRequestTypeDef",
    "StartTableDataImportJobResultTypeDef",
    "TableColumnTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "TableRowTypeDef",
    "TableTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateRowDataTypeDef",
    "UpsertRowDataTypeDef",
    "UpsertRowsResultTypeDef",
    "VariableValueTypeDef",
)

BatchCreateTableRowsRequestRequestTypeDef = TypedDict(
    "BatchCreateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToCreate": Sequence["CreateRowDataTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

BatchCreateTableRowsResultTypeDef = TypedDict(
    "BatchCreateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "createdRows": Dict[str, str],
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteTableRowsRequestRequestTypeDef = TypedDict(
    "BatchDeleteTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowIds": Sequence[str],
        "clientRequestToken": NotRequired[str],
    },
)

BatchDeleteTableRowsResultTypeDef = TypedDict(
    "BatchDeleteTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateTableRowsRequestRequestTypeDef = TypedDict(
    "BatchUpdateTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpdate": Sequence["UpdateRowDataTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

BatchUpdateTableRowsResultTypeDef = TypedDict(
    "BatchUpdateTableRowsResultTypeDef",
    {
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpsertTableRowsRequestRequestTypeDef = TypedDict(
    "BatchUpsertTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowsToUpsert": Sequence["UpsertRowDataTypeDef"],
        "clientRequestToken": NotRequired[str],
    },
)

BatchUpsertTableRowsResultTypeDef = TypedDict(
    "BatchUpsertTableRowsResultTypeDef",
    {
        "rows": Dict[str, "UpsertRowsResultTypeDef"],
        "workbookCursor": int,
        "failedBatchItems": List["FailedBatchItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CellInputTypeDef = TypedDict(
    "CellInputTypeDef",
    {
        "fact": NotRequired[str],
        "facts": NotRequired[Sequence[str]],
    },
)

CellTypeDef = TypedDict(
    "CellTypeDef",
    {
        "formula": NotRequired[str],
        "format": NotRequired[FormatType],
        "rawValue": NotRequired[str],
        "formattedValue": NotRequired[str],
        "formattedValues": NotRequired[List[str]],
    },
)

ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "name": str,
        "format": FormatType,
    },
)

CreateRowDataTypeDef = TypedDict(
    "CreateRowDataTypeDef",
    {
        "batchItemId": str,
        "cellsToCreate": Mapping[str, "CellInputTypeDef"],
    },
)

DataItemTypeDef = TypedDict(
    "DataItemTypeDef",
    {
        "overrideFormat": NotRequired[FormatType],
        "rawValue": NotRequired[str],
        "formattedValue": NotRequired[str],
    },
)

DelimitedTextImportOptionsTypeDef = TypedDict(
    "DelimitedTextImportOptionsTypeDef",
    {
        "delimiter": str,
        "hasHeaderRow": NotRequired[bool],
        "ignoreEmptyRows": NotRequired[bool],
        "dataCharacterEncoding": NotRequired[ImportDataCharacterEncodingType],
    },
)

DescribeTableDataImportJobRequestRequestTypeDef = TypedDict(
    "DescribeTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "jobId": str,
    },
)

DescribeTableDataImportJobResultTypeDef = TypedDict(
    "DescribeTableDataImportJobResultTypeDef",
    {
        "jobStatus": TableDataImportJobStatusType,
        "message": str,
        "jobMetadata": "TableDataImportJobMetadataTypeDef",
        "errorCode": ErrorCodeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationOptionsTypeDef = TypedDict(
    "DestinationOptionsTypeDef",
    {
        "columnMap": NotRequired[Dict[str, "SourceDataColumnPropertiesTypeDef"]],
    },
)

FailedBatchItemTypeDef = TypedDict(
    "FailedBatchItemTypeDef",
    {
        "id": str,
        "errorMessage": str,
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "formula": str,
        "contextRowId": NotRequired[str],
    },
)

GetScreenDataRequestRequestTypeDef = TypedDict(
    "GetScreenDataRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
        "variables": NotRequired[Mapping[str, "VariableValueTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

GetScreenDataResultTypeDef = TypedDict(
    "GetScreenDataResultTypeDef",
    {
        "results": Dict[str, "ResultSetTypeDef"],
        "workbookCursor": int,
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportDataSourceConfigTypeDef = TypedDict(
    "ImportDataSourceConfigTypeDef",
    {
        "dataSourceUrl": NotRequired[str],
    },
)

ImportDataSourceTypeDef = TypedDict(
    "ImportDataSourceTypeDef",
    {
        "dataSourceConfig": "ImportDataSourceConfigTypeDef",
    },
)

ImportJobSubmitterTypeDef = TypedDict(
    "ImportJobSubmitterTypeDef",
    {
        "email": NotRequired[str],
        "userArn": NotRequired[str],
    },
)

ImportOptionsTypeDef = TypedDict(
    "ImportOptionsTypeDef",
    {
        "destinationOptions": NotRequired["DestinationOptionsTypeDef"],
        "delimitedTextOptions": NotRequired["DelimitedTextImportOptionsTypeDef"],
    },
)

InvokeScreenAutomationRequestRequestTypeDef = TypedDict(
    "InvokeScreenAutomationRequestRequestTypeDef",
    {
        "workbookId": str,
        "appId": str,
        "screenId": str,
        "screenAutomationId": str,
        "variables": NotRequired[Mapping[str, "VariableValueTypeDef"]],
        "rowId": NotRequired[str],
        "clientRequestToken": NotRequired[str],
    },
)

InvokeScreenAutomationResultTypeDef = TypedDict(
    "InvokeScreenAutomationResultTypeDef",
    {
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTableColumnsRequestRequestTypeDef = TypedDict(
    "ListTableColumnsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "nextToken": NotRequired[str],
    },
)

ListTableColumnsResultTypeDef = TypedDict(
    "ListTableColumnsResultTypeDef",
    {
        "tableColumns": List["TableColumnTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTableRowsRequestRequestTypeDef = TypedDict(
    "ListTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "rowIds": NotRequired[Sequence[str]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTableRowsResultTypeDef = TypedDict(
    "ListTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "rowIdsNotFound": List[str],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "workbookId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTablesResultTypeDef = TypedDict(
    "ListTablesResultTypeDef",
    {
        "tables": List["TableTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": Dict[str, str],
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

QueryTableRowsRequestRequestTypeDef = TypedDict(
    "QueryTableRowsRequestRequestTypeDef",
    {
        "workbookId": str,
        "tableId": str,
        "filterFormula": "FilterTypeDef",
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

QueryTableRowsResultTypeDef = TypedDict(
    "QueryTableRowsResultTypeDef",
    {
        "columnIds": List[str],
        "rows": List["TableRowTypeDef"],
        "nextToken": str,
        "workbookCursor": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

ResultRowTypeDef = TypedDict(
    "ResultRowTypeDef",
    {
        "dataItems": List["DataItemTypeDef"],
        "rowId": NotRequired[str],
    },
)

ResultSetTypeDef = TypedDict(
    "ResultSetTypeDef",
    {
        "headers": List["ColumnMetadataTypeDef"],
        "rows": List["ResultRowTypeDef"],
    },
)

SourceDataColumnPropertiesTypeDef = TypedDict(
    "SourceDataColumnPropertiesTypeDef",
    {
        "columnIndex": NotRequired[int],
    },
)

StartTableDataImportJobRequestRequestTypeDef = TypedDict(
    "StartTableDataImportJobRequestRequestTypeDef",
    {
        "workbookId": str,
        "dataSource": "ImportDataSourceTypeDef",
        "dataFormat": Literal["DELIMITED_TEXT"],
        "destinationTableId": str,
        "importOptions": "ImportOptionsTypeDef",
        "clientRequestToken": str,
    },
)

StartTableDataImportJobResultTypeDef = TypedDict(
    "StartTableDataImportJobResultTypeDef",
    {
        "jobId": str,
        "jobStatus": TableDataImportJobStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TableColumnTypeDef = TypedDict(
    "TableColumnTypeDef",
    {
        "tableColumnId": NotRequired[str],
        "tableColumnName": NotRequired[str],
        "format": NotRequired[FormatType],
    },
)

TableDataImportJobMetadataTypeDef = TypedDict(
    "TableDataImportJobMetadataTypeDef",
    {
        "submitter": "ImportJobSubmitterTypeDef",
        "submitTime": datetime,
        "importOptions": "ImportOptionsTypeDef",
        "dataSource": "ImportDataSourceTypeDef",
    },
)

TableRowTypeDef = TypedDict(
    "TableRowTypeDef",
    {
        "rowId": str,
        "cells": List["CellTypeDef"],
    },
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "tableId": NotRequired[str],
        "tableName": NotRequired[str],
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

UpdateRowDataTypeDef = TypedDict(
    "UpdateRowDataTypeDef",
    {
        "rowId": str,
        "cellsToUpdate": Mapping[str, "CellInputTypeDef"],
    },
)

UpsertRowDataTypeDef = TypedDict(
    "UpsertRowDataTypeDef",
    {
        "batchItemId": str,
        "filter": "FilterTypeDef",
        "cellsToUpdate": Mapping[str, "CellInputTypeDef"],
    },
)

UpsertRowsResultTypeDef = TypedDict(
    "UpsertRowsResultTypeDef",
    {
        "rowIds": List[str],
        "upsertAction": UpsertActionType,
    },
)

VariableValueTypeDef = TypedDict(
    "VariableValueTypeDef",
    {
        "rawValue": str,
    },
)
