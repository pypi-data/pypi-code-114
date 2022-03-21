import click
import prismacloud.api
from prismacloud.cli import pass_environment
import logging

@click.command("scans", short_help="[CWPP] Retrieves scan reports for images scanned by the Jenkins plugin or twistcli")
@click.option('-l', '--limit', help='Number of documents to return')
@click.option('-s', '--search', help='Search term')
@pass_environment
def cli(ctx, limit, search):
    result = prismacloud.api.get("scans", { 
        "limit": limit,
        "search": search,
    })
    prismacloud.cli.output(result)