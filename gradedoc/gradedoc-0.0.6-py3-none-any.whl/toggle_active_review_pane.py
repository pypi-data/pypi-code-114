"""Toggle the review pane of the active document."""

from __future__ import annotations

import docxrev
from win32com.client import constants

from gradedoc import shared


def toggle_active_review_pane():
    """Toggle the review pane of the active document."""

    (paths, _) = shared.get_paths()

    active_document = docxrev.get_active_document(save_on_exit=False)
    with active_document:
        # Check if the document is in paths
        in_paths = active_document.path in paths  # we consume `paths` here
        # Now update the grade or raise an exception
        if in_paths:
            active_document.com.ActiveWindow.View.SplitSpecial = (
                constants.wdPaneRevisions
            )
        else:
            raise Exception("Active document not in paths.")
