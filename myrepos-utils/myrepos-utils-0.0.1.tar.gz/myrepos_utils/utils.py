#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (c) Michel Alexandre Salim
#
# Fedora-License-Identifier: GPLv2+
# SPDX-2.0-License-Identifier: GPL-2.0+
# SPDX-3.0-License-Identifier: GPL-2.0-or-later
#
# This program is free software.
# For more information on the license, see COPYING.md.
# For more information on free software, see
# <https://www.gnu.org/philosophy/free-sw.en.html>.

import configparser
import os

CONFIG = configparser.ConfigParser()
CONFIG.read(os.path.expanduser("~/.mrconfig"))


def get_repos(config: configparser.ConfigParser = CONFIG) -> list[str]:
    return list(config.keys())


def find_repo(
    query: list[str], config: configparser.ConfigParser = CONFIG
) -> list[str]:
    import re

    repos = get_repos(config)
    r = f".*{'.*'.join(query)}.*"
    return [os.path.expanduser(f"~/{repo}") for repo in repos if re.match(r, repo)]
