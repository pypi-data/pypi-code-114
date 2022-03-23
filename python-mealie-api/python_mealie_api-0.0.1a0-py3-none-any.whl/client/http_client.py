from __future__ import annotations

from typing import Mapping

from aiohttp.client import ClientSession
from aiohttp.client_exceptions import ClientError

from ..exception import HttpClientException
from ..model import Response


class HttpClient:
    def __init__(self, client_session: ClientSession) -> None:
        self._client = client_session

    async def get(self, url: str, headers: Mapping[str, str] | None = None) -> Response:
        try:
            async with self._client.get(url=url, headers=headers) as resp:
                status_code = resp.status
                output_data = await resp.json()
                return Response(status_code=status_code, data=output_data)
        except ClientError as error:
            raise HttpClientException() from error

    async def post(
        self,
        url: str,
        headers: Mapping[str, str] | None = None,
        data: Mapping[str, str] | None = None,
    ) -> Response:
        try:
            async with self._client.post(url=url, data=data, headers=headers) as resp:
                status_code = resp.status
                output_data = await resp.json()
                return Response(status_code=status_code, data=output_data)
        except ClientError as error:
            raise HttpClientException() from error

    async def put(
        self,
        url: str,
        headers: Mapping[str, str] | None = None,
        data: Mapping[str, str] | None = None,
    ) -> Response:
        try:
            async with self._client.put(url=url, data=data, headers=headers) as resp:

                status_code = resp.status
                output_data = await resp.json()
                return Response(status_code=status_code, data=output_data)
        except ClientError as error:
            raise HttpClientException() from error

    async def patch(
        self,
        url: str,
        headers: Mapping[str, str] | None = None,
        data: Mapping[str, str] | None = None,
    ) -> Response:
        try:
            async with self._client.patch(url=url, data=data, headers=headers) as resp:

                status_code = resp.status
                output_data = await resp.json()
                return Response(status_code=status_code, data=output_data)
        except ClientError as error:
            raise HttpClientException() from error

    async def delete(
        self,
        url: str,
        headers: Mapping[str, str] | None = None,
    ) -> Response:
        try:
            async with self._client.delete(url=url, headers=headers) as resp:

                status_code = resp.status
                output_data = await resp.json()
                return Response(status_code=status_code, data=output_data)
        except ClientError as error:
            raise HttpClientException() from error
