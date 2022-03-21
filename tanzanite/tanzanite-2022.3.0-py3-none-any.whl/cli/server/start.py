# -*- coding: utf-8 -*-

"""
Start the Tanzanite API server via the `tanzanite` (a.k.a., `tz`) CLI.
"""

# Standard imports
import contextlib
import logging
import os
import threading
import time

# External imports
import uvicorn

from cliff.command import Command

# Local imports
from tanzanite import (
    DEFAULT_API_PORT,
    DOMAIN,
    SPHINX_DOCS_HTML,
    TANZANITE_SOURCE_ROOT,
)
from tanzanite.utils import run


class Server(uvicorn.Server):
    """
    Customized server class.
    """
    def install_signal_handlers(self):
        pass

    @contextlib.contextmanager
    def run_in_thread(self):
        """
        Run in a separate thread.
        """
        thread = threading.Thread(target=self.run)
        thread.start()
        try:
            while not self.started:
                time.sleep(1e-3)
            yield
        finally:
            self.should_exit = True
            thread.join()


def run_app(
    app=None,
    host=DOMAIN,
    port=DEFAULT_API_PORT,
    log_level=None,
):
    """
    Run app in event loop.
    """
    # loop = asyncio.new_event_loop()
    # log_config = uvicorn.config.LOGGING_CONFIG
    # log_config["formatters"]["access"]["fmt"] = LOG_FORMAT
    # log_config["formatters"]["default"]["fmt"] = LOG_FORMAT
    # configure_logging()
    config = uvicorn.Config(
        app,
        # loop=loop,
        loop='anyio',
        host=host,
        port=port,
        log_level=log_level,
    )
    server = Server(config=config)

    with server.run_in_thread():
        time.sleep(3000)
        # loop.run_until_complete(server.run())


class CmdStartAPI(Command):
    """
    Start the API and database backend.

    This command performs the same steps that were performed in
    the `prestart.sh` Bash script from `tiangolo/full-stack-fastapi-postgresql`:

        https://github.com/tiangolo/full-stack-fastapi-postgresql/blob/490c554e23343eec0736b06e59b2108fdd057fdc/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/prestart.sh

    Those steps are:
        1. Start the database server.
        2. Run Alembic migrations to create or upgrade database tables.
        3. Create the initial database contents on first start.
    """  # noqa

    logger = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '-b', '--bind-ip',
            action='store',
            dest='host',
            default=DOMAIN,
            help='Bind server to this IP address or DNS name'
        )
        parser.add_argument(
            '-p', '--port',
            action='store',
            dest='port',
            default='8000',
            help='Listen on this TCP port'
        )
        parser.add_argument(
            '--reload',
            action='store_true',
            dest='reload',
            default=False,
            help='Reload the server when files change (for development)'
        )
        return parser

    def take_action(self, parsed_args):
        # from tanzanite.backend.app.app.main import app
        # log_level = 'TRACE' if self.app_args.debug else 'INFO'
        # run_app(
        #     'tanzanite.backend.app.app.main:app',
        #     host=parsed_args.host,
        #     port=int(parsed_args.port),
        #     log_level=log_level,
        # )
        #
        # uvicorn_config = app_logger.get_logging_config(
        #     log_file='tanzanite-api.log'
        # )
        if not SPHINX_DOCS_HTML.exists():
            run(['make', 'docs'], cwd=TANZANITE_SOURCE_ROOT)
        os.environ['TANZANITE_STARTED_UVICORN'] = ''
        # https://github.com/miguelgrinberg/python-socketio/issues/332#issuecomment-712928157
        #
        try:
            uvicorn.run(
                'tanzanite.backend.app.app.main:app',
                # **uvicorn_config,
                # Prevent uvicorn from messing up the logging configuration
                # put in place by cliff so the FastAPI app can use it.
                log_config={
                    'version': 1,
                    'disable_existing_loggers': False,
                },
                # loop='asyncio',
                host=parsed_args.host,
                port=int(parsed_args.port),
                # reload=parsed_args.reload,
                # reload_excludes='build',
                # workers=1,
                # limit_concurrency=1,
                # limit_max_requests=1,
            )
        except AttributeError as err:
            if "object has no attribute 'exc_traceback'" in err:
                print(err)

# vim: set ts=4 sw=4 tw=0 et :
