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
Wrapper around the Flirt API of Stark API

Classes:
    Flirt: Main class to interact with Flirt API
    FlirtObject: Returned object for some methods of class Flirt
"""

from .web import request, raise_accordingly


class FlirtObject:
    """A flirt object with the flirt id and flirt string"""

    def __init__(self):
        self._id = 0
        self._line = ""
        self._type = ""

    @property
    def id(self) -> int:
        """ID of the flirt line"""
        return self._id

    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def line(self) -> str:
        """Flirt line"""
        return self._line

    @line.setter
    def line(self, value: str):
        self._line = value

    @property
    def type(self) -> str:
        """Flirt type"""
        return self._type

    @type.setter
    def type(self, value: str):
        self._type = value


class Flirt:
    endpoint = "/flirt"

    async def random(self) -> FlirtObject:
        """Get a random flirt line from Stark API

        Returns:
            FlirtObject: A flirt object with the flirt id, flirt string and flirt type.
        """
        success, result = await request(self.endpoint)
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            obj = FlirtObject()
            obj.id = result["id"]
            obj.line = result["line"]
            obj.type = result["type"]
            return obj

    async def types(self) -> list[str]:
        """Get list of available types of Flirt API from Stark API

        Returns:
            list: A list of supported types.
        """
        success, result = await request(self.endpoint + "/types")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            ans: list[str] = result["types"]
            return ans

    async def random_of_type(self, type: str) -> FlirtObject:
        """Get a random flirt line of specified type from Stark API

        Returns:
            FlirtObject: A flirt object with the flirt id, flirt string and flirt type.
        """
        success, result = await request(self.endpoint + f"/{type}")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            obj = FlirtObject()
            obj.id = result["id"]
            obj.line = result["line"]
            obj.type = result["type"]
            return obj

    async def count(self) -> int:
        """Get total number of flirt lines in Stark API

        Returns:
            total_count (int): Flirt lines Count
        """
        success, result = await request(self.endpoint+"/count")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            return result["count"]

    async def get_flirt_line(self, n: int) -> FlirtObject:
        """Get nth flirt line of Stark API by passing an integer n

        Parameters:
            n (int): ID of the flirt line to get.

        Returns:
            FlirtObject: A flirt object with the flirt id, flirt string and flirt type
        Raises:

        """
        success, result = await request(self.endpoint+f"/{n}")
        if not success:
            err = result["description"]
            await raise_accordingly(err)
        else:
            obj = FlirtObject()
            obj.id = result["id"]
            obj.line = result["line"]
            obj.type = result["type"]
            return obj
