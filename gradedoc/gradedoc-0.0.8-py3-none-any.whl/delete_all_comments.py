"""Delete all comments from all documents."""

from __future__ import annotations

try:
    import docxrev
except TypeError as error:
    raise TypeError(
        "Cannot access the document. Save the document, close it,\n"
        "then re-open it and try again."
    ) from error

from gradedoc import shared


def delete_all_comments():
    """Delete all comments from all documents."""

    response = input(  # nosec
        "Are you sure you want to delete all comments? [y/N] >>> "
    )
    if response.lower() == "y":
        (paths, _) = shared.get_paths()
        for path in paths:
            docxrev.Document(path).delete_comments()
    else:
        print("Not deleting comments.")
