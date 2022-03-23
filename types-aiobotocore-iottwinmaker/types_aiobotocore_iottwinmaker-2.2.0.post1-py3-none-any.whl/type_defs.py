"""
Type annotations for iottwinmaker service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_iottwinmaker/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_iottwinmaker.type_defs import BatchPutPropertyErrorEntryTypeDef

    data: BatchPutPropertyErrorEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    ComponentUpdateTypeType,
    ErrorCodeType,
    OrderByTimeType,
    ParentEntityUpdateTypeType,
    PropertyUpdateTypeType,
    ScopeType,
    StateType,
    TypeType,
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
    "BatchPutPropertyErrorEntryTypeDef",
    "BatchPutPropertyErrorTypeDef",
    "BatchPutPropertyValuesRequestRequestTypeDef",
    "BatchPutPropertyValuesResponseTypeDef",
    "ComponentRequestTypeDef",
    "ComponentResponseTypeDef",
    "ComponentTypeSummaryTypeDef",
    "ComponentUpdateRequestTypeDef",
    "CreateComponentTypeRequestRequestTypeDef",
    "CreateComponentTypeResponseTypeDef",
    "CreateEntityRequestRequestTypeDef",
    "CreateEntityResponseTypeDef",
    "CreateSceneRequestRequestTypeDef",
    "CreateSceneResponseTypeDef",
    "CreateWorkspaceRequestRequestTypeDef",
    "CreateWorkspaceResponseTypeDef",
    "DataConnectorTypeDef",
    "DataTypeTypeDef",
    "DataValueTypeDef",
    "DeleteComponentTypeRequestRequestTypeDef",
    "DeleteComponentTypeResponseTypeDef",
    "DeleteEntityRequestRequestTypeDef",
    "DeleteEntityResponseTypeDef",
    "DeleteSceneRequestRequestTypeDef",
    "DeleteWorkspaceRequestRequestTypeDef",
    "EntityPropertyReferenceTypeDef",
    "EntitySummaryTypeDef",
    "ErrorDetailsTypeDef",
    "FunctionRequestTypeDef",
    "FunctionResponseTypeDef",
    "GetComponentTypeRequestRequestTypeDef",
    "GetComponentTypeResponseTypeDef",
    "GetEntityRequestRequestTypeDef",
    "GetEntityResponseTypeDef",
    "GetPropertyValueHistoryRequestRequestTypeDef",
    "GetPropertyValueHistoryResponseTypeDef",
    "GetPropertyValueRequestRequestTypeDef",
    "GetPropertyValueResponseTypeDef",
    "GetSceneRequestRequestTypeDef",
    "GetSceneResponseTypeDef",
    "GetWorkspaceRequestRequestTypeDef",
    "GetWorkspaceResponseTypeDef",
    "InterpolationParametersTypeDef",
    "LambdaFunctionTypeDef",
    "ListComponentTypesFilterTypeDef",
    "ListComponentTypesRequestRequestTypeDef",
    "ListComponentTypesResponseTypeDef",
    "ListEntitiesFilterTypeDef",
    "ListEntitiesRequestRequestTypeDef",
    "ListEntitiesResponseTypeDef",
    "ListScenesRequestRequestTypeDef",
    "ListScenesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspacesRequestRequestTypeDef",
    "ListWorkspacesResponseTypeDef",
    "ParentEntityUpdateRequestTypeDef",
    "PropertyDefinitionRequestTypeDef",
    "PropertyDefinitionResponseTypeDef",
    "PropertyFilterTypeDef",
    "PropertyLatestValueTypeDef",
    "PropertyRequestTypeDef",
    "PropertyResponseTypeDef",
    "PropertyValueEntryTypeDef",
    "PropertyValueHistoryTypeDef",
    "PropertyValueTypeDef",
    "RelationshipTypeDef",
    "RelationshipValueTypeDef",
    "ResponseMetadataTypeDef",
    "SceneSummaryTypeDef",
    "StatusTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateComponentTypeRequestRequestTypeDef",
    "UpdateComponentTypeResponseTypeDef",
    "UpdateEntityRequestRequestTypeDef",
    "UpdateEntityResponseTypeDef",
    "UpdateSceneRequestRequestTypeDef",
    "UpdateSceneResponseTypeDef",
    "UpdateWorkspaceRequestRequestTypeDef",
    "UpdateWorkspaceResponseTypeDef",
    "WorkspaceSummaryTypeDef",
)

BatchPutPropertyErrorEntryTypeDef = TypedDict(
    "BatchPutPropertyErrorEntryTypeDef",
    {
        "errors": List["BatchPutPropertyErrorTypeDef"],
    },
)

BatchPutPropertyErrorTypeDef = TypedDict(
    "BatchPutPropertyErrorTypeDef",
    {
        "entry": "PropertyValueEntryTypeDef",
        "errorCode": str,
        "errorMessage": str,
    },
)

BatchPutPropertyValuesRequestRequestTypeDef = TypedDict(
    "BatchPutPropertyValuesRequestRequestTypeDef",
    {
        "entries": Sequence["PropertyValueEntryTypeDef"],
        "workspaceId": str,
    },
)

BatchPutPropertyValuesResponseTypeDef = TypedDict(
    "BatchPutPropertyValuesResponseTypeDef",
    {
        "errorEntries": List["BatchPutPropertyErrorEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ComponentRequestTypeDef = TypedDict(
    "ComponentRequestTypeDef",
    {
        "componentTypeId": NotRequired[str],
        "description": NotRequired[str],
        "properties": NotRequired[Mapping[str, "PropertyRequestTypeDef"]],
    },
)

ComponentResponseTypeDef = TypedDict(
    "ComponentResponseTypeDef",
    {
        "componentName": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "definedIn": NotRequired[str],
        "description": NotRequired[str],
        "properties": NotRequired[Dict[str, "PropertyResponseTypeDef"]],
        "status": NotRequired["StatusTypeDef"],
    },
)

ComponentTypeSummaryTypeDef = TypedDict(
    "ComponentTypeSummaryTypeDef",
    {
        "arn": str,
        "componentTypeId": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "description": NotRequired[str],
        "status": NotRequired["StatusTypeDef"],
    },
)

ComponentUpdateRequestTypeDef = TypedDict(
    "ComponentUpdateRequestTypeDef",
    {
        "componentTypeId": NotRequired[str],
        "description": NotRequired[str],
        "propertyUpdates": NotRequired[Mapping[str, "PropertyRequestTypeDef"]],
        "updateType": NotRequired[ComponentUpdateTypeType],
    },
)

CreateComponentTypeRequestRequestTypeDef = TypedDict(
    "CreateComponentTypeRequestRequestTypeDef",
    {
        "componentTypeId": str,
        "workspaceId": str,
        "description": NotRequired[str],
        "extendsFrom": NotRequired[Sequence[str]],
        "functions": NotRequired[Mapping[str, "FunctionRequestTypeDef"]],
        "isSingleton": NotRequired[bool],
        "propertyDefinitions": NotRequired[Mapping[str, "PropertyDefinitionRequestTypeDef"]],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateComponentTypeResponseTypeDef = TypedDict(
    "CreateComponentTypeResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEntityRequestRequestTypeDef = TypedDict(
    "CreateEntityRequestRequestTypeDef",
    {
        "entityName": str,
        "workspaceId": str,
        "components": NotRequired[Mapping[str, "ComponentRequestTypeDef"]],
        "description": NotRequired[str],
        "entityId": NotRequired[str],
        "parentEntityId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateEntityResponseTypeDef = TypedDict(
    "CreateEntityResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "entityId": str,
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSceneRequestRequestTypeDef = TypedDict(
    "CreateSceneRequestRequestTypeDef",
    {
        "contentLocation": str,
        "sceneId": str,
        "workspaceId": str,
        "capabilities": NotRequired[Sequence[str]],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateSceneResponseTypeDef = TypedDict(
    "CreateSceneResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWorkspaceRequestRequestTypeDef = TypedDict(
    "CreateWorkspaceRequestRequestTypeDef",
    {
        "role": str,
        "s3Location": str,
        "workspaceId": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateWorkspaceResponseTypeDef = TypedDict(
    "CreateWorkspaceResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataConnectorTypeDef = TypedDict(
    "DataConnectorTypeDef",
    {
        "isNative": NotRequired[bool],
        "lambda": NotRequired["LambdaFunctionTypeDef"],
    },
)

DataTypeTypeDef = TypedDict(
    "DataTypeTypeDef",
    {
        "type": TypeType,
        "allowedValues": NotRequired[Sequence["DataValueTypeDef"]],
        "nestedType": NotRequired[Dict[str, Any]],
        "relationship": NotRequired["RelationshipTypeDef"],
        "unitOfMeasure": NotRequired[str],
    },
)

DataValueTypeDef = TypedDict(
    "DataValueTypeDef",
    {
        "booleanValue": NotRequired[bool],
        "doubleValue": NotRequired[float],
        "expression": NotRequired[str],
        "integerValue": NotRequired[int],
        "listValue": NotRequired[Sequence[Dict[str, Any]]],
        "longValue": NotRequired[int],
        "mapValue": NotRequired[Mapping[str, Dict[str, Any]]],
        "relationshipValue": NotRequired["RelationshipValueTypeDef"],
        "stringValue": NotRequired[str],
    },
)

DeleteComponentTypeRequestRequestTypeDef = TypedDict(
    "DeleteComponentTypeRequestRequestTypeDef",
    {
        "componentTypeId": str,
        "workspaceId": str,
    },
)

DeleteComponentTypeResponseTypeDef = TypedDict(
    "DeleteComponentTypeResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteEntityRequestRequestTypeDef = TypedDict(
    "DeleteEntityRequestRequestTypeDef",
    {
        "entityId": str,
        "workspaceId": str,
        "isRecursive": NotRequired[bool],
    },
)

DeleteEntityResponseTypeDef = TypedDict(
    "DeleteEntityResponseTypeDef",
    {
        "state": StateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSceneRequestRequestTypeDef = TypedDict(
    "DeleteSceneRequestRequestTypeDef",
    {
        "sceneId": str,
        "workspaceId": str,
    },
)

DeleteWorkspaceRequestRequestTypeDef = TypedDict(
    "DeleteWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

EntityPropertyReferenceTypeDef = TypedDict(
    "EntityPropertyReferenceTypeDef",
    {
        "propertyName": str,
        "componentName": NotRequired[str],
        "entityId": NotRequired[str],
        "externalIdProperty": NotRequired[Mapping[str, str]],
    },
)

EntitySummaryTypeDef = TypedDict(
    "EntitySummaryTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "entityId": str,
        "entityName": str,
        "status": "StatusTypeDef",
        "updateDateTime": datetime,
        "description": NotRequired[str],
        "hasChildEntities": NotRequired[bool],
        "parentEntityId": NotRequired[str],
    },
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "code": NotRequired[ErrorCodeType],
        "message": NotRequired[str],
    },
)

FunctionRequestTypeDef = TypedDict(
    "FunctionRequestTypeDef",
    {
        "implementedBy": NotRequired["DataConnectorTypeDef"],
        "requiredProperties": NotRequired[Sequence[str]],
        "scope": NotRequired[ScopeType],
    },
)

FunctionResponseTypeDef = TypedDict(
    "FunctionResponseTypeDef",
    {
        "implementedBy": NotRequired["DataConnectorTypeDef"],
        "isInherited": NotRequired[bool],
        "requiredProperties": NotRequired[List[str]],
        "scope": NotRequired[ScopeType],
    },
)

GetComponentTypeRequestRequestTypeDef = TypedDict(
    "GetComponentTypeRequestRequestTypeDef",
    {
        "componentTypeId": str,
        "workspaceId": str,
    },
)

GetComponentTypeResponseTypeDef = TypedDict(
    "GetComponentTypeResponseTypeDef",
    {
        "arn": str,
        "componentTypeId": str,
        "creationDateTime": datetime,
        "description": str,
        "extendsFrom": List[str],
        "functions": Dict[str, "FunctionResponseTypeDef"],
        "isAbstract": bool,
        "isSchemaInitialized": bool,
        "isSingleton": bool,
        "propertyDefinitions": Dict[str, "PropertyDefinitionResponseTypeDef"],
        "status": "StatusTypeDef",
        "updateDateTime": datetime,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEntityRequestRequestTypeDef = TypedDict(
    "GetEntityRequestRequestTypeDef",
    {
        "entityId": str,
        "workspaceId": str,
    },
)

GetEntityResponseTypeDef = TypedDict(
    "GetEntityResponseTypeDef",
    {
        "arn": str,
        "components": Dict[str, "ComponentResponseTypeDef"],
        "creationDateTime": datetime,
        "description": str,
        "entityId": str,
        "entityName": str,
        "hasChildEntities": bool,
        "parentEntityId": str,
        "status": "StatusTypeDef",
        "updateDateTime": datetime,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPropertyValueHistoryRequestRequestTypeDef = TypedDict(
    "GetPropertyValueHistoryRequestRequestTypeDef",
    {
        "endDateTime": Union[datetime, str],
        "selectedProperties": Sequence[str],
        "startDateTime": Union[datetime, str],
        "workspaceId": str,
        "componentName": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "entityId": NotRequired[str],
        "interpolation": NotRequired["InterpolationParametersTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "orderByTime": NotRequired[OrderByTimeType],
        "propertyFilters": NotRequired[Sequence["PropertyFilterTypeDef"]],
    },
)

GetPropertyValueHistoryResponseTypeDef = TypedDict(
    "GetPropertyValueHistoryResponseTypeDef",
    {
        "nextToken": str,
        "propertyValues": List["PropertyValueHistoryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPropertyValueRequestRequestTypeDef = TypedDict(
    "GetPropertyValueRequestRequestTypeDef",
    {
        "selectedProperties": Sequence[str],
        "workspaceId": str,
        "componentName": NotRequired[str],
        "componentTypeId": NotRequired[str],
        "entityId": NotRequired[str],
    },
)

GetPropertyValueResponseTypeDef = TypedDict(
    "GetPropertyValueResponseTypeDef",
    {
        "propertyValues": Dict[str, "PropertyLatestValueTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSceneRequestRequestTypeDef = TypedDict(
    "GetSceneRequestRequestTypeDef",
    {
        "sceneId": str,
        "workspaceId": str,
    },
)

GetSceneResponseTypeDef = TypedDict(
    "GetSceneResponseTypeDef",
    {
        "arn": str,
        "capabilities": List[str],
        "contentLocation": str,
        "creationDateTime": datetime,
        "description": str,
        "sceneId": str,
        "updateDateTime": datetime,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWorkspaceRequestRequestTypeDef = TypedDict(
    "GetWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
    },
)

GetWorkspaceResponseTypeDef = TypedDict(
    "GetWorkspaceResponseTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "description": str,
        "role": str,
        "s3Location": str,
        "updateDateTime": datetime,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InterpolationParametersTypeDef = TypedDict(
    "InterpolationParametersTypeDef",
    {
        "interpolationType": NotRequired[Literal["LINEAR"]],
        "intervalInSeconds": NotRequired[int],
    },
)

LambdaFunctionTypeDef = TypedDict(
    "LambdaFunctionTypeDef",
    {
        "arn": str,
    },
)

ListComponentTypesFilterTypeDef = TypedDict(
    "ListComponentTypesFilterTypeDef",
    {
        "extendsFrom": NotRequired[str],
        "isAbstract": NotRequired[bool],
        "namespace": NotRequired[str],
    },
)

ListComponentTypesRequestRequestTypeDef = TypedDict(
    "ListComponentTypesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "filters": NotRequired[Sequence["ListComponentTypesFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListComponentTypesResponseTypeDef = TypedDict(
    "ListComponentTypesResponseTypeDef",
    {
        "componentTypeSummaries": List["ComponentTypeSummaryTypeDef"],
        "maxResults": int,
        "nextToken": str,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEntitiesFilterTypeDef = TypedDict(
    "ListEntitiesFilterTypeDef",
    {
        "componentTypeId": NotRequired[str],
        "parentEntityId": NotRequired[str],
    },
)

ListEntitiesRequestRequestTypeDef = TypedDict(
    "ListEntitiesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "filters": NotRequired[Sequence["ListEntitiesFilterTypeDef"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListEntitiesResponseTypeDef = TypedDict(
    "ListEntitiesResponseTypeDef",
    {
        "entitySummaries": List["EntitySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScenesRequestRequestTypeDef = TypedDict(
    "ListScenesRequestRequestTypeDef",
    {
        "workspaceId": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListScenesResponseTypeDef = TypedDict(
    "ListScenesResponseTypeDef",
    {
        "nextToken": str,
        "sceneSummaries": List["SceneSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "nextToken": str,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWorkspacesRequestRequestTypeDef = TypedDict(
    "ListWorkspacesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListWorkspacesResponseTypeDef = TypedDict(
    "ListWorkspacesResponseTypeDef",
    {
        "nextToken": str,
        "workspaceSummaries": List["WorkspaceSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ParentEntityUpdateRequestTypeDef = TypedDict(
    "ParentEntityUpdateRequestTypeDef",
    {
        "updateType": ParentEntityUpdateTypeType,
        "parentEntityId": NotRequired[str],
    },
)

PropertyDefinitionRequestTypeDef = TypedDict(
    "PropertyDefinitionRequestTypeDef",
    {
        "configuration": NotRequired[Mapping[str, str]],
        "dataType": NotRequired["DataTypeTypeDef"],
        "defaultValue": NotRequired["DataValueTypeDef"],
        "isExternalId": NotRequired[bool],
        "isRequiredInEntity": NotRequired[bool],
        "isStoredExternally": NotRequired[bool],
        "isTimeSeries": NotRequired[bool],
    },
)

PropertyDefinitionResponseTypeDef = TypedDict(
    "PropertyDefinitionResponseTypeDef",
    {
        "dataType": "DataTypeTypeDef",
        "isExternalId": bool,
        "isFinal": bool,
        "isImported": bool,
        "isInherited": bool,
        "isRequiredInEntity": bool,
        "isStoredExternally": bool,
        "isTimeSeries": bool,
        "configuration": NotRequired[Dict[str, str]],
        "defaultValue": NotRequired["DataValueTypeDef"],
    },
)

PropertyFilterTypeDef = TypedDict(
    "PropertyFilterTypeDef",
    {
        "operator": NotRequired[str],
        "propertyName": NotRequired[str],
        "value": NotRequired["DataValueTypeDef"],
    },
)

PropertyLatestValueTypeDef = TypedDict(
    "PropertyLatestValueTypeDef",
    {
        "propertyReference": "EntityPropertyReferenceTypeDef",
        "propertyValue": NotRequired["DataValueTypeDef"],
    },
)

PropertyRequestTypeDef = TypedDict(
    "PropertyRequestTypeDef",
    {
        "definition": NotRequired["PropertyDefinitionRequestTypeDef"],
        "updateType": NotRequired[PropertyUpdateTypeType],
        "value": NotRequired["DataValueTypeDef"],
    },
)

PropertyResponseTypeDef = TypedDict(
    "PropertyResponseTypeDef",
    {
        "definition": NotRequired["PropertyDefinitionResponseTypeDef"],
        "value": NotRequired["DataValueTypeDef"],
    },
)

PropertyValueEntryTypeDef = TypedDict(
    "PropertyValueEntryTypeDef",
    {
        "entityPropertyReference": "EntityPropertyReferenceTypeDef",
        "propertyValues": NotRequired[Sequence["PropertyValueTypeDef"]],
    },
)

PropertyValueHistoryTypeDef = TypedDict(
    "PropertyValueHistoryTypeDef",
    {
        "entityPropertyReference": "EntityPropertyReferenceTypeDef",
        "values": NotRequired[List["PropertyValueTypeDef"]],
    },
)

PropertyValueTypeDef = TypedDict(
    "PropertyValueTypeDef",
    {
        "timestamp": Union[datetime, str],
        "value": "DataValueTypeDef",
    },
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "relationshipType": NotRequired[str],
        "targetComponentTypeId": NotRequired[str],
    },
)

RelationshipValueTypeDef = TypedDict(
    "RelationshipValueTypeDef",
    {
        "targetComponentName": NotRequired[str],
        "targetEntityId": NotRequired[str],
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

SceneSummaryTypeDef = TypedDict(
    "SceneSummaryTypeDef",
    {
        "arn": str,
        "contentLocation": str,
        "creationDateTime": datetime,
        "sceneId": str,
        "updateDateTime": datetime,
        "description": NotRequired[str],
    },
)

StatusTypeDef = TypedDict(
    "StatusTypeDef",
    {
        "error": NotRequired["ErrorDetailsTypeDef"],
        "state": NotRequired[StateType],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceARN": str,
        "tagKeys": Sequence[str],
    },
)

UpdateComponentTypeRequestRequestTypeDef = TypedDict(
    "UpdateComponentTypeRequestRequestTypeDef",
    {
        "componentTypeId": str,
        "workspaceId": str,
        "description": NotRequired[str],
        "extendsFrom": NotRequired[Sequence[str]],
        "functions": NotRequired[Mapping[str, "FunctionRequestTypeDef"]],
        "isSingleton": NotRequired[bool],
        "propertyDefinitions": NotRequired[Mapping[str, "PropertyDefinitionRequestTypeDef"]],
    },
)

UpdateComponentTypeResponseTypeDef = TypedDict(
    "UpdateComponentTypeResponseTypeDef",
    {
        "arn": str,
        "componentTypeId": str,
        "state": StateType,
        "workspaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEntityRequestRequestTypeDef = TypedDict(
    "UpdateEntityRequestRequestTypeDef",
    {
        "entityId": str,
        "workspaceId": str,
        "componentUpdates": NotRequired[Mapping[str, "ComponentUpdateRequestTypeDef"]],
        "description": NotRequired[str],
        "entityName": NotRequired[str],
        "parentEntityUpdate": NotRequired["ParentEntityUpdateRequestTypeDef"],
    },
)

UpdateEntityResponseTypeDef = TypedDict(
    "UpdateEntityResponseTypeDef",
    {
        "state": StateType,
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSceneRequestRequestTypeDef = TypedDict(
    "UpdateSceneRequestRequestTypeDef",
    {
        "sceneId": str,
        "workspaceId": str,
        "capabilities": NotRequired[Sequence[str]],
        "contentLocation": NotRequired[str],
        "description": NotRequired[str],
    },
)

UpdateSceneResponseTypeDef = TypedDict(
    "UpdateSceneResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateWorkspaceRequestRequestTypeDef = TypedDict(
    "UpdateWorkspaceRequestRequestTypeDef",
    {
        "workspaceId": str,
        "description": NotRequired[str],
        "role": NotRequired[str],
    },
)

UpdateWorkspaceResponseTypeDef = TypedDict(
    "UpdateWorkspaceResponseTypeDef",
    {
        "updateDateTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WorkspaceSummaryTypeDef = TypedDict(
    "WorkspaceSummaryTypeDef",
    {
        "arn": str,
        "creationDateTime": datetime,
        "updateDateTime": datetime,
        "workspaceId": str,
        "description": NotRequired[str],
    },
)
