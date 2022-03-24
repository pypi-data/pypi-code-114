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
Exceptions occurred while interacting with Stark API

Classes:
    TooLargeNumber: Raised if the number is larger than the maximum id
    HTTPError: Raised if HTTP Request to the API fails.
    UnsupportedType: Raised if the requested type is not supported by the API.
    NotANumber: Raised if the requested id is not a valid number
    UnknownException: Raised if there is an unknown exception from Stark API
"""


class UnknownException(Exception):
    """Raised if there is an unknown exception from Stark API"""
    pass


class TooLargeNumber(Exception):
    """Raised if the number is larger than the maximum id"""
    pass


class HTTPError(Exception):
    """Raised if HTTP Request to the API fails"""

    pass


class UnsupportedType(Exception):
    """Raised if the requested type is not supported by the API"""

    pass


class NotANumber(Exception):
    """Raised if the requested id is not a valid number"""

    pass
