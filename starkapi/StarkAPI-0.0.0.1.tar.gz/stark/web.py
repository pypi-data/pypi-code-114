# StarkAPI - Python wrapper around Stark API
# Copyright (C) 2022 Stark Bots <https://github.com/StarkBotsIndustries>
#
# This file is part of StarkAPI Python Library.
#
# StarkAPI is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# StarkAPI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with StarkAPI. If not, see <https://www.gnu.org/licenses/>.

"""
Module with easy-to-use functions to interact with the API asynchronously
"""

import httpx
from .exceptions import (
    HTTPError,
    TooLargeNumber,
    UnknownException,
    UnsupportedType,
    NotANumber
)
base_url = "https://stark-api.vercel.app"
supported_flirt_types = ["funny", "cheesy", "cute", "dirty", "tinder", "mix"]


async def request(endpoint: str) -> (bool, dict[str, str]):
    async with httpx.AsyncClient() as client:
        if not endpoint.startswith("/"):
            endpoint = "/"+endpoint
        client: httpx.AsyncClient
        url = base_url + endpoint
        response = await client.get(url)
        if not response.is_success:
            raise HTTPError(response)
        data: dict[str, str] = response.json()
        if not data["error"]:
            return True, data
        else:
            return False, data


async def raise_accordingly(err: str):
    if "unsupported type" in err.lower():
        raise UnsupportedType(err)
    elif "pass a number" in err.lower():
        raise NotANumber(err)
    elif "should lie" in err.lower():
        raise TooLargeNumber(err)
    else:
        raise UnknownException(err)
