"""
Type annotations for kinesis-video-archived-media service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_kinesis_video_archived_media/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_kinesis_video_archived_media.type_defs import ClipFragmentSelectorTypeDef

    data: ClipFragmentSelectorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ClipFragmentSelectorTypeType,
    ContainerFormatType,
    DASHDisplayFragmentNumberType,
    DASHDisplayFragmentTimestampType,
    DASHFragmentSelectorTypeType,
    DASHPlaybackModeType,
    FragmentSelectorTypeType,
    HLSDiscontinuityModeType,
    HLSDisplayFragmentTimestampType,
    HLSFragmentSelectorTypeType,
    HLSPlaybackModeType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClipFragmentSelectorTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHFragmentSelectorTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "GetClipInputRequestTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetMediaForFragmentListInputRequestTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "HLSFragmentSelectorTypeDef",
    "HLSTimestampRangeTypeDef",
    "ListFragmentsInputRequestTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "TimestampRangeTypeDef",
)

ClipFragmentSelectorTypeDef = TypedDict(
    "ClipFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": ClipFragmentSelectorTypeType,
        "TimestampRange": "ClipTimestampRangeTypeDef",
    },
)

ClipTimestampRangeTypeDef = TypedDict(
    "ClipTimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)

DASHFragmentSelectorTypeDef = TypedDict(
    "DASHFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": NotRequired[DASHFragmentSelectorTypeType],
        "TimestampRange": NotRequired["DASHTimestampRangeTypeDef"],
    },
)

DASHTimestampRangeTypeDef = TypedDict(
    "DASHTimestampRangeTypeDef",
    {
        "StartTimestamp": NotRequired[Union[datetime, str]],
        "EndTimestamp": NotRequired[Union[datetime, str]],
    },
)

FragmentSelectorTypeDef = TypedDict(
    "FragmentSelectorTypeDef",
    {
        "FragmentSelectorType": FragmentSelectorTypeType,
        "TimestampRange": "TimestampRangeTypeDef",
    },
)

FragmentTypeDef = TypedDict(
    "FragmentTypeDef",
    {
        "FragmentNumber": NotRequired[str],
        "FragmentSizeInBytes": NotRequired[int],
        "ProducerTimestamp": NotRequired[datetime],
        "ServerTimestamp": NotRequired[datetime],
        "FragmentLengthInMilliseconds": NotRequired[int],
    },
)

GetClipInputRequestTypeDef = TypedDict(
    "GetClipInputRequestTypeDef",
    {
        "ClipFragmentSelector": "ClipFragmentSelectorTypeDef",
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

GetClipOutputTypeDef = TypedDict(
    "GetClipOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDASHStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetDASHStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PlaybackMode": NotRequired[DASHPlaybackModeType],
        "DisplayFragmentTimestamp": NotRequired[DASHDisplayFragmentTimestampType],
        "DisplayFragmentNumber": NotRequired[DASHDisplayFragmentNumberType],
        "DASHFragmentSelector": NotRequired["DASHFragmentSelectorTypeDef"],
        "Expires": NotRequired[int],
        "MaxManifestFragmentResults": NotRequired[int],
    },
)

GetDASHStreamingSessionURLOutputTypeDef = TypedDict(
    "GetDASHStreamingSessionURLOutputTypeDef",
    {
        "DASHStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHLSStreamingSessionURLInputRequestTypeDef = TypedDict(
    "GetHLSStreamingSessionURLInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PlaybackMode": NotRequired[HLSPlaybackModeType],
        "HLSFragmentSelector": NotRequired["HLSFragmentSelectorTypeDef"],
        "ContainerFormat": NotRequired[ContainerFormatType],
        "DiscontinuityMode": NotRequired[HLSDiscontinuityModeType],
        "DisplayFragmentTimestamp": NotRequired[HLSDisplayFragmentTimestampType],
        "Expires": NotRequired[int],
        "MaxMediaPlaylistFragmentResults": NotRequired[int],
    },
)

GetHLSStreamingSessionURLOutputTypeDef = TypedDict(
    "GetHLSStreamingSessionURLOutputTypeDef",
    {
        "HLSStreamingSessionURL": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetMediaForFragmentListInputRequestTypeDef = TypedDict(
    "GetMediaForFragmentListInputRequestTypeDef",
    {
        "Fragments": Sequence[str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)

GetMediaForFragmentListOutputTypeDef = TypedDict(
    "GetMediaForFragmentListOutputTypeDef",
    {
        "ContentType": str,
        "Payload": StreamingBody,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

HLSFragmentSelectorTypeDef = TypedDict(
    "HLSFragmentSelectorTypeDef",
    {
        "FragmentSelectorType": NotRequired[HLSFragmentSelectorTypeType],
        "TimestampRange": NotRequired["HLSTimestampRangeTypeDef"],
    },
)

HLSTimestampRangeTypeDef = TypedDict(
    "HLSTimestampRangeTypeDef",
    {
        "StartTimestamp": NotRequired[Union[datetime, str]],
        "EndTimestamp": NotRequired[Union[datetime, str]],
    },
)

ListFragmentsInputRequestTypeDef = TypedDict(
    "ListFragmentsInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "FragmentSelector": NotRequired["FragmentSelectorTypeDef"],
    },
)

ListFragmentsOutputTypeDef = TypedDict(
    "ListFragmentsOutputTypeDef",
    {
        "Fragments": List["FragmentTypeDef"],
        "NextToken": str,
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

TimestampRangeTypeDef = TypedDict(
    "TimestampRangeTypeDef",
    {
        "StartTimestamp": Union[datetime, str],
        "EndTimestamp": Union[datetime, str],
    },
)
