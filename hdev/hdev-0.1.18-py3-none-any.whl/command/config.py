"""Sub-command to print, reformat and run items from pyproject.toml."""
from hdev.command.sub_command import SubCommand


class Config(SubCommand):
    """Sub-command to print, reformat and run items from pyproject.toml."""

    name = "config"
    help = "Get format and run data from pyproject.toml"

    @classmethod
    def configure_parser(cls, parser):
        """Set up arguments needed for the sub-command."""

        parser.add_argument(
            "path", nargs="?", help="Option to read. e.g. 'tool.option'"
        )

        parser.add_argument(
            "--if",
            dest="conditional",
            action="store_true",
            help="Only continue if the value is truthy",
        )

        parser.add_argument(
            "--run",
            "-r",
            action="store_true",
            help="Execute the value as a bash command",
        )

        parser.add_argument(
            "--template", "-t", help="A python format string to template the value into"
        )

        parser.add_argument(
            "--pretty",
            "-p",
            action="store_true",
            help="Format the output with more whitespace",
        )

        parser.add_argument(
            "--raw",
            action="store_true",
            help="Output data as it appears in Python (default is JSON)",
        )

    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        :raise TypeError: If asked to "run" anything other than a string
        """

        value = args.project.config

        # Get a specific value from the config rather than all of it
        if args.path:
            value = value.get(args.path)

        # Bail out if the value isn't truthy
        if args.conditional and not value:
            return

        # Apply a python string template to the value (no error handling)
        if args.template:
            value = args.template.format(value)

        # Run the string as a command
        if args.run:
            if not isinstance(value, str):
                raise TypeError(f"Can only execute strings not: {type(value)}")

            # pylint: disable=import-outside-toplevel
            from subprocess import check_output

            value = check_output(value, shell=True).decode("utf-8")

        # ... or format it to JSON
        elif not args.raw:
            # pylint: disable=import-outside-toplevel
            import json

            if args.pretty:
                value = json.dumps(value, indent=4, sort_keys=True)
            else:
                value = json.dumps(value)

        # Print the results
        if args.pretty:
            print(value)
        else:
            # Don't emit a new line to make this easy to splat into the middle
            # of other scripts
            print(value, end="")
