"""
Type annotations for worklink service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_worklink/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_worklink.type_defs import AssociateDomainRequestRequestTypeDef

    data: AssociateDomainRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from typing_extensions import NotRequired

from .literals import DeviceStatusType, DomainStatusType, FleetStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateDomainRequestRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    "AssociateWebsiteAuthorizationProviderResponseTypeDef",
    "AssociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    "AssociateWebsiteCertificateAuthorityResponseTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResponseTypeDef",
    "DeleteFleetRequestRequestTypeDef",
    "DescribeAuditStreamConfigurationRequestRequestTypeDef",
    "DescribeAuditStreamConfigurationResponseTypeDef",
    "DescribeCompanyNetworkConfigurationRequestRequestTypeDef",
    "DescribeCompanyNetworkConfigurationResponseTypeDef",
    "DescribeDevicePolicyConfigurationRequestRequestTypeDef",
    "DescribeDevicePolicyConfigurationResponseTypeDef",
    "DescribeDeviceRequestRequestTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainRequestRequestTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFleetMetadataRequestRequestTypeDef",
    "DescribeFleetMetadataResponseTypeDef",
    "DescribeIdentityProviderConfigurationRequestRequestTypeDef",
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    "DescribeWebsiteCertificateAuthorityRequestRequestTypeDef",
    "DescribeWebsiteCertificateAuthorityResponseTypeDef",
    "DeviceSummaryTypeDef",
    "DisassociateDomainRequestRequestTypeDef",
    "DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    "DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    "DomainSummaryTypeDef",
    "FleetSummaryTypeDef",
    "ListDevicesRequestRequestTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsRequestRequestTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFleetsRequestRequestTypeDef",
    "ListFleetsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebsiteAuthorizationProvidersRequestRequestTypeDef",
    "ListWebsiteAuthorizationProvidersResponseTypeDef",
    "ListWebsiteCertificateAuthoritiesRequestRequestTypeDef",
    "ListWebsiteCertificateAuthoritiesResponseTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreDomainAccessRequestRequestTypeDef",
    "RevokeDomainAccessRequestRequestTypeDef",
    "SignOutUserRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateAuditStreamConfigurationRequestRequestTypeDef",
    "UpdateCompanyNetworkConfigurationRequestRequestTypeDef",
    "UpdateDevicePolicyConfigurationRequestRequestTypeDef",
    "UpdateDomainMetadataRequestRequestTypeDef",
    "UpdateFleetMetadataRequestRequestTypeDef",
    "UpdateIdentityProviderConfigurationRequestRequestTypeDef",
    "WebsiteAuthorizationProviderSummaryTypeDef",
    "WebsiteCaSummaryTypeDef",
)

AssociateDomainRequestRequestTypeDef = TypedDict(
    "AssociateDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
        "AcmCertificateArn": str,
        "DisplayName": NotRequired[str],
    },
)

AssociateWebsiteAuthorizationProviderRequestRequestTypeDef = TypedDict(
    "AssociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderType": Literal["SAML"],
        "DomainName": NotRequired[str],
    },
)

AssociateWebsiteAuthorizationProviderResponseTypeDef = TypedDict(
    "AssociateWebsiteAuthorizationProviderResponseTypeDef",
    {
        "AuthorizationProviderId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "AssociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "Certificate": str,
        "DisplayName": NotRequired[str],
    },
)

AssociateWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "AssociateWebsiteCertificateAuthorityResponseTypeDef",
    {
        "WebsiteCaId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetRequestRequestTypeDef = TypedDict(
    "CreateFleetRequestRequestTypeDef",
    {
        "FleetName": str,
        "DisplayName": NotRequired[str],
        "OptimizeForEndUserLocation": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)

CreateFleetResponseTypeDef = TypedDict(
    "CreateFleetResponseTypeDef",
    {
        "FleetArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetRequestRequestTypeDef = TypedDict(
    "DeleteFleetRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeAuditStreamConfigurationResponseTypeDef = TypedDict(
    "DescribeAuditStreamConfigurationResponseTypeDef",
    {
        "AuditStreamArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCompanyNetworkConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeCompanyNetworkConfigurationResponseTypeDef = TypedDict(
    "DescribeCompanyNetworkConfigurationResponseTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDevicePolicyConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeDevicePolicyConfigurationResponseTypeDef = TypedDict(
    "DescribeDevicePolicyConfigurationResponseTypeDef",
    {
        "DeviceCaCertificate": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDeviceRequestRequestTypeDef = TypedDict(
    "DescribeDeviceRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DeviceId": str,
    },
)

DescribeDeviceResponseTypeDef = TypedDict(
    "DescribeDeviceResponseTypeDef",
    {
        "Status": DeviceStatusType,
        "Model": str,
        "Manufacturer": str,
        "OperatingSystem": str,
        "OperatingSystemVersion": str,
        "PatchLevel": str,
        "FirstAccessedTime": datetime,
        "LastAccessedTime": datetime,
        "Username": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDomainRequestRequestTypeDef = TypedDict(
    "DescribeDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DescribeDomainResponseTypeDef = TypedDict(
    "DescribeDomainResponseTypeDef",
    {
        "DomainName": str,
        "DisplayName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
        "AcmCertificateArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetMetadataRequestRequestTypeDef = TypedDict(
    "DescribeFleetMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeFleetMetadataResponseTypeDef = TypedDict(
    "DescribeFleetMetadataResponseTypeDef",
    {
        "CreatedTime": datetime,
        "LastUpdatedTime": datetime,
        "FleetName": str,
        "DisplayName": str,
        "OptimizeForEndUserLocation": bool,
        "CompanyCode": str,
        "FleetStatus": FleetStatusType,
        "Tags": Dict[str, str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdentityProviderConfigurationRequestRequestTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
    },
)

DescribeIdentityProviderConfigurationResponseTypeDef = TypedDict(
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    {
        "IdentityProviderType": Literal["SAML"],
        "ServiceProviderSamlMetadata": str,
        "IdentityProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

DescribeWebsiteCertificateAuthorityResponseTypeDef = TypedDict(
    "DescribeWebsiteCertificateAuthorityResponseTypeDef",
    {
        "Certificate": str,
        "CreatedTime": datetime,
        "DisplayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "DeviceId": NotRequired[str],
        "DeviceStatus": NotRequired[DeviceStatusType],
    },
)

DisassociateDomainRequestRequestTypeDef = TypedDict(
    "DisassociateDomainRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef = TypedDict(
    "DisassociateWebsiteAuthorizationProviderRequestRequestTypeDef",
    {
        "FleetArn": str,
        "AuthorizationProviderId": str,
    },
)

DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef = TypedDict(
    "DisassociateWebsiteCertificateAuthorityRequestRequestTypeDef",
    {
        "FleetArn": str,
        "WebsiteCaId": str,
    },
)

DomainSummaryTypeDef = TypedDict(
    "DomainSummaryTypeDef",
    {
        "DomainName": str,
        "CreatedTime": datetime,
        "DomainStatus": DomainStatusType,
        "DisplayName": NotRequired[str],
    },
)

FleetSummaryTypeDef = TypedDict(
    "FleetSummaryTypeDef",
    {
        "FleetArn": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "FleetName": NotRequired[str],
        "DisplayName": NotRequired[str],
        "CompanyCode": NotRequired[str],
        "FleetStatus": NotRequired[FleetStatusType],
        "Tags": NotRequired[Dict[str, str]],
    },
)

ListDevicesRequestRequestTypeDef = TypedDict(
    "ListDevicesRequestRequestTypeDef",
    {
        "FleetArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDevicesResponseTypeDef = TypedDict(
    "ListDevicesResponseTypeDef",
    {
        "Devices": List["DeviceSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListDomainsRequestRequestTypeDef = TypedDict(
    "ListDomainsRequestRequestTypeDef",
    {
        "FleetArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListDomainsResponseTypeDef = TypedDict(
    "ListDomainsResponseTypeDef",
    {
        "Domains": List["DomainSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFleetsRequestRequestTypeDef = TypedDict(
    "ListFleetsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListFleetsResponseTypeDef = TypedDict(
    "ListFleetsResponseTypeDef",
    {
        "FleetSummaryList": List["FleetSummaryTypeDef"],
        "NextToken": str,
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

ListWebsiteAuthorizationProvidersRequestRequestTypeDef = TypedDict(
    "ListWebsiteAuthorizationProvidersRequestRequestTypeDef",
    {
        "FleetArn": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)

ListWebsiteAuthorizationProvidersResponseTypeDef = TypedDict(
    "ListWebsiteAuthorizationProvidersResponseTypeDef",
    {
        "WebsiteAuthorizationProviders": List["WebsiteAuthorizationProviderSummaryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListWebsiteCertificateAuthoritiesRequestRequestTypeDef = TypedDict(
    "ListWebsiteCertificateAuthoritiesRequestRequestTypeDef",
    {
        "FleetArn": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)

ListWebsiteCertificateAuthoritiesResponseTypeDef = TypedDict(
    "ListWebsiteCertificateAuthoritiesResponseTypeDef",
    {
        "WebsiteCertificateAuthorities": List["WebsiteCaSummaryTypeDef"],
        "NextToken": str,
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

RestoreDomainAccessRequestRequestTypeDef = TypedDict(
    "RestoreDomainAccessRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

RevokeDomainAccessRequestRequestTypeDef = TypedDict(
    "RevokeDomainAccessRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
    },
)

SignOutUserRequestRequestTypeDef = TypedDict(
    "SignOutUserRequestRequestTypeDef",
    {
        "FleetArn": str,
        "Username": str,
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

UpdateAuditStreamConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateAuditStreamConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "AuditStreamArn": NotRequired[str],
    },
)

UpdateCompanyNetworkConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateCompanyNetworkConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "VpcId": str,
        "SubnetIds": Sequence[str],
        "SecurityGroupIds": Sequence[str],
    },
)

UpdateDevicePolicyConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateDevicePolicyConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DeviceCaCertificate": NotRequired[str],
    },
)

UpdateDomainMetadataRequestRequestTypeDef = TypedDict(
    "UpdateDomainMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DomainName": str,
        "DisplayName": NotRequired[str],
    },
)

UpdateFleetMetadataRequestRequestTypeDef = TypedDict(
    "UpdateFleetMetadataRequestRequestTypeDef",
    {
        "FleetArn": str,
        "DisplayName": NotRequired[str],
        "OptimizeForEndUserLocation": NotRequired[bool],
    },
)

UpdateIdentityProviderConfigurationRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderConfigurationRequestRequestTypeDef",
    {
        "FleetArn": str,
        "IdentityProviderType": Literal["SAML"],
        "IdentityProviderSamlMetadata": NotRequired[str],
    },
)

WebsiteAuthorizationProviderSummaryTypeDef = TypedDict(
    "WebsiteAuthorizationProviderSummaryTypeDef",
    {
        "AuthorizationProviderType": Literal["SAML"],
        "AuthorizationProviderId": NotRequired[str],
        "DomainName": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
    },
)

WebsiteCaSummaryTypeDef = TypedDict(
    "WebsiteCaSummaryTypeDef",
    {
        "WebsiteCaId": NotRequired[str],
        "CreatedTime": NotRequired[datetime],
        "DisplayName": NotRequired[str],
    },
)
