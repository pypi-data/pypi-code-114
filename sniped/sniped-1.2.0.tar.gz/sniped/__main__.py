from __future__ import annotations

import json
import pathlib
from urllib.request import Request, urlopen
import sys
from typing import Optional

from rich.pretty import pprint
import typer

from .configs import CONFIGS
from .languages import LANGUAGES, Language, language_to_service_value
from .services import ENDPOINTS, Service
from .themes import THEMES, Theme


app = typer.Typer()


def read_code_from_stdin():
    return "".join([line for line in sys.stdin])


def try_reading_from_file(possible_file_path: str) -> str:
    """Try reading from a file with the given path or return the arg unchanged."""

    possible_file = pathlib.Path(possible_file_path)
    if possible_file.exists() and possible_file.is_file():
        with open(possible_file, "r") as f:
            return f.read()

    return possible_file_path


@app.command()
def create(
    service: Service = typer.Argument(..., case_sensitive=False),
    code: str = typer.Argument(
        ...,
        metavar="CODE_OR_PATH",
        help=(
            "Code to include in the image or path to code file."
            + " Use '-' to read from stdin."
        ),
    ),
    language: Language = typer.Option(
        "auto",
        metavar="LANG",
        help="Language for syntax highlighting; 'auto' only works for carbon.",
        case_sensitive=False,
    ),
    key: Optional[str] = typer.Option(
        None,
        metavar="KEY_OR_PATH",
        help="(Path to file with) API key for Snappify.",
    ),
    out: Optional[pathlib.Path] = typer.Option(
        None,
        metavar="PATH",
        help="Write to given file instead of stdout.",
        dir_okay=False,
        writable=True,
    ),
    theme: Optional[Theme] = typer.Option(
        None,
        metavar="THEME",
        help="Theme to use for syntax highlighting.",
        case_sensitive=False,
    ),
):
    """Create a beautiful image from a snippet of code."""

    request = Request(ENDPOINTS[service])
    request.add_header("Content-Type", "application/json")

    if service == Service.SNAPPIFY:
        # Abort if we don't have a valid API key.
        if not key:
            typer.echo("Option '--key' required for the Snappify service.", err=True)
            raise typer.Abort()
        key = try_reading_from_file(key).strip()
        request.add_header("Authorization", key)

    code = read_code_from_stdin() if code == "-" else try_reading_from_file(code)

    config = CONFIGS[service]
    config["code"] = code

    if language not in LANGUAGES[service]:
        typer.echo(
            f"'--language {language.value}' not available for {service}.", err=True
        )
        raise typer.Abort()
    config["language"] = language_to_service_value(service, language.value)

    if theme is not None:
        if theme not in THEMES[service]:
            typer.echo(
                f"'--theme {theme.value}' not available for {service}.", err=True
            )
            raise typer.Abort()
        config["theme"] = theme.value

    with urlopen(request, data=json.dumps(config).encode()) as response:
        image = response.read()

    if out is None:
        sys.stdout.buffer.write(image)
    else:
        with open(out, "wb") as f:
            f.write(image)


@app.command()
def config(
    service: Service = typer.Argument(..., case_sensitive=False),
    show: bool = typer.Option(
        False,
        help="Print the configuration to stdout.",
    ),
    pretty: bool = typer.Option(
        True,
        help="Whether to use pretty printing or show plain output.",
    ),
    write: Optional[pathlib.Path] = typer.Option(
        None,
        metavar="WRITE_PATH",
        help="File to write default config to.",
        dir_okay=False,
        writable=True,
    ),
):
    """Manage the configuration for the services."""

    config = CONFIGS[service]
    dump = json.dumps(config, indent=4)

    if show:
        if pretty:
            pprint(config)
        else:
            print(dump)

    if write is not None:
        write.write_text(dump)


if __name__ == "__main__":
    app()
