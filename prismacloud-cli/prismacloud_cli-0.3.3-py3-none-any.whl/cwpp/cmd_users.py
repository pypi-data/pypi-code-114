import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("users", short_help="Retrieves a list of all users")
@pass_environment
def cli(ctx):
    result = prismacloud.api.get("users")
    prismacloud.cli.output(result)