"""Sub-command of `hdev` to clean projects."""
from hdev.command.sub_command import SubCommand


class Clean(SubCommand):
    """Sub-command of `hdev` to print out python version information."""

    name = "clean"
    help = "Clean a project directory"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument(
            "--all",
            "-a",
            action="store_true",
            help="Clean everything we know how to clean.",
        )

        parser.add_argument(
            "--deep",
            "-d",
            action="store_true",
            help="Clean items which might be slow to rebuild like tox and node modules",
        )

        parser.add_argument(
            "--branches",
            "-b",
            action="store_true",
            help="Clean and prune old and detached git branches as well",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # pylint: disable=import-outside-toplevel
        from hdev.command.clean._lazy import LazyClean

        LazyClean()(args)
