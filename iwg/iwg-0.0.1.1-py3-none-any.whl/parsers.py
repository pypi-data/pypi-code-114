"""
Parsers module includes various parsing functions.
"""

import markdown
from pathlib import Path
from typing import Union


def markdown_s(input: str) -> str:
    """
    Convert markdown to HTML
    """
    return markdown.markdown(input)


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

