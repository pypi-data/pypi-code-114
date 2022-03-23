"""
Type annotations for servicecatalog-appregistry service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_servicecatalog_appregistry/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import ResourceGroupStateType, SyncActionType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AssociateAttributeGroupRequestRequestTypeDef",
    "AssociateAttributeGroupResponseTypeDef",
    "AssociateResourceRequestRequestTypeDef",
    "AssociateResourceResponseTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "CreateApplicationRequestRequestTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateAttributeGroupRequestRequestTypeDef",
    "CreateAttributeGroupResponseTypeDef",
    "DeleteApplicationRequestRequestTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteAttributeGroupRequestRequestTypeDef",
    "DeleteAttributeGroupResponseTypeDef",
    "DisassociateAttributeGroupRequestRequestTypeDef",
    "DisassociateAttributeGroupResponseTypeDef",
    "DisassociateResourceRequestRequestTypeDef",
    "DisassociateResourceResponseTypeDef",
    "GetApplicationRequestRequestTypeDef",
    "GetApplicationResponseTypeDef",
    "GetAssociatedResourceRequestRequestTypeDef",
    "GetAssociatedResourceResponseTypeDef",
    "GetAttributeGroupRequestRequestTypeDef",
    "GetAttributeGroupResponseTypeDef",
    "IntegrationsTypeDef",
    "ListApplicationsRequestRequestTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListAssociatedAttributeGroupsRequestRequestTypeDef",
    "ListAssociatedAttributeGroupsResponseTypeDef",
    "ListAssociatedResourcesRequestRequestTypeDef",
    "ListAssociatedResourcesResponseTypeDef",
    "ListAttributeGroupsRequestRequestTypeDef",
    "ListAttributeGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceGroupTypeDef",
    "ResourceInfoTypeDef",
    "ResourceIntegrationsTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "SyncResourceRequestRequestTypeDef",
    "SyncResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateApplicationRequestRequestTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateAttributeGroupRequestRequestTypeDef",
    "UpdateAttributeGroupResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

AssociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "AssociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

AssociateAttributeGroupResponseTypeDef = TypedDict(
    "AssociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateResourceRequestRequestTypeDef = TypedDict(
    "AssociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

AssociateResourceResponseTypeDef = TypedDict(
    "AssociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
    },
)

AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": NotRequired[str],
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "creationTime": NotRequired[datetime],
        "lastUpdateTime": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)

CreateApplicationRequestRequestTypeDef = TypedDict(
    "CreateApplicationRequestRequestTypeDef",
    {
        "name": str,
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAttributeGroupRequestRequestTypeDef = TypedDict(
    "CreateAttributeGroupRequestRequestTypeDef",
    {
        "name": str,
        "attributes": str,
        "clientToken": str,
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateAttributeGroupResponseTypeDef = TypedDict(
    "CreateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteApplicationRequestRequestTypeDef = TypedDict(
    "DeleteApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)

DeleteApplicationResponseTypeDef = TypedDict(
    "DeleteApplicationResponseTypeDef",
    {
        "application": "ApplicationSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAttributeGroupRequestRequestTypeDef = TypedDict(
    "DeleteAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

DeleteAttributeGroupResponseTypeDef = TypedDict(
    "DeleteAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAttributeGroupRequestRequestTypeDef = TypedDict(
    "DisassociateAttributeGroupRequestRequestTypeDef",
    {
        "application": str,
        "attributeGroup": str,
    },
)

DisassociateAttributeGroupResponseTypeDef = TypedDict(
    "DisassociateAttributeGroupResponseTypeDef",
    {
        "applicationArn": str,
        "attributeGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateResourceRequestRequestTypeDef = TypedDict(
    "DisassociateResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

DisassociateResourceResponseTypeDef = TypedDict(
    "DisassociateResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetApplicationRequestRequestTypeDef = TypedDict(
    "GetApplicationRequestRequestTypeDef",
    {
        "application": str,
    },
)

GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
        "integrations": "IntegrationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAssociatedResourceRequestRequestTypeDef = TypedDict(
    "GetAssociatedResourceRequestRequestTypeDef",
    {
        "application": str,
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

GetAssociatedResourceResponseTypeDef = TypedDict(
    "GetAssociatedResourceResponseTypeDef",
    {
        "resource": "ResourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttributeGroupRequestRequestTypeDef = TypedDict(
    "GetAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
    },
)

GetAttributeGroupResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntegrationsTypeDef = TypedDict(
    "IntegrationsTypeDef",
    {
        "resourceGroup": NotRequired["ResourceGroupTypeDef"],
    },
)

ListApplicationsRequestRequestTypeDef = TypedDict(
    "ListApplicationsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {
        "applications": List["ApplicationSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedAttributeGroupsRequestRequestTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsRequestRequestTypeDef",
    {
        "application": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssociatedAttributeGroupsResponseTypeDef = TypedDict(
    "ListAssociatedAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List[str],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAssociatedResourcesRequestRequestTypeDef = TypedDict(
    "ListAssociatedResourcesRequestRequestTypeDef",
    {
        "application": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAssociatedResourcesResponseTypeDef = TypedDict(
    "ListAssociatedResourcesResponseTypeDef",
    {
        "resources": List["ResourceInfoTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttributeGroupsRequestRequestTypeDef = TypedDict(
    "ListAttributeGroupsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListAttributeGroupsResponseTypeDef = TypedDict(
    "ListAttributeGroupsResponseTypeDef",
    {
        "attributeGroups": List["AttributeGroupSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
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

ResourceGroupTypeDef = TypedDict(
    "ResourceGroupTypeDef",
    {
        "state": NotRequired[ResourceGroupStateType],
        "arn": NotRequired[str],
        "errorMessage": NotRequired[str],
    },
)

ResourceInfoTypeDef = TypedDict(
    "ResourceInfoTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
    },
)

ResourceIntegrationsTypeDef = TypedDict(
    "ResourceIntegrationsTypeDef",
    {
        "resourceGroup": NotRequired["ResourceGroupTypeDef"],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "associationTime": NotRequired[datetime],
        "integrations": NotRequired["ResourceIntegrationsTypeDef"],
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

SyncResourceRequestRequestTypeDef = TypedDict(
    "SyncResourceRequestRequestTypeDef",
    {
        "resourceType": Literal["CFN_STACK"],
        "resource": str,
    },
)

SyncResourceResponseTypeDef = TypedDict(
    "SyncResourceResponseTypeDef",
    {
        "applicationArn": str,
        "resourceArn": str,
        "actionTaken": SyncActionType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

UpdateApplicationRequestRequestTypeDef = TypedDict(
    "UpdateApplicationRequestRequestTypeDef",
    {
        "application": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
    },
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef",
    {
        "application": "ApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAttributeGroupRequestRequestTypeDef = TypedDict(
    "UpdateAttributeGroupRequestRequestTypeDef",
    {
        "attributeGroup": str,
        "name": NotRequired[str],
        "description": NotRequired[str],
        "attributes": NotRequired[str],
    },
)

UpdateAttributeGroupResponseTypeDef = TypedDict(
    "UpdateAttributeGroupResponseTypeDef",
    {
        "attributeGroup": "AttributeGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
