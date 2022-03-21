import click

from ocean import code
from ocean.utils import sprint


@click.command()
def cli():
    sprint(code.VERSION)
