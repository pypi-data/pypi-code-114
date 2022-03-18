import json
import time
import discord
import logging
import asyncio

from . import errors
from datetime import datetime
from aiohttp import ClientSession, ClientResponse
from asyncio import get_event_loop_policy, AbstractEventLoop
from typing import Optional, Union


class Client:
    """
    API wrapper for discordextremelist.xyz
    """
    def __init__(self, bot: discord.Client = None, token: str = None, *, baseurl: str = "https://api.discordextremelist.xyz/v2/", loop: AbstractEventLoop = None):
        self.bot: Optional[discord.Client] = bot
        self.token: Optional[str] = token
        self.baseurl: str = baseurl
        self.session: ClientSession = ClientSession(loop=loop or get_event_loop_policy().get_event_loop())

        # Logger
        self.logger: logging.Logger = logging.getLogger("del.py")

        # Loop
        self._loop_task: Optional[asyncio.Task] = None
        self.hit_ratelimit: bool = False

    def start_loop(self, wait_for: int = 1800) -> Union[errors.InvalidTime, None]:
        """
        Start the loop for stats posting
        """

        if wait_for < 30:
            raise errors.InvalidTime("The minimum interval between each post should be at least 30 seconds.")

        self._loop_task = self.bot.loop.create_task(self.__loop(wait_for=wait_for))

    async def __loop(self, wait_for: int) -> None:  # default is 30 minutes
        """
        The stat posting loop for Discord Extreme List API

        :param wait_for: Time interval between each post request in seconds. Minimum is 30 seconds
        """

        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            try:
                await self.post_stats(len(self.bot.guilds), len(self.bot.shards))
                self.logger.info(f"Successfully posted stats to the API ({len(self.bot.guilds)} Guild(s) & {len(self.bot.shards)} Shard(s))")
            except Exception as e:
                self.logger.error(f"Failed to post stats to the API: {e}")

            await asyncio.sleep(wait_for)

    def close_loop(self) -> None:
        """ Closes the loop safely """

        self._loop_task.cancel()

    async def ratelimit(self, response: ClientResponse) -> None:
        self.logger.warning("You have hit the ratelimit, will wait out so you wouldn't *hopefully* get api banned.")
        try:
            time = (datetime.utcfromtimestamp(int(response.headers.get("X-Ratelimit-Reset")) / 1000) - datetime.utcnow()).total_seconds()
            await asyncio.sleep(time)
        except (ValueError, TypeError):
            await asyncio.sleep(30)
        self.hit_ratelimit = False
        self.logger.info("Waited out the time, continuing to interact with the API")

    async def _response(self, response: ClientResponse) -> Union[errors.HTTPException, None]:
        if 500 % (response.status + 1) == 500:
            raise errors.HTTPException(raised_error="Discord Extreme List server error occured while posting the stats", status=response.status)
        elif response.status == 403:
            resp = json.loads(await response.text())
            raise errors.HTTPException(raised_error=resp["message"], status=response.status)
        elif response.status != 200:
            raise errors.HTTPException(raised_error="Discord Extreme List server responded with status that isn't 200 OK", status=response.status)
        else:
            ratelimit_header = response.headers.get("X-RateLimit-Remaining", None)
            if ratelimit_header and int(ratelimit_header) <= 2:  # 2 to be safe
                self.hit_ratelimit = True

    async def post_stats(self, guildCount: int, shardCount: int = None) -> Union[Optional[errors.HTTPException, errors.Unauthorized]]:
        """
        Post bot statistics to the API

        :param guildCount: Server count
        :param shardCount: Shard count (optional)
        """

        head = {"Authorization": self.token, "Content-Type": 'application/json'}
        if not self.token:
            raise errors.Unauthorized("The token is either invalid or missing.")

        to_post = json.dumps({'guildCount': guildCount, 'shardCount': shardCount})
        if not shardCount:
            to_post = json.dumps({'guildCount': guildCount})
        r = await self.session.post(self.baseurl + "bot/{0}/stats".format(self.bot.user.id), headers=head, data=to_post)
        await self._response(r)

        if self.hit_ratelimit:
            await self.ratelimit(response=r)

        result = json.loads(await r.text())
        if result['error']:
            raise errors.HTTPException(raised_error=result)
        else:
            self.logger.info(f"Successfully posted stats to the API ({len(self.bot.guilds)} Guild(s) & {len(self.bot.shards)} Shard(s))")

    async def get_website_stats(self) -> Union[errors.HTTPException, dict]:
        """
        Get website statistics

        :return WebsiteStats: Website statistics
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "stats")
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data

    async def get_website_health(self) -> Union[errors.HTTPException, dict]:
        """
        Get website health

        :return WebsiteHealth: Website health
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "health")
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data

    async def get_bot_info(self, botid: int) -> Union[errors.HTTPException, dict]:
        """
        Get a bot listed on discordextremelist.xyz

        :param botid: Bot to be fetched
        :return Bot: Bot that was fetched
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "bot/{0}".format(botid))
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data

    async def get_server_info(self, serverid: int) -> Union[errors.HTTPException, dict]:
        """
        Get a server listed on discordextremelist.xyz

        :param serverid: Server to be fetched
        :return Server: Server that was fetched
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "server/{0}".format(serverid))
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data

    async def get_template_info(self, templateid: str) -> Union[errors.HTTPException, dict]:
        """
        Get a template listed on discordextremelist.xyz

        :param templateid: Template to be fetched
        :return Template: Template that was fetched
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "template/{0}".format(templateid))
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data

    async def get_user_info(self, userid: str) -> Union[errors.HTTPException, dict]:
        """
        Get a registered user on discordextremelist.xyz

        :param userid: User to be fetched
        :return User: User that was fetched
        """

        start_time = time.time()
        r = await self.session.get(self.baseurl + "user/{0}".format(userid))
        await self._response(r)

        data = await r.json()
        if data['error']:
            raise errors.HTTPException(raised_error=data)

        data['time_taken'] = (time.time() - start_time) * 1000
        return data
