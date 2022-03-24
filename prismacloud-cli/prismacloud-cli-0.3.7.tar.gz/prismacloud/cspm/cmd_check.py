import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("check", short_help="[CSPM] Check and see if the Prisma Cloud API is up and running")
@pass_environment
def cli(ctx):
    result = pc_lib.get_endpoint("check", api='cspm')
    cli_output(result)