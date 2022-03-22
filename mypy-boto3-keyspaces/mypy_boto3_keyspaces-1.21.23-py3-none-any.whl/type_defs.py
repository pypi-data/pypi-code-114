"""
Type annotations for keyspaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_keyspaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_keyspaces.type_defs import CapacitySpecificationSummaryTypeDef

    data: CapacitySpecificationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    EncryptionTypeType,
    PointInTimeRecoveryStatusType,
    SortOrderType,
    TableStatusType,
    ThroughputModeType,
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
    "CapacitySpecificationSummaryTypeDef",
    "CapacitySpecificationTypeDef",
    "ClusteringKeyTypeDef",
    "ColumnDefinitionTypeDef",
    "CommentTypeDef",
    "CreateKeyspaceRequestRequestTypeDef",
    "CreateKeyspaceResponseTypeDef",
    "CreateTableRequestRequestTypeDef",
    "CreateTableResponseTypeDef",
    "DeleteKeyspaceRequestRequestTypeDef",
    "DeleteTableRequestRequestTypeDef",
    "EncryptionSpecificationTypeDef",
    "GetKeyspaceRequestRequestTypeDef",
    "GetKeyspaceResponseTypeDef",
    "GetTableRequestRequestTypeDef",
    "GetTableResponseTypeDef",
    "KeyspaceSummaryTypeDef",
    "ListKeyspacesRequestRequestTypeDef",
    "ListKeyspacesResponseTypeDef",
    "ListTablesRequestRequestTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PartitionKeyTypeDef",
    "PointInTimeRecoverySummaryTypeDef",
    "PointInTimeRecoveryTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreTableRequestRequestTypeDef",
    "RestoreTableResponseTypeDef",
    "SchemaDefinitionTypeDef",
    "StaticColumnTypeDef",
    "TableSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TimeToLiveTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateTableRequestRequestTypeDef",
    "UpdateTableResponseTypeDef",
)

CapacitySpecificationSummaryTypeDef = TypedDict(
    "CapacitySpecificationSummaryTypeDef",
    {
        "throughputMode": ThroughputModeType,
        "readCapacityUnits": NotRequired[int],
        "writeCapacityUnits": NotRequired[int],
        "lastUpdateToPayPerRequestTimestamp": NotRequired[datetime],
    },
)

CapacitySpecificationTypeDef = TypedDict(
    "CapacitySpecificationTypeDef",
    {
        "throughputMode": ThroughputModeType,
        "readCapacityUnits": NotRequired[int],
        "writeCapacityUnits": NotRequired[int],
    },
)

ClusteringKeyTypeDef = TypedDict(
    "ClusteringKeyTypeDef",
    {
        "name": str,
        "orderBy": SortOrderType,
    },
)

ColumnDefinitionTypeDef = TypedDict(
    "ColumnDefinitionTypeDef",
    {
        "name": str,
        "type": str,
    },
)

CommentTypeDef = TypedDict(
    "CommentTypeDef",
    {
        "message": str,
    },
)

CreateKeyspaceRequestRequestTypeDef = TypedDict(
    "CreateKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateKeyspaceResponseTypeDef = TypedDict(
    "CreateKeyspaceResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTableRequestRequestTypeDef = TypedDict(
    "CreateTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "schemaDefinition": "SchemaDefinitionTypeDef",
        "comment": NotRequired["CommentTypeDef"],
        "capacitySpecification": NotRequired["CapacitySpecificationTypeDef"],
        "encryptionSpecification": NotRequired["EncryptionSpecificationTypeDef"],
        "pointInTimeRecovery": NotRequired["PointInTimeRecoveryTypeDef"],
        "ttl": NotRequired["TimeToLiveTypeDef"],
        "defaultTimeToLive": NotRequired[int],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyspaceRequestRequestTypeDef = TypedDict(
    "DeleteKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
    },
)

DeleteTableRequestRequestTypeDef = TypedDict(
    "DeleteTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
    },
)

EncryptionSpecificationTypeDef = TypedDict(
    "EncryptionSpecificationTypeDef",
    {
        "type": EncryptionTypeType,
        "kmsKeyIdentifier": NotRequired[str],
    },
)

GetKeyspaceRequestRequestTypeDef = TypedDict(
    "GetKeyspaceRequestRequestTypeDef",
    {
        "keyspaceName": str,
    },
)

GetKeyspaceResponseTypeDef = TypedDict(
    "GetKeyspaceResponseTypeDef",
    {
        "keyspaceName": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTableRequestRequestTypeDef = TypedDict(
    "GetTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
    },
)

GetTableResponseTypeDef = TypedDict(
    "GetTableResponseTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "resourceArn": str,
        "creationTimestamp": datetime,
        "status": TableStatusType,
        "schemaDefinition": "SchemaDefinitionTypeDef",
        "capacitySpecification": "CapacitySpecificationSummaryTypeDef",
        "encryptionSpecification": "EncryptionSpecificationTypeDef",
        "pointInTimeRecovery": "PointInTimeRecoverySummaryTypeDef",
        "ttl": "TimeToLiveTypeDef",
        "defaultTimeToLive": int,
        "comment": "CommentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KeyspaceSummaryTypeDef = TypedDict(
    "KeyspaceSummaryTypeDef",
    {
        "keyspaceName": str,
        "resourceArn": str,
    },
)

ListKeyspacesRequestRequestTypeDef = TypedDict(
    "ListKeyspacesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListKeyspacesResponseTypeDef = TypedDict(
    "ListKeyspacesResponseTypeDef",
    {
        "nextToken": str,
        "keyspaces": List["KeyspaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTablesRequestRequestTypeDef = TypedDict(
    "ListTablesRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef",
    {
        "nextToken": str,
        "tables": List["TableSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "nextToken": str,
        "tags": List["TagTypeDef"],
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

PartitionKeyTypeDef = TypedDict(
    "PartitionKeyTypeDef",
    {
        "name": str,
    },
)

PointInTimeRecoverySummaryTypeDef = TypedDict(
    "PointInTimeRecoverySummaryTypeDef",
    {
        "status": PointInTimeRecoveryStatusType,
        "earliestRestorableTimestamp": NotRequired[datetime],
    },
)

PointInTimeRecoveryTypeDef = TypedDict(
    "PointInTimeRecoveryTypeDef",
    {
        "status": PointInTimeRecoveryStatusType,
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

RestoreTableRequestRequestTypeDef = TypedDict(
    "RestoreTableRequestRequestTypeDef",
    {
        "sourceKeyspaceName": str,
        "sourceTableName": str,
        "targetKeyspaceName": str,
        "targetTableName": str,
        "restoreTimestamp": NotRequired[Union[datetime, str]],
        "capacitySpecificationOverride": NotRequired["CapacitySpecificationTypeDef"],
        "encryptionSpecificationOverride": NotRequired["EncryptionSpecificationTypeDef"],
        "pointInTimeRecoveryOverride": NotRequired["PointInTimeRecoveryTypeDef"],
        "tagsOverride": NotRequired[Sequence["TagTypeDef"]],
    },
)

RestoreTableResponseTypeDef = TypedDict(
    "RestoreTableResponseTypeDef",
    {
        "restoredTableARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SchemaDefinitionTypeDef = TypedDict(
    "SchemaDefinitionTypeDef",
    {
        "allColumns": Sequence["ColumnDefinitionTypeDef"],
        "partitionKeys": Sequence["PartitionKeyTypeDef"],
        "clusteringKeys": NotRequired[Sequence["ClusteringKeyTypeDef"]],
        "staticColumns": NotRequired[Sequence["StaticColumnTypeDef"]],
    },
)

StaticColumnTypeDef = TypedDict(
    "StaticColumnTypeDef",
    {
        "name": str,
    },
)

TableSummaryTypeDef = TypedDict(
    "TableSummaryTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "resourceArn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": str,
        "value": str,
    },
)

TimeToLiveTypeDef = TypedDict(
    "TimeToLiveTypeDef",
    {
        "status": Literal["ENABLED"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

UpdateTableRequestRequestTypeDef = TypedDict(
    "UpdateTableRequestRequestTypeDef",
    {
        "keyspaceName": str,
        "tableName": str,
        "addColumns": NotRequired[Sequence["ColumnDefinitionTypeDef"]],
        "capacitySpecification": NotRequired["CapacitySpecificationTypeDef"],
        "encryptionSpecification": NotRequired["EncryptionSpecificationTypeDef"],
        "pointInTimeRecovery": NotRequired["PointInTimeRecoveryTypeDef"],
        "ttl": NotRequired["TimeToLiveTypeDef"],
        "defaultTimeToLive": NotRequired[int],
    },
)

UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef",
    {
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
