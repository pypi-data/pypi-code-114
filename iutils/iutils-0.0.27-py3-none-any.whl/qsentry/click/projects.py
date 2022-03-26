import click

from .main import (
    add_common_options,
    common_options,
    comma_separated_string_to_array,
    main,
)
from ..commands import ProjectsCommand


@main.group(invoke_without_command=True)
@add_common_options(common_options)
def projects(*args, **kwargs):
    """Project related commands"""
    pass


@projects.command()
@add_common_options(common_options)
@click.option(
    "--project",
    required=True,
    help="""The project slug""",
)
@click.option(
    "--attrs",
    default="",
    callback=comma_separated_string_to_array,
    help="""The argument to this option should be a comma separated string. For
            example, "id,dsn,rateLimit".""",
)
def list_keys(**kwargs):
    """List all client keys of the given project.

    List the key's id, dsn and rate limit by default. Use the --attrs option to
    change what attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["id", "dsn", "rateLimit"]
    ProjectsCommand(**kwargs).list_keys(kwargs["project"], attrs)
