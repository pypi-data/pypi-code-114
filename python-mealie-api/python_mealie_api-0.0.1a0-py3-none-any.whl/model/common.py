from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, List, Mapping

from pydantic import BaseModel


def to_camel_case(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


class Status(Enum):
    SUCCESS = auto()
    FAILURE = auto()


@dataclass(frozen=True)
class Response:
    status_code: int
    data: Mapping[str, Any] | None

    @property
    def status(self):
        return 400 > self.status_code


class Base(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class Detail(Base):
    loc: list[str]
    msg: str | None
    type: str | None


class ErrorResponse(Base):
    detail: list[Detail]


class User(Base):
    username: str | None
    full_name: str | None
    email: str
    admin: bool
    group: str
    favorite_recipes: List[str]
