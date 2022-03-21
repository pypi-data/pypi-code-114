# Copyright 2022 Ryo H
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Enumeration module."""

from enum import Enum


class BaseEnum(Enum):
    """Base class for enumeration."""

    def __str__(self):
        """__str__ method."""
        return self.value[1]

    def to_value(self) -> int:
        """Convert this object to integer type variable.

        :return: integer type variable
        """
        return self.value[0]

    @classmethod
    def value_of(cls, value: int):
        """Create instance matching the specified integer value.

        :param value: integer type variable
        :raises ValueError: when cannot create instance
        :return: this class instance
        """
        for priority in cls:
            if priority.value[0] == value:
                return priority
        raise ValueError(f"Invalid value. value: {value}")


class Priority(BaseEnum):
    """Priority class."""

    HIGH = (2, "High")
    NORMAL = (3, "Normal")
    LOW = (4, "Low")


class Resolution(BaseEnum):
    """Resolution class."""

    FIXED = (0, "Fixed")
    WONT_FIX = (1, "Won't Fix")
    INVALID = (2, "Invalid")
    DUPLICATION = (3, "Duplication")
    CANNOT_REPRODUCE = (4, "Cannot Reproduce")
