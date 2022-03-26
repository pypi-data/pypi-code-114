import pytoml as toml
from typing import Tuple, Union

class Document:
    def __init__(self, metadata=None, content=None):
        self.meta: dict = {} if metadata is None else metadata
        self.content: str = content


def extractFrontMatter(data: str) -> Tuple[Union[dict, None], str]:
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
        return metadata, "\n".join(lines[meta_end:])
    elif(lines[0] == "---"):
        meta_begin = 0
        meta_end = 0
        for i, it in enumerate(lines):
            if it == "---":
                meta_end = i
        
        metadata = toml.loads("\n".join(lines[meta_begin + 1:meta_end]))
        return metadata, "\n".join(lines[meta_end:])
    else:
        # NOTE(bora): Either no front-matter or front-matter type
        # cannot be detected.
        return (None, data)


def fromMarkdown(data: str) -> Document:
    frontmatter, markdown = extractFrontMatter(data)

    # TODO(bora): Parse markdown
    return Document(frontmatter, markdown)
