import click
import prismacloud.api as pc_lib
from prismacloud.cli import pass_environment, cli_output

@click.command("scans", short_help="[CWPP] Retrieves scan reports for images scanned by the Jenkins plugin or twistcli")
@click.option('-l', '--limit', help='Number of documents to return')
@click.option('-s', '--search', help='Search term')
@pass_environment
def cli(ctx, limit, search):
    result = pc_lib.get_endpoint("scans", {'limit': limit, 'search': search})
    cli_output(result)
