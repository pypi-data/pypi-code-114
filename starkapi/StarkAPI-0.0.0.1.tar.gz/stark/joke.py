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
Wrapper around the Joke API of Stark API

Classes:
    Joke: Main class to interact with Joke API
    JokeObject: Returned object for some methods of class Flirt
"""

from .web import request, raise_accordingly


class JokeObject:
    """A joke object with the joke id and joke string"""

    def __init__(self):
        self._id = 0
        self._joke = ""

    @property
    def id(self) -> int:
        """ID of the joke string"""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def joke(self) -> str:
        """Joke string"""
        return self._joke

    @joke.setter
    def joke(self, value: str):
        self._joke = value


class Joke:
    endpoint = "/joke"

    async def random(self) -> JokeObject:
        """Get a random joke from Stark API

        Returns:
            JokeObject: a joke object with the joke id and joke string
        """
        success, result = await request(self.endpoint)
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            obj = JokeObject()
            obj.id = result["id"]
            obj.joke = result["joke"]
            return obj

    async def count(self) -> int:
        """Get total number of jokes in Stark API

        Returns:
            total_count (int): Jokes Count
        """
        success, result = await request(self.endpoint+"/count")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            return result["count"]

    async def get_joke(self, n: int) -> JokeObject:
        """Get nth joke of Stark API by passing an integer n

        Parameters:
            n (int): ID of the joke to get.

        Returns:
            JokeObject: a joke object with the joke id and joke string

        Raises:

        """
        success, result = await request(self.endpoint+f"/{n}")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            obj = JokeObject()
            obj.joke = result["joke"]
            obj.id = result["id"]
            return obj
