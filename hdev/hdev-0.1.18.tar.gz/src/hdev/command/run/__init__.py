"""Sub-command of `hdev` to run custom commands."""
from hdev.command.sub_command import SubCommand


class Run(SubCommand):
    """Sub-command of `hdev` to run custom commands."""

    name = "run"
    help = "Run a custom command defined in the pyproject.toml file"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""

        parser.add_argument("command_name", nargs="*", help="Run a named command")
        parser.add_argument(
            "--command", "-c", help="Run a custom command instead of a named one"
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # pylint: disable=import-outside-toplevel
        from hdev.command.run._lazy import LazyRun

        LazyRun()(args)
