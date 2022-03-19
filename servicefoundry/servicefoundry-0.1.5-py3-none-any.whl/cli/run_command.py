import logging

import click
from rich import print_json
from rich.console import Console

from ..build import build_and_deploy
from .util import handle_exception

console = Console()
logger = logging.getLogger(__name__)


def get_run_command():
    @click.command(help="Create servicefoundry run")
    @click.option("--env")
    @click.argument("service_dir", type=click.Path(exists=True), nargs=1)
    def run(env, service_dir):
        try:
            deployment = build_and_deploy(env=env, base_dir=service_dir)
            print_json(data=deployment)
        except Exception as e:
            handle_exception(e)

    return run
