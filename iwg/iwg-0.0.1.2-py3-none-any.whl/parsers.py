"""
Parsers module includes various parsing functions.
"""

import markdown as markdownlib
from pathlib import Path
from typing import Union

# vikilink buildurl https://python-markdown.github.io/extensions/wikilinks/#examples

def markdown_s(input: str) -> str:
    """
    Convert markdown to HTML
    """
    # NOTE(bora): Docs: https://python-markdown.github.io/sitemap.html
    return markdownlib.markdown(
        input,
        extensions=["fenced_code", "footnotes"])


def markdown(
    in_file: Union[str, Path],
    out_file: Union[str, Path]
) -> None:
    """
    Convert markdown file to HTML
    """
    with open(in_file, encoding="utf-8") as fp_in:
        with open(out_file, "w", encoding="utf-8") as fp_out:
            fp_out.write(markdown_s(fp_in.read()))

