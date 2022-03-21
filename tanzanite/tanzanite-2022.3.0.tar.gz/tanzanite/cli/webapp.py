# -*- encoding: utf-8 -*-

"""
Open the Tanzanite web application.
"""

# Standard imports
import logging

# External imports
from cliff.command import Command

# Local imports
from tanzanite.utils import (
    add_browser_options,
    get_base_url,
    open_browser,
)


class CmdWebapp(Command):
    """
    Open the Tanzanite web application.

    Open the base URL for the ``tanzanite`` web application main page.
    For information about the browser feature, see ``help about``.
    """

    logger = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser = add_browser_options(parser)
        return parser

    def take_action(self, parsed_args):
        open_browser(
            url=get_base_url(),
            browser=parsed_args.browser,
            force=parsed_args.force,
        )


# vim: set ts=4 sw=4 tw=0 et :
