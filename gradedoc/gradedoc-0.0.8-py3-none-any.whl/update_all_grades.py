"""Update all grades."""

from __future__ import annotations

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error

from gradedoc import shared
from gradedoc.update_grade import update_grade


def update_all_grades():
    """Update all grades."""

    (paths, gradebook_path) = shared.get_paths()

    for path in paths:
        document = docxrev.Document(path)
        update_grade(document, gradebook_path)
