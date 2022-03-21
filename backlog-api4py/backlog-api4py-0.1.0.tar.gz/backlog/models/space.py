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

"""Space module."""

from dataclasses import dataclass
from datetime import datetime

from .base import Base


@dataclass
class Space(Base):
    """Space class."""

    space_key: str
    name: str
    owner_id: int
    lang: str
    timezone: str
    report_send_time: str
    text_formatting_rule: str
    created: datetime
    updated: datetime

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            space_key=data["spaceKey"],
            name=data["name"],
            owner_id=data["ownerId"],
            lang=data["lang"],
            timezone=data["timezone"],
            report_send_time=data["reportSendTime"],
            text_formatting_rule=data["textFormattingRule"],
            created=datetime.strptime(data["created"], cls._DATETIME_FORMAT),
            updated=datetime.strptime(data["updated"], cls._DATETIME_FORMAT),
        )
