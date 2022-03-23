"""
Type annotations for mgh service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mgh/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import ApplicationStatusType, ResourceAttributeTypeType, StatusType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "AssociateCreatedArtifactRequestRequestTypeDef",
    "AssociateDiscoveredResourceRequestRequestTypeDef",
    "CreateProgressUpdateStreamRequestRequestTypeDef",
    "CreatedArtifactTypeDef",
    "DeleteProgressUpdateStreamRequestRequestTypeDef",
    "DescribeApplicationStateRequestRequestTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskRequestRequestTypeDef",
    "DescribeMigrationTaskResultTypeDef",
    "DisassociateCreatedArtifactRequestRequestTypeDef",
    "DisassociateDiscoveredResourceRequestRequestTypeDef",
    "DiscoveredResourceTypeDef",
    "ImportMigrationTaskRequestRequestTypeDef",
    "ListApplicationStatesRequestRequestTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsRequestRequestTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesRequestRequestTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTasksRequestRequestTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "NotifyApplicationStateRequestRequestTypeDef",
    "NotifyMigrationTaskStateRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "PutResourceAttributesRequestRequestTypeDef",
    "ResourceAttributeTypeDef",
    "ResponseMetadataTypeDef",
    "TaskTypeDef",
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {
        "ApplicationId": NotRequired[str],
        "ApplicationStatus": NotRequired[ApplicationStatusType],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

AssociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "AssociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifact": "CreatedArtifactTypeDef",
        "DryRun": NotRequired[bool],
    },
)

AssociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "AssociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DiscoveredResource": "DiscoveredResourceTypeDef",
        "DryRun": NotRequired[bool],
    },
)

CreateProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "CreateProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
        "DryRun": NotRequired[bool],
    },
)

CreatedArtifactTypeDef = TypedDict(
    "CreatedArtifactTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
    },
)

DeleteProgressUpdateStreamRequestRequestTypeDef = TypedDict(
    "DeleteProgressUpdateStreamRequestRequestTypeDef",
    {
        "ProgressUpdateStreamName": str,
        "DryRun": NotRequired[bool],
    },
)

DescribeApplicationStateRequestRequestTypeDef = TypedDict(
    "DescribeApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
    },
)

DescribeApplicationStateResultTypeDef = TypedDict(
    "DescribeApplicationStateResultTypeDef",
    {
        "ApplicationStatus": ApplicationStatusType,
        "LastUpdatedTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMigrationTaskRequestRequestTypeDef = TypedDict(
    "DescribeMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
    },
)

DescribeMigrationTaskResultTypeDef = TypedDict(
    "DescribeMigrationTaskResultTypeDef",
    {
        "MigrationTask": "MigrationTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCreatedArtifactRequestRequestTypeDef = TypedDict(
    "DisassociateCreatedArtifactRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "CreatedArtifactName": str,
        "DryRun": NotRequired[bool],
    },
)

DisassociateDiscoveredResourceRequestRequestTypeDef = TypedDict(
    "DisassociateDiscoveredResourceRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ConfigurationId": str,
        "DryRun": NotRequired[bool],
    },
)

DiscoveredResourceTypeDef = TypedDict(
    "DiscoveredResourceTypeDef",
    {
        "ConfigurationId": str,
        "Description": NotRequired[str],
    },
)

ImportMigrationTaskRequestRequestTypeDef = TypedDict(
    "ImportMigrationTaskRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "DryRun": NotRequired[bool],
    },
)

ListApplicationStatesRequestRequestTypeDef = TypedDict(
    "ListApplicationStatesRequestRequestTypeDef",
    {
        "ApplicationIds": NotRequired[Sequence[str]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {
        "ApplicationStateList": List["ApplicationStateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCreatedArtifactsRequestRequestTypeDef = TypedDict(
    "ListCreatedArtifactsRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {
        "NextToken": str,
        "CreatedArtifactList": List["CreatedArtifactTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDiscoveredResourcesRequestRequestTypeDef = TypedDict(
    "ListDiscoveredResourcesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {
        "NextToken": str,
        "DiscoveredResourceList": List["DiscoveredResourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMigrationTasksRequestRequestTypeDef = TypedDict(
    "ListMigrationTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "ResourceName": NotRequired[str],
    },
)

ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {
        "NextToken": str,
        "MigrationTaskSummaryList": List["MigrationTaskSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProgressUpdateStreamsRequestRequestTypeDef = TypedDict(
    "ListProgressUpdateStreamsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List["ProgressUpdateStreamSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": NotRequired[str],
        "MigrationTaskName": NotRequired[str],
        "Status": NotRequired[StatusType],
        "ProgressPercent": NotRequired[int],
        "StatusDetail": NotRequired[str],
        "UpdateDateTime": NotRequired[datetime],
    },
)

MigrationTaskTypeDef = TypedDict(
    "MigrationTaskTypeDef",
    {
        "ProgressUpdateStream": NotRequired[str],
        "MigrationTaskName": NotRequired[str],
        "Task": NotRequired["TaskTypeDef"],
        "UpdateDateTime": NotRequired[datetime],
        "ResourceAttributeList": NotRequired[List["ResourceAttributeTypeDef"]],
    },
)

NotifyApplicationStateRequestRequestTypeDef = TypedDict(
    "NotifyApplicationStateRequestRequestTypeDef",
    {
        "ApplicationId": str,
        "Status": ApplicationStatusType,
        "UpdateDateTime": NotRequired[Union[datetime, str]],
        "DryRun": NotRequired[bool],
    },
)

NotifyMigrationTaskStateRequestRequestTypeDef = TypedDict(
    "NotifyMigrationTaskStateRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": "TaskTypeDef",
        "UpdateDateTime": Union[datetime, str],
        "NextUpdateSeconds": int,
        "DryRun": NotRequired[bool],
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

ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef",
    {
        "ProgressUpdateStreamName": NotRequired[str],
    },
)

PutResourceAttributesRequestRequestTypeDef = TypedDict(
    "PutResourceAttributesRequestRequestTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "ResourceAttributeList": Sequence["ResourceAttributeTypeDef"],
        "DryRun": NotRequired[bool],
    },
)

ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef",
    {
        "Type": ResourceAttributeTypeType,
        "Value": str,
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

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "Status": StatusType,
        "StatusDetail": NotRequired[str],
        "ProgressPercent": NotRequired[int],
    },
)
