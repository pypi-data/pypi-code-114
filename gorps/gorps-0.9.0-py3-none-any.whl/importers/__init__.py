from typing import Optional
from collections.abc import Iterable
from dataclasses import replace

from ..model import Recipe


def filter_recipes(
    recipes: Iterable[Recipe],
    titles: Optional[Iterable[str]],
    drop_ingredients: frozenset[str] = frozenset(),
) -> list[Recipe]:
    if titles is not None:
        recipes = filter_by_title(recipes, titles)
    if drop_ingredients:
        recipes = filter_ingredients(recipes, drop_ingredients)
    return list(recipes)


def filter_by_title(recipes: Iterable[Recipe], titles: Iterable[str]) -> list[Recipe]:
    recipes_by_title = {recipe.title: recipe for recipe in recipes}
    try:
        return [recipes_by_title[title] for title in titles]
    except KeyError:
        missing_titles = set(titles) - set(recipes_by_title)
        raise KeyError(
            f"Could not find recipes {', '.join(map(repr, missing_titles))}"
        ) from None


def filter_ingredients(
    recipes: Iterable[Recipe], ingredients: frozenset[str]
) -> Iterable[Recipe]:
    return (
        replace(
            recipe,
            ingredients=[
                ingredient
                for ingredient in recipe.ingredients
                if ingredient.name not in ingredients
            ],
        )
        for recipe in recipes
    )
