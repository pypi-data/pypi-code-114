"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_mediapackage/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdMarkersType,
    AdsOnDeliveryRestrictionsType,
    AdTriggersElementType,
    EncryptionMethodType,
    ManifestLayoutType,
    OriginationType,
    PlaylistTypeType,
    ProfileType,
    SegmentTemplateFormatType,
    StatusType,
    StreamOrderType,
    UtcTimingType,
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
    "AuthorizationTypeDef",
    "ChannelTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelRequestRequestTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateHarvestJobRequestRequestTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "CreateOriginEndpointRequestRequestTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "DeleteChannelRequestRequestTypeDef",
    "DeleteOriginEndpointRequestRequestTypeDef",
    "DescribeChannelRequestRequestTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeHarvestJobRequestRequestTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "DescribeOriginEndpointRequestRequestTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "HarvestJobTypeDef",
    "HlsEncryptionTypeDef",
    "HlsIngestTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "IngestEndpointTypeDef",
    "IngressAccessLogsTypeDef",
    "ListChannelsRequestRequestTypeDef",
    "ListChannelsResponseTypeDef",
    "ListHarvestJobsRequestRequestTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "ListOriginEndpointsRequestRequestTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "RotateChannelCredentialsRequestRequestTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "S3DestinationTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateChannelRequestRequestTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointRequestRequestTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": NotRequired[str],
        "Description": NotRequired[str],
        "EgressAccessLogs": NotRequired["EgressAccessLogsTypeDef"],
        "HlsIngest": NotRequired["HlsIngestTypeDef"],
        "Id": NotRequired[str],
        "IngressAccessLogs": NotRequired["IngressAccessLogsTypeDef"],
        "Tags": NotRequired[Dict[str, str]],
    },
)

CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "ConstantInitializationVector": NotRequired[str],
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)

CmafPackageCreateOrUpdateParametersTypeDef = TypedDict(
    "CmafPackageCreateOrUpdateParametersTypeDef",
    {
        "Encryption": NotRequired["CmafEncryptionTypeDef"],
        "HlsManifests": NotRequired[Sequence["HlsManifestCreateOrUpdateParametersTypeDef"]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "Encryption": NotRequired["CmafEncryptionTypeDef"],
        "HlsManifests": NotRequired[List["HlsManifestTypeDef"]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentPrefix": NotRequired[str],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired["EgressAccessLogsTypeDef"],
        "IngressAccessLogs": NotRequired["IngressAccessLogsTypeDef"],
    },
)

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateChannelRequestRequestTypeDef = TypedDict(
    "CreateChannelRequestRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateHarvestJobRequestRequestTypeDef = TypedDict(
    "CreateHarvestJobRequestRequestTypeDef",
    {
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
    },
)

CreateHarvestJobResponseTypeDef = TypedDict(
    "CreateHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateOriginEndpointRequestRequestTypeDef = TypedDict(
    "CreateOriginEndpointRequestRequestTypeDef",
    {
        "ChannelId": str,
        "Id": str,
        "Authorization": NotRequired["AuthorizationTypeDef"],
        "CmafPackage": NotRequired["CmafPackageCreateOrUpdateParametersTypeDef"],
        "DashPackage": NotRequired["DashPackageTypeDef"],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired["HlsPackageTypeDef"],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired["MssPackageTypeDef"],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Mapping[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)

CreateOriginEndpointResponseTypeDef = TypedDict(
    "CreateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "KeyRotationIntervalSeconds": NotRequired[int],
    },
)

DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired["DashEncryptionTypeDef"],
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestWindowSeconds": NotRequired[int],
        "MinBufferTimeSeconds": NotRequired[int],
        "MinUpdatePeriodSeconds": NotRequired[int],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "Profile": NotRequired[ProfileType],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
        "SuggestedPresentationDelaySeconds": NotRequired[int],
        "UtcTiming": NotRequired[UtcTimingType],
        "UtcTimingUri": NotRequired[str],
    },
)

DeleteChannelRequestRequestTypeDef = TypedDict(
    "DeleteChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeleteOriginEndpointRequestRequestTypeDef = TypedDict(
    "DeleteOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeChannelRequestRequestTypeDef = TypedDict(
    "DescribeChannelRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHarvestJobRequestRequestTypeDef = TypedDict(
    "DescribeHarvestJobRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeHarvestJobResponseTypeDef = TypedDict(
    "DescribeHarvestJobResponseTypeDef",
    {
        "Arn": str,
        "ChannelId": str,
        "CreatedAt": str,
        "EndTime": str,
        "Id": str,
        "OriginEndpointId": str,
        "S3Destination": "S3DestinationTypeDef",
        "StartTime": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeOriginEndpointRequestRequestTypeDef = TypedDict(
    "DescribeOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeOriginEndpointResponseTypeDef = TypedDict(
    "DescribeOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)

EncryptionContractConfigurationTypeDef = TypedDict(
    "EncryptionContractConfigurationTypeDef",
    {
        "PresetSpeke20Audio": Literal["PRESET-AUDIO-1"],
        "PresetSpeke20Video": Literal["PRESET-VIDEO-1"],
    },
)

HarvestJobTypeDef = TypedDict(
    "HarvestJobTypeDef",
    {
        "Arn": NotRequired[str],
        "ChannelId": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "EndTime": NotRequired[str],
        "Id": NotRequired[str],
        "OriginEndpointId": NotRequired[str],
        "S3Destination": NotRequired["S3DestinationTypeDef"],
        "StartTime": NotRequired[str],
        "Status": NotRequired[StatusType],
    },
)

HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
        "KeyRotationIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
    },
)

HlsIngestTypeDef = TypedDict(
    "HlsIngestTypeDef",
    {
        "IngestEndpoints": NotRequired[List["IngestEndpointTypeDef"]],
    },
)

HlsManifestCreateOrUpdateParametersTypeDef = TypedDict(
    "HlsManifestCreateOrUpdateParametersTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
    },
)

HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "Id": str,
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "Url": NotRequired[str],
    },
)

HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "AdTriggers": NotRequired[Sequence[AdTriggersElementType]],
        "AdsOnDeliveryRestrictions": NotRequired[AdsOnDeliveryRestrictionsType],
        "Encryption": NotRequired["HlsEncryptionTypeDef"],
        "IncludeDvbSubtitles": NotRequired[bool],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "PlaylistType": NotRequired[PlaylistTypeType],
        "PlaylistWindowSeconds": NotRequired[int],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)

IngestEndpointTypeDef = TypedDict(
    "IngestEndpointTypeDef",
    {
        "Id": NotRequired[str],
        "Password": NotRequired[str],
        "Url": NotRequired[str],
        "Username": NotRequired[str],
    },
)

IngressAccessLogsTypeDef = TypedDict(
    "IngressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)

ListChannelsRequestRequestTypeDef = TypedDict(
    "ListChannelsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {
        "Channels": List["ChannelTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListHarvestJobsRequestRequestTypeDef = TypedDict(
    "ListHarvestJobsRequestRequestTypeDef",
    {
        "IncludeChannelId": NotRequired[str],
        "IncludeStatus": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListHarvestJobsResponseTypeDef = TypedDict(
    "ListHarvestJobsResponseTypeDef",
    {
        "HarvestJobs": List["HarvestJobTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListOriginEndpointsRequestRequestTypeDef = TypedDict(
    "ListOriginEndpointsRequestRequestTypeDef",
    {
        "ChannelId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListOriginEndpointsResponseTypeDef = TypedDict(
    "ListOriginEndpointsResponseTypeDef",
    {
        "NextToken": str,
        "OriginEndpoints": List["OriginEndpointTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "Encryption": NotRequired["MssEncryptionTypeDef"],
        "ManifestWindowSeconds": NotRequired[int],
        "SegmentDurationSeconds": NotRequired[int],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

OriginEndpointTypeDef = TypedDict(
    "OriginEndpointTypeDef",
    {
        "Arn": NotRequired[str],
        "Authorization": NotRequired["AuthorizationTypeDef"],
        "ChannelId": NotRequired[str],
        "CmafPackage": NotRequired["CmafPackageTypeDef"],
        "DashPackage": NotRequired["DashPackageTypeDef"],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired["HlsPackageTypeDef"],
        "Id": NotRequired[str],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired["MssPackageTypeDef"],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "Tags": NotRequired[Dict[str, str]],
        "TimeDelaySeconds": NotRequired[int],
        "Url": NotRequired[str],
        "Whitelist": NotRequired[List[str]],
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

RotateChannelCredentialsRequestRequestTypeDef = TypedDict(
    "RotateChannelCredentialsRequestRequestTypeDef",
    {
        "Id": str,
    },
)

RotateChannelCredentialsResponseTypeDef = TypedDict(
    "RotateChannelCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RotateIngestEndpointCredentialsRequestRequestTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsRequestRequestTypeDef",
    {
        "Id": str,
        "IngestEndpointId": str,
    },
)

RotateIngestEndpointCredentialsResponseTypeDef = TypedDict(
    "RotateIngestEndpointCredentialsResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "BucketName": str,
        "ManifestKey": str,
        "RoleArn": str,
    },
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "ResourceId": str,
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
        "CertificateArn": NotRequired[str],
        "EncryptionContractConfiguration": NotRequired["EncryptionContractConfigurationTypeDef"],
    },
)

StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {
        "MaxVideoBitsPerSecond": NotRequired[int],
        "MinVideoBitsPerSecond": NotRequired[int],
        "StreamOrder": NotRequired[StreamOrderType],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

UpdateChannelRequestRequestTypeDef = TypedDict(
    "UpdateChannelRequestRequestTypeDef",
    {
        "Id": str,
        "Description": NotRequired[str],
    },
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef",
    {
        "Arn": str,
        "Description": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "HlsIngest": "HlsIngestTypeDef",
        "Id": str,
        "IngressAccessLogs": "IngressAccessLogsTypeDef",
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateOriginEndpointRequestRequestTypeDef = TypedDict(
    "UpdateOriginEndpointRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired["AuthorizationTypeDef"],
        "CmafPackage": NotRequired["CmafPackageCreateOrUpdateParametersTypeDef"],
        "DashPackage": NotRequired["DashPackageTypeDef"],
        "Description": NotRequired[str],
        "HlsPackage": NotRequired["HlsPackageTypeDef"],
        "ManifestName": NotRequired[str],
        "MssPackage": NotRequired["MssPackageTypeDef"],
        "Origination": NotRequired[OriginationType],
        "StartoverWindowSeconds": NotRequired[int],
        "TimeDelaySeconds": NotRequired[int],
        "Whitelist": NotRequired[Sequence[str]],
    },
)

UpdateOriginEndpointResponseTypeDef = TypedDict(
    "UpdateOriginEndpointResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "ChannelId": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "Description": str,
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "ManifestName": str,
        "MssPackage": "MssPackageTypeDef",
        "Origination": OriginationType,
        "StartoverWindowSeconds": int,
        "Tags": Dict[str, str],
        "TimeDelaySeconds": int,
        "Url": str,
        "Whitelist": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
