"""
Type annotations for elastictranscoder service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_elastictranscoder/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_elastictranscoder.type_defs import ArtworkTypeDef

    data: ArtworkTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtworkTypeDef",
    "AudioCodecOptionsTypeDef",
    "AudioParametersTypeDef",
    "CancelJobRequestRequestTypeDef",
    "CaptionFormatTypeDef",
    "CaptionSourceTypeDef",
    "CaptionsTypeDef",
    "ClipTypeDef",
    "CreateJobOutputTypeDef",
    "CreateJobPlaylistTypeDef",
    "CreateJobRequestRequestTypeDef",
    "CreateJobResponseTypeDef",
    "CreatePipelineRequestRequestTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresetRequestRequestTypeDef",
    "CreatePresetResponseTypeDef",
    "DeletePipelineRequestRequestTypeDef",
    "DeletePresetRequestRequestTypeDef",
    "DetectedPropertiesTypeDef",
    "EncryptionTypeDef",
    "HlsContentProtectionTypeDef",
    "InputCaptionsTypeDef",
    "JobAlbumArtTypeDef",
    "JobInputTypeDef",
    "JobOutputTypeDef",
    "JobTypeDef",
    "JobWatermarkTypeDef",
    "ListJobsByPipelineRequestRequestTypeDef",
    "ListJobsByPipelineResponseTypeDef",
    "ListJobsByStatusRequestRequestTypeDef",
    "ListJobsByStatusResponseTypeDef",
    "ListPipelinesRequestRequestTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListPresetsRequestRequestTypeDef",
    "ListPresetsResponseTypeDef",
    "NotificationsTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PipelineOutputConfigTypeDef",
    "PipelineTypeDef",
    "PlayReadyDrmTypeDef",
    "PlaylistTypeDef",
    "PresetTypeDef",
    "PresetWatermarkTypeDef",
    "ReadJobRequestRequestTypeDef",
    "ReadJobResponseTypeDef",
    "ReadPipelineRequestRequestTypeDef",
    "ReadPipelineResponseTypeDef",
    "ReadPresetRequestRequestTypeDef",
    "ReadPresetResponseTypeDef",
    "ResponseMetadataTypeDef",
    "TestRoleRequestRequestTypeDef",
    "TestRoleResponseTypeDef",
    "ThumbnailsTypeDef",
    "TimeSpanTypeDef",
    "TimingTypeDef",
    "UpdatePipelineNotificationsRequestRequestTypeDef",
    "UpdatePipelineNotificationsResponseTypeDef",
    "UpdatePipelineRequestRequestTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdatePipelineStatusRequestRequestTypeDef",
    "UpdatePipelineStatusResponseTypeDef",
    "VideoParametersTypeDef",
    "WaiterConfigTypeDef",
    "WarningTypeDef",
)

ArtworkTypeDef = TypedDict(
    "ArtworkTypeDef",
    {
        "InputKey": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
        "AlbumArtFormat": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
    },
)

AudioCodecOptionsTypeDef = TypedDict(
    "AudioCodecOptionsTypeDef",
    {
        "Profile": NotRequired[str],
        "BitDepth": NotRequired[str],
        "BitOrder": NotRequired[str],
        "Signed": NotRequired[str],
    },
)

AudioParametersTypeDef = TypedDict(
    "AudioParametersTypeDef",
    {
        "Codec": NotRequired[str],
        "SampleRate": NotRequired[str],
        "BitRate": NotRequired[str],
        "Channels": NotRequired[str],
        "AudioPackingMode": NotRequired[str],
        "CodecOptions": NotRequired["AudioCodecOptionsTypeDef"],
    },
)

CancelJobRequestRequestTypeDef = TypedDict(
    "CancelJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)

CaptionFormatTypeDef = TypedDict(
    "CaptionFormatTypeDef",
    {
        "Format": NotRequired[str],
        "Pattern": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
    },
)

CaptionSourceTypeDef = TypedDict(
    "CaptionSourceTypeDef",
    {
        "Key": NotRequired[str],
        "Language": NotRequired[str],
        "TimeOffset": NotRequired[str],
        "Label": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
    },
)

CaptionsTypeDef = TypedDict(
    "CaptionsTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[Sequence["CaptionSourceTypeDef"]],
        "CaptionFormats": NotRequired[Sequence["CaptionFormatTypeDef"]],
    },
)

ClipTypeDef = TypedDict(
    "ClipTypeDef",
    {
        "TimeSpan": NotRequired["TimeSpanTypeDef"],
    },
)

CreateJobOutputTypeDef = TypedDict(
    "CreateJobOutputTypeDef",
    {
        "Key": NotRequired[str],
        "ThumbnailPattern": NotRequired[str],
        "ThumbnailEncryption": NotRequired["EncryptionTypeDef"],
        "Rotate": NotRequired[str],
        "PresetId": NotRequired[str],
        "SegmentDuration": NotRequired[str],
        "Watermarks": NotRequired[Sequence["JobWatermarkTypeDef"]],
        "AlbumArt": NotRequired["JobAlbumArtTypeDef"],
        "Composition": NotRequired[Sequence["ClipTypeDef"]],
        "Captions": NotRequired["CaptionsTypeDef"],
        "Encryption": NotRequired["EncryptionTypeDef"],
    },
)

CreateJobPlaylistTypeDef = TypedDict(
    "CreateJobPlaylistTypeDef",
    {
        "Name": NotRequired[str],
        "Format": NotRequired[str],
        "OutputKeys": NotRequired[Sequence[str]],
        "HlsContentProtection": NotRequired["HlsContentProtectionTypeDef"],
        "PlayReadyDrm": NotRequired["PlayReadyDrmTypeDef"],
    },
)

CreateJobRequestRequestTypeDef = TypedDict(
    "CreateJobRequestRequestTypeDef",
    {
        "PipelineId": str,
        "Input": NotRequired["JobInputTypeDef"],
        "Inputs": NotRequired[Sequence["JobInputTypeDef"]],
        "Output": NotRequired["CreateJobOutputTypeDef"],
        "Outputs": NotRequired[Sequence["CreateJobOutputTypeDef"]],
        "OutputKeyPrefix": NotRequired[str],
        "Playlists": NotRequired[Sequence["CreateJobPlaylistTypeDef"]],
        "UserMetadata": NotRequired[Mapping[str, str]],
    },
)

CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePipelineRequestRequestTypeDef = TypedDict(
    "CreatePipelineRequestRequestTypeDef",
    {
        "Name": str,
        "InputBucket": str,
        "Role": str,
        "OutputBucket": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired["NotificationsTypeDef"],
        "ContentConfig": NotRequired["PipelineOutputConfigTypeDef"],
        "ThumbnailConfig": NotRequired["PipelineOutputConfigTypeDef"],
    },
)

CreatePipelineResponseTypeDef = TypedDict(
    "CreatePipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePresetRequestRequestTypeDef = TypedDict(
    "CreatePresetRequestRequestTypeDef",
    {
        "Name": str,
        "Container": str,
        "Description": NotRequired[str],
        "Video": NotRequired["VideoParametersTypeDef"],
        "Audio": NotRequired["AudioParametersTypeDef"],
        "Thumbnails": NotRequired["ThumbnailsTypeDef"],
    },
)

CreatePresetResponseTypeDef = TypedDict(
    "CreatePresetResponseTypeDef",
    {
        "Preset": "PresetTypeDef",
        "Warning": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePipelineRequestRequestTypeDef = TypedDict(
    "DeletePipelineRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePresetRequestRequestTypeDef = TypedDict(
    "DeletePresetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DetectedPropertiesTypeDef = TypedDict(
    "DetectedPropertiesTypeDef",
    {
        "Width": NotRequired[int],
        "Height": NotRequired[int],
        "FrameRate": NotRequired[str],
        "FileSize": NotRequired[int],
        "DurationMillis": NotRequired[int],
    },
)

EncryptionTypeDef = TypedDict(
    "EncryptionTypeDef",
    {
        "Mode": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "InitializationVector": NotRequired[str],
    },
)

HlsContentProtectionTypeDef = TypedDict(
    "HlsContentProtectionTypeDef",
    {
        "Method": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "InitializationVector": NotRequired[str],
        "LicenseAcquisitionUrl": NotRequired[str],
        "KeyStoragePolicy": NotRequired[str],
    },
)

InputCaptionsTypeDef = TypedDict(
    "InputCaptionsTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "CaptionSources": NotRequired[Sequence["CaptionSourceTypeDef"]],
    },
)

JobAlbumArtTypeDef = TypedDict(
    "JobAlbumArtTypeDef",
    {
        "MergePolicy": NotRequired[str],
        "Artwork": NotRequired[Sequence["ArtworkTypeDef"]],
    },
)

JobInputTypeDef = TypedDict(
    "JobInputTypeDef",
    {
        "Key": NotRequired[str],
        "FrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "Interlaced": NotRequired[str],
        "Container": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "TimeSpan": NotRequired["TimeSpanTypeDef"],
        "InputCaptions": NotRequired["InputCaptionsTypeDef"],
        "DetectedProperties": NotRequired["DetectedPropertiesTypeDef"],
    },
)

JobOutputTypeDef = TypedDict(
    "JobOutputTypeDef",
    {
        "Id": NotRequired[str],
        "Key": NotRequired[str],
        "ThumbnailPattern": NotRequired[str],
        "ThumbnailEncryption": NotRequired["EncryptionTypeDef"],
        "Rotate": NotRequired[str],
        "PresetId": NotRequired[str],
        "SegmentDuration": NotRequired[str],
        "Status": NotRequired[str],
        "StatusDetail": NotRequired[str],
        "Duration": NotRequired[int],
        "Width": NotRequired[int],
        "Height": NotRequired[int],
        "FrameRate": NotRequired[str],
        "FileSize": NotRequired[int],
        "DurationMillis": NotRequired[int],
        "Watermarks": NotRequired[List["JobWatermarkTypeDef"]],
        "AlbumArt": NotRequired["JobAlbumArtTypeDef"],
        "Composition": NotRequired[List["ClipTypeDef"]],
        "Captions": NotRequired["CaptionsTypeDef"],
        "Encryption": NotRequired["EncryptionTypeDef"],
        "AppliedColorSpaceConversion": NotRequired[str],
    },
)

JobTypeDef = TypedDict(
    "JobTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "PipelineId": NotRequired[str],
        "Input": NotRequired["JobInputTypeDef"],
        "Inputs": NotRequired[List["JobInputTypeDef"]],
        "Output": NotRequired["JobOutputTypeDef"],
        "Outputs": NotRequired[List["JobOutputTypeDef"]],
        "OutputKeyPrefix": NotRequired[str],
        "Playlists": NotRequired[List["PlaylistTypeDef"]],
        "Status": NotRequired[str],
        "UserMetadata": NotRequired[Dict[str, str]],
        "Timing": NotRequired["TimingTypeDef"],
    },
)

JobWatermarkTypeDef = TypedDict(
    "JobWatermarkTypeDef",
    {
        "PresetWatermarkId": NotRequired[str],
        "InputKey": NotRequired[str],
        "Encryption": NotRequired["EncryptionTypeDef"],
    },
)

ListJobsByPipelineRequestRequestTypeDef = TypedDict(
    "ListJobsByPipelineRequestRequestTypeDef",
    {
        "PipelineId": str,
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)

ListJobsByPipelineResponseTypeDef = TypedDict(
    "ListJobsByPipelineResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListJobsByStatusRequestRequestTypeDef = TypedDict(
    "ListJobsByStatusRequestRequestTypeDef",
    {
        "Status": str,
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)

ListJobsByStatusResponseTypeDef = TypedDict(
    "ListJobsByStatusResponseTypeDef",
    {
        "Jobs": List["JobTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPipelinesRequestRequestTypeDef = TypedDict(
    "ListPipelinesRequestRequestTypeDef",
    {
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)

ListPipelinesResponseTypeDef = TypedDict(
    "ListPipelinesResponseTypeDef",
    {
        "Pipelines": List["PipelineTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPresetsRequestRequestTypeDef = TypedDict(
    "ListPresetsRequestRequestTypeDef",
    {
        "Ascending": NotRequired[str],
        "PageToken": NotRequired[str],
    },
)

ListPresetsResponseTypeDef = TypedDict(
    "ListPresetsResponseTypeDef",
    {
        "Presets": List["PresetTypeDef"],
        "NextPageToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NotificationsTypeDef = TypedDict(
    "NotificationsTypeDef",
    {
        "Progressing": NotRequired[str],
        "Completed": NotRequired[str],
        "Warning": NotRequired[str],
        "Error": NotRequired[str],
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

PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "GranteeType": NotRequired[str],
        "Grantee": NotRequired[str],
        "Access": NotRequired[Sequence[str]],
    },
)

PipelineOutputConfigTypeDef = TypedDict(
    "PipelineOutputConfigTypeDef",
    {
        "Bucket": NotRequired[str],
        "StorageClass": NotRequired[str],
        "Permissions": NotRequired[Sequence["PermissionTypeDef"]],
    },
)

PipelineTypeDef = TypedDict(
    "PipelineTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Status": NotRequired[str],
        "InputBucket": NotRequired[str],
        "OutputBucket": NotRequired[str],
        "Role": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired["NotificationsTypeDef"],
        "ContentConfig": NotRequired["PipelineOutputConfigTypeDef"],
        "ThumbnailConfig": NotRequired["PipelineOutputConfigTypeDef"],
    },
)

PlayReadyDrmTypeDef = TypedDict(
    "PlayReadyDrmTypeDef",
    {
        "Format": NotRequired[str],
        "Key": NotRequired[str],
        "KeyMd5": NotRequired[str],
        "KeyId": NotRequired[str],
        "InitializationVector": NotRequired[str],
        "LicenseAcquisitionUrl": NotRequired[str],
    },
)

PlaylistTypeDef = TypedDict(
    "PlaylistTypeDef",
    {
        "Name": NotRequired[str],
        "Format": NotRequired[str],
        "OutputKeys": NotRequired[List[str]],
        "HlsContentProtection": NotRequired["HlsContentProtectionTypeDef"],
        "PlayReadyDrm": NotRequired["PlayReadyDrmTypeDef"],
        "Status": NotRequired[str],
        "StatusDetail": NotRequired[str],
    },
)

PresetTypeDef = TypedDict(
    "PresetTypeDef",
    {
        "Id": NotRequired[str],
        "Arn": NotRequired[str],
        "Name": NotRequired[str],
        "Description": NotRequired[str],
        "Container": NotRequired[str],
        "Audio": NotRequired["AudioParametersTypeDef"],
        "Video": NotRequired["VideoParametersTypeDef"],
        "Thumbnails": NotRequired["ThumbnailsTypeDef"],
        "Type": NotRequired[str],
    },
)

PresetWatermarkTypeDef = TypedDict(
    "PresetWatermarkTypeDef",
    {
        "Id": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "HorizontalAlign": NotRequired[str],
        "HorizontalOffset": NotRequired[str],
        "VerticalAlign": NotRequired[str],
        "VerticalOffset": NotRequired[str],
        "Opacity": NotRequired[str],
        "Target": NotRequired[str],
    },
)

ReadJobRequestRequestTypeDef = TypedDict(
    "ReadJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)

ReadJobResponseTypeDef = TypedDict(
    "ReadJobResponseTypeDef",
    {
        "Job": "JobTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReadPipelineRequestRequestTypeDef = TypedDict(
    "ReadPipelineRequestRequestTypeDef",
    {
        "Id": str,
    },
)

ReadPipelineResponseTypeDef = TypedDict(
    "ReadPipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReadPresetRequestRequestTypeDef = TypedDict(
    "ReadPresetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

ReadPresetResponseTypeDef = TypedDict(
    "ReadPresetResponseTypeDef",
    {
        "Preset": "PresetTypeDef",
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

TestRoleRequestRequestTypeDef = TypedDict(
    "TestRoleRequestRequestTypeDef",
    {
        "Role": str,
        "InputBucket": str,
        "OutputBucket": str,
        "Topics": Sequence[str],
    },
)

TestRoleResponseTypeDef = TypedDict(
    "TestRoleResponseTypeDef",
    {
        "Success": str,
        "Messages": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThumbnailsTypeDef = TypedDict(
    "ThumbnailsTypeDef",
    {
        "Format": NotRequired[str],
        "Interval": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
    },
)

TimeSpanTypeDef = TypedDict(
    "TimeSpanTypeDef",
    {
        "StartTime": NotRequired[str],
        "Duration": NotRequired[str],
    },
)

TimingTypeDef = TypedDict(
    "TimingTypeDef",
    {
        "SubmitTimeMillis": NotRequired[int],
        "StartTimeMillis": NotRequired[int],
        "FinishTimeMillis": NotRequired[int],
    },
)

UpdatePipelineNotificationsRequestRequestTypeDef = TypedDict(
    "UpdatePipelineNotificationsRequestRequestTypeDef",
    {
        "Id": str,
        "Notifications": "NotificationsTypeDef",
    },
)

UpdatePipelineNotificationsResponseTypeDef = TypedDict(
    "UpdatePipelineNotificationsResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePipelineRequestRequestTypeDef = TypedDict(
    "UpdatePipelineRequestRequestTypeDef",
    {
        "Id": str,
        "Name": NotRequired[str],
        "InputBucket": NotRequired[str],
        "Role": NotRequired[str],
        "AwsKmsKeyArn": NotRequired[str],
        "Notifications": NotRequired["NotificationsTypeDef"],
        "ContentConfig": NotRequired["PipelineOutputConfigTypeDef"],
        "ThumbnailConfig": NotRequired["PipelineOutputConfigTypeDef"],
    },
)

UpdatePipelineResponseTypeDef = TypedDict(
    "UpdatePipelineResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "Warnings": List["WarningTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePipelineStatusRequestRequestTypeDef = TypedDict(
    "UpdatePipelineStatusRequestRequestTypeDef",
    {
        "Id": str,
        "Status": str,
    },
)

UpdatePipelineStatusResponseTypeDef = TypedDict(
    "UpdatePipelineStatusResponseTypeDef",
    {
        "Pipeline": "PipelineTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VideoParametersTypeDef = TypedDict(
    "VideoParametersTypeDef",
    {
        "Codec": NotRequired[str],
        "CodecOptions": NotRequired[Mapping[str, str]],
        "KeyframesMaxDist": NotRequired[str],
        "FixedGOP": NotRequired[str],
        "BitRate": NotRequired[str],
        "FrameRate": NotRequired[str],
        "MaxFrameRate": NotRequired[str],
        "Resolution": NotRequired[str],
        "AspectRatio": NotRequired[str],
        "MaxWidth": NotRequired[str],
        "MaxHeight": NotRequired[str],
        "DisplayAspectRatio": NotRequired[str],
        "SizingPolicy": NotRequired[str],
        "PaddingPolicy": NotRequired[str],
        "Watermarks": NotRequired[Sequence["PresetWatermarkTypeDef"]],
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)

WarningTypeDef = TypedDict(
    "WarningTypeDef",
    {
        "Code": NotRequired[str],
        "Message": NotRequired[str],
    },
)
