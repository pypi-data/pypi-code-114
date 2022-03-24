#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: set ts=4
#
# Copyright 2021-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import argparse


##########
# Setups #
##########
def setup_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="tuxbake", description="TuxBake")
    #    parser.add_argument(
    #    "--version", action="version", version=f"%(prog)s, {__version__}"
    # )
    group = parser.add_argument_group("OE Build Parameters")
    group.add_argument(
        "--build-definition",
        help="Specify json file with build parameters",
        required=True,
    )
    group.add_argument(
        "--src-dir", help="source directory where the sources will be downloaded", default=None
    )
    group.add_argument(
        "--build-dir-name",
        help="Directory name passed to the source script during OE build. It defaults to build",
        default="build",
    )
    group.add_argument(
        "--local-manifest",
        help="Path to a local manifest file which will be used to override repo setup before doing repo sync. This input is ignored if sources used is git_trees in the build definition",
        default=None,
    )
    return parser
