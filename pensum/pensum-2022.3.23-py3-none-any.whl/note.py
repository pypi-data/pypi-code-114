#!/usr/bin/python3
# -*- coding:Utf-8 -*-

import re
import json

from pathlib import Path

from pensum.common import PathOrString, StringOrNone


class NoteDoesNotExists(Exception):
    pass


class NoteTag:

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
        return search.lower().strip() in [
            term for term in [self.singular, self.plural] if term is not None
        ]

    # TODO plutôt intégrer ça comme __str__ ?
    def to_string(self) -> str:
        if self.plural_side is None:
            return self.singular

        if self.plural_side == "left":
            return "{" + self.plural_mark + "}" + self.singular

        if self.plural_side == "right":
            return self.singular + "{" + self.plural_mark + "}"

    def from_string(self, tag_string: str) -> bool:
        tag_string = tag_string.strip()

        # No plural version of this tag

        if not "{" in tag_string:
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


class Note:
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

    def has_tag(self, tag_string: str) -> bool:
        for tag in self.tags:
            if tag.match(tag_string):
                return True

        return False

    def to_markdown(self) -> str:
        sections = []

        if self.title is not None:
            sections.append(f"# {self.title}\n")

        if self.tags:
            formatted_tags = ",".join([tag.to_string() for tag in self.tags])
            tags_section = "## Tags\n\n" + formatted_tags + "\n"
            sections.append(tags_section)

        if self.command is not None:
            command_section = "## Command\n\n"
            command_section += f"```\n{self.command}\n```\n"
            sections.append(command_section)

        return "\n".join(sections)

    def to_json(self):
        """
        JSON export for use by pensum (indexation of the note)
        """
        pass

    def to_file(self, filepath: PathOrString, json_entry: bool = False):
        """
        Save the note in a Markdown file.

        :param json_entry: Returns a JSON entry for pensum
        """
        pass

    def from_path(self, filepath: PathOrString):
        filepath = Path(filepath)

        if not filepath.exists():
            raise NoteDoesNotExists()

        with open(str(filepath), "r", encoding="utf8") as mdsource:
            markdown_string = mdsource.read()
            self.from_markdown(markdown_string)

    def from_markdown(self, markdown_string: str):
        pass
