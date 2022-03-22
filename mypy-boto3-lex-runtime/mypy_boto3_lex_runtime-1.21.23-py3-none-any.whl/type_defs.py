"""
Type annotations for lex-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lex_runtime.type_defs import ActiveContextTimeToLiveTypeDef

    data: ActiveContextTimeToLiveTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ConfirmationStatusType,
    DialogActionTypeType,
    DialogStateType,
    FulfillmentStateType,
    MessageFormatTypeType,
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
    "ActiveContextTimeToLiveTypeDef",
    "ActiveContextTypeDef",
    "ButtonTypeDef",
    "DeleteSessionRequestRequestTypeDef",
    "DeleteSessionResponseTypeDef",
    "DialogActionTypeDef",
    "GenericAttachmentTypeDef",
    "GetSessionRequestRequestTypeDef",
    "GetSessionResponseTypeDef",
    "IntentConfidenceTypeDef",
    "IntentSummaryTypeDef",
    "PostContentRequestRequestTypeDef",
    "PostContentResponseTypeDef",
    "PostTextRequestRequestTypeDef",
    "PostTextResponseTypeDef",
    "PredictedIntentTypeDef",
    "PutSessionRequestRequestTypeDef",
    "PutSessionResponseTypeDef",
    "ResponseCardTypeDef",
    "ResponseMetadataTypeDef",
    "SentimentResponseTypeDef",
)

ActiveContextTimeToLiveTypeDef = TypedDict(
    "ActiveContextTimeToLiveTypeDef",
    {
        "timeToLiveInSeconds": NotRequired[int],
        "turnsToLive": NotRequired[int],
    },
)

ActiveContextTypeDef = TypedDict(
    "ActiveContextTypeDef",
    {
        "name": str,
        "timeToLive": "ActiveContextTimeToLiveTypeDef",
        "parameters": Dict[str, str],
    },
)

ButtonTypeDef = TypedDict(
    "ButtonTypeDef",
    {
        "text": str,
        "value": str,
    },
)

DeleteSessionRequestRequestTypeDef = TypedDict(
    "DeleteSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
    },
)

DeleteSessionResponseTypeDef = TypedDict(
    "DeleteSessionResponseTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DialogActionTypeDef = TypedDict(
    "DialogActionTypeDef",
    {
        "type": DialogActionTypeType,
        "intentName": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "slotToElicit": NotRequired[str],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "message": NotRequired[str],
        "messageFormat": NotRequired[MessageFormatTypeType],
    },
)

GenericAttachmentTypeDef = TypedDict(
    "GenericAttachmentTypeDef",
    {
        "title": NotRequired[str],
        "subTitle": NotRequired[str],
        "attachmentLinkUrl": NotRequired[str],
        "imageUrl": NotRequired[str],
        "buttons": NotRequired[List["ButtonTypeDef"]],
    },
)

GetSessionRequestRequestTypeDef = TypedDict(
    "GetSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "checkpointLabelFilter": NotRequired[str],
    },
)

GetSessionResponseTypeDef = TypedDict(
    "GetSessionResponseTypeDef",
    {
        "recentIntentSummaryView": List["IntentSummaryTypeDef"],
        "sessionAttributes": Dict[str, str],
        "sessionId": str,
        "dialogAction": "DialogActionTypeDef",
        "activeContexts": List["ActiveContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IntentConfidenceTypeDef = TypedDict(
    "IntentConfidenceTypeDef",
    {
        "score": NotRequired[float],
    },
)

IntentSummaryTypeDef = TypedDict(
    "IntentSummaryTypeDef",
    {
        "dialogActionType": DialogActionTypeType,
        "intentName": NotRequired[str],
        "checkpointLabel": NotRequired[str],
        "slots": NotRequired[Dict[str, str]],
        "confirmationStatus": NotRequired[ConfirmationStatusType],
        "fulfillmentState": NotRequired[FulfillmentStateType],
        "slotToElicit": NotRequired[str],
    },
)

PostContentRequestRequestTypeDef = TypedDict(
    "PostContentRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "contentType": str,
        "inputStream": Union[bytes, IO[bytes], StreamingBody],
        "sessionAttributes": NotRequired[str],
        "requestAttributes": NotRequired[str],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[str],
    },
)

PostContentResponseTypeDef = TypedDict(
    "PostContentResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "nluIntentConfidence": str,
        "alternativeIntents": str,
        "slots": str,
        "sessionAttributes": str,
        "sentimentResponse": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "inputTranscript": str,
        "encodedInputTranscript": str,
        "audioStream": StreamingBody,
        "botVersion": str,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PostTextRequestRequestTypeDef = TypedDict(
    "PostTextRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "inputText": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "requestAttributes": NotRequired[Mapping[str, str]],
        "activeContexts": NotRequired[Sequence["ActiveContextTypeDef"]],
    },
)

PostTextResponseTypeDef = TypedDict(
    "PostTextResponseTypeDef",
    {
        "intentName": str,
        "nluIntentConfidence": "IntentConfidenceTypeDef",
        "alternativeIntents": List["PredictedIntentTypeDef"],
        "slots": Dict[str, str],
        "sessionAttributes": Dict[str, str],
        "message": str,
        "sentimentResponse": "SentimentResponseTypeDef",
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "responseCard": "ResponseCardTypeDef",
        "sessionId": str,
        "botVersion": str,
        "activeContexts": List["ActiveContextTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PredictedIntentTypeDef = TypedDict(
    "PredictedIntentTypeDef",
    {
        "intentName": NotRequired[str],
        "nluIntentConfidence": NotRequired["IntentConfidenceTypeDef"],
        "slots": NotRequired[Dict[str, str]],
    },
)

PutSessionRequestRequestTypeDef = TypedDict(
    "PutSessionRequestRequestTypeDef",
    {
        "botName": str,
        "botAlias": str,
        "userId": str,
        "sessionAttributes": NotRequired[Mapping[str, str]],
        "dialogAction": NotRequired["DialogActionTypeDef"],
        "recentIntentSummaryView": NotRequired[Sequence["IntentSummaryTypeDef"]],
        "accept": NotRequired[str],
        "activeContexts": NotRequired[Sequence["ActiveContextTypeDef"]],
    },
)

PutSessionResponseTypeDef = TypedDict(
    "PutSessionResponseTypeDef",
    {
        "contentType": str,
        "intentName": str,
        "slots": str,
        "sessionAttributes": str,
        "message": str,
        "encodedMessage": str,
        "messageFormat": MessageFormatTypeType,
        "dialogState": DialogStateType,
        "slotToElicit": str,
        "audioStream": StreamingBody,
        "sessionId": str,
        "activeContexts": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResponseCardTypeDef = TypedDict(
    "ResponseCardTypeDef",
    {
        "version": NotRequired[str],
        "contentType": NotRequired[Literal["application/vnd.amazonaws.card.generic"]],
        "genericAttachments": NotRequired[List["GenericAttachmentTypeDef"]],
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

SentimentResponseTypeDef = TypedDict(
    "SentimentResponseTypeDef",
    {
        "sentimentLabel": NotRequired[str],
        "sentimentScore": NotRequired[str],
    },
)
