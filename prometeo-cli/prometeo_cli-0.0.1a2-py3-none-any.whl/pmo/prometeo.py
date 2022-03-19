"""
This module provides the Prometeo CLI.
"""
# prometeo/prometeo.py

import typer

from typing import Optional
from pathlib import Path
from typing import Optional

from pmo import __app_name__, __version__
from controllers import prometeo_controller


app = typer.Typer()


def _username_callback(value: str):
    pass

def _password_callback(value: str):
    pass

def _provider_callback(value: str):
    pass


@app.command()
def login(
    username: str,
    provider: str,
    password: str
) -> None:
    """
    Initialize the to-do database.
    """
    prometeo_controller.login(provider, username, password)


@app.command()
def accounts(
) -> None:
    """
    Initialize the to-do database.
    """
    prometeo_controller.get_accounts()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

