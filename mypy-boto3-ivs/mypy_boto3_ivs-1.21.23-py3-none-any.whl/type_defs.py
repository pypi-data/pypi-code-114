"""
Type annotations for ivs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import AudioConfigurationTypeDef

    data: AudioConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    ChannelLatencyModeType,
    ChannelTypeType,
    RecordingConfigurationStateType,
    RecordingModeType,
    StreamHealthType,
    StreamStateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AudioConfigurationTypeDef",
    "BatchErrorTypeDef",
    "BatchGetChannelRequestRequestTypeDef",
    "BatchGetChannelResponseTypeDef",
    "BatchGetStreamKeyRequestRequestTypeDef",
    "BatchGetStreamKeyResponseTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateRecordingConfigurationRequestRequestTypeDef",
    "CreateRecordingConfigurationResponseTypeDef",
    "CreateStreamKeyRequestRequestTypeDef",
    "CreateStreamKeyResponseTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeletePlaybackKeyPairRequestRequestTypeDef",
    "DeleteRecordingConfigurationRequestRequestTypeDef",
    "DeleteStreamKeyRequestRequestTypeDef",
    "DestinationConfigurationTypeDef",
    "GetChannelRequestRequestTypeDef",
    "GetChannelResponseTypeDef",
    "GetPlaybackKeyPairRequestRequestTypeDef",
    "GetPlaybackKeyPairResponseTypeDef",
    "GetRecordingConfigurationRequestRequestTypeDef",
    "GetRecordingConfigurationResponseTypeDef",
    "GetStreamKeyRequestRequestTypeDef",
    "GetStreamKeyResponseTypeDef",
    "GetStreamRequestRequestTypeDef",
    "GetStreamResponseTypeDef",
    "GetStreamSessionRequestRequestTypeDef",
    "GetStreamSessionResponseTypeDef",
    "ImportPlaybackKeyPairRequestRequestTypeDef",
    "ImportPlaybackKeyPairResponseTypeDef",
    "IngestConfigurationTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackKeyPairsRequestRequestTypeDef",
    "ListPlaybackKeyPairsResponseTypeDef",
    "ListRecordingConfigurationsRequestRequestTypeDef",
    "ListRecordingConfigurationsResponseTypeDef",
    "ListStreamKeysRequestRequestTypeDef",
    "ListStreamKeysResponseTypeDef",
    "ListStreamSessionsRequestRequestTypeDef",
    "ListStreamSessionsResponseTypeDef",
    "ListStreamsRequestRequestTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "PutMetadataRequestRequestTypeDef",
    "RecordingConfigurationSummaryTypeDef",
    "RecordingConfigurationTypeDef",
    "ResponseMetadataTypeDef",
    "S3DestinationConfigurationTypeDef",
    "StopStreamRequestRequestTypeDef",
    "StreamEventTypeDef",
    "StreamFiltersTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSessionSummaryTypeDef",
    "StreamSessionTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagResourceRequestRequestTypeDef",
    "ThumbnailConfigurationTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "VideoConfigurationTypeDef",
)

AudioConfigurationTypeDef = TypedDict(
    "AudioConfigurationTypeDef",
    {
        "channels": NotRequired[int],
        "codec": NotRequired[str],
        "sampleRate": NotRequired[int],
        "targetBitrate": NotRequired[int],
    },
)

BatchErrorTypeDef = TypedDict(
    "BatchErrorTypeDef",
    {
        "arn": NotRequired[str],
        "code": NotRequired[str],
        "message": NotRequired[str],
    },
)

BatchGetChannelRequestRequestTypeDef = TypedDict(
    "BatchGetChannelRequestRequestTypeDef",
    {
        "arns": Sequence[str],
    },
)

BatchGetChannelResponseTypeDef = TypedDict(
    "BatchGetChannelResponseTypeDef",
    {
        "channels": List["ChannelTypeDef"],
        "errors": List["BatchErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchGetStreamKeyRequestRequestTypeDef = TypedDict(
    "BatchGetStreamKeyRequestRequestTypeDef",
    {
        "arns": Sequence[str],
    },
)

BatchGetStreamKeyResponseTypeDef = TypedDict(
    "BatchGetStreamKeyResponseTypeDef",
    {
        "errors": List["BatchErrorTypeDef"],
        "streamKeys": List["StreamKeyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "authorized": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "name": NotRequired[str],
        "recordingConfigurationArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": NotRequired[str],
        "authorized": NotRequired[bool],
        "ingestEndpoint": NotRequired[str],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "name": NotRequired[str],
        "playbackUrl": NotRequired[str],
        "recordingConfigurationArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "type": NotRequired[ChannelTypeType],
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "authorized": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "name": NotRequired[str],
        "recordingConfigurationArn": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "type": NotRequired[ChannelTypeType],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "CreateRecordingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "thumbnailConfiguration": NotRequired["ThumbnailConfigurationTypeDef"],
    },
)

CreateRecordingConfigurationResponseTypeDef = TypedDict(
    "CreateRecordingConfigurationResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateStreamKeyRequestRequestTypeDef = TypedDict(
    "CreateStreamKeyRequestRequestTypeDef",
    {
        "channelArn": str,
        "tags": NotRequired[Mapping[str, str]],
    },
)

CreateStreamKeyResponseTypeDef = TypedDict(
    "CreateStreamKeyResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeletePlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "DeletePlaybackKeyPairRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteRecordingConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DeleteStreamKeyRequestRequestTypeDef = TypedDict(
    "DeleteStreamKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "s3": NotRequired["S3DestinationConfigurationTypeDef"],
    },
)

GetChannelRequestRequestTypeDef = TypedDict(
    "GetChannelRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetChannelResponseTypeDef = TypedDict(
    "GetChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "GetPlaybackKeyPairRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetPlaybackKeyPairResponseTypeDef = TypedDict(
    "GetPlaybackKeyPairResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRecordingConfigurationRequestRequestTypeDef = TypedDict(
    "GetRecordingConfigurationRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetRecordingConfigurationResponseTypeDef = TypedDict(
    "GetRecordingConfigurationResponseTypeDef",
    {
        "recordingConfiguration": "RecordingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamKeyRequestRequestTypeDef = TypedDict(
    "GetStreamKeyRequestRequestTypeDef",
    {
        "arn": str,
    },
)

GetStreamKeyResponseTypeDef = TypedDict(
    "GetStreamKeyResponseTypeDef",
    {
        "streamKey": "StreamKeyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamRequestRequestTypeDef = TypedDict(
    "GetStreamRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)

GetStreamResponseTypeDef = TypedDict(
    "GetStreamResponseTypeDef",
    {
        "stream": "StreamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetStreamSessionRequestRequestTypeDef = TypedDict(
    "GetStreamSessionRequestRequestTypeDef",
    {
        "channelArn": str,
        "streamId": NotRequired[str],
    },
)

GetStreamSessionResponseTypeDef = TypedDict(
    "GetStreamSessionResponseTypeDef",
    {
        "streamSession": "StreamSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportPlaybackKeyPairRequestRequestTypeDef = TypedDict(
    "ImportPlaybackKeyPairRequestRequestTypeDef",
    {
        "publicKeyMaterial": str,
        "name": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)

ImportPlaybackKeyPairResponseTypeDef = TypedDict(
    "ImportPlaybackKeyPairResponseTypeDef",
    {
        "keyPair": "PlaybackKeyPairTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IngestConfigurationTypeDef = TypedDict(
    "IngestConfigurationTypeDef",
    {
        "audio": NotRequired["AudioConfigurationTypeDef"],
        "video": NotRequired["VideoConfigurationTypeDef"],
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "filterByName": NotRequired[str],
        "filterByRecordingConfigurationArn": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "channels": List["ChannelSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPlaybackKeyPairsRequestRequestTypeDef = TypedDict(
    "ListPlaybackKeyPairsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPlaybackKeyPairsResponseTypeDef = TypedDict(
    "ListPlaybackKeyPairsResponseTypeDef",
    {
        "keyPairs": List["PlaybackKeyPairSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRecordingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListRecordingConfigurationsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListRecordingConfigurationsResponseTypeDef = TypedDict(
    "ListRecordingConfigurationsResponseTypeDef",
    {
        "nextToken": str,
        "recordingConfigurations": List["RecordingConfigurationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamKeysRequestRequestTypeDef = TypedDict(
    "ListStreamKeysRequestRequestTypeDef",
    {
        "channelArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListStreamKeysResponseTypeDef = TypedDict(
    "ListStreamKeysResponseTypeDef",
    {
        "nextToken": str,
        "streamKeys": List["StreamKeySummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamSessionsRequestRequestTypeDef = TypedDict(
    "ListStreamSessionsRequestRequestTypeDef",
    {
        "channelArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListStreamSessionsResponseTypeDef = TypedDict(
    "ListStreamSessionsResponseTypeDef",
    {
        "nextToken": str,
        "streamSessions": List["StreamSessionSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListStreamsRequestRequestTypeDef = TypedDict(
    "ListStreamsRequestRequestTypeDef",
    {
        "filterBy": NotRequired["StreamFiltersTypeDef"],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListStreamsResponseTypeDef = TypedDict(
    "ListStreamsResponseTypeDef",
    {
        "nextToken": str,
        "streams": List["StreamSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
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

PlaybackKeyPairSummaryTypeDef = TypedDict(
    "PlaybackKeyPairSummaryTypeDef",
    {
        "arn": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

PlaybackKeyPairTypeDef = TypedDict(
    "PlaybackKeyPairTypeDef",
    {
        "arn": NotRequired[str],
        "fingerprint": NotRequired[str],
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

PutMetadataRequestRequestTypeDef = TypedDict(
    "PutMetadataRequestRequestTypeDef",
    {
        "channelArn": str,
        "metadata": str,
    },
)

RecordingConfigurationSummaryTypeDef = TypedDict(
    "RecordingConfigurationSummaryTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

RecordingConfigurationTypeDef = TypedDict(
    "RecordingConfigurationTypeDef",
    {
        "arn": str,
        "destinationConfiguration": "DestinationConfigurationTypeDef",
        "state": RecordingConfigurationStateType,
        "name": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "thumbnailConfiguration": NotRequired["ThumbnailConfigurationTypeDef"],
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

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
)

StopStreamRequestRequestTypeDef = TypedDict(
    "StopStreamRequestRequestTypeDef",
    {
        "channelArn": str,
    },
)

StreamEventTypeDef = TypedDict(
    "StreamEventTypeDef",
    {
        "eventTime": NotRequired[datetime],
        "name": NotRequired[str],
        "type": NotRequired[str],
    },
)

StreamFiltersTypeDef = TypedDict(
    "StreamFiltersTypeDef",
    {
        "health": NotRequired[StreamHealthType],
    },
)

StreamKeySummaryTypeDef = TypedDict(
    "StreamKeySummaryTypeDef",
    {
        "arn": NotRequired[str],
        "channelArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)

StreamKeyTypeDef = TypedDict(
    "StreamKeyTypeDef",
    {
        "arn": NotRequired[str],
        "channelArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "value": NotRequired[str],
    },
)

StreamSessionSummaryTypeDef = TypedDict(
    "StreamSessionSummaryTypeDef",
    {
        "endTime": NotRequired[datetime],
        "hasErrorEvent": NotRequired[bool],
        "startTime": NotRequired[datetime],
        "streamId": NotRequired[str],
    },
)

StreamSessionTypeDef = TypedDict(
    "StreamSessionTypeDef",
    {
        "channel": NotRequired["ChannelTypeDef"],
        "endTime": NotRequired[datetime],
        "ingestConfiguration": NotRequired["IngestConfigurationTypeDef"],
        "recordingConfiguration": NotRequired["RecordingConfigurationTypeDef"],
        "startTime": NotRequired[datetime],
        "streamId": NotRequired[str],
        "truncatedEvents": NotRequired[List["StreamEventTypeDef"]],
    },
)

StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "channelArn": NotRequired[str],
        "health": NotRequired[StreamHealthType],
        "startTime": NotRequired[datetime],
        "state": NotRequired[StreamStateType],
        "streamId": NotRequired[str],
        "viewerCount": NotRequired[int],
    },
)

StreamTypeDef = TypedDict(
    "StreamTypeDef",
    {
        "channelArn": NotRequired[str],
        "health": NotRequired[StreamHealthType],
        "playbackUrl": NotRequired[str],
        "startTime": NotRequired[datetime],
        "state": NotRequired[StreamStateType],
        "streamId": NotRequired[str],
        "viewerCount": NotRequired[int],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

ThumbnailConfigurationTypeDef = TypedDict(
    "ThumbnailConfigurationTypeDef",
    {
        "recordingMode": NotRequired[RecordingModeType],
        "targetIntervalSeconds": NotRequired[int],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "arn": str,
        "authorized": NotRequired[bool],
        "latencyMode": NotRequired[ChannelLatencyModeType],
        "name": NotRequired[str],
        "recordingConfigurationArn": NotRequired[str],
        "type": NotRequired[ChannelTypeType],
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "channel": "ChannelTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoConfigurationTypeDef = TypedDict(
    "VideoConfigurationTypeDef",
    {
        "avcLevel": NotRequired[str],
        "avcProfile": NotRequired[str],
        "codec": NotRequired[str],
        "encoder": NotRequired[str],
        "targetBitrate": NotRequired[int],
        "targetFramerate": NotRequired[int],
        "videoHeight": NotRequired[int],
        "videoWidth": NotRequired[int],
    },
)
