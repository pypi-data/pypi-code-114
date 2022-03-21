# Copyright Louis Paternault 2021-2022
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Plugin log progress."""

import contextlib
import logging
import threading

from ..hooks import contexthook
from . import Plugin


class Logging(Plugin):
    """Log stuff"""

    # pylint: disable=too-few-public-methods

    keyword = "logging"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lock = threading.Lock()
        self.logger = logging.getLogger("evariste.tree")
        self.count = 0
        self.total = 0

    @contexthook("Builder.compile")
    @contextlib.contextmanager
    def compile_builder(
        self, builder, *args, **kwargs
    ):  # pylint: disable=unused-argument
        """Save the total number of files to compile."""
        self.total = builder.tree.count()
        yield

    @contexthook("File.compile")
    @contextlib.contextmanager
    def compile_file(self, tree):
        """Log file compilation (including progress)."""
        with self.lock:
            self.count += 1
        count = self.count
        self.logger.info(
            f"Compiling [{count: >{len(str(self.total))}}/{self.total}] "
            f"'{tree.from_source}'…"
        )

        yield

        if tree.report.success:
            self.logger.info(
                f"Compiling [{count: >{len(str(self.total))}}/{self.total}] "
                f"'{tree.from_source}': success."
            )
        else:
            self.logger.info(
                f"Compiling [{count: >{len(str(self.total))}}/{self.total}] "
                f"'{tree.from_source}': failed."
            )
