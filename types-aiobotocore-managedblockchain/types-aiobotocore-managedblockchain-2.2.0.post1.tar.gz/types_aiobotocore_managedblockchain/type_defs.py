"""
Type annotations for managedblockchain service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_managedblockchain/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef

    data: ApprovalThresholdPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    EditionType,
    FrameworkType,
    InvitationStatusType,
    MemberStatusType,
    NetworkStatusType,
    NodeStatusType,
    ProposalStatusType,
    StateDBTypeType,
    ThresholdComparatorType,
    VoteValueType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalThresholdPolicyTypeDef",
    "CreateMemberInputRequestTypeDef",
    "CreateMemberOutputTypeDef",
    "CreateNetworkInputRequestTypeDef",
    "CreateNetworkOutputTypeDef",
    "CreateNodeInputRequestTypeDef",
    "CreateNodeOutputTypeDef",
    "CreateProposalInputRequestTypeDef",
    "CreateProposalOutputTypeDef",
    "DeleteMemberInputRequestTypeDef",
    "DeleteNodeInputRequestTypeDef",
    "GetMemberInputRequestTypeDef",
    "GetMemberOutputTypeDef",
    "GetNetworkInputRequestTypeDef",
    "GetNetworkOutputTypeDef",
    "GetNodeInputRequestTypeDef",
    "GetNodeOutputTypeDef",
    "GetProposalInputRequestTypeDef",
    "GetProposalOutputTypeDef",
    "InvitationTypeDef",
    "InviteActionTypeDef",
    "ListInvitationsInputRequestTypeDef",
    "ListInvitationsOutputTypeDef",
    "ListMembersInputRequestTypeDef",
    "ListMembersOutputTypeDef",
    "ListNetworksInputRequestTypeDef",
    "ListNetworksOutputTypeDef",
    "ListNodesInputRequestTypeDef",
    "ListNodesOutputTypeDef",
    "ListProposalVotesInputRequestTypeDef",
    "ListProposalVotesOutputTypeDef",
    "ListProposalsInputRequestTypeDef",
    "ListProposalsOutputTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationsTypeDef",
    "MemberConfigurationTypeDef",
    "MemberFabricAttributesTypeDef",
    "MemberFabricConfigurationTypeDef",
    "MemberFabricLogPublishingConfigurationTypeDef",
    "MemberFrameworkAttributesTypeDef",
    "MemberFrameworkConfigurationTypeDef",
    "MemberLogPublishingConfigurationTypeDef",
    "MemberSummaryTypeDef",
    "MemberTypeDef",
    "NetworkEthereumAttributesTypeDef",
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
    "NodeConfigurationTypeDef",
    "NodeEthereumAttributesTypeDef",
    "NodeFabricAttributesTypeDef",
    "NodeFabricLogPublishingConfigurationTypeDef",
    "NodeFrameworkAttributesTypeDef",
    "NodeLogPublishingConfigurationTypeDef",
    "NodeSummaryTypeDef",
    "NodeTypeDef",
    "ProposalActionsTypeDef",
    "ProposalSummaryTypeDef",
    "ProposalTypeDef",
    "RejectInvitationInputRequestTypeDef",
    "RemoveActionTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateMemberInputRequestTypeDef",
    "UpdateNodeInputRequestTypeDef",
    "VoteOnProposalInputRequestTypeDef",
    "VoteSummaryTypeDef",
    "VotingPolicyTypeDef",
)

ApprovalThresholdPolicyTypeDef = TypedDict(
    "ApprovalThresholdPolicyTypeDef",
    {
        "ThresholdPercentage": NotRequired[int],
        "ProposalDurationInHours": NotRequired[int],
        "ThresholdComparator": NotRequired[ThresholdComparatorType],
    },
)

CreateMemberInputRequestTypeDef = TypedDict(
    "CreateMemberInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "InvitationId": str,
        "NetworkId": str,
        "MemberConfiguration": "MemberConfigurationTypeDef",
    },
)

CreateMemberOutputTypeDef = TypedDict(
    "CreateMemberOutputTypeDef",
    {
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkInputRequestTypeDef = TypedDict(
    "CreateNetworkInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "Name": str,
        "Framework": FrameworkType,
        "FrameworkVersion": str,
        "VotingPolicy": "VotingPolicyTypeDef",
        "MemberConfiguration": "MemberConfigurationTypeDef",
        "Description": NotRequired[str],
        "FrameworkConfiguration": NotRequired["NetworkFrameworkConfigurationTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateNetworkOutputTypeDef = TypedDict(
    "CreateNetworkOutputTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNodeInputRequestTypeDef = TypedDict(
    "CreateNodeInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "NodeConfiguration": "NodeConfigurationTypeDef",
        "MemberId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateNodeOutputTypeDef = TypedDict(
    "CreateNodeOutputTypeDef",
    {
        "NodeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProposalInputRequestTypeDef = TypedDict(
    "CreateProposalInputRequestTypeDef",
    {
        "ClientRequestToken": str,
        "NetworkId": str,
        "MemberId": str,
        "Actions": "ProposalActionsTypeDef",
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateProposalOutputTypeDef = TypedDict(
    "CreateProposalOutputTypeDef",
    {
        "ProposalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteMemberInputRequestTypeDef = TypedDict(
    "DeleteMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

DeleteNodeInputRequestTypeDef = TypedDict(
    "DeleteNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
    },
)

GetMemberInputRequestTypeDef = TypedDict(
    "GetMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
    },
)

GetMemberOutputTypeDef = TypedDict(
    "GetMemberOutputTypeDef",
    {
        "Member": "MemberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkInputRequestTypeDef = TypedDict(
    "GetNetworkInputRequestTypeDef",
    {
        "NetworkId": str,
    },
)

GetNetworkOutputTypeDef = TypedDict(
    "GetNetworkOutputTypeDef",
    {
        "Network": "NetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNodeInputRequestTypeDef = TypedDict(
    "GetNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
    },
)

GetNodeOutputTypeDef = TypedDict(
    "GetNodeOutputTypeDef",
    {
        "Node": "NodeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProposalInputRequestTypeDef = TypedDict(
    "GetProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
    },
)

GetProposalOutputTypeDef = TypedDict(
    "GetProposalOutputTypeDef",
    {
        "Proposal": "ProposalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "InvitationId": NotRequired[str],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "Status": NotRequired[InvitationStatusType],
        "NetworkSummary": NotRequired["NetworkSummaryTypeDef"],
        "Arn": NotRequired[str],
    },
)

InviteActionTypeDef = TypedDict(
    "InviteActionTypeDef",
    {
        "Principal": str,
    },
)

ListInvitationsInputRequestTypeDef = TypedDict(
    "ListInvitationsInputRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListInvitationsOutputTypeDef = TypedDict(
    "ListInvitationsOutputTypeDef",
    {
        "Invitations": List["InvitationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMembersInputRequestTypeDef = TypedDict(
    "ListMembersInputRequestTypeDef",
    {
        "NetworkId": str,
        "Name": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "IsOwned": NotRequired[bool],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListMembersOutputTypeDef = TypedDict(
    "ListMembersOutputTypeDef",
    {
        "Members": List["MemberSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworksInputRequestTypeDef = TypedDict(
    "ListNetworksInputRequestTypeDef",
    {
        "Name": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "Status": NotRequired[NetworkStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListNetworksOutputTypeDef = TypedDict(
    "ListNetworksOutputTypeDef",
    {
        "Networks": List["NetworkSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNodesInputRequestTypeDef = TypedDict(
    "ListNodesInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": NotRequired[str],
        "Status": NotRequired[NodeStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListNodesOutputTypeDef = TypedDict(
    "ListNodesOutputTypeDef",
    {
        "Nodes": List["NodeSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProposalVotesInputRequestTypeDef = TypedDict(
    "ListProposalVotesInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListProposalVotesOutputTypeDef = TypedDict(
    "ListProposalVotesOutputTypeDef",
    {
        "ProposalVotes": List["VoteSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProposalsInputRequestTypeDef = TypedDict(
    "ListProposalsInputRequestTypeDef",
    {
        "NetworkId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListProposalsOutputTypeDef = TypedDict(
    "ListProposalsOutputTypeDef",
    {
        "Proposals": List["ProposalSummaryTypeDef"],
        "NextToken": str,
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

LogConfigurationTypeDef = TypedDict(
    "LogConfigurationTypeDef",
    {
        "Enabled": NotRequired[bool],
    },
)

LogConfigurationsTypeDef = TypedDict(
    "LogConfigurationsTypeDef",
    {
        "Cloudwatch": NotRequired["LogConfigurationTypeDef"],
    },
)

MemberConfigurationTypeDef = TypedDict(
    "MemberConfigurationTypeDef",
    {
        "Name": str,
        "FrameworkConfiguration": "MemberFrameworkConfigurationTypeDef",
        "Description": NotRequired[str],
        "LogPublishingConfiguration": NotRequired["MemberLogPublishingConfigurationTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
        "KmsKeyArn": NotRequired[str],
    },
)

MemberFabricAttributesTypeDef = TypedDict(
    "MemberFabricAttributesTypeDef",
    {
        "AdminUsername": NotRequired[str],
        "CaEndpoint": NotRequired[str],
    },
)

MemberFabricConfigurationTypeDef = TypedDict(
    "MemberFabricConfigurationTypeDef",
    {
        "AdminUsername": str,
        "AdminPassword": str,
    },
)

MemberFabricLogPublishingConfigurationTypeDef = TypedDict(
    "MemberFabricLogPublishingConfigurationTypeDef",
    {
        "CaLogs": NotRequired["LogConfigurationsTypeDef"],
    },
)

MemberFrameworkAttributesTypeDef = TypedDict(
    "MemberFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired["MemberFabricAttributesTypeDef"],
    },
)

MemberFrameworkConfigurationTypeDef = TypedDict(
    "MemberFrameworkConfigurationTypeDef",
    {
        "Fabric": NotRequired["MemberFabricConfigurationTypeDef"],
    },
)

MemberLogPublishingConfigurationTypeDef = TypedDict(
    "MemberLogPublishingConfigurationTypeDef",
    {
        "Fabric": NotRequired["MemberFabricLogPublishingConfigurationTypeDef"],
    },
)

MemberSummaryTypeDef = TypedDict(
    "MemberSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[MemberStatusType],
        "CreationDate": NotRequired[datetime],
        "IsOwned": NotRequired[bool],
        "Arn": NotRequired[str],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "NetworkId": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "FrameworkAttributes": NotRequired["MemberFrameworkAttributesTypeDef"],
        "LogPublishingConfiguration": NotRequired["MemberLogPublishingConfigurationTypeDef"],
        "Status": NotRequired[MemberStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)

NetworkEthereumAttributesTypeDef = TypedDict(
    "NetworkEthereumAttributesTypeDef",
    {
        "ChainId": NotRequired[str],
    },
)

NetworkFabricAttributesTypeDef = TypedDict(
    "NetworkFabricAttributesTypeDef",
    {
        "OrderingServiceEndpoint": NotRequired[str],
        "Edition": NotRequired[EditionType],
    },
)

NetworkFabricConfigurationTypeDef = TypedDict(
    "NetworkFabricConfigurationTypeDef",
    {
        "Edition": EditionType,
    },
)

NetworkFrameworkAttributesTypeDef = TypedDict(
    "NetworkFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired["NetworkFabricAttributesTypeDef"],
        "Ethereum": NotRequired["NetworkEthereumAttributesTypeDef"],
    },
)

NetworkFrameworkConfigurationTypeDef = TypedDict(
    "NetworkFrameworkConfigurationTypeDef",
    {
        "Fabric": NotRequired["NetworkFabricConfigurationTypeDef"],
    },
)

NetworkSummaryTypeDef = TypedDict(
    "NetworkSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "FrameworkVersion": NotRequired[str],
        "Status": NotRequired[NetworkStatusType],
        "CreationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)

NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Framework": NotRequired[FrameworkType],
        "FrameworkVersion": NotRequired[str],
        "FrameworkAttributes": NotRequired["NetworkFrameworkAttributesTypeDef"],
        "VpcEndpointServiceName": NotRequired[str],
        "VotingPolicy": NotRequired["VotingPolicyTypeDef"],
        "Status": NotRequired[NetworkStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
    },
)

NodeConfigurationTypeDef = TypedDict(
    "NodeConfigurationTypeDef",
    {
        "InstanceType": str,
        "AvailabilityZone": NotRequired[str],
        "LogPublishingConfiguration": NotRequired["NodeLogPublishingConfigurationTypeDef"],
        "StateDB": NotRequired[StateDBTypeType],
    },
)

NodeEthereumAttributesTypeDef = TypedDict(
    "NodeEthereumAttributesTypeDef",
    {
        "HttpEndpoint": NotRequired[str],
        "WebSocketEndpoint": NotRequired[str],
    },
)

NodeFabricAttributesTypeDef = TypedDict(
    "NodeFabricAttributesTypeDef",
    {
        "PeerEndpoint": NotRequired[str],
        "PeerEventEndpoint": NotRequired[str],
    },
)

NodeFabricLogPublishingConfigurationTypeDef = TypedDict(
    "NodeFabricLogPublishingConfigurationTypeDef",
    {
        "ChaincodeLogs": NotRequired["LogConfigurationsTypeDef"],
        "PeerLogs": NotRequired["LogConfigurationsTypeDef"],
    },
)

NodeFrameworkAttributesTypeDef = TypedDict(
    "NodeFrameworkAttributesTypeDef",
    {
        "Fabric": NotRequired["NodeFabricAttributesTypeDef"],
        "Ethereum": NotRequired["NodeEthereumAttributesTypeDef"],
    },
)

NodeLogPublishingConfigurationTypeDef = TypedDict(
    "NodeLogPublishingConfigurationTypeDef",
    {
        "Fabric": NotRequired["NodeFabricLogPublishingConfigurationTypeDef"],
    },
)

NodeSummaryTypeDef = TypedDict(
    "NodeSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "Status": NotRequired[NodeStatusType],
        "CreationDate": NotRequired[datetime],
        "AvailabilityZone": NotRequired[str],
        "InstanceType": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

NodeTypeDef = TypedDict(
    "NodeTypeDef",
    {
        "NetworkId": NotRequired[str],
        "MemberId": NotRequired[str],
        "Id": NotRequired[str],
        "InstanceType": NotRequired[str],
        "AvailabilityZone": NotRequired[str],
        "FrameworkAttributes": NotRequired["NodeFrameworkAttributesTypeDef"],
        "LogPublishingConfiguration": NotRequired["NodeLogPublishingConfigurationTypeDef"],
        "StateDB": NotRequired[StateDBTypeType],
        "Status": NotRequired[NodeStatusType],
        "CreationDate": NotRequired[datetime],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
        "KmsKeyArn": NotRequired[str],
    },
)

ProposalActionsTypeDef = TypedDict(
    "ProposalActionsTypeDef",
    {
        "Invitations": NotRequired[Sequence["InviteActionTypeDef"]],
        "Removals": NotRequired[Sequence["RemoveActionTypeDef"]],
    },
)

ProposalSummaryTypeDef = TypedDict(
    "ProposalSummaryTypeDef",
    {
        "ProposalId": NotRequired[str],
        "Description": NotRequired[str],
        "ProposedByMemberId": NotRequired[str],
        "ProposedByMemberName": NotRequired[str],
        "Status": NotRequired[ProposalStatusType],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "Arn": NotRequired[str],
    },
)

ProposalTypeDef = TypedDict(
    "ProposalTypeDef",
    {
        "ProposalId": NotRequired[str],
        "NetworkId": NotRequired[str],
        "Description": NotRequired[str],
        "Actions": NotRequired["ProposalActionsTypeDef"],
        "ProposedByMemberId": NotRequired[str],
        "ProposedByMemberName": NotRequired[str],
        "Status": NotRequired[ProposalStatusType],
        "CreationDate": NotRequired[datetime],
        "ExpirationDate": NotRequired[datetime],
        "YesVoteCount": NotRequired[int],
        "NoVoteCount": NotRequired[int],
        "OutstandingVoteCount": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "Arn": NotRequired[str],
    },
)

RejectInvitationInputRequestTypeDef = TypedDict(
    "RejectInvitationInputRequestTypeDef",
    {
        "InvitationId": str,
    },
)

RemoveActionTypeDef = TypedDict(
    "RemoveActionTypeDef",
    {
        "MemberId": str,
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

UpdateMemberInputRequestTypeDef = TypedDict(
    "UpdateMemberInputRequestTypeDef",
    {
        "NetworkId": str,
        "MemberId": str,
        "LogPublishingConfiguration": NotRequired["MemberLogPublishingConfigurationTypeDef"],
    },
)

UpdateNodeInputRequestTypeDef = TypedDict(
    "UpdateNodeInputRequestTypeDef",
    {
        "NetworkId": str,
        "NodeId": str,
        "MemberId": NotRequired[str],
        "LogPublishingConfiguration": NotRequired["NodeLogPublishingConfigurationTypeDef"],
    },
)

VoteOnProposalInputRequestTypeDef = TypedDict(
    "VoteOnProposalInputRequestTypeDef",
    {
        "NetworkId": str,
        "ProposalId": str,
        "VoterMemberId": str,
        "Vote": VoteValueType,
    },
)

VoteSummaryTypeDef = TypedDict(
    "VoteSummaryTypeDef",
    {
        "Vote": NotRequired[VoteValueType],
        "MemberName": NotRequired[str],
        "MemberId": NotRequired[str],
    },
)

VotingPolicyTypeDef = TypedDict(
    "VotingPolicyTypeDef",
    {
        "ApprovalThresholdPolicy": NotRequired["ApprovalThresholdPolicyTypeDef"],
    },
)
