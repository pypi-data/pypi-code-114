import json
import random

import aiohttp

from .exceptions import ClosedSessionError, ContentUnavailable, InvalidEndpointError


class _BaseClient:
    """Base API client class and methods"""

    def __init__(self, *, session: aiohttp.ClientSession) -> None:
        self._URL = "https://holyshit.wtf/"
        self._VALID_ENDPOINTS = (
            "insults",
            "8ball",
            "sixdigit",
            "pickuplines",
            "wave",
            "hug",
            "kiss",
            "cuddle",
            "slap",
            "kill",
            "lick",
            "headpat",
            "highfive",
            "bite",
            "punch",
            "pout",
            "poke",
            "stare",
            "tickle",
        )
        self._session = session
        self._session_owner = False  # Indicates whether the client was initialised by the create classmethod

    @classmethod
    def create(cls):
        """Create a client without an existing aiohttp session"""
        _session = aiohttp.ClientSession()
        inst = cls(session=_session)
        inst._session_owner = True
        return inst

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        return await self.close()

    async def _get_response(self, path: str) -> str:
        """Get a response from the API"""
        if self._session is not None and getattr(self._session, "closed", True):
            raise ClosedSessionError("Cannot operate on a closed session")
        elif path not in self._VALID_ENDPOINTS:
            raise InvalidEndpointError(f"Endpoint must be one of {self._VALID_ENDPOINTS}, got {path}")

        try:
            async with self._session.get(f"{self._URL}/{path}") as r:
                content = await r.text()
                if isinstance(data := json.loads(content, strict=False).get("response"), str):
                    return data.strip()
                else:
                    raise ContentUnavailable("The endpoint you're trying to access has returned an invalid response")
        except Exception as e:
            raise ContentUnavailable("Failed to fetch content from endpoint") from e

    async def _get_gif(self, path: str) -> str:
        """Fetch a GIF URL response from the API"""
        return await self._get_response(f"gifs/{path}")

    async def close(self) -> None:
        """Close the client's HTTP session if created by the create classmethod"""
        if getattr(self._session, "closed", True) == False and self._session_owner:
            return await self._session.close()


class Client(_BaseClient):
    """Client class with methods for interacting with API endpoints"""

    async def eightball(self) -> str:
        """Get a random Magic 8-Ball response"""
        return await self._get_response("8ball")

    async def insult(self) -> str:
        """Get a random 1-word insult"""
        return await self._get_response("insults")

    async def sixdigit(self) -> int:
        """Get a random 6-digit number"""
        return int(await self._get_response("6digit"))

    async def pickupline(self) -> str:
        """Get a random pickup line"""
        return await self._get_response("pickuplines")

    async def bite(self) -> str:
        """Get a random URL to a bite GIF"""
        return await self._get_gif("bite")

    async def cuddle(self) -> str:
        """Get a random URL to a cuddle GIF"""
        return await self._get_gif("cuddle")

    async def headpat(self) -> str:
        """Get a random URL to a headpat GIF"""
        return await self._get_gif("headpat")

    async def highfive(self) -> str:
        """Get a random URL to a high five GIF"""
        return await self._get_gif("highfive")

    async def hug(self) -> str:
        """Get a random URL to a hug GIF"""
        return await self._get_gif("hug")

    async def kick(self) -> str:
        """Get a random URL to a kick GIF"""
        return await self._get_gif("kick")

    async def kill(self):
        """Get a random URL to a kill GIF"""
        return await self._get_gif("kill")

    async def kiss(self) -> str:
        """Get a random URL to a kiss GIF"""
        return await self._get_gif("kiss")

    async def lick(self) -> str:
        """Get a random URL to a lick GIF"""
        return await self._get_gif("lick")

    async def poke(self) -> str:
        """Get a random URL to a poke GIF"""
        return await self._get_gif("poke")

    async def pout(self) -> str:
        """Get a random URL to a pout GIF"""
        return await self._get_gif("pout")

    async def punch(self) -> str:
        """Get a random URL to a punch GIF"""
        return await self._get_gif("punch")

    async def slap(self) -> str:
        """Get a random URL to a slap GIF"""
        return await self._get_gif("slap")

    async def stare(self) -> str:
        """Get a random URL to a stare GIF"""
        return await self._get_gif("stare")

    async def tickle(self) -> str:
        """Get a random URL to a tickle GIF"""
        return await self._get_gif("tickle")

    async def wave(self) -> str:
        """Get a random URL to a wave GIF"""
        return await self._get_gif("wave")

    async def random_gif(self) -> str:
        """Get a random GIF URL"""
        return await self._get_gif(random.choice(self._VALID_ENDPOINTS[4:]))
