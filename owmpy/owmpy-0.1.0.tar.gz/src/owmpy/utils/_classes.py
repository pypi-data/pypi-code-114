from typing import Any
import aiohttp


class _AutomaticClient:
    client: aiohttp.ClientSession
    appid: str | None

    def __init__(self, client: aiohttp.ClientSession | None = None, appid: str | None = None) -> None:
        self.client = client or aiohttp.ClientSession()
        self.appid = appid or None

    async def __aenter__(self, *args):
        return self

    async def __aexit__(self, *args):
        await self.client.close()
        return self
