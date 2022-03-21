import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("license", short_help="Returns the license stats including the credit per defender")
@pass_environment
def cli(ctx):
    result = prismacloud.api.get("stats/license")
    prismacloud.cli.output(result)