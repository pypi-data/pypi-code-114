from configparser import ConfigParser
from os.path import expanduser, join as pj


class AWSConfigReviewer(object):
    def __init__(self) -> None:
        self.__aws_config = self.read_awsclient_config()

    def read_awsclient_config(self) -> list:
        """Reads aws command line client config from default location"""
        config = ConfigParser()
        path = pj(expanduser("~"), ".aws/config")
        try:
            with open(path) as f:
                config.read_file(f)
        except FileNotFoundError:
            raise

        return [
            profile.split()[1] for profile in config.sections() if "profile" in profile
        ]

    @property
    def aws_config(self) -> list:
        return self.__aws_config
