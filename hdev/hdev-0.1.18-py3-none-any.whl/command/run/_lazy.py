"""Lazy loaded command content for Run."""

from subprocess import check_call


class LazyRun:  # pylint: disable=too-few-public-methods
    def __call__(self, args):
        """Run the command.

        :param args: An ArgParser Namespace object
        """
        if args.command:
            check_call(args.command, shell=True)
            return

        config = args.project.config.get("tool.hdev.run", {})
        self._run_command(config, command_name=args.command_name[0], debug=args.debug)

    @classmethod
    def _run_command(cls, config, command_name, debug=False):
        command_details = config.get(command_name)
        if not command_details:
            raise ValueError(
                f"No such command found: '{command_name}'. "
                f"Did you mean one of: {list(config.keys())}"
            )

        shell_command = command_details.get("command")
        if not shell_command:
            raise ValueError(f"Expected to find key 'command' in: {command_details}")

        if debug:
            print(f"Running: {shell_command}")

        check_call(shell_command, shell=True)
