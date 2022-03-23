"""
Type annotations for networkmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AttachmentStateType,
    AttachmentTypeType,
    ChangeActionType,
    ChangeSetStateType,
    ChangeTypeType,
    ConnectionStateType,
    ConnectionStatusType,
    ConnectionTypeType,
    ConnectPeerAssociationStateType,
    ConnectPeerStateType,
    CoreNetworkPolicyAliasType,
    CoreNetworkStateType,
    CustomerGatewayAssociationStateType,
    DeviceStateType,
    GlobalNetworkStateType,
    LinkAssociationStateType,
    LinkStateType,
    RouteAnalysisCompletionReasonCodeType,
    RouteAnalysisCompletionResultCodeType,
    RouteAnalysisStatusType,
    RouteStateType,
    RouteTableTypeType,
    RouteTypeType,
    SiteStateType,
    TransitGatewayConnectPeerAssociationStateType,
    TransitGatewayRegistrationStateType,
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
    "AWSLocationTypeDef",
    "AcceptAttachmentRequestRequestTypeDef",
    "AcceptAttachmentResponseTypeDef",
    "AssociateConnectPeerRequestRequestTypeDef",
    "AssociateConnectPeerResponseTypeDef",
    "AssociateCustomerGatewayRequestRequestTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkRequestRequestTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "AttachmentTypeDef",
    "BandwidthTypeDef",
    "BgpOptionsTypeDef",
    "ConnectAttachmentOptionsTypeDef",
    "ConnectAttachmentTypeDef",
    "ConnectPeerAssociationTypeDef",
    "ConnectPeerBgpConfigurationTypeDef",
    "ConnectPeerConfigurationTypeDef",
    "ConnectPeerSummaryTypeDef",
    "ConnectPeerTypeDef",
    "ConnectionHealthTypeDef",
    "ConnectionTypeDef",
    "CoreNetworkChangeTypeDef",
    "CoreNetworkChangeValuesTypeDef",
    "CoreNetworkEdgeTypeDef",
    "CoreNetworkPolicyErrorTypeDef",
    "CoreNetworkPolicyTypeDef",
    "CoreNetworkPolicyVersionTypeDef",
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    "CoreNetworkSegmentTypeDef",
    "CoreNetworkSummaryTypeDef",
    "CoreNetworkTypeDef",
    "CreateConnectAttachmentRequestRequestTypeDef",
    "CreateConnectAttachmentResponseTypeDef",
    "CreateConnectPeerRequestRequestTypeDef",
    "CreateConnectPeerResponseTypeDef",
    "CreateConnectionRequestRequestTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateCoreNetworkRequestRequestTypeDef",
    "CreateCoreNetworkResponseTypeDef",
    "CreateDeviceRequestRequestTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkRequestRequestTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkRequestRequestTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteRequestRequestTypeDef",
    "CreateSiteResponseTypeDef",
    "CreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    "CreateVpcAttachmentRequestRequestTypeDef",
    "CreateVpcAttachmentResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteAttachmentRequestRequestTypeDef",
    "DeleteAttachmentResponseTypeDef",
    "DeleteConnectPeerRequestRequestTypeDef",
    "DeleteConnectPeerResponseTypeDef",
    "DeleteConnectionRequestRequestTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    "DeleteCoreNetworkRequestRequestTypeDef",
    "DeleteCoreNetworkResponseTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkRequestRequestTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkRequestRequestTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSiteRequestRequestTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayRequestRequestTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksRequestRequestTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateConnectPeerRequestRequestTypeDef",
    "DisassociateConnectPeerResponseTypeDef",
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkRequestRequestTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    "GetConnectAttachmentRequestRequestTypeDef",
    "GetConnectAttachmentResponseTypeDef",
    "GetConnectPeerAssociationsRequestRequestTypeDef",
    "GetConnectPeerAssociationsResponseTypeDef",
    "GetConnectPeerRequestRequestTypeDef",
    "GetConnectPeerResponseTypeDef",
    "GetConnectionsRequestRequestTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCoreNetworkChangeSetRequestRequestTypeDef",
    "GetCoreNetworkChangeSetResponseTypeDef",
    "GetCoreNetworkPolicyRequestRequestTypeDef",
    "GetCoreNetworkPolicyResponseTypeDef",
    "GetCoreNetworkRequestRequestTypeDef",
    "GetCoreNetworkResponseTypeDef",
    "GetCustomerGatewayAssociationsRequestRequestTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesRequestRequestTypeDef",
    "GetDevicesResponseTypeDef",
    "GetLinkAssociationsRequestRequestTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksRequestRequestTypeDef",
    "GetLinksResponseTypeDef",
    "GetNetworkResourceCountsRequestRequestTypeDef",
    "GetNetworkResourceCountsResponseTypeDef",
    "GetNetworkResourceRelationshipsRequestRequestTypeDef",
    "GetNetworkResourceRelationshipsResponseTypeDef",
    "GetNetworkResourcesRequestRequestTypeDef",
    "GetNetworkResourcesResponseTypeDef",
    "GetNetworkRoutesRequestRequestTypeDef",
    "GetNetworkRoutesResponseTypeDef",
    "GetNetworkTelemetryRequestRequestTypeDef",
    "GetNetworkTelemetryResponseTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetRouteAnalysisRequestRequestTypeDef",
    "GetRouteAnalysisResponseTypeDef",
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    "GetSitesRequestRequestTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GetVpcAttachmentRequestRequestTypeDef",
    "GetVpcAttachmentResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListAttachmentsRequestRequestTypeDef",
    "ListAttachmentsResponseTypeDef",
    "ListConnectPeersRequestRequestTypeDef",
    "ListConnectPeersResponseTypeDef",
    "ListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    "ListCoreNetworksRequestRequestTypeDef",
    "ListCoreNetworksResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkResourceCountTypeDef",
    "NetworkResourceSummaryTypeDef",
    "NetworkResourceTypeDef",
    "NetworkRouteDestinationTypeDef",
    "NetworkRouteTypeDef",
    "NetworkTelemetryTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "ProposedSegmentChangeTypeDef",
    "PutCoreNetworkPolicyRequestRequestTypeDef",
    "PutCoreNetworkPolicyResponseTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "RegisterTransitGatewayRequestRequestTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "RejectAttachmentRequestRequestTypeDef",
    "RejectAttachmentResponseTypeDef",
    "RelationshipTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    "RouteAnalysisCompletionTypeDef",
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    "RouteAnalysisEndpointOptionsTypeDef",
    "RouteAnalysisPathTypeDef",
    "RouteAnalysisTypeDef",
    "RouteTableIdentifierTypeDef",
    "SiteToSiteVpnAttachmentTypeDef",
    "SiteTypeDef",
    "StartRouteAnalysisRequestRequestTypeDef",
    "StartRouteAnalysisResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateConnectionRequestRequestTypeDef",
    "UpdateConnectionResponseTypeDef",
    "UpdateCoreNetworkRequestRequestTypeDef",
    "UpdateCoreNetworkResponseTypeDef",
    "UpdateDeviceRequestRequestTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateGlobalNetworkRequestRequestTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkRequestRequestTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    "UpdateNetworkResourceMetadataResponseTypeDef",
    "UpdateSiteRequestRequestTypeDef",
    "UpdateSiteResponseTypeDef",
    "UpdateVpcAttachmentRequestRequestTypeDef",
    "UpdateVpcAttachmentResponseTypeDef",
    "VpcAttachmentTypeDef",
    "VpcOptionsTypeDef",
)

AWSLocationTypeDef = TypedDict(
    "AWSLocationTypeDef",
    {
        "Zone": NotRequired[str],
        "SubnetArn": NotRequired[str],
    },
)

AcceptAttachmentRequestRequestTypeDef = TypedDict(
    "AcceptAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

AcceptAttachmentResponseTypeDef = TypedDict(
    "AcceptAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateConnectPeerRequestRequestTypeDef = TypedDict(
    "AssociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)

AssociateConnectPeerResponseTypeDef = TypedDict(
    "AssociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": "ConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "AssociateCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayArn": str,
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)

AssociateCustomerGatewayResponseTypeDef = TypedDict(
    "AssociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateLinkRequestRequestTypeDef = TypedDict(
    "AssociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

AssociateLinkResponseTypeDef = TypedDict(
    "AssociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
        "DeviceId": str,
        "LinkId": NotRequired[str],
    },
)

AssociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "AttachmentType": NotRequired[AttachmentTypeType],
        "State": NotRequired[AttachmentStateType],
        "EdgeLocation": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "AttachmentPolicyRuleNumber": NotRequired[int],
        "SegmentName": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
        "ProposedSegmentChange": NotRequired["ProposedSegmentChangeTypeDef"],
        "CreatedAt": NotRequired[datetime],
        "UpdatedAt": NotRequired[datetime],
    },
)

BandwidthTypeDef = TypedDict(
    "BandwidthTypeDef",
    {
        "UploadSpeed": NotRequired[int],
        "DownloadSpeed": NotRequired[int],
    },
)

BgpOptionsTypeDef = TypedDict(
    "BgpOptionsTypeDef",
    {
        "PeerAsn": NotRequired[int],
    },
)

ConnectAttachmentOptionsTypeDef = TypedDict(
    "ConnectAttachmentOptionsTypeDef",
    {
        "Protocol": NotRequired[Literal["GRE"]],
    },
)

ConnectAttachmentTypeDef = TypedDict(
    "ConnectAttachmentTypeDef",
    {
        "Attachment": NotRequired["AttachmentTypeDef"],
        "TransportAttachmentId": NotRequired[str],
        "Options": NotRequired["ConnectAttachmentOptionsTypeDef"],
    },
)

ConnectPeerAssociationTypeDef = TypedDict(
    "ConnectPeerAssociationTypeDef",
    {
        "ConnectPeerId": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[ConnectPeerAssociationStateType],
    },
)

ConnectPeerBgpConfigurationTypeDef = TypedDict(
    "ConnectPeerBgpConfigurationTypeDef",
    {
        "CoreNetworkAsn": NotRequired[int],
        "PeerAsn": NotRequired[int],
        "CoreNetworkAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
    },
)

ConnectPeerConfigurationTypeDef = TypedDict(
    "ConnectPeerConfigurationTypeDef",
    {
        "CoreNetworkAddress": NotRequired[str],
        "PeerAddress": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "Protocol": NotRequired[Literal["GRE"]],
        "BgpConfigurations": NotRequired[List["ConnectPeerBgpConfigurationTypeDef"]],
    },
)

ConnectPeerSummaryTypeDef = TypedDict(
    "ConnectPeerSummaryTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "ConnectPeerId": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "ConnectPeerState": NotRequired[ConnectPeerStateType],
        "CreatedAt": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ConnectPeerTypeDef = TypedDict(
    "ConnectPeerTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "ConnectPeerId": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[ConnectPeerStateType],
        "CreatedAt": NotRequired[datetime],
        "Configuration": NotRequired["ConnectPeerConfigurationTypeDef"],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ConnectionHealthTypeDef = TypedDict(
    "ConnectionHealthTypeDef",
    {
        "Type": NotRequired[ConnectionTypeType],
        "Status": NotRequired[ConnectionStatusType],
        "Timestamp": NotRequired[datetime],
    },
)

ConnectionTypeDef = TypedDict(
    "ConnectionTypeDef",
    {
        "ConnectionId": NotRequired[str],
        "ConnectionArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "ConnectedDeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[ConnectionStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CoreNetworkChangeTypeDef = TypedDict(
    "CoreNetworkChangeTypeDef",
    {
        "Type": NotRequired[ChangeTypeType],
        "Action": NotRequired[ChangeActionType],
        "Identifier": NotRequired[str],
        "PreviousValues": NotRequired["CoreNetworkChangeValuesTypeDef"],
        "NewValues": NotRequired["CoreNetworkChangeValuesTypeDef"],
    },
)

CoreNetworkChangeValuesTypeDef = TypedDict(
    "CoreNetworkChangeValuesTypeDef",
    {
        "SegmentName": NotRequired[str],
        "EdgeLocations": NotRequired[List[str]],
        "Asn": NotRequired[int],
        "Cidr": NotRequired[str],
        "DestinationIdentifier": NotRequired[str],
        "InsideCidrBlocks": NotRequired[List[str]],
        "SharedSegments": NotRequired[List[str]],
    },
)

CoreNetworkEdgeTypeDef = TypedDict(
    "CoreNetworkEdgeTypeDef",
    {
        "EdgeLocation": NotRequired[str],
        "Asn": NotRequired[int],
        "InsideCidrBlocks": NotRequired[List[str]],
    },
)

CoreNetworkPolicyErrorTypeDef = TypedDict(
    "CoreNetworkPolicyErrorTypeDef",
    {
        "ErrorCode": str,
        "Message": str,
        "Path": NotRequired[str],
    },
)

CoreNetworkPolicyTypeDef = TypedDict(
    "CoreNetworkPolicyTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ChangeSetState": NotRequired[ChangeSetStateType],
        "PolicyErrors": NotRequired[List["CoreNetworkPolicyErrorTypeDef"]],
        "PolicyDocument": NotRequired[str],
    },
)

CoreNetworkPolicyVersionTypeDef = TypedDict(
    "CoreNetworkPolicyVersionTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "ChangeSetState": NotRequired[ChangeSetStateType],
    },
)

CoreNetworkSegmentEdgeIdentifierTypeDef = TypedDict(
    "CoreNetworkSegmentEdgeIdentifierTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "SegmentName": NotRequired[str],
        "EdgeLocation": NotRequired[str],
    },
)

CoreNetworkSegmentTypeDef = TypedDict(
    "CoreNetworkSegmentTypeDef",
    {
        "Name": NotRequired[str],
        "EdgeLocations": NotRequired[List[str]],
        "SharedSegments": NotRequired[List[str]],
    },
)

CoreNetworkSummaryTypeDef = TypedDict(
    "CoreNetworkSummaryTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "State": NotRequired[CoreNetworkStateType],
        "Description": NotRequired[str],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CoreNetworkTypeDef = TypedDict(
    "CoreNetworkTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "CoreNetworkArn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[CoreNetworkStateType],
        "Segments": NotRequired[List["CoreNetworkSegmentTypeDef"]],
        "Edges": NotRequired[List["CoreNetworkEdgeTypeDef"]],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

CreateConnectAttachmentRequestRequestTypeDef = TypedDict(
    "CreateConnectAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "EdgeLocation": str,
        "TransportAttachmentId": str,
        "Options": "ConnectAttachmentOptionsTypeDef",
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateConnectAttachmentResponseTypeDef = TypedDict(
    "CreateConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": "ConnectAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectPeerRequestRequestTypeDef = TypedDict(
    "CreateConnectPeerRequestRequestTypeDef",
    {
        "ConnectAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": Sequence[str],
        "CoreNetworkAddress": NotRequired[str],
        "BgpOptions": NotRequired["BgpOptionsTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateConnectPeerResponseTypeDef = TypedDict(
    "CreateConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConnectionRequestRequestTypeDef = TypedDict(
    "CreateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "ConnectedDeviceId": str,
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateConnectionResponseTypeDef = TypedDict(
    "CreateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCoreNetworkRequestRequestTypeDef = TypedDict(
    "CreateCoreNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "PolicyDocument": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

CreateCoreNetworkResponseTypeDef = TypedDict(
    "CreateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceRequestRequestTypeDef = TypedDict(
    "CreateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "AWSLocation": NotRequired["AWSLocationTypeDef"],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
        "SiteId": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDeviceResponseTypeDef = TypedDict(
    "CreateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "CreateGlobalNetworkRequestRequestTypeDef",
    {
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGlobalNetworkResponseTypeDef = TypedDict(
    "CreateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateLinkRequestRequestTypeDef = TypedDict(
    "CreateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Bandwidth": "BandwidthTypeDef",
        "SiteId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateLinkResponseTypeDef = TypedDict(
    "CreateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSiteRequestRequestTypeDef = TypedDict(
    "CreateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSiteResponseTypeDef = TypedDict(
    "CreateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "CreateSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpnConnectionArn": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "CreateSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": "SiteToSiteVpnAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "CreateVpcAttachmentRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "VpcArn": str,
        "SubnetArns": Sequence[str],
        "Options": NotRequired["VpcOptionsTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientToken": NotRequired[str],
    },
)

CreateVpcAttachmentResponseTypeDef = TypedDict(
    "CreateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomerGatewayAssociationTypeDef = TypedDict(
    "CustomerGatewayAssociationTypeDef",
    {
        "CustomerGatewayArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[CustomerGatewayAssociationStateType],
    },
)

DeleteAttachmentRequestRequestTypeDef = TypedDict(
    "DeleteAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

DeleteAttachmentResponseTypeDef = TypedDict(
    "DeleteAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectPeerRequestRequestTypeDef = TypedDict(
    "DeleteConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)

DeleteConnectPeerResponseTypeDef = TypedDict(
    "DeleteConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteConnectionRequestRequestTypeDef = TypedDict(
    "DeleteConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
    },
)

DeleteConnectionResponseTypeDef = TypedDict(
    "DeleteConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

DeleteCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "DeleteCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteCoreNetworkRequestRequestTypeDef = TypedDict(
    "DeleteCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)

DeleteCoreNetworkResponseTypeDef = TypedDict(
    "DeleteCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
    },
)

DeleteDeviceResponseTypeDef = TypedDict(
    "DeleteDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGlobalNetworkRequestRequestTypeDef = TypedDict(
    "DeleteGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
    },
)

DeleteGlobalNetworkResponseTypeDef = TypedDict(
    "DeleteGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLinkRequestRequestTypeDef = TypedDict(
    "DeleteLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
    },
)

DeleteLinkResponseTypeDef = TypedDict(
    "DeleteLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

DeleteSiteRequestRequestTypeDef = TypedDict(
    "DeleteSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
    },
)

DeleteSiteResponseTypeDef = TypedDict(
    "DeleteSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

DeregisterTransitGatewayResponseTypeDef = TypedDict(
    "DeregisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGlobalNetworksRequestRequestTypeDef = TypedDict(
    "DescribeGlobalNetworksRequestRequestTypeDef",
    {
        "GlobalNetworkIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

DescribeGlobalNetworksResponseTypeDef = TypedDict(
    "DescribeGlobalNetworksResponseTypeDef",
    {
        "GlobalNetworks": List["GlobalNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": NotRequired[str],
        "DeviceArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "AWSLocation": NotRequired["AWSLocationTypeDef"],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
        "SiteId": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[DeviceStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

DisassociateConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerId": str,
    },
)

DisassociateConnectPeerResponseTypeDef = TypedDict(
    "DisassociateConnectPeerResponseTypeDef",
    {
        "ConnectPeerAssociation": "ConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "DisassociateCustomerGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArn": str,
    },
)

DisassociateCustomerGatewayResponseTypeDef = TypedDict(
    "DisassociateCustomerGatewayResponseTypeDef",
    {
        "CustomerGatewayAssociation": "CustomerGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateLinkRequestRequestTypeDef = TypedDict(
    "DisassociateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "LinkId": str,
    },
)

DisassociateLinkResponseTypeDef = TypedDict(
    "DisassociateLinkResponseTypeDef",
    {
        "LinkAssociation": "LinkAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArn": str,
    },
)

DisassociateTransitGatewayConnectPeerResponseTypeDef = TypedDict(
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociation": "TransitGatewayConnectPeerAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExecuteCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "ExecuteCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

GetConnectAttachmentRequestRequestTypeDef = TypedDict(
    "GetConnectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetConnectAttachmentResponseTypeDef = TypedDict(
    "GetConnectAttachmentResponseTypeDef",
    {
        "ConnectAttachment": "ConnectAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "GetConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectPeerIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetConnectPeerAssociationsResponseTypeDef",
    {
        "ConnectPeerAssociations": List["ConnectPeerAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectPeerRequestRequestTypeDef = TypedDict(
    "GetConnectPeerRequestRequestTypeDef",
    {
        "ConnectPeerId": str,
    },
)

GetConnectPeerResponseTypeDef = TypedDict(
    "GetConnectPeerResponseTypeDef",
    {
        "ConnectPeer": "ConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConnectionsRequestRequestTypeDef = TypedDict(
    "GetConnectionsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionIds": NotRequired[Sequence[str]],
        "DeviceId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetConnectionsResponseTypeDef = TypedDict(
    "GetConnectionsResponseTypeDef",
    {
        "Connections": List["ConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreNetworkChangeSetRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkChangeSetRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetCoreNetworkChangeSetResponseTypeDef = TypedDict(
    "GetCoreNetworkChangeSetResponseTypeDef",
    {
        "CoreNetworkChanges": List["CoreNetworkChangeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": NotRequired[int],
        "Alias": NotRequired[CoreNetworkPolicyAliasType],
    },
)

GetCoreNetworkPolicyResponseTypeDef = TypedDict(
    "GetCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCoreNetworkRequestRequestTypeDef = TypedDict(
    "GetCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
    },
)

GetCoreNetworkResponseTypeDef = TypedDict(
    "GetCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetCustomerGatewayAssociationsRequestRequestTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CustomerGatewayArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetCustomerGatewayAssociationsResponseTypeDef = TypedDict(
    "GetCustomerGatewayAssociationsResponseTypeDef",
    {
        "CustomerGatewayAssociations": List["CustomerGatewayAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDevicesRequestRequestTypeDef = TypedDict(
    "GetDevicesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetDevicesResponseTypeDef = TypedDict(
    "GetDevicesResponseTypeDef",
    {
        "Devices": List["DeviceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLinkAssociationsRequestRequestTypeDef = TypedDict(
    "GetLinkAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetLinkAssociationsResponseTypeDef = TypedDict(
    "GetLinkAssociationsResponseTypeDef",
    {
        "LinkAssociations": List["LinkAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLinksRequestRequestTypeDef = TypedDict(
    "GetLinksRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkIds": NotRequired[Sequence[str]],
        "SiteId": NotRequired[str],
        "Type": NotRequired[str],
        "Provider": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetLinksResponseTypeDef = TypedDict(
    "GetLinksResponseTypeDef",
    {
        "Links": List["LinkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkResourceCountsRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceCountsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceType": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetNetworkResourceCountsResponseTypeDef = TypedDict(
    "GetNetworkResourceCountsResponseTypeDef",
    {
        "NetworkResourceCounts": List["NetworkResourceCountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkResourceRelationshipsRequestRequestTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetNetworkResourceRelationshipsResponseTypeDef = TypedDict(
    "GetNetworkResourceRelationshipsResponseTypeDef",
    {
        "Relationships": List["RelationshipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkResourcesRequestRequestTypeDef = TypedDict(
    "GetNetworkResourcesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetNetworkResourcesResponseTypeDef = TypedDict(
    "GetNetworkResourcesResponseTypeDef",
    {
        "NetworkResources": List["NetworkResourceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkRoutesRequestRequestTypeDef = TypedDict(
    "GetNetworkRoutesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteTableIdentifier": "RouteTableIdentifierTypeDef",
        "ExactCidrMatches": NotRequired[Sequence[str]],
        "LongestPrefixMatches": NotRequired[Sequence[str]],
        "SubnetOfMatches": NotRequired[Sequence[str]],
        "SupernetOfMatches": NotRequired[Sequence[str]],
        "PrefixListIds": NotRequired[Sequence[str]],
        "States": NotRequired[Sequence[RouteStateType]],
        "Types": NotRequired[Sequence[RouteTypeType]],
        "DestinationFilters": NotRequired[Mapping[str, Sequence[str]]],
    },
)

GetNetworkRoutesResponseTypeDef = TypedDict(
    "GetNetworkRoutesResponseTypeDef",
    {
        "RouteTableArn": str,
        "CoreNetworkSegmentEdge": "CoreNetworkSegmentEdgeIdentifierTypeDef",
        "RouteTableType": RouteTableTypeType,
        "RouteTableTimestamp": datetime,
        "NetworkRoutes": List["NetworkRouteTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkTelemetryRequestRequestTypeDef = TypedDict(
    "GetNetworkTelemetryRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "CoreNetworkId": NotRequired[str],
        "RegisteredGatewayArn": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetNetworkTelemetryResponseTypeDef = TypedDict(
    "GetNetworkTelemetryResponseTypeDef",
    {
        "NetworkTelemetry": List["NetworkTelemetryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRouteAnalysisRequestRequestTypeDef = TypedDict(
    "GetRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "RouteAnalysisId": str,
    },
)

GetRouteAnalysisResponseTypeDef = TypedDict(
    "GetRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": "RouteAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSiteToSiteVpnAttachmentRequestRequestTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetSiteToSiteVpnAttachmentResponseTypeDef = TypedDict(
    "GetSiteToSiteVpnAttachmentResponseTypeDef",
    {
        "SiteToSiteVpnAttachment": "SiteToSiteVpnAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSitesRequestRequestTypeDef = TypedDict(
    "GetSitesRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteIds": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetSitesResponseTypeDef = TypedDict(
    "GetSitesResponseTypeDef",
    {
        "Sites": List["SiteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayConnectPeerArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetTransitGatewayConnectPeerAssociationsResponseTypeDef = TypedDict(
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    {
        "TransitGatewayConnectPeerAssociations": List[
            "TransitGatewayConnectPeerAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTransitGatewayRegistrationsRequestRequestTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArns": NotRequired[Sequence[str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

GetTransitGatewayRegistrationsResponseTypeDef = TypedDict(
    "GetTransitGatewayRegistrationsResponseTypeDef",
    {
        "TransitGatewayRegistrations": List["TransitGatewayRegistrationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpcAttachmentRequestRequestTypeDef = TypedDict(
    "GetVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

GetVpcAttachmentResponseTypeDef = TypedDict(
    "GetVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GlobalNetworkTypeDef = TypedDict(
    "GlobalNetworkTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "GlobalNetworkArn": NotRequired[str],
        "Description": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[GlobalNetworkStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

LinkAssociationTypeDef = TypedDict(
    "LinkAssociationTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "LinkAssociationState": NotRequired[LinkAssociationStateType],
    },
)

LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": NotRequired[str],
        "LinkArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "SiteId": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired["BandwidthTypeDef"],
        "Provider": NotRequired[str],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[LinkStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

ListAttachmentsRequestRequestTypeDef = TypedDict(
    "ListAttachmentsRequestRequestTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "AttachmentType": NotRequired[AttachmentTypeType],
        "EdgeLocation": NotRequired[str],
        "State": NotRequired[AttachmentStateType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAttachmentsResponseTypeDef = TypedDict(
    "ListAttachmentsResponseTypeDef",
    {
        "Attachments": List["AttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConnectPeersRequestRequestTypeDef = TypedDict(
    "ListConnectPeersRequestRequestTypeDef",
    {
        "CoreNetworkId": NotRequired[str],
        "ConnectAttachmentId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListConnectPeersResponseTypeDef = TypedDict(
    "ListConnectPeersResponseTypeDef",
    {
        "ConnectPeers": List["ConnectPeerSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreNetworkPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCoreNetworkPolicyVersionsResponseTypeDef = TypedDict(
    "ListCoreNetworkPolicyVersionsResponseTypeDef",
    {
        "CoreNetworkPolicyVersions": List["CoreNetworkPolicyVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCoreNetworksRequestRequestTypeDef = TypedDict(
    "ListCoreNetworksRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCoreNetworksResponseTypeDef = TypedDict(
    "ListCoreNetworksResponseTypeDef",
    {
        "CoreNetworks": List["CoreNetworkSummaryTypeDef"],
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
        "TagList": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LocationTypeDef = TypedDict(
    "LocationTypeDef",
    {
        "Address": NotRequired[str],
        "Latitude": NotRequired[str],
        "Longitude": NotRequired[str],
    },
)

NetworkResourceCountTypeDef = TypedDict(
    "NetworkResourceCountTypeDef",
    {
        "ResourceType": NotRequired[str],
        "Count": NotRequired[int],
    },
)

NetworkResourceSummaryTypeDef = TypedDict(
    "NetworkResourceSummaryTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Definition": NotRequired[str],
        "NameTag": NotRequired[str],
        "IsMiddlebox": NotRequired[bool],
    },
)

NetworkResourceTypeDef = TypedDict(
    "NetworkResourceTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Definition": NotRequired[str],
        "DefinitionTimestamp": NotRequired[datetime],
        "Tags": NotRequired[List["TagTypeDef"]],
        "Metadata": NotRequired[Dict[str, str]],
    },
)

NetworkRouteDestinationTypeDef = TypedDict(
    "NetworkRouteDestinationTypeDef",
    {
        "CoreNetworkAttachmentId": NotRequired[str],
        "TransitGatewayAttachmentId": NotRequired[str],
        "SegmentName": NotRequired[str],
        "EdgeLocation": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
    },
)

NetworkRouteTypeDef = TypedDict(
    "NetworkRouteTypeDef",
    {
        "DestinationCidrBlock": NotRequired[str],
        "Destinations": NotRequired[List["NetworkRouteDestinationTypeDef"]],
        "PrefixListId": NotRequired[str],
        "State": NotRequired[RouteStateType],
        "Type": NotRequired[RouteTypeType],
    },
)

NetworkTelemetryTypeDef = TypedDict(
    "NetworkTelemetryTypeDef",
    {
        "RegisteredGatewayArn": NotRequired[str],
        "CoreNetworkId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "AccountId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceId": NotRequired[str],
        "ResourceArn": NotRequired[str],
        "Address": NotRequired[str],
        "Health": NotRequired["ConnectionHealthTypeDef"],
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

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "Sequence": NotRequired[int],
        "Resource": NotRequired["NetworkResourceSummaryTypeDef"],
        "DestinationCidrBlock": NotRequired[str],
    },
)

ProposedSegmentChangeTypeDef = TypedDict(
    "ProposedSegmentChangeTypeDef",
    {
        "Tags": NotRequired[List["TagTypeDef"]],
        "AttachmentPolicyRuleNumber": NotRequired[int],
        "SegmentName": NotRequired[str],
    },
)

PutCoreNetworkPolicyRequestRequestTypeDef = TypedDict(
    "PutCoreNetworkPolicyRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyDocument": str,
        "Description": NotRequired[str],
        "LatestVersionId": NotRequired[int],
        "ClientToken": NotRequired[str],
    },
)

PutCoreNetworkPolicyResponseTypeDef = TypedDict(
    "PutCoreNetworkPolicyResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyDocument": str,
        "ResourceArn": str,
    },
)

RegisterTransitGatewayRequestRequestTypeDef = TypedDict(
    "RegisterTransitGatewayRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "TransitGatewayArn": str,
    },
)

RegisterTransitGatewayResponseTypeDef = TypedDict(
    "RegisterTransitGatewayResponseTypeDef",
    {
        "TransitGatewayRegistration": "TransitGatewayRegistrationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectAttachmentRequestRequestTypeDef = TypedDict(
    "RejectAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)

RejectAttachmentResponseTypeDef = TypedDict(
    "RejectAttachmentResponseTypeDef",
    {
        "Attachment": "AttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RelationshipTypeDef = TypedDict(
    "RelationshipTypeDef",
    {
        "From": NotRequired[str],
        "To": NotRequired[str],
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

RestoreCoreNetworkPolicyVersionRequestRequestTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "PolicyVersionId": int,
    },
)

RestoreCoreNetworkPolicyVersionResponseTypeDef = TypedDict(
    "RestoreCoreNetworkPolicyVersionResponseTypeDef",
    {
        "CoreNetworkPolicy": "CoreNetworkPolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteAnalysisCompletionTypeDef = TypedDict(
    "RouteAnalysisCompletionTypeDef",
    {
        "ResultCode": NotRequired[RouteAnalysisCompletionResultCodeType],
        "ReasonCode": NotRequired[RouteAnalysisCompletionReasonCodeType],
        "ReasonContext": NotRequired[Dict[str, str]],
    },
)

RouteAnalysisEndpointOptionsSpecificationTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsSpecificationTypeDef",
    {
        "TransitGatewayAttachmentArn": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)

RouteAnalysisEndpointOptionsTypeDef = TypedDict(
    "RouteAnalysisEndpointOptionsTypeDef",
    {
        "TransitGatewayAttachmentArn": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "IpAddress": NotRequired[str],
    },
)

RouteAnalysisPathTypeDef = TypedDict(
    "RouteAnalysisPathTypeDef",
    {
        "CompletionStatus": NotRequired["RouteAnalysisCompletionTypeDef"],
        "Path": NotRequired[List["PathComponentTypeDef"]],
    },
)

RouteAnalysisTypeDef = TypedDict(
    "RouteAnalysisTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "OwnerAccountId": NotRequired[str],
        "RouteAnalysisId": NotRequired[str],
        "StartTimestamp": NotRequired[datetime],
        "Status": NotRequired[RouteAnalysisStatusType],
        "Source": NotRequired["RouteAnalysisEndpointOptionsTypeDef"],
        "Destination": NotRequired["RouteAnalysisEndpointOptionsTypeDef"],
        "IncludeReturnPath": NotRequired[bool],
        "UseMiddleboxes": NotRequired[bool],
        "ForwardPath": NotRequired["RouteAnalysisPathTypeDef"],
        "ReturnPath": NotRequired["RouteAnalysisPathTypeDef"],
    },
)

RouteTableIdentifierTypeDef = TypedDict(
    "RouteTableIdentifierTypeDef",
    {
        "TransitGatewayRouteTableArn": NotRequired[str],
        "CoreNetworkSegmentEdge": NotRequired["CoreNetworkSegmentEdgeIdentifierTypeDef"],
    },
)

SiteToSiteVpnAttachmentTypeDef = TypedDict(
    "SiteToSiteVpnAttachmentTypeDef",
    {
        "Attachment": NotRequired["AttachmentTypeDef"],
        "VpnConnectionArn": NotRequired[str],
    },
)

SiteTypeDef = TypedDict(
    "SiteTypeDef",
    {
        "SiteId": NotRequired[str],
        "SiteArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "Description": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
        "CreatedAt": NotRequired[datetime],
        "State": NotRequired[SiteStateType],
        "Tags": NotRequired[List["TagTypeDef"]],
    },
)

StartRouteAnalysisRequestRequestTypeDef = TypedDict(
    "StartRouteAnalysisRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Source": "RouteAnalysisEndpointOptionsSpecificationTypeDef",
        "Destination": "RouteAnalysisEndpointOptionsSpecificationTypeDef",
        "IncludeReturnPath": NotRequired[bool],
        "UseMiddleboxes": NotRequired[bool],
    },
)

StartRouteAnalysisResponseTypeDef = TypedDict(
    "StartRouteAnalysisResponseTypeDef",
    {
        "RouteAnalysis": "RouteAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

TransitGatewayConnectPeerAssociationTypeDef = TypedDict(
    "TransitGatewayConnectPeerAssociationTypeDef",
    {
        "TransitGatewayConnectPeerArn": NotRequired[str],
        "GlobalNetworkId": NotRequired[str],
        "DeviceId": NotRequired[str],
        "LinkId": NotRequired[str],
        "State": NotRequired[TransitGatewayConnectPeerAssociationStateType],
    },
)

TransitGatewayRegistrationStateReasonTypeDef = TypedDict(
    "TransitGatewayRegistrationStateReasonTypeDef",
    {
        "Code": NotRequired[TransitGatewayRegistrationStateType],
        "Message": NotRequired[str],
    },
)

TransitGatewayRegistrationTypeDef = TypedDict(
    "TransitGatewayRegistrationTypeDef",
    {
        "GlobalNetworkId": NotRequired[str],
        "TransitGatewayArn": NotRequired[str],
        "State": NotRequired["TransitGatewayRegistrationStateReasonTypeDef"],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateConnectionRequestRequestTypeDef = TypedDict(
    "UpdateConnectionRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ConnectionId": str,
        "LinkId": NotRequired[str],
        "ConnectedLinkId": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateConnectionResponseTypeDef = TypedDict(
    "UpdateConnectionResponseTypeDef",
    {
        "Connection": "ConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCoreNetworkRequestRequestTypeDef = TypedDict(
    "UpdateCoreNetworkRequestRequestTypeDef",
    {
        "CoreNetworkId": str,
        "Description": NotRequired[str],
    },
)

UpdateCoreNetworkResponseTypeDef = TypedDict(
    "UpdateCoreNetworkResponseTypeDef",
    {
        "CoreNetwork": "CoreNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateDeviceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "DeviceId": str,
        "AWSLocation": NotRequired["AWSLocationTypeDef"],
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Vendor": NotRequired[str],
        "Model": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
        "SiteId": NotRequired[str],
    },
)

UpdateDeviceResponseTypeDef = TypedDict(
    "UpdateDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalNetworkRequestRequestTypeDef = TypedDict(
    "UpdateGlobalNetworkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "Description": NotRequired[str],
    },
)

UpdateGlobalNetworkResponseTypeDef = TypedDict(
    "UpdateGlobalNetworkResponseTypeDef",
    {
        "GlobalNetwork": "GlobalNetworkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateLinkRequestRequestTypeDef = TypedDict(
    "UpdateLinkRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "LinkId": str,
        "Description": NotRequired[str],
        "Type": NotRequired[str],
        "Bandwidth": NotRequired["BandwidthTypeDef"],
        "Provider": NotRequired[str],
    },
)

UpdateLinkResponseTypeDef = TypedDict(
    "UpdateLinkResponseTypeDef",
    {
        "Link": "LinkTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNetworkResourceMetadataRequestRequestTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "ResourceArn": str,
        "Metadata": Mapping[str, str],
    },
)

UpdateNetworkResourceMetadataResponseTypeDef = TypedDict(
    "UpdateNetworkResourceMetadataResponseTypeDef",
    {
        "ResourceArn": str,
        "Metadata": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSiteRequestRequestTypeDef = TypedDict(
    "UpdateSiteRequestRequestTypeDef",
    {
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": NotRequired[str],
        "Location": NotRequired["LocationTypeDef"],
    },
)

UpdateSiteResponseTypeDef = TypedDict(
    "UpdateSiteResponseTypeDef",
    {
        "Site": "SiteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVpcAttachmentRequestRequestTypeDef = TypedDict(
    "UpdateVpcAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "AddSubnetArns": NotRequired[Sequence[str]],
        "RemoveSubnetArns": NotRequired[Sequence[str]],
        "Options": NotRequired["VpcOptionsTypeDef"],
    },
)

UpdateVpcAttachmentResponseTypeDef = TypedDict(
    "UpdateVpcAttachmentResponseTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "Attachment": NotRequired["AttachmentTypeDef"],
        "SubnetArns": NotRequired[List[str]],
        "Options": NotRequired["VpcOptionsTypeDef"],
    },
)

VpcOptionsTypeDef = TypedDict(
    "VpcOptionsTypeDef",
    {
        "Ipv6Support": NotRequired[bool],
    },
)
