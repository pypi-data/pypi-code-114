from gocd_tools.cli.defaults import SECRETS, SERVER
from gocd_tools.cli.run import cli_exec
from gocd_tools.cli.secrets import add_secrets_groups
from gocd_tools.cli.server import add_server_groups


def setup_cli(parser):
    setup_commands = parser.add_subparsers(title="COMMAND")

    # Secrets
    secrets_parser = setup_commands.add_parser(SECRETS)
    add_secrets_groups(secrets_parser)
    secrets_commands = secrets_parser.add_subparsers(title="COMMAND")
    secrets_init_parser = secrets_commands.add_parser("init")
    secrets_init_parser.set_defaults(
        func=cli_exec,
        module_path="gocd_tools.secrets",
        module_name="secrets",
        func_name="init_secrets_dir",
    )

    secrets_configure_parser = secrets_commands.add_parser("configure")
    secrets_configure_parser.set_defaults(
        func=cli_exec,
        module_path="gocd_tools.secrets",
        module_name="secrets",
        func_name="configure_secrets",
    )

    secrets_del_parser = secrets_commands.add_parser("del")
    secrets_del_parser.set_defaults(
        func=cli_exec,
        module_path="gocd_tools.secrets",
        module_name="secrets",
        func_name="del_secrets_dir",
    )

    # Server
    server_parsers = setup_commands.add_parser(SERVER)
    add_server_groups(server_parsers)
    server_commands = server_parsers.add_subparsers(title="COMMAND")
    server_init_parser = server_commands.add_parser("init")
    server_init_parser.set_defaults(
        func=cli_exec,
        module_path="gocd_tools.server",
        module_name="server",
        func_name="init_server",
    )

    server_configure_parser = server_commands.add_parser("configure")
    server_configure_parser.set_defaults(
        func=cli_exec,
        module_path="gocd_tools.server",
        module_name="server",
        func_name="configure_server",
    )
