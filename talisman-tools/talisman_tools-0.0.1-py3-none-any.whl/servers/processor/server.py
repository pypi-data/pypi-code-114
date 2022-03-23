import logging
from argparse import ArgumentParser
from pathlib import Path

from fastapi import FastAPI

from talisman_tools.configure import load_or_configure, wrap_model
from talisman_tools.plugin import EndpointPlugins, TDMPlugins
from talisman_tools.servers.exceptions import register_exception_handlers
from talisman_tools.servers.helper import add_extra_cli_argumants, register_shutdown, uvicorn_server_factory
from talisman_tools.servers.processor.methods.process import register_process_docs
from talisman_tools.servers.processor.methods.update import register_info, register_update
from tp_interfaces.abstract import AbstractUpdatableModel
from tp_interfaces.helpers.io import read_json

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser(description="talisman processor REST server")
    parser.add_argument('-dm', type=str, choices=set(TDMPlugins.plugins), metavar='<document model>')
    parser.add_argument('-models', nargs='+', type=Path, metavar='<model path>', default=[])
    parser.add_argument('-cfg', nargs='+', type=Path, metavar='<model json config path>', default=[])
    parser.add_argument('-wrapper', type=str, metavar='<wrapper json config path>',
                        help="wrapper config should refer to target model with 'wrapped' key")

    launcher = uvicorn_server_factory(parser)
    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    document_model = TDMPlugins.plugins[args.dm]

    processor = load_or_configure(args.models, args.cfg)
    print(f"Loaded {processor}")

    if args.wrapper is not None:
        processor = wrap_model(processor, read_json(args.wrapper))

    app = FastAPI(title="talisman-ie REST server", description=f"talisman-ie REST server for {processor}")

    register_process_docs(
        app=app,
        endpoint='/',
        processor=processor,
        document_model=document_model,
        logger=logger
    )

    if isinstance(processor, AbstractUpdatableModel):
        register_update(app, processor, processor.update_type)
        register_info(app, processor, processor.update_type)

    for endpoint, register in EndpointPlugins.flattened.items():
        register()(app=app, endpoint=endpoint, processor=processor, logger=logger)

    register_exception_handlers(app, logger=logger)
    register_shutdown(app, processor)

    processor.__enter__()
    launcher(app, args)


if __name__ == '__main__':
    main()
