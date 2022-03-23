"""
Type annotations for workspaces-web service type definitions.

[Open documentation](https://vemel.github.io/types_aiobotocore_docs/types_aiobotocore_workspaces_web/type_defs.html)

Usage::

    ```python
    from types_aiobotocore_workspaces_web.type_defs import AssociateBrowserSettingsRequestRequestTypeDef

    data: AssociateBrowserSettingsRequestRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody
from typing_extensions import NotRequired

from .literals import EnabledTypeType, IdentityProviderTypeType, PortalStatusType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateBrowserSettingsRequestRequestTypeDef",
    "AssociateBrowserSettingsResponseTypeDef",
    "AssociateNetworkSettingsRequestRequestTypeDef",
    "AssociateNetworkSettingsResponseTypeDef",
    "AssociateTrustStoreRequestRequestTypeDef",
    "AssociateTrustStoreResponseTypeDef",
    "AssociateUserSettingsRequestRequestTypeDef",
    "AssociateUserSettingsResponseTypeDef",
    "BrowserSettingsSummaryTypeDef",
    "BrowserSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CreateBrowserSettingsRequestRequestTypeDef",
    "CreateBrowserSettingsResponseTypeDef",
    "CreateIdentityProviderRequestRequestTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateNetworkSettingsRequestRequestTypeDef",
    "CreateNetworkSettingsResponseTypeDef",
    "CreatePortalRequestRequestTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateTrustStoreRequestRequestTypeDef",
    "CreateTrustStoreResponseTypeDef",
    "CreateUserSettingsRequestRequestTypeDef",
    "CreateUserSettingsResponseTypeDef",
    "DeleteBrowserSettingsRequestRequestTypeDef",
    "DeleteIdentityProviderRequestRequestTypeDef",
    "DeleteNetworkSettingsRequestRequestTypeDef",
    "DeletePortalRequestRequestTypeDef",
    "DeleteTrustStoreRequestRequestTypeDef",
    "DeleteUserSettingsRequestRequestTypeDef",
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    "DisassociateTrustStoreRequestRequestTypeDef",
    "DisassociateUserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsRequestRequestTypeDef",
    "GetBrowserSettingsResponseTypeDef",
    "GetIdentityProviderRequestRequestTypeDef",
    "GetIdentityProviderResponseTypeDef",
    "GetNetworkSettingsRequestRequestTypeDef",
    "GetNetworkSettingsResponseTypeDef",
    "GetPortalRequestRequestTypeDef",
    "GetPortalResponseTypeDef",
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    "GetPortalServiceProviderMetadataResponseTypeDef",
    "GetTrustStoreCertificateRequestRequestTypeDef",
    "GetTrustStoreCertificateResponseTypeDef",
    "GetTrustStoreRequestRequestTypeDef",
    "GetTrustStoreResponseTypeDef",
    "GetUserSettingsRequestRequestTypeDef",
    "GetUserSettingsResponseTypeDef",
    "IdentityProviderSummaryTypeDef",
    "IdentityProviderTypeDef",
    "ListBrowserSettingsRequestRequestTypeDef",
    "ListBrowserSettingsResponseTypeDef",
    "ListIdentityProvidersRequestRequestTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListNetworkSettingsRequestRequestTypeDef",
    "ListNetworkSettingsResponseTypeDef",
    "ListPortalsRequestRequestTypeDef",
    "ListPortalsResponseTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    "ListTrustStoreCertificatesResponseTypeDef",
    "ListTrustStoresRequestRequestTypeDef",
    "ListTrustStoresResponseTypeDef",
    "ListUserSettingsRequestRequestTypeDef",
    "ListUserSettingsResponseTypeDef",
    "NetworkSettingsSummaryTypeDef",
    "NetworkSettingsTypeDef",
    "PortalSummaryTypeDef",
    "PortalTypeDef",
    "ResponseMetadataTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TagTypeDef",
    "TrustStoreSummaryTypeDef",
    "TrustStoreTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateBrowserSettingsRequestRequestTypeDef",
    "UpdateBrowserSettingsResponseTypeDef",
    "UpdateIdentityProviderRequestRequestTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateNetworkSettingsRequestRequestTypeDef",
    "UpdateNetworkSettingsResponseTypeDef",
    "UpdatePortalRequestRequestTypeDef",
    "UpdatePortalResponseTypeDef",
    "UpdateTrustStoreRequestRequestTypeDef",
    "UpdateTrustStoreResponseTypeDef",
    "UpdateUserSettingsRequestRequestTypeDef",
    "UpdateUserSettingsResponseTypeDef",
    "UserSettingsSummaryTypeDef",
    "UserSettingsTypeDef",
)

AssociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
    },
)

AssociateBrowserSettingsResponseTypeDef = TypedDict(
    "AssociateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "AssociateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
    },
)

AssociateNetworkSettingsResponseTypeDef = TypedDict(
    "AssociateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "portalArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateTrustStoreRequestRequestTypeDef = TypedDict(
    "AssociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
    },
)

AssociateTrustStoreResponseTypeDef = TypedDict(
    "AssociateTrustStoreResponseTypeDef",
    {
        "portalArn": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateUserSettingsRequestRequestTypeDef = TypedDict(
    "AssociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
    },
)

AssociateUserSettingsResponseTypeDef = TypedDict(
    "AssociateUserSettingsResponseTypeDef",
    {
        "portalArn": str,
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BrowserSettingsSummaryTypeDef = TypedDict(
    "BrowserSettingsSummaryTypeDef",
    {
        "browserSettingsArn": NotRequired[str],
    },
)

BrowserSettingsTypeDef = TypedDict(
    "BrowserSettingsTypeDef",
    {
        "browserSettingsArn": str,
        "associatedPortalArns": NotRequired[List[str]],
        "browserPolicy": NotRequired[str],
    },
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "issuer": NotRequired[str],
        "notValidAfter": NotRequired[datetime],
        "notValidBefore": NotRequired[datetime],
        "subject": NotRequired[str],
        "thumbprint": NotRequired[str],
    },
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "body": NotRequired[bytes],
        "issuer": NotRequired[str],
        "notValidAfter": NotRequired[datetime],
        "notValidBefore": NotRequired[datetime],
        "subject": NotRequired[str],
        "thumbprint": NotRequired[str],
    },
)

CreateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "CreateBrowserSettingsRequestRequestTypeDef",
    {
        "browserPolicy": str,
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "customerManagedKey": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateBrowserSettingsResponseTypeDef = TypedDict(
    "CreateBrowserSettingsResponseTypeDef",
    {
        "browserSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIdentityProviderRequestRequestTypeDef = TypedDict(
    "CreateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderDetails": Mapping[str, str],
        "identityProviderName": str,
        "identityProviderType": IdentityProviderTypeType,
        "portalArn": str,
        "clientToken": NotRequired[str],
    },
)

CreateIdentityProviderResponseTypeDef = TypedDict(
    "CreateIdentityProviderResponseTypeDef",
    {
        "identityProviderArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "CreateNetworkSettingsRequestRequestTypeDef",
    {
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
        "vpcId": str,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateNetworkSettingsResponseTypeDef = TypedDict(
    "CreateNetworkSettingsResponseTypeDef",
    {
        "networkSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePortalRequestRequestTypeDef = TypedDict(
    "CreatePortalRequestRequestTypeDef",
    {
        "additionalEncryptionContext": NotRequired[Mapping[str, str]],
        "clientToken": NotRequired[str],
        "customerManagedKey": NotRequired[str],
        "displayName": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreatePortalResponseTypeDef = TypedDict(
    "CreatePortalResponseTypeDef",
    {
        "portalArn": str,
        "portalEndpoint": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrustStoreRequestRequestTypeDef = TypedDict(
    "CreateTrustStoreRequestRequestTypeDef",
    {
        "certificateList": Sequence[Union[bytes, IO[bytes], StreamingBody]],
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateTrustStoreResponseTypeDef = TypedDict(
    "CreateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateUserSettingsRequestRequestTypeDef = TypedDict(
    "CreateUserSettingsRequestRequestTypeDef",
    {
        "copyAllowed": EnabledTypeType,
        "downloadAllowed": EnabledTypeType,
        "pasteAllowed": EnabledTypeType,
        "printAllowed": EnabledTypeType,
        "uploadAllowed": EnabledTypeType,
        "clientToken": NotRequired[str],
        "tags": NotRequired[Sequence["TagTypeDef"]],
    },
)

CreateUserSettingsResponseTypeDef = TypedDict(
    "CreateUserSettingsResponseTypeDef",
    {
        "userSettingsArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

DeleteIdentityProviderRequestRequestTypeDef = TypedDict(
    "DeleteIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

DeleteNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DeleteNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

DeletePortalRequestRequestTypeDef = TypedDict(
    "DeletePortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DeleteTrustStoreRequestRequestTypeDef = TypedDict(
    "DeleteTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

DeleteUserSettingsRequestRequestTypeDef = TypedDict(
    "DeleteUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

DisassociateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateBrowserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateNetworkSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateTrustStoreRequestRequestTypeDef = TypedDict(
    "DisassociateTrustStoreRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

DisassociateUserSettingsRequestRequestTypeDef = TypedDict(
    "DisassociateUserSettingsRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetBrowserSettingsRequestRequestTypeDef = TypedDict(
    "GetBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
    },
)

GetBrowserSettingsResponseTypeDef = TypedDict(
    "GetBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetIdentityProviderRequestRequestTypeDef = TypedDict(
    "GetIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
    },
)

GetIdentityProviderResponseTypeDef = TypedDict(
    "GetIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetNetworkSettingsRequestRequestTypeDef = TypedDict(
    "GetNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
    },
)

GetNetworkSettingsResponseTypeDef = TypedDict(
    "GetNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalRequestRequestTypeDef = TypedDict(
    "GetPortalRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalResponseTypeDef = TypedDict(
    "GetPortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPortalServiceProviderMetadataRequestRequestTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataRequestRequestTypeDef",
    {
        "portalArn": str,
    },
)

GetPortalServiceProviderMetadataResponseTypeDef = TypedDict(
    "GetPortalServiceProviderMetadataResponseTypeDef",
    {
        "portalArn": str,
        "serviceProviderSamlMetadata": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreCertificateRequestRequestTypeDef = TypedDict(
    "GetTrustStoreCertificateRequestRequestTypeDef",
    {
        "thumbprint": str,
        "trustStoreArn": str,
    },
)

GetTrustStoreCertificateResponseTypeDef = TypedDict(
    "GetTrustStoreCertificateResponseTypeDef",
    {
        "certificate": "CertificateTypeDef",
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetTrustStoreRequestRequestTypeDef = TypedDict(
    "GetTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
    },
)

GetTrustStoreResponseTypeDef = TypedDict(
    "GetTrustStoreResponseTypeDef",
    {
        "trustStore": "TrustStoreTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetUserSettingsRequestRequestTypeDef = TypedDict(
    "GetUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
    },
)

GetUserSettingsResponseTypeDef = TypedDict(
    "GetUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

IdentityProviderSummaryTypeDef = TypedDict(
    "IdentityProviderSummaryTypeDef",
    {
        "identityProviderArn": NotRequired[str],
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)

IdentityProviderTypeDef = TypedDict(
    "IdentityProviderTypeDef",
    {
        "identityProviderArn": str,
        "identityProviderDetails": NotRequired[Dict[str, str]],
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)

ListBrowserSettingsRequestRequestTypeDef = TypedDict(
    "ListBrowserSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListBrowserSettingsResponseTypeDef = TypedDict(
    "ListBrowserSettingsResponseTypeDef",
    {
        "browserSettings": List["BrowserSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListIdentityProvidersRequestRequestTypeDef = TypedDict(
    "ListIdentityProvidersRequestRequestTypeDef",
    {
        "portalArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListIdentityProvidersResponseTypeDef = TypedDict(
    "ListIdentityProvidersResponseTypeDef",
    {
        "identityProviders": List["IdentityProviderSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListNetworkSettingsRequestRequestTypeDef = TypedDict(
    "ListNetworkSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListNetworkSettingsResponseTypeDef = TypedDict(
    "ListNetworkSettingsResponseTypeDef",
    {
        "networkSettings": List["NetworkSettingsSummaryTypeDef"],
        "nextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListPortalsRequestRequestTypeDef = TypedDict(
    "ListPortalsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListPortalsResponseTypeDef = TypedDict(
    "ListPortalsResponseTypeDef",
    {
        "nextToken": str,
        "portals": List["PortalSummaryTypeDef"],
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
        "tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrustStoreCertificatesRequestRequestTypeDef = TypedDict(
    "ListTrustStoreCertificatesRequestRequestTypeDef",
    {
        "trustStoreArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTrustStoreCertificatesResponseTypeDef = TypedDict(
    "ListTrustStoreCertificatesResponseTypeDef",
    {
        "certificateList": List["CertificateSummaryTypeDef"],
        "nextToken": str,
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTrustStoresRequestRequestTypeDef = TypedDict(
    "ListTrustStoresRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListTrustStoresResponseTypeDef = TypedDict(
    "ListTrustStoresResponseTypeDef",
    {
        "nextToken": str,
        "trustStores": List["TrustStoreSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListUserSettingsRequestRequestTypeDef = TypedDict(
    "ListUserSettingsRequestRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)

ListUserSettingsResponseTypeDef = TypedDict(
    "ListUserSettingsResponseTypeDef",
    {
        "nextToken": str,
        "userSettings": List["UserSettingsSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NetworkSettingsSummaryTypeDef = TypedDict(
    "NetworkSettingsSummaryTypeDef",
    {
        "networkSettingsArn": NotRequired[str],
        "vpcId": NotRequired[str],
    },
)

NetworkSettingsTypeDef = TypedDict(
    "NetworkSettingsTypeDef",
    {
        "networkSettingsArn": str,
        "associatedPortalArns": NotRequired[List[str]],
        "securityGroupIds": NotRequired[List[str]],
        "subnetIds": NotRequired[List[str]],
        "vpcId": NotRequired[str],
    },
)

PortalSummaryTypeDef = TypedDict(
    "PortalSummaryTypeDef",
    {
        "browserSettingsArn": NotRequired[str],
        "browserType": NotRequired[Literal["Chrome"]],
        "creationDate": NotRequired[datetime],
        "displayName": NotRequired[str],
        "networkSettingsArn": NotRequired[str],
        "portalArn": NotRequired[str],
        "portalEndpoint": NotRequired[str],
        "portalStatus": NotRequired[PortalStatusType],
        "rendererType": NotRequired[Literal["AppStream"]],
        "trustStoreArn": NotRequired[str],
        "userSettingsArn": NotRequired[str],
    },
)

PortalTypeDef = TypedDict(
    "PortalTypeDef",
    {
        "browserSettingsArn": NotRequired[str],
        "browserType": NotRequired[Literal["Chrome"]],
        "creationDate": NotRequired[datetime],
        "displayName": NotRequired[str],
        "networkSettingsArn": NotRequired[str],
        "portalArn": NotRequired[str],
        "portalEndpoint": NotRequired[str],
        "portalStatus": NotRequired[PortalStatusType],
        "rendererType": NotRequired[Literal["AppStream"]],
        "statusReason": NotRequired[str],
        "trustStoreArn": NotRequired[str],
        "userSettingsArn": NotRequired[str],
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

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence["TagTypeDef"],
        "clientToken": NotRequired[str],
    },
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TrustStoreSummaryTypeDef = TypedDict(
    "TrustStoreSummaryTypeDef",
    {
        "trustStoreArn": NotRequired[str],
    },
)

TrustStoreTypeDef = TypedDict(
    "TrustStoreTypeDef",
    {
        "associatedPortalArns": NotRequired[List[str]],
        "trustStoreArn": NotRequired[str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

UpdateBrowserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateBrowserSettingsRequestRequestTypeDef",
    {
        "browserSettingsArn": str,
        "browserPolicy": NotRequired[str],
        "clientToken": NotRequired[str],
    },
)

UpdateBrowserSettingsResponseTypeDef = TypedDict(
    "UpdateBrowserSettingsResponseTypeDef",
    {
        "browserSettings": "BrowserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateIdentityProviderRequestRequestTypeDef = TypedDict(
    "UpdateIdentityProviderRequestRequestTypeDef",
    {
        "identityProviderArn": str,
        "clientToken": NotRequired[str],
        "identityProviderDetails": NotRequired[Mapping[str, str]],
        "identityProviderName": NotRequired[str],
        "identityProviderType": NotRequired[IdentityProviderTypeType],
    },
)

UpdateIdentityProviderResponseTypeDef = TypedDict(
    "UpdateIdentityProviderResponseTypeDef",
    {
        "identityProvider": "IdentityProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateNetworkSettingsRequestRequestTypeDef = TypedDict(
    "UpdateNetworkSettingsRequestRequestTypeDef",
    {
        "networkSettingsArn": str,
        "clientToken": NotRequired[str],
        "securityGroupIds": NotRequired[Sequence[str]],
        "subnetIds": NotRequired[Sequence[str]],
        "vpcId": NotRequired[str],
    },
)

UpdateNetworkSettingsResponseTypeDef = TypedDict(
    "UpdateNetworkSettingsResponseTypeDef",
    {
        "networkSettings": "NetworkSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdatePortalRequestRequestTypeDef = TypedDict(
    "UpdatePortalRequestRequestTypeDef",
    {
        "portalArn": str,
        "displayName": NotRequired[str],
    },
)

UpdatePortalResponseTypeDef = TypedDict(
    "UpdatePortalResponseTypeDef",
    {
        "portal": "PortalTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateTrustStoreRequestRequestTypeDef = TypedDict(
    "UpdateTrustStoreRequestRequestTypeDef",
    {
        "trustStoreArn": str,
        "certificatesToAdd": NotRequired[Sequence[Union[bytes, IO[bytes], StreamingBody]]],
        "certificatesToDelete": NotRequired[Sequence[str]],
        "clientToken": NotRequired[str],
    },
)

UpdateTrustStoreResponseTypeDef = TypedDict(
    "UpdateTrustStoreResponseTypeDef",
    {
        "trustStoreArn": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateUserSettingsRequestRequestTypeDef = TypedDict(
    "UpdateUserSettingsRequestRequestTypeDef",
    {
        "userSettingsArn": str,
        "clientToken": NotRequired[str],
        "copyAllowed": NotRequired[EnabledTypeType],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
    },
)

UpdateUserSettingsResponseTypeDef = TypedDict(
    "UpdateUserSettingsResponseTypeDef",
    {
        "userSettings": "UserSettingsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserSettingsSummaryTypeDef = TypedDict(
    "UserSettingsSummaryTypeDef",
    {
        "copyAllowed": NotRequired[EnabledTypeType],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
        "userSettingsArn": NotRequired[str],
    },
)

UserSettingsTypeDef = TypedDict(
    "UserSettingsTypeDef",
    {
        "userSettingsArn": str,
        "associatedPortalArns": NotRequired[List[str]],
        "copyAllowed": NotRequired[EnabledTypeType],
        "downloadAllowed": NotRequired[EnabledTypeType],
        "pasteAllowed": NotRequired[EnabledTypeType],
        "printAllowed": NotRequired[EnabledTypeType],
        "uploadAllowed": NotRequired[EnabledTypeType],
    },
)
