from pathlib import Path
from shutil import copy
from site import getuserbase
from typing import Any

from blulib.config_parser import ConfigParser, SectionNotFoundError
from tealprint import TealPrint

from ..config import config
from ..core.entities.config_file_args import ConfigFileArgs


class ConfigGateway:
    def __init__(self) -> None:
        self.filename = f".{config.app_name}.cfg"
        self.path = Path.home().joinpath(self.filename)

    def get_args(self) -> ConfigFileArgs:
        args = ConfigFileArgs()

        if not self.path.exists():
            return args

        config = ConfigParser()
        config.read(self.path)

        try:
            config.to_object(
                args,
                "General",
                "int:port",
            )
        except SectionNotFoundError:
            TealPrint.warning(f"Section [General] not found in configuration ({self.path})")

        return args
