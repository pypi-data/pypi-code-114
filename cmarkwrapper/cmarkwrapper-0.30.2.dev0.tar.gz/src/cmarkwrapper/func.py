from paka import cmark


def markdown_to_html(
    markdown: str,
    breaks: bool = False,
    safe: bool = True,
    sourcepos: bool = False,
    smart: bool = False,
) -> str:
    """Convert markup to HTML."""
    return cmark.to_html(markdown, breaks, safe, sourcepos, smart)


def markdown_to_xml(markdown: str, sourcepos: bool = False, smart: bool = False) -> str:
    """Convert markup to XML."""
    return cmark.to_xml(markdown, sourcepos, smart)


def markdown_to_commonmark(
    markdown: str, breaks: bool = False, width: int = 0, smart: bool = False
) -> str:
    """Convert markup to CommonMark."""
    return cmark.to_commonmark(markdown, breaks, width, smart)


def markdown_to_man(
    markdown: str, breaks: bool = False, width: int = 0, smart: bool = False
) -> str:
    """Convert markup to groff man page."""
    return cmark.to_man(markdown, breaks, width, smart)


def markdown_to_latex(
    markdown: str, breaks: bool = False, width: int = 0, smart: bool = False
) -> str:
    """Convert markup to LaTeX."""
    return cmark.to_latex(markdown, breaks, width, smart)
