"""
Parsers module includes various parsing functions.
"""

from pathlib import Path
import markdown
import pytoml as toml
import yaml


from typing import Union, Tuple

# vikilink buildurl https://python-markdown.github.io/extensions/wikilinks/#examples

def markdown_to_html(input: str, markdown_ext: list=None) -> str:
    """
    Convert markdown to HTML
    """

    # NOTE(bora): Docs: https://python-markdown.github.io/sitemap.html
    markdown_ext = (markdown_ext
        if markdown_ext is not None
        else ["fenced_code", "footnotes", "tables"])
    
    return markdown.markdown(input, extensions=markdown_ext)


def _markdown_file_to_html(
    infile: Union[str, Path],
    outfile: Union[str, Path]
) -> None:
    """
    Convert markdown file to HTML
    """
    with open(infile, encoding="utf-8") as fp_in:
        with open(outfile, "w", encoding="utf-8") as fp_out:
            fp_out.write(markdown_to_html(fp_in.read()))


def extract_front_matter(data: str) -> Tuple[Union[dict, None], str]:
    """
    Returns:
        A tuple containing the frontmatter and the rest of the
        document. If frontmatter is not detected first field
        will be `None`.
    """

    lines = data.strip().splitlines()

    if(lines[0] == "+++"):
        meta_begin = 0
        meta_end = 0
        for i, it in enumerate(lines):
            if it == "+++":
                meta_end = i
        
        metadata = toml.loads("\n".join(lines[meta_begin + 1:meta_end]))
        return metadata, "\n".join(lines[meta_end + 1:])
    elif(lines[0] == "---"):
        meta_begin = 0
        meta_end = 0
        for i, it in enumerate(lines):
            if it == "---":
                meta_end = i
        
        metadata = yaml.safe_load("\n".join(lines[meta_begin + 1:meta_end]))
        return metadata, "\n".join(lines[meta_end + 1:])
    else:
        # NOTE(bora): Either no front-matter or front-matter type
        # cannot be detected.
        return None, data