#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/28 10:00
# @Author  : Lifeng
# @Site    : 
# @File    : cli.py
# @Software: PyCharm


import sys
import logging
import argparse
from dfwsgroup_ios import __description__, __version__
from dfwsgroup_ios.ios.script import gain_fastbot_runner, command_main


def main():
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        "-V", "--version", dest="version", action="store_true", help="show version"
    )
    subparsers = parser.add_subparsers()
    gain_fastbot_runner(subparsers)
    args = parser.parse_args()

    if sys.argv[1] == "run":
        sys.exit(command_main(args))
    elif sys.argv[1] in ["-V", "--version"]:
        if parser.parse_args().version:
            print(f"version：{__version__}")
    else:
        logging.error(f"{sys.argv[1:]}")
        raise Exception
