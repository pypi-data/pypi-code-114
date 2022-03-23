"""
Type annotations for gamelift service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_gamelift/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_gamelift.type_defs import AcceptMatchInputRequestTypeDef

    data: AcceptMatchInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    AcceptanceTypeType,
    BackfillModeType,
    BalancingStrategyType,
    BuildStatusType,
    CertificateTypeType,
    ComparisonOperatorTypeType,
    EC2InstanceTypeType,
    EventCodeType,
    FleetStatusType,
    FleetTypeType,
    FlexMatchModeType,
    GameServerGroupDeleteOptionType,
    GameServerGroupInstanceTypeType,
    GameServerGroupStatusType,
    GameServerInstanceStatusType,
    GameServerProtectionPolicyType,
    GameServerUtilizationStatusType,
    GameSessionPlacementStateType,
    GameSessionStatusType,
    InstanceStatusType,
    IpProtocolType,
    MatchmakingConfigurationStatusType,
    MetricNameType,
    OperatingSystemType,
    PlayerSessionCreationPolicyType,
    PlayerSessionStatusType,
    PolicyTypeType,
    PriorityTypeType,
    ProtectionPolicyType,
    RoutingStrategyTypeType,
    ScalingAdjustmentTypeType,
    ScalingStatusTypeType,
    SortOrderType,
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
    "AcceptMatchInputRequestTypeDef",
    "AliasTypeDef",
    "AttributeValueTypeDef",
    "AwsCredentialsTypeDef",
    "BuildTypeDef",
    "CertificateConfigurationTypeDef",
    "ClaimGameServerInputRequestTypeDef",
    "ClaimGameServerOutputTypeDef",
    "CreateAliasInputRequestTypeDef",
    "CreateAliasOutputTypeDef",
    "CreateBuildInputRequestTypeDef",
    "CreateBuildOutputTypeDef",
    "CreateFleetInputRequestTypeDef",
    "CreateFleetLocationsInputRequestTypeDef",
    "CreateFleetLocationsOutputTypeDef",
    "CreateFleetOutputTypeDef",
    "CreateGameServerGroupInputRequestTypeDef",
    "CreateGameServerGroupOutputTypeDef",
    "CreateGameSessionInputRequestTypeDef",
    "CreateGameSessionOutputTypeDef",
    "CreateGameSessionQueueInputRequestTypeDef",
    "CreateGameSessionQueueOutputTypeDef",
    "CreateMatchmakingConfigurationInputRequestTypeDef",
    "CreateMatchmakingConfigurationOutputTypeDef",
    "CreateMatchmakingRuleSetInputRequestTypeDef",
    "CreateMatchmakingRuleSetOutputTypeDef",
    "CreatePlayerSessionInputRequestTypeDef",
    "CreatePlayerSessionOutputTypeDef",
    "CreatePlayerSessionsInputRequestTypeDef",
    "CreatePlayerSessionsOutputTypeDef",
    "CreateScriptInputRequestTypeDef",
    "CreateScriptOutputTypeDef",
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    "DeleteAliasInputRequestTypeDef",
    "DeleteBuildInputRequestTypeDef",
    "DeleteFleetInputRequestTypeDef",
    "DeleteFleetLocationsInputRequestTypeDef",
    "DeleteFleetLocationsOutputTypeDef",
    "DeleteGameServerGroupInputRequestTypeDef",
    "DeleteGameServerGroupOutputTypeDef",
    "DeleteGameSessionQueueInputRequestTypeDef",
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    "DeleteScalingPolicyInputRequestTypeDef",
    "DeleteScriptInputRequestTypeDef",
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    "DeregisterGameServerInputRequestTypeDef",
    "DescribeAliasInputRequestTypeDef",
    "DescribeAliasOutputTypeDef",
    "DescribeBuildInputRequestTypeDef",
    "DescribeBuildOutputTypeDef",
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    "DescribeEC2InstanceLimitsOutputTypeDef",
    "DescribeFleetAttributesInputRequestTypeDef",
    "DescribeFleetAttributesOutputTypeDef",
    "DescribeFleetCapacityInputRequestTypeDef",
    "DescribeFleetCapacityOutputTypeDef",
    "DescribeFleetEventsInputRequestTypeDef",
    "DescribeFleetEventsOutputTypeDef",
    "DescribeFleetLocationAttributesInputRequestTypeDef",
    "DescribeFleetLocationAttributesOutputTypeDef",
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    "DescribeFleetLocationCapacityOutputTypeDef",
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    "DescribeFleetLocationUtilizationOutputTypeDef",
    "DescribeFleetPortSettingsInputRequestTypeDef",
    "DescribeFleetPortSettingsOutputTypeDef",
    "DescribeFleetUtilizationInputRequestTypeDef",
    "DescribeFleetUtilizationOutputTypeDef",
    "DescribeGameServerGroupInputRequestTypeDef",
    "DescribeGameServerGroupOutputTypeDef",
    "DescribeGameServerInputRequestTypeDef",
    "DescribeGameServerInstancesInputRequestTypeDef",
    "DescribeGameServerInstancesOutputTypeDef",
    "DescribeGameServerOutputTypeDef",
    "DescribeGameSessionDetailsInputRequestTypeDef",
    "DescribeGameSessionDetailsOutputTypeDef",
    "DescribeGameSessionPlacementInputRequestTypeDef",
    "DescribeGameSessionPlacementOutputTypeDef",
    "DescribeGameSessionQueuesInputRequestTypeDef",
    "DescribeGameSessionQueuesOutputTypeDef",
    "DescribeGameSessionsInputRequestTypeDef",
    "DescribeGameSessionsOutputTypeDef",
    "DescribeInstancesInputRequestTypeDef",
    "DescribeInstancesOutputTypeDef",
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    "DescribeMatchmakingInputRequestTypeDef",
    "DescribeMatchmakingOutputTypeDef",
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    "DescribePlayerSessionsInputRequestTypeDef",
    "DescribePlayerSessionsOutputTypeDef",
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    "DescribeRuntimeConfigurationOutputTypeDef",
    "DescribeScalingPoliciesInputRequestTypeDef",
    "DescribeScalingPoliciesOutputTypeDef",
    "DescribeScriptInputRequestTypeDef",
    "DescribeScriptOutputTypeDef",
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    "DesiredPlayerSessionTypeDef",
    "EC2InstanceCountsTypeDef",
    "EC2InstanceLimitTypeDef",
    "EventTypeDef",
    "FilterConfigurationTypeDef",
    "FleetAttributesTypeDef",
    "FleetCapacityTypeDef",
    "FleetUtilizationTypeDef",
    "GamePropertyTypeDef",
    "GameServerGroupAutoScalingPolicyTypeDef",
    "GameServerGroupTypeDef",
    "GameServerInstanceTypeDef",
    "GameServerTypeDef",
    "GameSessionConnectionInfoTypeDef",
    "GameSessionDetailTypeDef",
    "GameSessionPlacementTypeDef",
    "GameSessionQueueDestinationTypeDef",
    "GameSessionQueueTypeDef",
    "GameSessionTypeDef",
    "GetGameSessionLogUrlInputRequestTypeDef",
    "GetGameSessionLogUrlOutputTypeDef",
    "GetInstanceAccessInputRequestTypeDef",
    "GetInstanceAccessOutputTypeDef",
    "InstanceAccessTypeDef",
    "InstanceCredentialsTypeDef",
    "InstanceDefinitionTypeDef",
    "InstanceTypeDef",
    "IpPermissionTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "ListAliasesInputRequestTypeDef",
    "ListAliasesOutputTypeDef",
    "ListBuildsInputRequestTypeDef",
    "ListBuildsOutputTypeDef",
    "ListFleetsInputRequestTypeDef",
    "ListFleetsOutputTypeDef",
    "ListGameServerGroupsInputRequestTypeDef",
    "ListGameServerGroupsOutputTypeDef",
    "ListGameServersInputRequestTypeDef",
    "ListGameServersOutputTypeDef",
    "ListScriptsInputRequestTypeDef",
    "ListScriptsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationAttributesTypeDef",
    "LocationConfigurationTypeDef",
    "LocationStateTypeDef",
    "MatchedPlayerSessionTypeDef",
    "MatchmakingConfigurationTypeDef",
    "MatchmakingRuleSetTypeDef",
    "MatchmakingTicketTypeDef",
    "PaginatorConfigTypeDef",
    "PlacedPlayerSessionTypeDef",
    "PlayerLatencyPolicyTypeDef",
    "PlayerLatencyTypeDef",
    "PlayerSessionTypeDef",
    "PlayerTypeDef",
    "PriorityConfigurationTypeDef",
    "PutScalingPolicyInputRequestTypeDef",
    "PutScalingPolicyOutputTypeDef",
    "RegisterGameServerInputRequestTypeDef",
    "RegisterGameServerOutputTypeDef",
    "RequestUploadCredentialsInputRequestTypeDef",
    "RequestUploadCredentialsOutputTypeDef",
    "ResolveAliasInputRequestTypeDef",
    "ResolveAliasOutputTypeDef",
    "ResourceCreationLimitPolicyTypeDef",
    "ResponseMetadataTypeDef",
    "ResumeGameServerGroupInputRequestTypeDef",
    "ResumeGameServerGroupOutputTypeDef",
    "RoutingStrategyTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3LocationTypeDef",
    "ScalingPolicyTypeDef",
    "ScriptTypeDef",
    "SearchGameSessionsInputRequestTypeDef",
    "SearchGameSessionsOutputTypeDef",
    "ServerProcessTypeDef",
    "StartFleetActionsInputRequestTypeDef",
    "StartFleetActionsOutputTypeDef",
    "StartGameSessionPlacementInputRequestTypeDef",
    "StartGameSessionPlacementOutputTypeDef",
    "StartMatchBackfillInputRequestTypeDef",
    "StartMatchBackfillOutputTypeDef",
    "StartMatchmakingInputRequestTypeDef",
    "StartMatchmakingOutputTypeDef",
    "StopFleetActionsInputRequestTypeDef",
    "StopFleetActionsOutputTypeDef",
    "StopGameSessionPlacementInputRequestTypeDef",
    "StopGameSessionPlacementOutputTypeDef",
    "StopMatchmakingInputRequestTypeDef",
    "SuspendGameServerGroupInputRequestTypeDef",
    "SuspendGameServerGroupOutputTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TargetConfigurationTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAliasInputRequestTypeDef",
    "UpdateAliasOutputTypeDef",
    "UpdateBuildInputRequestTypeDef",
    "UpdateBuildOutputTypeDef",
    "UpdateFleetAttributesInputRequestTypeDef",
    "UpdateFleetAttributesOutputTypeDef",
    "UpdateFleetCapacityInputRequestTypeDef",
    "UpdateFleetCapacityOutputTypeDef",
    "UpdateFleetPortSettingsInputRequestTypeDef",
    "UpdateFleetPortSettingsOutputTypeDef",
    "UpdateGameServerGroupInputRequestTypeDef",
    "UpdateGameServerGroupOutputTypeDef",
    "UpdateGameServerInputRequestTypeDef",
    "UpdateGameServerOutputTypeDef",
    "UpdateGameSessionInputRequestTypeDef",
    "UpdateGameSessionOutputTypeDef",
    "UpdateGameSessionQueueInputRequestTypeDef",
    "UpdateGameSessionQueueOutputTypeDef",
    "UpdateMatchmakingConfigurationInputRequestTypeDef",
    "UpdateMatchmakingConfigurationOutputTypeDef",
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    "UpdateRuntimeConfigurationOutputTypeDef",
    "UpdateScriptInputRequestTypeDef",
    "UpdateScriptOutputTypeDef",
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    "ValidateMatchmakingRuleSetOutputTypeDef",
    "VpcPeeringAuthorizationTypeDef",
    "VpcPeeringConnectionStatusTypeDef",
    "VpcPeeringConnectionTypeDef",
)

AcceptMatchInputRequestTypeDef = TypedDict(
    "AcceptMatchInputRequestTypeDef",
    {
        "TicketId": str,
        "PlayerIds": Sequence[str],
        "AcceptanceType": AcceptanceTypeType,
    },
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "AliasId": NotRequired[str],
        "Name": NotRequired[str],
        "AliasArn": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingStrategy": NotRequired["RoutingStrategyTypeDef"],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "S": NotRequired[str],
        "N": NotRequired[float],
        "SL": NotRequired[List[str]],
        "SDM": NotRequired[Dict[str, float]],
    },
)

AwsCredentialsTypeDef = TypedDict(
    "AwsCredentialsTypeDef",
    {
        "AccessKeyId": NotRequired[str],
        "SecretAccessKey": NotRequired[str],
        "SessionToken": NotRequired[str],
    },
)

BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "BuildId": NotRequired[str],
        "BuildArn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "Status": NotRequired[BuildStatusType],
        "SizeOnDisk": NotRequired[int],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "CreationTime": NotRequired[datetime],
    },
)

CertificateConfigurationTypeDef = TypedDict(
    "CertificateConfigurationTypeDef",
    {
        "CertificateType": CertificateTypeType,
    },
)

ClaimGameServerInputRequestTypeDef = TypedDict(
    "ClaimGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": NotRequired[str],
        "GameServerData": NotRequired[str],
    },
)

ClaimGameServerOutputTypeDef = TypedDict(
    "ClaimGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAliasInputRequestTypeDef = TypedDict(
    "CreateAliasInputRequestTypeDef",
    {
        "Name": str,
        "RoutingStrategy": "RoutingStrategyTypeDef",
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAliasOutputTypeDef = TypedDict(
    "CreateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBuildInputRequestTypeDef = TypedDict(
    "CreateBuildInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired["S3LocationTypeDef"],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateBuildOutputTypeDef = TypedDict(
    "CreateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetInputRequestTypeDef = TypedDict(
    "CreateFleetInputRequestTypeDef",
    {
        "Name": str,
        "EC2InstanceType": EC2InstanceTypeType,
        "Description": NotRequired[str],
        "BuildId": NotRequired[str],
        "ScriptId": NotRequired[str],
        "ServerLaunchPath": NotRequired[str],
        "ServerLaunchParameters": NotRequired[str],
        "LogPaths": NotRequired[Sequence[str]],
        "EC2InboundPermissions": NotRequired[Sequence["IpPermissionTypeDef"]],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "RuntimeConfiguration": NotRequired["RuntimeConfigurationTypeDef"],
        "ResourceCreationLimitPolicy": NotRequired["ResourceCreationLimitPolicyTypeDef"],
        "MetricGroups": NotRequired[Sequence[str]],
        "PeerVpcAwsAccountId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "InstanceRoleArn": NotRequired[str],
        "CertificateConfiguration": NotRequired["CertificateConfigurationTypeDef"],
        "Locations": NotRequired[Sequence["LocationConfigurationTypeDef"]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFleetLocationsInputRequestTypeDef = TypedDict(
    "CreateFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": Sequence["LocationConfigurationTypeDef"],
    },
)

CreateFleetLocationsOutputTypeDef = TypedDict(
    "CreateFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetOutputTypeDef = TypedDict(
    "CreateFleetOutputTypeDef",
    {
        "FleetAttributes": "FleetAttributesTypeDef",
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameServerGroupInputRequestTypeDef = TypedDict(
    "CreateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": str,
        "MinSize": int,
        "MaxSize": int,
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceDefinitions": Sequence["InstanceDefinitionTypeDef"],
        "AutoScalingPolicy": NotRequired["GameServerGroupAutoScalingPolicyTypeDef"],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "VpcSubnets": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGameServerGroupOutputTypeDef = TypedDict(
    "CreateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameSessionInputRequestTypeDef = TypedDict(
    "CreateGameSessionInputRequestTypeDef",
    {
        "MaximumPlayerSessionCount": int,
        "FleetId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Name": NotRequired[str],
        "GameProperties": NotRequired[Sequence["GamePropertyTypeDef"]],
        "CreatorId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "IdempotencyToken": NotRequired[str],
        "GameSessionData": NotRequired[str],
        "Location": NotRequired[str],
    },
)

CreateGameSessionOutputTypeDef = TypedDict(
    "CreateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGameSessionQueueInputRequestTypeDef = TypedDict(
    "CreateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[Sequence["PlayerLatencyPolicyTypeDef"]],
        "Destinations": NotRequired[Sequence["GameSessionQueueDestinationTypeDef"]],
        "FilterConfiguration": NotRequired["FilterConfigurationTypeDef"],
        "PriorityConfiguration": NotRequired["PriorityConfigurationTypeDef"],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGameSessionQueueOutputTypeDef = TypedDict(
    "CreateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "CreateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "RequestTimeoutSeconds": int,
        "AcceptanceRequired": bool,
        "RuleSetName": str,
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[Sequence[str]],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "GameProperties": NotRequired[Sequence["GamePropertyTypeDef"]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "CreateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "CreateMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
        "RuleSetBody": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "CreateMatchmakingRuleSetOutputTypeDef",
    {
        "RuleSet": "MatchmakingRuleSetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlayerSessionInputRequestTypeDef = TypedDict(
    "CreatePlayerSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerId": str,
        "PlayerData": NotRequired[str],
    },
)

CreatePlayerSessionOutputTypeDef = TypedDict(
    "CreatePlayerSessionOutputTypeDef",
    {
        "PlayerSession": "PlayerSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlayerSessionsInputRequestTypeDef = TypedDict(
    "CreatePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": str,
        "PlayerIds": Sequence[str],
        "PlayerDataMap": NotRequired[Mapping[str, str]],
    },
)

CreatePlayerSessionsOutputTypeDef = TypedDict(
    "CreatePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateScriptInputRequestTypeDef = TypedDict(
    "CreateScriptInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired["S3LocationTypeDef"],
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateScriptOutputTypeDef = TypedDict(
    "CreateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

CreateVpcPeeringAuthorizationOutputTypeDef = TypedDict(
    "CreateVpcPeeringAuthorizationOutputTypeDef",
    {
        "VpcPeeringAuthorization": "VpcPeeringAuthorizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "CreateVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "PeerVpcAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteAliasInputRequestTypeDef = TypedDict(
    "DeleteAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

DeleteBuildInputRequestTypeDef = TypedDict(
    "DeleteBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

DeleteFleetInputRequestTypeDef = TypedDict(
    "DeleteFleetInputRequestTypeDef",
    {
        "FleetId": str,
    },
)

DeleteFleetLocationsInputRequestTypeDef = TypedDict(
    "DeleteFleetLocationsInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": Sequence[str],
    },
)

DeleteFleetLocationsOutputTypeDef = TypedDict(
    "DeleteFleetLocationsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationStates": List["LocationStateTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameServerGroupInputRequestTypeDef = TypedDict(
    "DeleteGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "DeleteOption": NotRequired[GameServerGroupDeleteOptionType],
    },
)

DeleteGameServerGroupOutputTypeDef = TypedDict(
    "DeleteGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGameSessionQueueInputRequestTypeDef = TypedDict(
    "DeleteGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "DeleteMatchmakingRuleSetInputRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteScalingPolicyInputRequestTypeDef = TypedDict(
    "DeleteScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
    },
)

DeleteScriptInputRequestTypeDef = TypedDict(
    "DeleteScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)

DeleteVpcPeeringAuthorizationInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringAuthorizationInputRequestTypeDef",
    {
        "GameLiftAwsAccountId": str,
        "PeerVpcId": str,
    },
)

DeleteVpcPeeringConnectionInputRequestTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionInputRequestTypeDef",
    {
        "FleetId": str,
        "VpcPeeringConnectionId": str,
    },
)

DeregisterGameServerInputRequestTypeDef = TypedDict(
    "DeregisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

DescribeAliasInputRequestTypeDef = TypedDict(
    "DescribeAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

DescribeAliasOutputTypeDef = TypedDict(
    "DescribeAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBuildInputRequestTypeDef = TypedDict(
    "DescribeBuildInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

DescribeBuildOutputTypeDef = TypedDict(
    "DescribeBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEC2InstanceLimitsInputRequestTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsInputRequestTypeDef",
    {
        "EC2InstanceType": NotRequired[EC2InstanceTypeType],
        "Location": NotRequired[str],
    },
)

DescribeEC2InstanceLimitsOutputTypeDef = TypedDict(
    "DescribeEC2InstanceLimitsOutputTypeDef",
    {
        "EC2InstanceLimits": List["EC2InstanceLimitTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetAttributesInputRequestTypeDef = TypedDict(
    "DescribeFleetAttributesInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetAttributesOutputTypeDef = TypedDict(
    "DescribeFleetAttributesOutputTypeDef",
    {
        "FleetAttributes": List["FleetAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetCapacityInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetCapacityOutputTypeDef = TypedDict(
    "DescribeFleetCapacityOutputTypeDef",
    {
        "FleetCapacity": List["FleetCapacityTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetEventsInputRequestTypeDef = TypedDict(
    "DescribeFleetEventsInputRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": NotRequired[Union[datetime, str]],
        "EndTime": NotRequired[Union[datetime, str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetEventsOutputTypeDef = TypedDict(
    "DescribeFleetEventsOutputTypeDef",
    {
        "Events": List["EventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationAttributesInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationAttributesInputRequestTypeDef",
    {
        "FleetId": str,
        "Locations": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetLocationAttributesOutputTypeDef = TypedDict(
    "DescribeFleetLocationAttributesOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "LocationAttributes": List["LocationAttributesTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationCapacityInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationCapacityInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationCapacityOutputTypeDef = TypedDict(
    "DescribeFleetLocationCapacityOutputTypeDef",
    {
        "FleetCapacity": "FleetCapacityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetLocationUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": str,
    },
)

DescribeFleetLocationUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetLocationUtilizationOutputTypeDef",
    {
        "FleetUtilization": "FleetUtilizationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetPortSettingsInputRequestTypeDef = TypedDict(
    "DescribeFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
        "Location": NotRequired[str],
    },
)

DescribeFleetPortSettingsOutputTypeDef = TypedDict(
    "DescribeFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "InboundPermissions": List["IpPermissionTypeDef"],
        "UpdateStatus": Literal["PENDING_UPDATE"],
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetUtilizationInputRequestTypeDef = TypedDict(
    "DescribeFleetUtilizationInputRequestTypeDef",
    {
        "FleetIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeFleetUtilizationOutputTypeDef = TypedDict(
    "DescribeFleetUtilizationOutputTypeDef",
    {
        "FleetUtilization": List["FleetUtilizationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerGroupInputRequestTypeDef = TypedDict(
    "DescribeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
    },
)

DescribeGameServerGroupOutputTypeDef = TypedDict(
    "DescribeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerInputRequestTypeDef = TypedDict(
    "DescribeGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
    },
)

DescribeGameServerInstancesInputRequestTypeDef = TypedDict(
    "DescribeGameServerInstancesInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "InstanceIds": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeGameServerInstancesOutputTypeDef = TypedDict(
    "DescribeGameServerInstancesOutputTypeDef",
    {
        "GameServerInstances": List["GameServerInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameServerOutputTypeDef = TypedDict(
    "DescribeGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionDetailsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionDetailsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeGameSessionDetailsOutputTypeDef = TypedDict(
    "DescribeGameSessionDetailsOutputTypeDef",
    {
        "GameSessionDetails": List["GameSessionDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionPlacementInputRequestTypeDef = TypedDict(
    "DescribeGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)

DescribeGameSessionPlacementOutputTypeDef = TypedDict(
    "DescribeGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionQueuesInputRequestTypeDef = TypedDict(
    "DescribeGameSessionQueuesInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeGameSessionQueuesOutputTypeDef = TypedDict(
    "DescribeGameSessionQueuesOutputTypeDef",
    {
        "GameSessionQueues": List["GameSessionQueueTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGameSessionsInputRequestTypeDef = TypedDict(
    "DescribeGameSessionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "StatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeGameSessionsOutputTypeDef = TypedDict(
    "DescribeGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesInputRequestTypeDef = TypedDict(
    "DescribeInstancesInputRequestTypeDef",
    {
        "FleetId": str,
        "InstanceId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "Location": NotRequired[str],
    },
)

DescribeInstancesOutputTypeDef = TypedDict(
    "DescribeInstancesOutputTypeDef",
    {
        "Instances": List["InstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingConfigurationsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "RuleSetName": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMatchmakingConfigurationsOutputTypeDef = TypedDict(
    "DescribeMatchmakingConfigurationsOutputTypeDef",
    {
        "Configurations": List["MatchmakingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingInputRequestTypeDef",
    {
        "TicketIds": Sequence[str],
    },
)

DescribeMatchmakingOutputTypeDef = TypedDict(
    "DescribeMatchmakingOutputTypeDef",
    {
        "TicketList": List["MatchmakingTicketTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMatchmakingRuleSetsInputRequestTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsInputRequestTypeDef",
    {
        "Names": NotRequired[Sequence[str]],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeMatchmakingRuleSetsOutputTypeDef = TypedDict(
    "DescribeMatchmakingRuleSetsOutputTypeDef",
    {
        "RuleSets": List["MatchmakingRuleSetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlayerSessionsInputRequestTypeDef = TypedDict(
    "DescribePlayerSessionsInputRequestTypeDef",
    {
        "GameSessionId": NotRequired[str],
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
        "PlayerSessionStatusFilter": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribePlayerSessionsOutputTypeDef = TypedDict(
    "DescribePlayerSessionsOutputTypeDef",
    {
        "PlayerSessions": List["PlayerSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "DescribeRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
    },
)

DescribeRuntimeConfigurationOutputTypeDef = TypedDict(
    "DescribeRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScalingPoliciesInputRequestTypeDef = TypedDict(
    "DescribeScalingPoliciesInputRequestTypeDef",
    {
        "FleetId": str,
        "StatusFilter": NotRequired[ScalingStatusTypeType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "Location": NotRequired[str],
    },
)

DescribeScalingPoliciesOutputTypeDef = TypedDict(
    "DescribeScalingPoliciesOutputTypeDef",
    {
        "ScalingPolicies": List["ScalingPolicyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScriptInputRequestTypeDef = TypedDict(
    "DescribeScriptInputRequestTypeDef",
    {
        "ScriptId": str,
    },
)

DescribeScriptOutputTypeDef = TypedDict(
    "DescribeScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringAuthorizationsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringAuthorizationsOutputTypeDef",
    {
        "VpcPeeringAuthorizations": List["VpcPeeringAuthorizationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsInputRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
    },
)

DescribeVpcPeeringConnectionsOutputTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsOutputTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DesiredPlayerSessionTypeDef = TypedDict(
    "DesiredPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerData": NotRequired[str],
    },
)

EC2InstanceCountsTypeDef = TypedDict(
    "EC2InstanceCountsTypeDef",
    {
        "DESIRED": NotRequired[int],
        "MINIMUM": NotRequired[int],
        "MAXIMUM": NotRequired[int],
        "PENDING": NotRequired[int],
        "ACTIVE": NotRequired[int],
        "IDLE": NotRequired[int],
        "TERMINATING": NotRequired[int],
    },
)

EC2InstanceLimitTypeDef = TypedDict(
    "EC2InstanceLimitTypeDef",
    {
        "EC2InstanceType": NotRequired[EC2InstanceTypeType],
        "CurrentInstances": NotRequired[int],
        "InstanceLimit": NotRequired[int],
        "Location": NotRequired[str],
    },
)

EventTypeDef = TypedDict(
    "EventTypeDef",
    {
        "EventId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "EventCode": NotRequired[EventCodeType],
        "Message": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "PreSignedLogUrl": NotRequired[str],
    },
)

FilterConfigurationTypeDef = TypedDict(
    "FilterConfigurationTypeDef",
    {
        "AllowedLocations": NotRequired[Sequence[str]],
    },
)

FleetAttributesTypeDef = TypedDict(
    "FleetAttributesTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "FleetType": NotRequired[FleetTypeType],
        "InstanceType": NotRequired[EC2InstanceTypeType],
        "Description": NotRequired[str],
        "Name": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "Status": NotRequired[FleetStatusType],
        "BuildId": NotRequired[str],
        "BuildArn": NotRequired[str],
        "ScriptId": NotRequired[str],
        "ScriptArn": NotRequired[str],
        "ServerLaunchPath": NotRequired[str],
        "ServerLaunchParameters": NotRequired[str],
        "LogPaths": NotRequired[List[str]],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "ResourceCreationLimitPolicy": NotRequired["ResourceCreationLimitPolicyTypeDef"],
        "MetricGroups": NotRequired[List[str]],
        "StoppedActions": NotRequired[List[Literal["AUTO_SCALING"]]],
        "InstanceRoleArn": NotRequired[str],
        "CertificateConfiguration": NotRequired["CertificateConfigurationTypeDef"],
    },
)

FleetCapacityTypeDef = TypedDict(
    "FleetCapacityTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "InstanceType": NotRequired[EC2InstanceTypeType],
        "InstanceCounts": NotRequired["EC2InstanceCountsTypeDef"],
        "Location": NotRequired[str],
    },
)

FleetUtilizationTypeDef = TypedDict(
    "FleetUtilizationTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "ActiveServerProcessCount": NotRequired[int],
        "ActiveGameSessionCount": NotRequired[int],
        "CurrentPlayerSessionCount": NotRequired[int],
        "MaximumPlayerSessionCount": NotRequired[int],
        "Location": NotRequired[str],
    },
)

GamePropertyTypeDef = TypedDict(
    "GamePropertyTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

GameServerGroupAutoScalingPolicyTypeDef = TypedDict(
    "GameServerGroupAutoScalingPolicyTypeDef",
    {
        "TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef",
        "EstimatedInstanceWarmup": NotRequired[int],
    },
)

GameServerGroupTypeDef = TypedDict(
    "GameServerGroupTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "RoleArn": NotRequired[str],
        "InstanceDefinitions": NotRequired[List["InstanceDefinitionTypeDef"]],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "AutoScalingGroupArn": NotRequired[str],
        "Status": NotRequired[GameServerGroupStatusType],
        "StatusReason": NotRequired[str],
        "SuspendedActions": NotRequired[List[Literal["REPLACE_INSTANCE_TYPES"]]],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
    },
)

GameServerInstanceTypeDef = TypedDict(
    "GameServerInstanceTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "InstanceId": NotRequired[str],
        "InstanceStatus": NotRequired[GameServerInstanceStatusType],
    },
)

GameServerTypeDef = TypedDict(
    "GameServerTypeDef",
    {
        "GameServerGroupName": NotRequired[str],
        "GameServerGroupArn": NotRequired[str],
        "GameServerId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "ConnectionInfo": NotRequired[str],
        "GameServerData": NotRequired[str],
        "ClaimStatus": NotRequired[Literal["CLAIMED"]],
        "UtilizationStatus": NotRequired[GameServerUtilizationStatusType],
        "RegistrationTime": NotRequired[datetime],
        "LastClaimTime": NotRequired[datetime],
        "LastHealthCheckTime": NotRequired[datetime],
    },
)

GameSessionConnectionInfoTypeDef = TypedDict(
    "GameSessionConnectionInfoTypeDef",
    {
        "GameSessionArn": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "MatchedPlayerSessions": NotRequired[List["MatchedPlayerSessionTypeDef"]],
    },
)

GameSessionDetailTypeDef = TypedDict(
    "GameSessionDetailTypeDef",
    {
        "GameSession": NotRequired["GameSessionTypeDef"],
        "ProtectionPolicy": NotRequired[ProtectionPolicyType],
    },
)

GameSessionPlacementTypeDef = TypedDict(
    "GameSessionPlacementTypeDef",
    {
        "PlacementId": NotRequired[str],
        "GameSessionQueueName": NotRequired[str],
        "Status": NotRequired[GameSessionPlacementStateType],
        "GameProperties": NotRequired[List["GamePropertyTypeDef"]],
        "MaximumPlayerSessionCount": NotRequired[int],
        "GameSessionName": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "GameSessionArn": NotRequired[str],
        "GameSessionRegion": NotRequired[str],
        "PlayerLatencies": NotRequired[List["PlayerLatencyTypeDef"]],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlacedPlayerSessions": NotRequired[List["PlacedPlayerSessionTypeDef"]],
        "GameSessionData": NotRequired[str],
        "MatchmakerData": NotRequired[str],
    },
)

GameSessionQueueDestinationTypeDef = TypedDict(
    "GameSessionQueueDestinationTypeDef",
    {
        "DestinationArn": NotRequired[str],
    },
)

GameSessionQueueTypeDef = TypedDict(
    "GameSessionQueueTypeDef",
    {
        "Name": NotRequired[str],
        "GameSessionQueueArn": NotRequired[str],
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[List["PlayerLatencyPolicyTypeDef"]],
        "Destinations": NotRequired[List["GameSessionQueueDestinationTypeDef"]],
        "FilterConfiguration": NotRequired["FilterConfigurationTypeDef"],
        "PriorityConfiguration": NotRequired["PriorityConfigurationTypeDef"],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
    },
)

GameSessionTypeDef = TypedDict(
    "GameSessionTypeDef",
    {
        "GameSessionId": NotRequired[str],
        "Name": NotRequired[str],
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "CurrentPlayerSessionCount": NotRequired[int],
        "MaximumPlayerSessionCount": NotRequired[int],
        "Status": NotRequired[GameSessionStatusType],
        "StatusReason": NotRequired[Literal["INTERRUPTED"]],
        "GameProperties": NotRequired[List["GamePropertyTypeDef"]],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlayerSessionCreationPolicy": NotRequired[PlayerSessionCreationPolicyType],
        "CreatorId": NotRequired[str],
        "GameSessionData": NotRequired[str],
        "MatchmakerData": NotRequired[str],
        "Location": NotRequired[str],
    },
)

GetGameSessionLogUrlInputRequestTypeDef = TypedDict(
    "GetGameSessionLogUrlInputRequestTypeDef",
    {
        "GameSessionId": str,
    },
)

GetGameSessionLogUrlOutputTypeDef = TypedDict(
    "GetGameSessionLogUrlOutputTypeDef",
    {
        "PreSignedUrl": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInstanceAccessInputRequestTypeDef = TypedDict(
    "GetInstanceAccessInputRequestTypeDef",
    {
        "FleetId": str,
        "InstanceId": str,
    },
)

GetInstanceAccessOutputTypeDef = TypedDict(
    "GetInstanceAccessOutputTypeDef",
    {
        "InstanceAccess": "InstanceAccessTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceAccessTypeDef = TypedDict(
    "InstanceAccessTypeDef",
    {
        "FleetId": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Credentials": NotRequired["InstanceCredentialsTypeDef"],
    },
)

InstanceCredentialsTypeDef = TypedDict(
    "InstanceCredentialsTypeDef",
    {
        "UserName": NotRequired[str],
        "Secret": NotRequired[str],
    },
)

InstanceDefinitionTypeDef = TypedDict(
    "InstanceDefinitionTypeDef",
    {
        "InstanceType": GameServerGroupInstanceTypeType,
        "WeightedCapacity": NotRequired[str],
    },
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "InstanceId": NotRequired[str],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "OperatingSystem": NotRequired[OperatingSystemType],
        "Type": NotRequired[EC2InstanceTypeType],
        "Status": NotRequired[InstanceStatusType],
        "CreationTime": NotRequired[datetime],
        "Location": NotRequired[str],
    },
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "IpRange": str,
        "Protocol": IpProtocolType,
    },
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": NotRequired[str],
        "LaunchTemplateName": NotRequired[str],
        "Version": NotRequired[str],
    },
)

ListAliasesInputRequestTypeDef = TypedDict(
    "ListAliasesInputRequestTypeDef",
    {
        "RoutingStrategyType": NotRequired[RoutingStrategyTypeType],
        "Name": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAliasesOutputTypeDef = TypedDict(
    "ListAliasesOutputTypeDef",
    {
        "Aliases": List["AliasTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBuildsInputRequestTypeDef = TypedDict(
    "ListBuildsInputRequestTypeDef",
    {
        "Status": NotRequired[BuildStatusType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {
        "Builds": List["BuildTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsInputRequestTypeDef = TypedDict(
    "ListFleetsInputRequestTypeDef",
    {
        "BuildId": NotRequired[str],
        "ScriptId": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFleetsOutputTypeDef = TypedDict(
    "ListFleetsOutputTypeDef",
    {
        "FleetIds": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServerGroupsInputRequestTypeDef = TypedDict(
    "ListGameServerGroupsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGameServerGroupsOutputTypeDef = TypedDict(
    "ListGameServerGroupsOutputTypeDef",
    {
        "GameServerGroups": List["GameServerGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGameServersInputRequestTypeDef = TypedDict(
    "ListGameServersInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "SortOrder": NotRequired[SortOrderType],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListGameServersOutputTypeDef = TypedDict(
    "ListGameServersOutputTypeDef",
    {
        "GameServers": List["GameServerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListScriptsInputRequestTypeDef = TypedDict(
    "ListScriptsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListScriptsOutputTypeDef = TypedDict(
    "ListScriptsOutputTypeDef",
    {
        "Scripts": List["ScriptTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationAttributesTypeDef = TypedDict(
    "LocationAttributesTypeDef",
    {
        "LocationState": NotRequired["LocationStateTypeDef"],
        "StoppedActions": NotRequired[List[Literal["AUTO_SCALING"]]],
        "UpdateStatus": NotRequired[Literal["PENDING_UPDATE"]],
    },
)

LocationConfigurationTypeDef = TypedDict(
    "LocationConfigurationTypeDef",
    {
        "Location": NotRequired[str],
    },
)

LocationStateTypeDef = TypedDict(
    "LocationStateTypeDef",
    {
        "Location": NotRequired[str],
        "Status": NotRequired[FleetStatusType],
    },
)

MatchedPlayerSessionTypeDef = TypedDict(
    "MatchedPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
    },
)

MatchmakingConfigurationTypeDef = TypedDict(
    "MatchmakingConfigurationTypeDef",
    {
        "Name": NotRequired[str],
        "ConfigurationArn": NotRequired[str],
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[List[str]],
        "RequestTimeoutSeconds": NotRequired[int],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "AcceptanceRequired": NotRequired[bool],
        "RuleSetName": NotRequired[str],
        "RuleSetArn": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "GameProperties": NotRequired[List["GamePropertyTypeDef"]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
    },
)

MatchmakingRuleSetTypeDef = TypedDict(
    "MatchmakingRuleSetTypeDef",
    {
        "RuleSetBody": str,
        "RuleSetName": NotRequired[str],
        "RuleSetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
    },
)

MatchmakingTicketTypeDef = TypedDict(
    "MatchmakingTicketTypeDef",
    {
        "TicketId": NotRequired[str],
        "ConfigurationName": NotRequired[str],
        "ConfigurationArn": NotRequired[str],
        "Status": NotRequired[MatchmakingConfigurationStatusType],
        "StatusReason": NotRequired[str],
        "StatusMessage": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Players": NotRequired[List["PlayerTypeDef"]],
        "GameSessionConnectionInfo": NotRequired["GameSessionConnectionInfoTypeDef"],
        "EstimatedWaitTime": NotRequired[int],
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

PlacedPlayerSessionTypeDef = TypedDict(
    "PlacedPlayerSessionTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerSessionId": NotRequired[str],
    },
)

PlayerLatencyPolicyTypeDef = TypedDict(
    "PlayerLatencyPolicyTypeDef",
    {
        "MaximumIndividualPlayerLatencyMilliseconds": NotRequired[int],
        "PolicyDurationSeconds": NotRequired[int],
    },
)

PlayerLatencyTypeDef = TypedDict(
    "PlayerLatencyTypeDef",
    {
        "PlayerId": NotRequired[str],
        "RegionIdentifier": NotRequired[str],
        "LatencyInMilliseconds": NotRequired[float],
    },
)

PlayerSessionTypeDef = TypedDict(
    "PlayerSessionTypeDef",
    {
        "PlayerSessionId": NotRequired[str],
        "PlayerId": NotRequired[str],
        "GameSessionId": NotRequired[str],
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "TerminationTime": NotRequired[datetime],
        "Status": NotRequired[PlayerSessionStatusType],
        "IpAddress": NotRequired[str],
        "DnsName": NotRequired[str],
        "Port": NotRequired[int],
        "PlayerData": NotRequired[str],
    },
)

PlayerTypeDef = TypedDict(
    "PlayerTypeDef",
    {
        "PlayerId": NotRequired[str],
        "PlayerAttributes": NotRequired[Dict[str, "AttributeValueTypeDef"]],
        "Team": NotRequired[str],
        "LatencyInMs": NotRequired[Dict[str, int]],
    },
)

PriorityConfigurationTypeDef = TypedDict(
    "PriorityConfigurationTypeDef",
    {
        "PriorityOrder": NotRequired[Sequence[PriorityTypeType]],
        "LocationOrder": NotRequired[Sequence[str]],
    },
)

PutScalingPolicyInputRequestTypeDef = TypedDict(
    "PutScalingPolicyInputRequestTypeDef",
    {
        "Name": str,
        "FleetId": str,
        "MetricName": MetricNameType,
        "ScalingAdjustment": NotRequired[int],
        "ScalingAdjustmentType": NotRequired[ScalingAdjustmentTypeType],
        "Threshold": NotRequired[float],
        "ComparisonOperator": NotRequired[ComparisonOperatorTypeType],
        "EvaluationPeriods": NotRequired[int],
        "PolicyType": NotRequired[PolicyTypeType],
        "TargetConfiguration": NotRequired["TargetConfigurationTypeDef"],
    },
)

PutScalingPolicyOutputTypeDef = TypedDict(
    "PutScalingPolicyOutputTypeDef",
    {
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterGameServerInputRequestTypeDef = TypedDict(
    "RegisterGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "InstanceId": str,
        "ConnectionInfo": NotRequired[str],
        "GameServerData": NotRequired[str],
    },
)

RegisterGameServerOutputTypeDef = TypedDict(
    "RegisterGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestUploadCredentialsInputRequestTypeDef = TypedDict(
    "RequestUploadCredentialsInputRequestTypeDef",
    {
        "BuildId": str,
    },
)

RequestUploadCredentialsOutputTypeDef = TypedDict(
    "RequestUploadCredentialsOutputTypeDef",
    {
        "UploadCredentials": "AwsCredentialsTypeDef",
        "StorageLocation": "S3LocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResolveAliasInputRequestTypeDef = TypedDict(
    "ResolveAliasInputRequestTypeDef",
    {
        "AliasId": str,
    },
)

ResolveAliasOutputTypeDef = TypedDict(
    "ResolveAliasOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResourceCreationLimitPolicyTypeDef = TypedDict(
    "ResourceCreationLimitPolicyTypeDef",
    {
        "NewGameSessionsPerCreator": NotRequired[int],
        "PolicyPeriodInMinutes": NotRequired[int],
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

ResumeGameServerGroupInputRequestTypeDef = TypedDict(
    "ResumeGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "ResumeActions": Sequence[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

ResumeGameServerGroupOutputTypeDef = TypedDict(
    "ResumeGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RoutingStrategyTypeDef = TypedDict(
    "RoutingStrategyTypeDef",
    {
        "Type": NotRequired[RoutingStrategyTypeType],
        "FleetId": NotRequired[str],
        "Message": NotRequired[str],
    },
)

RuntimeConfigurationTypeDef = TypedDict(
    "RuntimeConfigurationTypeDef",
    {
        "ServerProcesses": NotRequired[Sequence["ServerProcessTypeDef"]],
        "MaxConcurrentGameSessionActivations": NotRequired[int],
        "GameSessionActivationTimeoutSeconds": NotRequired[int],
    },
)

S3LocationTypeDef = TypedDict(
    "S3LocationTypeDef",
    {
        "Bucket": NotRequired[str],
        "Key": NotRequired[str],
        "RoleArn": NotRequired[str],
        "ObjectVersion": NotRequired[str],
    },
)

ScalingPolicyTypeDef = TypedDict(
    "ScalingPolicyTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ScalingStatusTypeType],
        "ScalingAdjustment": NotRequired[int],
        "ScalingAdjustmentType": NotRequired[ScalingAdjustmentTypeType],
        "ComparisonOperator": NotRequired[ComparisonOperatorTypeType],
        "Threshold": NotRequired[float],
        "EvaluationPeriods": NotRequired[int],
        "MetricName": NotRequired[MetricNameType],
        "PolicyType": NotRequired[PolicyTypeType],
        "TargetConfiguration": NotRequired["TargetConfigurationTypeDef"],
        "UpdateStatus": NotRequired[Literal["PENDING_UPDATE"]],
        "Location": NotRequired[str],
    },
)

ScriptTypeDef = TypedDict(
    "ScriptTypeDef",
    {
        "ScriptId": NotRequired[str],
        "ScriptArn": NotRequired[str],
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "SizeOnDisk": NotRequired[int],
        "CreationTime": NotRequired[datetime],
        "StorageLocation": NotRequired["S3LocationTypeDef"],
    },
)

SearchGameSessionsInputRequestTypeDef = TypedDict(
    "SearchGameSessionsInputRequestTypeDef",
    {
        "FleetId": NotRequired[str],
        "AliasId": NotRequired[str],
        "Location": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "SortExpression": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchGameSessionsOutputTypeDef = TypedDict(
    "SearchGameSessionsOutputTypeDef",
    {
        "GameSessions": List["GameSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServerProcessTypeDef = TypedDict(
    "ServerProcessTypeDef",
    {
        "LaunchPath": str,
        "ConcurrentExecutions": int,
        "Parameters": NotRequired[str],
    },
)

StartFleetActionsInputRequestTypeDef = TypedDict(
    "StartFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": Sequence[Literal["AUTO_SCALING"]],
        "Location": NotRequired[str],
    },
)

StartFleetActionsOutputTypeDef = TypedDict(
    "StartFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGameSessionPlacementInputRequestTypeDef = TypedDict(
    "StartGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
        "GameSessionQueueName": str,
        "MaximumPlayerSessionCount": int,
        "GameProperties": NotRequired[Sequence["GamePropertyTypeDef"]],
        "GameSessionName": NotRequired[str],
        "PlayerLatencies": NotRequired[Sequence["PlayerLatencyTypeDef"]],
        "DesiredPlayerSessions": NotRequired[Sequence["DesiredPlayerSessionTypeDef"]],
        "GameSessionData": NotRequired[str],
    },
)

StartGameSessionPlacementOutputTypeDef = TypedDict(
    "StartGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMatchBackfillInputRequestTypeDef = TypedDict(
    "StartMatchBackfillInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": Sequence["PlayerTypeDef"],
        "TicketId": NotRequired[str],
        "GameSessionArn": NotRequired[str],
    },
)

StartMatchBackfillOutputTypeDef = TypedDict(
    "StartMatchBackfillOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartMatchmakingInputRequestTypeDef = TypedDict(
    "StartMatchmakingInputRequestTypeDef",
    {
        "ConfigurationName": str,
        "Players": Sequence["PlayerTypeDef"],
        "TicketId": NotRequired[str],
    },
)

StartMatchmakingOutputTypeDef = TypedDict(
    "StartMatchmakingOutputTypeDef",
    {
        "MatchmakingTicket": "MatchmakingTicketTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFleetActionsInputRequestTypeDef = TypedDict(
    "StopFleetActionsInputRequestTypeDef",
    {
        "FleetId": str,
        "Actions": Sequence[Literal["AUTO_SCALING"]],
        "Location": NotRequired[str],
    },
)

StopFleetActionsOutputTypeDef = TypedDict(
    "StopFleetActionsOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopGameSessionPlacementInputRequestTypeDef = TypedDict(
    "StopGameSessionPlacementInputRequestTypeDef",
    {
        "PlacementId": str,
    },
)

StopGameSessionPlacementOutputTypeDef = TypedDict(
    "StopGameSessionPlacementOutputTypeDef",
    {
        "GameSessionPlacement": "GameSessionPlacementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopMatchmakingInputRequestTypeDef = TypedDict(
    "StopMatchmakingInputRequestTypeDef",
    {
        "TicketId": str,
    },
)

SuspendGameServerGroupInputRequestTypeDef = TypedDict(
    "SuspendGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "SuspendActions": Sequence[Literal["REPLACE_INSTANCE_TYPES"]],
    },
)

SuspendGameServerGroupOutputTypeDef = TypedDict(
    "SuspendGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

TargetTrackingConfigurationTypeDef = TypedDict(
    "TargetTrackingConfigurationTypeDef",
    {
        "TargetValue": float,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAliasInputRequestTypeDef = TypedDict(
    "UpdateAliasInputRequestTypeDef",
    {
        "AliasId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "RoutingStrategy": NotRequired["RoutingStrategyTypeDef"],
    },
)

UpdateAliasOutputTypeDef = TypedDict(
    "UpdateAliasOutputTypeDef",
    {
        "Alias": "AliasTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBuildInputRequestTypeDef = TypedDict(
    "UpdateBuildInputRequestTypeDef",
    {
        "BuildId": str,
        "Name": NotRequired[str],
        "Version": NotRequired[str],
    },
)

UpdateBuildOutputTypeDef = TypedDict(
    "UpdateBuildOutputTypeDef",
    {
        "Build": "BuildTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetAttributesInputRequestTypeDef = TypedDict(
    "UpdateFleetAttributesInputRequestTypeDef",
    {
        "FleetId": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "NewGameSessionProtectionPolicy": NotRequired[ProtectionPolicyType],
        "ResourceCreationLimitPolicy": NotRequired["ResourceCreationLimitPolicyTypeDef"],
        "MetricGroups": NotRequired[Sequence[str]],
    },
)

UpdateFleetAttributesOutputTypeDef = TypedDict(
    "UpdateFleetAttributesOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetCapacityInputRequestTypeDef = TypedDict(
    "UpdateFleetCapacityInputRequestTypeDef",
    {
        "FleetId": str,
        "DesiredInstances": NotRequired[int],
        "MinSize": NotRequired[int],
        "MaxSize": NotRequired[int],
        "Location": NotRequired[str],
    },
)

UpdateFleetCapacityOutputTypeDef = TypedDict(
    "UpdateFleetCapacityOutputTypeDef",
    {
        "FleetId": str,
        "FleetArn": str,
        "Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFleetPortSettingsInputRequestTypeDef = TypedDict(
    "UpdateFleetPortSettingsInputRequestTypeDef",
    {
        "FleetId": str,
        "InboundPermissionAuthorizations": NotRequired[Sequence["IpPermissionTypeDef"]],
        "InboundPermissionRevocations": NotRequired[Sequence["IpPermissionTypeDef"]],
    },
)

UpdateFleetPortSettingsOutputTypeDef = TypedDict(
    "UpdateFleetPortSettingsOutputTypeDef",
    {
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameServerGroupInputRequestTypeDef = TypedDict(
    "UpdateGameServerGroupInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "RoleArn": NotRequired[str],
        "InstanceDefinitions": NotRequired[Sequence["InstanceDefinitionTypeDef"]],
        "GameServerProtectionPolicy": NotRequired[GameServerProtectionPolicyType],
        "BalancingStrategy": NotRequired[BalancingStrategyType],
    },
)

UpdateGameServerGroupOutputTypeDef = TypedDict(
    "UpdateGameServerGroupOutputTypeDef",
    {
        "GameServerGroup": "GameServerGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameServerInputRequestTypeDef = TypedDict(
    "UpdateGameServerInputRequestTypeDef",
    {
        "GameServerGroupName": str,
        "GameServerId": str,
        "GameServerData": NotRequired[str],
        "UtilizationStatus": NotRequired[GameServerUtilizationStatusType],
        "HealthCheck": NotRequired[Literal["HEALTHY"]],
    },
)

UpdateGameServerOutputTypeDef = TypedDict(
    "UpdateGameServerOutputTypeDef",
    {
        "GameServer": "GameServerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameSessionInputRequestTypeDef = TypedDict(
    "UpdateGameSessionInputRequestTypeDef",
    {
        "GameSessionId": str,
        "MaximumPlayerSessionCount": NotRequired[int],
        "Name": NotRequired[str],
        "PlayerSessionCreationPolicy": NotRequired[PlayerSessionCreationPolicyType],
        "ProtectionPolicy": NotRequired[ProtectionPolicyType],
    },
)

UpdateGameSessionOutputTypeDef = TypedDict(
    "UpdateGameSessionOutputTypeDef",
    {
        "GameSession": "GameSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGameSessionQueueInputRequestTypeDef = TypedDict(
    "UpdateGameSessionQueueInputRequestTypeDef",
    {
        "Name": str,
        "TimeoutInSeconds": NotRequired[int],
        "PlayerLatencyPolicies": NotRequired[Sequence["PlayerLatencyPolicyTypeDef"]],
        "Destinations": NotRequired[Sequence["GameSessionQueueDestinationTypeDef"]],
        "FilterConfiguration": NotRequired["FilterConfigurationTypeDef"],
        "PriorityConfiguration": NotRequired["PriorityConfigurationTypeDef"],
        "CustomEventData": NotRequired[str],
        "NotificationTarget": NotRequired[str],
    },
)

UpdateGameSessionQueueOutputTypeDef = TypedDict(
    "UpdateGameSessionQueueOutputTypeDef",
    {
        "GameSessionQueue": "GameSessionQueueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMatchmakingConfigurationInputRequestTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationInputRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "GameSessionQueueArns": NotRequired[Sequence[str]],
        "RequestTimeoutSeconds": NotRequired[int],
        "AcceptanceTimeoutSeconds": NotRequired[int],
        "AcceptanceRequired": NotRequired[bool],
        "RuleSetName": NotRequired[str],
        "NotificationTarget": NotRequired[str],
        "AdditionalPlayerCount": NotRequired[int],
        "CustomEventData": NotRequired[str],
        "GameProperties": NotRequired[Sequence["GamePropertyTypeDef"]],
        "GameSessionData": NotRequired[str],
        "BackfillMode": NotRequired[BackfillModeType],
        "FlexMatchMode": NotRequired[FlexMatchModeType],
    },
)

UpdateMatchmakingConfigurationOutputTypeDef = TypedDict(
    "UpdateMatchmakingConfigurationOutputTypeDef",
    {
        "Configuration": "MatchmakingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRuntimeConfigurationInputRequestTypeDef = TypedDict(
    "UpdateRuntimeConfigurationInputRequestTypeDef",
    {
        "FleetId": str,
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
    },
)

UpdateRuntimeConfigurationOutputTypeDef = TypedDict(
    "UpdateRuntimeConfigurationOutputTypeDef",
    {
        "RuntimeConfiguration": "RuntimeConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateScriptInputRequestTypeDef = TypedDict(
    "UpdateScriptInputRequestTypeDef",
    {
        "ScriptId": str,
        "Name": NotRequired[str],
        "Version": NotRequired[str],
        "StorageLocation": NotRequired["S3LocationTypeDef"],
        "ZipFile": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

UpdateScriptOutputTypeDef = TypedDict(
    "UpdateScriptOutputTypeDef",
    {
        "Script": "ScriptTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ValidateMatchmakingRuleSetInputRequestTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetInputRequestTypeDef",
    {
        "RuleSetBody": str,
    },
)

ValidateMatchmakingRuleSetOutputTypeDef = TypedDict(
    "ValidateMatchmakingRuleSetOutputTypeDef",
    {
        "Valid": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcPeeringAuthorizationTypeDef = TypedDict(
    "VpcPeeringAuthorizationTypeDef",
    {
        "GameLiftAwsAccountId": NotRequired[str],
        "PeerVpcAwsAccountId": NotRequired[str],
        "PeerVpcId": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "ExpirationTime": NotRequired[datetime],
    },
)

VpcPeeringConnectionStatusTypeDef = TypedDict(
    "VpcPeeringConnectionStatusTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "FleetId": NotRequired[str],
        "FleetArn": NotRequired[str],
        "IpV4CidrBlock": NotRequired[str],
        "VpcPeeringConnectionId": NotRequired[str],
        "Status": NotRequired["VpcPeeringConnectionStatusTypeDef"],
        "PeerVpcId": NotRequired[str],
        "GameLiftVpcId": NotRequired[str],
    },
)
