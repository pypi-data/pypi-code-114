"""Openrecipe xml export"""

from fractions import Fraction
from xml.etree.ElementTree import Element, SubElement, ElementTree
from typing import IO

from ..model import Recipe, Ingredient, AmountRange
from .openrecipes import encode_img
from .base import TextExporterBaseAtomic


class Exporter(TextExporterBaseAtomic):
    name = "openrecipes-xml"
    ext = "openrecipes"

    @classmethod
    def export_stream(cls, recipe: Recipe, stream: IO[str]) -> None:
        root = Element("recipe")
        root.attrib.update(serialize_recipe(recipe))
        for ingredient in recipe.all_ingredients():
            child = SubElement(root, "ingredient")
            child.attrib.update(serialize_ingredient(ingredient))
        ElementTree(root).write(stream, encoding="unicode", xml_declaration=True)


def serialize_recipe(recipe: Recipe) -> dict[str, str]:
    return dict(
        name=recipe.title,
        image=encode_img(recipe.image) or "",
        portions=str(int(recipe.amount)) if recipe.amount is not None else "1",
        instruction=recipe.instruction,
    )


def serialize_ingredient(ingredient: Ingredient) -> dict[str, str]:
    if isinstance(ingredient.amount, AmountRange):
        count = (ingredient.amount.min + ingredient.amount.max) / 2
    elif ingredient.amount is not None:
        count = ingredient.amount
    else:
        count = Fraction(1)
    return dict(
        article=ingredient.name,
        count=str(scaled_int(count)),
        unit=ingredient.unit or "",
    )


def scaled_int(x: Fraction) -> int:
    return int(x * 1000.0)
