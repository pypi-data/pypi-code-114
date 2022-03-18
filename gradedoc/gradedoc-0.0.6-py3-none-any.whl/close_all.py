"""Save and close all documents."""

from __future__ import annotations

import docxrev

from gradedoc import shared


def close_all():
    """Save and close all documents."""

    (paths, _) = shared.get_paths()
    for path in paths:
        document = docxrev.Document(path, save_on_exit=True, close_on_exit=True)
        with document:
            pass
