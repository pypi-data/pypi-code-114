from __future__ import annotations

import json
import pathlib
from urllib.request import Request, urlopen
import sys

import typer

from .configs import CARBON, SNAPPIFY

app = typer.Typer()

CARBON_ENDPOINT = "https://carbonara-42.herokuapp.com/api/cook"
SNAPPIFY_ENDPOINT = "https://api.snappify.io/snap/simple"


def read_code_from_stdin():
    return "".join([line for line in sys.stdin])


def try_reading_from_file(possible_file_path: str) -> str:
    """Try reading from a file with the given path or return the arg unchanged."""

    possible_file = pathlib.Path(possible_file_path)
    if possible_file.exists() and possible_file.is_file():
        with open(possible_file, "r") as f:
            return f.read()

    return possible_file_path


def load_config(config_file_path: str | pathlib.Path) -> dict:
    with open(config_file_path) as f:
        return json.load(f)


def make_image_from_request(
    code: str, language: str, out: str, request: Request, config: dict
):

    request.add_header("Content-Type", "application/json")

    code = read_code_from_stdin() if code == "-" else try_reading_from_file(code)
    config["code"] = code
    config["language"] = language

    with urlopen(request, data=json.dumps(config).encode()) as response:
        image = response.read()

    with open(out, "wb") as f:
        f.write(image)


@app.command()
def carbon(
    code: str,
    language: str = typer.Argument("auto"),
    out: str = typer.Argument("out.png"),
):
    make_image_from_request(
        code,
        language,
        out,
        Request(CARBON_ENDPOINT),
        CARBON,
    )


@app.command()
def snappify(code: str, key: str, language: str, out: str = typer.Argument("out.png")):
    req = Request(SNAPPIFY_ENDPOINT)
    key = try_reading_from_file(key)
    req.add_header("Authorization", key)
    make_image_from_request(
        code,
        language,
        out,
        Request(SNAPPIFY_ENDPOINT),
        SNAPPIFY,
    )


if __name__ == "__main__":
    app()
