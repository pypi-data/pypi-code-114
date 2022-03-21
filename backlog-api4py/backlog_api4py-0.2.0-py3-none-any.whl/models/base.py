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

"""Base model module."""

import json
from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import Any, Dict


class Base(metaclass=ABCMeta):

    _DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%SZ"

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> "Base":
        """Create instance from dictionary type variable.

        :param data: dictionary type variable
        :return: this class instance
        """
        raise NotImplementedError

    def to_json_string(self) -> str:
        """Convert this object to JSON string.

        :return: JSON string
        """
        return json.dumps(
            self.to_dict(),
            ensure_ascii=False,
            default=self._convert_value)

    def to_dict(self) -> Dict[str, Any]:
        """Convert this object to dictionary type variable.

        :return: dictionary type variable
        """
        data: Dict[str, Any] = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, tuple, set)):
                data[key] = []
                for item in value:
                    if hasattr(item, "to_dict"):
                        data[key].append(item.to_dict())
                    else:
                        data[key].append(item)
            elif hasattr(value, "to_dict"):
                data[key] = value.to_dict()
            elif value is not None:
                data[key] = value

        return data

    def _convert_value(self, value):
        """Convert data type that cannot be processed by json.dumps().

        :param value: data to be converted
        :raises TypeError: when cannot convert data type
        :return: converted data
        """
        if isinstance(value, datetime):
            return value.strftime(self._DATETIME_FORMAT)
        raise TypeError(f"data cannot be converted. value: {repr(value)}")
