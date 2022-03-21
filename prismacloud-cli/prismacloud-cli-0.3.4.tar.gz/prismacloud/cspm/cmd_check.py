import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("check", short_help="[CSPM] Check and see if the Prisma Cloud API is up and running")
@pass_environment
def cli(ctx):
    result = prismacloud.api.get("check", type='cspm')
    prismacloud.cli.output(result)