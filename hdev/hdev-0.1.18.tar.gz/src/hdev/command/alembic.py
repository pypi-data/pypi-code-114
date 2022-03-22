"""Sub-command of `hdev` to run Alembic (DB migrations) commands."""
import argparse

from hdev.command.sub_command import SubCommand


class Alembic(SubCommand):
    """Sub-command of `hdev` to run Alembic (DB migrations) commands."""

    name = "alembic"
    help = "Run alembic commands to create and execute DB migrations."

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""
        parser.add_argument(
            "alembic_args",
            nargs=argparse.REMAINDER,
            help="Arguments to pass to alembic.",
        )

    def __call__(self, args):
        """Run the command."""
        # pylint: disable=import-outside-toplevel
        from hdev.tox_cmd import run_tox

        alembic_config_file = args.project.root_dir / "conf/alembic.ini"

        run_tox(
            "dev", f'alembic -c {alembic_config_file} {" ".join(args.alembic_args)}'
        )
