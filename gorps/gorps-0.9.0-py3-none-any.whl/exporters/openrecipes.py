"""Export to an openrecipes sqlite database.

On an android phone, the db is accessible at
/data/user/0/org.jschwab.openrecipes/files/database.db
via adb pull.
"""

import os
from io import BytesIO
import sqlite3
from dataclasses import fields, field, Field
from fractions import Fraction
from typing import Optional, Union, Any, TypeVar
from collections.abc import Iterable, Collection, Sequence, Callable

from PIL import Image as PilImage


from ..model import Recipe, Ingredient, Image, AmountRange
from .base import ExporterBase

home = os.path.expanduser("~")
recipe_fields = {f.name: f for f in fields(Recipe)}
ingredient_fields = {f.name: f for f in fields(Ingredient)}

# OR field - recipes field:
field_mapping = (
    ("name", "title"),
    ("instruction", "instruction"),
    ("portions", "amount"),
    ("image", "image"),
)
OR_recipe_cols = tuple(or_field for or_field, _ in field_mapping)
OR_recipe_fields = tuple(
    recipe_fields[recipe_field] for _, recipe_field in field_mapping
)

id_field = field()
id_field.type = bytes
id_field.name = "title"

SCHEMA = """CREATE TABLE IF NOT EXISTS settings( name TEXT PRIMARY KEY, value BLOB);
CREATE TABLE IF NOT EXISTS recipes( id BLOB PRIMARY KEY, name TEXT, image TEXT, portions INTEGER DEFAULT 1, instruction TEXT, changed INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS ingredients( id INTEGER PRIMARY KEY, idRecipe BLOB NOT NULL 	REFERENCES recipes(id) 	ON DELETE CASCADE 	ON UPDATE CASCADE, count INTEGER, unit TEXT, article TEXT);
"""


class Exporter(ExporterBase):
    name = "openrecipes"
    ext = "db"

    @classmethod
    def export(cls, recipes: Iterable[Recipe], out: str) -> None:
        OpenRecipesDB.save_recipes(list(recipes), db=out)


class OpenRecipesDB:
    db_file = os.path.join(home, ".local", "share", "OpenRecipes", "database.db")

    @classmethod
    def save_recipes(
        cls, recipes: Collection[Recipe], db: Optional[str] = None
    ) -> None:
        if db is None:
            db = cls.db_file
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        cursor.executescript(SCHEMA)

        with connection:
            db_recipy_names = frozenset(
                row[0] for row in cursor.execute("SELECT name FROM recipes")
            )
            existing_recipes = filter(lambda r: r.title in db_recipy_names, recipes)
            new_recipes = filter(lambda r: r.title not in db_recipy_names, recipes)
            converters: dict[Field[Any], Callable[[Any], Any]] = {
                recipe_fields["amount"]: un_null(default=1),
                recipe_fields["image"]: encode_img,
                id_field: title_to_bytes,
            }
            structured_update(
                cursor,
                "name",
                OR_recipe_cols,
                OR_recipe_fields,
                "recipes",
                existing_recipes,
                types=converters,
            )
            new_recipes_tbl = tabularize(
                new_recipes,
                OR_recipe_fields + (id_field,),
                extra_values=(0,),
                types=converters,
            )

            columns = ", ".join(OR_recipe_cols + ("id", "changed"))
            values = ", ".join(("?",) * (len(OR_recipe_cols) + 2))
            cursor.executemany(
                f"INSERT INTO recipes ({columns}) VALUES ({values})",
                new_recipes_tbl,
            )

            # filter ingredients by local recipy names
            recipy_names = {r.title for r in recipes}
            rows = (
                row
                for row in cursor.execute(
                    "SELECT I.id, I.article, I.count, I.unit, recipes.name "
                    "FROM recipes, ingredients I WHERE recipes.id = I.idRecipe"
                )
                if row[-1] in recipy_names
            )
            db_ingredients_with_id = dict(map(lambda t: (t[1:], t[0]), rows))
            db_ingredients = frozenset(db_ingredients_with_id)
            memory_ingredients: list[tuple[Any, ...]] = sum(
                map(
                    lambda rec: list(
                        tabularize(
                            rec.all_ingredients(),
                            tab_fields=(
                                ingredient_fields["name"],
                                ingredient_fields["amount"],
                                ingredient_fields["unit"],
                            ),
                            extra_values=(rec.title,),
                            types={ingredient_fields["amount"]: rescale_amount},
                        )
                    ),
                    recipes,
                ),
                [],
            )
            new_ingredients = unique_in_order(memory_ingredients, seen=db_ingredients)
            delete_ingredients = db_ingredients - frozenset(memory_ingredients)
            cursor.executemany(
                "INSERT INTO ingredients (idRecipe, article, count, unit) "
                " SELECT id, ?,?,? FROM recipes"
                "  WHERE name = ?",
                new_ingredients,
            )
            cursor.executemany(
                "DELETE FROM ingredients WHERE id = ?",
                map(lambda i: (db_ingredients_with_id[i],), delete_ingredients),
            )

        cursor.close()
        connection.close()


def un_null(default: int) -> Callable[[Optional[Fraction]], int]:
    def _un_null(value: Optional[Fraction]) -> int:
        if value is None:
            return default
        return int(value)

    return _un_null


def rescale_amount(amount: Optional[Union[Fraction, AmountRange]]) -> Optional[int]:
    if amount is None:
        return None
    if isinstance(amount, AmountRange):
        amount = amount.min
    return int(amount * 1000)


def image_to_png(data: bytes) -> bytes:
    pic = PilImage.open(BytesIO(data))
    if pic.format == "PNG":
        return data
    out_stream = BytesIO()
    pic.save(out_stream, format="PNG")
    return out_stream.getvalue()


def encode_img(image: Optional[Image]) -> Optional[str]:
    if image is None or image.data is None:
        return None
    return Image(fmt="image/png", data=image_to_png(image.data)).as_b64()


def title_to_bytes(title: str) -> sqlite3.Binary:
    return sqlite3.Binary(title.encode())


def structured_update(
    cursor: sqlite3.Cursor,
    unique_col: str,
    cols: Sequence[str],
    q_fields: tuple[Field[Any], ...],
    table: str,
    recs: Iterable[Any],
    **kwargs: Any,
) -> None:
    unique_field = q_fields[cols.index(unique_col)]

    values = tabularize(recs, q_fields + (unique_field,), **kwargs)

    columns = ", ".join(f"{col} = ?" for col in cols)
    cursor.executemany(
        f"UPDATE {table} SET {columns} WHERE {unique_col} = ?",
        values,
    )


def tabularize(
    recs: Iterable[Any],
    tab_fields: Sequence[Field[Any]],
    extra_values: tuple[Any, ...] = (),
    types: Optional[dict[Field[Any], Callable[[Any], Any]]] = None,
) -> Iterable[tuple[Any, ...]]:
    if types is None:
        types = {}

    def id_(x: Any) -> Any:
        return x

    return (
        tuple(types.get(f, id_)(getattr(rec, f.name)) for f in tab_fields)
        + extra_values
        for rec in recs
    )


T = TypeVar("T")


def unique_in_order(lst: Iterable[T], seen: frozenset[T] = frozenset()) -> Iterable[T]:
    """
    >>> lst = [2, 3, 1, 2, 6, 1, 6]
    >>> list(unique_in_order(lst)
    [2, 3, 1, 6]
    """
    mutable_seen = set(seen)
    seen_add = mutable_seen.add
    return (i for i in lst if i not in seen and not seen_add(i))
