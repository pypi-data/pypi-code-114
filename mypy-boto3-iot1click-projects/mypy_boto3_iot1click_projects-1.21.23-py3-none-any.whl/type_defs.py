"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.type_defs import AssociateDeviceWithPlacementRequestRequestTypeDef

    data: AssociateDeviceWithPlacementRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    "CreatePlacementRequestRequestTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "DeletePlacementRequestRequestTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DescribePlacementRequestRequestTypeDef",
    "DescribePlacementResponseTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResponseTypeDef",
    "DeviceTemplateTypeDef",
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementRequestRequestTypeDef",
    "GetDevicesInPlacementResponseTypeDef",
    "ListPlacementsRequestRequestTypeDef",
    "ListPlacementsResponseTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementDescriptionTypeDef",
    "PlacementSummaryTypeDef",
    "PlacementTemplateTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectSummaryTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePlacementRequestRequestTypeDef",
    "UpdateProjectRequestRequestTypeDef",
)

AssociateDeviceWithPlacementRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceId": str,
        "deviceTemplateName": str,
    },
)

CreatePlacementRequestRequestTypeDef = TypedDict(
    "CreatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired["PlacementTemplateTypeDef"],
        "tags": NotRequired[Mapping[str, str]],
    },
)

DeletePlacementRequestRequestTypeDef = TypedDict(
    "DeletePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribePlacementRequestRequestTypeDef = TypedDict(
    "DescribePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
    },
)

DescribePlacementResponseTypeDef = TypedDict(
    "DescribePlacementResponseTypeDef",
    {
        "placement": "PlacementDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectName": str,
    },
)

DescribeProjectResponseTypeDef = TypedDict(
    "DescribeProjectResponseTypeDef",
    {
        "project": "ProjectDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTemplateTypeDef = TypedDict(
    "DeviceTemplateTypeDef",
    {
        "deviceType": NotRequired[str],
        "callbackOverrides": NotRequired[Mapping[str, str]],
    },
)

DisassociateDeviceFromPlacementRequestRequestTypeDef = TypedDict(
    "DisassociateDeviceFromPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "deviceTemplateName": str,
    },
)

GetDevicesInPlacementRequestRequestTypeDef = TypedDict(
    "GetDevicesInPlacementRequestRequestTypeDef",
    {
        "projectName": str,
        "placementName": str,
    },
)

GetDevicesInPlacementResponseTypeDef = TypedDict(
    "GetDevicesInPlacementResponseTypeDef",
    {
        "devices": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlacementsRequestRequestTypeDef = TypedDict(
    "ListPlacementsRequestRequestTypeDef",
    {
        "projectName": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListPlacementsResponseTypeDef = TypedDict(
    "ListPlacementsResponseTypeDef",
    {
        "placements": List["PlacementSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

ListProjectsResponseTypeDef = TypedDict(
    "ListProjectsResponseTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
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

PlacementDescriptionTypeDef = TypedDict(
    "PlacementDescriptionTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "attributes": Dict[str, str],
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementSummaryTypeDef = TypedDict(
    "PlacementSummaryTypeDef",
    {
        "projectName": str,
        "placementName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
    },
)

PlacementTemplateTypeDef = TypedDict(
    "PlacementTemplateTypeDef",
    {
        "defaultAttributes": NotRequired[Mapping[str, str]],
        "deviceTemplates": NotRequired[Mapping[str, "DeviceTemplateTypeDef"]],
    },
)

ProjectDescriptionTypeDef = TypedDict(
    "ProjectDescriptionTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "placementTemplate": NotRequired["PlacementTemplateTypeDef"],
        "tags": NotRequired[Dict[str, str]],
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "projectName": str,
        "createdDate": datetime,
        "updatedDate": datetime,
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
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

UpdatePlacementRequestRequestTypeDef = TypedDict(
    "UpdatePlacementRequestRequestTypeDef",
    {
        "placementName": str,
        "projectName": str,
        "attributes": NotRequired[Mapping[str, str]],
    },
)

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectName": str,
        "description": NotRequired[str],
        "placementTemplate": NotRequired["PlacementTemplateTypeDef"],
    },
)
