"""Update the grade of the active document."""

from __future__ import annotations

import docxrev

from gradedoc import shared
from gradedoc.update_grade import update_grade


def update_active_grade():
    """Update the active document grade, insert common comments, update gradebook."""

    (paths, gradebook_path) = shared.get_paths()

    active_document = docxrev.get_active_document(save_on_exit=False)
    with active_document:
        # Check if the document is in paths
        in_paths = active_document.path in paths  # we consume `paths` here
        # Now update the grade or raise an exception
        if in_paths:
            active_document.save_on_exit = True  # only save if we're updating the grade
            update_grade(active_document, gradebook_path)
        else:
            raise Exception("Active document not in paths.")
