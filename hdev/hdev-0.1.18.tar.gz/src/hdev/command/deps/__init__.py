"""Sub-command of `hdev` to list dependencies."""
from hdev.command.sub_command import SubCommand


class Deps(SubCommand):
    """Sub-command of `hdev` to list dependencies."""

    name = "deps"
    help = "Get dependency information"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument("--package", "-p", help="Get details of a specific package")

        parser.add_argument(
            "--json",
            "-j",
            action="store_true",
            help="Dump json data about the dependencies instead of text",
        )

        parser.add_argument(
            "--graph",
            "-g",
            action="store_true",
            help="Graph the dependencies",
        )

        parser.add_argument(
            "--python-version",
            default="3.9",
            help="Specify the target python version (for graphing)",
        )

        parser.add_argument(
            "--python-version-max",
            help="Specify the max python version (for graphing)",
        )

        parser.add_argument(
            "--show",
            "-s",
            action="store_true",
            help="Open the graph for viewing once made",
        )

        parser.add_argument(
            "--output-file",
            "-o",
            help="Specify a filename (for graphing)",
        )

        parser.add_argument(
            "--verbose",
            "-v",
            action="store_true",
            help="Dump additional data",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # pylint: disable=import-outside-toplevel
        from hdev.command.deps._lazy import LazyDeps

        LazyDeps()(args)
