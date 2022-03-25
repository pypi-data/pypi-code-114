import click

from i8_terminal.commands.user import user
from i8_terminal.config import USER_SETTINGS, delete_user_settings


@user.command()
def logout() -> None:
    if USER_SETTINGS:
        delete_user_settings()
        click.echo("User logged out successfully!")
    else:
        click.echo("You are already logged out!")
