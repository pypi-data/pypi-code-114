"""Toggle the review pane of the active document."""

from __future__ import annotations

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error
from win32com.client import constants

from gradedoc import shared


def toggle_active_review_pane():
    """Toggle the review pane of the active document."""
    active_document = docxrev.get_active_document(save_on_exit=False)
    toggle_review_pane(active_document)


def toggle_review_pane(document: docxrev.Document):
    """Toggle the review pane of the document."""

    (paths, _) = shared.get_paths()

    with document:
        # Check if the document is in paths
        in_paths = document.path in paths  # we consume `paths` here
        # Now update the grade or raise an exception
        if in_paths:
            document.com.ActiveWindow.View.SplitSpecial = constants.wdPaneRevisions
        else:
            raise IOError("Active document not in paths.")
