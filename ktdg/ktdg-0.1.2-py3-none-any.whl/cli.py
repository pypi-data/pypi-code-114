from pathlib import Path

import typer

from .config import read_config, save_config
from .generation import generate, save_data


def init_cli() -> typer.Typer:
    cli = typer.Typer(context_settings={"help_option_names": ["-h", "--help"]})
    cli.command("generate")(generate_)
    cli.command("g", hidden=True)(generate_)
    cli.command("create")(create_config)
    cli.command("c", hidden=True)(create_config)
    return cli


def run_cli() -> None:
    cli = init_cli()
    cli()


def generate_(config: str) -> None:
    """
    (g) Generates the data for the given config, saving it as a json file named
    "data.json".

    \b
    Parameters
    ----------
    config : str
      Configuration file to use
    """
    config_ = read_config(Path(config))
    data = generate(config_)
    save_data(data)


def create_config(
    config: str,
) -> None:
    """
    (c) Creates a config or completes it, saving it to the given file.

    \b
    Parameters
    ----------
    config : str
      Path of the config to complete or create
    """
    path = Path(config)
    config_ = read_config(path)
    save_config(config_, path)
