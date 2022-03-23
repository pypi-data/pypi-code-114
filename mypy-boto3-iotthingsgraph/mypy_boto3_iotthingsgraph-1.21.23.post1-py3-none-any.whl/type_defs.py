"""
Type annotations for iotthingsgraph service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import AssociateEntityToThingRequestRequestTypeDef

    data: AssociateEntityToThingRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    DeploymentTargetType,
    EntityFilterNameType,
    EntityTypeType,
    FlowExecutionEventTypeType,
    FlowExecutionStatusType,
    NamespaceDeletionStatusType,
    SystemInstanceDeploymentStatusType,
    SystemInstanceFilterNameType,
    UploadStatusType,
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
    "AssociateEntityToThingRequestRequestTypeDef",
    "CreateFlowTemplateRequestRequestTypeDef",
    "CreateFlowTemplateResponseTypeDef",
    "CreateSystemInstanceRequestRequestTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "CreateSystemTemplateRequestRequestTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "DefinitionDocumentTypeDef",
    "DeleteFlowTemplateRequestRequestTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeleteSystemInstanceRequestRequestTypeDef",
    "DeleteSystemTemplateRequestRequestTypeDef",
    "DependencyRevisionTypeDef",
    "DeploySystemInstanceRequestRequestTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "DeprecateFlowTemplateRequestRequestTypeDef",
    "DeprecateSystemTemplateRequestRequestTypeDef",
    "DescribeNamespaceRequestRequestTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "DissociateEntityFromThingRequestRequestTypeDef",
    "EntityDescriptionTypeDef",
    "EntityFilterTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateFilterTypeDef",
    "FlowTemplateSummaryTypeDef",
    "GetEntitiesRequestRequestTypeDef",
    "GetEntitiesResponseTypeDef",
    "GetFlowTemplateRequestRequestTypeDef",
    "GetFlowTemplateResponseTypeDef",
    "GetFlowTemplateRevisionsRequestRequestTypeDef",
    "GetFlowTemplateRevisionsResponseTypeDef",
    "GetNamespaceDeletionStatusResponseTypeDef",
    "GetSystemInstanceRequestRequestTypeDef",
    "GetSystemInstanceResponseTypeDef",
    "GetSystemTemplateRequestRequestTypeDef",
    "GetSystemTemplateResponseTypeDef",
    "GetSystemTemplateRevisionsRequestRequestTypeDef",
    "GetSystemTemplateRevisionsResponseTypeDef",
    "GetUploadStatusRequestRequestTypeDef",
    "GetUploadStatusResponseTypeDef",
    "ListFlowExecutionMessagesRequestRequestTypeDef",
    "ListFlowExecutionMessagesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SearchEntitiesRequestRequestTypeDef",
    "SearchEntitiesResponseTypeDef",
    "SearchFlowExecutionsRequestRequestTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesRequestRequestTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "SearchSystemInstancesRequestRequestTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "SearchSystemTemplatesRequestRequestTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SearchThingsRequestRequestTypeDef",
    "SearchThingsResponseTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateFilterTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "UndeploySystemInstanceRequestRequestTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateFlowTemplateRequestRequestTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UpdateSystemTemplateRequestRequestTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "UploadEntityDefinitionsRequestRequestTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
)

AssociateEntityToThingRequestRequestTypeDef = TypedDict(
    "AssociateEntityToThingRequestRequestTypeDef",
    {
        "thingName": str,
        "entityId": str,
        "namespaceVersion": NotRequired[int],
    },
)

CreateFlowTemplateRequestRequestTypeDef = TypedDict(
    "CreateFlowTemplateRequestRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
        "compatibleNamespaceVersion": NotRequired[int],
    },
)

CreateFlowTemplateResponseTypeDef = TypedDict(
    "CreateFlowTemplateResponseTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSystemInstanceRequestRequestTypeDef = TypedDict(
    "CreateSystemInstanceRequestRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
        "target": DeploymentTargetType,
        "tags": NotRequired[Sequence["TagTypeDef"]],
        "greengrassGroupName": NotRequired[str],
        "s3BucketName": NotRequired[str],
        "metricsConfiguration": NotRequired["MetricsConfigurationTypeDef"],
        "flowActionsRoleArn": NotRequired[str],
    },
)

CreateSystemInstanceResponseTypeDef = TypedDict(
    "CreateSystemInstanceResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSystemTemplateRequestRequestTypeDef = TypedDict(
    "CreateSystemTemplateRequestRequestTypeDef",
    {
        "definition": "DefinitionDocumentTypeDef",
        "compatibleNamespaceVersion": NotRequired[int],
    },
)

CreateSystemTemplateResponseTypeDef = TypedDict(
    "CreateSystemTemplateResponseTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DefinitionDocumentTypeDef = TypedDict(
    "DefinitionDocumentTypeDef",
    {
        "language": Literal["GRAPHQL"],
        "text": str,
    },
)

DeleteFlowTemplateRequestRequestTypeDef = TypedDict(
    "DeleteFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSystemInstanceRequestRequestTypeDef = TypedDict(
    "DeleteSystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)

DeleteSystemTemplateRequestRequestTypeDef = TypedDict(
    "DeleteSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef",
    {
        "id": NotRequired[str],
        "revisionNumber": NotRequired[int],
    },
)

DeploySystemInstanceRequestRequestTypeDef = TypedDict(
    "DeploySystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)

DeploySystemInstanceResponseTypeDef = TypedDict(
    "DeploySystemInstanceResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "greengrassDeploymentId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeprecateFlowTemplateRequestRequestTypeDef = TypedDict(
    "DeprecateFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DeprecateSystemTemplateRequestRequestTypeDef = TypedDict(
    "DeprecateSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
    },
)

DescribeNamespaceRequestRequestTypeDef = TypedDict(
    "DescribeNamespaceRequestRequestTypeDef",
    {
        "namespaceName": NotRequired[str],
    },
)

DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DissociateEntityFromThingRequestRequestTypeDef = TypedDict(
    "DissociateEntityFromThingRequestRequestTypeDef",
    {
        "thingName": str,
        "entityType": EntityTypeType,
    },
)

EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "type": NotRequired[EntityTypeType],
        "createdAt": NotRequired[datetime],
        "definition": NotRequired["DefinitionDocumentTypeDef"],
    },
)

EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef",
    {
        "name": NotRequired[EntityFilterNameType],
        "value": NotRequired[Sequence[str]],
    },
)

FlowExecutionMessageTypeDef = TypedDict(
    "FlowExecutionMessageTypeDef",
    {
        "messageId": NotRequired[str],
        "eventType": NotRequired[FlowExecutionEventTypeType],
        "timestamp": NotRequired[datetime],
        "payload": NotRequired[str],
    },
)

FlowExecutionSummaryTypeDef = TypedDict(
    "FlowExecutionSummaryTypeDef",
    {
        "flowExecutionId": NotRequired[str],
        "status": NotRequired[FlowExecutionStatusType],
        "systemInstanceId": NotRequired[str],
        "flowTemplateId": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
    },
)

FlowTemplateDescriptionTypeDef = TypedDict(
    "FlowTemplateDescriptionTypeDef",
    {
        "summary": NotRequired["FlowTemplateSummaryTypeDef"],
        "definition": NotRequired["DefinitionDocumentTypeDef"],
        "validatedNamespaceVersion": NotRequired[int],
    },
)

FlowTemplateFilterTypeDef = TypedDict(
    "FlowTemplateFilterTypeDef",
    {
        "name": Literal["DEVICE_MODEL_ID"],
        "value": Sequence[str],
    },
)

FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
    },
)

GetEntitiesRequestRequestTypeDef = TypedDict(
    "GetEntitiesRequestRequestTypeDef",
    {
        "ids": Sequence[str],
        "namespaceVersion": NotRequired[int],
    },
)

GetEntitiesResponseTypeDef = TypedDict(
    "GetEntitiesResponseTypeDef",
    {
        "descriptions": List["EntityDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFlowTemplateRequestRequestTypeDef = TypedDict(
    "GetFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
    },
)

GetFlowTemplateResponseTypeDef = TypedDict(
    "GetFlowTemplateResponseTypeDef",
    {
        "description": "FlowTemplateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFlowTemplateRevisionsRequestRequestTypeDef = TypedDict(
    "GetFlowTemplateRevisionsRequestRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsResponseTypeDef",
    {
        "summaries": List["FlowTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "GetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": NamespaceDeletionStatusType,
        "errorCode": Literal["VALIDATION_FAILED"],
        "errorMessage": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSystemInstanceRequestRequestTypeDef = TypedDict(
    "GetSystemInstanceRequestRequestTypeDef",
    {
        "id": str,
    },
)

GetSystemInstanceResponseTypeDef = TypedDict(
    "GetSystemInstanceResponseTypeDef",
    {
        "description": "SystemInstanceDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSystemTemplateRequestRequestTypeDef = TypedDict(
    "GetSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
        "revisionNumber": NotRequired[int],
    },
)

GetSystemTemplateResponseTypeDef = TypedDict(
    "GetSystemTemplateResponseTypeDef",
    {
        "description": "SystemTemplateDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSystemTemplateRevisionsRequestRequestTypeDef = TypedDict(
    "GetSystemTemplateRevisionsRequestRequestTypeDef",
    {
        "id": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

GetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsResponseTypeDef",
    {
        "summaries": List["SystemTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUploadStatusRequestRequestTypeDef = TypedDict(
    "GetUploadStatusRequestRequestTypeDef",
    {
        "uploadId": str,
    },
)

GetUploadStatusResponseTypeDef = TypedDict(
    "GetUploadStatusResponseTypeDef",
    {
        "uploadId": str,
        "uploadStatus": UploadStatusType,
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
        "createdDate": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowExecutionMessagesRequestRequestTypeDef = TypedDict(
    "ListFlowExecutionMessagesRequestRequestTypeDef",
    {
        "flowExecutionId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesResponseTypeDef",
    {
        "messages": List["FlowExecutionMessageTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": List["TagTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {
        "cloudMetricEnabled": NotRequired[bool],
        "metricRuleRoleArn": NotRequired[str],
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

SearchEntitiesRequestRequestTypeDef = TypedDict(
    "SearchEntitiesRequestRequestTypeDef",
    {
        "entityTypes": Sequence[EntityTypeType],
        "filters": NotRequired[Sequence["EntityFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "namespaceVersion": NotRequired[int],
    },
)

SearchEntitiesResponseTypeDef = TypedDict(
    "SearchEntitiesResponseTypeDef",
    {
        "descriptions": List["EntityDescriptionTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFlowExecutionsRequestRequestTypeDef = TypedDict(
    "SearchFlowExecutionsRequestRequestTypeDef",
    {
        "systemInstanceId": str,
        "flowExecutionId": NotRequired[str],
        "startTime": NotRequired[Union[datetime, str]],
        "endTime": NotRequired[Union[datetime, str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

SearchFlowExecutionsResponseTypeDef = TypedDict(
    "SearchFlowExecutionsResponseTypeDef",
    {
        "summaries": List["FlowExecutionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchFlowTemplatesRequestRequestTypeDef = TypedDict(
    "SearchFlowTemplatesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["FlowTemplateFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

SearchFlowTemplatesResponseTypeDef = TypedDict(
    "SearchFlowTemplatesResponseTypeDef",
    {
        "summaries": List["FlowTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSystemInstancesRequestRequestTypeDef = TypedDict(
    "SearchSystemInstancesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["SystemInstanceFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

SearchSystemInstancesResponseTypeDef = TypedDict(
    "SearchSystemInstancesResponseTypeDef",
    {
        "summaries": List["SystemInstanceSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSystemTemplatesRequestRequestTypeDef = TypedDict(
    "SearchSystemTemplatesRequestRequestTypeDef",
    {
        "filters": NotRequired[Sequence["SystemTemplateFilterTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

SearchSystemTemplatesResponseTypeDef = TypedDict(
    "SearchSystemTemplatesResponseTypeDef",
    {
        "summaries": List["SystemTemplateSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchThingsRequestRequestTypeDef = TypedDict(
    "SearchThingsRequestRequestTypeDef",
    {
        "entityId": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
        "namespaceVersion": NotRequired[int],
    },
)

SearchThingsResponseTypeDef = TypedDict(
    "SearchThingsResponseTypeDef",
    {
        "things": List["ThingTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SystemInstanceDescriptionTypeDef = TypedDict(
    "SystemInstanceDescriptionTypeDef",
    {
        "summary": NotRequired["SystemInstanceSummaryTypeDef"],
        "definition": NotRequired["DefinitionDocumentTypeDef"],
        "s3BucketName": NotRequired[str],
        "metricsConfiguration": NotRequired["MetricsConfigurationTypeDef"],
        "validatedNamespaceVersion": NotRequired[int],
        "validatedDependencyRevisions": NotRequired[List["DependencyRevisionTypeDef"]],
        "flowActionsRoleArn": NotRequired[str],
    },
)

SystemInstanceFilterTypeDef = TypedDict(
    "SystemInstanceFilterTypeDef",
    {
        "name": NotRequired[SystemInstanceFilterNameType],
        "value": NotRequired[Sequence[str]],
    },
)

SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[SystemInstanceDeploymentStatusType],
        "target": NotRequired[DeploymentTargetType],
        "greengrassGroupName": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "updatedAt": NotRequired[datetime],
        "greengrassGroupId": NotRequired[str],
        "greengrassGroupVersionId": NotRequired[str],
    },
)

SystemTemplateDescriptionTypeDef = TypedDict(
    "SystemTemplateDescriptionTypeDef",
    {
        "summary": NotRequired["SystemTemplateSummaryTypeDef"],
        "definition": NotRequired["DefinitionDocumentTypeDef"],
        "validatedNamespaceVersion": NotRequired[int],
    },
)

SystemTemplateFilterTypeDef = TypedDict(
    "SystemTemplateFilterTypeDef",
    {
        "name": Literal["FLOW_TEMPLATE_ID"],
        "value": Sequence[str],
    },
)

SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "revisionNumber": NotRequired[int],
        "createdAt": NotRequired[datetime],
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

ThingTypeDef = TypedDict(
    "ThingTypeDef",
    {
        "thingArn": NotRequired[str],
        "thingName": NotRequired[str],
    },
)

UndeploySystemInstanceRequestRequestTypeDef = TypedDict(
    "UndeploySystemInstanceRequestRequestTypeDef",
    {
        "id": NotRequired[str],
    },
)

UndeploySystemInstanceResponseTypeDef = TypedDict(
    "UndeploySystemInstanceResponseTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateFlowTemplateRequestRequestTypeDef = TypedDict(
    "UpdateFlowTemplateRequestRequestTypeDef",
    {
        "id": str,
        "definition": "DefinitionDocumentTypeDef",
        "compatibleNamespaceVersion": NotRequired[int],
    },
)

UpdateFlowTemplateResponseTypeDef = TypedDict(
    "UpdateFlowTemplateResponseTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSystemTemplateRequestRequestTypeDef = TypedDict(
    "UpdateSystemTemplateRequestRequestTypeDef",
    {
        "id": str,
        "definition": "DefinitionDocumentTypeDef",
        "compatibleNamespaceVersion": NotRequired[int],
    },
)

UpdateSystemTemplateResponseTypeDef = TypedDict(
    "UpdateSystemTemplateResponseTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UploadEntityDefinitionsRequestRequestTypeDef = TypedDict(
    "UploadEntityDefinitionsRequestRequestTypeDef",
    {
        "document": NotRequired["DefinitionDocumentTypeDef"],
        "syncWithPublicNamespace": NotRequired[bool],
        "deprecateExistingEntities": NotRequired[bool],
    },
)

UploadEntityDefinitionsResponseTypeDef = TypedDict(
    "UploadEntityDefinitionsResponseTypeDef",
    {
        "uploadId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
