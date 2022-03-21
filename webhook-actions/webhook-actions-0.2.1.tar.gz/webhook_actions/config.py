from pathlib import Path

from tealprint import TealLevel, TealPrint

from .core.entities.config_file_args import ConfigFileArgs

_app_name = "webhook-actions"


class Config:
    def __init__(self):
        # Default values
        self.app_name: str = _app_name
        self.webhook_dir = Path.home().joinpath(self.app_name)
        self.log_level: TealLevel = TealLevel.info
        self.port: int = 5000

    def set_args_settings(self, args):
        """Set additional configuration from script arguments"""
        if args.verbose:
            self.log_level = TealLevel.verbose
        elif args.debug:
            self.log_level = TealLevel.debug
        TealPrint.level = self.log_level

    def set_from_config_file(self, args: ConfigFileArgs) -> None:
        if args.port:
            self.port = args.port


config = Config()
