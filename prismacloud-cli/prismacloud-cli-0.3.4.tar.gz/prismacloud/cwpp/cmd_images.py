import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("images", short_help="Retrieves image scan reports")
@click.option('-l', '--limit')
@pass_environment
def cli(ctx, limit):
    result = prismacloud.api.get("images", { "limit": limit })
    prismacloud.cli.output(result)