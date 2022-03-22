#!/usr/bin/env python

"""mite-cli

Usage:
    mite-cli new <project_dir> [options]

Options:
    --log-level=LEVEL       Set logger level: DEBUG, INFO, WARNING, ERROR, CRITICAL [default: INFO]
    -e --createvenv         Create a python virtual environment
"""  # noqa: E501

import logging

from docopt import docopt

from .new_project import new_project

logger = logging.getLogger(__name__)


def setup_logging(opts):
    logging.basicConfig(
        level=opts["--log-level"],
        format="<%(levelname)s> %(message)s",
        force=True,
    )


def main():
    opts = docopt(__doc__)
    setup_logging(opts)
    if opts["new"]:
        new_project(opts["<project_dir>"], opts["--createvenv"])


if __name__ == "__main__":
    main()
