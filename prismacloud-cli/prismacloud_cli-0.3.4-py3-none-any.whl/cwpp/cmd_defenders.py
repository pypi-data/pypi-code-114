import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.group("defenders", short_help="Retrieves Defenders information.")
@pass_environment
def cli(ctx):
    pass

@click.command()
def list():
    result = prismacloud.api.get("defenders")
    prismacloud.cli.output(result)

@click.command()
def names():
    result = prismacloud.api.get("defenders/names")
    prismacloud.cli.output(result)

@click.command()
def summary():
    result = prismacloud.api.get("defenders/summary")
    prismacloud.cli.output(result)

cli.add_command(list)
cli.add_command(names)
cli.add_command(summary)