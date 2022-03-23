"""
Type annotations for schemas service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_schemas/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_schemas.type_defs import CreateDiscovererRequestRequestTypeDef

    data: CreateDiscovererRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import CodeGenerationStatusType, DiscovererStateType, TypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDiscovererRequestRequestTypeDef",
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryRequestRequestTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "CreateSchemaResponseTypeDef",
    "DeleteDiscovererRequestRequestTypeDef",
    "DeleteRegistryRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSchemaVersionRequestRequestTypeDef",
    "DescribeCodeBindingRequestRequestTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererRequestRequestTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryRequestRequestTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DiscovererSummaryTypeDef",
    "ExportSchemaRequestRequestTypeDef",
    "ExportSchemaResponseTypeDef",
    "GetCodeBindingSourceRequestRequestTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaRequestRequestTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListDiscoverersRequestRequestTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListRegistriesRequestRequestTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsRequestRequestTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "ListSchemasResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutCodeBindingRequestRequestTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "RegistrySummaryTypeDef",
    "ResponseMetadataTypeDef",
    "SchemaSummaryTypeDef",
    "SchemaVersionSummaryTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasRequestRequestTypeDef",
    "SearchSchemasResponseTypeDef",
    "StartDiscovererRequestRequestTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererRequestRequestTypeDef",
    "StopDiscovererResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDiscovererRequestRequestTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryRequestRequestTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "UpdateSchemaResponseTypeDef",
    "WaiterConfigTypeDef",
)

CreateDiscovererRequestRequestTypeDef = TypedDict(
    "CreateDiscovererRequestRequestTypeDef",
    {
        "SourceArn": str,
        "Description": NotRequired[str],
        "CrossAccount": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateDiscovererResponseTypeDef = TypedDict(
    "CreateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRegistryRequestRequestTypeDef = TypedDict(
    "CreateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Content": str,
        "RegistryName": str,
        "SchemaName": str,
        "Type": TypeType,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDiscovererRequestRequestTypeDef = TypedDict(
    "DeleteDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DeleteRegistryRequestRequestTypeDef = TypedDict(
    "DeleteRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": NotRequired[str],
    },
)

DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)

DeleteSchemaVersionRequestRequestTypeDef = TypedDict(
    "DeleteSchemaVersionRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": str,
    },
)

DescribeCodeBindingRequestRequestTypeDef = TypedDict(
    "DescribeCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)

DescribeCodeBindingResponseTypeDef = TypedDict(
    "DescribeCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDiscovererRequestRequestTypeDef = TypedDict(
    "DescribeDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

DescribeDiscovererResponseTypeDef = TypedDict(
    "DescribeDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistryRequestRequestTypeDef = TypedDict(
    "DescribeRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)

DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSchemaRequestRequestTypeDef = TypedDict(
    "DescribeSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)

DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": NotRequired[str],
        "DiscovererId": NotRequired[str],
        "SourceArn": NotRequired[str],
        "State": NotRequired[DiscovererStateType],
        "CrossAccount": NotRequired[bool],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ExportSchemaRequestRequestTypeDef = TypedDict(
    "ExportSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Type": str,
        "SchemaVersion": NotRequired[str],
    },
)

ExportSchemaResponseTypeDef = TypedDict(
    "ExportSchemaResponseTypeDef",
    {
        "Content": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCodeBindingSourceRequestRequestTypeDef = TypedDict(
    "GetCodeBindingSourceRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)

GetCodeBindingSourceResponseTypeDef = TypedDict(
    "GetCodeBindingSourceResponseTypeDef",
    {
        "Body": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDiscoveredSchemaRequestRequestTypeDef = TypedDict(
    "GetDiscoveredSchemaRequestRequestTypeDef",
    {
        "Events": Sequence[str],
        "Type": TypeType,
    },
)

GetDiscoveredSchemaResponseTypeDef = TypedDict(
    "GetDiscoveredSchemaResponseTypeDef",
    {
        "Content": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": NotRequired[str],
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoverersRequestRequestTypeDef = TypedDict(
    "ListDiscoverersRequestRequestTypeDef",
    {
        "DiscovererIdPrefix": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "SourceArnPrefix": NotRequired[str],
    },
)

ListDiscoverersResponseTypeDef = TypedDict(
    "ListDiscoverersResponseTypeDef",
    {
        "Discoverers": List["DiscovererSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRegistriesRequestRequestTypeDef = TypedDict(
    "ListRegistriesRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "RegistryNamePrefix": NotRequired[str],
        "Scope": NotRequired[str],
    },
)

ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "NextToken": str,
        "Registries": List["RegistrySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemaVersionsRequestRequestTypeDef = TypedDict(
    "ListSchemaVersionsRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "NextToken": str,
        "SchemaVersions": List["SchemaVersionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "SchemaNamePrefix": NotRequired[str],
    },
)

ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SchemaSummaryTypeDef"],
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

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)

PutCodeBindingRequestRequestTypeDef = TypedDict(
    "PutCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)

PutCodeBindingResponseTypeDef = TypedDict(
    "PutCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
        "RegistryName": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)

PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {
        "RegistryArn": NotRequired[str],
        "RegistryName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
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

SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "LastModified": NotRequired[datetime],
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "VersionCount": NotRequired[int],
    },
)

SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

SearchSchemaSummaryTypeDef = TypedDict(
    "SearchSchemaSummaryTypeDef",
    {
        "RegistryName": NotRequired[str],
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaVersions": NotRequired[List["SearchSchemaVersionSummaryTypeDef"]],
    },
)

SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

SearchSchemasRequestRequestTypeDef = TypedDict(
    "SearchSchemasRequestRequestTypeDef",
    {
        "Keywords": str,
        "RegistryName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchSchemasResponseTypeDef = TypedDict(
    "SearchSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List["SearchSchemaSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartDiscovererRequestRequestTypeDef = TypedDict(
    "StartDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StartDiscovererResponseTypeDef = TypedDict(
    "StartDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopDiscovererRequestRequestTypeDef = TypedDict(
    "StopDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)

StopDiscovererResponseTypeDef = TypedDict(
    "StopDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
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

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDiscovererRequestRequestTypeDef = TypedDict(
    "UpdateDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
        "Description": NotRequired[str],
        "CrossAccount": NotRequired[bool],
    },
)

UpdateDiscovererResponseTypeDef = TypedDict(
    "UpdateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRegistryRequestRequestTypeDef = TypedDict(
    "UpdateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
    },
)

UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "ClientTokenId": NotRequired[str],
        "Content": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)

UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
