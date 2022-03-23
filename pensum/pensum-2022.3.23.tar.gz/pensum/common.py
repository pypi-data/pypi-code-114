#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Common variables and functions for Pensum.

Copyright (C) 2022  Etienne Nadji

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more
details.

You should have received a copy of the GNU Affero General Public License along
with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# Imports ===============================================================#

import importlib.resources as pkg_resources

from pathlib import Path

from typing import Union, Optional

import pensum.topics as topics

# Variables globales ====================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

PathOrString = Union[Path, str]
StringOrNone = Optional[str]

# Fonctions =============================================================#


def load_topic(name: str) -> str:
    """
    Load Pensum help topic from markdown source in Pensum package.
    """
    return pkg_resources.read_text(topics, f"{name}.md")


# vim:set shiftwidth=4 softtabstop=4:
