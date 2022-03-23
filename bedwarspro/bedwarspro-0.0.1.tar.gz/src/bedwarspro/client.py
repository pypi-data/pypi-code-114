import asyncio
import json
from typing import Optional

import aiohttp

from .errors import *
from .models import *

try:
    import ujson

    JSON_DECODER = ujson.loads
except ImportError:
    JSON_DECODER = json.loads


class Client:
    """Main client object; interact with the API. """

    def __init__(self, key=None, *, loop=None):
        self.loop = asyncio.get_event_loop() if loop is None else loop

        if key is None:
            raise APIError("You must specify an API key.")

        self.key = key

        self._session = aiohttp.ClientSession(loop=self.loop)

    async def __aenter__(self):
        # Open a new session if it has been closed
        if self._session.closed:
            self._session = aiohttp.ClientSession(loop=self.loop)
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._session.close()

    def _run(self, future):
        return self.loop.run_until_complete(future)

    async def _get(
            self,
            path: str,
            *,
            params: Optional[dict] = None,
    ) -> dict:
        params['key'] = self.key
        response = await self._session.get(
            f'https://api.bedwarspro.net/{path}',
            params=params,
        )

        if response.status == 200:
            return await response.json(loads=JSON_DECODER)
        else:
            try:
                text = await response.json(loads=JSON_DECODER)
                text = text.get('cause')
            except Exception:
                raise APIError('An unexpected error occurred with the Bedwars Pro API')
            else:
                raise APIError(f'{text}')

    async def close(self) -> None:
        """Safely close aiohttp session. """
        await self._session.close()

    async def player(self, id=None) -> Player:
        """Create a :class:`Player` object based off an API response."""
        if id is None:
            raise APIError('You must specify a player\'s uuid or name')

        if len(id) > 16:
            params = {"uuid": id}
        else:
            params = {"name": id}

        response = await self._get('player', params=params)

        if not response.get('player'):
            raise APIError(f'Player {id} either does not exist or has not played on Bedwars Pro before')

        data = {
            'raw': response['player'],
        }

        return Player(**data)
