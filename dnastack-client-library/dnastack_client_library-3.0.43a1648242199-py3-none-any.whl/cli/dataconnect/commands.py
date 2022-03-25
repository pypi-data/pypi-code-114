import json
import os
from datetime import datetime
from typing import Optional

import click
from requests import HTTPError

from .tables import commands as tables_commands
from ..utils import get_client, format_query_result_as_csv, handle_error_gracefully
from ...exceptions import ServiceException


@click.group("dataconnect")
def dataconnect():
    pass


@dataconnect.command("query")
@click.pass_context
@click.argument("query")
@click.option("-o", "--output",
              help="The path to the output file (Note: When the option is specified, there will be no output to stdout.)",
              required=False,
              default=None)
@click.option("-f",
              "--format",
              help="Output Format",
              type=click.Choice(["json", "csv"]),
              show_choices=True,
              default="json",
              show_default=True)
@handle_error_gracefully
def data_connect_query(ctx: click.Context, query: str, output: Optional[str] = None, format: str = "json"):
    iterator = get_client(ctx).data_connect.query(query)

    try:
        if format == "json":
            result_output = json.dumps(list(iterator), indent=4)
        else:
            result_output = format_query_result_as_csv(list(iterator))
    except HTTPError as h:
        error_json = json.loads(h.response.text)
        error_msg = "Unable to get the paginated response"
        if "errors" in error_json:
            error_msg += f": {error_json['errors'][0]['title']}"
        raise ServiceException(
            url=get_client(ctx).dataconnect.url,
            msg=error_msg,
        )

    if output:
        with open(output, "w") as fs:
            fs.write(result_output)
    else:
        click.echo(result_output, nl=(format != "csv"))


# noinspection PyTypeChecker
dataconnect.add_command(tables_commands.tables)
