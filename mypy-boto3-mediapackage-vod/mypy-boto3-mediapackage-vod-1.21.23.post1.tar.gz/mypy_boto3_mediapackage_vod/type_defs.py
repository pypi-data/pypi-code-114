"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import (
    AdMarkersType,
    EncryptionMethodType,
    ManifestLayoutType,
    ProfileType,
    SegmentTemplateFormatType,
    StreamOrderType,
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
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsRequestRequestTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateAssetRequestRequestTypeDef",
    "CreateAssetResponseTypeDef",
    "CreatePackagingConfigurationRequestRequestTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "CreatePackagingGroupRequestRequestTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "DeleteAssetRequestRequestTypeDef",
    "DeletePackagingConfigurationRequestRequestTypeDef",
    "DeletePackagingGroupRequestRequestTypeDef",
    "DescribeAssetRequestRequestTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribePackagingConfigurationRequestRequestTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "DescribePackagingGroupRequestRequestTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "ListAssetsRequestRequestTypeDef",
    "ListAssetsResponseTypeDef",
    "ListPackagingConfigurationsRequestRequestTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "ListPackagingGroupsRequestRequestTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadataTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackagingGroupRequestRequestTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": NotRequired[str],
        "CreatedAt": NotRequired[str],
        "Id": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
        "ResourceId": NotRequired[str],
        "SourceArn": NotRequired[str],
        "SourceRoleArn": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef",
    {
        "CdnIdentifierSecret": str,
        "SecretsRoleArn": str,
    },
)

CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "ConstantInitializationVector": NotRequired[str],
    },
)

CmafPackageTypeDef = TypedDict(
    "CmafPackageTypeDef",
    {
        "HlsManifests": Sequence["HlsManifestTypeDef"],
        "Encryption": NotRequired["CmafEncryptionTypeDef"],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
    },
)

ConfigureLogsRequestRequestTypeDef = TypedDict(
    "ConfigureLogsRequestRequestTypeDef",
    {
        "Id": str,
        "EgressAccessLogs": NotRequired["EgressAccessLogsTypeDef"],
    },
)

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateAssetRequestRequestTypeDef = TypedDict(
    "CreateAssetRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "ResourceId": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "CreatePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
        "PackagingGroupId": str,
        "CmafPackage": NotRequired["CmafPackageTypeDef"],
        "DashPackage": NotRequired["DashPackageTypeDef"],
        "HlsPackage": NotRequired["HlsPackageTypeDef"],
        "MssPackage": NotRequired["MssPackageTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePackagingConfigurationResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePackagingGroupRequestRequestTypeDef = TypedDict(
    "CreatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired["AuthorizationTypeDef"],
        "EgressAccessLogs": NotRequired["EgressAccessLogsTypeDef"],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreatePackagingGroupResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
)

DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": NotRequired[ManifestLayoutType],
        "ManifestName": NotRequired[str],
        "MinBufferTimeSeconds": NotRequired[int],
        "Profile": NotRequired[ProfileType],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

DashPackageTypeDef = TypedDict(
    "DashPackageTypeDef",
    {
        "DashManifests": Sequence["DashManifestTypeDef"],
        "Encryption": NotRequired["DashEncryptionTypeDef"],
        "IncludeEncoderConfigurationInSegments": NotRequired[bool],
        "PeriodTriggers": NotRequired[Sequence[Literal["ADS"]]],
        "SegmentDurationSeconds": NotRequired[int],
        "SegmentTemplateFormat": NotRequired[SegmentTemplateFormatType],
    },
)

DeleteAssetRequestRequestTypeDef = TypedDict(
    "DeleteAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DeletePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DeletePackagingGroupRequestRequestTypeDef = TypedDict(
    "DeletePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetRequestRequestTypeDef = TypedDict(
    "DescribeAssetRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingConfigurationRequestRequestTypeDef = TypedDict(
    "DescribePackagingConfigurationRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingConfigurationResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackagingGroupRequestRequestTypeDef = TypedDict(
    "DescribePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
    },
)

DescribePackagingGroupResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EgressAccessLogsTypeDef = TypedDict(
    "EgressAccessLogsTypeDef",
    {
        "LogGroupName": NotRequired[str],
    },
)

EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef",
    {
        "PackagingConfigurationId": NotRequired[str],
        "Status": NotRequired[str],
        "Url": NotRequired[str],
    },
)

HlsEncryptionTypeDef = TypedDict(
    "HlsEncryptionTypeDef",
    {
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "ConstantInitializationVector": NotRequired[str],
        "EncryptionMethod": NotRequired[EncryptionMethodType],
    },
)

HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": NotRequired[AdMarkersType],
        "IncludeIframeOnlyStream": NotRequired[bool],
        "ManifestName": NotRequired[str],
        "ProgramDateTimeIntervalSeconds": NotRequired[int],
        "RepeatExtXKey": NotRequired[bool],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

HlsPackageTypeDef = TypedDict(
    "HlsPackageTypeDef",
    {
        "HlsManifests": Sequence["HlsManifestTypeDef"],
        "Encryption": NotRequired["HlsEncryptionTypeDef"],
        "IncludeDvbSubtitles": NotRequired[bool],
        "SegmentDurationSeconds": NotRequired[int],
        "UseAudioRenditionGroup": NotRequired[bool],
    },
)

ListAssetsRequestRequestTypeDef = TypedDict(
    "ListAssetsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {
        "Assets": List["AssetShallowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListPackagingConfigurationsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "PackagingGroupId": NotRequired[str],
    },
)

ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingConfigurations": List["PackagingConfigurationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagingGroupsRequestRequestTypeDef = TypedDict(
    "ListPackagingGroupsRequestRequestTypeDef",
    {
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {
        "NextToken": str,
        "PackagingGroups": List["PackagingGroupTypeDef"],
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

MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {
        "ManifestName": NotRequired[str],
        "StreamSelection": NotRequired["StreamSelectionTypeDef"],
    },
)

MssPackageTypeDef = TypedDict(
    "MssPackageTypeDef",
    {
        "MssManifests": Sequence["MssManifestTypeDef"],
        "Encryption": NotRequired["MssEncryptionTypeDef"],
        "SegmentDurationSeconds": NotRequired[int],
    },
)

PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": NotRequired[str],
        "CmafPackage": NotRequired["CmafPackageTypeDef"],
        "DashPackage": NotRequired["DashPackageTypeDef"],
        "HlsPackage": NotRequired["HlsPackageTypeDef"],
        "Id": NotRequired[str],
        "MssPackage": NotRequired["MssPackageTypeDef"],
        "PackagingGroupId": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)

PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "Arn": NotRequired[str],
        "Authorization": NotRequired["AuthorizationTypeDef"],
        "DomainName": NotRequired[str],
        "EgressAccessLogs": NotRequired["EgressAccessLogsTypeDef"],
        "Id": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
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

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {
        "RoleArn": str,
        "SystemIds": Sequence[str],
        "Url": str,
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

UpdatePackagingGroupRequestRequestTypeDef = TypedDict(
    "UpdatePackagingGroupRequestRequestTypeDef",
    {
        "Id": str,
        "Authorization": NotRequired["AuthorizationTypeDef"],
    },
)

UpdatePackagingGroupResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
