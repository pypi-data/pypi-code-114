"""
Type annotations for codeartifact service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeartifact/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeartifact.type_defs import AssetSummaryTypeDef

    data: AssetSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import (
    DomainStatusType,
    HashAlgorithmType,
    PackageFormatType,
    PackageVersionErrorCodeType,
    PackageVersionStatusType,
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
    "AssetSummaryTypeDef",
    "AssociateExternalConnectionRequestRequestTypeDef",
    "AssociateExternalConnectionResultTypeDef",
    "CopyPackageVersionsRequestRequestTypeDef",
    "CopyPackageVersionsResultTypeDef",
    "CreateDomainRequestRequestTypeDef",
    "CreateDomainResultTypeDef",
    "CreateRepositoryRequestRequestTypeDef",
    "CreateRepositoryResultTypeDef",
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    "DeleteDomainPermissionsPolicyResultTypeDef",
    "DeleteDomainRequestRequestTypeDef",
    "DeleteDomainResultTypeDef",
    "DeletePackageVersionsRequestRequestTypeDef",
    "DeletePackageVersionsResultTypeDef",
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    "DeleteRepositoryRequestRequestTypeDef",
    "DeleteRepositoryResultTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResultTypeDef",
    "DescribePackageVersionRequestRequestTypeDef",
    "DescribePackageVersionResultTypeDef",
    "DescribeRepositoryRequestRequestTypeDef",
    "DescribeRepositoryResultTypeDef",
    "DisassociateExternalConnectionRequestRequestTypeDef",
    "DisassociateExternalConnectionResultTypeDef",
    "DisposePackageVersionsRequestRequestTypeDef",
    "DisposePackageVersionsResultTypeDef",
    "DomainDescriptionTypeDef",
    "DomainSummaryTypeDef",
    "GetAuthorizationTokenRequestRequestTypeDef",
    "GetAuthorizationTokenResultTypeDef",
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    "GetDomainPermissionsPolicyResultTypeDef",
    "GetPackageVersionAssetRequestRequestTypeDef",
    "GetPackageVersionAssetResultTypeDef",
    "GetPackageVersionReadmeRequestRequestTypeDef",
    "GetPackageVersionReadmeResultTypeDef",
    "GetRepositoryEndpointRequestRequestTypeDef",
    "GetRepositoryEndpointResultTypeDef",
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    "GetRepositoryPermissionsPolicyResultTypeDef",
    "LicenseInfoTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResultTypeDef",
    "ListPackageVersionAssetsRequestRequestTypeDef",
    "ListPackageVersionAssetsResultTypeDef",
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    "ListPackageVersionDependenciesResultTypeDef",
    "ListPackageVersionsRequestRequestTypeDef",
    "ListPackageVersionsResultTypeDef",
    "ListPackagesRequestRequestTypeDef",
    "ListPackagesResultTypeDef",
    "ListRepositoriesInDomainRequestRequestTypeDef",
    "ListRepositoriesInDomainResultTypeDef",
    "ListRepositoriesRequestRequestTypeDef",
    "ListRepositoriesResultTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PackageDependencyTypeDef",
    "PackageSummaryTypeDef",
    "PackageVersionDescriptionTypeDef",
    "PackageVersionErrorTypeDef",
    "PackageVersionSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    "PutDomainPermissionsPolicyResultTypeDef",
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    "PutRepositoryPermissionsPolicyResultTypeDef",
    "RepositoryDescriptionTypeDef",
    "RepositoryExternalConnectionInfoTypeDef",
    "RepositorySummaryTypeDef",
    "ResourcePolicyTypeDef",
    "ResponseMetadataTypeDef",
    "SuccessfulPackageVersionInfoTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    "UpdatePackageVersionsStatusResultTypeDef",
    "UpdateRepositoryRequestRequestTypeDef",
    "UpdateRepositoryResultTypeDef",
    "UpstreamRepositoryInfoTypeDef",
    "UpstreamRepositoryTypeDef",
)

AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "name": str,
        "size": NotRequired[int],
        "hashes": NotRequired[Dict[HashAlgorithmType, str]],
    },
)

AssociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "AssociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
        "domainOwner": NotRequired[str],
    },
)

AssociateExternalConnectionResultTypeDef = TypedDict(
    "AssociateExternalConnectionResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CopyPackageVersionsRequestRequestTypeDef = TypedDict(
    "CopyPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "sourceRepository": str,
        "destinationRepository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versions": NotRequired[Sequence[str]],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "allowOverwrite": NotRequired[bool],
        "includeFromUpstream": NotRequired[bool],
    },
)

CopyPackageVersionsResultTypeDef = TypedDict(
    "CopyPackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDomainRequestRequestTypeDef = TypedDict(
    "CreateDomainRequestRequestTypeDef",
    {
        "domain": str,
        "encryptionKey": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateRepositoryRequestRequestTypeDef = TypedDict(
    "CreateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[Sequence["UpstreamRepositoryTypeDef"]],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateRepositoryResultTypeDef = TypedDict(
    "CreateRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)

DeleteDomainPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteDomainRequestRequestTypeDef = TypedDict(
    "DeleteDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeletePackageVersionsRequestRequestTypeDef = TypedDict(
    "DeletePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

DeletePackageVersionsResultTypeDef = TypedDict(
    "DeletePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)

DeleteRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "DeleteRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteRepositoryRequestRequestTypeDef = TypedDict(
    "DeleteRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)

DeleteRepositoryResultTypeDef = TypedDict(
    "DeleteRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)

DescribeDomainResultTypeDef = TypedDict(
    "DescribeDomainResultTypeDef",
    {
        "domain": "DomainDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePackageVersionRequestRequestTypeDef = TypedDict(
    "DescribePackageVersionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

DescribePackageVersionResultTypeDef = TypedDict(
    "DescribePackageVersionResultTypeDef",
    {
        "packageVersion": "PackageVersionDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRepositoryRequestRequestTypeDef = TypedDict(
    "DescribeRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)

DescribeRepositoryResultTypeDef = TypedDict(
    "DescribeRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateExternalConnectionRequestRequestTypeDef = TypedDict(
    "DisassociateExternalConnectionRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "externalConnection": str,
        "domainOwner": NotRequired[str],
    },
)

DisassociateExternalConnectionResultTypeDef = TypedDict(
    "DisassociateExternalConnectionResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisposePackageVersionsRequestRequestTypeDef = TypedDict(
    "DisposePackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

DisposePackageVersionsResultTypeDef = TypedDict(
    "DisposePackageVersionsResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DomainDescriptionTypeDef = TypedDict(
    "DomainDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "owner": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[DomainStatusType],
        "createdTime": NotRequired[datetime],
        "encryptionKey": NotRequired[str],
        "repositoryCount": NotRequired[int],
        "assetSizeBytes": NotRequired[int],
        "s3BucketArn": NotRequired[str],
    },
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "name": NotRequired[str],
        "owner": NotRequired[str],
        "arn": NotRequired[str],
        "status": NotRequired[DomainStatusType],
        "createdTime": NotRequired[datetime],
        "encryptionKey": NotRequired[str],
    },
)

GetAuthorizationTokenRequestRequestTypeDef = TypedDict(
    "GetAuthorizationTokenRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "durationSeconds": NotRequired[int],
    },
)

GetAuthorizationTokenResultTypeDef = TypedDict(
    "GetAuthorizationTokenResultTypeDef",
    {
        "authorizationToken": str,
        "expiration": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "GetDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
    },
)

GetDomainPermissionsPolicyResultTypeDef = TypedDict(
    "GetDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPackageVersionAssetRequestRequestTypeDef = TypedDict(
    "GetPackageVersionAssetRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "asset": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "packageVersionRevision": NotRequired[str],
    },
)

GetPackageVersionAssetResultTypeDef = TypedDict(
    "GetPackageVersionAssetResultTypeDef",
    {
        "asset": StreamingBody,
        "assetName": str,
        "packageVersion": str,
        "packageVersionRevision": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPackageVersionReadmeRequestRequestTypeDef = TypedDict(
    "GetPackageVersionReadmeRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
    },
)

GetPackageVersionReadmeResultTypeDef = TypedDict(
    "GetPackageVersionReadmeResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "readme": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryEndpointRequestRequestTypeDef = TypedDict(
    "GetRepositoryEndpointRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "domainOwner": NotRequired[str],
    },
)

GetRepositoryEndpointResultTypeDef = TypedDict(
    "GetRepositoryEndpointResultTypeDef",
    {
        "repositoryEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
    },
)

GetRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "GetRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LicenseInfoTypeDef = TypedDict(
    "LicenseInfoTypeDef",
    {
        "name": NotRequired[str],
        "url": NotRequired[str],
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListDomainsResultTypeDef = TypedDict(
    "ListDomainsResultTypeDef",
    {
        "domains": List["DomainSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageVersionAssetsRequestRequestTypeDef = TypedDict(
    "ListPackageVersionAssetsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPackageVersionAssetsResultTypeDef = TypedDict(
    "ListPackageVersionAssetsResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "assets": List["AssetSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageVersionDependenciesRequestRequestTypeDef = TypedDict(
    "ListPackageVersionDependenciesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "packageVersion": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "nextToken": NotRequired[str],
    },
)

ListPackageVersionDependenciesResultTypeDef = TypedDict(
    "ListPackageVersionDependenciesResultTypeDef",
    {
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "version": str,
        "versionRevision": str,
        "nextToken": str,
        "dependencies": List["PackageDependencyTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackageVersionsRequestRequestTypeDef = TypedDict(
    "ListPackageVersionsRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
        "sortBy": NotRequired[Literal["PUBLISHED_TIME"]],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPackageVersionsResultTypeDef = TypedDict(
    "ListPackageVersionsResultTypeDef",
    {
        "defaultDisplayVersion": str,
        "format": PackageFormatType,
        "namespace": str,
        "package": str,
        "versions": List["PackageVersionSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPackagesRequestRequestTypeDef = TypedDict(
    "ListPackagesRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packagePrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPackagesResultTypeDef = TypedDict(
    "ListPackagesResultTypeDef",
    {
        "packages": List["PackageSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesInDomainRequestRequestTypeDef = TypedDict(
    "ListRepositoriesInDomainRequestRequestTypeDef",
    {
        "domain": str,
        "domainOwner": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "repositoryPrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListRepositoriesInDomainResultTypeDef = TypedDict(
    "ListRepositoriesInDomainResultTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListRepositoriesRequestRequestTypeDef = TypedDict(
    "ListRepositoriesRequestRequestTypeDef",
    {
        "repositoryPrefix": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListRepositoriesResultTypeDef = TypedDict(
    "ListRepositoriesResultTypeDef",
    {
        "repositories": List["RepositorySummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef",
    {
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PackageDependencyTypeDef = TypedDict(
    "PackageDependencyTypeDef",
    {
        "namespace": NotRequired[str],
        "package": NotRequired[str],
        "dependencyType": NotRequired[str],
        "versionRequirement": NotRequired[str],
    },
)

PackageSummaryTypeDef = TypedDict(
    "PackageSummaryTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "package": NotRequired[str],
    },
)

PackageVersionDescriptionTypeDef = TypedDict(
    "PackageVersionDescriptionTypeDef",
    {
        "format": NotRequired[PackageFormatType],
        "namespace": NotRequired[str],
        "packageName": NotRequired[str],
        "displayName": NotRequired[str],
        "version": NotRequired[str],
        "summary": NotRequired[str],
        "homePage": NotRequired[str],
        "sourceCodeRepository": NotRequired[str],
        "publishedTime": NotRequired[datetime],
        "licenses": NotRequired[List["LicenseInfoTypeDef"]],
        "revision": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
    },
)

PackageVersionErrorTypeDef = TypedDict(
    "PackageVersionErrorTypeDef",
    {
        "errorCode": NotRequired[PackageVersionErrorCodeType],
        "errorMessage": NotRequired[str],
    },
)

PackageVersionSummaryTypeDef = TypedDict(
    "PackageVersionSummaryTypeDef",
    {
        "version": str,
        "status": PackageVersionStatusType,
        "revision": NotRequired[str],
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

PutDomainPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "PutDomainPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "policyDocument": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)

PutDomainPermissionsPolicyResultTypeDef = TypedDict(
    "PutDomainPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PutRepositoryPermissionsPolicyRequestRequestTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "policyDocument": str,
        "domainOwner": NotRequired[str],
        "policyRevision": NotRequired[str],
    },
)

PutRepositoryPermissionsPolicyResultTypeDef = TypedDict(
    "PutRepositoryPermissionsPolicyResultTypeDef",
    {
        "policy": "ResourcePolicyTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RepositoryDescriptionTypeDef = TypedDict(
    "RepositoryDescriptionTypeDef",
    {
        "name": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "domainName": NotRequired[str],
        "domainOwner": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[List["UpstreamRepositoryInfoTypeDef"]],
        "externalConnections": NotRequired[List["RepositoryExternalConnectionInfoTypeDef"]],
    },
)

RepositoryExternalConnectionInfoTypeDef = TypedDict(
    "RepositoryExternalConnectionInfoTypeDef",
    {
        "externalConnectionName": NotRequired[str],
        "packageFormat": NotRequired[PackageFormatType],
        "status": NotRequired[Literal["Available"]],
    },
)

RepositorySummaryTypeDef = TypedDict(
    "RepositorySummaryTypeDef",
    {
        "name": NotRequired[str],
        "administratorAccount": NotRequired[str],
        "domainName": NotRequired[str],
        "domainOwner": NotRequired[str],
        "arn": NotRequired[str],
        "description": NotRequired[str],
    },
)

ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "resourceArn": NotRequired[str],
        "revision": NotRequired[str],
        "document": NotRequired[str],
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

SuccessfulPackageVersionInfoTypeDef = TypedDict(
    "SuccessfulPackageVersionInfoTypeDef",
    {
        "revision": NotRequired[str],
        "status": NotRequired[PackageVersionStatusType],
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
        "key": str,
        "value": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdatePackageVersionsStatusRequestRequestTypeDef = TypedDict(
    "UpdatePackageVersionsStatusRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "format": PackageFormatType,
        "package": str,
        "versions": Sequence[str],
        "targetStatus": PackageVersionStatusType,
        "domainOwner": NotRequired[str],
        "namespace": NotRequired[str],
        "versionRevisions": NotRequired[Mapping[str, str]],
        "expectedStatus": NotRequired[PackageVersionStatusType],
    },
)

UpdatePackageVersionsStatusResultTypeDef = TypedDict(
    "UpdatePackageVersionsStatusResultTypeDef",
    {
        "successfulVersions": Dict[str, "SuccessfulPackageVersionInfoTypeDef"],
        "failedVersions": Dict[str, "PackageVersionErrorTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateRepositoryRequestRequestTypeDef = TypedDict(
    "UpdateRepositoryRequestRequestTypeDef",
    {
        "domain": str,
        "repository": str,
        "domainOwner": NotRequired[str],
        "description": NotRequired[str],
        "upstreams": NotRequired[Sequence["UpstreamRepositoryTypeDef"]],
    },
)

UpdateRepositoryResultTypeDef = TypedDict(
    "UpdateRepositoryResultTypeDef",
    {
        "repository": "RepositoryDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpstreamRepositoryInfoTypeDef = TypedDict(
    "UpstreamRepositoryInfoTypeDef",
    {
        "repositoryName": NotRequired[str],
    },
)

UpstreamRepositoryTypeDef = TypedDict(
    "UpstreamRepositoryTypeDef",
    {
        "repositoryName": str,
    },
)
