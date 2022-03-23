"""
Type annotations for chime service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_chime/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from typing_extensions import NotRequired

from .literals import (
    AccountStatusType,
    AccountTypeType,
    AppInstanceDataTypeType,
    ArtifactsStateType,
    AudioMuxTypeType,
    CallingNameStatusType,
    CapabilityType,
    ChannelMembershipTypeType,
    ChannelMessagePersistenceTypeType,
    ChannelMessageTypeType,
    ChannelModeType,
    ChannelPrivacyType,
    EmailStatusType,
    ErrorCodeType,
    GeoMatchLevelType,
    InviteStatusType,
    LicenseType,
    MediaPipelineStatusType,
    MemberTypeType,
    NotificationTargetType,
    NumberSelectionBehaviorType,
    OrderedPhoneNumberStatusType,
    OriginationRouteProtocolType,
    PhoneNumberAssociationNameType,
    PhoneNumberOrderStatusType,
    PhoneNumberProductTypeType,
    PhoneNumberStatusType,
    PhoneNumberTypeType,
    ProxySessionStatusType,
    RegistrationStatusType,
    RoomMembershipRoleType,
    SipRuleTriggerTypeType,
    SortOrderType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
    UserTypeType,
    VoiceConnectorAwsRegionType,
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
    "AccountSettingsTypeDef",
    "AccountTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceStreamingConfigurationTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserMembershipSummaryTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "ArtifactsConfigurationTypeDef",
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    "AttendeeTypeDef",
    "AudioArtifactsConfigurationTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchSuspendUserRequestRequestTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserRequestRequestTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "BatchUpdateUserRequestRequestTypeDef",
    "BatchUpdateUserResponseTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ChimeSdkMeetingConfigurationTypeDef",
    "ContentArtifactsConfigurationTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAccountRequestRequestTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAppInstanceAdminRequestRequestTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceRequestRequestTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserRequestRequestTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateBotRequestRequestTypeDef",
    "CreateBotResponseTypeDef",
    "CreateChannelBanRequestRequestTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelMembershipRequestRequestTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorRequestRequestTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    "CreateMediaCapturePipelineResponseTypeDef",
    "CreateMeetingDialOutRequestRequestTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionRequestRequestTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateRoomMembershipRequestRequestTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationRequestRequestTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleRequestRequestTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorRequestRequestTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DeleteAccountRequestRequestTypeDef",
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    "DeleteAppInstanceRequestRequestTypeDef",
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "DeleteAppInstanceUserRequestRequestTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteChannelBanRequestRequestTypeDef",
    "DeleteChannelMembershipRequestRequestTypeDef",
    "DeleteChannelMessageRequestRequestTypeDef",
    "DeleteChannelModeratorRequestRequestTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteEventsConfigurationRequestRequestTypeDef",
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "DeletePhoneNumberRequestRequestTypeDef",
    "DeleteProxySessionRequestRequestTypeDef",
    "DeleteRoomMembershipRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    "DeleteSipRuleRequestRequestTypeDef",
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    "DeleteVoiceConnectorRequestRequestTypeDef",
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceRequestRequestTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserRequestRequestTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "DescribeChannelBanRequestRequestTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipRequestRequestTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorRequestRequestTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "EventsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetAccountRequestRequestTypeDef",
    "GetAccountResponseTypeDef",
    "GetAccountSettingsRequestRequestTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetBotRequestRequestTypeDef",
    "GetBotResponseTypeDef",
    "GetChannelMessageRequestRequestTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetEventsConfigurationRequestRequestTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetMediaCapturePipelineRequestRequestTypeDef",
    "GetMediaCapturePipelineResponseTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "GetMeetingResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetPhoneNumberOrderRequestRequestTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberRequestRequestTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionRequestRequestTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetRetentionSettingsRequestRequestTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "GetRoomRequestRequestTypeDef",
    "GetRoomResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationRequestRequestTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleRequestRequestTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetUserRequestRequestTypeDef",
    "GetUserResponseTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorRequestRequestTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "IdentityTypeDef",
    "InviteTypeDef",
    "InviteUsersRequestRequestTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsRequestRequestTypeDef",
    "ListAccountsResponseTypeDef",
    "ListAppInstanceAdminsRequestRequestTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceUsersRequestRequestTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesRequestRequestTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListAttendeeTagsRequestRequestTypeDef",
    "ListAttendeeTagsResponseTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListBotsRequestRequestTypeDef",
    "ListBotsResponseTypeDef",
    "ListChannelBansRequestRequestTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsRequestRequestTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesRequestRequestTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsRequestRequestTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    "ListMediaCapturePipelinesResponseTypeDef",
    "ListMeetingTagsRequestRequestTypeDef",
    "ListMeetingTagsResponseTypeDef",
    "ListMeetingsRequestRequestTypeDef",
    "ListMeetingsResponseTypeDef",
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersRequestRequestTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsRequestRequestTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListRoomMembershipsRequestRequestTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListRoomsResponseTypeDef",
    "ListSipMediaApplicationsRequestRequestTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesRequestRequestTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListUsersResponseTypeDef",
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsRequestRequestTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LogoutUserRequestRequestTypeDef",
    "MediaCapturePipelineTypeDef",
    "MediaPlacementTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "MeetingTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MembershipItemTypeDef",
    "MessagingSessionEndpointTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    "PutEventsConfigurationRequestRequestTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "PutRetentionSettingsRequestRequestTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "RedactChannelMessageRequestRequestTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "RedactConversationMessageRequestRequestTypeDef",
    "RedactRoomMessageRequestRequestTypeDef",
    "RegenerateSecurityTokenRequestRequestTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "ResetPersonalPINRequestRequestTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestorePhoneNumberRequestRequestTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SelectedVideoStreamsTypeDef",
    "SendChannelMessageRequestRequestTypeDef",
    "SendChannelMessageResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "SourceConfigurationTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagAttendeeRequestRequestTypeDef",
    "TagMeetingRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TelephonySettingsTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "TranscriptionConfigurationTypeDef",
    "UntagAttendeeRequestRequestTypeDef",
    "UntagMeetingRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAccountRequestRequestTypeDef",
    "UpdateAccountResponseTypeDef",
    "UpdateAccountSettingsRequestRequestTypeDef",
    "UpdateAppInstanceRequestRequestTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserRequestRequestTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "UpdateBotRequestRequestTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateChannelMessageRequestRequestTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateGlobalSettingsRequestRequestTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberRequestRequestTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    "UpdateProxySessionRequestRequestTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateRoomMembershipRequestRequestTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    "UpdateSipMediaApplicationCallResponseTypeDef",
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleRequestRequestTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorRequestRequestTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VideoArtifactsConfigurationTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
)

AccountSettingsTypeDef = TypedDict(
    "AccountSettingsTypeDef",
    {
        "DisableRemoteControl": NotRequired[bool],
        "EnableDialOut": NotRequired[bool],
    },
)

AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "AwsAccountId": str,
        "AccountId": str,
        "Name": str,
        "AccountType": NotRequired[AccountTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "DefaultLicense": NotRequired[LicenseType],
        "SupportedLicenses": NotRequired[List[LicenseType]],
        "AccountStatus": NotRequired[AccountStatusType],
        "SigninDelegateGroups": NotRequired[List["SigninDelegateGroupTypeDef"]],
    },
)

AlexaForBusinessMetadataTypeDef = TypedDict(
    "AlexaForBusinessMetadataTypeDef",
    {
        "IsAlexaForBusinessEnabled": NotRequired[bool],
        "AlexaForBusinessRoomArn": NotRequired[str],
    },
)

AppInstanceAdminSummaryTypeDef = TypedDict(
    "AppInstanceAdminSummaryTypeDef",
    {
        "Admin": NotRequired["IdentityTypeDef"],
    },
)

AppInstanceAdminTypeDef = TypedDict(
    "AppInstanceAdminTypeDef",
    {
        "Admin": NotRequired["IdentityTypeDef"],
        "AppInstanceArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
    },
)

AppInstanceRetentionSettingsTypeDef = TypedDict(
    "AppInstanceRetentionSettingsTypeDef",
    {
        "ChannelRetentionSettings": NotRequired["ChannelRetentionSettingsTypeDef"],
    },
)

AppInstanceStreamingConfigurationTypeDef = TypedDict(
    "AppInstanceStreamingConfigurationTypeDef",
    {
        "AppInstanceDataType": AppInstanceDataTypeType,
        "ResourceArn": str,
    },
)

AppInstanceSummaryTypeDef = TypedDict(
    "AppInstanceSummaryTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)

AppInstanceTypeDef = TypedDict(
    "AppInstanceTypeDef",
    {
        "AppInstanceArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {
        "Type": NotRequired[ChannelMembershipTypeType],
        "ReadMarkerTimestamp": NotRequired[datetime],
    },
)

AppInstanceUserSummaryTypeDef = TypedDict(
    "AppInstanceUserSummaryTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "Metadata": NotRequired[str],
    },
)

AppInstanceUserTypeDef = TypedDict(
    "AppInstanceUserTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "Name": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "Metadata": NotRequired[str],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ArtifactsConfigurationTypeDef = TypedDict(
    "ArtifactsConfigurationTypeDef",
    {
        "Audio": "AudioArtifactsConfigurationTypeDef",
        "Video": "VideoArtifactsConfigurationTypeDef",
        "Content": "ContentArtifactsConfigurationTypeDef",
    },
)

AssociatePhoneNumberWithUserRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumberWithUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "E164PhoneNumber": str,
    },
)

AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
        "ForceAssociate": NotRequired[bool],
    },
)

AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
        "ForceAssociate": NotRequired[bool],
    },
)

AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef = TypedDict(
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef = TypedDict(
    "AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "SigninDelegateGroups": Sequence["SigninDelegateGroupTypeDef"],
    },
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "AttendeeId": NotRequired[str],
        "JoinToken": NotRequired[str],
    },
)

AudioArtifactsConfigurationTypeDef = TypedDict(
    "AudioArtifactsConfigurationTypeDef",
    {
        "MuxType": AudioMuxTypeType,
    },
)

BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": NotRequired["IdentityTypeDef"],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Members": NotRequired[List["IdentityTypeDef"]],
        "ChannelArn": NotRequired[str],
    },
)

BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": Sequence["CreateAttendeeRequestItemTypeDef"],
    },
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateChannelMembershipErrorTypeDef = TypedDict(
    "BatchCreateChannelMembershipErrorTypeDef",
    {
        "MemberArn": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

BatchCreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArns": Sequence[str],
        "Type": NotRequired[ChannelMembershipTypeType],
        "ChimeBearer": NotRequired[str],
    },
)

BatchCreateChannelMembershipResponseTypeDef = TypedDict(
    "BatchCreateChannelMembershipResponseTypeDef",
    {
        "BatchChannelMemberships": "BatchChannelMembershipsTypeDef",
        "Errors": List["BatchCreateChannelMembershipErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchCreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "BatchCreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MembershipItemList": Sequence["MembershipItemTypeDef"],
    },
)

BatchCreateRoomMembershipResponseTypeDef = TypedDict(
    "BatchCreateRoomMembershipResponseTypeDef",
    {
        "Errors": List["MemberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchDeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberIds": Sequence[str],
    },
)

BatchDeletePhoneNumberResponseTypeDef = TypedDict(
    "BatchDeletePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchSuspendUserRequestRequestTypeDef = TypedDict(
    "BatchSuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": Sequence[str],
    },
)

BatchSuspendUserResponseTypeDef = TypedDict(
    "BatchSuspendUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUnsuspendUserRequestRequestTypeDef = TypedDict(
    "BatchUnsuspendUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserIdList": Sequence[str],
    },
)

BatchUnsuspendUserResponseTypeDef = TypedDict(
    "BatchUnsuspendUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "BatchUpdatePhoneNumberRequestRequestTypeDef",
    {
        "UpdatePhoneNumberRequestItems": Sequence["UpdatePhoneNumberRequestItemTypeDef"],
    },
)

BatchUpdatePhoneNumberResponseTypeDef = TypedDict(
    "BatchUpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchUpdateUserRequestRequestTypeDef = TypedDict(
    "BatchUpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UpdateUserRequestItems": Sequence["UpdateUserRequestItemTypeDef"],
    },
)

BatchUpdateUserResponseTypeDef = TypedDict(
    "BatchUpdateUserResponseTypeDef",
    {
        "UserErrors": List["UserErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BotTypeDef = TypedDict(
    "BotTypeDef",
    {
        "BotId": NotRequired[str],
        "UserId": NotRequired[str],
        "DisplayName": NotRequired[str],
        "BotType": NotRequired[Literal["ChatBot"]],
        "Disabled": NotRequired[bool],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "BotEmail": NotRequired[str],
        "SecurityToken": NotRequired[str],
    },
)

BusinessCallingSettingsTypeDef = TypedDict(
    "BusinessCallingSettingsTypeDef",
    {
        "CdrBucket": NotRequired[str],
    },
)

ChannelBanSummaryTypeDef = TypedDict(
    "ChannelBanSummaryTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
    },
)

ChannelBanTypeDef = TypedDict(
    "ChannelBanTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired["IdentityTypeDef"],
    },
)

ChannelMembershipForAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired["ChannelSummaryTypeDef"],
        "AppInstanceUserMembershipSummary": NotRequired["AppInstanceUserMembershipSummaryTypeDef"],
    },
)

ChannelMembershipSummaryTypeDef = TypedDict(
    "ChannelMembershipSummaryTypeDef",
    {
        "Member": NotRequired["IdentityTypeDef"],
    },
)

ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": NotRequired["IdentityTypeDef"],
        "Type": NotRequired[ChannelMembershipTypeType],
        "Member": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "Sender": NotRequired["IdentityTypeDef"],
        "Redacted": NotRequired[bool],
    },
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": NotRequired[str],
        "MessageId": NotRequired[str],
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "Type": NotRequired[ChannelMessageTypeType],
        "CreatedTimestamp": NotRequired[datetime],
        "LastEditedTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
        "Sender": NotRequired["IdentityTypeDef"],
        "Redacted": NotRequired[bool],
        "Persistence": NotRequired[ChannelMessagePersistenceTypeType],
    },
)

ChannelModeratedByAppInstanceUserSummaryTypeDef = TypedDict(
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    {
        "ChannelSummary": NotRequired["ChannelSummaryTypeDef"],
    },
)

ChannelModeratorSummaryTypeDef = TypedDict(
    "ChannelModeratorSummaryTypeDef",
    {
        "Moderator": NotRequired["IdentityTypeDef"],
    },
)

ChannelModeratorTypeDef = TypedDict(
    "ChannelModeratorTypeDef",
    {
        "Moderator": NotRequired["IdentityTypeDef"],
        "ChannelArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "CreatedBy": NotRequired["IdentityTypeDef"],
    },
)

ChannelRetentionSettingsTypeDef = TypedDict(
    "ChannelRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "LastMessageTimestamp": NotRequired[datetime],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Name": NotRequired[str],
        "ChannelArn": NotRequired[str],
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "CreatedBy": NotRequired["IdentityTypeDef"],
        "CreatedTimestamp": NotRequired[datetime],
        "LastMessageTimestamp": NotRequired[datetime],
        "LastUpdatedTimestamp": NotRequired[datetime],
    },
)

ChimeSdkMeetingConfigurationTypeDef = TypedDict(
    "ChimeSdkMeetingConfigurationTypeDef",
    {
        "SourceConfiguration": NotRequired["SourceConfigurationTypeDef"],
        "ArtifactsConfiguration": NotRequired["ArtifactsConfigurationTypeDef"],
    },
)

ContentArtifactsConfigurationTypeDef = TypedDict(
    "ContentArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["ContentOnly"]],
    },
)

ConversationRetentionSettingsTypeDef = TypedDict(
    "ConversationRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)

CreateAccountRequestRequestTypeDef = TypedDict(
    "CreateAccountRequestRequestTypeDef",
    {
        "Name": str,
    },
)

CreateAccountResponseTypeDef = TypedDict(
    "CreateAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

CreateAppInstanceAdminResponseTypeDef = TypedDict(
    "CreateAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "IdentityTypeDef",
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceRequestRequestTypeDef",
    {
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAppInstanceResponseTypeDef = TypedDict(
    "CreateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "CreateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUserId": str,
        "Name": str,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAppInstanceUserResponseTypeDef = TypedDict(
    "CreateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)

CreateAttendeeRequestItemTypeDef = TypedDict(
    "CreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAttendeeRequestRequestTypeDef = TypedDict(
    "CreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
        "Tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateBotRequestRequestTypeDef = TypedDict(
    "CreateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "DisplayName": str,
        "Domain": NotRequired[str],
    },
)

CreateBotResponseTypeDef = TypedDict(
    "CreateBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelBanRequestRequestTypeDef = TypedDict(
    "CreateChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

CreateChannelBanResponseTypeDef = TypedDict(
    "CreateChannelBanResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelMembershipRequestRequestTypeDef = TypedDict(
    "CreateChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "Type": ChannelMembershipTypeType,
        "ChimeBearer": NotRequired[str],
    },
)

CreateChannelMembershipResponseTypeDef = TypedDict(
    "CreateChannelMembershipResponseTypeDef",
    {
        "ChannelArn": str,
        "Member": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelModeratorRequestRequestTypeDef = TypedDict(
    "CreateChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

CreateChannelModeratorResponseTypeDef = TypedDict(
    "CreateChannelModeratorResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelModerator": "IdentityTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "ClientRequestToken": str,
        "Mode": NotRequired[ChannelModeType],
        "Privacy": NotRequired[ChannelPrivacyType],
        "Metadata": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "ChimeBearer": NotRequired[str],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "CreateMediaCapturePipelineRequestRequestTypeDef",
    {
        "SourceType": Literal["ChimeSdkMeeting"],
        "SourceArn": str,
        "SinkType": Literal["S3Bucket"],
        "SinkArn": str,
        "ClientRequestToken": NotRequired[str],
        "ChimeSdkMeetingConfiguration": NotRequired["ChimeSdkMeetingConfigurationTypeDef"],
    },
)

CreateMediaCapturePipelineResponseTypeDef = TypedDict(
    "CreateMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingDialOutRequestRequestTypeDef = TypedDict(
    "CreateMeetingDialOutRequestRequestTypeDef",
    {
        "MeetingId": str,
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "JoinToken": str,
    },
)

CreateMeetingDialOutResponseTypeDef = TypedDict(
    "CreateMeetingDialOutResponseTypeDef",
    {
        "TransactionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingRequestRequestTypeDef = TypedDict(
    "CreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ExternalMeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "NotificationsConfiguration": NotRequired["MeetingNotificationConfigurationTypeDef"],
    },
)

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "ExternalMeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "Tags": NotRequired[Sequence["TagTypeDef"]],
        "NotificationsConfiguration": NotRequired["MeetingNotificationConfigurationTypeDef"],
        "Attendees": NotRequired[Sequence["CreateAttendeeRequestItemTypeDef"]],
    },
)

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "Attendees": List["AttendeeTypeDef"],
        "Errors": List["CreateAttendeeErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "CreatePhoneNumberOrderRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
        "E164PhoneNumbers": Sequence[str],
    },
)

CreatePhoneNumberOrderResponseTypeDef = TypedDict(
    "CreatePhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateProxySessionRequestRequestTypeDef = TypedDict(
    "CreateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ParticipantPhoneNumbers": Sequence[str],
        "Capabilities": Sequence[CapabilityType],
        "Name": NotRequired[str],
        "ExpiryMinutes": NotRequired[int],
        "NumberSelectionBehavior": NotRequired[NumberSelectionBehaviorType],
        "GeoMatchLevel": NotRequired[GeoMatchLevelType],
        "GeoMatchParams": NotRequired["GeoMatchParamsTypeDef"],
    },
)

CreateProxySessionResponseTypeDef = TypedDict(
    "CreateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoomMembershipRequestRequestTypeDef = TypedDict(
    "CreateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
        "Role": NotRequired[RoomMembershipRoleType],
    },
)

CreateRoomMembershipResponseTypeDef = TypedDict(
    "CreateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": str,
        "ClientRequestToken": NotRequired[str],
    },
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "FromPhoneNumber": str,
        "ToPhoneNumber": str,
        "SipMediaApplicationId": str,
        "SipHeaders": NotRequired[Mapping[str, str]],
    },
)

CreateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "CreateSipMediaApplicationRequestRequestTypeDef",
    {
        "AwsRegion": str,
        "Name": str,
        "Endpoints": Sequence["SipMediaApplicationEndpointTypeDef"],
    },
)

CreateSipMediaApplicationResponseTypeDef = TypedDict(
    "CreateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateSipRuleRequestRequestTypeDef = TypedDict(
    "CreateSipRuleRequestRequestTypeDef",
    {
        "Name": str,
        "TriggerType": SipRuleTriggerTypeType,
        "TriggerValue": str,
        "TargetApplications": Sequence["SipRuleTargetApplicationTypeDef"],
        "Disabled": NotRequired[bool],
    },
)

CreateSipRuleResponseTypeDef = TypedDict(
    "CreateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "Username": NotRequired[str],
        "Email": NotRequired[str],
        "UserType": NotRequired[UserTypeType],
    },
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "CreateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "Name": str,
        "VoiceConnectorItems": NotRequired[Sequence["VoiceConnectorItemTypeDef"]],
    },
)

CreateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "CreateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "CreateVoiceConnectorRequestRequestTypeDef",
    {
        "Name": str,
        "RequireEncryption": bool,
        "AwsRegion": NotRequired[VoiceConnectorAwsRegionType],
    },
)

CreateVoiceConnectorResponseTypeDef = TypedDict(
    "CreateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CredentialTypeDef = TypedDict(
    "CredentialTypeDef",
    {
        "Username": NotRequired[str],
        "Password": NotRequired[str],
    },
)

DNISEmergencyCallingConfigurationTypeDef = TypedDict(
    "DNISEmergencyCallingConfigurationTypeDef",
    {
        "EmergencyPhoneNumber": str,
        "CallingCountry": str,
        "TestPhoneNumber": NotRequired[str],
    },
)

DeleteAccountRequestRequestTypeDef = TypedDict(
    "DeleteAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

DeleteAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DeleteAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DeleteAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

DeleteChannelBanRequestRequestTypeDef = TypedDict(
    "DeleteChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DeleteChannelMembershipRequestRequestTypeDef = TypedDict(
    "DeleteChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DeleteChannelMessageRequestRequestTypeDef = TypedDict(
    "DeleteChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)

DeleteChannelModeratorRequestRequestTypeDef = TypedDict(
    "DeleteChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DeleteEventsConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

DeleteMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "DeleteMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

DeletePhoneNumberRequestRequestTypeDef = TypedDict(
    "DeletePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

DeleteProxySessionRequestRequestTypeDef = TypedDict(
    "DeleteProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

DeleteRoomMembershipRequestRequestTypeDef = TypedDict(
    "DeleteRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
    },
)

DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

DeleteSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "DeleteSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

DeleteSipRuleRequestRequestTypeDef = TypedDict(
    "DeleteSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

DeleteVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Usernames": Sequence[str],
    },
)

DeleteVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "DeleteVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

DescribeAppInstanceAdminRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceAdminRequestRequestTypeDef",
    {
        "AppInstanceAdminArn": str,
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceAdminResponseTypeDef = TypedDict(
    "DescribeAppInstanceAdminResponseTypeDef",
    {
        "AppInstanceAdmin": "AppInstanceAdminTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

DescribeAppInstanceResponseTypeDef = TypedDict(
    "DescribeAppInstanceResponseTypeDef",
    {
        "AppInstance": "AppInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
    },
)

DescribeAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUser": "AppInstanceUserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelBanRequestRequestTypeDef = TypedDict(
    "DescribeChannelBanRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelBanResponseTypeDef = TypedDict(
    "DescribeChannelBanResponseTypeDef",
    {
        "ChannelBan": "ChannelBanTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelMembershipForAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipForAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelMembershipRequestRequestTypeDef = TypedDict(
    "DescribeChannelMembershipRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MemberArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelMembershipResponseTypeDef = TypedDict(
    "DescribeChannelMembershipResponseTypeDef",
    {
        "ChannelMembership": "ChannelMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "AppInstanceUserArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channel": "ChannelModeratedByAppInstanceUserSummaryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelModeratorRequestRequestTypeDef = TypedDict(
    "DescribeChannelModeratorRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChannelModeratorArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelModeratorResponseTypeDef = TypedDict(
    "DescribeChannelModeratorResponseTypeDef",
    {
        "ChannelModerator": "ChannelModeratorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumberFromUserRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumberFromUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "E164PhoneNumbers": Sequence[str],
    },
)

DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef = TypedDict(
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    {
        "PhoneNumberErrors": List["PhoneNumberErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef = TypedDict(
    "DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "GroupNames": Sequence[str],
    },
)

EmergencyCallingConfigurationTypeDef = TypedDict(
    "EmergencyCallingConfigurationTypeDef",
    {
        "DNIS": NotRequired[List["DNISEmergencyCallingConfigurationTypeDef"]],
    },
)

EngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "EngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeMedicalRegionType],
        "ContentIdentificationType": NotRequired[Literal["PHI"]],
    },
)

EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": TranscribeLanguageCodeType,
        "VocabularyFilterMethod": NotRequired[TranscribeVocabularyFilterMethodType],
        "VocabularyFilterName": NotRequired[str],
        "VocabularyName": NotRequired[str],
        "Region": NotRequired[TranscribeRegionType],
        "EnablePartialResultsStabilization": NotRequired[bool],
        "PartialResultsStability": NotRequired[TranscribePartialResultsStabilityType],
        "ContentIdentificationType": NotRequired[Literal["PII"]],
        "ContentRedactionType": NotRequired[Literal["PII"]],
        "PiiEntityTypes": NotRequired[str],
        "LanguageModelName": NotRequired[str],
    },
)

EventsConfigurationTypeDef = TypedDict(
    "EventsConfigurationTypeDef",
    {
        "BotId": NotRequired[str],
        "OutboundEventsHTTPSEndpoint": NotRequired[str],
        "LambdaFunctionArn": NotRequired[str],
    },
)

GeoMatchParamsTypeDef = TypedDict(
    "GeoMatchParamsTypeDef",
    {
        "Country": str,
        "AreaCode": str,
    },
)

GetAccountRequestRequestTypeDef = TypedDict(
    "GetAccountRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountResponseTypeDef = TypedDict(
    "GetAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAccountSettingsRequestRequestTypeDef = TypedDict(
    "GetAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetAccountSettingsResponseTypeDef = TypedDict(
    "GetAccountSettingsResponseTypeDef",
    {
        "AccountSettings": "AccountSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
    },
)

GetAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetBotRequestRequestTypeDef = TypedDict(
    "GetBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetBotResponseTypeDef = TypedDict(
    "GetBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetChannelMessageRequestRequestTypeDef = TypedDict(
    "GetChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)

GetChannelMessageResponseTypeDef = TypedDict(
    "GetChannelMessageResponseTypeDef",
    {
        "ChannelMessage": "ChannelMessageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEventsConfigurationRequestRequestTypeDef = TypedDict(
    "GetEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

GetEventsConfigurationResponseTypeDef = TypedDict(
    "GetEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetGlobalSettingsResponseTypeDef = TypedDict(
    "GetGlobalSettingsResponseTypeDef",
    {
        "BusinessCalling": "BusinessCallingSettingsTypeDef",
        "VoiceConnector": "VoiceConnectorSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaCapturePipelineRequestRequestTypeDef = TypedDict(
    "GetMediaCapturePipelineRequestRequestTypeDef",
    {
        "MediaPipelineId": str,
    },
)

GetMediaCapturePipelineResponseTypeDef = TypedDict(
    "GetMediaCapturePipelineResponseTypeDef",
    {
        "MediaCapturePipeline": "MediaCapturePipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": "MeetingTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMessagingSessionEndpointResponseTypeDef = TypedDict(
    "GetMessagingSessionEndpointResponseTypeDef",
    {
        "Endpoint": "MessagingSessionEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberOrderRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberOrderRequestRequestTypeDef",
    {
        "PhoneNumberOrderId": str,
    },
)

GetPhoneNumberOrderResponseTypeDef = TypedDict(
    "GetPhoneNumberOrderResponseTypeDef",
    {
        "PhoneNumberOrder": "PhoneNumberOrderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberRequestRequestTypeDef = TypedDict(
    "GetPhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

GetPhoneNumberResponseTypeDef = TypedDict(
    "GetPhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPhoneNumberSettingsResponseTypeDef = TypedDict(
    "GetPhoneNumberSettingsResponseTypeDef",
    {
        "CallingName": str,
        "CallingNameUpdatedTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetProxySessionRequestRequestTypeDef = TypedDict(
    "GetProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
    },
)

GetProxySessionResponseTypeDef = TypedDict(
    "GetProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRetentionSettingsRequestRequestTypeDef = TypedDict(
    "GetRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
    },
)

GetRetentionSettingsResponseTypeDef = TypedDict(
    "GetRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
    },
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "GetSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
    },
)

GetSipMediaApplicationResponseTypeDef = TypedDict(
    "GetSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSipRuleRequestRequestTypeDef = TypedDict(
    "GetSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
    },
)

GetSipRuleResponseTypeDef = TypedDict(
    "GetSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "UserSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
    },
)

GetVoiceConnectorGroupResponseTypeDef = TypedDict(
    "GetVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "GetVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorProxyResponseTypeDef = TypedDict(
    "GetVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorResponseTypeDef = TypedDict(
    "GetVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationHealthRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationHealthResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    {
        "TerminationHealth": "TerminationHealthTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "GetVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

GetVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "GetVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityTypeDef = TypedDict(
    "IdentityTypeDef",
    {
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
    },
)

InviteTypeDef = TypedDict(
    "InviteTypeDef",
    {
        "InviteId": NotRequired[str],
        "Status": NotRequired[InviteStatusType],
        "EmailAddress": NotRequired[str],
        "EmailStatus": NotRequired[EmailStatusType],
    },
)

InviteUsersRequestRequestTypeDef = TypedDict(
    "InviteUsersRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserEmailList": Sequence[str],
        "UserType": NotRequired[UserTypeType],
    },
)

InviteUsersResponseTypeDef = TypedDict(
    "InviteUsersResponseTypeDef",
    {
        "Invites": List["InviteTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAccountsRequestRequestTypeDef = TypedDict(
    "ListAccountsRequestRequestTypeDef",
    {
        "Name": NotRequired[str],
        "UserEmail": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAccountsResponseTypeDef = TypedDict(
    "ListAccountsResponseTypeDef",
    {
        "Accounts": List["AccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceAdminsRequestRequestTypeDef = TypedDict(
    "ListAppInstanceAdminsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstanceAdminsResponseTypeDef = TypedDict(
    "ListAppInstanceAdminsResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceAdmins": List["AppInstanceAdminSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstanceUsersRequestRequestTypeDef = TypedDict(
    "ListAppInstanceUsersRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstanceUsersResponseTypeDef = TypedDict(
    "ListAppInstanceUsersResponseTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceUsers": List["AppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAppInstancesRequestRequestTypeDef = TypedDict(
    "ListAppInstancesRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListAppInstancesResponseTypeDef = TypedDict(
    "ListAppInstancesResponseTypeDef",
    {
        "AppInstances": List["AppInstanceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttendeeTagsRequestRequestTypeDef = TypedDict(
    "ListAttendeeTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

ListAttendeeTagsResponseTypeDef = TypedDict(
    "ListAttendeeTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAttendeesRequestRequestTypeDef = TypedDict(
    "ListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List["AttendeeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListBotsRequestRequestTypeDef = TypedDict(
    "ListBotsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListBotsResponseTypeDef = TypedDict(
    "ListBotsResponseTypeDef",
    {
        "Bots": List["BotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelBansRequestRequestTypeDef = TypedDict(
    "ListChannelBansRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelBansResponseTypeDef = TypedDict(
    "ListChannelBansResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelBans": List["ChannelBanSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelMembershipsForAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    {
        "ChannelMemberships": List["ChannelMembershipForAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMembershipsRequestRequestTypeDef = TypedDict(
    "ListChannelMembershipsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Type": NotRequired[ChannelMembershipTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelMembershipsResponseTypeDef = TypedDict(
    "ListChannelMembershipsResponseTypeDef",
    {
        "ChannelArn": str,
        "ChannelMemberships": List["ChannelMembershipSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelMessagesRequestRequestTypeDef = TypedDict(
    "ListChannelMessagesRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "SortOrder": NotRequired[SortOrderType],
        "NotBefore": NotRequired[Union[datetime, str]],
        "NotAfter": NotRequired[Union[datetime, str]],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelMessagesResponseTypeDef = TypedDict(
    "ListChannelMessagesResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelMessages": List["ChannelMessageSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelModeratorsRequestRequestTypeDef = TypedDict(
    "ListChannelModeratorsRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelModeratorsResponseTypeDef = TypedDict(
    "ListChannelModeratorsResponseTypeDef",
    {
        "ChannelArn": str,
        "NextToken": str,
        "ChannelModerators": List["ChannelModeratorSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelsModeratedByAppInstanceUserResponseTypeDef = TypedDict(
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    {
        "Channels": List["ChannelModeratedByAppInstanceUserSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Privacy": NotRequired[ChannelPrivacyType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMediaCapturePipelinesRequestRequestTypeDef = TypedDict(
    "ListMediaCapturePipelinesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMediaCapturePipelinesResponseTypeDef = TypedDict(
    "ListMediaCapturePipelinesResponseTypeDef",
    {
        "MediaCapturePipelines": List["MediaCapturePipelineTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingTagsRequestRequestTypeDef = TypedDict(
    "ListMeetingTagsRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

ListMeetingTagsResponseTypeDef = TypedDict(
    "ListMeetingTagsResponseTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListMeetingsRequestRequestTypeDef = TypedDict(
    "ListMeetingsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListMeetingsResponseTypeDef = TypedDict(
    "ListMeetingsResponseTypeDef",
    {
        "Meetings": List["MeetingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumberOrdersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumberOrdersRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListPhoneNumberOrdersResponseTypeDef = TypedDict(
    "ListPhoneNumberOrdersResponseTypeDef",
    {
        "PhoneNumberOrders": List["PhoneNumberOrderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPhoneNumbersRequestRequestTypeDef = TypedDict(
    "ListPhoneNumbersRequestRequestTypeDef",
    {
        "Status": NotRequired[PhoneNumberStatusType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "FilterName": NotRequired[PhoneNumberAssociationNameType],
        "FilterValue": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListProxySessionsRequestRequestTypeDef = TypedDict(
    "ListProxySessionsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Status": NotRequired[ProxySessionStatusType],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListProxySessionsResponseTypeDef = TypedDict(
    "ListProxySessionsResponseTypeDef",
    {
        "ProxySessions": List["ProxySessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoomMembershipsRequestRequestTypeDef = TypedDict(
    "ListRoomMembershipsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRoomMembershipsResponseTypeDef = TypedDict(
    "ListRoomMembershipsResponseTypeDef",
    {
        "RoomMemberships": List["RoomMembershipTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "AccountId": str,
        "MemberId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "Rooms": List["RoomTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipMediaApplicationsRequestRequestTypeDef = TypedDict(
    "ListSipMediaApplicationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSipMediaApplicationsResponseTypeDef = TypedDict(
    "ListSipMediaApplicationsResponseTypeDef",
    {
        "SipMediaApplications": List["SipMediaApplicationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSipRulesRequestRequestTypeDef = TypedDict(
    "ListSipRulesRequestRequestTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListSipRulesResponseTypeDef = TypedDict(
    "ListSipRulesResponseTypeDef",
    {
        "SipRules": List["SipRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSupportedPhoneNumberCountriesRequestRequestTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesRequestRequestTypeDef",
    {
        "ProductType": PhoneNumberProductTypeType,
    },
)

ListSupportedPhoneNumberCountriesResponseTypeDef = TypedDict(
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    {
        "PhoneNumberCountries": List["PhoneNumberCountryTypeDef"],
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

ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserEmail": NotRequired[str],
        "UserType": NotRequired[UserTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List["UserTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorGroupsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListVoiceConnectorGroupsResponseTypeDef = TypedDict(
    "ListVoiceConnectorGroupsResponseTypeDef",
    {
        "VoiceConnectorGroups": List["VoiceConnectorGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
    },
)

ListVoiceConnectorTerminationCredentialsResponseTypeDef = TypedDict(
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    {
        "Usernames": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVoiceConnectorsRequestRequestTypeDef = TypedDict(
    "ListVoiceConnectorsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListVoiceConnectorsResponseTypeDef = TypedDict(
    "ListVoiceConnectorsResponseTypeDef",
    {
        "VoiceConnectors": List["VoiceConnectorTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "EnableSIPLogs": NotRequired[bool],
        "EnableMediaMetricLogs": NotRequired[bool],
    },
)

LogoutUserRequestRequestTypeDef = TypedDict(
    "LogoutUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

MediaCapturePipelineTypeDef = TypedDict(
    "MediaCapturePipelineTypeDef",
    {
        "MediaPipelineId": NotRequired[str],
        "SourceType": NotRequired[Literal["ChimeSdkMeeting"]],
        "SourceArn": NotRequired[str],
        "Status": NotRequired[MediaPipelineStatusType],
        "SinkType": NotRequired[Literal["S3Bucket"]],
        "SinkArn": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "ChimeSdkMeetingConfiguration": NotRequired["ChimeSdkMeetingConfigurationTypeDef"],
    },
)

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": NotRequired[str],
        "AudioFallbackUrl": NotRequired[str],
        "ScreenDataUrl": NotRequired[str],
        "ScreenSharingUrl": NotRequired[str],
        "ScreenViewingUrl": NotRequired[str],
        "SignalingUrl": NotRequired[str],
        "TurnControlUrl": NotRequired[str],
        "EventIngestionUrl": NotRequired[str],
    },
)

MeetingNotificationConfigurationTypeDef = TypedDict(
    "MeetingNotificationConfigurationTypeDef",
    {
        "SnsTopicArn": NotRequired[str],
        "SqsQueueArn": NotRequired[str],
    },
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": NotRequired[str],
        "ExternalMeetingId": NotRequired[str],
        "MediaPlacement": NotRequired["MediaPlacementTypeDef"],
        "MediaRegion": NotRequired[str],
    },
)

MemberErrorTypeDef = TypedDict(
    "MemberErrorTypeDef",
    {
        "MemberId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "MemberId": NotRequired[str],
        "MemberType": NotRequired[MemberTypeType],
        "Email": NotRequired[str],
        "FullName": NotRequired[str],
        "AccountId": NotRequired[str],
    },
)

MembershipItemTypeDef = TypedDict(
    "MembershipItemTypeDef",
    {
        "MemberId": NotRequired[str],
        "Role": NotRequired[RoomMembershipRoleType],
    },
)

MessagingSessionEndpointTypeDef = TypedDict(
    "MessagingSessionEndpointTypeDef",
    {
        "Url": NotRequired[str],
    },
)

OrderedPhoneNumberTypeDef = TypedDict(
    "OrderedPhoneNumberTypeDef",
    {
        "E164PhoneNumber": NotRequired[str],
        "Status": NotRequired[OrderedPhoneNumberStatusType],
    },
)

OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": NotRequired[str],
        "Port": NotRequired[int],
        "Protocol": NotRequired[OriginationRouteProtocolType],
        "Priority": NotRequired[int],
        "Weight": NotRequired[int],
    },
)

OriginationTypeDef = TypedDict(
    "OriginationTypeDef",
    {
        "Routes": NotRequired[List["OriginationRouteTypeDef"]],
        "Disabled": NotRequired[bool],
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

ParticipantTypeDef = TypedDict(
    "ParticipantTypeDef",
    {
        "PhoneNumber": NotRequired[str],
        "ProxyPhoneNumber": NotRequired[str],
    },
)

PhoneNumberAssociationTypeDef = TypedDict(
    "PhoneNumberAssociationTypeDef",
    {
        "Value": NotRequired[str],
        "Name": NotRequired[PhoneNumberAssociationNameType],
        "AssociatedTimestamp": NotRequired[datetime],
    },
)

PhoneNumberCapabilitiesTypeDef = TypedDict(
    "PhoneNumberCapabilitiesTypeDef",
    {
        "InboundCall": NotRequired[bool],
        "OutboundCall": NotRequired[bool],
        "InboundSMS": NotRequired[bool],
        "OutboundSMS": NotRequired[bool],
        "InboundMMS": NotRequired[bool],
        "OutboundMMS": NotRequired[bool],
    },
)

PhoneNumberCountryTypeDef = TypedDict(
    "PhoneNumberCountryTypeDef",
    {
        "CountryCode": NotRequired[str],
        "SupportedPhoneNumberTypes": NotRequired[List[PhoneNumberTypeType]],
    },
)

PhoneNumberErrorTypeDef = TypedDict(
    "PhoneNumberErrorTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

PhoneNumberOrderTypeDef = TypedDict(
    "PhoneNumberOrderTypeDef",
    {
        "PhoneNumberOrderId": NotRequired[str],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberOrderStatusType],
        "OrderedPhoneNumbers": NotRequired[List["OrderedPhoneNumberTypeDef"]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": NotRequired[str],
        "E164PhoneNumber": NotRequired[str],
        "Country": NotRequired[str],
        "Type": NotRequired[PhoneNumberTypeType],
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "Status": NotRequired[PhoneNumberStatusType],
        "Capabilities": NotRequired["PhoneNumberCapabilitiesTypeDef"],
        "Associations": NotRequired[List["PhoneNumberAssociationTypeDef"]],
        "CallingName": NotRequired[str],
        "CallingNameStatus": NotRequired[CallingNameStatusType],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "DeletionTimestamp": NotRequired[datetime],
    },
)

ProxySessionTypeDef = TypedDict(
    "ProxySessionTypeDef",
    {
        "VoiceConnectorId": NotRequired[str],
        "ProxySessionId": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[ProxySessionStatusType],
        "ExpiryMinutes": NotRequired[int],
        "Capabilities": NotRequired[List[CapabilityType]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "EndedTimestamp": NotRequired[datetime],
        "Participants": NotRequired[List["ParticipantTypeDef"]],
        "NumberSelectionBehavior": NotRequired[NumberSelectionBehaviorType],
        "GeoMatchLevel": NotRequired[GeoMatchLevelType],
        "GeoMatchParams": NotRequired["GeoMatchParamsTypeDef"],
    },
)

ProxyTypeDef = TypedDict(
    "ProxyTypeDef",
    {
        "DefaultSessionExpiryMinutes": NotRequired[int],
        "Disabled": NotRequired[bool],
        "FallBackPhoneNumber": NotRequired[str],
        "PhoneNumberCountries": NotRequired[List[str]],
    },
)

PutAppInstanceRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
    },
)

PutAppInstanceRetentionSettingsResponseTypeDef = TypedDict(
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    {
        "AppInstanceRetentionSettings": "AppInstanceRetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutAppInstanceStreamingConfigurationsRequestRequestTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "AppInstanceStreamingConfigurations": Sequence["AppInstanceStreamingConfigurationTypeDef"],
    },
)

PutAppInstanceStreamingConfigurationsResponseTypeDef = TypedDict(
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    {
        "AppInstanceStreamingConfigurations": List["AppInstanceStreamingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutEventsConfigurationRequestRequestTypeDef = TypedDict(
    "PutEventsConfigurationRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
        "OutboundEventsHTTPSEndpoint": NotRequired[str],
        "LambdaFunctionArn": NotRequired[str],
    },
)

PutEventsConfigurationResponseTypeDef = TypedDict(
    "PutEventsConfigurationResponseTypeDef",
    {
        "EventsConfiguration": "EventsConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRetentionSettingsRequestRequestTypeDef = TypedDict(
    "PutRetentionSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "RetentionSettings": "RetentionSettingsTypeDef",
    },
)

PutRetentionSettingsResponseTypeDef = TypedDict(
    "PutRetentionSettingsResponseTypeDef",
    {
        "RetentionSettings": "RetentionSettingsTypeDef",
        "InitiateDeletionTimestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "SipMediaApplicationLoggingConfiguration": NotRequired[
            "SipMediaApplicationLoggingConfigurationTypeDef"
        ],
    },
)

PutSipMediaApplicationLoggingConfigurationResponseTypeDef = TypedDict(
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    {
        "SipMediaApplicationLoggingConfiguration": "SipMediaApplicationLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
    },
)

PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    {
        "EmergencyCallingConfiguration": "EmergencyCallingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
    },
)

PutVoiceConnectorLoggingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    {
        "LoggingConfiguration": "LoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorOriginationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorOriginationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Origination": "OriginationTypeDef",
    },
)

PutVoiceConnectorOriginationResponseTypeDef = TypedDict(
    "PutVoiceConnectorOriginationResponseTypeDef",
    {
        "Origination": "OriginationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorProxyRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorProxyRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "DefaultSessionExpiryMinutes": int,
        "PhoneNumberPoolCountries": Sequence[str],
        "FallBackPhoneNumber": NotRequired[str],
        "Disabled": NotRequired[bool],
    },
)

PutVoiceConnectorProxyResponseTypeDef = TypedDict(
    "PutVoiceConnectorProxyResponseTypeDef",
    {
        "Proxy": "ProxyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
    },
)

PutVoiceConnectorStreamingConfigurationResponseTypeDef = TypedDict(
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    {
        "StreamingConfiguration": "StreamingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Credentials": NotRequired[Sequence["CredentialTypeDef"]],
    },
)

PutVoiceConnectorTerminationRequestRequestTypeDef = TypedDict(
    "PutVoiceConnectorTerminationRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Termination": "TerminationTypeDef",
    },
)

PutVoiceConnectorTerminationResponseTypeDef = TypedDict(
    "PutVoiceConnectorTerminationResponseTypeDef",
    {
        "Termination": "TerminationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactChannelMessageRequestRequestTypeDef = TypedDict(
    "RedactChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ChimeBearer": NotRequired[str],
    },
)

RedactChannelMessageResponseTypeDef = TypedDict(
    "RedactChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RedactConversationMessageRequestRequestTypeDef = TypedDict(
    "RedactConversationMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "ConversationId": str,
        "MessageId": str,
    },
)

RedactRoomMessageRequestRequestTypeDef = TypedDict(
    "RedactRoomMessageRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MessageId": str,
    },
)

RegenerateSecurityTokenRequestRequestTypeDef = TypedDict(
    "RegenerateSecurityTokenRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
    },
)

RegenerateSecurityTokenResponseTypeDef = TypedDict(
    "RegenerateSecurityTokenResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetPersonalPINRequestRequestTypeDef = TypedDict(
    "ResetPersonalPINRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
    },
)

ResetPersonalPINResponseTypeDef = TypedDict(
    "ResetPersonalPINResponseTypeDef",
    {
        "User": "UserTypeDef",
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

RestorePhoneNumberRequestRequestTypeDef = TypedDict(
    "RestorePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
    },
)

RestorePhoneNumberResponseTypeDef = TypedDict(
    "RestorePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetentionSettingsTypeDef = TypedDict(
    "RetentionSettingsTypeDef",
    {
        "RoomRetentionSettings": NotRequired["RoomRetentionSettingsTypeDef"],
        "ConversationRetentionSettings": NotRequired["ConversationRetentionSettingsTypeDef"],
    },
)

RoomMembershipTypeDef = TypedDict(
    "RoomMembershipTypeDef",
    {
        "RoomId": NotRequired[str],
        "Member": NotRequired["MemberTypeDef"],
        "Role": NotRequired[RoomMembershipRoleType],
        "InvitedBy": NotRequired[str],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

RoomRetentionSettingsTypeDef = TypedDict(
    "RoomRetentionSettingsTypeDef",
    {
        "RetentionDays": NotRequired[int],
    },
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomId": NotRequired[str],
        "Name": NotRequired[str],
        "AccountId": NotRequired[str],
        "CreatedBy": NotRequired[str],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

SearchAvailablePhoneNumbersRequestRequestTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersRequestRequestTypeDef",
    {
        "AreaCode": NotRequired[str],
        "City": NotRequired[str],
        "Country": NotRequired[str],
        "State": NotRequired[str],
        "TollFreePrefix": NotRequired[str],
        "PhoneNumberType": NotRequired[PhoneNumberTypeType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

SearchAvailablePhoneNumbersResponseTypeDef = TypedDict(
    "SearchAvailablePhoneNumbersResponseTypeDef",
    {
        "E164PhoneNumbers": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SelectedVideoStreamsTypeDef = TypedDict(
    "SelectedVideoStreamsTypeDef",
    {
        "AttendeeIds": NotRequired[Sequence[str]],
        "ExternalUserIds": NotRequired[Sequence[str]],
    },
)

SendChannelMessageRequestRequestTypeDef = TypedDict(
    "SendChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Content": str,
        "Type": ChannelMessageTypeType,
        "Persistence": ChannelMessagePersistenceTypeType,
        "ClientRequestToken": str,
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

SendChannelMessageResponseTypeDef = TypedDict(
    "SendChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SigninDelegateGroupTypeDef = TypedDict(
    "SigninDelegateGroupTypeDef",
    {
        "GroupName": NotRequired[str],
    },
)

SipMediaApplicationCallTypeDef = TypedDict(
    "SipMediaApplicationCallTypeDef",
    {
        "TransactionId": NotRequired[str],
    },
)

SipMediaApplicationEndpointTypeDef = TypedDict(
    "SipMediaApplicationEndpointTypeDef",
    {
        "LambdaArn": NotRequired[str],
    },
)

SipMediaApplicationLoggingConfigurationTypeDef = TypedDict(
    "SipMediaApplicationLoggingConfigurationTypeDef",
    {
        "EnableSipMediaApplicationMessageLogs": NotRequired[bool],
    },
)

SipMediaApplicationTypeDef = TypedDict(
    "SipMediaApplicationTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "AwsRegion": NotRequired[str],
        "Name": NotRequired[str],
        "Endpoints": NotRequired[List["SipMediaApplicationEndpointTypeDef"]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

SipRuleTargetApplicationTypeDef = TypedDict(
    "SipRuleTargetApplicationTypeDef",
    {
        "SipMediaApplicationId": NotRequired[str],
        "Priority": NotRequired[int],
        "AwsRegion": NotRequired[str],
    },
)

SipRuleTypeDef = TypedDict(
    "SipRuleTypeDef",
    {
        "SipRuleId": NotRequired[str],
        "Name": NotRequired[str],
        "Disabled": NotRequired[bool],
        "TriggerType": NotRequired[SipRuleTriggerTypeType],
        "TriggerValue": NotRequired[str],
        "TargetApplications": NotRequired[List["SipRuleTargetApplicationTypeDef"]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
    },
)

SourceConfigurationTypeDef = TypedDict(
    "SourceConfigurationTypeDef",
    {
        "SelectedVideoStreams": NotRequired["SelectedVideoStreamsTypeDef"],
    },
)

StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": "TranscriptionConfigurationTypeDef",
    },
)

StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

StreamingConfigurationTypeDef = TypedDict(
    "StreamingConfigurationTypeDef",
    {
        "DataRetentionInHours": int,
        "Disabled": NotRequired[bool],
        "StreamingNotificationTargets": NotRequired[List["StreamingNotificationTargetTypeDef"]],
    },
)

StreamingNotificationTargetTypeDef = TypedDict(
    "StreamingNotificationTargetTypeDef",
    {
        "NotificationTarget": NotificationTargetType,
    },
)

TagAttendeeRequestRequestTypeDef = TypedDict(
    "TagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "Tags": Sequence["TagTypeDef"],
    },
)

TagMeetingRequestRequestTypeDef = TypedDict(
    "TagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Tags": Sequence["TagTypeDef"],
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

TelephonySettingsTypeDef = TypedDict(
    "TelephonySettingsTypeDef",
    {
        "InboundCalling": bool,
        "OutboundCalling": bool,
        "SMS": bool,
    },
)

TerminationHealthTypeDef = TypedDict(
    "TerminationHealthTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "Source": NotRequired[str],
    },
)

TerminationTypeDef = TypedDict(
    "TerminationTypeDef",
    {
        "CpsLimit": NotRequired[int],
        "DefaultPhoneNumber": NotRequired[str],
        "CallingRegions": NotRequired[List[str]],
        "CidrAllowedList": NotRequired[List[str]],
        "Disabled": NotRequired[bool],
    },
)

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": NotRequired["EngineTranscribeSettingsTypeDef"],
        "EngineTranscribeMedicalSettings": NotRequired["EngineTranscribeMedicalSettingsTypeDef"],
    },
)

UntagAttendeeRequestRequestTypeDef = TypedDict(
    "UntagAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
        "TagKeys": Sequence[str],
    },
)

UntagMeetingRequestRequestTypeDef = TypedDict(
    "UntagMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TagKeys": Sequence[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)

UpdateAccountRequestRequestTypeDef = TypedDict(
    "UpdateAccountRequestRequestTypeDef",
    {
        "AccountId": str,
        "Name": NotRequired[str],
        "DefaultLicense": NotRequired[LicenseType],
    },
)

UpdateAccountResponseTypeDef = TypedDict(
    "UpdateAccountResponseTypeDef",
    {
        "Account": "AccountTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAccountSettingsRequestRequestTypeDef = TypedDict(
    "UpdateAccountSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "AccountSettings": "AccountSettingsTypeDef",
    },
)

UpdateAppInstanceRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceRequestRequestTypeDef",
    {
        "AppInstanceArn": str,
        "Name": str,
        "Metadata": NotRequired[str],
    },
)

UpdateAppInstanceResponseTypeDef = TypedDict(
    "UpdateAppInstanceResponseTypeDef",
    {
        "AppInstanceArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateAppInstanceUserRequestRequestTypeDef = TypedDict(
    "UpdateAppInstanceUserRequestRequestTypeDef",
    {
        "AppInstanceUserArn": str,
        "Name": str,
        "Metadata": NotRequired[str],
    },
)

UpdateAppInstanceUserResponseTypeDef = TypedDict(
    "UpdateAppInstanceUserResponseTypeDef",
    {
        "AppInstanceUserArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBotRequestRequestTypeDef = TypedDict(
    "UpdateBotRequestRequestTypeDef",
    {
        "AccountId": str,
        "BotId": str,
        "Disabled": NotRequired[bool],
    },
)

UpdateBotResponseTypeDef = TypedDict(
    "UpdateBotResponseTypeDef",
    {
        "Bot": "BotTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelMessageRequestRequestTypeDef = TypedDict(
    "UpdateChannelMessageRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": NotRequired[str],
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

UpdateChannelMessageResponseTypeDef = TypedDict(
    "UpdateChannelMessageResponseTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelReadMarkerRequestRequestTypeDef = TypedDict(
    "UpdateChannelReadMarkerRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "ChimeBearer": NotRequired[str],
    },
)

UpdateChannelReadMarkerResponseTypeDef = TypedDict(
    "UpdateChannelReadMarkerResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "ChannelArn": str,
        "Name": str,
        "Mode": ChannelModeType,
        "Metadata": NotRequired[str],
        "ChimeBearer": NotRequired[str],
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "ChannelArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGlobalSettingsRequestRequestTypeDef = TypedDict(
    "UpdateGlobalSettingsRequestRequestTypeDef",
    {
        "BusinessCalling": NotRequired["BusinessCallingSettingsTypeDef"],
        "VoiceConnector": NotRequired["VoiceConnectorSettingsTypeDef"],
    },
)

UpdatePhoneNumberRequestItemTypeDef = TypedDict(
    "UpdatePhoneNumberRequestItemTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
    },
)

UpdatePhoneNumberRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberRequestRequestTypeDef",
    {
        "PhoneNumberId": str,
        "ProductType": NotRequired[PhoneNumberProductTypeType],
        "CallingName": NotRequired[str],
    },
)

UpdatePhoneNumberResponseTypeDef = TypedDict(
    "UpdatePhoneNumberResponseTypeDef",
    {
        "PhoneNumber": "PhoneNumberTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePhoneNumberSettingsRequestRequestTypeDef = TypedDict(
    "UpdatePhoneNumberSettingsRequestRequestTypeDef",
    {
        "CallingName": str,
    },
)

UpdateProxySessionRequestRequestTypeDef = TypedDict(
    "UpdateProxySessionRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "ProxySessionId": str,
        "Capabilities": Sequence[CapabilityType],
        "ExpiryMinutes": NotRequired[int],
    },
)

UpdateProxySessionResponseTypeDef = TypedDict(
    "UpdateProxySessionResponseTypeDef",
    {
        "ProxySession": "ProxySessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRoomMembershipRequestRequestTypeDef = TypedDict(
    "UpdateRoomMembershipRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "MemberId": str,
        "Role": NotRequired[RoomMembershipRoleType],
    },
)

UpdateRoomMembershipResponseTypeDef = TypedDict(
    "UpdateRoomMembershipResponseTypeDef",
    {
        "RoomMembership": "RoomMembershipTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRoomRequestRequestTypeDef = TypedDict(
    "UpdateRoomRequestRequestTypeDef",
    {
        "AccountId": str,
        "RoomId": str,
        "Name": NotRequired[str],
    },
)

UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "Room": "RoomTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationCallRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "TransactionId": str,
        "Arguments": Mapping[str, str],
    },
)

UpdateSipMediaApplicationCallResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationCallResponseTypeDef",
    {
        "SipMediaApplicationCall": "SipMediaApplicationCallTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipMediaApplicationRequestRequestTypeDef = TypedDict(
    "UpdateSipMediaApplicationRequestRequestTypeDef",
    {
        "SipMediaApplicationId": str,
        "Name": NotRequired[str],
        "Endpoints": NotRequired[Sequence["SipMediaApplicationEndpointTypeDef"]],
    },
)

UpdateSipMediaApplicationResponseTypeDef = TypedDict(
    "UpdateSipMediaApplicationResponseTypeDef",
    {
        "SipMediaApplication": "SipMediaApplicationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSipRuleRequestRequestTypeDef = TypedDict(
    "UpdateSipRuleRequestRequestTypeDef",
    {
        "SipRuleId": str,
        "Name": str,
        "Disabled": NotRequired[bool],
        "TargetApplications": NotRequired[Sequence["SipRuleTargetApplicationTypeDef"]],
    },
)

UpdateSipRuleResponseTypeDef = TypedDict(
    "UpdateSipRuleResponseTypeDef",
    {
        "SipRule": "SipRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserRequestItemTypeDef = TypedDict(
    "UpdateUserRequestItemTypeDef",
    {
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired["AlexaForBusinessMetadataTypeDef"],
    },
)

UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "AlexaForBusinessMetadata": NotRequired["AlexaForBusinessMetadataTypeDef"],
    },
)

UpdateUserResponseTypeDef = TypedDict(
    "UpdateUserResponseTypeDef",
    {
        "User": "UserTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestRequestTypeDef",
    {
        "AccountId": str,
        "UserId": str,
        "UserSettings": "UserSettingsTypeDef",
    },
)

UpdateVoiceConnectorGroupRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupRequestRequestTypeDef",
    {
        "VoiceConnectorGroupId": str,
        "Name": str,
        "VoiceConnectorItems": Sequence["VoiceConnectorItemTypeDef"],
    },
)

UpdateVoiceConnectorGroupResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorGroupResponseTypeDef",
    {
        "VoiceConnectorGroup": "VoiceConnectorGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVoiceConnectorRequestRequestTypeDef = TypedDict(
    "UpdateVoiceConnectorRequestRequestTypeDef",
    {
        "VoiceConnectorId": str,
        "Name": str,
        "RequireEncryption": bool,
    },
)

UpdateVoiceConnectorResponseTypeDef = TypedDict(
    "UpdateVoiceConnectorResponseTypeDef",
    {
        "VoiceConnector": "VoiceConnectorTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserErrorTypeDef = TypedDict(
    "UserErrorTypeDef",
    {
        "UserId": NotRequired[str],
        "ErrorCode": NotRequired[ErrorCodeType],
        "ErrorMessage": NotRequired[str],
    },
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "Telephony": "TelephonySettingsTypeDef",
    },
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "UserId": str,
        "AccountId": NotRequired[str],
        "PrimaryEmail": NotRequired[str],
        "PrimaryProvisionedNumber": NotRequired[str],
        "DisplayName": NotRequired[str],
        "LicenseType": NotRequired[LicenseType],
        "UserType": NotRequired[UserTypeType],
        "UserRegistrationStatus": NotRequired[RegistrationStatusType],
        "UserInvitationStatus": NotRequired[InviteStatusType],
        "RegisteredOn": NotRequired[datetime],
        "InvitedOn": NotRequired[datetime],
        "AlexaForBusinessMetadata": NotRequired["AlexaForBusinessMetadataTypeDef"],
        "PersonalPIN": NotRequired[str],
    },
)

VideoArtifactsConfigurationTypeDef = TypedDict(
    "VideoArtifactsConfigurationTypeDef",
    {
        "State": ArtifactsStateType,
        "MuxType": NotRequired[Literal["VideoOnly"]],
    },
)

VoiceConnectorGroupTypeDef = TypedDict(
    "VoiceConnectorGroupTypeDef",
    {
        "VoiceConnectorGroupId": NotRequired[str],
        "Name": NotRequired[str],
        "VoiceConnectorItems": NotRequired[List["VoiceConnectorItemTypeDef"]],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "VoiceConnectorGroupArn": NotRequired[str],
    },
)

VoiceConnectorItemTypeDef = TypedDict(
    "VoiceConnectorItemTypeDef",
    {
        "VoiceConnectorId": str,
        "Priority": int,
    },
)

VoiceConnectorSettingsTypeDef = TypedDict(
    "VoiceConnectorSettingsTypeDef",
    {
        "CdrBucket": NotRequired[str],
    },
)

VoiceConnectorTypeDef = TypedDict(
    "VoiceConnectorTypeDef",
    {
        "VoiceConnectorId": NotRequired[str],
        "AwsRegion": NotRequired[VoiceConnectorAwsRegionType],
        "Name": NotRequired[str],
        "OutboundHostName": NotRequired[str],
        "RequireEncryption": NotRequired[bool],
        "CreatedTimestamp": NotRequired[datetime],
        "UpdatedTimestamp": NotRequired[datetime],
        "VoiceConnectorArn": NotRequired[str],
    },
)
