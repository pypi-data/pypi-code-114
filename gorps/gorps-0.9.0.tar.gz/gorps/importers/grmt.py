"""Import module to load from grmt files (https://thinkle.github.io/gourmet/).

Note: gourmet is still python 2.7, therefore to be considered as unmaintained.
"""

import os
import re
from collections import OrderedDict
from collections.abc import Callable, Sequence
from typing import Optional, Union, Any, Iterable
from dataclasses import dataclass, fields, Field, asdict
import sqlite3
from functools import reduce
from fractions import Fraction

from ..model import Recipe, Ingredient, IngredientGroup, Image, AmountRange

home = os.path.expanduser("~")


@dataclass
class GrmtIngredient(Ingredient):
    amount: Optional[Fraction] = None
    amount_max: Optional[Fraction] = None


@dataclass
class GrmtRecipe(Recipe):
    modifications: Optional[str] = None
    rating: int = 0
    cuisine: Optional[str] = None


recipe_fields = {f.name: f for f in fields(GrmtRecipe)}
ingredient_fields = {f.name: f for f in fields(GrmtIngredient)}
ingredient_table = (
    ("unit", ingredient_fields["unit"]),
    ("amount", ingredient_fields["amount"]),
    ("rangeamount", ingredient_fields["amount_max"]),
    ("item", ingredient_fields["name"]),
    ("optional", ingredient_fields["optional"]),
)

recipe_table = (
    ("title", recipe_fields["title"]),
    ("instructions", recipe_fields["instruction"]),
    ("modifications", recipe_fields["modifications"]),
    ("cuisine", recipe_fields["cuisine"]),
    ("description", recipe_fields["description"]),
    ("source", recipe_fields["source"]),
    ("preptime", recipe_fields["preparation_time"]),
    ("cooktime", recipe_fields["cooking_time"]),
    ("yields", recipe_fields["amount"]),
    ("yield_unit", recipe_fields["amount_unit"]),
    ("image", recipe_fields["image"]),
    ("link", recipe_fields["link"]),
)


class GourmetDB:
    db_file = os.path.join(home, ".gourmet", "recipes.db")

    @classmethod
    def load_recipes(cls) -> tuple[Recipe, ...]:
        db = sqlite3.connect(cls.db_file)
        cursor = db.cursor()
        recipes = structured_select(
            cursor,
            GrmtRecipe,
            ("id",),
            recipe_table,
            "SELECT {} FROM recipe WHERE NOT deleted",
        )
        recipes = {key: to_recipe(val) for key, val in recipes}

        ingredients = [
            convert_ingredient(i)
            for i in structured_select(
                cursor,
                Ingredient,
                ("recipe_id", "inggroup"),
                ingredient_table,
                "SELECT {} FROM ingredients "
                " WHERE NOT deleted ORDER BY recipe_id, position",
            )
        ]

        ingredients_by_recipe_id = group_by(lambda t: (t[0], t[1:]), ingredients)
        for recipe_id, ingredients in ingredients_by_recipe_id.items():

            def id_(t: tuple[Any, Any]) -> tuple[Any, Any]:
                return t

            grouped_ingredients = group_by(id_, ingredients, dct=OrderedDict)
            groupless_ingredients = grouped_ingredients.pop(None, [])
            recipes[recipe_id].ingredients = [
                IngredientGroup(name=t[0], ingredients=t[1])
                for t in grouped_ingredients.items()
            ] + groupless_ingredients
        categories = cursor.execute(
            "SELECT recipe_id, category FROM categories ORDER BY recipe_id"
        )
        categories_by_recipe_id = group_by(id_, categories)
        for recipe_id, categories in categories_by_recipe_id.items():
            if categories:
                recipes[recipe_id].tags.setdefault("category", []).extend(categories)
        return tuple(recipes.values())


def convert_ingredient(ingredient: GrmtIngredient) -> Ingredient:
    kwargs = asdict(ingredient)
    amount_max = kwargs.pop("amount_max", None)
    if amount_max is not None:
        if ingredient.amount is None:
            raise ValueError("amount_max specified without amount")
        kwargs["amount"] = AmountRange(ingredient.amount, amount_max)

    return Ingredient(**kwargs)


def group_by(
    decompose: Callable[[Any], tuple[Any, Any]], lst: Iterable[Any], dct: type = dict
) -> dict[Any, Any]:
    def classify(grouped: Any, t: Any) -> Any:
        key, val = decompose(t)
        grouped.setdefault(key, []).append(val)
        return grouped

    return reduce(classify, lst, dct())


def to_recipe(grmt_recipe: GrmtRecipe) -> Recipe:
    grmt_data = asdict(grmt_recipe)
    del grmt_data["notes"], grmt_data["description"]
    modifications = grmt_data.pop("modifications")
    grmt_data.pop("rating", None)
    cuisine = grmt_data.pop("cuisine")
    tags = {}
    if cuisine:
        tags["cuisine"] = [cuisine]
    new_tags, notes, description = parse_modifications(modifications)
    tags.update(new_tags)
    if tags:
        grmt_data["tags"] = tags
    for f in ("amount_unit", "link", "source", "cooking_time"):
        if not getattr(grmt_recipe, f):
            grmt_data.pop(f, None)
    if grmt_data.get("image") is not None:
        grmt_data["image"] = Image(fmt="image/jpeg", data=grmt_data["image"])

    if grmt_data.get("cooking_time") == 0:
        grmt_data["cooking_time"] = None
    if grmt_data.get("preparation_time") == 0:
        grmt_data["preparation_time"] = None

    recipe = Recipe(notes=notes, description=description, **grmt_data)
    return recipe


def parse_modifications(
    modifications: str,
) -> tuple[dict[str, Any], Optional[str], Optional[Any]]:
    if modifications is None:
        return {}, None, None
    tags: dict[str, Any] = {}

    def extract(s: str, r: str) -> tuple[str, Optional[str]]:
        regex = re.compile(r, flags=re.MULTILINE)
        m = regex.search(s)
        if m:
            start = m.start()
            stop = m.end()
            if r[-1] == "$" and len(s) > stop and s[stop] == "\n":
                stop += 1
            return s[:start] + s[stop:], m.groups()[0].strip("\n\t ")
        return s, None

    for sec in ("decription", "description", "difficulty", "tools"):
        for d1, d2 in (("<", ">"), ("&lt;", "&gt;")):
            modifications, m = extract(
                modifications,
                r"{d1}{sec}{d2}\n?((.|\n)*)\n?{d1}/{sec}{d2}$".format(
                    sec=sec, d1=d1, d2=d2
                ),
            )
            if m:
                tags[sec] = m
    description = tags.pop("decription", None) or tags.pop("description", None)
    if description:
        description = description.strip("\n\t ")
    for key in ("Glas", "Zubereitung", "Deko"):
        modifications, m = extract(modifications, rf"^{key}: ?(.*)$")
        if m:
            tags[key] = m
    modifications, m = extract(modifications, r"^(Keine Deko)$")
    if m:
        tags["Deko"] = None
    modifications = modifications.strip("\n \t")
    tools = tags.get("tools")
    if tools:
        tags["tools"] = [t.strip("\n\t *") for t in tools.split("\n")]
    return tags, modifications or None, description or None


def structured_select(
    cursor: sqlite3.Cursor,
    cls: type,
    extra_cols: tuple[str, ...],
    field_mapping: Iterable[tuple[str, Field[Any]]],
    query: str,
) -> Iterable[Any]:
    cols, fields_ = zip(*field_mapping)
    split = len(extra_cols)

    def row_to_struct(row: Sequence[Any]) -> tuple[Any, ...]:
        key = row[:split]
        val = row[split:]
        data = {f.name: force_type(f.type, v) for f, v in zip(fields_, val)}
        return (*key, cls(**data))

    return map(
        row_to_struct, cursor.execute(query.format(", ".join(extra_cols + cols)))
    )


def force_optional_type(T: Any, val: Any) -> Any:
    if (
        getattr(T, "__origin__", None) is Union
        and isinstance(None, T.__args__)
        and len(T.__args__) == 2
    ):
        if val is None:
            return None
        T1, T2 = T.__args__
        if isinstance(None, T1):
            return T2(val)
        return force_type(T1, val)
    return force_type(T, val)


def force_type(T: type, val: Any) -> Any:
    if T not in (str, int, Fraction, bool):
        return val
    return T(val)
