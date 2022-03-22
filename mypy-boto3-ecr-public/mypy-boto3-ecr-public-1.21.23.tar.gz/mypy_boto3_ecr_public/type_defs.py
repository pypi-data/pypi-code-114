"""
Type annotations for ecr-public service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecr_public/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecr_public.type_defs import AuthorizationDataTypeDef

    data: AuthorizationDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    ImageFailureCodeType,
    LayerAvailabilityType,
    LayerFailureCodeType,
    RegistryAliasStatusType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AuthorizationDataTypeDef",
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    "BatchCheckLayerAvailabilityResponseTypeDef",
    "BatchDeleteImageRequestRequestTypeDef",
    "BatchDeleteImageResponseTypeDef",
    "CompleteLayerUploadRequestRequestTypeDef",
    "CompleteLayerUploadResponseTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResponseTypeDef",
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    "DeleteRepositoryPolicyResponseTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResponseTypeDef",
    "DescribeImageTagsRequestRequestTypeDef",
    "DescribeImageTagsResponseTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResponseTypeDef",
    "DescribeRegistriesRequestRequestTypeDef",
    "DescribeRegistriesResponseTypeDef",
    "DescribeRepositoriesRequestRequestTypeDef",
    "DescribeRepositoriesResponseTypeDef",
    "GetAuthorizationTokenResponseTypeDef",
    "GetRegistryCatalogDataResponseTypeDef",
    "GetRepositoryCatalogDataRequestRequestTypeDef",
    "GetRepositoryCatalogDataResponseTypeDef",
    "GetRepositoryPolicyRequestRequestTypeDef",
    "GetRepositoryPolicyResponseTypeDef",
    "ImageDetailTypeDef",
    "ImageFailureTypeDef",
    "ImageIdentifierTypeDef",
    "ImageTagDetailTypeDef",
    "ImageTypeDef",
    "InitiateLayerUploadRequestRequestTypeDef",
    "InitiateLayerUploadResponseTypeDef",
    "LayerFailureTypeDef",
    "LayerTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutImageRequestRequestTypeDef",
    "PutImageResponseTypeDef",
    "PutRegistryCatalogDataRequestRequestTypeDef",
    "PutRegistryCatalogDataResponseTypeDef",
    "PutRepositoryCatalogDataRequestRequestTypeDef",
    "PutRepositoryCatalogDataResponseTypeDef",
    "ReferencedImageDetailTypeDef",
    "RegistryAliasTypeDef",
    "RegistryCatalogDataTypeDef",
    "RegistryTypeDef",
    "RepositoryCatalogDataInputTypeDef",
    "RepositoryCatalogDataTypeDef",
    "RepositoryTypeDef",
    "ResponseMetadataTypeDef",
    "SetRepositoryPolicyRequestRequestTypeDef",
    "SetRepositoryPolicyResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UploadLayerPartRequestRequestTypeDef",
    "UploadLayerPartResponseTypeDef",
)

AuthorizationDataTypeDef = TypedDict(
    "AuthorizationDataTypeDef",
    {
        "authorizationToken": NotRequired[str],
        "expiresAt": NotRequired[datetime],
    },
)

BatchCheckLayerAvailabilityRequestRequestTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityRequestRequestTypeDef",
    {
        "repositoryName": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)

BatchCheckLayerAvailabilityResponseTypeDef = TypedDict(
    "BatchCheckLayerAvailabilityResponseTypeDef",
    {
        "layers": List["LayerTypeDef"],
        "failures": List["LayerFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BatchDeleteImageRequestRequestTypeDef = TypedDict(
    "BatchDeleteImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageIds": Sequence["ImageIdentifierTypeDef"],
        "registryId": NotRequired[str],
    },
)

BatchDeleteImageResponseTypeDef = TypedDict(
    "BatchDeleteImageResponseTypeDef",
    {
        "imageIds": List["ImageIdentifierTypeDef"],
        "failures": List["ImageFailureTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CompleteLayerUploadRequestRequestTypeDef = TypedDict(
    "CompleteLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "layerDigests": Sequence[str],
        "registryId": NotRequired[str],
    },
)

CompleteLayerUploadResponseTypeDef = TypedDict(
    "CompleteLayerUploadResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "layerDigest": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": NotRequired["RepositoryCatalogDataInputTypeDef"],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRepositoryResponseTypeDef = TypedDict(
    "CreateRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

DeleteRepositoryPolicyResponseTypeDef = TypedDict(
    "DeleteRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)

DeleteRepositoryResponseTypeDef = TypedDict(
    "DeleteRepositoryResponseTypeDef",
    {
        "repository": "RepositoryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImageTagsRequestRequestTypeDef = TypedDict(
    "DescribeImageTagsRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeImageTagsResponseTypeDef = TypedDict(
    "DescribeImageTagsResponseTypeDef",
    {
        "imageTagDetails": List["ImageTagDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
        "imageIds": NotRequired[Sequence["ImageIdentifierTypeDef"]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeImagesResponseTypeDef = TypedDict(
    "DescribeImagesResponseTypeDef",
    {
        "imageDetails": List["ImageDetailTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegistriesRequestRequestTypeDef = TypedDict(
    "DescribeRegistriesRequestRequestTypeDef",
    {
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeRegistriesResponseTypeDef = TypedDict(
    "DescribeRegistriesResponseTypeDef",
    {
        "registries": List["RegistryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoriesRequestRequestTypeDef = TypedDict(
    "DescribeRepositoriesRequestRequestTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryNames": NotRequired[Sequence[str]],
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)

DescribeRepositoriesResponseTypeDef = TypedDict(
    "DescribeRepositoriesResponseTypeDef",
    {
        "repositories": List["RepositoryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAuthorizationTokenResponseTypeDef = TypedDict(
    "GetAuthorizationTokenResponseTypeDef",
    {
        "authorizationData": "AuthorizationDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRegistryCatalogDataResponseTypeDef = TypedDict(
    "GetRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "GetRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

GetRepositoryCatalogDataResponseTypeDef = TypedDict(
    "GetRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

GetRepositoryPolicyResponseTypeDef = TypedDict(
    "GetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDetailTypeDef = TypedDict(
    "ImageDetailTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageDigest": NotRequired[str],
        "imageTags": NotRequired[List[str]],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
    },
)

ImageFailureTypeDef = TypedDict(
    "ImageFailureTypeDef",
    {
        "imageId": NotRequired["ImageIdentifierTypeDef"],
        "failureCode": NotRequired[ImageFailureCodeType],
        "failureReason": NotRequired[str],
    },
)

ImageIdentifierTypeDef = TypedDict(
    "ImageIdentifierTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageTag": NotRequired[str],
    },
)

ImageTagDetailTypeDef = TypedDict(
    "ImageTagDetailTypeDef",
    {
        "imageTag": NotRequired[str],
        "createdAt": NotRequired[datetime],
        "imageDetail": NotRequired["ReferencedImageDetailTypeDef"],
    },
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "imageId": NotRequired["ImageIdentifierTypeDef"],
        "imageManifest": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
    },
)

InitiateLayerUploadRequestRequestTypeDef = TypedDict(
    "InitiateLayerUploadRequestRequestTypeDef",
    {
        "repositoryName": str,
        "registryId": NotRequired[str],
    },
)

InitiateLayerUploadResponseTypeDef = TypedDict(
    "InitiateLayerUploadResponseTypeDef",
    {
        "uploadId": str,
        "partSize": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LayerFailureTypeDef = TypedDict(
    "LayerFailureTypeDef",
    {
        "layerDigest": NotRequired[str],
        "failureCode": NotRequired[LayerFailureCodeType],
        "failureReason": NotRequired[str],
    },
)

LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "layerDigest": NotRequired[str],
        "layerAvailability": NotRequired[LayerAvailabilityType],
        "layerSize": NotRequired[int],
        "mediaType": NotRequired[str],
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
        "tags": List["TagTypeDef"],
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

PutImageRequestRequestTypeDef = TypedDict(
    "PutImageRequestRequestTypeDef",
    {
        "repositoryName": str,
        "imageManifest": str,
        "registryId": NotRequired[str],
        "imageManifestMediaType": NotRequired[str],
        "imageTag": NotRequired[str],
        "imageDigest": NotRequired[str],
    },
)

PutImageResponseTypeDef = TypedDict(
    "PutImageResponseTypeDef",
    {
        "image": "ImageTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRegistryCatalogDataRequestRequestTypeDef = TypedDict(
    "PutRegistryCatalogDataRequestRequestTypeDef",
    {
        "displayName": NotRequired[str],
    },
)

PutRegistryCatalogDataResponseTypeDef = TypedDict(
    "PutRegistryCatalogDataResponseTypeDef",
    {
        "registryCatalogData": "RegistryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryCatalogDataRequestRequestTypeDef = TypedDict(
    "PutRepositoryCatalogDataRequestRequestTypeDef",
    {
        "repositoryName": str,
        "catalogData": "RepositoryCatalogDataInputTypeDef",
        "registryId": NotRequired[str],
    },
)

PutRepositoryCatalogDataResponseTypeDef = TypedDict(
    "PutRepositoryCatalogDataResponseTypeDef",
    {
        "catalogData": "RepositoryCatalogDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReferencedImageDetailTypeDef = TypedDict(
    "ReferencedImageDetailTypeDef",
    {
        "imageDigest": NotRequired[str],
        "imageSizeInBytes": NotRequired[int],
        "imagePushedAt": NotRequired[datetime],
        "imageManifestMediaType": NotRequired[str],
        "artifactMediaType": NotRequired[str],
    },
)

RegistryAliasTypeDef = TypedDict(
    "RegistryAliasTypeDef",
    {
        "name": str,
        "status": RegistryAliasStatusType,
        "primaryRegistryAlias": bool,
        "defaultRegistryAlias": bool,
    },
)

RegistryCatalogDataTypeDef = TypedDict(
    "RegistryCatalogDataTypeDef",
    {
        "displayName": NotRequired[str],
    },
)

RegistryTypeDef = TypedDict(
    "RegistryTypeDef",
    {
        "registryId": str,
        "registryArn": str,
        "registryUri": str,
        "verified": bool,
        "aliases": List["RegistryAliasTypeDef"],
    },
)

RepositoryCatalogDataInputTypeDef = TypedDict(
    "RepositoryCatalogDataInputTypeDef",
    {
        "description": NotRequired[str],
        "architectures": NotRequired[Sequence[str]],
        "operatingSystems": NotRequired[Sequence[str]],
        "logoImageBlob": NotRequired[Union[bytes, IO[bytes], StreamingBody]],
        "aboutText": NotRequired[str],
        "usageText": NotRequired[str],
    },
)

RepositoryCatalogDataTypeDef = TypedDict(
    "RepositoryCatalogDataTypeDef",
    {
        "description": NotRequired[str],
        "architectures": NotRequired[List[str]],
        "operatingSystems": NotRequired[List[str]],
        "logoUrl": NotRequired[str],
        "aboutText": NotRequired[str],
        "usageText": NotRequired[str],
        "marketplaceCertified": NotRequired[bool],
    },
)

RepositoryTypeDef = TypedDict(
    "RepositoryTypeDef",
    {
        "repositoryArn": NotRequired[str],
        "registryId": NotRequired[str],
        "repositoryName": NotRequired[str],
        "repositoryUri": NotRequired[str],
        "createdAt": NotRequired[datetime],
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

SetRepositoryPolicyRequestRequestTypeDef = TypedDict(
    "SetRepositoryPolicyRequestRequestTypeDef",
    {
        "repositoryName": str,
        "policyText": str,
        "registryId": NotRequired[str],
        "force": NotRequired[bool],
    },
)

SetRepositoryPolicyResponseTypeDef = TypedDict(
    "SetRepositoryPolicyResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "policyText": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": NotRequired[str],
        "Value": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UploadLayerPartRequestRequestTypeDef = TypedDict(
    "UploadLayerPartRequestRequestTypeDef",
    {
        "repositoryName": str,
        "uploadId": str,
        "partFirstByte": int,
        "partLastByte": int,
        "layerPartBlob": Union[bytes, IO[bytes], StreamingBody],
        "registryId": NotRequired[str],
    },
)

UploadLayerPartResponseTypeDef = TypedDict(
    "UploadLayerPartResponseTypeDef",
    {
        "registryId": str,
        "repositoryName": str,
        "uploadId": str,
        "lastByteReceived": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
