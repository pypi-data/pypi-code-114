import json

import click

from .tables import commands as tables_commands
from ..utils import get_client, format_query_result_as_csv, handle_error_gracefully


@click.group("collections")
def collections():
    pass


@collections.command(name="list", help="List collections")
@click.pass_context
@handle_error_gracefully
def list_collections(ctx: click.Context):
    listed_collections = get_client(ctx).collections.list_collections()
    click.echo(
        json.dumps(
            [c.dict() for c in listed_collections],
            indent=2,
        )
    )


@collections.command("query", help="Query data")
@click.pass_context
@click.argument("collection_name")
@click.argument("query")
@click.option(
    "-f",
    "--format",
    type=click.Choice(["json", "csv"]),
    show_choices=True,
    default="json",
    show_default=True,
)
@handle_error_gracefully
def query_collection(ctx: click.Context, collection_name: str, query: str, format: str = "json"):
    results = [r for r in get_client(ctx).collections.get_data_connect_client(collection_name).query(query)]
    if format == "json":
        click.echo(json.dumps(list(results), indent=2))
    else:
        click.echo(format_query_result_as_csv(list(results)), nl=False)


# noinspection PyTypeChecker
collections.add_command(tables_commands.tables)
