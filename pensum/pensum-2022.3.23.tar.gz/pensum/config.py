#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Pensum configuration.

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

import copy
import json

from pathlib import Path
from typing import Optional

import stop_words

from pensum.common import PathOrString

# Variables globales ====================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

# Classes ===============================================================#


class Configuration:
    """
    Pensum configuration object.
    """

    def __init__(self):
        self.filepath = None

        self.settings = {
            # Lang
            "lang": "en",
            # PM : command line for pensum -------------------------------
            "pm": {
                # Use a pager (generally "less") in the following command
                "pager": {
                    "help": True,
                    "cat": False,
                    "ls": False,
                    "search": False,
                },
                # Topics display options
                "topics": {
                    # Code coloration theme. Defaults to rich default.
                    "theme": "monokai",
                },
                # Text editor
                "editor": "edit",
            },
            # Builders ---------------------------------------------------
            "builders": {
                # HTML
                "html": {
                    "css_note": None,
                    "css_toc": None,
                }
            },
            # "running" key in settings : for temporary values related to
            # Pensum client like "pm". This, in order to avoid saving
            # OS / client related data into configuration.
            # "running" { temporary data }
        }

    def set(self, value, **kwargs) -> bool:
        """
        Set configuration option.
        """

        def cast_bool(option_value):
            """
            Tries to convert value to boolean.
            """

            try:
                tmp = {"yes": True, "no": False}[option_value.lower()]
                return tmp
            except KeyError:
                raise TypeError from KeyError

        # Tries some conversions with value -------------------------

        casted = None

        try:
            casted = cast_bool(value)
        except TypeError:
            pass

        if casted is not None:
            value = casted

        modified = False

        # Save after setting option ---------------------------------

        if (save_opt := kwargs.get("save")) is None:
            save = False
        else:
            save = bool(save_opt)

        # -----------------------------------------------------------

        if (key := kwargs.get("key")) is None:
            raise ValueError("Tried to set option without any group.")

        if (group := kwargs.get("group")) is None:
            if key in self.settings:
                self.settings[key] = value
                modified = True

        else:
            if (subgroup := kwargs.get("subgroup")) is None:
                if group in self.settings:
                    if key in self.settings[group]:
                        self.settings[group][key] = value
                        modified = True
            else:
                if group in self.settings:
                    if subgroup in self.settings[group]:
                        if key in self.settings[group][subgroup]:
                            self.settings[group][subgroup][key] = value
                            modified = True

        # -----------------------------------------------------------

        if modified and save:
            self.save()

        return modified

    def set_from_locator(
        self, locator: str, value, save: bool = False
    ) -> bool:
        """
        Return configuration values following the syntax group.value.subvalue…

        lang => Configuration.settings["lang"]
        lang.tui => Configuration.settings["lang"]["tui"]
        lang.tui.msg => Configuration.settings["lang"]["tui"]["msg"]
        …
        """

        locator = locator.split(".")

        modified = False

        if len(locator) == 1:
            # lang -> lang
            modified = self.set(value, key=locator[0])

        if len(locator) == 2:
            # builder.x -> builder.x
            modified = self.set(value, group=locator[0], key=locator[1])

        if len(locator) == 3:
            # builder.html.css_note -> builder.html.css_note
            modified = self.set(
                value, group=locator[0], subgroup=locator[1], key=locator[2]
            )

        if modified and save:
            self.save()

        return modified

    def get(self, locator: str):
        """
        Return configuration values following the syntax group.value.subvalue…

        lang => Configuration.settings["lang"]
        lang.tui => Configuration.settings["lang"]["tui"]
        lang.tui.msg => Configuration.settings["lang"]["tui"]["msg"]
        …
        """

        locator = locator.split(".")

        proxy = self.settings

        for part in locator:
            if part in proxy:
                proxy = proxy[part]

        return proxy

    def get_build_options(self, build_format):
        """
        Returns build options of build format build_format.
        """

        if build_format in self.settings["builders"]:
            return self.settings["builders"][build_format]

        return {}

    def check_lang(self) -> bool:
        """
        Checks main lang settings.
        """

        lang = self.settings["lang"].lower().strip()

        for code, complete in stop_words.LANGUAGE_MAPPING.items():
            if lang == code:
                return True

            if lang == complete:
                self.settings["lang"] = code
                return True

        return False

    def from_file(self, filepath: PathOrString, create: bool = False) -> bool:
        """
        Load configuration from filepath file.
        """

        if not isinstance(filepath, Path):
            filepath = Path(filepath)

        self.filepath = filepath.resolve()

        try:
            with open(str(self.filepath), "r", encoding="utf8") as cfg:
                data = cfg.read()
                self.settings = json.loads(data)
        except FileNotFoundError:
            if create:
                self.save()
            else:
                raise FileNotFoundError(
                    str(self.filepath)
                ) from FileNotFoundError

        self.settings["running"] = {
            "config_file": str(filepath),
        }

        return True

    def save(self) -> bool:
        """
        Save configuration.
        """

        source_data = copy.deepcopy(self.settings)

        # Remove datas related to Pensum running
        if "running" in source_data:
            source_data.pop("running")

        data = json.dumps(source_data)

        with open(str(self.filepath), "w", encoding="utf8") as cfg:
            cfg.write(data)

        return True


if __name__ == "__main__":
    test = Configuration()
    print(test.settings)

    test.set_from_locator("lang", "fr")
    test.set_from_locator("builders.html.css_note", "ABC")

    test.set("de", key="lang")
    test.set("DEF", group="builders", subgroup="html", key="css_toc")
    test.set("araire", group="boite", key="outil")

    print(test.settings)

    print(test.get("pm.pager.help"))
    print(test.get("pm.pager.cat"))


# vim:set shiftwidth=4 softtabstop=4:
