"""
Type annotations for lexv2-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lexv2_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lexv2_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ConfirmationStateType,
    DialogActionTypeType,
    IntentStateType,
    MessageContentTypeType,
    SentimentTypeType,
    ShapeType,
    StyleTypeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "ConfidenceScoreTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "ImageResponseCardTypeDef",
    "IntentTypeDef",
    "InterpretationTypeDef",
    "MessageTypeDef",
    "PutSessionRequestRequestTypeDef",
    "PutSessionResponseTypeDef",
    "RecognizeTextRequestRequestTypeDef",
    "RecognizeTextResponseTypeDef",
    "RecognizeUtteranceRequestRequestTypeDef",
    "RecognizeUtteranceResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RuntimeHintDetailsTypeDef",
    "RuntimeHintValueTypeDef",
    "RuntimeHintsTypeDef",
    "SentimentResponseTypeDef",
    "SentimentScoreTypeDef",
    "SessionStateTypeDef",
    "SlotTypeDef",
    "ValueTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": int,
        "turnsToLive": int,
    },
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveTypeDef",
        "contextAttributes": Dict[str, str],
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

ConfidenceScoreTypeDef = TypedDict(
    "ConfidenceScoreTypeDef",
    {
        "score": NotRequired[float],
    },
)

DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "slotToElicit": NotRequired[str],
        "slotElicitationStyle": NotRequired[StyleTypeType],
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "sessionId": str,
        "messages": List["MessageTypeDef"],
        "interpretations": List["InterpretationTypeDef"],
        "sessionState": "SessionStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageResponseCardTypeDef = TypedDict(
    "ImageResponseCardTypeDef",
    {
        "title": str,
        "subtitle": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List["ButtonTypeDef"]],
    },
)

IntentTypeDef = TypedDict(
    "IntentTypeDef",
    {
        "name": str,
        "slots": NotRequired[Dict[str, "SlotTypeDef"]],
        "state": NotRequired[IntentStateType],
        "confirmationState": NotRequired[ConfirmationStateType],
    },
)

InterpretationTypeDef = TypedDict(
    "InterpretationTypeDef",
    {
        "nluConfidence": NotRequired["ConfidenceScoreTypeDef"],
        "sentimentResponse": NotRequired["SentimentResponseTypeDef"],
        "intent": NotRequired["IntentTypeDef"],
    },
)

MessageTypeDef = TypedDict(
    "MessageTypeDef",
    {
        "contentType": MessageContentTypeType,
        "content": NotRequired[str],
        "imageResponseCard": NotRequired["ImageResponseCardTypeDef"],
    },
)

PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "sessionState": "SessionStateTypeDef",
        "messages": NotRequired[Sequence["MessageTypeDef"]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "responseContentType": NotRequired[str],
    },
)

PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "messages": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "audioStream": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecognizeTextRequestRequestTypeDef = TypedDict(
    "RecognizeTextRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "text": str,
        "sessionState": NotRequired["SessionStateTypeDef"],
        "requestAttributes": NotRequired[Mapping[str, str]],
    },
)

RecognizeTextResponseTypeDef = TypedDict(
    "RecognizeTextResponseTypeDef",
    {
        "messages": List["MessageTypeDef"],
        "sessionState": "SessionStateTypeDef",
        "interpretations": List["InterpretationTypeDef"],
        "requestAttributes": Dict[str, str],
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RecognizeUtteranceRequestRequestTypeDef = TypedDict(
    "RecognizeUtteranceRequestRequestTypeDef",
    {
        "botId": str,
        "botAliasId": str,
        "localeId": str,
        "sessionId": str,
        "requestContentType": str,
        "sessionState": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "responseContentType": NotRequired[str],
        "inputStream": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
    },
)

RecognizeUtteranceResponseTypeDef = TypedDict(
    "RecognizeUtteranceResponseTypeDef",
    {
        "inputMode": str,
        "contentType": str,
        "messages": str,
        "interpretations": str,
        "sessionState": str,
        "requestAttributes": str,
        "sessionId": str,
        "inputTranscript": str,
        "audioStream": StreamingBody,
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

RuntimeHintDetailsTypeDef = TypedDict(
    "RuntimeHintDetailsTypeDef",
    {
        "runtimeHintValues": List["RuntimeHintValueTypeDef"],
    },
)

RuntimeHintValueTypeDef = TypedDict(
    "RuntimeHintValueTypeDef",
    {
        "phrase": str,
    },
)

RuntimeHintsTypeDef = TypedDict(
    "RuntimeHintsTypeDef",
    {
        "slotHints": NotRequired[Dict[str, Dict[str, "RuntimeHintDetailsTypeDef"]]],
    },
)

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentiment": NotRequired[SentimentTypeType],
        "sentimentScore": NotRequired["SentimentScoreTypeDef"],
    },
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {
        "positive": NotRequired[float],
        "negative": NotRequired[float],
        "neutral": NotRequired[float],
        "mixed": NotRequired[float],
    },
)

SessionStateTypeDef = TypedDict(
    "SessionStateTypeDef",
    {
        "dialogAction": NotRequired["DialogActionTypeDef"],
        "intent": NotRequired["IntentTypeDef"],
        "activeContexts": NotRequired[List["ActiveContextTypeDef"]],
        "sessionAttributes": NotRequired[Dict[str, str]],
        "originatingRequestId": NotRequired[str],
        "runtimeHints": NotRequired["RuntimeHintsTypeDef"],
    },
)

SlotTypeDef = TypedDict(
    "SlotTypeDef",
    {
        "value": NotRequired["ValueTypeDef"],
        "shape": NotRequired[ShapeType],
        "values": NotRequired[List[Dict[str, Any]]],
    },
)

ValueTypeDef = TypedDict(
    "ValueTypeDef",
    {
        "interpretedValue": str,
        "originalValue": NotRequired[str],
        "resolvedValues": NotRequired[List[str]],
    },
)
