import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("tags", short_help="Retrieves a list of tags")
@pass_environment
def cli(ctx):
    result = prismacloud.api.get("tags")
    prismacloud.cli.output(result)