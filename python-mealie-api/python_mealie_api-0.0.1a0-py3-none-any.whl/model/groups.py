from .common import Base, User
from .model import MealPlanResponse
from .shopping_lists import ShoppingList


class Category(Base):
    name: str
    id: int
    slug: str


class Group(Base):
    name: str
    id: int
    categories: list[Category]
    webhook_urls: list[str]
    webhook_time: str
    webhook_enable: bool
    users: list[User]
    meal_plans: list[MealPlanResponse]
    shopping_lists: list[ShoppingList]


class GroupUpdate(Base):
    name: str
    id: int
    categories: list[Category]
    webhook_urls: list[str]
    webhook_time: str
    webhook_enable: bool


class CreateGroup(Base):
    name: str
