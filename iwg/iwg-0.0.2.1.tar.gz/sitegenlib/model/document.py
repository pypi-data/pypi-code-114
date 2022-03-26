import dataclasses

from ..parsing import extract_front_matter, markdown_to_html


@dataclasses.dataclass
class Document:
    meta: dict = dataclasses.field(default_factory=dict)
    content: str = None


def from_markdown(data: str, markdown_ext: dict=None) -> Document:
    markdown_ext = (markdown_ext
        if markdown_ext is not None
        else ["fenced_code", "footnotes", "tables"])
    
    frontmatter, markdown = extract_front_matter(data)
    html = markdown_to_html(markdown, markdown_ext)
    
    return Document(frontmatter, html)
