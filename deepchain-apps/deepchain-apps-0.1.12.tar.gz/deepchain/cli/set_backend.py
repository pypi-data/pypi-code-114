from urllib.parse import urlparse
from argparse import ArgumentParser
from deepchain.cli.cli_utils import get_config_url

import yaml
from deepchain.cli import BaseCLICommand
from deepchain.utils.get_input import get_input

from .apps_utils import ensure_has_config_file, ensure_has_config_folder


def set_backend_command_factory(args):
    return SetBackendCommand(args.backend_url)


class SetBackendCommand(BaseCLICommand):

    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        be_parser: ArgumentParser = parser.add_parser(name="set-backend",
                                                      help="set the deepchaing backend url")
        be_parser.add_argument(
            "--backend_url",
            "-b",
            help="set the backend url",
            required=False,
        )
        be_parser.set_defaults(func=set_backend_command_factory)

    def __init__(self, backend_url: str):
        self.backend_url = backend_url

    def run(self):
        root_path = ensure_has_config_folder()
        config_path = ensure_has_config_file(root_path)

        with open(config_path, "r+") as config:
            data = yaml.load(config, Loader=yaml.SafeLoader)
            data = {} if data is None else data

        if not self.validate_url(self.backend_url):
            print("Please enter a valid url")
            self.backend_url = get_input("Backend url: ", validator=lambda x: self.validate_url(x),
                                         error_message="Please enter a valid url")
        # TODO : some sort of validation : hit a test endpoint with current pat to se if every thing is working
        data["backend_url"] = self.backend_url

        with open(config_path, "w") as config:
            yaml.dump(data, config, Dumper=yaml.SafeDumper)

    def validate_url(self, url: str) -> bool:
        """
        Validate the url
        """
        if url is None:
            return False
        try:
            result = urlparse(url)
            return all([result.netloc])
        except Exception:
            return False

    def get_default_backend_url(self) -> str:
        """
        Get the default backend url
        """
        return get_config_url()
