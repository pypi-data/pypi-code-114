from aiohttp import ClientSession
from asyncio import get_event_loop, sleep, get_running_loop
from .gateway import DiscordGateway
from .errors import ApiError
import asyncio
try:
    import ujson as json
except ImportError:
    import json

class HttpClient:
    def __init__(self, *, token: str=None,
                 loop=None, log: bool=False):
        self.token = token
        self.log = log
        self.baseurl = "https://discord.com/api/v10"
        self.loop = loop
        self.ws = None
        self.session = ClientSession(loop=loop,
                                     json_serialize=json.dumps)
        
    async def __aenter__(self):
        self.loop = get_running_loop()
        return self
    
    async def __aexit__(self, *args, **kwargs):
        if self.session is not None:
            await self.session.close()

    def print(self, name, content):
        if self.log is True:
            print(f"[{name}]:{content}")
            
    async def json_or_text(self, r):
        if r.headers["Content-Type"] == "application/json":
            return await r.json()
        
    async def ws_connect(self, url):
        return await self.session.ws_connect(url)
    
    async def login(self):
        return await self.request("GET", "/users/@me")
    
    def get(self, path: str, *args, **kwargs):
        return self.request("GET", path, *args, **kwargs)
    
    def post(self, path: str, *args, **kwargs):
        return self.request("POST", *args, **kwargs)
    
    def delete(self, path: str, *args, **kwargs):
        return self.request("DELETE", path, *args, **kwargs)
    
    def patch(self, path: str, *args, **kwargs):
        return self.request("PATCH", path, *args, **kwargs)
    
    async def request(self, method: str, path: str, *args, **kwargs):
        headers = {
            "Authorization": f"Bot {self.token}"
        }
        if kwargs.get("json"):
            headers["Content-Type"] = "application/json"
        kwargs["headers"] = headers
        for t in range(5):
            async with self.session.request(method, self.baseurl + path, *args, **kwargs) as r:
                if r.status == 429:
                    if r.headers.get("X-RateLimit-Global"):
                        raise ApiError("Now api is limit. Wait a minute please.")
                    else:
                        await sleep(int(r.headers["X-RateLimit-Reset-After"]))
                elif r.status == 404:
                    raise ApiError("Not Found Error")
                elif 300 > r.status >= 200:
                    return await self.json_or_text(r)
