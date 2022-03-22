"""Save all documents."""

from __future__ import annotations

import docxrev

from gradedoc import shared


def save_all():
    """Save all documents without closing them."""

    (paths, _) = shared.get_paths()
    for path in paths:
        document = docxrev.Document(path, save_on_exit=True, close_on_exit=False)
        with document:
            pass
