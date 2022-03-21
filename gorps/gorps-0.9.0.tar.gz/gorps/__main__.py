#!/usr/bin/env python3

from typing import Any, Optional, Union
from collections.abc import Iterable, Sequence
import logging
import json

from .model import Recipe
from .importers.yml import load as load_recipes, load_recipe, RECIPE_DIR
from .importers import filter_recipes
from .exporters import export, exporter_by_name, guess_format
from .exporters.templating import load_text_file
from .log import setup_logging
from .img_actions import set_image, extract_image
from .cli import (
    Argument,
    MutuallyExclusiveGroup,
    Action,
    declarative_parser,
    StoreDictKeyPair,
    map_dict,
)


def parse_title_file(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        return [t.strip("\n") for t in f.readlines()]


def parse_grouped_title_file(path: str) -> list[dict[str, Any]]:
    with open(path, encoding="utf-8") as f:
        grouped_titles = json.load(f)
        if not isinstance(grouped_titles, list):
            raise ValueError("Invalid input file")
        return grouped_titles


input_args: list[Union[Argument, MutuallyExclusiveGroup]] = [
    MutuallyExclusiveGroup(
        Argument(
            "-i",
            type=parse_title_file,
            default=None,
            dest="titles",
            help="input txt file (1 recipe title per line)",
        ),
        # The 2 are mutually exclusive, otherwise -i could
        # overwrite an item already specified by --title
        Argument(
            "--title",
            dest="titles",
            action="append",
            default=None,
            help="The recipes to export. All if no titles are specified",
        ),
    ),
    Argument(
        "sources",
        default=[],
        nargs="*",
        help=f"Specify files / folders to look for recipes. If not specified, defaults to {RECIPE_DIR} (if existing)",
    ),
]


def collect_tags(recipes: Iterable[Recipe]) -> list[str]:
    return sorted({t for r in recipes for t in r.tags.get("category", [])})


class Actions:
    class ListTags(Action):
        """List all tags contained in the recipes"""

        args = input_args

        def __call__(
            self, sources: Iterable[str], titles: Optional[Iterable[str]]
        ) -> None:
            logging.info("Loading DB ...")
            recipes = filter_recipes(load_recipes(sources=sources), titles=titles)

            print("\n".join(collect_tags(recipes)))

    class Export(Action):
        """Export to a file / directory"""

        description = "Needs a path as an argument. If the path is an existing directory or ends with a path separator, multiple output files will be created (named after the recipes title). Otherwise all selected recipes will be exported to a single file. The format is inferred by the extension or can be specified manually by the --fmt option."
        args = input_args + [
            Argument(
                "--filter-ingredient",
                dest="drop_ingredients",
                action="append",
                default=[],
                help="Drop specified ingredient from all loaded recipes",
            ),
            Argument("-o", dest="out", type=str, help="output file"),
            Argument(
                "--fmt",
                type=map_dict(exporter_by_name, err_msg="Invalid format: {key}."),
                default=None,
                help=f"Output format (one of {','.join(exporter_by_name)})",
            ),
            Argument(
                "--variable",
                "-V",
                dest="variables",
                action=StoreDictKeyPair,
                type=lambda s: s.split("="),
                default={},
                help="Declare a variable which can be accessed from within a template",
            ),
            Argument(
                "--variable-file",
                default=None,
                help="Load variables from a json file and make them accessible to templates",
            ),
            Argument(
                "--template",
                default=None,
                type=str,
                help="Specify a template",
            ),
            MutuallyExclusiveGroup(
                Argument(
                    "--group-by",
                    dest="group_selector",
                    default=None,
                    help="Group recipies by some attribute. The groups will be available in a 'groups' dict for templating.",
                ),
                Argument(
                    "--grouped-titles",
                    default=None,
                    type=parse_grouped_title_file,
                    help='Load a json file containing a dict of the form {"group": ["title1", "title2", ...], ...}',
                ),
            ),
            Argument(
                "--group",
                dest="groups",
                action="append",
                default=[],
                help="Adds a group name to filter groups provided by --group-by. Can be passed multiple times.",
            ),
        ]

        def __call__(
            self,
            sources: Iterable[str],
            titles: Optional[Iterable[str]],
            drop_ingredients: Sequence[str],
            **args: Any,
        ) -> None:
            logging.info("Loading DB ...")
            template = args.get("template")
            if template is not None:
                fmt = args.get("fmt")
                if fmt is None:
                    args["fmt"] = guess_format(template)
                args["template"] = load_text_file(template)
            recipes = filter_recipes(
                load_recipes(sources=sources),
                titles=titles,
                drop_ingredients=frozenset(drop_ingredients),
            )
            export(recipes=recipes, **args)

    class SetImage(Action):
        """Add an image to a recipe."""

        args = [Argument("recipe"), Argument("--pic", dest="image")]

        def __call__(self, recipe: str, image: str) -> None:
            recipe_obj = load_recipe(recipe)
            set_image(recipe=recipe_obj, image=image, out=recipe)

    class ExtractImage(Action):
        """Extract an image from a recipe and write to a file."""

        args = [Argument("recipe"), Argument("-o", dest="out")]

        def __call__(self, recipe: str, out: Optional[str] = None) -> None:
            recipe_obj = load_recipe(recipe)
            extract_image(recipe=recipe_obj, out=out)


def main(
    shell_args: Optional[Sequence[str]] = None, log_level: int = logging.INFO
) -> None:
    setup_logging(log_level)
    parser, action_by_name = declarative_parser(Actions)

    args = vars(parser.parse_args(shell_args))
    action_name = args.pop("action")

    action = action_by_name[action_name]
    action(**args)


if __name__ == "__main__":
    main()
