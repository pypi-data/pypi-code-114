from .common import Base


class Item(Base):
    title: str | None
    text: str | None
    quantitiy: int | None
    checked: bool | None


class ShoppingList(Base):
    id: int
    name: str
    group: str | None
    items: list[Item]


class ShoppingListUpdate(Base):
    name: str
    group: str | None
    items: list[Item]
