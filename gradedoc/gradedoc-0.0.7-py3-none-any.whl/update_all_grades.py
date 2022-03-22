"""Update all grades."""

from __future__ import annotations

import docxrev

from gradedoc import shared
from gradedoc.update_grade import update_grade


def update_all_grades():
    """Update all grades."""

    (paths, gradebook_path) = shared.get_paths()

    for path in paths:
        document = docxrev.Document(path)
        update_grade(document, gradebook_path)
