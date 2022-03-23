import logging
import logging.config
from argparse import ArgumentParser, Namespace
from contextlib import AbstractContextManager
from itertools import chain
from typing import Callable, Set

import uvicorn
from fastapi import FastAPI

from talisman_tools.configure.configure import read_json_config


def register_shutdown(app: FastAPI, context_manager: AbstractContextManager):
    @app.on_event("shutdown")
    async def exit_manager():
        context_manager.__exit__(None, None, None)


def uvicorn_server_factory(parser: ArgumentParser) -> Callable[[FastAPI, Namespace], None]:
    parser.add_argument('-remote', action='store_true', help='should listen for remote connections')
    parser.add_argument('-port', type=int, help='port to listen on', default=8000)
    parser.add_argument('-logging_conf', help='path to json file with logging config', default='talisman-tools/default_logging_conf.json')

    def launcher(app: FastAPI, args: Namespace) -> None:
        logging.config.dictConfig(read_json_config(args.logging_conf))
        host = "0.0.0.0" if args.remote else "127.0.0.1"
        uvicorn.run(app, host=host, port=args.port, log_config=None)

    return launcher


def add_extra_cli_argumants(parser: ArgumentParser) -> Set[Callable[[Namespace], None]]:
    from talisman_tools.plugin import CLIPlugins
    actions = set()
    for cli_factory in chain.from_iterable(CLIPlugins.plugins.values()):
        actions.add(cli_factory(parser))
    return actions
