"""Add template comments to all documents."""

from __future__ import annotations

import docxrev
from win32com.client import constants

from gradedoc import shared


def add_template_comments():
    """Add template comments to all documents."""

    (paths, _) = shared.get_paths()

    for path in paths:
        with docxrev.Document(path) as document:

            # Don't modify documents that already have comments
            if document.comments:
                continue

            # Convenient access to COM objects
            com_selection = document.com.Windows(1).Selection
            com_find = com_selection.Find

            document.com.Application.CommandBars.ExecuteMso("TableOfContentsRemove")

            # Go to the top of the document and add the summary comment
            com_selection.HomeKey(constants.wdStory)
            com_selection.Comments.Add(
                Range=com_selection.Range, Text=shared.SUMMARY_COMMENT
            )

            # Find headers and add header comments pointing to them
            for header, header_comment in zip(shared.HEADERS, shared.HEADER_COMMENTS):

                # Find the header
                com_find.Execute(
                    FindText=header,  # Find the header
                    # Ensure certain `Find` options are set
                    Forward=True,
                    MatchCase=False,
                    MatchWholeWord=False,
                    MatchWildcards=False,
                    MatchSoundsLike=False,
                    MatchAllWordForms=False,
                    Wrap=False,
                    Format=False,
                    Replace=constants.wdReplaceNone,
                )

                # Add the header comment pointing to the `Range` just found
                com_selection.Comments.Add(
                    Range=com_selection.Range,
                    Text=header_comment,
                )
                com_selection.EndKey()

            # Go back to the top of the document when done
            com_selection.HomeKey(constants.wdStory)
