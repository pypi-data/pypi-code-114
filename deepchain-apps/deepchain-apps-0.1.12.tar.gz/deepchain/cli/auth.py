"""Module that allow the authentification by register the personnal token"""

import argparse
import getpass
from urllib.parse import urlparse
from argparse import ArgumentParser
from deepchain.cli.cli_utils import get_config_url

import yaml
from deepchain.cli import BaseCLICommand
from deepchain.utils.constants import CHECKPOINT_SIZE

from .apps_utils import ensure_has_config_file, ensure_has_config_folder


def auth_command_factory(args):
    return AuthCommand(args.pat, args.backend_url)


class AuthCommand(BaseCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        login_parser: ArgumentParser = parser.add_parser(name="login",
                                                         help="login to deepchain")

        login_parser.add_argument(
            "--pat",
            "-p",
            help="set the pat",
            required=False,

        )
        login_parser.add_argument(
            "--backend_url",
            "-b",
            required=False,
            help=argparse.SUPPRESS
        )
        login_parser.set_defaults(func=auth_command_factory)

    def __init__(self, pat: str, backend_url: str):
        self.pat = pat
        self.backend_url = backend_url

    def run(self):
        """
        Login function that create a subdirectory and store the token
        We first create .deepchain folder, then config file if not exist
        """
        root_path = ensure_has_config_folder()
        config_path = ensure_has_config_file(root_path)

        with open(config_path, "r+") as config:
            data = yaml.load(config, Loader=yaml.SafeLoader)
            data = {} if data is None else data

        if self.pat is None:
            self.pat = getpass.getpass("PAT:")
        if self.backend_url is None:
            if "backend_url" in data:
                self.backend_url = data["backend_url"]
            else:
                self.backend_url = self.get_default_backend_url()
        # TODO : some sort of validation : hit a test endpoint with current pat to se if every thing is working
        is_validurl = self.validate_url(self.backend_url)
        if not is_validurl:
            raise ValueError("Invalid backend url")

        data["pat"] = self.pat
        data["backend_url"] = self.normalize_url(self.backend_url)
        data["size_limit"] = CHECKPOINT_SIZE

        with open(config_path, "w") as config:
            yaml.dump(data, config, Dumper=yaml.SafeDumper)

    def validate_url(self, url: str) -> bool:
        """
        Validate the url
        """
        parsed = urlparse(url)
        return parsed.scheme and parsed.netloc

    def normalize_url(self, url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    def get_default_backend_url(self) -> str:
        """
        Get the default backend url
        """
        return get_config_url()
