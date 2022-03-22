"""Save and close all documents."""

from __future__ import annotations

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error

from gradedoc import shared


def close_all():
    """Save and close all documents."""

    (paths, _) = shared.get_paths()
    for path in paths:
        document = docxrev.Document(path, save_on_exit=True, close_on_exit=True)
        with document:
            pass
