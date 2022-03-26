import click

from .main import (
    add_common_options,
    common_options,
    comma_separated_string_to_array,
    main,
)
from ..commands import OrgsCommand


common_orgs_options = [
    click.option(
        "--attrs",
        default="",
        callback=comma_separated_string_to_array,
        help="""The argument to this option should be a comma separated string.
                For example, "id,name".""",
    ),
]


@main.group(invoke_without_command=True)
def orgs(*args, **kwargs):
    """Organization related commands"""
    pass


@orgs.command()
@add_common_options(common_options)
@add_common_options(common_orgs_options)
def list_projects(**kwargs):
    """List all projects of the given organization.

    List the project's id and name by default. Use the --attrs option to change
    what attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["id", "name"]
    OrgsCommand(**kwargs).list_projects(attrs)


@orgs.command()
@add_common_options(common_options)
@add_common_options(common_orgs_options)
def list_users(**kwargs):
    """List all users of the given organization.

    List the user's id and email by default. Use the --attrs option to change
    what attributes to show.
    """
    attrs = kwargs["attrs"] if kwargs["attrs"] else ["id", "email"]
    OrgsCommand(**kwargs).list_users(attrs)
