#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Notes and notes tags for Pensum.

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

import re

from pathlib import Path
from typing import NoReturn

from pensum.common import PathOrString, StringOrNone


class NoteDoesNotExists(Exception):
    """
    This note (and probably the file related to) does not exist.
    """


class NoteTag:
    """
    Note tag.

    Handle singular and plural variants.
    """

    alt_pattern = re.compile("(.*)\|(.*)")
    end_pattern = re.compile("(.*){(.*)}")
    start_pattern = re.compile("{(.*)}(.*)")

    def __init__(self, tag_string: StringOrNone = None):
        self.singular = None
        self.plural = None

        self.plural_side = None
        self.plural_mark = None

        if tag_string is not None:
            self.from_string(tag_string)

    def match(self, search: str) -> bool:
        """
        Does the search search matches with singular or plural variant of
        this tag ?
        """

        return search.lower().strip() in [
            term.lower()
            for term in [self.singular, self.plural]
            if term is not None
        ]

    def __str__(self) -> str:
        """
        str conversion only returns the singular, as the string representing
        singular and plural variants of the tag are not usefull in that
        context.
        """

        if self.singular is None:
            return ""

        return self.singular

    def __repr__(self) -> str:
        """
        Return a string representing the formatted tag with plural information.
        """

        if self.plural_side is None:
            return self.singular

        if self.plural_side == "alternative":
            return f"{self.singular}|{self.plural}"

        if self.plural_side == "left":
            return "{" + self.plural_mark + "}" + self.singular

        if self.plural_side == "right":
            return self.singular + "{" + self.plural_mark + "}"

    def from_string(self, tag_string: str) -> bool:
        """
        Loads tag content from a string, including singular and plural
        variant.

        :type tag_string: str
        :param tag_string: String representing the tag and it's plural variant.
                           More details below.

        Tag string
        ----------

          If you don't want to define a plural variant of your tag, the tag
          string is only… the tag name.

            "Debian"

          Tags are always evaluated case-insensitively. If your note has
          tags "debian", "Debian", Pensum will export "debian,Debian"

          There is two ways to to define singular and plural. By an alternative
          or by affixes (prefix or suffix).

          - Affixes :
            - `"user{s}"` produce singular "user" and plural "users".
            - `"{every }user"` produce singular "user" and plural "every user".

          - Alternative :

            In that case, order is always singular, plural.

            `"terminal|terminaux"` produce singular "terminal" and plural
            "terminaux".
        """

        tag_string = tag_string.strip()

        if not "{" in tag_string:
            test_alt = NoteTag.alt_pattern.match(tag_string)

            # a|b tag string produce singular "a" and plural "b"

            if bool(test_alt):
                self.singular = test_alt.groups()[0]
                self.plural = test_alt.groups()[1]
                self.plural_side = "alternative"
                return True

            # No plural version of this tag

            self.singular = tag_string

            return True

        # disk{s} tag string produce singular "disk" and plural "disks"

        test_start = NoteTag.end_pattern.match(tag_string)

        if bool(test_start):
            self.singular = test_start.groups()[0]
            self.plural = "".join(test_start.groups())
            self.plural_side = "right"
            self.plural_mark = test_start.groups()[1]
            return True

        # Plural mark before singular word

        test_end = NoteTag.start_pattern.match(tag_string)

        if bool(test_end):
            self.singular = test_end.groups()[1]
            self.plural = "".join(test_end.groups())
            self.plural_side = "left"
            self.plural_mark = test_end.groups()[0]
            return True

        return False


class Note:
    """
    Command line note.
    """

    atx1 = re.compile("# (.*)")
    atx2 = re.compile("## (.*)")

    def __init__(self):
        # Note tags
        self.tags = []
        # Note title (header 1 of the Markdown file)
        self.title = None
        # Main command (## Command section)
        self.command = None
        # Short description of the note (paragraph following note title)
        self.short = None
        # Discussion of the command (## Discussion section)
        self.discussion = None
        # Note ID
        self.note_id = None
        self.new_id = None

        self.filepath = None

    def has_tag(self, tag_string: str) -> bool:
        """
        Does this note use that tag ?
        """

        for tag in self.tags:
            if tag.match(tag_string):
                return True

        return False

    def to_markdown(self, skiped_sections=[], tags_format="raw") -> str:
        """
        Returns a Markdown string representing the note.

        :type skiped_sections: list
        :param skiped_sections: List of sections to avoid when making the
                                Markdown string. Can contain :
                                "short", "id", "tags", "command", "discussion"
        :rtype: str
        """

        def section(level, title, data=False):
            text = f"{'#'*level} {title}\n"

            if data:
                text += "\n"
                text += data
                text += "\n"

            return text

        def md_code(data):
            return f"```\n{data}\n```"

        sections = []

        if self.title is not None:
            if "title" not in skiped_sections:
                sections.append(section(1, self.title))

        if self.short is not None:
            if "short" not in skiped_sections:
                sections.append(f"{self.short.strip()}\n")

        if self.note_id is not None:
            if "id" not in skiped_sections:
                sections.append(section(2, "ID", self.note_id.strip()))

        if self.tags:
            if "tags" not in skiped_sections:
                if tags_format == "singular":
                    formatted_tags = ",".join(
                        [str(tag) for tag in self.tags]
                    ).strip()
                else:
                    formatted_tags = ",".join(
                        [tag.__repr__() for tag in self.tags]
                    ).strip()

                sections.append(section(2, "Tags", formatted_tags))

        if self.command is not None:
            if "command" not in skiped_sections:
                sections.append(
                    section(2, "Command", md_code(self.command.strip()))
                )

        if self.discussion is not None:
            if "discussion" not in skiped_sections:
                sections.append(
                    section(2, "Discussion", self.discussion.strip())
                )

        return "\n".join(sections)

    def to_file(self, filepath: PathOrString) -> bool:
        """
        Save the note in a Markdown file.

        :type filepath: Union[pathlib.Path, str]
        :param filepath: File path
        """
        md_content = self.to_markdown()

        with open(str(filepath), "w", encoding="utf8") as mdout:
            mdout.write(md_content)

        return True

    def from_file(self, filepath: PathOrString) -> bool:
        """
        Loads note from a Markdown file.

        :type filepath: Union[pathlib.Path, str]
        :param filepath: File path
        """

        filepath = Path(filepath)

        if not filepath.exists():
            raise NoteDoesNotExists()

        self.filepath = filepath.resolve()

        success = False

        with open(str(filepath), "r", encoding="utf8") as mdsource:
            markdown_string = mdsource.read()
            success = self.from_markdown(markdown_string.split("\n"))

        return success

    def tags_from_string(self, tags_string) -> NoReturn:
        tags = []

        raw = [
            raw_string.strip()
            for raw_string in tags_string.split(",")
            if raw_string.strip()
        ]

        for raw_tag in raw:
            tag = NoteTag()
            success = tag.from_string(raw_tag)

            if not success:
                continue

            tags.append(tag)

        self.tags = tags

    def set_id(self, new_id) -> NoReturn:
        if self.filepath is None:
            self.note_id = new_id
            return

        if self.filepath.stem == new_id:
            self.note_id = new_id
        else:
            self.new_id = new_id

    def remove_old_note_id(self) -> NoReturn:
        if self.new_id is None:
            return

        # New filepath from new_id
        new_filepath = self.filepath.parent / f"{self.new_id}.md"

        # Update self.note_id and export to new filepath
        self.note_id = self.new_id
        self.to_file(new_filepath)

        # Remove old filepath, fix self.filepath with the new one
        self.filepath.unlink()
        self.filepath = new_filepath

        self.new_id = None

    def from_markdown(self, markdown_string: str) -> bool:
        """
        Loads note content from a Markdown string.
        """

        if not markdown_string:
            return False

        parsing_done = []
        skip_next_empty = False
        parsing_codeblock = False

        for line in markdown_string:

            # Skip the line if it is empty and we request so --------

            if not line.strip() and skip_next_empty:
                skip_next_empty = False
                continue

            # Search for level 1 : note title -----------------------

            test_title = Note.atx1.match(line)

            if bool(test_title):
                self.title = test_title.groups()[0]
                parsing_done.append("title")
                skip_next_empty = True
                continue

            # Search for level 2 sections ---------------------------

            test_level2 = Note.atx2.match(line)

            if bool(test_level2):
                header = test_level2.groups()[0]

                if header == "ID":
                    parsing_done.append("short")

                # if header in ["Tags", "Command", "Discussion"]:
                # pass

                skip_next_empty = True

                continue

            # Discussion --------------------------------------------

            if parsing_done == ["title", "short", "id", "tags", "command"]:
                if self.discussion is None:
                    self.discussion = ""

                if line.strip():
                    self.discussion += f"{line}\n"
                else:
                    self.discussion += "\n"

                continue

            # Command -----------------------------------------------

            if parsing_done == ["title", "short", "id", "tags"]:

                # Start and end of code block -------------

                if line.strip().startswith("```"):
                    parsing_codeblock = not (parsing_codeblock)

                    if not parsing_codeblock:
                        self.command = self.command.strip()
                        parsing_done.append("command")

                    continue

                # -----------------------------------------

                if self.command is None:
                    self.command = ""

                if line.strip():
                    self.command += f"{line}\n"
                else:
                    self.command += "\n"

                continue

            # TAGS --------------------------------------------------

            if parsing_done == ["title", "short", "id"]:
                if not line.strip():
                    continue

                self.tags_from_string(line.strip())

                parsing_done.append("tags")
                continue

            # ID ----------------------------------------------------

            if parsing_done == ["title", "short"]:
                if not line.strip():
                    continue

                self.set_id(line.strip())
                parsing_done.append("id")
                continue

            # SHORT -------------------------------------------------

            if parsing_done == ["title"]:
                if not line.strip():
                    continue

                if self.short is None:
                    self.short = ""

                self.short += line
                continue

        if self.new_id is not None:
            self.remove_old_note_id()

        return True


def test_filepath(filepath) -> NoReturn:
    note = Note()
    note.from_file(filepath)
    print("-----------")
    print("Titre :", note.title)
    print("Short :", note.short)
    print("ID :", note.note_id)

    print()

    print("Tags :")
    for tag in note.tags:
        print(" -", tag.singular, tag.plural)

    print()

    for idx, line in enumerate(note.command.strip().split("\n")):
        print(idx, line)

    print()

    for idx, line in enumerate(note.discussion.strip().split("\n")):
        print(idx, line)


# vim:set shiftwidth=4 softtabstop=4:
