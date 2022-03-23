from __future__ import annotations

from datetime import date, datetime
from typing import Any, Mapping

from .common import Base, User


class RecipeResponse(Base):
    id: int | None
    name: str | None
    slug: str | None
    image: str | None
    description: str | None
    recipe_category: list[str]
    tags: list[str]
    rating: int | None
    date_added: date | None
    date_updated: datetime | None
    recipe_yield: str | None
    recipe_ingredient: list[RecipeIngredient]
    recipe_instructions: list[Any]
    nutrition: Nutrition | None
    tools: list[str]
    total_time: str | None
    prep_time: str | None
    perform_time: str | None
    settings: Setting | None
    assets: list[Asset]
    notes: list[Note]
    org_url: str | None
    extras: Mapping[str, Any] | None
    comments: list[Comment]


class Comment(Base):
    text: str | None
    id: int | None
    uuid: str | None
    recipe_slug: str | None
    date_added: datetime | None
    user: User | None


class Note(Base):
    title: str | None
    text: str | None


class Asset(Base):
    name: str | None
    icon: str | None
    file_name: str | None


class Setting(Base):
    public: bool
    show_nutrition: bool
    show_assets: bool
    landscape_view: bool
    disable_comments: bool
    disable_amount: bool


class Nutrition(Base):
    calories: str | None
    fat_content: str | None
    protein_content: str | None
    carbohydrate_content: str | None
    fiber_content: str | None
    sodium_content: str | None
    sugar_content: str | None


class RecipeIngredient(Base):
    title: str | None
    note: str | None
    unit: RecipeIngredientUnit | None
    food: RecipeIngredientFood | None
    disable_amount: bool | None
    quantity: int | None


class RecipeIngredientUnit(Base):
    name: str | None
    description: str | None


class RecipeIngredientFood(Base):
    name: str | None
    description: str | None


class RecipeStep(Base):
    title: str | None
    text: str | None
