"""Sub-command of `hdev` to manipulate requirements files."""
import sys

from hdev.command.sub_command import SubCommand


class Requirements(SubCommand):
    """Sub-command of `hdev` to manipulate requirements files."""

    name = "requirements"
    help = "Compiles .txt requirements file based on the existing .in files using pip-tools"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""

        parser.add_argument(
            "--package",
            required="--file" in sys.argv,
            dest="package",
            help="Upgrade a single package or set it to a specific version. "
            "Use `package-name` for the latest, or `package-name=1.2.3` "
            "for a specific version",
        )

        parser.add_argument(
            "--file",
            dest="upgrade_targets",
            nargs="+",
            help="If --package is specified, limit upgrades to this specific "
            "requirements file. Can be specified multiple times",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        # pylint: disable=import-outside-toplevel
        from hdev.command.requirements._lazy import LazyRequirements

        LazyRequirements()(args)
