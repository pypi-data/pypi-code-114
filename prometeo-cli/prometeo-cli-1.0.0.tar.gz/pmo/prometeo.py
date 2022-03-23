"""
This module provides the Prometeo CLI.
"""
# prometeo/prometeo.py

import typer

from datetime import datetime
from typing import Optional
from pathlib import Path
from typing import Optional

from pmo import __app_name__, __version__
from controllers import prometeo_controller, configuration_controller
from helpers import TablePrinter, Profiler


app = typer.Typer()
controller = prometeo_controller.PrometeoActionsController()
config_controller = configuration_controller.ConfigurationController()

def date_callback(value):
    if value is None:
        raise typer.BadParameter('Date cannot be null')
    return value


def validate_movements_params(card, account):
    if account == None and card == None:
        raise typer.Exit('Must select one option')

    if account and card:
        raise typer.Exit('Must select only one option')


@app.command()
def login(
    provider: str = typer.Option(None, envvar='PROMETEO_PROVIDER'),
    interactive: bool = typer.Option(False)
) -> None:
    """
    Start a banking session
    """
    typer.echo('Loggin in')

    if interactive:
        controller.login(provider, interactive)
        raise typer.Exit('logged in succesfully')

    if provider is None:
        raise typer.Exit('You must specify a provider to login with --provider')

    controller.login(provider, interactive)

    raise typer.Exit('Logged in succesfully')



@app.command()
def logout() -> None:
    """
    Logout
    """
    typer.echo('Loggin out')
    controller.logout()
    typer.echo('Logged out')


@app.command()
def accounts() -> None:
    """
    Get accounts
    """
    accounts = controller.get_accounts()
    printer = TablePrinter()
    printer.print_accounts(accounts)

@app.command()
def cards() -> None:
    """
    Get credit cards
    """
    cards = controller.get_cards()
    printer = TablePrinter()
    printer.print_cards(cards)


@app.command()
def movements(
    account: str = typer.Option(
        None,'--account', '-a'
    ),
    card: str = typer.Option(
        None, '--card', '-c'
    ),
    start_date: datetime = typer.Option(
        None, formats=["%Y-%m-%d"], callback=date_callback
    ),
    end_date: datetime = typer.Option(
        None, formats=["%Y-%m-%d"], callback=date_callback
    ),
    currency: str = typer.Option(
        None, '--currency', '-cu'
    )
) -> None:
    """
    Get movements
    """
    validate_movements_params(card, account)

    if account and not card:
        movements = controller.get_account_movements(account, start_date, end_date)

    if card and not account:
        if not currency:
            raise typer.Exit('Must enter currency')
        movements = controller.get_card_movements(card, start_date, end_date, currency)

    printer = TablePrinter()
    printer.print_movements(movements)


@app.command()
def providers():
    providers = controller.get_providers()
    printer = TablePrinter()
    printer.print_providers(providers)


@app.command()
def config(credential: bool = typer.Option(False), environment: bool = typer.Option(False)):

    if credential and environment:
        raise typer.Exit('Please select only one option')

    if credential:
        config_controller.add_new_credential()
        raise typer.Exit('Credential saved')

    if environment:
        config_controller.add_new_environment()
        raise typer.Exit('New environment saved')


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
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

