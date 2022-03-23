"""
Type annotations for gamesparks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_gamesparks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_gamesparks.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    DeploymentActionType,
    DeploymentStateType,
    GameStateType,
    GeneratedCodeJobStateType,
    OperationType,
    StageStateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionTypeDef",
    "CreateGameRequestRequestTypeDef",
    "CreateGameResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateStageRequestRequestTypeDef",
    "CreateStageResultTypeDef",
    "DeleteGameRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DisconnectPlayerRequestRequestTypeDef",
    "DisconnectPlayerResultTypeDef",
    "ExportSnapshotRequestRequestTypeDef",
    "ExportSnapshotResultTypeDef",
    "ExtensionDetailsTypeDef",
    "ExtensionVersionDetailsTypeDef",
    "GameConfigurationDetailsTypeDef",
    "GameDetailsTypeDef",
    "GameSummaryTypeDef",
    "GeneratedCodeJobDetailsTypeDef",
    "GeneratorTypeDef",
    "GetExtensionRequestRequestTypeDef",
    "GetExtensionResultTypeDef",
    "GetExtensionVersionRequestRequestTypeDef",
    "GetExtensionVersionResultTypeDef",
    "GetGameConfigurationRequestRequestTypeDef",
    "GetGameConfigurationResultTypeDef",
    "GetGameRequestRequestTypeDef",
    "GetGameResultTypeDef",
    "GetGeneratedCodeJobRequestRequestTypeDef",
    "GetGeneratedCodeJobResultTypeDef",
    "GetPlayerConnectionStatusRequestRequestTypeDef",
    "GetPlayerConnectionStatusResultTypeDef",
    "GetSnapshotRequestRequestTypeDef",
    "GetSnapshotResultTypeDef",
    "GetStageDeploymentRequestRequestTypeDef",
    "GetStageDeploymentResultTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStageResultTypeDef",
    "ImportGameConfigurationRequestRequestTypeDef",
    "ImportGameConfigurationResultTypeDef",
    "ImportGameConfigurationSourceTypeDef",
    "ListExtensionVersionsRequestRequestTypeDef",
    "ListExtensionVersionsResultTypeDef",
    "ListExtensionsRequestRequestTypeDef",
    "ListExtensionsResultTypeDef",
    "ListGamesRequestRequestTypeDef",
    "ListGamesResultTypeDef",
    "ListGeneratedCodeJobsRequestRequestTypeDef",
    "ListGeneratedCodeJobsResultTypeDef",
    "ListSnapshotsRequestRequestTypeDef",
    "ListSnapshotsResultTypeDef",
    "ListStageDeploymentsRequestRequestTypeDef",
    "ListStageDeploymentsResultTypeDef",
    "ListStagesRequestRequestTypeDef",
    "ListStagesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SectionModificationTypeDef",
    "SectionTypeDef",
    "SnapshotDetailsTypeDef",
    "SnapshotSummaryTypeDef",
    "StageDeploymentDetailsTypeDef",
    "StageDeploymentSummaryTypeDef",
    "StageDetailsTypeDef",
    "StageSummaryTypeDef",
    "StartGeneratedCodeJobRequestRequestTypeDef",
    "StartGeneratedCodeJobResultTypeDef",
    "StartStageDeploymentRequestRequestTypeDef",
    "StartStageDeploymentResultTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateGameConfigurationRequestRequestTypeDef",
    "UpdateGameConfigurationResultTypeDef",
    "UpdateGameRequestRequestTypeDef",
    "UpdateGameResultTypeDef",
    "UpdateSnapshotRequestRequestTypeDef",
    "UpdateSnapshotResultTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateStageResultTypeDef",
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "Created": NotRequired[datetime],
        "Id": NotRequired[str],
    },
)

CreateGameRequestRequestTypeDef = TypedDict(
    "CreateGameRequestRequestTypeDef",
    {
        "GameName": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateGameResultTypeDef = TypedDict(
    "CreateGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSnapshotRequestRequestTypeDef = TypedDict(
    "CreateSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "Description": NotRequired[str],
    },
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "GameName": str,
        "Role": str,
        "StageName": str,
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateStageResultTypeDef = TypedDict(
    "CreateStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameRequestRequestTypeDef = TypedDict(
    "DeleteGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)

DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)

DisconnectPlayerRequestRequestTypeDef = TypedDict(
    "DisconnectPlayerRequestRequestTypeDef",
    {
        "GameName": str,
        "PlayerId": str,
        "StageName": str,
    },
)

DisconnectPlayerResultTypeDef = TypedDict(
    "DisconnectPlayerResultTypeDef",
    {
        "DisconnectFailures": List[str],
        "DisconnectSuccesses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportSnapshotRequestRequestTypeDef = TypedDict(
    "ExportSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
    },
)

ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef",
    {
        "S3Url": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExtensionDetailsTypeDef = TypedDict(
    "ExtensionDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "Namespace": NotRequired[str],
    },
)

ExtensionVersionDetailsTypeDef = TypedDict(
    "ExtensionVersionDetailsTypeDef",
    {
        "Name": NotRequired[str],
        "Namespace": NotRequired[str],
        "Schema": NotRequired[str],
        "Version": NotRequired[str],
    },
)

GameConfigurationDetailsTypeDef = TypedDict(
    "GameConfigurationDetailsTypeDef",
    {
        "Created": NotRequired[datetime],
        "LastUpdated": NotRequired[datetime],
        "Sections": NotRequired[Dict[str, "SectionTypeDef"]],
    },
)

GameDetailsTypeDef = TypedDict(
    "GameDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Created": NotRequired[datetime],
        "Description": NotRequired[str],
        "EnableTerminationProtection": NotRequired[bool],
        "LastUpdated": NotRequired[datetime],
        "Name": NotRequired[str],
        "State": NotRequired[GameStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

GameSummaryTypeDef = TypedDict(
    "GameSummaryTypeDef",
    {
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[GameStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

GeneratedCodeJobDetailsTypeDef = TypedDict(
    "GeneratedCodeJobDetailsTypeDef",
    {
        "Description": NotRequired[str],
        "ExpirationTime": NotRequired[datetime],
        "GeneratedCodeJobId": NotRequired[str],
        "S3Url": NotRequired[str],
        "Status": NotRequired[GeneratedCodeJobStateType],
    },
)

GeneratorTypeDef = TypedDict(
    "GeneratorTypeDef",
    {
        "GameSdkVersion": NotRequired[str],
        "Language": NotRequired[str],
        "TargetPlatform": NotRequired[str],
    },
)

GetExtensionRequestRequestTypeDef = TypedDict(
    "GetExtensionRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
    },
)

GetExtensionResultTypeDef = TypedDict(
    "GetExtensionResultTypeDef",
    {
        "Extension": "ExtensionDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetExtensionVersionRequestRequestTypeDef = TypedDict(
    "GetExtensionVersionRequestRequestTypeDef",
    {
        "ExtensionVersion": str,
        "Name": str,
        "Namespace": str,
    },
)

GetExtensionVersionResultTypeDef = TypedDict(
    "GetExtensionVersionResultTypeDef",
    {
        "ExtensionVersion": "ExtensionVersionDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGameConfigurationRequestRequestTypeDef = TypedDict(
    "GetGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
        "Sections": NotRequired[Sequence[str]],
    },
)

GetGameConfigurationResultTypeDef = TypedDict(
    "GetGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGameRequestRequestTypeDef = TypedDict(
    "GetGameRequestRequestTypeDef",
    {
        "GameName": str,
    },
)

GetGameResultTypeDef = TypedDict(
    "GetGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGeneratedCodeJobRequestRequestTypeDef = TypedDict(
    "GetGeneratedCodeJobRequestRequestTypeDef",
    {
        "GameName": str,
        "JobId": str,
        "SnapshotId": str,
    },
)

GetGeneratedCodeJobResultTypeDef = TypedDict(
    "GetGeneratedCodeJobResultTypeDef",
    {
        "GeneratedCodeJob": "GeneratedCodeJobDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlayerConnectionStatusRequestRequestTypeDef = TypedDict(
    "GetPlayerConnectionStatusRequestRequestTypeDef",
    {
        "GameName": str,
        "PlayerId": str,
        "StageName": str,
    },
)

GetPlayerConnectionStatusResultTypeDef = TypedDict(
    "GetPlayerConnectionStatusResultTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotRequestRequestTypeDef = TypedDict(
    "GetSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
        "Sections": NotRequired[Sequence[str]],
    },
)

GetSnapshotResultTypeDef = TypedDict(
    "GetSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageDeploymentRequestRequestTypeDef = TypedDict(
    "GetStageDeploymentRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
        "DeploymentId": NotRequired[str],
    },
)

GetStageDeploymentResultTypeDef = TypedDict(
    "GetStageDeploymentResultTypeDef",
    {
        "StageDeployment": "StageDeploymentDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
    },
)

GetStageResultTypeDef = TypedDict(
    "GetStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportGameConfigurationRequestRequestTypeDef = TypedDict(
    "ImportGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
        "ImportSource": "ImportGameConfigurationSourceTypeDef",
    },
)

ImportGameConfigurationResultTypeDef = TypedDict(
    "ImportGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportGameConfigurationSourceTypeDef = TypedDict(
    "ImportGameConfigurationSourceTypeDef",
    {
        "File": Union[bytes, IO[bytes], StreamingBody],
    },
)

ListExtensionVersionsRequestRequestTypeDef = TypedDict(
    "ListExtensionVersionsRequestRequestTypeDef",
    {
        "Name": str,
        "Namespace": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListExtensionVersionsResultTypeDef = TypedDict(
    "ListExtensionVersionsResultTypeDef",
    {
        "ExtensionVersions": List["ExtensionVersionDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListExtensionsRequestRequestTypeDef = TypedDict(
    "ListExtensionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListExtensionsResultTypeDef = TypedDict(
    "ListExtensionsResultTypeDef",
    {
        "Extensions": List["ExtensionDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGamesRequestRequestTypeDef = TypedDict(
    "ListGamesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGamesResultTypeDef = TypedDict(
    "ListGamesResultTypeDef",
    {
        "Games": List["GameSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGeneratedCodeJobsRequestRequestTypeDef = TypedDict(
    "ListGeneratedCodeJobsRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGeneratedCodeJobsResultTypeDef = TypedDict(
    "ListGeneratedCodeJobsResultTypeDef",
    {
        "GeneratedCodeJobs": List["GeneratedCodeJobDetailsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSnapshotsRequestRequestTypeDef = TypedDict(
    "ListSnapshotsRequestRequestTypeDef",
    {
        "GameName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSnapshotsResultTypeDef = TypedDict(
    "ListSnapshotsResultTypeDef",
    {
        "NextToken": str,
        "Snapshots": List["SnapshotSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStageDeploymentsRequestRequestTypeDef = TypedDict(
    "ListStageDeploymentsRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListStageDeploymentsResultTypeDef = TypedDict(
    "ListStageDeploymentsResultTypeDef",
    {
        "NextToken": str,
        "StageDeployments": List["StageDeploymentSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStagesRequestRequestTypeDef = TypedDict(
    "ListStagesRequestRequestTypeDef",
    {
        "GameName": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListStagesResultTypeDef = TypedDict(
    "ListStagesResultTypeDef",
    {
        "NextToken": str,
        "Stages": List["StageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
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

SectionModificationTypeDef = TypedDict(
    "SectionModificationTypeDef",
    {
        "Operation": OperationType,
        "Path": str,
        "Section": str,
        "Value": NotRequired[Mapping[str, Any]],
    },
)

SectionTypeDef = TypedDict(
    "SectionTypeDef",
    {
        "Attributes": NotRequired[Dict[str, Any]],
        "Name": NotRequired[str],
        "Size": NotRequired[int],
    },
)

SnapshotDetailsTypeDef = TypedDict(
    "SnapshotDetailsTypeDef",
    {
        "Created": NotRequired[datetime],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "Sections": NotRequired[Dict[str, "SectionTypeDef"]],
    },
)

SnapshotSummaryTypeDef = TypedDict(
    "SnapshotSummaryTypeDef",
    {
        "Created": NotRequired[datetime],
        "Description": NotRequired[str],
        "Id": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
    },
)

StageDeploymentDetailsTypeDef = TypedDict(
    "StageDeploymentDetailsTypeDef",
    {
        "Created": NotRequired[datetime],
        "DeploymentAction": NotRequired[DeploymentActionType],
        "DeploymentId": NotRequired[str],
        "DeploymentState": NotRequired[DeploymentStateType],
        "LastUpdated": NotRequired[datetime],
        "SnapshotId": NotRequired[str],
    },
)

StageDeploymentSummaryTypeDef = TypedDict(
    "StageDeploymentSummaryTypeDef",
    {
        "DeploymentAction": NotRequired[DeploymentActionType],
        "DeploymentId": NotRequired[str],
        "DeploymentState": NotRequired[DeploymentStateType],
        "LastUpdated": NotRequired[datetime],
        "SnapshotId": NotRequired[str],
    },
)

StageDetailsTypeDef = TypedDict(
    "StageDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Created": NotRequired[datetime],
        "Description": NotRequired[str],
        "GameKey": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "LogGroup": NotRequired[str],
        "Name": NotRequired[str],
        "Role": NotRequired[str],
        "State": NotRequired[StageStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

StageSummaryTypeDef = TypedDict(
    "StageSummaryTypeDef",
    {
        "Description": NotRequired[str],
        "GameKey": NotRequired[str],
        "Name": NotRequired[str],
        "State": NotRequired[StageStateType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

StartGeneratedCodeJobRequestRequestTypeDef = TypedDict(
    "StartGeneratedCodeJobRequestRequestTypeDef",
    {
        "GameName": str,
        "Generator": "GeneratorTypeDef",
        "SnapshotId": str,
    },
)

StartGeneratedCodeJobResultTypeDef = TypedDict(
    "StartGeneratedCodeJobResultTypeDef",
    {
        "GeneratedCodeJobId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartStageDeploymentRequestRequestTypeDef = TypedDict(
    "StartStageDeploymentRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
        "StageName": str,
        "ClientToken": NotRequired[str],
    },
)

StartStageDeploymentResultTypeDef = TypedDict(
    "StartStageDeploymentResultTypeDef",
    {
        "StageDeployment": "StageDeploymentDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateGameConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateGameConfigurationRequestRequestTypeDef",
    {
        "GameName": str,
        "Modifications": Sequence["SectionModificationTypeDef"],
    },
)

UpdateGameConfigurationResultTypeDef = TypedDict(
    "UpdateGameConfigurationResultTypeDef",
    {
        "GameConfiguration": "GameConfigurationDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameRequestRequestTypeDef = TypedDict(
    "UpdateGameRequestRequestTypeDef",
    {
        "GameName": str,
        "Description": NotRequired[str],
    },
)

UpdateGameResultTypeDef = TypedDict(
    "UpdateGameResultTypeDef",
    {
        "Game": "GameDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSnapshotRequestRequestTypeDef = TypedDict(
    "UpdateSnapshotRequestRequestTypeDef",
    {
        "GameName": str,
        "SnapshotId": str,
        "Description": NotRequired[str],
    },
)

UpdateSnapshotResultTypeDef = TypedDict(
    "UpdateSnapshotResultTypeDef",
    {
        "Snapshot": "SnapshotDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateStageRequestRequestTypeDef = TypedDict(
    "UpdateStageRequestRequestTypeDef",
    {
        "GameName": str,
        "StageName": str,
        "Description": NotRequired[str],
        "Role": NotRequired[str],
    },
)

UpdateStageResultTypeDef = TypedDict(
    "UpdateStageResultTypeDef",
    {
        "Stage": "StageDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
