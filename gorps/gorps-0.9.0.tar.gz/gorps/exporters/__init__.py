import os
from typing import Optional, Union, Any
from collections.abc import Iterable, Sequence
import json

from ..model import Recipe, Ingredient, IngredientGroup
from .base import ExporterBase, slugify
from .templating import class_selector, fmt_ingredients, accept_fallback_value
from .templating.exporter import TemplateExporterBase
from . import xml, svg, md, html
from .html import make_paragraphs

exporters: list[type[ExporterBase]] = [
    xml.Exporter,
    svg.Exporter,
    md.Exporter,
    html.Exporter,
]

try:
    from . import openrecipes, openrecipes_xml

    exporters += [openrecipes.Exporter, openrecipes_xml.Exporter]
except ModuleNotFoundError:
    pass

exporter_by_ext = {exporter.ext: exporter for exporter in exporters}
exporter_by_name = {exporter.name: exporter for exporter in exporters}


def export(
    out: str,
    recipes: Iterable[Recipe],
    variables: Optional[dict[str, str]] = None,
    variable_file: Optional[str] = None,
    template: Optional[str] = None,
    grouped_titles: Optional[list[dict[str, Any]]] = None,
    group_selector: Optional[str] = None,
    groups: Sequence[str] = (),
    fmt: Optional[type[ExporterBase]] = None,
) -> None:
    exporter_class = fmt or guess_format(out)
    if exporter_class is None:
        raise ValueError("Could not infer format from output or template")
    exporter_options: dict[str, Any] = {}
    if template is not None:
        exporter_options["template"] = template
    variables = merge_dicts(
        vars_from_file(variable_file),
        variables,
        build_groups(recipes, grouped_titles, group_selector, groups),
        {helper.__name__: helper for helper in HELPERS}
        if issubclass(exporter_class, TemplateExporterBase)
        else None,
    )
    if variables:
        exporter_options["variables"] = variables
    exporter = exporter_class(**exporter_options)
    if os.path.isdir(out) or out.endswith(os.path.sep):
        os.makedirs(os.path.dirname(out), exist_ok=True)
        exporter.export_multifile(recipes, out_dir=out)
    else:
        exporter.export(recipes, out=out)


def is_group(obj: Union[Ingredient, IngredientGroup]) -> bool:
    return isinstance(obj, IngredientGroup)


def fmt_time(t: int) -> str:
    return f"{t // 60}:{t % 60:02} min"


HELPERS = [
    is_group,
    accept_fallback_value(fmt_time),
    accept_fallback_value(fmt_ingredients),
    accept_fallback_value(make_paragraphs),
    accept_fallback_value(slugify),
]


def merge_dicts(*dicts: Optional[dict[str, Any]]) -> dict[str, Any]:
    merged = {}
    for d in dicts:
        if d is not None:
            merged.update(d)
    return merged


def vars_from_file(variable_file: Optional[str] = None) -> dict[str, Any]:
    if variable_file is None:
        return {}
    with open(variable_file, encoding="utf-8") as f:
        variables: dict[str, Any] = json.load(f)
        return variables


def guess_format(path: Optional[str]) -> Optional[type[ExporterBase]]:
    if path is None:
        return None
    _, ext = os.path.splitext(path)
    try:
        return exporter_by_ext[ext.lstrip(".")]
    except KeyError:
        return None


def build_groups(
    recipes: Iterable[Recipe],
    grouped_titles: Optional[list[dict[str, Any]]],
    selector: Optional[str],
    groups: Iterable[str],
) -> dict[str, Any]:
    groups = list(groups)
    if grouped_titles is not None:
        if groups:
            grouped_titles = [
                group for group in grouped_titles if group["name"] in groups
            ]
        return {"groups": group_titles(recipes, grouped_titles)}
    if selector is None:
        return {}
    return {"groups": group_by(list(recipes), selector, groups)}


def group_by(
    recipes: Sequence[Recipe], selector: str, group_names: Sequence[str] = ()
) -> list[tuple[str, list[Recipe]]]:
    select = class_selector(selector, default=None)
    groups: dict[str, list[Recipe]] = {}
    for recipe in recipes:
        attr = select(recipe)
        if attr is None:
            continue
        if not isinstance(attr, Sequence):
            attr = [attr]
        for group_name in attr:
            if group_name in group_names or not group_names:
                groups.setdefault(group_name, []).append(recipe)
    if group_names:
        return [(group_name, groups[group_name]) for group_name in group_names]
    return sorted(groups.items(), key=lambda item: item[0])


def group_titles(
    recipes: Iterable[Recipe], grouped_titles: list[dict[str, Any]]
) -> list[tuple[str, list[Recipe]]]:
    groups_by_title: dict[str, set[str]] = {}
    for group in grouped_titles:
        for title in group["titles"]:
            groups_by_title.setdefault(title, set()).add(group["name"])
    missing_titles = set(groups_by_title)
    grouped_recipes: dict[str, list[Recipe]] = {}
    for recipe in recipes:
        groups = groups_by_title.get(recipe.title, ())
        missing_titles.discard(recipe.title)
        for group_name in groups:
            grouped_recipes.setdefault(group_name, []).append(recipe)
    if missing_titles:
        raise ValueError(
            f"Could not find recipes with titles: {', '.join(missing_titles)}"
        )
    return [(group["name"], grouped_recipes[group["name"]]) for group in grouped_titles]
