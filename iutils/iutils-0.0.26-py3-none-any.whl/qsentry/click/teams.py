import click

from .main import add_common_options, common_options, main
from ..commands import TeamsCommand


@main.command()
@add_common_options(common_options)
def teams(**kwargs):
    """Team related commands"""
    TeamsCommand(**kwargs).run(**kwargs)
