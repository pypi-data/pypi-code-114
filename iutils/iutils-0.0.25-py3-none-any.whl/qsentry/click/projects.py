import click

from .main import add_common_options, common_options, main


@main.group(invoke_without_command=True)
@add_common_options(common_options)
def projects(*args, **kwargs):
    """Project related commands"""
    pass
