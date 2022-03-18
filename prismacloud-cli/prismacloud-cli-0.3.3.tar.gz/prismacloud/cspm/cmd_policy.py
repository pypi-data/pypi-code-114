import click
import prismacloud.api
from prismacloud.cli import pass_environment

@click.command("policy", short_help="[CSPM] Returns available policies, both system default and custom")
@pass_environment
def cli(ctx):
    result = prismacloud.api.get("policy", type='cspm')
    prismacloud.cli.output(result)