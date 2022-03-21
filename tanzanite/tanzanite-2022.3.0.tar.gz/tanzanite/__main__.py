# -*- encoding: utf-8 -*-

"""The Tanzanite purpleteaming and CTF platform."""

# See the COPYRIGHT variable in tanzanite/__init__.py (also found
# in output of ``tanzanite help``).

# Standard imports
import os
import sys
import textwrap

from pathlib import Path

# External imports
from dotenv import load_dotenv

# pylint: disable=wrong-import-order,ungrouped-imports
#
# Replace cliff SmartHelpFormatter class before first use.
# NOTE: Each cliff subcommand gets its own parser that inherits the
# "SmartHelpFormatter" class. The app itself does not, so it is set
# explicitly below.
#
from tanzanite.utils import CustomFormatter
from cliff import _argparse
_argparse.SmartHelpFormatter = CustomFormatter


from cliff.app import App
from cliff.commandmanager import CommandManager
from psec.exceptions import SecretNotFoundError
from psec.utils import (
    get_default_environment,
    show_current_value,
    umask,
    Timer,
)
# pylint: enable=wrong-import-order,ungrouped-imports


# # Local imports
from tanzanite import (
    DEFAULT_UMASK,
    TANZANITE_DATA_DIR,
    _copyright as tanzanite_copyright
)
from tanzanite.core import app_logger
from tanzanite.utils import get_version


if sys.version_info < (3, 7, 0):
    print(f"The { os.path.basename(sys.argv[0]) } program "
          "prequires Python 3.7.0 or newer\n"
          "Found Python { sys.version }", file=sys.stderr)
    sys.exit(1)


ARGV = sys.argv[1:]
DEFAULT_ENVIRONMENT = get_default_environment()

# The `.env` file support is intended to make it easier to
# have consistent behavior between CLI and API components.
# For best security, DO NOT put any secrets in that file,
# rather put them in a `python-secrets` environment and
# only set `D2_ENVIRONMENT` and `D2_SECRETS_BASEDIR` and
# any other variables controlling program behavior (e.g.,
# setting `TANZANITE_DEBUG` for debugging features),
# not project configuration settings that are better
# managed with `python-secrets`.
env_specific_dotenv = Path(f'.env.{DEFAULT_ENVIRONMENT}').absolute()
dotenv_path = (
    str(env_specific_dotenv)
    if env_specific_dotenv.exists()
    else str(Path('.env').absolute())
)
load_dotenv(dotenv_path=dotenv_path)


# TODO(dittrich): Add this to psec secrets?
AUTO_LOGIN_SUPERUSER = os.environ.get(
    'TANZANITE_AUTO_LOGIN_SUPERUSER'
) is not None


class TanzaniteApp(App):
    """The Tanzanite purpleteaming and CTF platform."""

    def __init__(self):
        super().__init__(
            description=__doc__.strip(),
            version=get_version(),
            command_manager=CommandManager(
                namespace='tanzanite'
            ),
            deferred_help=True,
        )
        self.environment = None
        self.timer = Timer()
        self.secrets = None
        self.auth_token = None
        self.auth_token_header = None
        self.settings = None
        self.argv0 = Path(sys.argv[0]).name

    def build_option_parser(self, description, version, argparse_kwargs=None):
        parser = super().build_option_parser(
            description,
            version
        )
        # Ensure the `formatter_class` is set properly for the app itself.
        parser.formatter_class = CustomFormatter
        # Global options
        parser.add_argument(
            '-D', '--data-dir',
            metavar='<data-directory>',
            dest='data_dir',
            default=TANZANITE_DATA_DIR,
            help=('Root directory for holding data files '
                  '(Env: ``TANZANITE_DATA_DIR``)')
        )
        parser.add_argument(
            '--elapsed',
            action='store_true',
            dest='elapsed',
            default=False,
            help='Show elapsed time (and ASCII bell) on exit'
        )
        parser.add_argument(
            '-e', '--environment',
            metavar='<environment>',
            dest='environment',
            default=DEFAULT_ENVIRONMENT,
            help='Deployment environment selector (Env: ``D2_ENVIRONMENT``)'
        )
        parser.add_argument(
            '-P', '--env-var-prefix',
            metavar='<prefix>',
            dest='env_var_prefix',
            default=None,
            help='Prefix string for environment variables'
        )
        parser.add_argument(
            '-E', '--export-env-vars',
            action='store_true',
            dest='export_env_vars',
            default=False,
            help='Export secrets as environment variables'
        )
        parser.add_argument(
            '--umask',
            metavar='<umask>',
            type=umask,
            default=oct(DEFAULT_UMASK),
            help='Mask to apply during app execution'
        )
        parser.add_argument(
            '--disallow-auth-token-cache',
            action='store_true',
            default=False,
            help='Do not cache JWT in secrets environment directory'
        )
        parser.epilog = textwrap.dedent(f"""
        For help information on individual commands, use ``tanzanite <command> --help``.

        Several commands have features that will attempt to open a browser. See
        ``tanzanite about --help`` to see help information about this feature and how
        to control which browser(s) will be used.

        To improve overall security when doing this, a default process umask of
        {DEFAULT_UMASK:#05o} is set when the app initializes. When running programs like the
        example above where they create sensitive files in the environment
        directory, this reduces the chance that secrets created during execution
        will end up with overly broad permissions.  If you need to relax these
        permissions, use the ``--umask`` option to apply the desired mask.

        Note that ``tanzanite`` directly invokes some ``cliff`` command classes
        from ``python-secrets``. These commands are identified in the command list
        below in parentheses.  The side-effect of this is that some of the
        ``--help`` output for these commands refers to ``psec`` instead of
        ``tanzanite`` in the text.  Don't let this confuse you! ;)  Also, not all
        command line options that are supported by ``psec`` are supported by
        ``tanzanite``, so if you need to do things like changing the base directory
        for storing secrets, do so by using ``psec -E run`` with the options you need
        and in turn run ``tanzanite``.

        Environment variables consumed:
          BROWSER                Default browser for use by webbrowser.open().{show_current_value('BROWSER')}
          D2_ENVIRONMENT         Default python-secrets environment identifier.{show_current_value('D2_ENVIRONMENT')}
          D2_SECRETS_BASEDIR     Secrets environment storage root directory.{show_current_value('D2_SECRETS_BASEDIR')}
          TANZANITE_DEBUG        Enable debugging.{show_current_value('TANZANITE_DEBUG')}

        { tanzanite_copyright() }""")  # noqa
        return parser

    def configure_logging(self):
        """
        Create logging handlers for any log output.
        """
        log_file = self.options.log_file
        app_logger.global_configure_logging(
            log_file=log_file,
            verbose_level=self.options.verbose_level,
            stderr=self.stderr,
            log_file_message_format=self.LOG_FILE_MESSAGE_FORMAT,
            console_message_format=self.CONSOLE_MESSAGE_FORMAT,
        )

    def initialize_app(self, argv):
        self.LOG.debug('[*] initialize_app')
        # # Ensure that the debugging environment variable is set such that
        # # it aligns with the command line argument so programs and
        # # subprocesses that don't have access to `self.options` variables
        # # behave the same.
        # debug_str = "true" if self.options.debug else "false"
        # if (
        #     'TANZANITE_DEBUG' not in os.environ
        #     or os.environ.get('TANZANITE_DEBUG').lower() == 'false'
        # ):
        #     os.environ['TANZANITE_DEBUG'] = debug_str
        # self.options.debug = (
        #     (os.environ.get('TANZANITE_DEBUG').lower() == 'true')
        #     or self.options.debug
        # )
        self.set_environment(self.options.environment)
        # Ensure `psec` environment matches `tanzanite` environment name.
        os.environ['D2_ENVIRONMENT'] = self.options.environment
        if len(argv) > 0 and (argv[0] not in ['about', 'complete', 'help']):
            # Load configuration from default python-secrets environment
            # and export environment variables for use by programs running
            # in child processes (e.g., Vagrant, Packer, etc.) to access.
            # self.secrets = SecretsEnvironment(
            #     environment=self.options.environment,
            #     export_env_vars=True,
            #     verbose_level=self.options.verbose_level,
            #     env_var_prefix=self.options.env_var_prefix,
            # )
            # if not self.secrets.environment_exists():
            #     sys.exit(
            #         f"environment '{str(self.get_environment())}' "
            #         "does not exist (try 'psec environments list'?)"
            #     )
            # self.secrets.read_secrets_and_descriptions()
            #
            # Now we can create the settings object from exported secrets.
            from tanzanite.core.config import (  # pylint: disable=import-outside-toplevel  # noqa: E501
                settings,
                secrets_environment,
            )
            self.settings = settings
            self.secrets = secrets_environment

    def prepare_to_run_command(self, cmd):
        self.LOG.debug(
            '[+] command line: %s',
            " ".join([arg for arg in sys.argv])
        )
        os.umask(self.options.umask)
        # The `run` command will always require exporting environment
        # variables.
        setattr(self, 'export_env_var', True)
        if self.options.elapsed:
            self.timer.start()
        # Ensure command classes contain the `requires_login` attribute
        # when authentication is required.
        # TODO(dittrich): use a decorator instead?
        if (
            getattr(cmd, 'requires_login', False) is True
            and self.auth_token is None
        ):
            from tanzanite.core.security import ( # pylint: disable=import-outside-toplevel  # noqa
                get_cached_auth_token,
                get_jwt_path,
                cli_login_for_access_token,
            )

            must_log_in = f"[-] not logged in: use '{self.argv0} login' first"
            username, password = None, None
            jwt_path = get_jwt_path()
            auth_token = get_cached_auth_token(jwt_path=jwt_path)
            if auth_token is not None:
                self.LOG.debug("[+] already logged in")
            else:
                # FIXME when code is stable
                if True:  # AUTO_LOGIN_SUPERUSER is True:
                    try:
                        username = self.secrets.get_secret(
                            "tanzanite_admin_user_email"
                        )
                        password = self.secrets.get_secret(
                            "tanzanite_admin_password"
                        )
                    except SecretNotFoundError:
                        sys.exit(must_log_in)
                auth_token = cli_login_for_access_token(
                    jwt_path=jwt_path,
                    cache_auth_token=(
                        not self.options.disallow_auth_token_cache
                    ),
                    username=username,
                    password=password,
                )
                if auth_token is None:
                    sys.exit(must_log_in)
            self.auth_token = auth_token
            self.auth_token_header = {
                "token": f"Bearer {self.auth_token}"
            }

    def clean_up(self, cmd, result, err):
        self.LOG.debug('[*] clean_up %s', cmd.__class__.__name__)
        if self.options.elapsed:
            self.timer.stop()
            elapsed = self.timer.elapsed()
            if result != 0:
                self.LOG.debug('[!] elapsed time: %s', elapsed)
            elif (
                self.options.verbose_level >= 0
                and cmd.__class__.__name__ != "CompleteCommand"
            ):
                self.stderr.write(f'[+] elapsed time {elapsed}\n')
                if sys.stdout.isatty():
                    self.stderr.write('\a')
                    self.stderr.flush()

    def set_environment(self, environment=DEFAULT_ENVIRONMENT):
        """Set variable for current environment"""
        self.environment = environment

    def get_environment(self):
        """Get the current environment setting"""
        return self.environment


def main(argv=sys.argv[1:]):  # pylint: disable=dangerous-default-value
    """
    Command line interface for the ``tanzanite`` project.
    """

    try:
        myapp = TanzaniteApp()
        result = myapp.run(argv)
    except KeyboardInterrupt:
        sys.stderr.write("\nReceived keyboard interrupt: exiting\n")
        result = 1
    return result


if __name__ == '__main__':
    # Ensure that running program with either "python -m tanzanite"
    # or just "tanzanite" result in same argv.
    argv0 = Path(sys.argv[0])
    sys.argv[0] = (
        argv0.parent.name
        if argv0.name == '__main__.py'
        else argv0.name
    )
    sys.exit(main(sys.argv[1:]))


# vim: set ts=4 sw=4 tw=0 et :
