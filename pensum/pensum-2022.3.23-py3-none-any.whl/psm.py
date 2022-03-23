#!/usr/bin/python3
# -*- coding:Utf-8 -*-

"""Pensum, a command lines reminder.

Usage:
  psm.py ls [<tag>]
  psm.py cat <note_id> [-d] [-s] [-t]
  psm.py new <note_id> [<note_title>]
  psm.py find <request>
  psm.py build <format> [<output_folder>] [--verbose]
  psm.py option (set|get) [<option_name>] [<option_value>] [--verbose]
  psm.py help [<topic>]

Options:
  -h --help  Displays help.
  --verbose  Verbosity of info command
  -d         Hide Discussion section
  -s         Hide short
  -t         Hide title

For a more detailed help, type "psm help psm".

Pensum, by Étienne Nadji.
"""

# Imports ===============================================================#

import re
import sys
import subprocess

from typing import NoReturn, Union

from pathlib import Path

try:
    import docopt

    arguments = docopt.docopt(__doc__, version="0.1")
except ImportError:
    print("Missing python package : docopt")
    sys.exit(1)

try:
    from appdirs import AppDirs
except ImportError:
    print("Missing python package : appdirs")
    sys.exit(1)

try:
    from rich import box
    from rich.table import Table
    from rich.padding import Padding
    from rich.console import Console
    from rich.markdown import Markdown
except ImportError:
    print("Missing python package : rich")
    sys.exit(1)

import pensum.base as database
import pensum.config as config
import pensum.builders as builders

from pensum.common import StringOrNone, load_topic

# Variables globales ====================================================#

__author__ = "Etienne Nadji <etnadji@eml.cc>"

# Classes ===============================================================#


class PensumCLI:
    """
    Command line for Pensum.
    """

    commands = ["find", "ls", "build", "cat", "new", "help", "option"]
    build_formats = ["html"]

    search_tag_pattern = re.compile("@(.*)")

    def __init__(
        self,
        notes: database.Notes,
        args: dict,
        configuration: config.Configuration,
    ):
        self.base = notes
        self.config = configuration
        self.arguments = args
        self.console = Console()
        self.pager = self.console.pager(styles=True)

        # Loading help topics ---------------------------------------

        if (topic_theme := self.config.get("psm.topics.theme")) is None:
            topic_theme = "monokai"

        self.topics = {
            topic_name: Markdown(
                load_topic(topic_name), code_theme=topic_theme
            )
            for topic_name in ["buildformats", "psm"]
        }

    def get_command(self) -> StringOrNone:
        """
        Return the name of the command used or None.
        """

        for arg_name in self.arguments:
            if arg_name in PensumCLI.commands:
                if self.arguments[arg_name]:
                    return arg_name

        return None

    def get_argument(self, arg_name, onlytrue=False) -> Union[str, bool, None]:
        """
        Get argument from docopt arguments or None.
        """

        if arg_name in self.arguments:
            if onlytrue:
                return bool(self.arguments[arg_name])

            return self.arguments[arg_name]

        return None

    def verbose(self) -> bool:
        """
        Are we in a verbose mode ?
        """
        return self.arguments["--verbose"] is not None

    def do_new(self) -> int:
        """
        Create a new note with <note_id> ID and maybe <note_title> title.
        """

        new_id = self.get_argument("<note_id>")
        new_title = self.get_argument("<note_title>")

        note_path = self.base.new_note(new_id, new_title)

        if not note_path:
            return 1

        args = ["edit", str(note_path)]

        subprocess.Popen(" ".join(args), shell=True)

        return 0

    def do_build(self) -> int:
        """
        Build the notes in <format>.
        """

        build_format = None

        for format_code in PensumCLI.build_formats:
            if arguments["<format>"].lower() == format_code:
                build_format = format_code
                break

        if build_format is None:
            return 1

        if build_format not in builders.FORMATS:
            return 1

        cli_options = {"verbose": self.verbose()}

        if arguments["<output_folder>"] is not None:
            cli_options["output_folder"] = arguments["<output_folder>"]

        config_options = self.config.get_build_options(build_format)
        options = {**cli_options, **config_options}

        builder = builders.FORMATS[build_format](self.base, **options)
        builder.start()
        builder.build_all()

        return 0

    def do_cat(self) -> int:
        """
        cat a command line note.
        """

        note = self.base.by_id(self.arguments["<note_id>"])

        skiped_sections = ["id", "tags"]

        for arg_name, section in {
            "-t": "title",
            "-s": "short",
            "-d": "discussion",
        }.items():
            if self.get_argument(arg_name, True):
                skiped_sections.append(section)

        # not note : who's there ?
        if not note:
            return 1

        if self.config.get("psm.pager.cat"):
            with self.pager:
                self.console.print(
                    # ID and Tags are skiped
                    Padding(
                        Markdown(note.to_markdown(skiped_sections)),
                        pad=1,
                    )
                )
        else:
            self.console.print(
                # ID and Tags are skiped
                Padding(
                    Markdown(note.to_markdown(skiped_sections)),
                    pad=1,
                )
            )

        return 0

    def do_list(self) -> int:
        """
        List all the notes or only notes matching <tag>.
        """

        # --- Prepare the table --------------------------------

        table = Table(title="Notes", box=box.MINIMAL)

        table.add_column("ID", no_wrap=True)
        table.add_column("Title")
        table.add_column("Tags", justify="right")

        # --- Select the notes to display ----------------------

        selection = []

        if arguments["<tag>"] is None:
            selection = self.base.notes.values()
        else:
            selection = self.base.by_tag(arguments["<tag>"])

        # There is no notes with that tag => this a fine result
        if not selection and arguments["<tag>"] is not None:
            return 0

        # There is no notes in the base => an empty base is an error
        if not selection and arguments["<tag>"] is None:
            return 1

        # --- Make the rows ------------------------------------

        rows = [
            [
                note.note_id,
                note.title,
                ", ".join([str(tag) for tag in note.tags]),
            ]
            for note in selection
        ]

        for row in rows:
            table.add_row(*row)

        # --- Shows the table ----------------------------------

        if self.config.get("psm.pager.ls"):
            with self.pager:
                self.console.print(Padding(table, pad=1))
        else:
            self.console.print(Padding(table, pad=1))

        return 0

    def do_search(self) -> int:
        """
        Search across the notes.

        <request> by default, search request across titles
        <request> @user starts a tag "user" search instead
        """

        request = self.arguments["<request>"]
        results = []

        test_tag = PensumCLI.search_tag_pattern.match(request)

        if bool(test_tag):
            tag_request = test_tag.groups()[0]
            results = self.base.matching_tag(tag_request)
        else:
            results = self.base.matching_title(
                request, self.config.get("lang")
            )

        if not results:
            return 0

        results = list(set(results))

        # --- Prepare the table --------------------------------

        table = Table(title="Notes", box=box.MINIMAL)

        table.add_column("ID", no_wrap=True)
        table.add_column("Title")
        table.add_column("Tags", justify="right")

        # --- Make the rows ------------------------------------

        rows = [
            [
                note.note_id,
                note.title,
                ", ".join([str(tag) for tag in note.tags]),
            ]
            for note in results
        ]

        for row in rows:
            table.add_row(*row)

        # --- Shows the table ----------------------------------

        if self.config.get("psm.pager.search"):
            with self.pager:
                self.console.print(Padding(table, pad=1))
        else:
            self.console.print(Padding(table, pad=1))

        return 0

    def do_help(self) -> int:
        """
        Shows help related to <topic>.
        """

        cli_topic = self.get_argument("<topic>")

        if cli_topic is None:
            print("Pensum help topics :\n")

            for topic_name in self.topics.keys():
                print(f" - {topic_name}")

            print("")

            return 0

        if cli_topic not in self.topics:
            return 1

        if self.config.get("psm.pager.help"):
            with self.pager:
                self.console.print(Padding(self.topics[cli_topic], pad=1))
        else:
            self.console.print(Padding(self.topics[cli_topic], pad=1))

        return 0

    def do_option(self) -> int:
        """
        Set or get option.
        """

        option_name = self.get_argument("<option_name>")
        option_value = self.get_argument("<option_value>")

        if self.get_argument("get", True):

            if option_name is None:
                print(self.config.settings)
            else:
                value = self.config.get(option_name)
                print(value)

            return 0

        if self.get_argument("set", True):
            if option_value is None:
                return 1

            setted = self.config.set_from_locator(
                option_name, option_value, True
            )

            if not setted:
                return 1

            if self.verbose():
                print(f"{option_name}='{option_value}'")

            return 0

        return 1

    def run(self) -> int:
        """
        Run the CLI commands.
        """

        command = self.get_command()

        if command is None:
            return 1

        return {
            "ls": self.do_list,
            "cat": self.do_cat,
            "new": self.do_new,
            "help": self.do_help,
            "find": self.do_search,
            "build": self.do_build,
            "option": self.do_option,
        }[command]()


# Fonctions =============================================================#


def main() -> NoReturn:
    """
    Entry point for Pensum cli / shell
    """

    # --- Folders, paths, etc ------------------------------

    folders = AppDirs(appname="Pensum")

    # Notes

    data_dir = Path(folders.user_data_dir)
    data_dir.mkdir(exist_ok=True)

    notes = database.Notes()
    notes.load(data_dir)

    # Configuration

    config_dir = Path(folders.user_config_dir)
    config_dir.mkdir(exist_ok=True)

    config_file = config_dir / "config.json"

    configuration = config.Configuration()
    configuration.from_file(config_file, True)

    # --- One command line ---------------------------------

    cli = PensumCLI(notes, arguments, configuration)
    sys.exit(cli.run())


# vim:set shiftwidth=4 softtabstop=4:
