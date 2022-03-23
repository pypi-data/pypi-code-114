"""
Type annotations for iotwireless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef

    data: AbpV1_0_xTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    BatteryLevelType,
    ConnectionStatusType,
    DeviceStateType,
    DlClassType,
    EventNotificationTopicStatusType,
    EventType,
    ExpressionTypeType,
    FuotaDeviceStatusType,
    FuotaTaskStatusType,
    LogLevelType,
    MessageTypeType,
    SigningAlgType,
    SupportedRfRegionType,
    WirelessDeviceEventType,
    WirelessDeviceFrameInfoType,
    WirelessDeviceIdTypeType,
    WirelessDeviceTypeType,
    WirelessGatewayEventType,
    WirelessGatewayIdTypeType,
    WirelessGatewayServiceTypeType,
    WirelessGatewayTaskStatusType,
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
    "AbpV1_0_xTypeDef",
    "AbpV1_1TypeDef",
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    "CertificateListTypeDef",
    "CreateDestinationRequestRequestTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileRequestRequestTypeDef",
    "CreateDeviceProfileResponseTypeDef",
    "CreateFuotaTaskRequestRequestTypeDef",
    "CreateFuotaTaskResponseTypeDef",
    "CreateMulticastGroupRequestRequestTypeDef",
    "CreateMulticastGroupResponseTypeDef",
    "CreateServiceProfileRequestRequestTypeDef",
    "CreateServiceProfileResponseTypeDef",
    "CreateWirelessDeviceRequestRequestTypeDef",
    "CreateWirelessDeviceResponseTypeDef",
    "CreateWirelessGatewayRequestRequestTypeDef",
    "CreateWirelessGatewayResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    "CreateWirelessGatewayTaskResponseTypeDef",
    "DeleteDestinationRequestRequestTypeDef",
    "DeleteDeviceProfileRequestRequestTypeDef",
    "DeleteFuotaTaskRequestRequestTypeDef",
    "DeleteMulticastGroupRequestRequestTypeDef",
    "DeleteQueuedMessagesRequestRequestTypeDef",
    "DeleteServiceProfileRequestRequestTypeDef",
    "DeleteWirelessDeviceRequestRequestTypeDef",
    "DeleteWirelessGatewayRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "DeviceRegistrationStateEventConfigurationTypeDef",
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    "DownlinkQueueMessageTypeDef",
    "FPortsTypeDef",
    "FuotaTaskTypeDef",
    "GetDestinationRequestRequestTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceProfileRequestRequestTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "GetFuotaTaskRequestRequestTypeDef",
    "GetFuotaTaskResponseTypeDef",
    "GetLogLevelsByResourceTypesResponseTypeDef",
    "GetMulticastGroupRequestRequestTypeDef",
    "GetMulticastGroupResponseTypeDef",
    "GetMulticastGroupSessionRequestRequestTypeDef",
    "GetMulticastGroupSessionResponseTypeDef",
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    "GetPartnerAccountRequestRequestTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "GetResourceEventConfigurationRequestRequestTypeDef",
    "GetResourceEventConfigurationResponseTypeDef",
    "GetResourceLogLevelRequestRequestTypeDef",
    "GetResourceLogLevelResponseTypeDef",
    "GetServiceEndpointRequestRequestTypeDef",
    "GetServiceEndpointResponseTypeDef",
    "GetServiceProfileRequestRequestTypeDef",
    "GetServiceProfileResponseTypeDef",
    "GetWirelessDeviceRequestRequestTypeDef",
    "GetWirelessDeviceResponseTypeDef",
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    "GetWirelessDeviceStatisticsResponseTypeDef",
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    "GetWirelessGatewayCertificateResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    "GetWirelessGatewayRequestRequestTypeDef",
    "GetWirelessGatewayResponseTypeDef",
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    "GetWirelessGatewayStatisticsResponseTypeDef",
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    "GetWirelessGatewayTaskResponseTypeDef",
    "ListDestinationsRequestRequestTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesRequestRequestTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "ListFuotaTasksRequestRequestTypeDef",
    "ListFuotaTasksResponseTypeDef",
    "ListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    "ListMulticastGroupsRequestRequestTypeDef",
    "ListMulticastGroupsResponseTypeDef",
    "ListPartnerAccountsRequestRequestTypeDef",
    "ListPartnerAccountsResponseTypeDef",
    "ListQueuedMessagesRequestRequestTypeDef",
    "ListQueuedMessagesResponseTypeDef",
    "ListServiceProfilesRequestRequestTypeDef",
    "ListServiceProfilesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWirelessDevicesRequestRequestTypeDef",
    "ListWirelessDevicesResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    "ListWirelessGatewaysRequestRequestTypeDef",
    "ListWirelessGatewaysResponseTypeDef",
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANDeviceTypeDef",
    "LoRaWANFuotaTaskGetInfoTypeDef",
    "LoRaWANFuotaTaskTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANGatewayTypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANMulticastGetTypeDef",
    "LoRaWANMulticastMetadataTypeDef",
    "LoRaWANMulticastSessionTypeDef",
    "LoRaWANMulticastTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANStartFuotaTaskTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "MulticastGroupByFuotaTaskTypeDef",
    "MulticastGroupTypeDef",
    "MulticastWirelessMetadataTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "ProximityEventConfigurationTypeDef",
    "PutResourceLogLevelRequestRequestTypeDef",
    "ResetResourceLogLevelRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "SendDataToMulticastGroupRequestRequestTypeDef",
    "SendDataToMulticastGroupResponseTypeDef",
    "SendDataToWirelessDeviceRequestRequestTypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkEventNotificationConfigurationsTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    "StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    "StartFuotaTaskRequestRequestTypeDef",
    "StartMulticastGroupSessionRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TestWirelessDeviceRequestRequestTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "TraceContentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDestinationRequestRequestTypeDef",
    "UpdateFuotaTaskRequestRequestTypeDef",
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    "UpdateMulticastGroupRequestRequestTypeDef",
    "UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    "UpdatePartnerAccountRequestRequestTypeDef",
    "UpdateResourceEventConfigurationRequestRequestTypeDef",
    "UpdateWirelessDeviceRequestRequestTypeDef",
    "UpdateWirelessGatewayRequestRequestTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "WirelessDeviceEventLogOptionTypeDef",
    "WirelessDeviceLogOptionTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "WirelessGatewayEventLogOptionTypeDef",
    "WirelessGatewayLogOptionTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "WirelessMetadataTypeDef",
)

AbpV1_0_xTypeDef = TypedDict(
    "AbpV1_0_xTypeDef",
    {
        "DevAddr": NotRequired[str],
        "SessionKeys": NotRequired["SessionKeysAbpV1_0_xTypeDef"],
    },
)

AbpV1_1TypeDef = TypedDict(
    "AbpV1_1TypeDef",
    {
        "DevAddr": NotRequired[str],
        "SessionKeys": NotRequired["SessionKeysAbpV1_1TypeDef"],
    },
)

AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

AssociateAwsAccountWithPartnerAccountResponseTypeDef = TypedDict(
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateMulticastGroupWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)

AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

AssociateWirelessDeviceWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessDeviceWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

AssociateWirelessGatewayWithCertificateRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateRequestRequestTypeDef",
    {
        "Id": str,
        "IotCertificateId": str,
    },
)

AssociateWirelessGatewayWithCertificateResponseTypeDef = TypedDict(
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateWirelessGatewayWithThingRequestRequestTypeDef = TypedDict(
    "AssociateWirelessGatewayWithThingRequestRequestTypeDef",
    {
        "Id": str,
        "ThingArn": str,
    },
)

CancelMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "CancelMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

CertificateListTypeDef = TypedDict(
    "CertificateListTypeDef",
    {
        "SigningAlg": SigningAlgType,
        "Value": str,
    },
)

CreateDestinationRequestRequestTypeDef = TypedDict(
    "CreateDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": ExpressionTypeType,
        "Expression": str,
        "RoleArn": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
    },
)

CreateDestinationResponseTypeDef = TypedDict(
    "CreateDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDeviceProfileRequestRequestTypeDef = TypedDict(
    "CreateDeviceProfileRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANDeviceProfileTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
    },
)

CreateDeviceProfileResponseTypeDef = TypedDict(
    "CreateDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFuotaTaskRequestRequestTypeDef = TypedDict(
    "CreateFuotaTaskRequestRequestTypeDef",
    {
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANFuotaTaskTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateFuotaTaskResponseTypeDef = TypedDict(
    "CreateFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMulticastGroupRequestRequestTypeDef = TypedDict(
    "CreateMulticastGroupRequestRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANMulticastTypeDef",
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateMulticastGroupResponseTypeDef = TypedDict(
    "CreateMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateServiceProfileRequestRequestTypeDef = TypedDict(
    "CreateServiceProfileRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANServiceProfileTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
    },
)

CreateServiceProfileResponseTypeDef = TypedDict(
    "CreateServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "CreateWirelessDeviceRequestRequestTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "DestinationName": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANDeviceTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWirelessDeviceResponseTypeDef = TypedDict(
    "CreateWirelessDeviceResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayRequestRequestTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ClientRequestToken": NotRequired[str],
    },
)

CreateWirelessGatewayResponseTypeDef = TypedDict(
    "CreateWirelessGatewayResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": NotRequired[str],
        "Update": NotRequired["UpdateWirelessGatewayTaskCreateTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "Id": str,
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "CreateWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessGatewayTaskDefinitionId": str,
    },
)

CreateWirelessGatewayTaskResponseTypeDef = TypedDict(
    "CreateWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayTaskDefinitionId": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDestinationRequestRequestTypeDef = TypedDict(
    "DeleteDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

DeleteDeviceProfileRequestRequestTypeDef = TypedDict(
    "DeleteDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteFuotaTaskRequestRequestTypeDef = TypedDict(
    "DeleteFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteMulticastGroupRequestRequestTypeDef = TypedDict(
    "DeleteMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteQueuedMessagesRequestRequestTypeDef = TypedDict(
    "DeleteQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
        "MessageId": str,
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
    },
)

DeleteServiceProfileRequestRequestTypeDef = TypedDict(
    "DeleteServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessDeviceRequestRequestTypeDef = TypedDict(
    "DeleteWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "DeleteWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DestinationsTypeDef = TypedDict(
    "DestinationsTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "ExpressionType": NotRequired[ExpressionTypeType],
        "Expression": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

DeviceProfileTypeDef = TypedDict(
    "DeviceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
    },
)

DeviceRegistrationStateEventConfigurationTypeDef = TypedDict(
    "DeviceRegistrationStateEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired["SidewalkEventNotificationConfigurationsTypeDef"],
    },
)

DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef = TypedDict(
    "DisassociateAwsAccountFromPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateMulticastGroupFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "MulticastGroupId": str,
    },
)

DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "WirelessDeviceId": str,
    },
)

DisassociateWirelessDeviceFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessDeviceFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DisassociateWirelessGatewayFromThingRequestRequestTypeDef = TypedDict(
    "DisassociateWirelessGatewayFromThingRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DownlinkQueueMessageTypeDef = TypedDict(
    "DownlinkQueueMessageTypeDef",
    {
        "MessageId": NotRequired[str],
        "TransmitMode": NotRequired[int],
        "ReceivedAt": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANSendDataToDeviceTypeDef"],
    },
)

FPortsTypeDef = TypedDict(
    "FPortsTypeDef",
    {
        "Fuota": NotRequired[int],
        "Multicast": NotRequired[int],
        "ClockSync": NotRequired[int],
    },
)

FuotaTaskTypeDef = TypedDict(
    "FuotaTaskTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

GetDestinationRequestRequestTypeDef = TypedDict(
    "GetDestinationRequestRequestTypeDef",
    {
        "Name": str,
    },
)

GetDestinationResponseTypeDef = TypedDict(
    "GetDestinationResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Expression": str,
        "ExpressionType": ExpressionTypeType,
        "Description": str,
        "RoleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceProfileRequestRequestTypeDef = TypedDict(
    "GetDeviceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetDeviceProfileResponseTypeDef = TypedDict(
    "GetDeviceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANDeviceProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetFuotaTaskRequestRequestTypeDef = TypedDict(
    "GetFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetFuotaTaskResponseTypeDef = TypedDict(
    "GetFuotaTaskResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Status": FuotaTaskStatusType,
        "Name": str,
        "Description": str,
        "LoRaWAN": "LoRaWANFuotaTaskGetInfoTypeDef",
        "FirmwareUpdateImage": str,
        "FirmwareUpdateRole": str,
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetLogLevelsByResourceTypesResponseTypeDef = TypedDict(
    "GetLogLevelsByResourceTypesResponseTypeDef",
    {
        "DefaultLogLevel": LogLevelType,
        "WirelessGatewayLogOptions": List["WirelessGatewayLogOptionTypeDef"],
        "WirelessDeviceLogOptions": List["WirelessDeviceLogOptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMulticastGroupRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetMulticastGroupResponseTypeDef = TypedDict(
    "GetMulticastGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Description": str,
        "Status": str,
        "LoRaWAN": "LoRaWANMulticastGetTypeDef",
        "CreatedAt": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "GetMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetMulticastGroupSessionResponseTypeDef = TypedDict(
    "GetMulticastGroupSessionResponseTypeDef",
    {
        "LoRaWAN": "LoRaWANMulticastSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
    },
)

GetNetworkAnalyzerConfigurationResponseTypeDef = TypedDict(
    "GetNetworkAnalyzerConfigurationResponseTypeDef",
    {
        "TraceContent": "TraceContentTypeDef",
        "WirelessDevices": List[str],
        "WirelessGateways": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPartnerAccountRequestRequestTypeDef = TypedDict(
    "GetPartnerAccountRequestRequestTypeDef",
    {
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

GetPartnerAccountResponseTypeDef = TypedDict(
    "GetPartnerAccountResponseTypeDef",
    {
        "Sidewalk": "SidewalkAccountInfoWithFingerprintTypeDef",
        "AccountLinked": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "GetResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": Literal["PartnerAccountId"],
        "PartnerType": NotRequired[Literal["Sidewalk"]],
    },
)

GetResourceEventConfigurationResponseTypeDef = TypedDict(
    "GetResourceEventConfigurationResponseTypeDef",
    {
        "DeviceRegistrationState": "DeviceRegistrationStateEventConfigurationTypeDef",
        "Proximity": "ProximityEventConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "GetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
    },
)

GetResourceLogLevelResponseTypeDef = TypedDict(
    "GetResourceLogLevelResponseTypeDef",
    {
        "LogLevel": LogLevelType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceEndpointRequestRequestTypeDef = TypedDict(
    "GetServiceEndpointRequestRequestTypeDef",
    {
        "ServiceType": NotRequired[WirelessGatewayServiceTypeType],
    },
)

GetServiceEndpointResponseTypeDef = TypedDict(
    "GetServiceEndpointResponseTypeDef",
    {
        "ServiceType": WirelessGatewayServiceTypeType,
        "ServiceEndpoint": str,
        "ServerTrust": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetServiceProfileRequestRequestTypeDef = TypedDict(
    "GetServiceProfileRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetServiceProfileResponseTypeDef = TypedDict(
    "GetServiceProfileResponseTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Id": str,
        "LoRaWAN": "LoRaWANGetServiceProfileInfoTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessDeviceIdTypeType,
    },
)

GetWirelessDeviceResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Sidewalk": "SidewalkDeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessDeviceStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsRequestRequestTypeDef",
    {
        "WirelessDeviceId": str,
    },
)

GetWirelessDeviceStatisticsResponseTypeDef = TypedDict(
    "GetWirelessDeviceStatisticsResponseTypeDef",
    {
        "WirelessDeviceId": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANDeviceMetadataTypeDef",
        "Sidewalk": "SidewalkDeviceMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayCertificateRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayCertificateRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayCertificateResponseTypeDef = TypedDict(
    "GetWirelessGatewayCertificateResponseTypeDef",
    {
        "IotCertificateId": str,
        "LoRaWANNetworkServerCertificateId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayFirmwareInformationRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayFirmwareInformationResponseTypeDef = TypedDict(
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    {
        "LoRaWAN": "LoRaWANGatewayCurrentVersionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": WirelessGatewayIdTypeType,
    },
)

GetWirelessGatewayResponseTypeDef = TypedDict(
    "GetWirelessGatewayResponseTypeDef",
    {
        "Name": str,
        "Id": str,
        "Description": str,
        "LoRaWAN": "LoRaWANGatewayTypeDef",
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayStatisticsRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsRequestRequestTypeDef",
    {
        "WirelessGatewayId": str,
    },
)

GetWirelessGatewayStatisticsResponseTypeDef = TypedDict(
    "GetWirelessGatewayStatisticsResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "LastUplinkReceivedAt": str,
        "ConnectionStatus": ConnectionStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskDefinitionRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskDefinitionResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    {
        "AutoCreateTasks": bool,
        "Name": str,
        "Update": "UpdateWirelessGatewayTaskCreateTypeDef",
        "Arn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetWirelessGatewayTaskRequestRequestTypeDef = TypedDict(
    "GetWirelessGatewayTaskRequestRequestTypeDef",
    {
        "Id": str,
    },
)

GetWirelessGatewayTaskResponseTypeDef = TypedDict(
    "GetWirelessGatewayTaskResponseTypeDef",
    {
        "WirelessGatewayId": str,
        "WirelessGatewayTaskDefinitionId": str,
        "LastUplinkReceivedAt": str,
        "TaskCreatedAt": str,
        "Status": WirelessGatewayTaskStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDestinationsRequestRequestTypeDef = TypedDict(
    "ListDestinationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListDestinationsResponseTypeDef = TypedDict(
    "ListDestinationsResponseTypeDef",
    {
        "NextToken": str,
        "DestinationList": List["DestinationsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceProfilesRequestRequestTypeDef = TypedDict(
    "ListDeviceProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDeviceProfilesResponseTypeDef = TypedDict(
    "ListDeviceProfilesResponseTypeDef",
    {
        "NextToken": str,
        "DeviceProfileList": List["DeviceProfileTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFuotaTasksRequestRequestTypeDef = TypedDict(
    "ListFuotaTasksRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFuotaTasksResponseTypeDef = TypedDict(
    "ListFuotaTasksResponseTypeDef",
    {
        "NextToken": str,
        "FuotaTaskList": List["FuotaTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMulticastGroupsByFuotaTaskRequestRequestTypeDef = TypedDict(
    "ListMulticastGroupsByFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMulticastGroupsByFuotaTaskResponseTypeDef = TypedDict(
    "ListMulticastGroupsByFuotaTaskResponseTypeDef",
    {
        "NextToken": str,
        "MulticastGroupList": List["MulticastGroupByFuotaTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMulticastGroupsRequestRequestTypeDef = TypedDict(
    "ListMulticastGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMulticastGroupsResponseTypeDef = TypedDict(
    "ListMulticastGroupsResponseTypeDef",
    {
        "NextToken": str,
        "MulticastGroupList": List["MulticastGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPartnerAccountsRequestRequestTypeDef = TypedDict(
    "ListPartnerAccountsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPartnerAccountsResponseTypeDef = TypedDict(
    "ListPartnerAccountsResponseTypeDef",
    {
        "NextToken": str,
        "Sidewalk": List["SidewalkAccountInfoWithFingerprintTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListQueuedMessagesRequestRequestTypeDef = TypedDict(
    "ListQueuedMessagesRequestRequestTypeDef",
    {
        "Id": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
    },
)

ListQueuedMessagesResponseTypeDef = TypedDict(
    "ListQueuedMessagesResponseTypeDef",
    {
        "NextToken": str,
        "DownlinkQueueMessagesList": List["DownlinkQueueMessageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListServiceProfilesRequestRequestTypeDef = TypedDict(
    "ListServiceProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListServiceProfilesResponseTypeDef = TypedDict(
    "ListServiceProfilesResponseTypeDef",
    {
        "NextToken": str,
        "ServiceProfileList": List["ServiceProfileTypeDef"],
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

ListWirelessDevicesRequestRequestTypeDef = TypedDict(
    "ListWirelessDevicesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DestinationName": NotRequired[str],
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "WirelessDeviceType": NotRequired[WirelessDeviceTypeType],
        "FuotaTaskId": NotRequired[str],
        "MulticastGroupId": NotRequired[str],
    },
)

ListWirelessDevicesResponseTypeDef = TypedDict(
    "ListWirelessDevicesResponseTypeDef",
    {
        "NextToken": str,
        "WirelessDeviceList": List["WirelessDeviceStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "TaskDefinitionType": NotRequired[Literal["UPDATE"]],
    },
)

ListWirelessGatewayTaskDefinitionsResponseTypeDef = TypedDict(
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    {
        "NextToken": str,
        "TaskDefinitions": List["UpdateWirelessGatewayTaskEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWirelessGatewaysRequestRequestTypeDef = TypedDict(
    "ListWirelessGatewaysRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWirelessGatewaysResponseTypeDef = TypedDict(
    "ListWirelessGatewaysResponseTypeDef",
    {
        "NextToken": str,
        "WirelessGatewayList": List["WirelessGatewayStatisticsTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoRaWANDeviceMetadataTypeDef = TypedDict(
    "LoRaWANDeviceMetadataTypeDef",
    {
        "DevEui": NotRequired[str],
        "FPort": NotRequired[int],
        "DataRate": NotRequired[int],
        "Frequency": NotRequired[int],
        "Timestamp": NotRequired[str],
        "Gateways": NotRequired[List["LoRaWANGatewayMetadataTypeDef"]],
    },
)

LoRaWANDeviceProfileTypeDef = TypedDict(
    "LoRaWANDeviceProfileTypeDef",
    {
        "SupportsClassB": NotRequired[bool],
        "ClassBTimeout": NotRequired[int],
        "PingSlotPeriod": NotRequired[int],
        "PingSlotDr": NotRequired[int],
        "PingSlotFreq": NotRequired[int],
        "SupportsClassC": NotRequired[bool],
        "ClassCTimeout": NotRequired[int],
        "MacVersion": NotRequired[str],
        "RegParamsRevision": NotRequired[str],
        "RxDelay1": NotRequired[int],
        "RxDrOffset1": NotRequired[int],
        "RxDataRate2": NotRequired[int],
        "RxFreq2": NotRequired[int],
        "FactoryPresetFreqsList": NotRequired[Sequence[int]],
        "MaxEirp": NotRequired[int],
        "MaxDutyCycle": NotRequired[int],
        "RfRegion": NotRequired[str],
        "SupportsJoin": NotRequired[bool],
        "Supports32BitFCnt": NotRequired[bool],
    },
)

LoRaWANDeviceTypeDef = TypedDict(
    "LoRaWANDeviceTypeDef",
    {
        "DevEui": NotRequired[str],
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
        "OtaaV1_1": NotRequired["OtaaV1_1TypeDef"],
        "OtaaV1_0_x": NotRequired["OtaaV1_0_xTypeDef"],
        "AbpV1_1": NotRequired["AbpV1_1TypeDef"],
        "AbpV1_0_x": NotRequired["AbpV1_0_xTypeDef"],
        "FPorts": NotRequired["FPortsTypeDef"],
    },
)

LoRaWANFuotaTaskGetInfoTypeDef = TypedDict(
    "LoRaWANFuotaTaskGetInfoTypeDef",
    {
        "RfRegion": NotRequired[str],
        "StartTime": NotRequired[datetime],
    },
)

LoRaWANFuotaTaskTypeDef = TypedDict(
    "LoRaWANFuotaTaskTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
    },
)

LoRaWANGatewayCurrentVersionTypeDef = TypedDict(
    "LoRaWANGatewayCurrentVersionTypeDef",
    {
        "CurrentVersion": NotRequired["LoRaWANGatewayVersionTypeDef"],
    },
)

LoRaWANGatewayMetadataTypeDef = TypedDict(
    "LoRaWANGatewayMetadataTypeDef",
    {
        "GatewayEui": NotRequired[str],
        "Snr": NotRequired[float],
        "Rssi": NotRequired[float],
    },
)

LoRaWANGatewayTypeDef = TypedDict(
    "LoRaWANGatewayTypeDef",
    {
        "GatewayEui": NotRequired[str],
        "RfRegion": NotRequired[str],
        "JoinEuiFilters": NotRequired[Sequence[Sequence[str]]],
        "NetIdFilters": NotRequired[Sequence[str]],
        "SubBands": NotRequired[Sequence[int]],
    },
)

LoRaWANGatewayVersionTypeDef = TypedDict(
    "LoRaWANGatewayVersionTypeDef",
    {
        "PackageVersion": NotRequired[str],
        "Model": NotRequired[str],
        "Station": NotRequired[str],
    },
)

LoRaWANGetServiceProfileInfoTypeDef = TypedDict(
    "LoRaWANGetServiceProfileInfoTypeDef",
    {
        "UlRate": NotRequired[int],
        "UlBucketSize": NotRequired[int],
        "UlRatePolicy": NotRequired[str],
        "DlRate": NotRequired[int],
        "DlBucketSize": NotRequired[int],
        "DlRatePolicy": NotRequired[str],
        "AddGwMetadata": NotRequired[bool],
        "DevStatusReqFreq": NotRequired[int],
        "ReportDevStatusBattery": NotRequired[bool],
        "ReportDevStatusMargin": NotRequired[bool],
        "DrMin": NotRequired[int],
        "DrMax": NotRequired[int],
        "ChannelMask": NotRequired[str],
        "PrAllowed": NotRequired[bool],
        "HrAllowed": NotRequired[bool],
        "RaAllowed": NotRequired[bool],
        "NwkGeoLoc": NotRequired[bool],
        "TargetPer": NotRequired[int],
        "MinGwDiversity": NotRequired[int],
    },
)

LoRaWANListDeviceTypeDef = TypedDict(
    "LoRaWANListDeviceTypeDef",
    {
        "DevEui": NotRequired[str],
    },
)

LoRaWANMulticastGetTypeDef = TypedDict(
    "LoRaWANMulticastGetTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
        "DlClass": NotRequired[DlClassType],
        "NumberOfDevicesRequested": NotRequired[int],
        "NumberOfDevicesInGroup": NotRequired[int],
    },
)

LoRaWANMulticastMetadataTypeDef = TypedDict(
    "LoRaWANMulticastMetadataTypeDef",
    {
        "FPort": NotRequired[int],
    },
)

LoRaWANMulticastSessionTypeDef = TypedDict(
    "LoRaWANMulticastSessionTypeDef",
    {
        "DlDr": NotRequired[int],
        "DlFreq": NotRequired[int],
        "SessionStartTime": NotRequired[datetime],
        "SessionTimeout": NotRequired[int],
    },
)

LoRaWANMulticastTypeDef = TypedDict(
    "LoRaWANMulticastTypeDef",
    {
        "RfRegion": NotRequired[SupportedRfRegionType],
        "DlClass": NotRequired[DlClassType],
    },
)

LoRaWANSendDataToDeviceTypeDef = TypedDict(
    "LoRaWANSendDataToDeviceTypeDef",
    {
        "FPort": NotRequired[int],
    },
)

LoRaWANServiceProfileTypeDef = TypedDict(
    "LoRaWANServiceProfileTypeDef",
    {
        "AddGwMetadata": NotRequired[bool],
    },
)

LoRaWANStartFuotaTaskTypeDef = TypedDict(
    "LoRaWANStartFuotaTaskTypeDef",
    {
        "StartTime": NotRequired[Union[datetime, str]],
    },
)

LoRaWANUpdateDeviceTypeDef = TypedDict(
    "LoRaWANUpdateDeviceTypeDef",
    {
        "DeviceProfileId": NotRequired[str],
        "ServiceProfileId": NotRequired[str],
    },
)

LoRaWANUpdateGatewayTaskCreateTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    {
        "UpdateSignature": NotRequired[str],
        "SigKeyCrc": NotRequired[int],
        "CurrentVersion": NotRequired["LoRaWANGatewayVersionTypeDef"],
        "UpdateVersion": NotRequired["LoRaWANGatewayVersionTypeDef"],
    },
)

LoRaWANUpdateGatewayTaskEntryTypeDef = TypedDict(
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    {
        "CurrentVersion": NotRequired["LoRaWANGatewayVersionTypeDef"],
        "UpdateVersion": NotRequired["LoRaWANGatewayVersionTypeDef"],
    },
)

MulticastGroupByFuotaTaskTypeDef = TypedDict(
    "MulticastGroupByFuotaTaskTypeDef",
    {
        "Id": NotRequired[str],
    },
)

MulticastGroupTypeDef = TypedDict(
    "MulticastGroupTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

MulticastWirelessMetadataTypeDef = TypedDict(
    "MulticastWirelessMetadataTypeDef",
    {
        "LoRaWAN": NotRequired["LoRaWANMulticastMetadataTypeDef"],
    },
)

OtaaV1_0_xTypeDef = TypedDict(
    "OtaaV1_0_xTypeDef",
    {
        "AppKey": NotRequired[str],
        "AppEui": NotRequired[str],
        "GenAppKey": NotRequired[str],
    },
)

OtaaV1_1TypeDef = TypedDict(
    "OtaaV1_1TypeDef",
    {
        "AppKey": NotRequired[str],
        "NwkKey": NotRequired[str],
        "JoinEui": NotRequired[str],
    },
)

ProximityEventConfigurationTypeDef = TypedDict(
    "ProximityEventConfigurationTypeDef",
    {
        "Sidewalk": NotRequired["SidewalkEventNotificationConfigurationsTypeDef"],
    },
)

PutResourceLogLevelRequestRequestTypeDef = TypedDict(
    "PutResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
        "LogLevel": LogLevelType,
    },
)

ResetResourceLogLevelRequestRequestTypeDef = TypedDict(
    "ResetResourceLogLevelRequestRequestTypeDef",
    {
        "ResourceIdentifier": str,
        "ResourceType": str,
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

SendDataToMulticastGroupRequestRequestTypeDef = TypedDict(
    "SendDataToMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "PayloadData": str,
        "WirelessMetadata": "MulticastWirelessMetadataTypeDef",
    },
)

SendDataToMulticastGroupResponseTypeDef = TypedDict(
    "SendDataToMulticastGroupResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendDataToWirelessDeviceRequestRequestTypeDef = TypedDict(
    "SendDataToWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
        "TransmitMode": int,
        "PayloadData": str,
        "WirelessMetadata": NotRequired["WirelessMetadataTypeDef"],
    },
)

SendDataToWirelessDeviceResponseTypeDef = TypedDict(
    "SendDataToWirelessDeviceResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ServiceProfileTypeDef = TypedDict(
    "ServiceProfileTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Id": NotRequired[str],
    },
)

SessionKeysAbpV1_0_xTypeDef = TypedDict(
    "SessionKeysAbpV1_0_xTypeDef",
    {
        "NwkSKey": NotRequired[str],
        "AppSKey": NotRequired[str],
    },
)

SessionKeysAbpV1_1TypeDef = TypedDict(
    "SessionKeysAbpV1_1TypeDef",
    {
        "FNwkSIntKey": NotRequired[str],
        "SNwkSIntKey": NotRequired[str],
        "NwkSEncKey": NotRequired[str],
        "AppSKey": NotRequired[str],
    },
)

SidewalkAccountInfoTypeDef = TypedDict(
    "SidewalkAccountInfoTypeDef",
    {
        "AmazonId": NotRequired[str],
        "AppServerPrivateKey": NotRequired[str],
    },
)

SidewalkAccountInfoWithFingerprintTypeDef = TypedDict(
    "SidewalkAccountInfoWithFingerprintTypeDef",
    {
        "AmazonId": NotRequired[str],
        "Fingerprint": NotRequired[str],
        "Arn": NotRequired[str],
    },
)

SidewalkDeviceMetadataTypeDef = TypedDict(
    "SidewalkDeviceMetadataTypeDef",
    {
        "Rssi": NotRequired[int],
        "BatteryLevel": NotRequired[BatteryLevelType],
        "Event": NotRequired[EventType],
        "DeviceState": NotRequired[DeviceStateType],
    },
)

SidewalkDeviceTypeDef = TypedDict(
    "SidewalkDeviceTypeDef",
    {
        "AmazonId": NotRequired[str],
        "SidewalkId": NotRequired[str],
        "SidewalkManufacturingSn": NotRequired[str],
        "DeviceCertificates": NotRequired[List["CertificateListTypeDef"]],
    },
)

SidewalkEventNotificationConfigurationsTypeDef = TypedDict(
    "SidewalkEventNotificationConfigurationsTypeDef",
    {
        "AmazonIdEventTopic": NotRequired[EventNotificationTopicStatusType],
    },
)

SidewalkListDeviceTypeDef = TypedDict(
    "SidewalkListDeviceTypeDef",
    {
        "AmazonId": NotRequired[str],
        "SidewalkId": NotRequired[str],
        "SidewalkManufacturingSn": NotRequired[str],
        "DeviceCertificates": NotRequired[List["CertificateListTypeDef"]],
    },
)

SidewalkSendDataToDeviceTypeDef = TypedDict(
    "SidewalkSendDataToDeviceTypeDef",
    {
        "Seq": NotRequired[int],
        "MessageType": NotRequired[MessageTypeType],
    },
)

SidewalkUpdateAccountTypeDef = TypedDict(
    "SidewalkUpdateAccountTypeDef",
    {
        "AppServerPrivateKey": NotRequired[str],
    },
)

StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef = TypedDict(
    "StartBulkAssociateWirelessDeviceWithMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "QueryString": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef = TypedDict(
    "StartBulkDisassociateWirelessDeviceFromMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "QueryString": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

StartFuotaTaskRequestRequestTypeDef = TypedDict(
    "StartFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "LoRaWAN": NotRequired["LoRaWANStartFuotaTaskTypeDef"],
    },
)

StartMulticastGroupSessionRequestRequestTypeDef = TypedDict(
    "StartMulticastGroupSessionRequestRequestTypeDef",
    {
        "Id": str,
        "LoRaWAN": "LoRaWANMulticastSessionTypeDef",
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

TestWirelessDeviceRequestRequestTypeDef = TypedDict(
    "TestWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
    },
)

TestWirelessDeviceResponseTypeDef = TypedDict(
    "TestWirelessDeviceResponseTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TraceContentTypeDef = TypedDict(
    "TraceContentTypeDef",
    {
        "WirelessDeviceFrameInfo": NotRequired[WirelessDeviceFrameInfoType],
        "LogLevel": NotRequired[LogLevelType],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateDestinationRequestRequestTypeDef = TypedDict(
    "UpdateDestinationRequestRequestTypeDef",
    {
        "Name": str,
        "ExpressionType": NotRequired[ExpressionTypeType],
        "Expression": NotRequired[str],
        "Description": NotRequired[str],
        "RoleArn": NotRequired[str],
    },
)

UpdateFuotaTaskRequestRequestTypeDef = TypedDict(
    "UpdateFuotaTaskRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANFuotaTaskTypeDef"],
        "FirmwareUpdateImage": NotRequired[str],
        "FirmwareUpdateRole": NotRequired[str],
    },
)

UpdateLogLevelsByResourceTypesRequestRequestTypeDef = TypedDict(
    "UpdateLogLevelsByResourceTypesRequestRequestTypeDef",
    {
        "DefaultLogLevel": NotRequired[LogLevelType],
        "WirelessDeviceLogOptions": NotRequired[Sequence["WirelessDeviceLogOptionTypeDef"]],
        "WirelessGatewayLogOptions": NotRequired[Sequence["WirelessGatewayLogOptionTypeDef"]],
    },
)

UpdateMulticastGroupRequestRequestTypeDef = TypedDict(
    "UpdateMulticastGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANMulticastTypeDef"],
    },
)

UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateNetworkAnalyzerConfigurationRequestRequestTypeDef",
    {
        "ConfigurationName": str,
        "TraceContent": NotRequired["TraceContentTypeDef"],
        "WirelessDevicesToAdd": NotRequired[Sequence[str]],
        "WirelessDevicesToRemove": NotRequired[Sequence[str]],
        "WirelessGatewaysToAdd": NotRequired[Sequence[str]],
        "WirelessGatewaysToRemove": NotRequired[Sequence[str]],
    },
)

UpdatePartnerAccountRequestRequestTypeDef = TypedDict(
    "UpdatePartnerAccountRequestRequestTypeDef",
    {
        "Sidewalk": "SidewalkUpdateAccountTypeDef",
        "PartnerAccountId": str,
        "PartnerType": Literal["Sidewalk"],
    },
)

UpdateResourceEventConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateResourceEventConfigurationRequestRequestTypeDef",
    {
        "Identifier": str,
        "IdentifierType": Literal["PartnerAccountId"],
        "PartnerType": NotRequired[Literal["Sidewalk"]],
        "DeviceRegistrationState": NotRequired["DeviceRegistrationStateEventConfigurationTypeDef"],
        "Proximity": NotRequired["ProximityEventConfigurationTypeDef"],
    },
)

UpdateWirelessDeviceRequestRequestTypeDef = TypedDict(
    "UpdateWirelessDeviceRequestRequestTypeDef",
    {
        "Id": str,
        "DestinationName": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANUpdateDeviceTypeDef"],
    },
)

UpdateWirelessGatewayRequestRequestTypeDef = TypedDict(
    "UpdateWirelessGatewayRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "JoinEuiFilters": NotRequired[Sequence[Sequence[str]]],
        "NetIdFilters": NotRequired[Sequence[str]],
    },
)

UpdateWirelessGatewayTaskCreateTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskCreateTypeDef",
    {
        "UpdateDataSource": NotRequired[str],
        "UpdateDataRole": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANUpdateGatewayTaskCreateTypeDef"],
    },
)

UpdateWirelessGatewayTaskEntryTypeDef = TypedDict(
    "UpdateWirelessGatewayTaskEntryTypeDef",
    {
        "Id": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANUpdateGatewayTaskEntryTypeDef"],
        "Arn": NotRequired[str],
    },
)

WirelessDeviceEventLogOptionTypeDef = TypedDict(
    "WirelessDeviceEventLogOptionTypeDef",
    {
        "Event": WirelessDeviceEventType,
        "LogLevel": LogLevelType,
    },
)

WirelessDeviceLogOptionTypeDef = TypedDict(
    "WirelessDeviceLogOptionTypeDef",
    {
        "Type": WirelessDeviceTypeType,
        "LogLevel": LogLevelType,
        "Events": NotRequired[List["WirelessDeviceEventLogOptionTypeDef"]],
    },
)

WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[WirelessDeviceTypeType],
        "Name": NotRequired[str],
        "DestinationName": NotRequired[str],
        "LastUplinkReceivedAt": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANListDeviceTypeDef"],
        "Sidewalk": NotRequired["SidewalkListDeviceTypeDef"],
        "FuotaDeviceStatus": NotRequired[FuotaDeviceStatusType],
        "MulticastDeviceStatus": NotRequired[str],
        "McGroupId": NotRequired[int],
    },
)

WirelessGatewayEventLogOptionTypeDef = TypedDict(
    "WirelessGatewayEventLogOptionTypeDef",
    {
        "Event": WirelessGatewayEventType,
        "LogLevel": LogLevelType,
    },
)

WirelessGatewayLogOptionTypeDef = TypedDict(
    "WirelessGatewayLogOptionTypeDef",
    {
        "Type": Literal["LoRaWAN"],
        "LogLevel": LogLevelType,
        "Events": NotRequired[List["WirelessGatewayEventLogOptionTypeDef"]],
    },
)

WirelessGatewayStatisticsTypeDef = TypedDict(
    "WirelessGatewayStatisticsTypeDef",
    {
        "Arn": NotRequired[str],
        "Id": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "LoRaWAN": NotRequired["LoRaWANGatewayTypeDef"],
        "LastUplinkReceivedAt": NotRequired[str],
    },
)

WirelessMetadataTypeDef = TypedDict(
    "WirelessMetadataTypeDef",
    {
        "LoRaWAN": NotRequired["LoRaWANSendDataToDeviceTypeDef"],
        "Sidewalk": NotRequired["SidewalkSendDataToDeviceTypeDef"],
    },
)
