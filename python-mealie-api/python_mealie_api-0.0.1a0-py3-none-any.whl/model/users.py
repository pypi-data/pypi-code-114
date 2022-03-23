from __future__ import annotations

from .common import Base, User
from .recipe import RecipeResponse


class Token(Base):
    name: str | None
    id: int | None


class UserResponse(User):
    id: int
    tokens: list[Token]


class UserWithFavorites(User):
    favoriteRecipes: list[RecipeResponse]


class UpdatePasswordRequest(Base):
    current_password: str
    new_password: str
