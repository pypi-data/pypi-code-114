"""
Type annotations for sso-oidc service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenRequestRequestTypeDef

    data: CreateTokenRequestRequestTypeDef = {...}
    ```
"""
import sys
from typing import Dict, Sequence

from typing_extensions import NotRequired

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateTokenRequestRequestTypeDef",
    "CreateTokenResponseTypeDef",
    "RegisterClientRequestRequestTypeDef",
    "RegisterClientResponseTypeDef",
    "ResponseMetadataTypeDef",
    "StartDeviceAuthorizationRequestRequestTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)

CreateTokenRequestRequestTypeDef = TypedDict(
    "CreateTokenRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "grantType": str,
        "deviceCode": str,
        "code": NotRequired[str],
        "refreshToken": NotRequired[str],
        "scope": NotRequired[Sequence[str]],
        "redirectUri": NotRequired[str],
    },
)

CreateTokenResponseTypeDef = TypedDict(
    "CreateTokenResponseTypeDef",
    {
        "accessToken": str,
        "tokenType": str,
        "expiresIn": int,
        "refreshToken": str,
        "idToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterClientRequestRequestTypeDef = TypedDict(
    "RegisterClientRequestRequestTypeDef",
    {
        "clientName": str,
        "clientType": str,
        "scopes": NotRequired[Sequence[str]],
    },
)

RegisterClientResponseTypeDef = TypedDict(
    "RegisterClientResponseTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "clientIdIssuedAt": int,
        "clientSecretExpiresAt": int,
        "authorizationEndpoint": str,
        "tokenEndpoint": str,
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

StartDeviceAuthorizationRequestRequestTypeDef = TypedDict(
    "StartDeviceAuthorizationRequestRequestTypeDef",
    {
        "clientId": str,
        "clientSecret": str,
        "startUrl": str,
    },
)

StartDeviceAuthorizationResponseTypeDef = TypedDict(
    "StartDeviceAuthorizationResponseTypeDef",
    {
        "deviceCode": str,
        "userCode": str,
        "verificationUri": str,
        "verificationUriComplete": str,
        "expiresIn": int,
        "interval": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
