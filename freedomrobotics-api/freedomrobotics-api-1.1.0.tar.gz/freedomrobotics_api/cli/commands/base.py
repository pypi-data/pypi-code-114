import sys
from contextlib import contextmanager

import click

from freedomrobotics_api.credentials import ENVIRONMENTS

common_options = [
    click.option('-u', '--user'),
    click.option('--env', '--environment', default='release', type=click.Choice(ENVIRONMENTS)),
]


def add_options(options):
    """Decorator to allow sharing options between commands
    taken from https://stackoverflow.com/a/40195800/2349395
    """
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


@contextmanager
def error_message_catch(message, do_exit=True):
    try:
        yield
        click.echo(click.style(f"{message} OK", fg='green'))
    except Exception as e:
        click.echo(click.style(f"{message} FAILED: {e}", fg='red'))
        if do_exit:
            sys.exit(1)
