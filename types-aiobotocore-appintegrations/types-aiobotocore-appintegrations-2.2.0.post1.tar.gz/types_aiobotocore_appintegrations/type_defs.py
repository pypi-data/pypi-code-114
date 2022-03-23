"""
Type annotations for appintegrations service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_appintegrations/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_appintegrations.type_defs import CreateDataIntegrationRequestRequestTypeDef

    data: CreateDataIntegrationRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDataIntegrationRequestRequestTypeDef",
    "CreateDataIntegrationResponseTypeDef",
    "CreateEventIntegrationRequestRequestTypeDef",
    "CreateEventIntegrationResponseTypeDef",
    "DataIntegrationAssociationSummaryTypeDef",
    "DataIntegrationSummaryTypeDef",
    "DeleteDataIntegrationRequestRequestTypeDef",
    "DeleteEventIntegrationRequestRequestTypeDef",
    "EventFilterTypeDef",
    "EventIntegrationAssociationTypeDef",
    "EventIntegrationTypeDef",
    "GetDataIntegrationRequestRequestTypeDef",
    "GetDataIntegrationResponseTypeDef",
    "GetEventIntegrationRequestRequestTypeDef",
    "GetEventIntegrationResponseTypeDef",
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    "ListDataIntegrationAssociationsResponseTypeDef",
    "ListDataIntegrationsRequestRequestTypeDef",
    "ListDataIntegrationsResponseTypeDef",
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    "ListEventIntegrationAssociationsResponseTypeDef",
    "ListEventIntegrationsRequestRequestTypeDef",
    "ListEventIntegrationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "ScheduleConfigurationTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDataIntegrationRequestRequestTypeDef",
    "UpdateEventIntegrationRequestRequestTypeDef",
)

CreateDataIntegrationRequestRequestTypeDef = TypedDict(
    "CreateDataIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "KmsKey": NotRequired[str],
        "SourceURI": NotRequired[str],
        "ScheduleConfig": NotRequired["ScheduleConfigurationTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "ClientToken": NotRequired[str],
    },
)

CreateDataIntegrationResponseTypeDef = TypedDict(
    "CreateDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "Tags": Dict[str, str],
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEventIntegrationRequestRequestTypeDef = TypedDict(
    "CreateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "EventFilter": "EventFilterTypeDef",
        "EventBridgeBus": str,
        "Description": NotRequired[str],
        "ClientToken": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateEventIntegrationResponseTypeDef = TypedDict(
    "CreateEventIntegrationResponseTypeDef",
    {
        "EventIntegrationArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DataIntegrationAssociationSummaryTypeDef = TypedDict(
    "DataIntegrationAssociationSummaryTypeDef",
    {
        "DataIntegrationAssociationArn": NotRequired[str],
        "DataIntegrationArn": NotRequired[str],
        "ClientId": NotRequired[str],
    },
)

DataIntegrationSummaryTypeDef = TypedDict(
    "DataIntegrationSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "SourceURI": NotRequired[str],
    },
)

DeleteDataIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteDataIntegrationRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
    },
)

DeleteEventIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

EventFilterTypeDef = TypedDict(
    "EventFilterTypeDef",
    {
        "Source": str,
    },
)

EventIntegrationAssociationTypeDef = TypedDict(
    "EventIntegrationAssociationTypeDef",
    {
        "EventIntegrationAssociationArn": NotRequired[str],
        "EventIntegrationAssociationId": NotRequired[str],
        "EventIntegrationName": NotRequired[str],
        "ClientId": NotRequired[str],
        "EventBridgeRuleName": NotRequired[str],
        "ClientAssociationMetadata": NotRequired[Dict[str, str]],
    },
)

EventIntegrationTypeDef = TypedDict(
    "EventIntegrationTypeDef",
    {
        "EventIntegrationArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "EventFilter": NotRequired["EventFilterTypeDef"],
        "EventBridgeBus": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

GetDataIntegrationRequestRequestTypeDef = TypedDict(
    "GetDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
    },
)

GetDataIntegrationResponseTypeDef = TypedDict(
    "GetDataIntegrationResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "KmsKey": str,
        "SourceURI": str,
        "ScheduleConfiguration": "ScheduleConfigurationTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventIntegrationRequestRequestTypeDef = TypedDict(
    "GetEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetEventIntegrationResponseTypeDef = TypedDict(
    "GetEventIntegrationResponseTypeDef",
    {
        "Name": str,
        "Description": str,
        "EventIntegrationArn": str,
        "EventBridgeBus": str,
        "EventFilter": "EventFilterTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationAssociationsRequestRequestTypeDef",
    {
        "DataIntegrationIdentifier": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListDataIntegrationAssociationsResponseTypeDef",
    {
        "DataIntegrationAssociations": List["DataIntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDataIntegrationsRequestRequestTypeDef = TypedDict(
    "ListDataIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDataIntegrationsResponseTypeDef = TypedDict(
    "ListDataIntegrationsResponseTypeDef",
    {
        "DataIntegrations": List["DataIntegrationSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventIntegrationAssociationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationAssociationsRequestRequestTypeDef",
    {
        "EventIntegrationName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEventIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListEventIntegrationAssociationsResponseTypeDef",
    {
        "EventIntegrationAssociations": List["EventIntegrationAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEventIntegrationsRequestRequestTypeDef = TypedDict(
    "ListEventIntegrationsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListEventIntegrationsResponseTypeDef = TypedDict(
    "ListEventIntegrationsResponseTypeDef",
    {
        "EventIntegrations": List["EventIntegrationTypeDef"],
        "NextToken": str,
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

ScheduleConfigurationTypeDef = TypedDict(
    "ScheduleConfigurationTypeDef",
    {
        "FirstExecutionFrom": NotRequired[str],
        "Object": NotRequired[str],
        "ScheduleExpression": NotRequired[str],
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

UpdateDataIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateDataIntegrationRequestRequestTypeDef",
    {
        "Identifier": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateEventIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateEventIntegrationRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)
