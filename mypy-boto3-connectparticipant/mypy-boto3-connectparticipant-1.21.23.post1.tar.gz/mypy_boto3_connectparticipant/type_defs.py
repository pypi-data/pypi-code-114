"""
Type annotations for connectparticipant service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connectparticipant/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connectparticipant.type_defs import AttachmentItemTypeDef

    data: AttachmentItemTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from typing_extensions import NotRequired

from .literals import (
    ArtifactStatusType,
    ChatItemTypeType,
    ConnectionTypeType,
    ParticipantRoleType,
    ScanDirectionType,
    SortKeyType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentItemTypeDef",
    "CompleteAttachmentUploadRequestRequestTypeDef",
    "ConnectionCredentialsTypeDef",
    "CreateParticipantConnectionRequestRequestTypeDef",
    "CreateParticipantConnectionResponseTypeDef",
    "DisconnectParticipantRequestRequestTypeDef",
    "GetAttachmentRequestRequestTypeDef",
    "GetAttachmentResponseTypeDef",
    "GetTranscriptRequestRequestTypeDef",
    "GetTranscriptResponseTypeDef",
    "ItemTypeDef",
    "ResponseMetadataTypeDef",
    "SendEventRequestRequestTypeDef",
    "SendEventResponseTypeDef",
    "SendMessageRequestRequestTypeDef",
    "SendMessageResponseTypeDef",
    "StartAttachmentUploadRequestRequestTypeDef",
    "StartAttachmentUploadResponseTypeDef",
    "StartPositionTypeDef",
    "UploadMetadataTypeDef",
    "WebsocketTypeDef",
)

AttachmentItemTypeDef = TypedDict(
    "AttachmentItemTypeDef",
    {
        "ContentType": NotRequired[str],
        "AttachmentId": NotRequired[str],
        "AttachmentName": NotRequired[str],
        "Status": NotRequired[ArtifactStatusType],
    },
)

CompleteAttachmentUploadRequestRequestTypeDef = TypedDict(
    "CompleteAttachmentUploadRequestRequestTypeDef",
    {
        "AttachmentIds": Sequence[str],
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

ConnectionCredentialsTypeDef = TypedDict(
    "ConnectionCredentialsTypeDef",
    {
        "ConnectionToken": NotRequired[str],
        "Expiry": NotRequired[str],
    },
)

CreateParticipantConnectionRequestRequestTypeDef = TypedDict(
    "CreateParticipantConnectionRequestRequestTypeDef",
    {
        "Type": Sequence[ConnectionTypeType],
        "ParticipantToken": str,
        "ConnectParticipant": NotRequired[bool],
    },
)

CreateParticipantConnectionResponseTypeDef = TypedDict(
    "CreateParticipantConnectionResponseTypeDef",
    {
        "Websocket": "WebsocketTypeDef",
        "ConnectionCredentials": "ConnectionCredentialsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisconnectParticipantRequestRequestTypeDef = TypedDict(
    "DisconnectParticipantRequestRequestTypeDef",
    {
        "ConnectionToken": str,
        "ClientToken": NotRequired[str],
    },
)

GetAttachmentRequestRequestTypeDef = TypedDict(
    "GetAttachmentRequestRequestTypeDef",
    {
        "AttachmentId": str,
        "ConnectionToken": str,
    },
)

GetAttachmentResponseTypeDef = TypedDict(
    "GetAttachmentResponseTypeDef",
    {
        "Url": str,
        "UrlExpiry": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTranscriptRequestRequestTypeDef = TypedDict(
    "GetTranscriptRequestRequestTypeDef",
    {
        "ConnectionToken": str,
        "ContactId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "ScanDirection": NotRequired[ScanDirectionType],
        "SortOrder": NotRequired[SortKeyType],
        "StartPosition": NotRequired["StartPositionTypeDef"],
    },
)

GetTranscriptResponseTypeDef = TypedDict(
    "GetTranscriptResponseTypeDef",
    {
        "InitialContactId": str,
        "Transcript": List["ItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "AbsoluteTime": NotRequired[str],
        "Content": NotRequired[str],
        "ContentType": NotRequired[str],
        "Id": NotRequired[str],
        "Type": NotRequired[ChatItemTypeType],
        "ParticipantId": NotRequired[str],
        "DisplayName": NotRequired[str],
        "ParticipantRole": NotRequired[ParticipantRoleType],
        "Attachments": NotRequired[List["AttachmentItemTypeDef"]],
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

SendEventRequestRequestTypeDef = TypedDict(
    "SendEventRequestRequestTypeDef",
    {
        "ContentType": str,
        "ConnectionToken": str,
        "Content": NotRequired[str],
        "ClientToken": NotRequired[str],
    },
)

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SendMessageRequestRequestTypeDef = TypedDict(
    "SendMessageRequestRequestTypeDef",
    {
        "ContentType": str,
        "Content": str,
        "ConnectionToken": str,
        "ClientToken": NotRequired[str],
    },
)

SendMessageResponseTypeDef = TypedDict(
    "SendMessageResponseTypeDef",
    {
        "Id": str,
        "AbsoluteTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAttachmentUploadRequestRequestTypeDef = TypedDict(
    "StartAttachmentUploadRequestRequestTypeDef",
    {
        "ContentType": str,
        "AttachmentSizeInBytes": int,
        "AttachmentName": str,
        "ClientToken": str,
        "ConnectionToken": str,
    },
)

StartAttachmentUploadResponseTypeDef = TypedDict(
    "StartAttachmentUploadResponseTypeDef",
    {
        "AttachmentId": str,
        "UploadMetadata": "UploadMetadataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartPositionTypeDef = TypedDict(
    "StartPositionTypeDef",
    {
        "Id": NotRequired[str],
        "AbsoluteTime": NotRequired[str],
        "MostRecent": NotRequired[int],
    },
)

UploadMetadataTypeDef = TypedDict(
    "UploadMetadataTypeDef",
    {
        "Url": NotRequired[str],
        "UrlExpiry": NotRequired[str],
        "HeadersToInclude": NotRequired[Dict[str, str]],
    },
)

WebsocketTypeDef = TypedDict(
    "WebsocketTypeDef",
    {
        "Url": NotRequired[str],
        "ConnectionExpiry": NotRequired[str],
    },
)
