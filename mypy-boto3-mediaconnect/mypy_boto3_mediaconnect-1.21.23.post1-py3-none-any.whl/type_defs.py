"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddFlowMediaStreamsRequestRequestTypeDef

    data: AddFlowMediaStreamsRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AlgorithmType,
    ColorimetryType,
    EncoderProfileType,
    EncodingNameType,
    EntitlementStatusType,
    FailoverModeType,
    KeyTypeType,
    MaintenanceDayType,
    MediaStreamTypeType,
    NetworkInterfaceTypeType,
    ProtocolType,
    RangeType,
    ReservationStateType,
    ScanModeType,
    SourceTypeType,
    StateType,
    StatusType,
    TcsType,
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
    "AddFlowMediaStreamsRequestRequestTypeDef",
    "AddFlowMediaStreamsResponseTypeDef",
    "AddFlowOutputsRequestRequestTypeDef",
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesRequestRequestTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddMaintenanceTypeDef",
    "AddMediaStreamRequestTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowRequestRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowRequestRequestTypeDef",
    "DeleteFlowResponseTypeDef",
    "DescribeFlowRequestRequestTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeOfferingRequestRequestTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationRequestRequestTypeDef",
    "DescribeReservationResponseTypeDef",
    "DestinationConfigurationRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "EncodingParametersRequestTypeDef",
    "EncodingParametersTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "FmtpRequestTypeDef",
    "FmtpTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsRequestRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "InputConfigurationRequestTypeDef",
    "InputConfigurationTypeDef",
    "InterfaceRequestTypeDef",
    "InterfaceTypeDef",
    "ListEntitlementsRequestRequestTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsRequestRequestTypeDef",
    "ListFlowsResponseTypeDef",
    "ListOfferingsRequestRequestTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsRequestRequestTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "MaintenanceTypeDef",
    "MediaStreamAttributesRequestTypeDef",
    "MediaStreamAttributesTypeDef",
    "MediaStreamOutputConfigurationRequestTypeDef",
    "MediaStreamOutputConfigurationTypeDef",
    "MediaStreamSourceConfigurationRequestTypeDef",
    "MediaStreamSourceConfigurationTypeDef",
    "MediaStreamTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingRequestRequestTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    "RemoveFlowMediaStreamResponseTypeDef",
    "RemoveFlowOutputRequestRequestTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceRequestRequestTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeFlowEntitlementRequestRequestTypeDef",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "SourcePriorityTypeDef",
    "SourceTypeDef",
    "StartFlowRequestRequestTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowRequestRequestTypeDef",
    "StopFlowResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TransportTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementRequestRequestTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    "UpdateFlowMediaStreamResponseTypeDef",
    "UpdateFlowOutputRequestRequestTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowRequestRequestTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceRequestRequestTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "UpdateMaintenanceTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)

AddFlowMediaStreamsRequestRequestTypeDef = TypedDict(
    "AddFlowMediaStreamsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": Sequence["AddMediaStreamRequestTypeDef"],
    },
)

AddFlowMediaStreamsResponseTypeDef = TypedDict(
    "AddFlowMediaStreamsResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreams": List["MediaStreamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowOutputsRequestRequestTypeDef = TypedDict(
    "AddFlowOutputsRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Outputs": Sequence["AddOutputRequestTypeDef"],
    },
)

AddFlowOutputsResponseTypeDef = TypedDict(
    "AddFlowOutputsResponseTypeDef",
    {
        "FlowArn": str,
        "Outputs": List["OutputTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowSourcesRequestRequestTypeDef = TypedDict(
    "AddFlowSourcesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "Sources": Sequence["SetSourceRequestTypeDef"],
    },
)

AddFlowSourcesResponseTypeDef = TypedDict(
    "AddFlowSourcesResponseTypeDef",
    {
        "FlowArn": str,
        "Sources": List["SourceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddFlowVpcInterfacesRequestRequestTypeDef = TypedDict(
    "AddFlowVpcInterfacesRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": Sequence["VpcInterfaceRequestTypeDef"],
    },
)

AddFlowVpcInterfacesResponseTypeDef = TypedDict(
    "AddFlowVpcInterfacesResponseTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaces": List["VpcInterfaceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddMaintenanceTypeDef = TypedDict(
    "AddMaintenanceTypeDef",
    {
        "MaintenanceDay": MaintenanceDayType,
        "MaintenanceStartHour": str,
    },
)

AddMediaStreamRequestTypeDef = TypedDict(
    "AddMediaStreamRequestTypeDef",
    {
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
        "Attributes": NotRequired["MediaStreamAttributesRequestTypeDef"],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "VideoFormat": NotRequired[str],
    },
)

AddOutputRequestTypeDef = TypedDict(
    "AddOutputRequestTypeDef",
    {
        "Protocol": ProtocolType,
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence["MediaStreamOutputConfigurationRequestTypeDef"]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Port": NotRequired[int],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired["VpcInterfaceAttachmentTypeDef"],
    },
)

CreateFlowRequestRequestTypeDef = TypedDict(
    "CreateFlowRequestRequestTypeDef",
    {
        "Name": str,
        "AvailabilityZone": NotRequired[str],
        "Entitlements": NotRequired[Sequence["GrantEntitlementRequestTypeDef"]],
        "MediaStreams": NotRequired[Sequence["AddMediaStreamRequestTypeDef"]],
        "Outputs": NotRequired[Sequence["AddOutputRequestTypeDef"]],
        "Source": NotRequired["SetSourceRequestTypeDef"],
        "SourceFailoverConfig": NotRequired["FailoverConfigTypeDef"],
        "Sources": NotRequired[Sequence["SetSourceRequestTypeDef"]],
        "VpcInterfaces": NotRequired[Sequence["VpcInterfaceRequestTypeDef"]],
        "Maintenance": NotRequired["AddMaintenanceTypeDef"],
    },
)

CreateFlowResponseTypeDef = TypedDict(
    "CreateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFlowRequestRequestTypeDef = TypedDict(
    "DeleteFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DeleteFlowResponseTypeDef = TypedDict(
    "DeleteFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowRequestRequestTypeDef = TypedDict(
    "DescribeFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

DescribeFlowResponseTypeDef = TypedDict(
    "DescribeFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "Messages": "MessagesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOfferingRequestRequestTypeDef = TypedDict(
    "DescribeOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
    },
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Offering": "OfferingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservationRequestRequestTypeDef = TypedDict(
    "DescribeReservationRequestRequestTypeDef",
    {
        "ReservationArn": str,
    },
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationConfigurationRequestTypeDef = TypedDict(
    "DestinationConfigurationRequestTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "DestinationIp": str,
        "DestinationPort": int,
        "Interface": "InterfaceTypeDef",
        "OutboundIp": str,
    },
)

EncodingParametersRequestTypeDef = TypedDict(
    "EncodingParametersRequestTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

EncodingParametersTypeDef = TypedDict(
    "EncodingParametersTypeDef",
    {
        "CompressionFactor": float,
        "EncoderProfile": EncoderProfileType,
    },
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "RoleArn": str,
        "Algorithm": NotRequired[AlgorithmType],
        "ConstantInitializationVector": NotRequired[str],
        "DeviceId": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Region": NotRequired[str],
        "ResourceId": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Url": NotRequired[str],
    },
)

EntitlementTypeDef = TypedDict(
    "EntitlementTypeDef",
    {
        "EntitlementArn": str,
        "Name": str,
        "Subscribers": List[str],
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
    },
)

FailoverConfigTypeDef = TypedDict(
    "FailoverConfigTypeDef",
    {
        "FailoverMode": NotRequired[FailoverModeType],
        "RecoveryWindow": NotRequired[int],
        "SourcePriority": NotRequired["SourcePriorityTypeDef"],
        "State": NotRequired[StateType],
    },
)

FlowTypeDef = TypedDict(
    "FlowTypeDef",
    {
        "AvailabilityZone": str,
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "Name": str,
        "Outputs": List["OutputTypeDef"],
        "Source": "SourceTypeDef",
        "Status": StatusType,
        "Description": NotRequired[str],
        "EgressIp": NotRequired[str],
        "MediaStreams": NotRequired[List["MediaStreamTypeDef"]],
        "SourceFailoverConfig": NotRequired["FailoverConfigTypeDef"],
        "Sources": NotRequired[List["SourceTypeDef"]],
        "VpcInterfaces": NotRequired[List["VpcInterfaceTypeDef"]],
        "Maintenance": NotRequired["MaintenanceTypeDef"],
    },
)

FmtpRequestTypeDef = TypedDict(
    "FmtpRequestTypeDef",
    {
        "ChannelOrder": NotRequired[str],
        "Colorimetry": NotRequired[ColorimetryType],
        "ExactFramerate": NotRequired[str],
        "Par": NotRequired[str],
        "Range": NotRequired[RangeType],
        "ScanMode": NotRequired[ScanModeType],
        "Tcs": NotRequired[TcsType],
    },
)

FmtpTypeDef = TypedDict(
    "FmtpTypeDef",
    {
        "ChannelOrder": NotRequired[str],
        "Colorimetry": NotRequired[ColorimetryType],
        "ExactFramerate": NotRequired[str],
        "Par": NotRequired[str],
        "Range": NotRequired[RangeType],
        "ScanMode": NotRequired[ScanModeType],
        "Tcs": NotRequired[TcsType],
    },
)

GrantEntitlementRequestTypeDef = TypedDict(
    "GrantEntitlementRequestTypeDef",
    {
        "Subscribers": Sequence[str],
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
        "Name": NotRequired[str],
    },
)

GrantFlowEntitlementsRequestRequestTypeDef = TypedDict(
    "GrantFlowEntitlementsRequestRequestTypeDef",
    {
        "Entitlements": Sequence["GrantEntitlementRequestTypeDef"],
        "FlowArn": str,
    },
)

GrantFlowEntitlementsResponseTypeDef = TypedDict(
    "GrantFlowEntitlementsResponseTypeDef",
    {
        "Entitlements": List["EntitlementTypeDef"],
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InputConfigurationRequestTypeDef = TypedDict(
    "InputConfigurationRequestTypeDef",
    {
        "InputPort": int,
        "Interface": "InterfaceRequestTypeDef",
    },
)

InputConfigurationTypeDef = TypedDict(
    "InputConfigurationTypeDef",
    {
        "InputIp": str,
        "InputPort": int,
        "Interface": "InterfaceTypeDef",
    },
)

InterfaceRequestTypeDef = TypedDict(
    "InterfaceRequestTypeDef",
    {
        "Name": str,
    },
)

InterfaceTypeDef = TypedDict(
    "InterfaceTypeDef",
    {
        "Name": str,
    },
)

ListEntitlementsRequestRequestTypeDef = TypedDict(
    "ListEntitlementsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListEntitlementsResponseTypeDef = TypedDict(
    "ListEntitlementsResponseTypeDef",
    {
        "Entitlements": List["ListedEntitlementTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFlowsRequestRequestTypeDef = TypedDict(
    "ListFlowsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListFlowsResponseTypeDef = TypedDict(
    "ListFlowsResponseTypeDef",
    {
        "Flows": List["ListedFlowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOfferingsRequestRequestTypeDef = TypedDict(
    "ListOfferingsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "Offerings": List["OfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListReservationsRequestRequestTypeDef = TypedDict(
    "ListReservationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {
        "NextToken": str,
        "Reservations": List["ReservationTypeDef"],
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

ListedEntitlementTypeDef = TypedDict(
    "ListedEntitlementTypeDef",
    {
        "EntitlementArn": str,
        "EntitlementName": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
    },
)

ListedFlowTypeDef = TypedDict(
    "ListedFlowTypeDef",
    {
        "AvailabilityZone": str,
        "Description": str,
        "FlowArn": str,
        "Name": str,
        "SourceType": SourceTypeType,
        "Status": StatusType,
        "Maintenance": NotRequired["MaintenanceTypeDef"],
    },
)

MaintenanceTypeDef = TypedDict(
    "MaintenanceTypeDef",
    {
        "MaintenanceDay": NotRequired[MaintenanceDayType],
        "MaintenanceDeadline": NotRequired[str],
        "MaintenanceScheduledDate": NotRequired[str],
        "MaintenanceStartHour": NotRequired[str],
    },
)

MediaStreamAttributesRequestTypeDef = TypedDict(
    "MediaStreamAttributesRequestTypeDef",
    {
        "Fmtp": NotRequired["FmtpRequestTypeDef"],
        "Lang": NotRequired[str],
    },
)

MediaStreamAttributesTypeDef = TypedDict(
    "MediaStreamAttributesTypeDef",
    {
        "Fmtp": "FmtpTypeDef",
        "Lang": NotRequired[str],
    },
)

MediaStreamOutputConfigurationRequestTypeDef = TypedDict(
    "MediaStreamOutputConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "DestinationConfigurations": NotRequired[
            Sequence["DestinationConfigurationRequestTypeDef"]
        ],
        "EncodingParameters": NotRequired["EncodingParametersRequestTypeDef"],
    },
)

MediaStreamOutputConfigurationTypeDef = TypedDict(
    "MediaStreamOutputConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "DestinationConfigurations": NotRequired[List["DestinationConfigurationTypeDef"]],
        "EncodingParameters": NotRequired["EncodingParametersTypeDef"],
    },
)

MediaStreamSourceConfigurationRequestTypeDef = TypedDict(
    "MediaStreamSourceConfigurationRequestTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "InputConfigurations": NotRequired[Sequence["InputConfigurationRequestTypeDef"]],
    },
)

MediaStreamSourceConfigurationTypeDef = TypedDict(
    "MediaStreamSourceConfigurationTypeDef",
    {
        "EncodingName": EncodingNameType,
        "MediaStreamName": str,
        "InputConfigurations": NotRequired[List["InputConfigurationTypeDef"]],
    },
)

MediaStreamTypeDef = TypedDict(
    "MediaStreamTypeDef",
    {
        "Fmt": int,
        "MediaStreamId": int,
        "MediaStreamName": str,
        "MediaStreamType": MediaStreamTypeType,
        "Attributes": NotRequired["MediaStreamAttributesTypeDef"],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "VideoFormat": NotRequired[str],
    },
)

MessagesTypeDef = TypedDict(
    "MessagesTypeDef",
    {
        "Errors": List[str],
    },
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ResourceSpecification": "ResourceSpecificationTypeDef",
    },
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "Name": str,
        "OutputArn": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "EntitlementArn": NotRequired[str],
        "ListenerAddress": NotRequired[str],
        "MediaLiveInputArn": NotRequired[str],
        "MediaStreamOutputConfigurations": NotRequired[
            List["MediaStreamOutputConfigurationTypeDef"]
        ],
        "Port": NotRequired[int],
        "Transport": NotRequired["TransportTypeDef"],
        "VpcInterfaceAttachment": NotRequired["VpcInterfaceAttachmentTypeDef"],
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

PurchaseOfferingRequestRequestTypeDef = TypedDict(
    "PurchaseOfferingRequestRequestTypeDef",
    {
        "OfferingArn": str,
        "ReservationName": str,
        "Start": str,
    },
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef",
    {
        "Reservation": "ReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "RemoveFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
    },
)

RemoveFlowMediaStreamResponseTypeDef = TypedDict(
    "RemoveFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowOutputRequestRequestTypeDef = TypedDict(
    "RemoveFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
    },
)

RemoveFlowOutputResponseTypeDef = TypedDict(
    "RemoveFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowSourceRequestRequestTypeDef = TypedDict(
    "RemoveFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
    },
)

RemoveFlowSourceResponseTypeDef = TypedDict(
    "RemoveFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveFlowVpcInterfaceRequestRequestTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "VpcInterfaceName": str,
    },
)

RemoveFlowVpcInterfaceResponseTypeDef = TypedDict(
    "RemoveFlowVpcInterfaceResponseTypeDef",
    {
        "FlowArn": str,
        "NonDeletedNetworkInterfaceIds": List[str],
        "VpcInterfaceName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": Literal["MONTHS"],
        "End": str,
        "OfferingArn": str,
        "OfferingDescription": str,
        "PricePerUnit": str,
        "PriceUnits": Literal["HOURLY"],
        "ReservationArn": str,
        "ReservationName": str,
        "ReservationState": ReservationStateType,
        "ResourceSpecification": "ResourceSpecificationTypeDef",
        "Start": str,
    },
)

ResourceSpecificationTypeDef = TypedDict(
    "ResourceSpecificationTypeDef",
    {
        "ResourceType": Literal["Mbps_Outbound_Bandwidth"],
        "ReservedBitrate": NotRequired[int],
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

RevokeFlowEntitlementRequestRequestTypeDef = TypedDict(
    "RevokeFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
    },
)

RevokeFlowEntitlementResponseTypeDef = TypedDict(
    "RevokeFlowEntitlementResponseTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": NotRequired["EncryptionTypeDef"],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence["MediaStreamSourceConfigurationRequestTypeDef"]
        ],
        "MinLatency": NotRequired[int],
        "Name": NotRequired[str],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
    },
)

SourcePriorityTypeDef = TypedDict(
    "SourcePriorityTypeDef",
    {
        "PrimarySource": NotRequired[str],
    },
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Name": str,
        "SourceArn": str,
        "DataTransferSubscriberFeePercent": NotRequired[int],
        "Decryption": NotRequired["EncryptionTypeDef"],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestIp": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            List["MediaStreamSourceConfigurationTypeDef"]
        ],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "Transport": NotRequired["TransportTypeDef"],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
    },
)

StartFlowRequestRequestTypeDef = TypedDict(
    "StartFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StartFlowResponseTypeDef = TypedDict(
    "StartFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StopFlowRequestRequestTypeDef = TypedDict(
    "StopFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
    },
)

StopFlowResponseTypeDef = TypedDict(
    "StopFlowResponseTypeDef",
    {
        "FlowArn": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

TransportTypeDef = TypedDict(
    "TransportTypeDef",
    {
        "Protocol": ProtocolType,
        "CidrAllowList": NotRequired[List[str]],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MinLatency": NotRequired[int],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateEncryptionTypeDef = TypedDict(
    "UpdateEncryptionTypeDef",
    {
        "Algorithm": NotRequired[AlgorithmType],
        "ConstantInitializationVector": NotRequired[str],
        "DeviceId": NotRequired[str],
        "KeyType": NotRequired[KeyTypeType],
        "Region": NotRequired[str],
        "ResourceId": NotRequired[str],
        "RoleArn": NotRequired[str],
        "SecretArn": NotRequired[str],
        "Url": NotRequired[str],
    },
)

UpdateFailoverConfigTypeDef = TypedDict(
    "UpdateFailoverConfigTypeDef",
    {
        "FailoverMode": NotRequired[FailoverModeType],
        "RecoveryWindow": NotRequired[int],
        "SourcePriority": NotRequired["SourcePriorityTypeDef"],
        "State": NotRequired[StateType],
    },
)

UpdateFlowEntitlementRequestRequestTypeDef = TypedDict(
    "UpdateFlowEntitlementRequestRequestTypeDef",
    {
        "EntitlementArn": str,
        "FlowArn": str,
        "Description": NotRequired[str],
        "Encryption": NotRequired["UpdateEncryptionTypeDef"],
        "EntitlementStatus": NotRequired[EntitlementStatusType],
        "Subscribers": NotRequired[Sequence[str]],
    },
)

UpdateFlowEntitlementResponseTypeDef = TypedDict(
    "UpdateFlowEntitlementResponseTypeDef",
    {
        "Entitlement": "EntitlementTypeDef",
        "FlowArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowMediaStreamRequestRequestTypeDef = TypedDict(
    "UpdateFlowMediaStreamRequestRequestTypeDef",
    {
        "FlowArn": str,
        "MediaStreamName": str,
        "Attributes": NotRequired["MediaStreamAttributesRequestTypeDef"],
        "ClockRate": NotRequired[int],
        "Description": NotRequired[str],
        "MediaStreamType": NotRequired[MediaStreamTypeType],
        "VideoFormat": NotRequired[str],
    },
)

UpdateFlowMediaStreamResponseTypeDef = TypedDict(
    "UpdateFlowMediaStreamResponseTypeDef",
    {
        "FlowArn": str,
        "MediaStream": "MediaStreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowOutputRequestRequestTypeDef = TypedDict(
    "UpdateFlowOutputRequestRequestTypeDef",
    {
        "FlowArn": str,
        "OutputArn": str,
        "CidrAllowList": NotRequired[Sequence[str]],
        "Description": NotRequired[str],
        "Destination": NotRequired[str],
        "Encryption": NotRequired["UpdateEncryptionTypeDef"],
        "MaxLatency": NotRequired[int],
        "MediaStreamOutputConfigurations": NotRequired[
            Sequence["MediaStreamOutputConfigurationRequestTypeDef"]
        ],
        "MinLatency": NotRequired[int],
        "Port": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "RemoteId": NotRequired[str],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "SmoothingLatency": NotRequired[int],
        "StreamId": NotRequired[str],
        "VpcInterfaceAttachment": NotRequired["VpcInterfaceAttachmentTypeDef"],
    },
)

UpdateFlowOutputResponseTypeDef = TypedDict(
    "UpdateFlowOutputResponseTypeDef",
    {
        "FlowArn": str,
        "Output": "OutputTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowRequestRequestTypeDef = TypedDict(
    "UpdateFlowRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceFailoverConfig": NotRequired["UpdateFailoverConfigTypeDef"],
        "Maintenance": NotRequired["UpdateMaintenanceTypeDef"],
    },
)

UpdateFlowResponseTypeDef = TypedDict(
    "UpdateFlowResponseTypeDef",
    {
        "Flow": "FlowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateFlowSourceRequestRequestTypeDef = TypedDict(
    "UpdateFlowSourceRequestRequestTypeDef",
    {
        "FlowArn": str,
        "SourceArn": str,
        "Decryption": NotRequired["UpdateEncryptionTypeDef"],
        "Description": NotRequired[str],
        "EntitlementArn": NotRequired[str],
        "IngestPort": NotRequired[int],
        "MaxBitrate": NotRequired[int],
        "MaxLatency": NotRequired[int],
        "MaxSyncBuffer": NotRequired[int],
        "MediaStreamSourceConfigurations": NotRequired[
            Sequence["MediaStreamSourceConfigurationRequestTypeDef"]
        ],
        "MinLatency": NotRequired[int],
        "Protocol": NotRequired[ProtocolType],
        "SenderControlPort": NotRequired[int],
        "SenderIpAddress": NotRequired[str],
        "StreamId": NotRequired[str],
        "VpcInterfaceName": NotRequired[str],
        "WhitelistCidr": NotRequired[str],
    },
)

UpdateFlowSourceResponseTypeDef = TypedDict(
    "UpdateFlowSourceResponseTypeDef",
    {
        "FlowArn": str,
        "Source": "SourceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateMaintenanceTypeDef = TypedDict(
    "UpdateMaintenanceTypeDef",
    {
        "MaintenanceDay": NotRequired[MaintenanceDayType],
        "MaintenanceScheduledDate": NotRequired[str],
        "MaintenanceStartHour": NotRequired[str],
    },
)

VpcInterfaceAttachmentTypeDef = TypedDict(
    "VpcInterfaceAttachmentTypeDef",
    {
        "VpcInterfaceName": NotRequired[str],
    },
)

VpcInterfaceRequestTypeDef = TypedDict(
    "VpcInterfaceRequestTypeDef",
    {
        "Name": str,
        "RoleArn": str,
        "SecurityGroupIds": Sequence[str],
        "SubnetId": str,
        "NetworkInterfaceType": NotRequired[NetworkInterfaceTypeType],
    },
)

VpcInterfaceTypeDef = TypedDict(
    "VpcInterfaceTypeDef",
    {
        "Name": str,
        "NetworkInterfaceIds": List[str],
        "NetworkInterfaceType": NetworkInterfaceTypeType,
        "RoleArn": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
