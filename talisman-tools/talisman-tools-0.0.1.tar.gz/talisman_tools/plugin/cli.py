from .abstract import AbstractPluginManager


class CLIPluginManager(AbstractPluginManager):
    def __init__(self):
        AbstractPluginManager.__init__(self, 'CLI_OPTIONS')

    @staticmethod
    def _check_value(value) -> bool:
        return isinstance(value, set)  # TODO: improve validation
