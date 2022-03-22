"""Entry point for the hdev script."""
import os
import sys
from argparse import ArgumentParser, Namespace
from functools import cached_property
from pathlib import Path

from hdev import command


class HParser(ArgumentParser):
    """Overwrites ArgumentParser to control the `error` behaviour."""

    def error(self, message):
        """Change the default behavior to print help on errors."""
        sys.stderr.write(f"error: {message}\n")
        self.print_help()
        sys.exit(2)


class HArgs(Namespace):  # pylint: disable=too-few-public-methods
    """A child of Namespace which adds HDev specific tweaks."""

    @cached_property
    def project(self):
        """Get the project associated with this call if any.

        This is based on the specified `--project-dir`.

        :return: A project
        :raise EnvironmentError: If the project directory cannot be found
            from the specified directory or any of it's parents.
        """
        # pylint: disable=import-outside-toplevel
        from hdev.model.project import Project

        # pylint: disable=no-member
        # The member is added by the parser
        return Project.from_child_dir(self._project_dir)


def create_parser():
    """Create the root parser for the `hdev` command."""

    parser = HParser()

    parser.add_argument(
        "--project",
        metavar="PROJECT_DIR",
        dest="project_dirs",
        action="append",
        type=Path,
        help="Path of the project's root. Defaults to '.'. "
        "Can be specified multiple times",
    )

    parser.add_argument(
        "--find",
        dest="find",
        metavar="FIND_COMMAND",
        help="Find projects from the current directory. This can be one of "
        "'APPS', 'LIBS', 'ANY' or a comma separated list of project names.",
    )

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debugging info",
    )

    subparsers = parser.add_subparsers(required=True, dest="sub_command")

    for sub_command in [
        command.Alembic(),
        command.Clean(),
        command.Config(),
        command.Deps(),
        command.InstallPython(),
        command.PythonVersion(),
        command.Requirements(),
        command.Run(),
        command.Template(),
    ]:
        sub_command.add_to_parser(subparsers)

    return parser


def main():
    """Create an argsparse cmdline tools to expose hdev functionality.

    Main entry point of hdev
    """
    parser = create_parser()
    args = parser.parse_args(namespace=HArgs())
    handler = args.handler

    for project_dir in _get_project_dirs(args):
        _run_command(parser, handler, args, project_dir)


def _get_project_dirs(args):
    if args.find:
        # pylint: disable=import-outside-toplevel
        from hdev.model.project import Project

        kwargs = {}
        if args.find == "APPS":
            kwargs["filter_type"] = Project.Type.APPLICATION
        elif args.find == "LIBS":
            kwargs["filter_type"] = Project.Type.LIBRARY
        elif args.find == "ANY":
            ...
        elif args.find.isupper():
            raise ValueError(
                f"Unknown find command: {args.find}. Did you mean one of APPS, LIBS or ANY?"
            )
        else:
            kwargs["filter_name"] = [name.strip() for name in args.find.split(",")]

        return list(
            project.root_dir for project in Project.find(dir_path=Path("."), **kwargs)
        )

    if not args.project_dirs:
        return [Path(".")]

    return args.project_dirs


def _run_command(parser, handler, args, project_dir):
    # pylint: disable=import-outside-toplevel
    from copy import deepcopy

    # Always switch to the target directory before we start work
    os.chdir(project_dir)

    args = deepcopy(args)
    # pylint: disable=protected-access
    args._project_dir = project_dir

    try:
        handler(args)

    except SystemExit:  # pylint: disable=try-except-raise
        # The handler is controlling the exit, and we should respect that
        raise

    except Exception as err:  # pylint: disable=broad-except
        if args.debug:
            raise

        # Another error has been raised, so dump it and print the help too
        print(f"Error: {err}\n")
        parser.print_usage()
        sys.exit(2)


if __name__ == "__main__":  # pragma: nocover
    main()
