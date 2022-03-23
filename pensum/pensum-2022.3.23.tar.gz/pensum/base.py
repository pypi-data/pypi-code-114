#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""
Notes database of Pensum.

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

from pathlib import Path
from typing import Literal, Union, List, Dict

import stop_words

from pensum.common import PathOrString, StringOrNone
from pensum.notes import Note, NoteTag, NoteDoesNotExists

# Variables globales ====================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

Lang = Literal[list(stop_words.LANGUAGE_MAPPING.keys())]
NoteOrBool = Union[Note, bool]

# Classes ===============================================================#


class Notes:
    """
    Notes database of Pensum.
    """

    def __init__(self):
        self.folder = None
        self.notes = {}

        self.agregates = {}

    def new_note(self, note_id: str, note_title: StringOrNone = None) -> Path:
        """
        Make a new note file named note_id.md, with note_title if not None.

        :param note_id: Note ID
        :type note_id: str
        :param note_title: Note title. "New note" if None.
        :type note_title: Union[str, None]
        :returns: Note filepath
        :rtype: pathlib.Path
        """

        if note_id is None:
            return False

        note_path = self.folder / f"{note_id}.md"

        note = Note()
        note.title = {True: "New note", False: note_title}[note_title is None]
        note.short = "Summary of what this note is about."
        note.note_id = note_id
        note.command = "—"
        note.discussion = "—"
        note.tags.append(NoteTag("placeholder{s}"))

        note.to_file(note_path)

        return note_path

    def add_note(self, note: Note, agregates: bool = False) -> bool:
        """
        Add note to the base.

        :param note: Note to add
        :type note: pensum.notes.Note
        :param agregates: Refresh search agregates.
        :type agregates: bool
        :returns: Success
        :rtype: bool
        """

        self.notes[note.note_id] = note

        if agregates:
            self.agregates["tags"] = self.agregated_tags()
            self.agregates["titles"] = self.agregated_titles()

        return True

    def load(self, folder_path: PathOrString) -> bool:
        """
        Load all notes from folder_path.
        """

        self.folder = folder_path

        for note_path in self.folder.glob("*.md"):
            try:
                new_note = Note()
                success = new_note.from_file(note_path)
            except NoteDoesNotExists:
                success = False

            if success:
                self.add_note(new_note)

        self.agregates["tags"] = self.agregated_tags()
        self.agregates["titles"] = self.agregated_titles()

        return True

    def matching_tag(self, tag_request: str) -> List[Note]:
        """
        Search notes using tag tag_request in base agregate.

        :param tag_request: Tag name
        :type tag_request: str
        :returns: List of notes
        :rtype: List[pensum.notes.Note]
        """

        results = []

        for tag, notes in self.agregates["tags"].items():
            if tag.match(tag_request):
                results += notes

        return results

    def matching_title(self, request: str, lang: Lang = "fr") -> List[Note]:
        """
        Search notes using title request in base agregate.

        :param request: title request
        :type request: str
        :param lang: lang code for performing a title search without stop words
        :type lang: str
        :returns: List of notes
        :rtype: List[pensum.notes.Note]
        """

        def basic_matching(base, request):
            return [
                note
                for title, note in base.agregates["titles"].items()
                if request.lower() in title.lower()
            ]

        results = []

        if lang is not None:
            try:
                skiped_words = stop_words.get_stop_words(lang)

                new_request = [
                    word
                    for word in request.split()
                    if word not in skiped_words
                ]

                if new_request:

                    for title, note in self.agregates["titles"].items():
                        note_title = [
                            note_word.lower() for note_word in title.split()
                        ]

                        for word in new_request:
                            if word.lower() in note_title:
                                if note not in results:
                                    results.append(note)
                                    break

                    if results:
                        return results

            except stop_words.StopWordError:
                pass

        results = basic_matching(self, request)

        return results

    def agregated_titles(self) -> Dict[str, List[Note]]:
        return {note.title: note for note in self.notes.values()}

    def agregated_tags(self) -> Dict[NoteTag, List[Note]]:
        tmp = {}

        for note in self.notes.values():

            for tag in note.tags:
                if tag.__repr__() not in tmp:
                    tmp[tag.__repr__()] = []

                tmp[tag.__repr__()].append(note)

        agregate = {}

        for tag_string, notes in tmp.items():
            agregate[NoteTag(tag_string)] = notes

        return agregate

    def by_tag(self, tag_string: str) -> List[Note]:
        """
        Returns all notes with tag matching matching tag_string.
        """

        return [
            note for note in self.notes.values() if note.has_tag(tag_string)
        ]

    def by_id(self, note_id: str) -> NoteOrBool:
        """
        Return the note matching note_id.
        """

        if note_id in self.notes:
            return self.notes[note_id]

        return False


# vim:set shiftwidth=4 softtabstop=4:
