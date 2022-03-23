import logging
from typing import Any, Optional, Union
import aiohttp

from rmlab_errors import (
    ExpiredTokenError,
    ValueError,
)

from rmlab_http_client.types import (
    AuthType,
    Endpoint,
)

from rmlab_http_client.client._core import (
    _HTTPClientBase,
    HTTPClientApiKey,
    HTTPClientBasic,
    HTTPClientJWT,
    HTTPClientPublic,
)


class HTTPClientJWTExpirable:
    """HTTP Client context requring jwt auth, recovers at expiration given a refresh token"""

    def __init__(
        self,
        endpoint: Endpoint,
        address: str,
        *,
        access_jwt: str,
        refresh_address: str,
        refresh_endpoint: Endpoint,
        refresh_jwt: str,
    ):
        """Initializes instance.

        Args:
            address (str): Resource endpoint behind the access token
            access_jwt (str): Access token
            refresh_address (str): Address to submit the token refresh request
            refresh_jwt (str): Refresh token
        """

        self._access_endpoint = endpoint
        self._access_jwt = access_jwt

        self._request_address = address
        self._refresh_address = refresh_address
        self._refresh_jwt = refresh_jwt
        self._retry = False

        self._refresh_endpoint = refresh_endpoint

    async def __aenter__(self):
        """Initializes asynchronous context manager for resources behind expiration-aware JWT auth.

        Returns:
            HTTPClientJWTExpirable: This client instance.
        """

        self._retry = True

        return self

    async def __aexit__(self, exc_ty, exc_val, tb):

        if exc_ty is not None:
            logging.error(
                f"HTTPClientJWTExpirable context manager got error {exc_ty}. Re-raising"
            )
            # Return None or False => re-raise
        else:
            return True

    async def submit_request(
        self, data: Optional[Union[aiohttp.FormData, dict]] = None
    ) -> Any:
        """Submit requests resilient to access token expiration.

        Args:
            data (Optional[Union[aiohttp.FormData, dict]], optional): Data payload. Defaults to None.

        Returns:
            Any: Response data payload or None
        """

        while self._retry:

            try:

                # We won't retry unless a ExpiredTokenError is raised
                if self._retry:
                    self._retry = False

                async with SyncClient(
                    self._access_endpoint,
                    address=self._request_address,
                    access_jwt=self._access_jwt,
                ) as access_client:

                    return await access_client.submit_request(data)

            except ExpiredTokenError:

                async with SyncClient(
                    self._refresh_endpoint,
                    address=self._refresh_address,
                    access_jwt=self._refresh_jwt,
                ) as refresh_client:

                    auth_resp = await refresh_client.submit_request()

                # Re-set credentials
                self._refresh_jwt = auth_resp["refresh_token"]
                self._access_jwt = auth_resp["access_token"]

                self._retry = True


def SyncClient(
    endpoint: Endpoint,
    *,
    address: str,
    basic_auth: Optional[str] = None,
    api_key: Optional[str] = None,
    access_jwt: Optional[str] = None,
    refresh_jwt: Optional[str] = None,
    refresh_address: Optional[str] = None,
    refresh_endpoint: Optional[Endpoint] = None,
) -> _HTTPClientBase:
    """Creates a context for a synchronous HTTP client.

    Args:
        endpoint (Endpoint): Endpoint instance.
        address (str): Base address.
        basic_auth (Optional[str], optional): Basic auth data, required if endpoint.auth is BASIC. Defaults to None.
        api_key (Optional[str], optional): Api key auth data, required if endpoint.auth is APIKEY. Defaults to None.
        access_jwt (Optional[str], optional): Access jwt data, required if endpoint.auth is JWT. Defaults to None.
        refresh_jwt (Optional[str], optional): Refresh jwt data, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.
        refresh_address (Optional[str], optional): Address for token refresh, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.
        refresh_endpoint (Optional[List[str]], optional): Resource for token refresh, required if endpoint.auth is JWT_EXPIRABLE. Defaults to None.

    Raises:
        ValueError: If any argument dependent on endpoint.auth is not passed

    Returns:
        HTTPClientBase: A synchronous http client context.
    """

    if endpoint.auth == AuthType.PUBLIC:

        return HTTPClientPublic(endpoint=endpoint, address=address)

    elif endpoint.auth == AuthType.BASIC:

        if basic_auth is None:
            raise ValueError(f"Require `basic_auth` for endpoint")

        return HTTPClientBasic(endpoint=endpoint, address=address, auth_data=basic_auth)

    elif endpoint.auth == AuthType.APIKEY:

        if api_key is None:
            raise ValueError(f"Require `api_key` for endpoint")

        return HTTPClientApiKey(endpoint=endpoint, address=address, api_key=api_key)

    elif endpoint.auth == AuthType.JWT:

        if access_jwt is None:
            raise ValueError(f"Require `access_jwt` for endpoint")

        return HTTPClientJWT(
            endpoint=endpoint,
            address=address,
            jwt=access_jwt,
        )

    elif endpoint.auth == AuthType.JWT_EXPIRABLE:

        if access_jwt is None:
            raise ValueError(f"Require `acccess_jwt` for endpoint")
        if refresh_jwt is None:
            raise ValueError(f"Require `refresh_jwt` for endpoint")
        if refresh_address is None:
            raise ValueError(f"Require `refresh_address` for endpoint")
        if refresh_endpoint is None:
            raise ValueError(f"Require `refresh_endpoint` for endpoint")

        endpoint_as_jwt = Endpoint(
            id=endpoint.id,
            resource=endpoint.resource,
            method=endpoint.method,
            payload=endpoint.payload,
            auth=AuthType.JWT,
            communication=endpoint.communication,
            response=endpoint.response,
            arguments=endpoint.arguments,
        )

        return HTTPClientJWTExpirable(
            endpoint=endpoint_as_jwt,
            address=address,
            access_jwt=access_jwt,
            refresh_jwt=refresh_jwt,
            refresh_address=refresh_address,
            refresh_endpoint=refresh_endpoint,
        )

    else:

        raise ValueError(f"Unhandled auth type `{endpoint.auth}`")
