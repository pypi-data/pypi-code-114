from __future__ import annotations

import json
import pathlib
from urllib.request import Request, urlopen
import sys

import typer

from .configs import CARBON

app = typer.Typer()

CARBON_ENDPOINT = "https://carbonara-42.herokuapp.com/api/cook"
CARBON_CONFIG = (pathlib.Path(__file__) / "../carbon.config.json").resolve()


def read_code_from_stdin():
    return "".join([line for line in sys.stdin])


def load_config(config_file_path: str | pathlib.Path) -> dict:
    with open(config_file_path) as f:
        return json.load(f)


@app.command()
def carbon(code: str, language: str, out: str):
    req = Request(CARBON_ENDPOINT)
    req.add_header("Content-Type", "application/json")

    possible_code_file = pathlib.Path(code)
    if possible_code_file.exists() and possible_code_file.is_file():
        with open(possible_code_file, "r") as f:
            code = f.read()
    elif code == "-":
        code = read_code_from_stdin()

    config = CARBON
    config["code"] = code
    config["language"] = language

    with urlopen(req, data=json.dumps(config).encode()) as response:
        image = response.read()
    with open(out, "wb") as f:
        f.write(image)


if __name__ == "__main__":
    app()
