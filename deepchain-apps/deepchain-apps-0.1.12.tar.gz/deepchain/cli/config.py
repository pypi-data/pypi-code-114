"""deploy modules helps for the deployement of application on deepchain"""
from argparse import ArgumentParser
import yaml
from deepchain.cli import BaseCLICommand

from .apps_utils import ensure_has_config_file, ensure_has_config_folder


def config_command_factory(args):
    return ConfigCommand(args.backend_url)


class ConfigCommand(BaseCLICommand):
    def __init__(self, backend_url: str):
        self.backend_url = backend_url

    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        deploy_parser = parser.add_parser(  # type: ignore
            name="config", help="update deepchain cli configuration"
        )

        deploy_parser.add_argument(
            "--backend_url",
            '-b',
            type=str,
            help="sets deepchain api base url",
        )
        deploy_parser.set_defaults(func=config_command_factory)

    def run(self):
        root_path = ensure_has_config_folder()
        path = ensure_has_config_file(root_path)

        with open(path, "r+") as config_file:
            data = yaml.load(config_file, Loader=yaml.SafeLoader)
            data = {} if data is None else data

        if self.backend_url:
            data["backend_url"] = self.backend_url

        with open(path, "w") as app_file:
            yaml.dump(data, app_file, Dumper=yaml.SafeDumper)
