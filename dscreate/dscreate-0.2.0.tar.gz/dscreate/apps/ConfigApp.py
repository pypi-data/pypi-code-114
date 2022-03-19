from .BaseApp import DsCreate
import os

class ConfigApp(DsCreate):

    name = 'ConfigApp'
    description = '''
    Prints the path for a dscreate configuration file.
    If a subcommand is provided, a configuration filepath is printed for that specific application.

    If not subcommand is provided, the global configuration file is printed.
    '''

    def start(self) -> None:
        if len(self.extra_args) == 0:
            print(os.path.join(self.dsconfig, 'ds', self.config_file_name))
        elif len(self.extra_args):
            path = os.path.join(self.dsconfig, self.extra_args[0], self.config_file_name)
            print(path)