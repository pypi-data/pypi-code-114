"""Entry point for the CLI (Init of parser)"""

#!/usr/bin/python3 # noqa: E265
import argparse

from deepchain.cli.set_backend import SetBackendCommand

from deepchain.cli.apps import AppsCommand
from deepchain.cli.auth import AuthCommand
from deepchain.cli.deploy import DeployCommand
from deepchain.cli.download import DownloadCommand
from deepchain.cli.config import ConfigCommand

# from .inference import InferenceCommand
from deepchain.cli.scaffold import CreateCommand


def main():
    parser = argparse.ArgumentParser(
        description="deepchain CLI",
        add_help=True,
        usage="deepchain <command> [--<args>] [<arguments>]",
    )
    commands_parser = parser.add_subparsers(help="deepchain-cli command helpers")

    AuthCommand.register_subcommand(commands_parser)
    CreateCommand.register_subcommand(commands_parser)
    DeployCommand.register_subcommand(commands_parser)
    AppsCommand.register_subcommand(commands_parser)
    DownloadCommand.register_subcommand(commands_parser)
    ConfigCommand.register_subcommand(commands_parser)
    SetBackendCommand.register_subcommand(commands_parser)
    # InferenceCommand.register_subcommand(commands_parser)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        exit(1)

    service = args.func(args)
    service.run()


if __name__ == "__main__":
    main()
