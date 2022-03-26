"""Main CLI application"""
import json
import sys

import click

from kiraak.config import API, Auth
from kiraak.main import main


@click.command()
@click.argument(
    "json_file", type=click.Path(exists=True, dir_okay=False), required=False
)
@click.option("-c", "--clear", is_flag=True)
@click.option("-g", "--get-catalog", is_flag=True)
def cli(json_file: str, clear, get_catalog) -> None:
    """Initiates cli"""
    if clear:  # Clear cached login data
        Auth.CONF_FILE.unlink()
        API.TOKEN_FILE.unlink()
        sys.exit()

    if get_catalog:
        from kiraak.get_catalog import download_catalog

        download_catalog()
        sys.exit()

    if not json_file:
        click.echo("No json file provided")
        raise click.Abort()

    if not json_file.endswith(".json"):
        click.echo("File must be a JSON file (.json)!")
        raise click.Abort()
    try:
        with open(json_file, "r") as file:
            json.load(file)
    except json.JSONDecodeError as err:
        click.echo("File must be a valid JSON file!")
        raise click.Abort() from err

    click.echo(f"Adding orders from {json_file}")
    main(json_file)
