# -*- encoding: utf-8 -*-

"""
About the Tanzanite application.
"""

# Standard import
import logging

# External imports
from cliff.command import Command

# Local imports
from tanzanite import _copyright as tz_copyright
from tanzanite.utils import (
    add_browser_options,
    get_version,
    open_browser,
)


class CmdAbout(Command):
    """
    Output information about the ``tanzanite`` CLI.

    This includes version number, copyright, and related information (which
    isn't easy to force ``autoprogram-cliff`` to parse correctly in ``help``
    output, so it isn't shown here).

    The ``--readthedocs`` option will open a browser to the ``tanzanite``
    documentation web page.

    ABOUT THE BROWSER OPEN FEATURE

    This program uses the Python ``webbrowser`` module to open a
    browser.

        https://docs.python.org/3/library/webbrowser.html

    This module supports a large set of browsers for various operating
    system distributions. It will attempt to chose an appropriate
    browser from operating system defaults.  If it is not possible to
    open a graphical browser application, it may open the ``lynx`` text
    browser.

    You can choose which browser ``webbrowser`` will open using the
    identifier from the set in the ``webbrowser`` documentation.
    Either specify the browser using the ``--browser`` option on the
    command line, or export the environment variable ``BROWSER``
    set to the identifier (e.g., ``export BROWSER=firefox``).

    It is also possible to set the ``BROWSER`` environment variable
    to a full path to an executable to run. On Windows 10 with Windows
    Subsystem for Linux, you can use this feature to open a Windows
    executable outside of WSL. (E.g., using
    ``export BROWSER='/c/Program Files/Mozilla Firefox/firefox.exe'``
    will open Firefox installed in that path).

    Also note that when this program attempts to open a browser,
    an exception may be thrown if the process has no TTY. If this
    happens, use the ``--force`` option to bypass this behavior and
    attempt to open the browser anyway.
    """

    logger = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument(
            '--readthedocs',
            action='store_true',
            dest='readthedocs',
            default=False,
            help='Open a browser to the ``tanzanite`` ReadTheDocs page'
        )
        parser = add_browser_options(parser)
        return parser

    def take_action(self, parsed_args):
        if parsed_args.readthedocs:
            docs_url = "https://tanzanite.readthedocs.io"
            # TODO(dittrich): Add option to use the locally served version
            self.logger.info('[+] opening url %s in browser', docs_url)
            open_browser(
                url=docs_url,
                browser=parsed_args.browser,
                force=parsed_args.force
            )
        else:
            version = get_version()
            if (
                self.app_args.verbose_level < 1
                or self.cmd_name == "version"
            ):
                self.app.stdout.write(f'{version}\n')
            else:
                # Hacking formatting for `tanzanite help` by adding a tab here.
                self.app.stdout.write(
                    f'{self.app.argv0} version {version}\n{tz_copyright()}\n'
                )


# vim: set ts=4 sw=4 tw=0 et :
