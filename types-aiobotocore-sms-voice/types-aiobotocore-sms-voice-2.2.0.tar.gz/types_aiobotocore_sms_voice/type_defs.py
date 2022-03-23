"""
Type annotations for sms-voice service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_sms_voice/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_sms_voice.type_defs import CallInstructionsMessageTypeTypeDef

    data: CallInstructionsMessageTypeTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import EventTypeType

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CallInstructionsMessageTypeTypeDef",
    "CloudWatchLogsDestinationTypeDef",
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    "CreateConfigurationSetRequestRequestTypeDef",
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    "DeleteConfigurationSetRequestRequestTypeDef",
    "EventDestinationDefinitionTypeDef",
    "EventDestinationTypeDef",
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    "KinesisFirehoseDestinationTypeDef",
    "ListConfigurationSetsRequestRequestTypeDef",
    "ListConfigurationSetsResponseTypeDef",
    "PlainTextMessageTypeTypeDef",
    "ResponseMetadataTypeDef",
    "SSMLMessageTypeTypeDef",
    "SendVoiceMessageRequestRequestTypeDef",
    "SendVoiceMessageResponseTypeDef",
    "SnsDestinationTypeDef",
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    "VoiceMessageContentTypeDef",
)

CallInstructionsMessageTypeTypeDef = TypedDict(
    "CallInstructionsMessageTypeTypeDef",
    {
        "Text": NotRequired[str],
    },
)

CloudWatchLogsDestinationTypeDef = TypedDict(
    "CloudWatchLogsDestinationTypeDef",
    {
        "IamRoleArn": NotRequired[str],
        "LogGroupArn": NotRequired[str],
    },
)

CreateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestination": NotRequired["EventDestinationDefinitionTypeDef"],
        "EventDestinationName": NotRequired[str],
    },
)

CreateConfigurationSetRequestRequestTypeDef = TypedDict(
    "CreateConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": NotRequired[str],
    },
)

DeleteConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
    },
)

DeleteConfigurationSetRequestRequestTypeDef = TypedDict(
    "DeleteConfigurationSetRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

EventDestinationDefinitionTypeDef = TypedDict(
    "EventDestinationDefinitionTypeDef",
    {
        "CloudWatchLogsDestination": NotRequired["CloudWatchLogsDestinationTypeDef"],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired["KinesisFirehoseDestinationTypeDef"],
        "MatchingEventTypes": NotRequired[Sequence[EventTypeType]],
        "SnsDestination": NotRequired["SnsDestinationTypeDef"],
    },
)

EventDestinationTypeDef = TypedDict(
    "EventDestinationTypeDef",
    {
        "CloudWatchLogsDestination": NotRequired["CloudWatchLogsDestinationTypeDef"],
        "Enabled": NotRequired[bool],
        "KinesisFirehoseDestination": NotRequired["KinesisFirehoseDestinationTypeDef"],
        "MatchingEventTypes": NotRequired[List[EventTypeType]],
        "Name": NotRequired[str],
        "SnsDestination": NotRequired["SnsDestinationTypeDef"],
    },
)

GetConfigurationSetEventDestinationsRequestRequestTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
    },
)

GetConfigurationSetEventDestinationsResponseTypeDef = TypedDict(
    "GetConfigurationSetEventDestinationsResponseTypeDef",
    {
        "EventDestinations": List["EventDestinationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

KinesisFirehoseDestinationTypeDef = TypedDict(
    "KinesisFirehoseDestinationTypeDef",
    {
        "DeliveryStreamArn": NotRequired[str],
        "IamRoleArn": NotRequired[str],
    },
)

ListConfigurationSetsRequestRequestTypeDef = TypedDict(
    "ListConfigurationSetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "PageSize": NotRequired[str],
    },
)

ListConfigurationSetsResponseTypeDef = TypedDict(
    "ListConfigurationSetsResponseTypeDef",
    {
        "ConfigurationSets": List[str],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PlainTextMessageTypeTypeDef = TypedDict(
    "PlainTextMessageTypeTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Text": NotRequired[str],
        "VoiceId": NotRequired[str],
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

SSMLMessageTypeTypeDef = TypedDict(
    "SSMLMessageTypeTypeDef",
    {
        "LanguageCode": NotRequired[str],
        "Text": NotRequired[str],
        "VoiceId": NotRequired[str],
    },
)

SendVoiceMessageRequestRequestTypeDef = TypedDict(
    "SendVoiceMessageRequestRequestTypeDef",
    {
        "CallerId": NotRequired[str],
        "ConfigurationSetName": NotRequired[str],
        "Content": NotRequired["VoiceMessageContentTypeDef"],
        "DestinationPhoneNumber": NotRequired[str],
        "OriginationPhoneNumber": NotRequired[str],
    },
)

SendVoiceMessageResponseTypeDef = TypedDict(
    "SendVoiceMessageResponseTypeDef",
    {
        "MessageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnsDestinationTypeDef = TypedDict(
    "SnsDestinationTypeDef",
    {
        "TopicArn": NotRequired[str],
    },
)

UpdateConfigurationSetEventDestinationRequestRequestTypeDef = TypedDict(
    "UpdateConfigurationSetEventDestinationRequestRequestTypeDef",
    {
        "ConfigurationSetName": str,
        "EventDestinationName": str,
        "EventDestination": NotRequired["EventDestinationDefinitionTypeDef"],
    },
)

VoiceMessageContentTypeDef = TypedDict(
    "VoiceMessageContentTypeDef",
    {
        "CallInstructionsMessage": NotRequired["CallInstructionsMessageTypeTypeDef"],
        "PlainTextMessage": NotRequired["PlainTextMessageTypeTypeDef"],
        "SSMLMessage": NotRequired["SSMLMessageTypeTypeDef"],
    },
)
