"""
Type annotations for alexaforbusiness service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_alexaforbusiness/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_alexaforbusiness.type_defs import AddressBookDataTypeDef

    data: AddressBookDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    BusinessReportFailureCodeType,
    BusinessReportFormatType,
    BusinessReportIntervalType,
    BusinessReportStatusType,
    CommsProtocolType,
    ConferenceProviderTypeType,
    ConnectionStatusType,
    DeviceEventTypeType,
    DeviceStatusDetailCodeType,
    DeviceStatusType,
    DistanceUnitType,
    EnablementTypeFilterType,
    EnablementTypeType,
    EndOfMeetingReminderTypeType,
    EnrollmentStatusType,
    FeatureType,
    NetworkSecurityTypeType,
    PhoneNumberTypeType,
    RequirePinType,
    SkillTypeFilterType,
    SkillTypeType,
    SortValueType,
    TemperatureUnitType,
    WakeWordType,
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
    "AddressBookDataTypeDef",
    "AddressBookTypeDef",
    "ApproveSkillRequestRequestTypeDef",
    "AssociateContactWithAddressBookRequestRequestTypeDef",
    "AssociateDeviceWithNetworkProfileRequestRequestTypeDef",
    "AssociateDeviceWithRoomRequestRequestTypeDef",
    "AssociateSkillGroupWithRoomRequestRequestTypeDef",
    "AssociateSkillWithSkillGroupRequestRequestTypeDef",
    "AssociateSkillWithUsersRequestRequestTypeDef",
    "AudioTypeDef",
    "BusinessReportContentRangeTypeDef",
    "BusinessReportRecurrenceTypeDef",
    "BusinessReportS3LocationTypeDef",
    "BusinessReportScheduleTypeDef",
    "BusinessReportTypeDef",
    "CategoryTypeDef",
    "ConferencePreferenceTypeDef",
    "ConferenceProviderTypeDef",
    "ContactDataTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateAddressBookRequestRequestTypeDef",
    "CreateAddressBookResponseTypeDef",
    "CreateBusinessReportScheduleRequestRequestTypeDef",
    "CreateBusinessReportScheduleResponseTypeDef",
    "CreateConferenceProviderRequestRequestTypeDef",
    "CreateConferenceProviderResponseTypeDef",
    "CreateContactRequestRequestTypeDef",
    "CreateContactResponseTypeDef",
    "CreateEndOfMeetingReminderTypeDef",
    "CreateGatewayGroupRequestRequestTypeDef",
    "CreateGatewayGroupResponseTypeDef",
    "CreateInstantBookingTypeDef",
    "CreateMeetingRoomConfigurationTypeDef",
    "CreateNetworkProfileRequestRequestTypeDef",
    "CreateNetworkProfileResponseTypeDef",
    "CreateProfileRequestRequestTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateRequireCheckInTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSkillGroupRequestRequestTypeDef",
    "CreateSkillGroupResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "DeleteAddressBookRequestRequestTypeDef",
    "DeleteBusinessReportScheduleRequestRequestTypeDef",
    "DeleteConferenceProviderRequestRequestTypeDef",
    "DeleteContactRequestRequestTypeDef",
    "DeleteDeviceRequestRequestTypeDef",
    "DeleteDeviceUsageDataRequestRequestTypeDef",
    "DeleteGatewayGroupRequestRequestTypeDef",
    "DeleteNetworkProfileRequestRequestTypeDef",
    "DeleteProfileRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DeleteRoomSkillParameterRequestRequestTypeDef",
    "DeleteSkillAuthorizationRequestRequestTypeDef",
    "DeleteSkillGroupRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeveloperInfoTypeDef",
    "DeviceDataTypeDef",
    "DeviceEventTypeDef",
    "DeviceNetworkProfileInfoTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceTypeDef",
    "DisassociateContactFromAddressBookRequestRequestTypeDef",
    "DisassociateDeviceFromRoomRequestRequestTypeDef",
    "DisassociateSkillFromSkillGroupRequestRequestTypeDef",
    "DisassociateSkillFromUsersRequestRequestTypeDef",
    "DisassociateSkillGroupFromRoomRequestRequestTypeDef",
    "EndOfMeetingReminderTypeDef",
    "FilterTypeDef",
    "ForgetSmartHomeAppliancesRequestRequestTypeDef",
    "GatewayGroupSummaryTypeDef",
    "GatewayGroupTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTypeDef",
    "GetAddressBookRequestRequestTypeDef",
    "GetAddressBookResponseTypeDef",
    "GetConferencePreferenceResponseTypeDef",
    "GetConferenceProviderRequestRequestTypeDef",
    "GetConferenceProviderResponseTypeDef",
    "GetContactRequestRequestTypeDef",
    "GetContactResponseTypeDef",
    "GetDeviceRequestRequestTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGatewayGroupRequestRequestTypeDef",
    "GetGatewayGroupResponseTypeDef",
    "GetGatewayRequestRequestTypeDef",
    "GetGatewayResponseTypeDef",
    "GetInvitationConfigurationResponseTypeDef",
    "GetNetworkProfileRequestRequestTypeDef",
    "GetNetworkProfileResponseTypeDef",
    "GetProfileRequestRequestTypeDef",
    "GetProfileResponseTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "GetRoomSkillParameterRequestRequestTypeDef",
    "GetRoomSkillParameterResponseTypeDef",
    "GetSkillGroupRequestRequestTypeDef",
    "GetSkillGroupResponseTypeDef",
    "IPDialInTypeDef",
    "InstantBookingTypeDef",
    "ListBusinessReportSchedulesRequestRequestTypeDef",
    "ListBusinessReportSchedulesResponseTypeDef",
    "ListConferenceProvidersRequestRequestTypeDef",
    "ListConferenceProvidersResponseTypeDef",
    "ListDeviceEventsRequestRequestTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListGatewayGroupsRequestRequestTypeDef",
    "ListGatewayGroupsResponseTypeDef",
    "ListGatewaysRequestRequestTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListSkillsRequestRequestTypeDef",
    "ListSkillsResponseTypeDef",
    "ListSkillsStoreCategoriesRequestRequestTypeDef",
    "ListSkillsStoreCategoriesResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryRequestRequestTypeDef",
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ListSmartHomeAppliancesRequestRequestTypeDef",
    "ListSmartHomeAppliancesResponseTypeDef",
    "ListTagsRequestRequestTypeDef",
    "ListTagsResponseTypeDef",
    "MeetingRoomConfigurationTypeDef",
    "MeetingSettingTypeDef",
    "NetworkProfileDataTypeDef",
    "NetworkProfileTypeDef",
    "PSTNDialInTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ProfileDataTypeDef",
    "ProfileTypeDef",
    "PutConferencePreferenceRequestRequestTypeDef",
    "PutInvitationConfigurationRequestRequestTypeDef",
    "PutRoomSkillParameterRequestRequestTypeDef",
    "PutSkillAuthorizationRequestRequestTypeDef",
    "RegisterAVSDeviceRequestRequestTypeDef",
    "RegisterAVSDeviceResponseTypeDef",
    "RejectSkillRequestRequestTypeDef",
    "RequireCheckInTypeDef",
    "ResolveRoomRequestRequestTypeDef",
    "ResolveRoomResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RevokeInvitationRequestRequestTypeDef",
    "RoomDataTypeDef",
    "RoomSkillParameterTypeDef",
    "RoomTypeDef",
    "SearchAddressBooksRequestRequestTypeDef",
    "SearchAddressBooksResponseTypeDef",
    "SearchContactsRequestRequestTypeDef",
    "SearchContactsResponseTypeDef",
    "SearchDevicesRequestRequestTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchNetworkProfilesRequestRequestTypeDef",
    "SearchNetworkProfilesResponseTypeDef",
    "SearchProfilesRequestRequestTypeDef",
    "SearchProfilesResponseTypeDef",
    "SearchRoomsRequestRequestTypeDef",
    "SearchRoomsResponseTypeDef",
    "SearchSkillGroupsRequestRequestTypeDef",
    "SearchSkillGroupsResponseTypeDef",
    "SearchUsersRequestRequestTypeDef",
    "SearchUsersResponseTypeDef",
    "SendAnnouncementRequestRequestTypeDef",
    "SendAnnouncementResponseTypeDef",
    "SendInvitationRequestRequestTypeDef",
    "SipAddressTypeDef",
    "SkillDetailsTypeDef",
    "SkillGroupDataTypeDef",
    "SkillGroupTypeDef",
    "SkillSummaryTypeDef",
    "SkillsStoreSkillTypeDef",
    "SmartHomeApplianceTypeDef",
    "SortTypeDef",
    "SsmlTypeDef",
    "StartDeviceSyncRequestRequestTypeDef",
    "StartSmartHomeApplianceDiscoveryRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TextTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAddressBookRequestRequestTypeDef",
    "UpdateBusinessReportScheduleRequestRequestTypeDef",
    "UpdateConferenceProviderRequestRequestTypeDef",
    "UpdateContactRequestRequestTypeDef",
    "UpdateDeviceRequestRequestTypeDef",
    "UpdateEndOfMeetingReminderTypeDef",
    "UpdateGatewayGroupRequestRequestTypeDef",
    "UpdateGatewayRequestRequestTypeDef",
    "UpdateInstantBookingTypeDef",
    "UpdateMeetingRoomConfigurationTypeDef",
    "UpdateNetworkProfileRequestRequestTypeDef",
    "UpdateProfileRequestRequestTypeDef",
    "UpdateRequireCheckInTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateSkillGroupRequestRequestTypeDef",
    "UserDataTypeDef",
)

AddressBookDataTypeDef = TypedDict(
    "AddressBookDataTypeDef",
    {
        "AddressBookArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

AddressBookTypeDef = TypedDict(
    "AddressBookTypeDef",
    {
        "AddressBookArn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

ApproveSkillRequestRequestTypeDef = TypedDict(
    "ApproveSkillRequestRequestTypeDef",
    {
        "SkillId": str,
    },
)

AssociateContactWithAddressBookRequestRequestTypeDef = TypedDict(
    "AssociateContactWithAddressBookRequestRequestTypeDef",
    {
        "ContactArn": str,
        "AddressBookArn": str,
    },
)

AssociateDeviceWithNetworkProfileRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithNetworkProfileRequestRequestTypeDef",
    {
        "DeviceArn": str,
        "NetworkProfileArn": str,
    },
)

AssociateDeviceWithRoomRequestRequestTypeDef = TypedDict(
    "AssociateDeviceWithRoomRequestRequestTypeDef",
    {
        "DeviceArn": NotRequired[str],
        "RoomArn": NotRequired[str],
    },
)

AssociateSkillGroupWithRoomRequestRequestTypeDef = TypedDict(
    "AssociateSkillGroupWithRoomRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "RoomArn": NotRequired[str],
    },
)

AssociateSkillWithSkillGroupRequestRequestTypeDef = TypedDict(
    "AssociateSkillWithSkillGroupRequestRequestTypeDef",
    {
        "SkillId": str,
        "SkillGroupArn": NotRequired[str],
    },
)

AssociateSkillWithUsersRequestRequestTypeDef = TypedDict(
    "AssociateSkillWithUsersRequestRequestTypeDef",
    {
        "SkillId": str,
    },
)

AudioTypeDef = TypedDict(
    "AudioTypeDef",
    {
        "Locale": Literal["en-US"],
        "Location": str,
    },
)

BusinessReportContentRangeTypeDef = TypedDict(
    "BusinessReportContentRangeTypeDef",
    {
        "Interval": BusinessReportIntervalType,
    },
)

BusinessReportRecurrenceTypeDef = TypedDict(
    "BusinessReportRecurrenceTypeDef",
    {
        "StartDate": NotRequired[str],
    },
)

BusinessReportS3LocationTypeDef = TypedDict(
    "BusinessReportS3LocationTypeDef",
    {
        "Path": NotRequired[str],
        "BucketName": NotRequired[str],
    },
)

BusinessReportScheduleTypeDef = TypedDict(
    "BusinessReportScheduleTypeDef",
    {
        "ScheduleArn": NotRequired[str],
        "ScheduleName": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "Format": NotRequired[BusinessReportFormatType],
        "ContentRange": NotRequired["BusinessReportContentRangeTypeDef"],
        "Recurrence": NotRequired["BusinessReportRecurrenceTypeDef"],
        "LastBusinessReport": NotRequired["BusinessReportTypeDef"],
    },
)

BusinessReportTypeDef = TypedDict(
    "BusinessReportTypeDef",
    {
        "Status": NotRequired[BusinessReportStatusType],
        "FailureCode": NotRequired[BusinessReportFailureCodeType],
        "S3Location": NotRequired["BusinessReportS3LocationTypeDef"],
        "DeliveryTime": NotRequired[datetime],
        "DownloadUrl": NotRequired[str],
    },
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef",
    {
        "CategoryId": NotRequired[int],
        "CategoryName": NotRequired[str],
    },
)

ConferencePreferenceTypeDef = TypedDict(
    "ConferencePreferenceTypeDef",
    {
        "DefaultConferenceProviderArn": NotRequired[str],
    },
)

ConferenceProviderTypeDef = TypedDict(
    "ConferenceProviderTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Type": NotRequired[ConferenceProviderTypeType],
        "IPDialIn": NotRequired["IPDialInTypeDef"],
        "PSTNDialIn": NotRequired["PSTNDialInTypeDef"],
        "MeetingSetting": NotRequired["MeetingSettingTypeDef"],
    },
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "ContactArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "PhoneNumbers": NotRequired[List["PhoneNumberTypeDef"]],
        "SipAddresses": NotRequired[List["SipAddressTypeDef"]],
    },
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": NotRequired[str],
        "DisplayName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "PhoneNumbers": NotRequired[List["PhoneNumberTypeDef"]],
        "SipAddresses": NotRequired[List["SipAddressTypeDef"]],
    },
)

ContentTypeDef = TypedDict(
    "ContentTypeDef",
    {
        "TextList": NotRequired[Sequence["TextTypeDef"]],
        "SsmlList": NotRequired[Sequence["SsmlTypeDef"]],
        "AudioList": NotRequired[Sequence["AudioTypeDef"]],
    },
)

CreateAddressBookRequestRequestTypeDef = TypedDict(
    "CreateAddressBookRequestRequestTypeDef",
    {
        "Name": str,
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAddressBookResponseTypeDef = TypedDict(
    "CreateAddressBookResponseTypeDef",
    {
        "AddressBookArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBusinessReportScheduleRequestRequestTypeDef = TypedDict(
    "CreateBusinessReportScheduleRequestRequestTypeDef",
    {
        "Format": BusinessReportFormatType,
        "ContentRange": "BusinessReportContentRangeTypeDef",
        "ScheduleName": NotRequired[str],
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "Recurrence": NotRequired["BusinessReportRecurrenceTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "CreateBusinessReportScheduleResponseTypeDef",
    {
        "ScheduleArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateConferenceProviderRequestRequestTypeDef = TypedDict(
    "CreateConferenceProviderRequestRequestTypeDef",
    {
        "ConferenceProviderName": str,
        "ConferenceProviderType": ConferenceProviderTypeType,
        "MeetingSetting": "MeetingSettingTypeDef",
        "IPDialIn": NotRequired["IPDialInTypeDef"],
        "PSTNDialIn": NotRequired["PSTNDialInTypeDef"],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateConferenceProviderResponseTypeDef = TypedDict(
    "CreateConferenceProviderResponseTypeDef",
    {
        "ConferenceProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateContactRequestRequestTypeDef = TypedDict(
    "CreateContactRequestRequestTypeDef",
    {
        "FirstName": str,
        "DisplayName": NotRequired[str],
        "LastName": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "PhoneNumbers": NotRequired[Sequence["PhoneNumberTypeDef"]],
        "SipAddresses": NotRequired[Sequence["SipAddressTypeDef"]],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateContactResponseTypeDef = TypedDict(
    "CreateContactResponseTypeDef",
    {
        "ContactArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateEndOfMeetingReminderTypeDef = TypedDict(
    "CreateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": Sequence[int],
        "ReminderType": EndOfMeetingReminderTypeType,
        "Enabled": bool,
    },
)

CreateGatewayGroupRequestRequestTypeDef = TypedDict(
    "CreateGatewayGroupRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateGatewayGroupResponseTypeDef = TypedDict(
    "CreateGatewayGroupResponseTypeDef",
    {
        "GatewayGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstantBookingTypeDef = TypedDict(
    "CreateInstantBookingTypeDef",
    {
        "DurationInMinutes": int,
        "Enabled": bool,
    },
)

CreateMeetingRoomConfigurationTypeDef = TypedDict(
    "CreateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": NotRequired[bool],
        "EndOfMeetingReminder": NotRequired["CreateEndOfMeetingReminderTypeDef"],
        "InstantBooking": NotRequired["CreateInstantBookingTypeDef"],
        "RequireCheckIn": NotRequired["CreateRequireCheckInTypeDef"],
    },
)

CreateNetworkProfileRequestRequestTypeDef = TypedDict(
    "CreateNetworkProfileRequestRequestTypeDef",
    {
        "NetworkProfileName": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityTypeType,
        "ClientRequestToken": str,
        "Description": NotRequired[str],
        "EapMethod": NotRequired[Literal["EAP_TLS"]],
        "CurrentPassword": NotRequired[str],
        "NextPassword": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "TrustAnchors": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateNetworkProfileResponseTypeDef = TypedDict(
    "CreateNetworkProfileResponseTypeDef",
    {
        "NetworkProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProfileRequestRequestTypeDef = TypedDict(
    "CreateProfileRequestRequestTypeDef",
    {
        "ProfileName": str,
        "Timezone": str,
        "Address": str,
        "DistanceUnit": DistanceUnitType,
        "TemperatureUnit": TemperatureUnitType,
        "WakeWord": WakeWordType,
        "Locale": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "SetupModeDisabled": NotRequired[bool],
        "MaxVolumeLimit": NotRequired[int],
        "PSTNEnabled": NotRequired[bool],
        "DataRetentionOptIn": NotRequired[bool],
        "MeetingRoomConfiguration": NotRequired["CreateMeetingRoomConfigurationTypeDef"],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef",
    {
        "ProfileArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRequireCheckInTypeDef = TypedDict(
    "CreateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": int,
        "Enabled": bool,
    },
)

CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "RoomName": str,
        "Description": NotRequired[str],
        "ProfileArn": NotRequired[str],
        "ProviderCalendarId": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "RoomArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSkillGroupRequestRequestTypeDef = TypedDict(
    "CreateSkillGroupRequestRequestTypeDef",
    {
        "SkillGroupName": str,
        "Description": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateSkillGroupResponseTypeDef = TypedDict(
    "CreateSkillGroupResponseTypeDef",
    {
        "SkillGroupArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserId": str,
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "Email": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "UserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAddressBookRequestRequestTypeDef = TypedDict(
    "DeleteAddressBookRequestRequestTypeDef",
    {
        "AddressBookArn": str,
    },
)

DeleteBusinessReportScheduleRequestRequestTypeDef = TypedDict(
    "DeleteBusinessReportScheduleRequestRequestTypeDef",
    {
        "ScheduleArn": str,
    },
)

DeleteConferenceProviderRequestRequestTypeDef = TypedDict(
    "DeleteConferenceProviderRequestRequestTypeDef",
    {
        "ConferenceProviderArn": str,
    },
)

DeleteContactRequestRequestTypeDef = TypedDict(
    "DeleteContactRequestRequestTypeDef",
    {
        "ContactArn": str,
    },
)

DeleteDeviceRequestRequestTypeDef = TypedDict(
    "DeleteDeviceRequestRequestTypeDef",
    {
        "DeviceArn": str,
    },
)

DeleteDeviceUsageDataRequestRequestTypeDef = TypedDict(
    "DeleteDeviceUsageDataRequestRequestTypeDef",
    {
        "DeviceArn": str,
        "DeviceUsageType": Literal["VOICE"],
    },
)

DeleteGatewayGroupRequestRequestTypeDef = TypedDict(
    "DeleteGatewayGroupRequestRequestTypeDef",
    {
        "GatewayGroupArn": str,
    },
)

DeleteNetworkProfileRequestRequestTypeDef = TypedDict(
    "DeleteNetworkProfileRequestRequestTypeDef",
    {
        "NetworkProfileArn": str,
    },
)

DeleteProfileRequestRequestTypeDef = TypedDict(
    "DeleteProfileRequestRequestTypeDef",
    {
        "ProfileArn": NotRequired[str],
    },
)

DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "RoomArn": NotRequired[str],
    },
)

DeleteRoomSkillParameterRequestRequestTypeDef = TypedDict(
    "DeleteRoomSkillParameterRequestRequestTypeDef",
    {
        "SkillId": str,
        "ParameterKey": str,
        "RoomArn": NotRequired[str],
    },
)

DeleteSkillAuthorizationRequestRequestTypeDef = TypedDict(
    "DeleteSkillAuthorizationRequestRequestTypeDef",
    {
        "SkillId": str,
        "RoomArn": NotRequired[str],
    },
)

DeleteSkillGroupRequestRequestTypeDef = TypedDict(
    "DeleteSkillGroupRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
    },
)

DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "EnrollmentId": str,
        "UserArn": NotRequired[str],
    },
)

DeveloperInfoTypeDef = TypedDict(
    "DeveloperInfoTypeDef",
    {
        "DeveloperName": NotRequired[str],
        "PrivacyPolicy": NotRequired[str],
        "Email": NotRequired[str],
        "Url": NotRequired[str],
    },
)

DeviceDataTypeDef = TypedDict(
    "DeviceDataTypeDef",
    {
        "DeviceArn": NotRequired[str],
        "DeviceSerialNumber": NotRequired[str],
        "DeviceType": NotRequired[str],
        "DeviceName": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
        "MacAddress": NotRequired[str],
        "DeviceStatus": NotRequired[DeviceStatusType],
        "NetworkProfileArn": NotRequired[str],
        "NetworkProfileName": NotRequired[str],
        "RoomArn": NotRequired[str],
        "RoomName": NotRequired[str],
        "DeviceStatusInfo": NotRequired["DeviceStatusInfoTypeDef"],
        "CreatedTime": NotRequired[datetime],
    },
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {
        "Type": NotRequired[DeviceEventTypeType],
        "Value": NotRequired[str],
        "Timestamp": NotRequired[datetime],
    },
)

DeviceNetworkProfileInfoTypeDef = TypedDict(
    "DeviceNetworkProfileInfoTypeDef",
    {
        "NetworkProfileArn": NotRequired[str],
        "CertificateArn": NotRequired[str],
        "CertificateExpirationTime": NotRequired[datetime],
    },
)

DeviceStatusDetailTypeDef = TypedDict(
    "DeviceStatusDetailTypeDef",
    {
        "Feature": NotRequired[FeatureType],
        "Code": NotRequired[DeviceStatusDetailCodeType],
    },
)

DeviceStatusInfoTypeDef = TypedDict(
    "DeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": NotRequired[List["DeviceStatusDetailTypeDef"]],
        "ConnectionStatus": NotRequired[ConnectionStatusType],
        "ConnectionStatusUpdatedTime": NotRequired[datetime],
    },
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceArn": NotRequired[str],
        "DeviceSerialNumber": NotRequired[str],
        "DeviceType": NotRequired[str],
        "DeviceName": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
        "MacAddress": NotRequired[str],
        "RoomArn": NotRequired[str],
        "DeviceStatus": NotRequired[DeviceStatusType],
        "DeviceStatusInfo": NotRequired["DeviceStatusInfoTypeDef"],
        "NetworkProfileInfo": NotRequired["DeviceNetworkProfileInfoTypeDef"],
    },
)

DisassociateContactFromAddressBookRequestRequestTypeDef = TypedDict(
    "DisassociateContactFromAddressBookRequestRequestTypeDef",
    {
        "ContactArn": str,
        "AddressBookArn": str,
    },
)

DisassociateDeviceFromRoomRequestRequestTypeDef = TypedDict(
    "DisassociateDeviceFromRoomRequestRequestTypeDef",
    {
        "DeviceArn": NotRequired[str],
    },
)

DisassociateSkillFromSkillGroupRequestRequestTypeDef = TypedDict(
    "DisassociateSkillFromSkillGroupRequestRequestTypeDef",
    {
        "SkillId": str,
        "SkillGroupArn": NotRequired[str],
    },
)

DisassociateSkillFromUsersRequestRequestTypeDef = TypedDict(
    "DisassociateSkillFromUsersRequestRequestTypeDef",
    {
        "SkillId": str,
    },
)

DisassociateSkillGroupFromRoomRequestRequestTypeDef = TypedDict(
    "DisassociateSkillGroupFromRoomRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "RoomArn": NotRequired[str],
    },
)

EndOfMeetingReminderTypeDef = TypedDict(
    "EndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": NotRequired[List[int]],
        "ReminderType": NotRequired[EndOfMeetingReminderTypeType],
        "Enabled": NotRequired[bool],
    },
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Key": str,
        "Values": Sequence[str],
    },
)

ForgetSmartHomeAppliancesRequestRequestTypeDef = TypedDict(
    "ForgetSmartHomeAppliancesRequestRequestTypeDef",
    {
        "RoomArn": str,
    },
)

GatewayGroupSummaryTypeDef = TypedDict(
    "GatewayGroupSummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

GatewayGroupTypeDef = TypedDict(
    "GatewayGroupTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

GatewaySummaryTypeDef = TypedDict(
    "GatewaySummaryTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "GatewayGroupArn": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
    },
)

GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "GatewayGroupArn": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
    },
)

GetAddressBookRequestRequestTypeDef = TypedDict(
    "GetAddressBookRequestRequestTypeDef",
    {
        "AddressBookArn": str,
    },
)

GetAddressBookResponseTypeDef = TypedDict(
    "GetAddressBookResponseTypeDef",
    {
        "AddressBook": "AddressBookTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConferencePreferenceResponseTypeDef = TypedDict(
    "GetConferencePreferenceResponseTypeDef",
    {
        "Preference": "ConferencePreferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConferenceProviderRequestRequestTypeDef = TypedDict(
    "GetConferenceProviderRequestRequestTypeDef",
    {
        "ConferenceProviderArn": str,
    },
)

GetConferenceProviderResponseTypeDef = TypedDict(
    "GetConferenceProviderResponseTypeDef",
    {
        "ConferenceProvider": "ConferenceProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetContactRequestRequestTypeDef = TypedDict(
    "GetContactRequestRequestTypeDef",
    {
        "ContactArn": str,
    },
)

GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef",
    {
        "Contact": "ContactTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDeviceRequestRequestTypeDef = TypedDict(
    "GetDeviceRequestRequestTypeDef",
    {
        "DeviceArn": NotRequired[str],
    },
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "Device": "DeviceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGatewayGroupRequestRequestTypeDef = TypedDict(
    "GetGatewayGroupRequestRequestTypeDef",
    {
        "GatewayGroupArn": str,
    },
)

GetGatewayGroupResponseTypeDef = TypedDict(
    "GetGatewayGroupResponseTypeDef",
    {
        "GatewayGroup": "GatewayGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGatewayRequestRequestTypeDef = TypedDict(
    "GetGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
    },
)

GetGatewayResponseTypeDef = TypedDict(
    "GetGatewayResponseTypeDef",
    {
        "Gateway": "GatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetInvitationConfigurationResponseTypeDef = TypedDict(
    "GetInvitationConfigurationResponseTypeDef",
    {
        "OrganizationName": str,
        "ContactEmail": str,
        "PrivateSkillIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkProfileRequestRequestTypeDef = TypedDict(
    "GetNetworkProfileRequestRequestTypeDef",
    {
        "NetworkProfileArn": str,
    },
)

GetNetworkProfileResponseTypeDef = TypedDict(
    "GetNetworkProfileResponseTypeDef",
    {
        "NetworkProfile": "NetworkProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProfileRequestRequestTypeDef = TypedDict(
    "GetProfileRequestRequestTypeDef",
    {
        "ProfileArn": NotRequired[str],
    },
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef",
    {
        "Profile": "ProfileTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "RoomArn": NotRequired[str],
    },
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomSkillParameterRequestRequestTypeDef = TypedDict(
    "GetRoomSkillParameterRequestRequestTypeDef",
    {
        "SkillId": str,
        "ParameterKey": str,
        "RoomArn": NotRequired[str],
    },
)

GetRoomSkillParameterResponseTypeDef = TypedDict(
    "GetRoomSkillParameterResponseTypeDef",
    {
        "RoomSkillParameter": "RoomSkillParameterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSkillGroupRequestRequestTypeDef = TypedDict(
    "GetSkillGroupRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
    },
)

GetSkillGroupResponseTypeDef = TypedDict(
    "GetSkillGroupResponseTypeDef",
    {
        "SkillGroup": "SkillGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IPDialInTypeDef = TypedDict(
    "IPDialInTypeDef",
    {
        "Endpoint": str,
        "CommsProtocol": CommsProtocolType,
    },
)

InstantBookingTypeDef = TypedDict(
    "InstantBookingTypeDef",
    {
        "DurationInMinutes": NotRequired[int],
        "Enabled": NotRequired[bool],
    },
)

ListBusinessReportSchedulesRequestRequestTypeDef = TypedDict(
    "ListBusinessReportSchedulesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "ListBusinessReportSchedulesResponseTypeDef",
    {
        "BusinessReportSchedules": List["BusinessReportScheduleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListConferenceProvidersRequestRequestTypeDef = TypedDict(
    "ListConferenceProvidersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListConferenceProvidersResponseTypeDef = TypedDict(
    "ListConferenceProvidersResponseTypeDef",
    {
        "ConferenceProviders": List["ConferenceProviderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDeviceEventsRequestRequestTypeDef = TypedDict(
    "ListDeviceEventsRequestRequestTypeDef",
    {
        "DeviceArn": str,
        "EventType": NotRequired[DeviceEventTypeType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {
        "DeviceEvents": List["DeviceEventTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewayGroupsRequestRequestTypeDef = TypedDict(
    "ListGatewayGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGatewayGroupsResponseTypeDef = TypedDict(
    "ListGatewayGroupsResponseTypeDef",
    {
        "GatewayGroups": List["GatewayGroupSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysRequestRequestTypeDef = TypedDict(
    "ListGatewaysRequestRequestTypeDef",
    {
        "GatewayGroupArn": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {
        "Gateways": List["GatewaySummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSkillsRequestRequestTypeDef = TypedDict(
    "ListSkillsRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "EnablementType": NotRequired[EnablementTypeFilterType],
        "SkillType": NotRequired[SkillTypeFilterType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSkillsResponseTypeDef = TypedDict(
    "ListSkillsResponseTypeDef",
    {
        "SkillSummaries": List["SkillSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSkillsStoreCategoriesRequestRequestTypeDef = TypedDict(
    "ListSkillsStoreCategoriesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "ListSkillsStoreCategoriesResponseTypeDef",
    {
        "CategoryList": List["CategoryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSkillsStoreSkillsByCategoryRequestRequestTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryRequestRequestTypeDef",
    {
        "CategoryId": int,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    {
        "SkillsStoreSkills": List["SkillsStoreSkillTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSmartHomeAppliancesRequestRequestTypeDef = TypedDict(
    "ListSmartHomeAppliancesRequestRequestTypeDef",
    {
        "RoomArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "ListSmartHomeAppliancesResponseTypeDef",
    {
        "SmartHomeAppliances": List["SmartHomeApplianceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsRequestRequestTypeDef = TypedDict(
    "ListTagsRequestRequestTypeDef",
    {
        "Arn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MeetingRoomConfigurationTypeDef = TypedDict(
    "MeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": NotRequired[bool],
        "EndOfMeetingReminder": NotRequired["EndOfMeetingReminderTypeDef"],
        "InstantBooking": NotRequired["InstantBookingTypeDef"],
        "RequireCheckIn": NotRequired["RequireCheckInTypeDef"],
    },
)

MeetingSettingTypeDef = TypedDict(
    "MeetingSettingTypeDef",
    {
        "RequirePin": RequirePinType,
    },
)

NetworkProfileDataTypeDef = TypedDict(
    "NetworkProfileDataTypeDef",
    {
        "NetworkProfileArn": NotRequired[str],
        "NetworkProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "Ssid": NotRequired[str],
        "SecurityType": NotRequired[NetworkSecurityTypeType],
        "EapMethod": NotRequired[Literal["EAP_TLS"]],
        "CertificateAuthorityArn": NotRequired[str],
    },
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "NetworkProfileArn": NotRequired[str],
        "NetworkProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "Ssid": NotRequired[str],
        "SecurityType": NotRequired[NetworkSecurityTypeType],
        "EapMethod": NotRequired[Literal["EAP_TLS"]],
        "CurrentPassword": NotRequired[str],
        "NextPassword": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "TrustAnchors": NotRequired[List[str]],
    },
)

PSTNDialInTypeDef = TypedDict(
    "PSTNDialInTypeDef",
    {
        "CountryCode": str,
        "PhoneNumber": str,
        "OneClickIdDelay": str,
        "OneClickPinDelay": str,
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

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "Number": str,
        "Type": PhoneNumberTypeType,
    },
)

ProfileDataTypeDef = TypedDict(
    "ProfileDataTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "Address": NotRequired[str],
        "Timezone": NotRequired[str],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "TemperatureUnit": NotRequired[TemperatureUnitType],
        "WakeWord": NotRequired[WakeWordType],
        "Locale": NotRequired[str],
    },
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "Address": NotRequired[str],
        "Timezone": NotRequired[str],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "TemperatureUnit": NotRequired[TemperatureUnitType],
        "WakeWord": NotRequired[WakeWordType],
        "Locale": NotRequired[str],
        "SetupModeDisabled": NotRequired[bool],
        "MaxVolumeLimit": NotRequired[int],
        "PSTNEnabled": NotRequired[bool],
        "DataRetentionOptIn": NotRequired[bool],
        "AddressBookArn": NotRequired[str],
        "MeetingRoomConfiguration": NotRequired["MeetingRoomConfigurationTypeDef"],
    },
)

PutConferencePreferenceRequestRequestTypeDef = TypedDict(
    "PutConferencePreferenceRequestRequestTypeDef",
    {
        "ConferencePreference": "ConferencePreferenceTypeDef",
    },
)

PutInvitationConfigurationRequestRequestTypeDef = TypedDict(
    "PutInvitationConfigurationRequestRequestTypeDef",
    {
        "OrganizationName": str,
        "ContactEmail": NotRequired[str],
        "PrivateSkillIds": NotRequired[Sequence[str]],
    },
)

PutRoomSkillParameterRequestRequestTypeDef = TypedDict(
    "PutRoomSkillParameterRequestRequestTypeDef",
    {
        "SkillId": str,
        "RoomSkillParameter": "RoomSkillParameterTypeDef",
        "RoomArn": NotRequired[str],
    },
)

PutSkillAuthorizationRequestRequestTypeDef = TypedDict(
    "PutSkillAuthorizationRequestRequestTypeDef",
    {
        "AuthorizationResult": Mapping[str, str],
        "SkillId": str,
        "RoomArn": NotRequired[str],
    },
)

RegisterAVSDeviceRequestRequestTypeDef = TypedDict(
    "RegisterAVSDeviceRequestRequestTypeDef",
    {
        "ClientId": str,
        "UserCode": str,
        "ProductId": str,
        "AmazonId": str,
        "DeviceSerialNumber": NotRequired[str],
        "RoomArn": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

RegisterAVSDeviceResponseTypeDef = TypedDict(
    "RegisterAVSDeviceResponseTypeDef",
    {
        "DeviceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectSkillRequestRequestTypeDef = TypedDict(
    "RejectSkillRequestRequestTypeDef",
    {
        "SkillId": str,
    },
)

RequireCheckInTypeDef = TypedDict(
    "RequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": NotRequired[int],
        "Enabled": NotRequired[bool],
    },
)

ResolveRoomRequestRequestTypeDef = TypedDict(
    "ResolveRoomRequestRequestTypeDef",
    {
        "UserId": str,
        "SkillId": str,
    },
)

ResolveRoomResponseTypeDef = TypedDict(
    "ResolveRoomResponseTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "RoomSkillParameters": List["RoomSkillParameterTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

RevokeInvitationRequestRequestTypeDef = TypedDict(
    "RevokeInvitationRequestRequestTypeDef",
    {
        "UserArn": NotRequired[str],
        "EnrollmentId": NotRequired[str],
    },
)

RoomDataTypeDef = TypedDict(
    "RoomDataTypeDef",
    {
        "RoomArn": NotRequired[str],
        "RoomName": NotRequired[str],
        "Description": NotRequired[str],
        "ProviderCalendarId": NotRequired[str],
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
    },
)

RoomSkillParameterTypeDef = TypedDict(
    "RoomSkillParameterTypeDef",
    {
        "ParameterKey": str,
        "ParameterValue": str,
    },
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomArn": NotRequired[str],
        "RoomName": NotRequired[str],
        "Description": NotRequired[str],
        "ProviderCalendarId": NotRequired[str],
        "ProfileArn": NotRequired[str],
    },
)

SearchAddressBooksRequestRequestTypeDef = TypedDict(
    "SearchAddressBooksRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchAddressBooksResponseTypeDef = TypedDict(
    "SearchAddressBooksResponseTypeDef",
    {
        "AddressBooks": List["AddressBookDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchContactsRequestRequestTypeDef = TypedDict(
    "SearchContactsRequestRequestTypeDef",
    {
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

SearchContactsResponseTypeDef = TypedDict(
    "SearchContactsResponseTypeDef",
    {
        "Contacts": List["ContactDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchDevicesRequestRequestTypeDef = TypedDict(
    "SearchDevicesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {
        "Devices": List["DeviceDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchNetworkProfilesRequestRequestTypeDef = TypedDict(
    "SearchNetworkProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchNetworkProfilesResponseTypeDef = TypedDict(
    "SearchNetworkProfilesResponseTypeDef",
    {
        "NetworkProfiles": List["NetworkProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchProfilesRequestRequestTypeDef = TypedDict(
    "SearchProfilesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {
        "Profiles": List["ProfileDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchRoomsRequestRequestTypeDef = TypedDict(
    "SearchRoomsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchRoomsResponseTypeDef = TypedDict(
    "SearchRoomsResponseTypeDef",
    {
        "Rooms": List["RoomDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchSkillGroupsRequestRequestTypeDef = TypedDict(
    "SearchSkillGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchSkillGroupsResponseTypeDef = TypedDict(
    "SearchSkillGroupsResponseTypeDef",
    {
        "SkillGroups": List["SkillGroupDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SearchUsersRequestRequestTypeDef = TypedDict(
    "SearchUsersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence["FilterTypeDef"]],
        "SortCriteria": NotRequired[Sequence["SortTypeDef"]],
    },
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {
        "Users": List["UserDataTypeDef"],
        "NextToken": str,
        "TotalCount": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendAnnouncementRequestRequestTypeDef = TypedDict(
    "SendAnnouncementRequestRequestTypeDef",
    {
        "RoomFilters": Sequence["FilterTypeDef"],
        "Content": "ContentTypeDef",
        "ClientRequestToken": str,
        "TimeToLiveInSeconds": NotRequired[int],
    },
)

SendAnnouncementResponseTypeDef = TypedDict(
    "SendAnnouncementResponseTypeDef",
    {
        "AnnouncementArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendInvitationRequestRequestTypeDef = TypedDict(
    "SendInvitationRequestRequestTypeDef",
    {
        "UserArn": NotRequired[str],
    },
)

SipAddressTypeDef = TypedDict(
    "SipAddressTypeDef",
    {
        "Uri": str,
        "Type": Literal["WORK"],
    },
)

SkillDetailsTypeDef = TypedDict(
    "SkillDetailsTypeDef",
    {
        "ProductDescription": NotRequired[str],
        "InvocationPhrase": NotRequired[str],
        "ReleaseDate": NotRequired[str],
        "EndUserLicenseAgreement": NotRequired[str],
        "GenericKeywords": NotRequired[List[str]],
        "BulletPoints": NotRequired[List[str]],
        "NewInThisVersionBulletPoints": NotRequired[List[str]],
        "SkillTypes": NotRequired[List[str]],
        "Reviews": NotRequired[Dict[str, str]],
        "DeveloperInfo": NotRequired["DeveloperInfoTypeDef"],
    },
)

SkillGroupDataTypeDef = TypedDict(
    "SkillGroupDataTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "SkillGroupName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

SkillGroupTypeDef = TypedDict(
    "SkillGroupTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "SkillGroupName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

SkillSummaryTypeDef = TypedDict(
    "SkillSummaryTypeDef",
    {
        "SkillId": NotRequired[str],
        "SkillName": NotRequired[str],
        "SupportsLinking": NotRequired[bool],
        "EnablementType": NotRequired[EnablementTypeType],
        "SkillType": NotRequired[SkillTypeType],
    },
)

SkillsStoreSkillTypeDef = TypedDict(
    "SkillsStoreSkillTypeDef",
    {
        "SkillId": NotRequired[str],
        "SkillName": NotRequired[str],
        "ShortDescription": NotRequired[str],
        "IconUrl": NotRequired[str],
        "SampleUtterances": NotRequired[List[str]],
        "SkillDetails": NotRequired["SkillDetailsTypeDef"],
        "SupportsLinking": NotRequired[bool],
    },
)

SmartHomeApplianceTypeDef = TypedDict(
    "SmartHomeApplianceTypeDef",
    {
        "FriendlyName": NotRequired[str],
        "Description": NotRequired[str],
        "ManufacturerName": NotRequired[str],
    },
)

SortTypeDef = TypedDict(
    "SortTypeDef",
    {
        "Key": str,
        "Value": SortValueType,
    },
)

SsmlTypeDef = TypedDict(
    "SsmlTypeDef",
    {
        "Locale": Literal["en-US"],
        "Value": str,
    },
)

StartDeviceSyncRequestRequestTypeDef = TypedDict(
    "StartDeviceSyncRequestRequestTypeDef",
    {
        "Features": Sequence[FeatureType],
        "RoomArn": NotRequired[str],
        "DeviceArn": NotRequired[str],
    },
)

StartSmartHomeApplianceDiscoveryRequestRequestTypeDef = TypedDict(
    "StartSmartHomeApplianceDiscoveryRequestRequestTypeDef",
    {
        "RoomArn": str,
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "Arn": str,
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

TextTypeDef = TypedDict(
    "TextTypeDef",
    {
        "Locale": Literal["en-US"],
        "Value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "Arn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAddressBookRequestRequestTypeDef = TypedDict(
    "UpdateAddressBookRequestRequestTypeDef",
    {
        "AddressBookArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateBusinessReportScheduleRequestRequestTypeDef = TypedDict(
    "UpdateBusinessReportScheduleRequestRequestTypeDef",
    {
        "ScheduleArn": str,
        "S3BucketName": NotRequired[str],
        "S3KeyPrefix": NotRequired[str],
        "Format": NotRequired[BusinessReportFormatType],
        "ScheduleName": NotRequired[str],
        "Recurrence": NotRequired["BusinessReportRecurrenceTypeDef"],
    },
)

UpdateConferenceProviderRequestRequestTypeDef = TypedDict(
    "UpdateConferenceProviderRequestRequestTypeDef",
    {
        "ConferenceProviderArn": str,
        "ConferenceProviderType": ConferenceProviderTypeType,
        "MeetingSetting": "MeetingSettingTypeDef",
        "IPDialIn": NotRequired["IPDialInTypeDef"],
        "PSTNDialIn": NotRequired["PSTNDialInTypeDef"],
    },
)

UpdateContactRequestRequestTypeDef = TypedDict(
    "UpdateContactRequestRequestTypeDef",
    {
        "ContactArn": str,
        "DisplayName": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "PhoneNumber": NotRequired[str],
        "PhoneNumbers": NotRequired[Sequence["PhoneNumberTypeDef"]],
        "SipAddresses": NotRequired[Sequence["SipAddressTypeDef"]],
    },
)

UpdateDeviceRequestRequestTypeDef = TypedDict(
    "UpdateDeviceRequestRequestTypeDef",
    {
        "DeviceArn": NotRequired[str],
        "DeviceName": NotRequired[str],
    },
)

UpdateEndOfMeetingReminderTypeDef = TypedDict(
    "UpdateEndOfMeetingReminderTypeDef",
    {
        "ReminderAtMinutes": NotRequired[Sequence[int]],
        "ReminderType": NotRequired[EndOfMeetingReminderTypeType],
        "Enabled": NotRequired[bool],
    },
)

UpdateGatewayGroupRequestRequestTypeDef = TypedDict(
    "UpdateGatewayGroupRequestRequestTypeDef",
    {
        "GatewayGroupArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UpdateGatewayRequestRequestTypeDef = TypedDict(
    "UpdateGatewayRequestRequestTypeDef",
    {
        "GatewayArn": str,
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "SoftwareVersion": NotRequired[str],
    },
)

UpdateInstantBookingTypeDef = TypedDict(
    "UpdateInstantBookingTypeDef",
    {
        "DurationInMinutes": NotRequired[int],
        "Enabled": NotRequired[bool],
    },
)

UpdateMeetingRoomConfigurationTypeDef = TypedDict(
    "UpdateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": NotRequired[bool],
        "EndOfMeetingReminder": NotRequired["UpdateEndOfMeetingReminderTypeDef"],
        "InstantBooking": NotRequired["UpdateInstantBookingTypeDef"],
        "RequireCheckIn": NotRequired["UpdateRequireCheckInTypeDef"],
    },
)

UpdateNetworkProfileRequestRequestTypeDef = TypedDict(
    "UpdateNetworkProfileRequestRequestTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": NotRequired[str],
        "Description": NotRequired[str],
        "CurrentPassword": NotRequired[str],
        "NextPassword": NotRequired[str],
        "CertificateAuthorityArn": NotRequired[str],
        "TrustAnchors": NotRequired[Sequence[str]],
    },
)

UpdateProfileRequestRequestTypeDef = TypedDict(
    "UpdateProfileRequestRequestTypeDef",
    {
        "ProfileArn": NotRequired[str],
        "ProfileName": NotRequired[str],
        "IsDefault": NotRequired[bool],
        "Timezone": NotRequired[str],
        "Address": NotRequired[str],
        "DistanceUnit": NotRequired[DistanceUnitType],
        "TemperatureUnit": NotRequired[TemperatureUnitType],
        "WakeWord": NotRequired[WakeWordType],
        "Locale": NotRequired[str],
        "SetupModeDisabled": NotRequired[bool],
        "MaxVolumeLimit": NotRequired[int],
        "PSTNEnabled": NotRequired[bool],
        "DataRetentionOptIn": NotRequired[bool],
        "MeetingRoomConfiguration": NotRequired["UpdateMeetingRoomConfigurationTypeDef"],
    },
)

UpdateRequireCheckInTypeDef = TypedDict(
    "UpdateRequireCheckInTypeDef",
    {
        "ReleaseAfterMinutes": NotRequired[int],
        "Enabled": NotRequired[bool],
    },
)

UpdateRoomRequestRequestTypeDef = TypedDict(
    "UpdateRoomRequestRequestTypeDef",
    {
        "RoomArn": NotRequired[str],
        "RoomName": NotRequired[str],
        "Description": NotRequired[str],
        "ProviderCalendarId": NotRequired[str],
        "ProfileArn": NotRequired[str],
    },
)

UpdateSkillGroupRequestRequestTypeDef = TypedDict(
    "UpdateSkillGroupRequestRequestTypeDef",
    {
        "SkillGroupArn": NotRequired[str],
        "SkillGroupName": NotRequired[str],
        "Description": NotRequired[str],
    },
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "UserArn": NotRequired[str],
        "FirstName": NotRequired[str],
        "LastName": NotRequired[str],
        "Email": NotRequired[str],
        "EnrollmentStatus": NotRequired[EnrollmentStatusType],
        "EnrollmentId": NotRequired[str],
    },
)
