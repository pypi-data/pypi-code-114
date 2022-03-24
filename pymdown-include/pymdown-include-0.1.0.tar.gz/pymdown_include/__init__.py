# Copyright 2020 Jacques Supcik
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import re
import sys
from pathlib import Path

from markdown import Markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

logger = logging.getLogger(__name__)


MIN_PYTHON = (3, 7)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

INCLUDE_RE = re.compile(r"\{!\s*(?P<filename>.+?)\s*!(?P<flags>.*?)\}")
HEAD_RE = re.compile(r"^(?P<heading>#+)")


class PymdownInclude(Extension):
    def __init__(self, **kwargs):
        self.config = {
            "SEARCH_PATH": [[Path(".")], "search_path"],
            "ENCODING": ["utf-8", "encoding"],
        }
        super(PymdownInclude, self).__init__(**kwargs)

    def extendMarkdown(self, md: Markdown):
        """Add pieces to Markdown."""
        logger.debug("Registering extension")
        md.preprocessors.register(PymdownIncludePreprocessor(self), "include", 26)

    def open_file(self, file_name: str):
        logger.debug("Opening: %s", file_name)
        path = Path(file_name).expanduser()
        encoding = self.getConfig("ENCODING")
        if not path.is_absolute():
            for base in self.getConfig("SEARCH_PATH"):
                p: Path = base / path
                logger.debug("Considering: %s", p)
                if p.is_file():
                    path = p
                    break
            else:
                raise Exception(f"I can't find {file_name}")
        return open(path, mode="rt", encoding=encoding)


class PymdownIncludePreprocessor(Preprocessor):
    def __init__(self, extension: Extension):
        self.extension = extension

    def readlines(
        self, filename: str, flags: str, prolog: str, epilog: str, heading_level: int
    ):
        logger.debug("Importing: %s", filename)
        with self.extension.open_file(filename) as file:
            res = [line.rstrip() for line in file]
            if "#" in flags:

                def f(l):
                    m = HEAD_RE.search(l)
                    return (
                        m.group("heading") + "#" * heading_level + m.string[m.end() :]
                        if m
                        else l
                    )

                res = [f(l) for l in res]
            else:
                m0 = re.search(r"\+(\d+)", flags)
                if m0:

                    def f(l):
                        m = HEAD_RE.search(l)
                        return (
                            m.group("heading")
                            + "#" * int(m0.group(1))
                            + m.string[m.end() :]
                            if m
                            else l
                        )

                    res = [f(l) for l in res]

            if "*" in flags:
                res = [prolog + l for l in res]
            elif ">" in flags:
                res = [prolog + l for l in res[0:1]] + [
                    " " * len(prolog) + l for l in res[1:]
                ]
            else:
                res[0] = prolog + res[0]
            res[-1] = res[-1] + epilog
            return res

    def run(self, lines):
        logger.debug("Running...")
        result = list()
        hl = 0
        while len(lines) > 0:
            line = lines.pop(0)
            m = HEAD_RE.search(line)
            if m:
                hl = len(m.group("heading"))
            m = INCLUDE_RE.search(line)
            if m is None:
                result.append(line)
            else:
                included_lines = self.readlines(
                    filename=m.group("filename"),
                    flags=m.group("flags"),
                    prolog=m.string[0 : m.start()],
                    epilog=m.string[m.end() :],
                    heading_level=hl,
                )
                lines = included_lines + lines

        return result


def makeExtension(**kwargs):  # pragma: no cover
    """Return an instance of the PymdownIncludeExtension"""
    return PymdownInclude(**kwargs)
