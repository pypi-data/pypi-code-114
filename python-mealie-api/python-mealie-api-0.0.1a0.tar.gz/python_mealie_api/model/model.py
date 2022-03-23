from __future__ import annotations

from datetime import date

from .common import Base


class MealPlanResponse(Base):
    group: str | None
    start_date: date | None
    end_date: date | None
    plan_days: list[PlanDay]
    uid: int | None
    shopping_list: int | None


class PlanDay(Base):
    date: date | None
    meals: list[Meal]


class Meal(Base):
    slug: str | None
    name: str | None
    description: str | None


class StatisticsResponse(Base):
    total_recipes: int
    total_users: int
    total_groups: int
    uncategorized_recipes: int
    untagged_recipes: int
