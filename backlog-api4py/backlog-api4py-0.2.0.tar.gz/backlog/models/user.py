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

"""User module."""

from dataclasses import dataclass
from typing import Optional

from .base import Base


@dataclass
class NulabAccount(Base):
    """Nulab Account class."""

    nulab_id: str
    name: str
    unique_id: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nulab_id=data["nulabId"],
            name=data["name"],
            unique_id=data["uniqueId"],
        )


@dataclass
class User(Base):
    """User class."""

    id: int
    user_id: Optional[str]
    name: str
    role_type: int
    lang: Optional[str]
    mail_address: str
    nulab_account: Optional[NulabAccount]
    keyword: str

    @classmethod
    def from_dict(cls, data: dict):
        nulab_account = NulabAccount.from_dict(
            data["nulabAccount"]) if data["nulabAccount"] else None

        return cls(
            id=data["id"],
            user_id=data["userId"],
            name=data["name"],
            role_type=data["roleType"],
            lang=data["lang"],
            mail_address=data["mailAddress"],
            nulab_account=nulab_account,
            keyword=data["keyword"],
        )
