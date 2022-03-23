import logging
from argparse import ArgumentParser

from fastapi import FastAPI

from talisman_tools.servers.exceptions import register_exception_handlers
from talisman_tools.servers.helper import add_extra_cli_argumants, register_shutdown, uvicorn_server_factory
from talisman_tools.servers.loader.methods.load import register_load_docs
from tp_interfaces.knowledge_base.manager import KBManager

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description='kb loader server')

    launcher = uvicorn_server_factory(parser)
    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    app = FastAPI(title='kb loader server', description='kb loader server')

    kb = KBManager().knowledge_base

    register_load_docs(
        app=app,
        kb=kb,
        logger=logger
    )

    register_exception_handlers(app)
    register_shutdown(app, kb)

    kb.__enter__()
    launcher(app, args)


if __name__ == '__main__':
    main()
