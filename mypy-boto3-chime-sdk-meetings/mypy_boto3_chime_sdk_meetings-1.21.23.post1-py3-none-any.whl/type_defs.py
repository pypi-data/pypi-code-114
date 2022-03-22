"""
Type annotations for chime-sdk-meetings service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime_sdk_meetings/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime_sdk_meetings.type_defs import AttendeeTypeDef

    data: AttendeeTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
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
    "AttendeeTypeDef",
    "AudioFeaturesTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "GetMeetingResponseTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "ListAttendeesResponseTypeDef",
    "MediaPlacementTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "MeetingTypeDef",
    "NotificationsConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "TranscriptionConfigurationTypeDef",
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": NotRequired[str],
        "AttendeeId": NotRequired[str],
        "JoinToken": NotRequired[str],
    },
)

AudioFeaturesTypeDef = TypedDict(
    "AudioFeaturesTypeDef",
    {
        "EchoReduction": NotRequired[MeetingFeatureStatusType],
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
    },
)

CreateAttendeeRequestRequestTypeDef = TypedDict(
    "CreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": "AttendeeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateMeetingRequestRequestTypeDef = TypedDict(
    "CreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "MeetingHostId": NotRequired[str],
        "NotificationsConfiguration": NotRequired["NotificationsConfigurationTypeDef"],
        "MeetingFeatures": NotRequired["MeetingFeaturesConfigurationTypeDef"],
        "PrimaryMeetingId": NotRequired[str],
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
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "Attendees": Sequence["CreateAttendeeRequestItemTypeDef"],
        "MeetingHostId": NotRequired[str],
        "MeetingFeatures": NotRequired["MeetingFeaturesConfigurationTypeDef"],
        "NotificationsConfiguration": NotRequired["NotificationsConfigurationTypeDef"],
        "PrimaryMeetingId": NotRequired[str],
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

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
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
        "LanguageCode": NotRequired[TranscribeLanguageCodeType],
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
        "IdentifyLanguage": NotRequired[bool],
        "LanguageOptions": NotRequired[str],
        "PreferredLanguage": NotRequired[TranscribeLanguageCodeType],
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

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": NotRequired[str],
        "AudioFallbackUrl": NotRequired[str],
        "SignalingUrl": NotRequired[str],
        "TurnControlUrl": NotRequired[str],
        "ScreenDataUrl": NotRequired[str],
        "ScreenViewingUrl": NotRequired[str],
        "ScreenSharingUrl": NotRequired[str],
        "EventIngestionUrl": NotRequired[str],
    },
)

MeetingFeaturesConfigurationTypeDef = TypedDict(
    "MeetingFeaturesConfigurationTypeDef",
    {
        "Audio": NotRequired["AudioFeaturesTypeDef"],
    },
)

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": NotRequired[str],
        "MeetingHostId": NotRequired[str],
        "ExternalMeetingId": NotRequired[str],
        "MediaRegion": NotRequired[str],
        "MediaPlacement": NotRequired["MediaPlacementTypeDef"],
        "MeetingFeatures": NotRequired["MeetingFeaturesConfigurationTypeDef"],
        "PrimaryMeetingId": NotRequired[str],
    },
)

NotificationsConfigurationTypeDef = TypedDict(
    "NotificationsConfigurationTypeDef",
    {
        "LambdaFunctionArn": NotRequired[str],
        "SnsTopicArn": NotRequired[str],
        "SqsQueueArn": NotRequired[str],
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

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": NotRequired["EngineTranscribeSettingsTypeDef"],
        "EngineTranscribeMedicalSettings": NotRequired["EngineTranscribeMedicalSettingsTypeDef"],
    },
)
