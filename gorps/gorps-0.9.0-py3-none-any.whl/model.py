from collections.abc import Callable
from typing import Any, Union, Optional
from datetime import timedelta
from fractions import Fraction
from dataclasses import dataclass, field
import base64


@dataclass
class AmountRange:
    min: Fraction
    max: Fraction

    @classmethod
    def from_dict(cls, dct: dict[str, Any]) -> "AmountRange":
        return cls(**{key: Fraction(val) for key, val in dct.items()})


@dataclass
class Ingredient:
    name: str
    amount: Optional[Union[Fraction, AmountRange]] = None
    unit: Optional[str] = None
    optional: bool = False

    @classmethod
    def from_dict(cls, dct: dict[str, Any]) -> "Ingredient":
        amount = dct.pop("amount", None)
        if isinstance(amount, dict):
            amount = AmountRange.from_dict(amount)
        elif amount is not None:
            amount = Fraction(amount)
        return cls(**dct, amount=amount)


@dataclass
class IngredientGroup:
    name: str
    ingredients: list[Ingredient] = field(default_factory=list)


@dataclass
class Value:
    value: Fraction
    unit: str

    @classmethod
    def from_dict(cls, dct: dict[str, Any]) -> "Value":
        deserialize_item(dct, "value", Fraction)
        return cls(**dct)


@dataclass
class Image:
    fmt: str
    data: bytes

    def as_b64(self) -> str:
        return f"data:{self.fmt};base64,{base64.b64encode(self.data).decode()}"


@dataclass
class Recipe:
    title: str
    instruction: str
    description: Optional[str] = None
    amount: Optional[Fraction] = None
    amount_unit: Optional[str] = None
    preparation_time: Optional[timedelta] = None
    cooking_time: Optional[timedelta] = None
    image: Optional[Image] = None
    source: Optional[str] = None
    link: Optional[str] = None
    ingredients: list[Union[Ingredient, IngredientGroup]] = field(default_factory=list)
    nutrition_labels: dict[str, Value] = field(default_factory=dict)
    notes: Optional[str] = None
    tags: dict[str, Any] = field(default_factory=dict)

    def all_ingredients(self) -> list[Ingredient]:
        return sum(
            map(
                lambda i: (i.ingredients if isinstance(i, IngredientGroup) else [i]),
                self.ingredients,
            ),
            [],
        )

    @classmethod
    def from_dict(cls, dct: dict[str, Any]) -> "Recipe":
        ingredients = [
            parse_ingredient_group(igt) for igt in dct.pop("ingredients", [])
        ]
        try:
            nutrition_labels = {
                name: Value.from_dict(val)
                for name, val in dct.pop("nutrition_labels", {}).items()
            }
        except AttributeError:
            raise ValueError(dct["title"]) from None
        deserialize_optional_item(dct, "image", lambda data: Image(**data))
        deserialize_optional_item(dct, "amount", Fraction)
        return cls(ingredients=ingredients, nutrition_labels=nutrition_labels, **dct)


def deserialize_item(data: dict[str, Any], key: str, type_: type) -> dict[str, Any]:
    data[key] = type_(data[key])
    return data


def deserialize_optional_item(
    data: dict[str, Any], key: str, type_: Callable[[Any], Any]
) -> dict[str, Any]:
    value = data.pop(key, None)
    if value is not None:
        data[key] = type_(value)
    return data


def parse_ingredient_group(obj: dict[str, Any]) -> Union[Ingredient, IngredientGroup]:
    ingredients = obj.pop("ingredients", None)
    if ingredients:
        return IngredientGroup(
            ingredients=[Ingredient.from_dict(i) for i in ingredients], **obj
        )
    return Ingredient.from_dict(obj)
