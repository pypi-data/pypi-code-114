#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Building formats for Pensum.

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

import os
import shutil

from pathlib import Path
from typing import NoReturn

import pypandoc

# Variables globales 1/2 ================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

# Classes ===============================================================#


class Builder:
    def __init__(self, base, **kwargs):
        self.base = base
        self.options = kwargs
        self.failed = {}

        self.building = False

    def get_option(self, option_name, onlytrue=False):
        if option_name not in self.options:
            return None

        if onlytrue:
            if bool(self.options[option_name]):
                return self.options[option_name]

            return None

        return self.options[option_name]

    def handle_fail(self, note, details) -> NoReturn:
        """
        Predefined method for collecting the build failure of a note.
        """
        self.failed[note] = details

    def build_note(self, note):
        """
        Predefined method for building one note.

        As this method is empty, it can't fail.
        """

        return True, {}

    def build_all(self):
        """
        Predefined method for building all notes.

        Collect every note building fail.
        """

        self.building = "all"

        for note_object in self.base.notes.values():
            result, details = self.build_note(note_object)

            if not result:
                self.handle_fail(note_object, details)

        self.building = False

    def start(self):
        """
        Predefined method executed before any conversion command.
        """
        pass

    def end(self):
        """
        Predefined method executed after any conversion command.
        """
        pass


class BasicPandocBuilder(Builder):
    def __init__(self, base, **kwargs):
        Builder.__init__(self, base, **kwargs)

        self.output = {
            "folder": None,
            "extension": "txt",
            "format": "html",
            "default_name": "output",
            "skiped_sections": ["id", "tags"],
        }

    def start(self):
        self.output["folder"] = self.get_option("output_folder")

        if self.output["folder"] is None:
            self.output["folder"] = Path.cwd() / self.output["default_name"]
        else:
            self.output["folder"] = Path(self.output["folder"]).resolve()

        self.output["folder"].mkdir(exist_ok=True)

    def pandoc_extra_args(self, extra_args):
        return extra_args

    def build_note(self, note):
        md_content = note.to_markdown(
            skiped_sections=self.output["skiped_sections"]
        )

        # Manage extra arguments -----------------------------------------

        extra_args = []
        extra_args = self.pandoc_extra_args(extra_args)

        if self.get_option("verbose", True):
            if extra_args:
                print("Pandoc arguments :", extra_args)

        # ----------------------------------------------------------------

        file_name = "{}.{}".format(note.note_id, self.output["extension"])
        output_path = self.output["folder"] / file_name

        pypandoc.convert_text(
            md_content,
            self.output["format"],
            format="md",
            outputfile=str(output_path),
            extra_args=extra_args,
        )

        # ----------------------------------------------------------------

        # Everything fine
        return True, {}


class DokuWiki(BasicPandocBuilder):
    """
    DokuWiki export.
    """

    def __init__(self, base, **kwargs):
        BasicPandocBuilder.__init__(self, base, **kwargs)

        self.output["format"] = "dokuwiki"
        self.output["default_name"] = "wiki_output"
        self.output["skiped_sections"] = ["id", "tags"]


class MediaWiki(BasicPandocBuilder):
    """
    MediaWiki export.
    """

    def __init__(self, base, **kwargs):
        BasicPandocBuilder.__init__(self, base, **kwargs)

        self.output["format"] = "mediawiki"
        self.output["default_name"] = "wiki_output"
        self.output["skiped_sections"] = ["id", "tags"]


class HTML(Builder):
    """
    HTML export.
    """

    def __init__(self, base, **kwargs):
        Builder.__init__(self, base, **kwargs)

        self.output_folder = None

    def start(self):
        self.output_folder = self.get_option("output_folder")

        if self.output_folder is None:
            self.output_folder = Path.cwd() / "html_output"
        else:
            self.output_folder = Path(self.output_folder).resolve()

        self.output_folder.mkdir(exist_ok=True)

    def build_all(self):
        Builder.build_all(self)

        # Manage extra arguments -----------------------------------------

        extra_args = ["--standalone", "--metadata", "title=Pensum notes"]

        css_toc = self.get_option("css_toc")

        if css_toc is not None:
            css_toc = Path(css_toc).resolve()
            css_out = self.output_folder / css_toc.name

            if css_toc.exists():
                extra_args.append("--css={}".format(str(css_toc)))

                shutil.copy(str(css_toc), str(css_out))

        # ----------------------------------------------------------------

        md_content = "\n"

        for note_object in self.base.notes.values():
            note_title = note_object.title
            note_id = note_object.note_id

            line = f"- [{note_title}]({note_id}.html)\n"
            md_content += line

        md_content += "\n"

        # ----------------------------------------------------------------

        output_path = self.output_folder / "index.html"

        pypandoc.convert_text(
            md_content,
            "html",
            format="md",
            outputfile=str(output_path),
            extra_args=extra_args,
        )

        if css_toc is not None:
            # Pandoc writes CSS filepath as given in arguments so we fix
            # the path from absolute to relative.

            code = ""
            with open(str(output_path), "r", encoding="utf8") as mdo:
                code = mdo.read()

            code = code.replace(str(css_toc.parent) + os.sep, "")
            with open(str(output_path), "w", encoding="utf8") as mdo:
                mdo.write(code)

        # ----------------------------------------------------------------

    def build_note(self, note):
        md_content = note.to_markdown(
            skiped_sections=["id", "title", "tags"], tags_format="singular"
        )

        # Manage extra arguments -----------------------------------------

        extra_args = ["--standalone", "--metadata", f"title={note.title}"]

        css_note = self.get_option("css_note")

        if css_note is not None:
            css_note = Path(css_note).resolve()
            css_out = self.output_folder / css_note.name

            if css_note.exists():
                extra_args.append("--css={}".format(str(css_note)))

                shutil.copy(str(css_note), str(css_out))

        if self.get_option("verbose", True):
            if extra_args:
                print("Pandoc arguments :", extra_args)

        # Add link to index page -----------------------------------------

        if self.building == "all":
            md_content = "<nav>[Index](index.html)</nav>\n\n" + md_content
            md_content += "\n\n<footer>[Index](index.html)</footer>"

        # ----------------------------------------------------------------

        output_path = self.output_folder / f"{note.note_id}.html"

        pypandoc.convert_text(
            md_content,
            "html",
            format="md",
            outputfile=str(output_path),
            extra_args=extra_args,
        )

        if css_note is not None:
            # Pandoc writes CSS filepath as given in arguments so we fix
            # the path from absolute to relative.

            code = ""
            with open(str(output_path), "r", encoding="utf8") as mdo:
                code = mdo.read()

            code = code.replace(str(css_note.parent) + os.sep, "")
            with open(str(output_path), "w", encoding="utf8") as mdo:
                mdo.write(code)

        # ----------------------------------------------------------------

        # Everything fine
        return True, {}


class PensumBuilder(Builder):
    """
    Pensum notes builder.
    """

    def build_note(self, note):
        build_path = self.base.folder / f"{note.note_id}.md"
        result = note.to_file(build_path)

        if not result:
            # Error details to complete with raised exceptions found
            details = {}

            if self.building == "all":
                # Avoid handling fail two times as build_all will do that.
                return False, details

            # Handle the fail when building this note is not a part of build
            # all notes
            self.handle_fail(note, details)
            return False, details

        # Everything fine
        return True, {}


# Variables globales 2/2 ================================================#

FORMATS = {
    "html": HTML,
    "pensum": PensumBuilder,
    "dokuwiki": DokuWiki,
    "mediawiki": MediaWiki,
}

# vim:set shiftwidth=4 softtabstop=4:
