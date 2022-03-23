"""
Type annotations for mobile service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mobile/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mobile.type_defs import BundleDetailsTypeDef

    data: BundleDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import PlatformType, ProjectStateType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BundleDetailsTypeDef",
    "CreateProjectRequestRequestTypeDef",
    "CreateProjectResultTypeDef",
    "DeleteProjectRequestRequestTypeDef",
    "DeleteProjectResultTypeDef",
    "DescribeBundleRequestRequestTypeDef",
    "DescribeBundleResultTypeDef",
    "DescribeProjectRequestRequestTypeDef",
    "DescribeProjectResultTypeDef",
    "ExportBundleRequestRequestTypeDef",
    "ExportBundleResultTypeDef",
    "ExportProjectRequestRequestTypeDef",
    "ExportProjectResultTypeDef",
    "ListBundlesRequestRequestTypeDef",
    "ListBundlesResultTypeDef",
    "ListProjectsRequestRequestTypeDef",
    "ListProjectsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDetailsTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "ResponseMetadataTypeDef",
    "UpdateProjectRequestRequestTypeDef",
    "UpdateProjectResultTypeDef",
)

BundleDetailsTypeDef = TypedDict(
    "BundleDetailsTypeDef",
    {
        "bundleId": NotRequired[str],
        "title": NotRequired[str],
        "version": NotRequired[str],
        "description": NotRequired[str],
        "iconUrl": NotRequired[str],
        "availablePlatforms": NotRequired[List[PlatformType]],
    },
)

CreateProjectRequestRequestTypeDef = TypedDict(
    "CreateProjectRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "region": NotRequired[str],
        "contents": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "snapshotId": NotRequired[str],
    },
)

CreateProjectResultTypeDef = TypedDict(
    "CreateProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteProjectRequestRequestTypeDef = TypedDict(
    "DeleteProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)

DeleteProjectResultTypeDef = TypedDict(
    "DeleteProjectResultTypeDef",
    {
        "deletedResources": List["ResourceTypeDef"],
        "orphanedResources": List["ResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleRequestRequestTypeDef = TypedDict(
    "DescribeBundleRequestRequestTypeDef",
    {
        "bundleId": str,
    },
)

DescribeBundleResultTypeDef = TypedDict(
    "DescribeBundleResultTypeDef",
    {
        "details": "BundleDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeProjectRequestRequestTypeDef = TypedDict(
    "DescribeProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "syncFromResources": NotRequired[bool],
    },
)

DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportBundleRequestRequestTypeDef = TypedDict(
    "ExportBundleRequestRequestTypeDef",
    {
        "bundleId": str,
        "projectId": NotRequired[str],
        "platform": NotRequired[PlatformType],
    },
)

ExportBundleResultTypeDef = TypedDict(
    "ExportBundleResultTypeDef",
    {
        "downloadUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportProjectRequestRequestTypeDef = TypedDict(
    "ExportProjectRequestRequestTypeDef",
    {
        "projectId": str,
    },
)

ExportProjectResultTypeDef = TypedDict(
    "ExportProjectResultTypeDef",
    {
        "downloadUrl": str,
        "shareUrl": str,
        "snapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBundlesRequestRequestTypeDef = TypedDict(
    "ListBundlesRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBundlesResultTypeDef = TypedDict(
    "ListBundlesResultTypeDef",
    {
        "bundleList": List["BundleDetailsTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProjectsRequestRequestTypeDef = TypedDict(
    "ListProjectsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListProjectsResultTypeDef = TypedDict(
    "ListProjectsResultTypeDef",
    {
        "projects": List["ProjectSummaryTypeDef"],
        "nextToken": str,
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

ProjectDetailsTypeDef = TypedDict(
    "ProjectDetailsTypeDef",
    {
        "name": NotRequired[str],
        "projectId": NotRequired[str],
        "region": NotRequired[str],
        "state": NotRequired[ProjectStateType],
        "createdDate": NotRequired[datetime],
        "lastUpdatedDate": NotRequired[datetime],
        "consoleUrl": NotRequired[str],
        "resources": NotRequired[List["ResourceTypeDef"]],
    },
)

ProjectSummaryTypeDef = TypedDict(
    "ProjectSummaryTypeDef",
    {
        "name": NotRequired[str],
        "projectId": NotRequired[str],
    },
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "type": NotRequired[str],
        "name": NotRequired[str],
        "arn": NotRequired[str],
        "feature": NotRequired[str],
        "attributes": NotRequired[Dict[str, str]],
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

UpdateProjectRequestRequestTypeDef = TypedDict(
    "UpdateProjectRequestRequestTypeDef",
    {
        "projectId": str,
        "contents": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UpdateProjectResultTypeDef = TypedDict(
    "UpdateProjectResultTypeDef",
    {
        "details": "ProjectDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
