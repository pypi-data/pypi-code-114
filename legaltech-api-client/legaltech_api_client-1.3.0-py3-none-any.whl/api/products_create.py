from typing import Any, Dict, Optional, Union, cast

import httpx

from legaltech_api_client.client import Client
from legaltech_api_client.models.create_product_request import CreateProductRequest
from legaltech_api_client.models.create_product_response import CreateProductResponse
from legaltech_api_client.types import Response


def _get_kwargs(
    *,
    client: Client,
    data: CreateProductRequest,
    authorization: str,
) -> Dict[str, Any]:
    url = "{}/api/v1/products/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    headers["Authorization"] = authorization

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateProductResponse]]:
    if response.status_code == 200:
        response_200 = CreateProductResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateProductResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    data: CreateProductRequest,
    authorization: str,
) -> Response[Union[Any, CreateProductResponse]]:
    """Create new Product.

    Args:
        client (Client):
        data (CreateProductRequest):
        authorization (str):

    Returns:
        Response[Union[Any, CreateProductResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        data=data,
        authorization=authorization,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    data: CreateProductRequest,
    authorization: str,
) -> Optional[Union[Any, CreateProductResponse]]:
    """Create new Product.

    Args:
        client (Client):
        data (CreateProductRequest):
        authorization (str):

    Returns:
        Response[Union[Any, CreateProductResponse]]
    """

    return sync_detailed(
        client=client,
        data=data,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    data: CreateProductRequest,
    authorization: str,
) -> Response[Union[Any, CreateProductResponse]]:
    """Create new Product.

    Args:
        client (Client):
        data (CreateProductRequest):
        authorization (str):

    Returns:
        Response[Union[Any, CreateProductResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        data=data,
        authorization=authorization,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    data: CreateProductRequest,
    authorization: str,
) -> Optional[Union[Any, CreateProductResponse]]:
    """Create new Product.

    Args:
        client (Client):
        data (CreateProductRequest):
        authorization (str):

    Returns:
        Response[Union[Any, CreateProductResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            data=data,
            authorization=authorization,
        )
    ).parsed
