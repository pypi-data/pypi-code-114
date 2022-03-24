#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: set ts=4
#
# Copyright 2021-present Linaro Limited
#
# SPDX-License-Identifier: MIT

from tuxbake.argparse import setup_parser
from tuxbake.build import build
from tuxbake.models import OEBuild
import json


##############
# Entrypoint #
##############
def run(options) -> int:
    main()
    return


def main() -> int:
    # Parse command line
    parser = setup_parser()
    options = parser.parse_args()
    with open(options.build_definition) as reader:
        build(
            **(json.load(reader)),
            src_dir=options.src_dir,
            build_dir=options.build_dir_name,
            local_manifest=options.local_manifest,
        )


def start():
    if __name__ == "__main__":
        sys.exit(main())
