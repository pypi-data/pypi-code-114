"""
Type annotations for globalaccelerator service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/type_defs.html)

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    AcceleratorStatusType,
    ByoipCidrStateType,
    ClientAffinityType,
    CustomRoutingAcceleratorStatusType,
    CustomRoutingDestinationTrafficStateType,
    CustomRoutingProtocolType,
    HealthCheckProtocolType,
    HealthStateType,
    ProtocolType,
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
    "AcceleratorAttributesTypeDef",
    "AcceleratorTypeDef",
    "AddCustomRoutingEndpointsRequestRequestTypeDef",
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AdvertiseByoipCidrRequestRequestTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "AllowCustomRoutingTrafficRequestRequestTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorRequestRequestTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCustomRoutingAcceleratorRequestRequestTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupRequestRequestTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerRequestRequestTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupRequestRequestTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerRequestRequestTypeDef",
    "CreateListenerResponseTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeleteAcceleratorRequestRequestTypeDef",
    "DeleteCustomRoutingAcceleratorRequestRequestTypeDef",
    "DeleteCustomRoutingEndpointGroupRequestRequestTypeDef",
    "DeleteCustomRoutingListenerRequestRequestTypeDef",
    "DeleteEndpointGroupRequestRequestTypeDef",
    "DeleteListenerRequestRequestTypeDef",
    "DenyCustomRoutingTrafficRequestRequestTypeDef",
    "DeprovisionByoipCidrRequestRequestTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesRequestRequestTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorRequestRequestTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorRequestRequestTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupRequestRequestTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerRequestRequestTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupRequestRequestTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerRequestRequestTypeDef",
    "DescribeListenerResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsRequestRequestTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsRequestRequestTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCustomRoutingAcceleratorsRequestRequestTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsRequestRequestTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersRequestRequestTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsRequestRequestTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsRequestRequestTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersRequestRequestTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrRequestRequestTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "RemoveCustomRoutingEndpointsRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SocketAddressTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAcceleratorAttributesRequestRequestTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorRequestRequestTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorRequestRequestTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerRequestRequestTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupRequestRequestTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerRequestRequestTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrRequestRequestTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
)

AcceleratorAttributesTypeDef = TypedDict(
    "AcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": NotRequired[bool],
        "FlowLogsS3Bucket": NotRequired[str],
        "FlowLogsS3Prefix": NotRequired[str],
    },
)

AcceleratorTypeDef = TypedDict(
    "AcceleratorTypeDef",
    {
        "AcceleratorArn": NotRequired[str],
        "Name": NotRequired[str],
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "Enabled": NotRequired[bool],
        "IpSets": NotRequired[List["IpSetTypeDef"]],
        "DnsName": NotRequired[str],
        "Status": NotRequired[AcceleratorStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

AddCustomRoutingEndpointsRequestRequestTypeDef = TypedDict(
    "AddCustomRoutingEndpointsRequestRequestTypeDef",
    {
        "EndpointConfigurations": Sequence["CustomRoutingEndpointConfigurationTypeDef"],
        "EndpointGroupArn": str,
    },
)

AddCustomRoutingEndpointsResponseTypeDef = TypedDict(
    "AddCustomRoutingEndpointsResponseTypeDef",
    {
        "EndpointDescriptions": List["CustomRoutingEndpointDescriptionTypeDef"],
        "EndpointGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "AdvertiseByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

AdvertiseByoipCidrResponseTypeDef = TypedDict(
    "AdvertiseByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllowCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "AllowCustomRoutingTrafficRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
        "DestinationAddresses": NotRequired[Sequence[str]],
        "DestinationPorts": NotRequired[Sequence[int]],
        "AllowAllTrafficToEndpoint": NotRequired[bool],
    },
)

ByoipCidrEventTypeDef = TypedDict(
    "ByoipCidrEventTypeDef",
    {
        "Message": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": NotRequired[str],
        "State": NotRequired[ByoipCidrStateType],
        "Events": NotRequired[List["ByoipCidrEventTypeDef"]],
    },
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

CreateAcceleratorRequestRequestTypeDef = TypedDict(
    "CreateAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "IpAddresses": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAcceleratorResponseTypeDef = TypedDict(
    "CreateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "Name": str,
        "IdempotencyToken": str,
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "IpAddresses": NotRequired[Sequence[str]],
        "Enabled": NotRequired[bool],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "DestinationConfigurations": Sequence["CustomRoutingDestinationConfigurationTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "CreateCustomRoutingListenerRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": Sequence["PortRangeTypeDef"],
        "IdempotencyToken": str,
    },
)

CreateCustomRoutingListenerResponseTypeDef = TypedDict(
    "CreateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndpointGroupRequestRequestTypeDef = TypedDict(
    "CreateEndpointGroupRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "EndpointGroupRegion": str,
        "IdempotencyToken": str,
        "EndpointConfigurations": NotRequired[Sequence["EndpointConfigurationTypeDef"]],
        "TrafficDialPercentage": NotRequired[float],
        "HealthCheckPort": NotRequired[int],
        "HealthCheckProtocol": NotRequired[HealthCheckProtocolType],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "ThresholdCount": NotRequired[int],
        "PortOverrides": NotRequired[Sequence["PortOverrideTypeDef"]],
    },
)

CreateEndpointGroupResponseTypeDef = TypedDict(
    "CreateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateListenerRequestRequestTypeDef = TypedDict(
    "CreateListenerRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "PortRanges": Sequence["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "IdempotencyToken": str,
        "ClientAffinity": NotRequired[ClientAffinityType],
    },
)

CreateListenerResponseTypeDef = TypedDict(
    "CreateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CustomRoutingAcceleratorAttributesTypeDef = TypedDict(
    "CustomRoutingAcceleratorAttributesTypeDef",
    {
        "FlowLogsEnabled": NotRequired[bool],
        "FlowLogsS3Bucket": NotRequired[str],
        "FlowLogsS3Prefix": NotRequired[str],
    },
)

CustomRoutingAcceleratorTypeDef = TypedDict(
    "CustomRoutingAcceleratorTypeDef",
    {
        "AcceleratorArn": NotRequired[str],
        "Name": NotRequired[str],
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "Enabled": NotRequired[bool],
        "IpSets": NotRequired[List["IpSetTypeDef"]],
        "DnsName": NotRequired[str],
        "Status": NotRequired[CustomRoutingAcceleratorStatusType],
        "CreatedTime": NotRequired[datetime],
        "LastModifiedTime": NotRequired[datetime],
    },
)

CustomRoutingDestinationConfigurationTypeDef = TypedDict(
    "CustomRoutingDestinationConfigurationTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
        "Protocols": Sequence[CustomRoutingProtocolType],
    },
)

CustomRoutingDestinationDescriptionTypeDef = TypedDict(
    "CustomRoutingDestinationDescriptionTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
        "Protocols": NotRequired[List[ProtocolType]],
    },
)

CustomRoutingEndpointConfigurationTypeDef = TypedDict(
    "CustomRoutingEndpointConfigurationTypeDef",
    {
        "EndpointId": NotRequired[str],
    },
)

CustomRoutingEndpointDescriptionTypeDef = TypedDict(
    "CustomRoutingEndpointDescriptionTypeDef",
    {
        "EndpointId": NotRequired[str],
    },
)

CustomRoutingEndpointGroupTypeDef = TypedDict(
    "CustomRoutingEndpointGroupTypeDef",
    {
        "EndpointGroupArn": NotRequired[str],
        "EndpointGroupRegion": NotRequired[str],
        "DestinationDescriptions": NotRequired[List["CustomRoutingDestinationDescriptionTypeDef"]],
        "EndpointDescriptions": NotRequired[List["CustomRoutingEndpointDescriptionTypeDef"]],
    },
)

CustomRoutingListenerTypeDef = TypedDict(
    "CustomRoutingListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "PortRanges": NotRequired[List["PortRangeTypeDef"]],
    },
)

DeleteAcceleratorRequestRequestTypeDef = TypedDict(
    "DeleteAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DeleteCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "DeleteCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DeleteEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DeleteListenerRequestRequestTypeDef = TypedDict(
    "DeleteListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DenyCustomRoutingTrafficRequestRequestTypeDef = TypedDict(
    "DenyCustomRoutingTrafficRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointId": str,
        "DestinationAddresses": NotRequired[Sequence[str]],
        "DestinationPorts": NotRequired[Sequence[int]],
        "DenyAllTrafficToEndpoint": NotRequired[bool],
    },
)

DeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "DeprovisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

DeprovisionByoipCidrResponseTypeDef = TypedDict(
    "DeprovisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAcceleratorRequestRequestTypeDef = TypedDict(
    "DescribeAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeAcceleratorResponseTypeDef = TypedDict(
    "DescribeAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
    },
)

DescribeCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingEndpointGroupRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeCustomRoutingEndpointGroupResponseTypeDef = TypedDict(
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "CustomRoutingEndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "DescribeCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeCustomRoutingListenerResponseTypeDef = TypedDict(
    "DescribeCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEndpointGroupRequestRequestTypeDef = TypedDict(
    "DescribeEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
    },
)

DescribeEndpointGroupResponseTypeDef = TypedDict(
    "DescribeEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeListenerRequestRequestTypeDef = TypedDict(
    "DescribeListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
    },
)

DescribeListenerResponseTypeDef = TypedDict(
    "DescribeListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationPortMappingTypeDef = TypedDict(
    "DestinationPortMappingTypeDef",
    {
        "AcceleratorArn": NotRequired[str],
        "AcceleratorSocketAddresses": NotRequired[List["SocketAddressTypeDef"]],
        "EndpointGroupArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "EndpointGroupRegion": NotRequired[str],
        "DestinationSocketAddress": NotRequired["SocketAddressTypeDef"],
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "DestinationTrafficState": NotRequired[CustomRoutingDestinationTrafficStateType],
    },
)

EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "EndpointId": NotRequired[str],
        "Weight": NotRequired[int],
        "ClientIPPreservationEnabled": NotRequired[bool],
    },
)

EndpointDescriptionTypeDef = TypedDict(
    "EndpointDescriptionTypeDef",
    {
        "EndpointId": NotRequired[str],
        "Weight": NotRequired[int],
        "HealthState": NotRequired[HealthStateType],
        "HealthReason": NotRequired[str],
        "ClientIPPreservationEnabled": NotRequired[bool],
    },
)

EndpointGroupTypeDef = TypedDict(
    "EndpointGroupTypeDef",
    {
        "EndpointGroupArn": NotRequired[str],
        "EndpointGroupRegion": NotRequired[str],
        "EndpointDescriptions": NotRequired[List["EndpointDescriptionTypeDef"]],
        "TrafficDialPercentage": NotRequired[float],
        "HealthCheckPort": NotRequired[int],
        "HealthCheckProtocol": NotRequired[HealthCheckProtocolType],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "ThresholdCount": NotRequired[int],
        "PortOverrides": NotRequired[List["PortOverrideTypeDef"]],
    },
)

IpSetTypeDef = TypedDict(
    "IpSetTypeDef",
    {
        "IpFamily": NotRequired[str],
        "IpAddresses": NotRequired[List[str]],
    },
)

ListAcceleratorsRequestRequestTypeDef = TypedDict(
    "ListAcceleratorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAcceleratorsResponseTypeDef = TypedDict(
    "ListAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["AcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListByoipCidrsRequestRequestTypeDef = TypedDict(
    "ListByoipCidrsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListByoipCidrsResponseTypeDef = TypedDict(
    "ListByoipCidrsResponseTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingAcceleratorsRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCustomRoutingAcceleratorsResponseTypeDef = TypedDict(
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    {
        "Accelerators": List["CustomRoutingAcceleratorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingEndpointGroupsRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCustomRoutingEndpointGroupsResponseTypeDef = TypedDict(
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["CustomRoutingEndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingListenersRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingListenersRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCustomRoutingListenersResponseTypeDef = TypedDict(
    "ListCustomRoutingListenersResponseTypeDef",
    {
        "Listeners": List["CustomRoutingListenerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationRequestRequestTypeDef",
    {
        "EndpointId": str,
        "DestinationAddress": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCustomRoutingPortMappingsByDestinationResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    {
        "DestinationPortMappings": List["DestinationPortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListCustomRoutingPortMappingsRequestRequestTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "EndpointGroupArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListCustomRoutingPortMappingsResponseTypeDef = TypedDict(
    "ListCustomRoutingPortMappingsResponseTypeDef",
    {
        "PortMappings": List["PortMappingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListEndpointGroupsRequestRequestTypeDef = TypedDict(
    "ListEndpointGroupsRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEndpointGroupsResponseTypeDef = TypedDict(
    "ListEndpointGroupsResponseTypeDef",
    {
        "EndpointGroups": List["EndpointGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListListenersRequestRequestTypeDef = TypedDict(
    "ListListenersRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListListenersResponseTypeDef = TypedDict(
    "ListListenersResponseTypeDef",
    {
        "Listeners": List["ListenerTypeDef"],
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
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": NotRequired[str],
        "PortRanges": NotRequired[List["PortRangeTypeDef"]],
        "Protocol": NotRequired[ProtocolType],
        "ClientAffinity": NotRequired[ClientAffinityType],
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

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {
        "AcceleratorPort": NotRequired[int],
        "EndpointGroupArn": NotRequired[str],
        "EndpointId": NotRequired[str],
        "DestinationSocketAddress": NotRequired["SocketAddressTypeDef"],
        "Protocols": NotRequired[List[CustomRoutingProtocolType]],
        "DestinationTrafficState": NotRequired[CustomRoutingDestinationTrafficStateType],
    },
)

PortOverrideTypeDef = TypedDict(
    "PortOverrideTypeDef",
    {
        "ListenerPort": NotRequired[int],
        "EndpointPort": NotRequired[int],
    },
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "FromPort": NotRequired[int],
        "ToPort": NotRequired[int],
    },
)

ProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "ProvisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CidrAuthorizationContext": "CidrAuthorizationContextTypeDef",
    },
)

ProvisionByoipCidrResponseTypeDef = TypedDict(
    "ProvisionByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveCustomRoutingEndpointsRequestRequestTypeDef = TypedDict(
    "RemoveCustomRoutingEndpointsRequestRequestTypeDef",
    {
        "EndpointIds": Sequence[str],
        "EndpointGroupArn": str,
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

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "IpAddress": NotRequired[str],
        "Port": NotRequired[int],
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
        "Key": str,
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "UpdateAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "FlowLogsEnabled": NotRequired[bool],
        "FlowLogsS3Bucket": NotRequired[str],
        "FlowLogsS3Prefix": NotRequired[str],
    },
)

UpdateAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "AcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAcceleratorRequestRequestTypeDef = TypedDict(
    "UpdateAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "Name": NotRequired[str],
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "Enabled": NotRequired[bool],
    },
)

UpdateAcceleratorResponseTypeDef = TypedDict(
    "UpdateAcceleratorResponseTypeDef",
    {
        "Accelerator": "AcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "FlowLogsEnabled": NotRequired[bool],
        "FlowLogsS3Bucket": NotRequired[str],
        "FlowLogsS3Prefix": NotRequired[str],
    },
)

UpdateCustomRoutingAcceleratorAttributesResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    {
        "AcceleratorAttributes": "CustomRoutingAcceleratorAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomRoutingAcceleratorRequestRequestTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorRequestRequestTypeDef",
    {
        "AcceleratorArn": str,
        "Name": NotRequired[str],
        "IpAddressType": NotRequired[Literal["IPV4"]],
        "Enabled": NotRequired[bool],
    },
)

UpdateCustomRoutingAcceleratorResponseTypeDef = TypedDict(
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    {
        "Accelerator": "CustomRoutingAcceleratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateCustomRoutingListenerRequestRequestTypeDef = TypedDict(
    "UpdateCustomRoutingListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": Sequence["PortRangeTypeDef"],
    },
)

UpdateCustomRoutingListenerResponseTypeDef = TypedDict(
    "UpdateCustomRoutingListenerResponseTypeDef",
    {
        "Listener": "CustomRoutingListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateEndpointGroupRequestRequestTypeDef = TypedDict(
    "UpdateEndpointGroupRequestRequestTypeDef",
    {
        "EndpointGroupArn": str,
        "EndpointConfigurations": NotRequired[Sequence["EndpointConfigurationTypeDef"]],
        "TrafficDialPercentage": NotRequired[float],
        "HealthCheckPort": NotRequired[int],
        "HealthCheckProtocol": NotRequired[HealthCheckProtocolType],
        "HealthCheckPath": NotRequired[str],
        "HealthCheckIntervalSeconds": NotRequired[int],
        "ThresholdCount": NotRequired[int],
        "PortOverrides": NotRequired[Sequence["PortOverrideTypeDef"]],
    },
)

UpdateEndpointGroupResponseTypeDef = TypedDict(
    "UpdateEndpointGroupResponseTypeDef",
    {
        "EndpointGroup": "EndpointGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateListenerRequestRequestTypeDef = TypedDict(
    "UpdateListenerRequestRequestTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": NotRequired[Sequence["PortRangeTypeDef"]],
        "Protocol": NotRequired[ProtocolType],
        "ClientAffinity": NotRequired[ClientAffinityType],
    },
)

UpdateListenerResponseTypeDef = TypedDict(
    "UpdateListenerResponseTypeDef",
    {
        "Listener": "ListenerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

WithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "WithdrawByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)

WithdrawByoipCidrResponseTypeDef = TypedDict(
    "WithdrawByoipCidrResponseTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
