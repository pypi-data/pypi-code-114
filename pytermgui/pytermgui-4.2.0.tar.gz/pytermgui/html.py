from __future__ import annotations

from .widgets import Widget
from .parser import TokenType, StyledText, tim

BASE_HTML = """\
<html>
    <body>
        {content}
    <body
<html>
"""

STYLE_TO_TAG = {
    "bold": "<b>",
    "italic": "<i>",
}


def to_html(obj: Widget | StyledText | str) -> str:

    buff = ""
    if isinstance(obj, Widget):
        for line in obj.get_lines():
            buff += to_html(line) + "<br>\n"

        return buff

    for token in tim.tokenize_ansi(obj):
        print(token)
        if token.ttype is TokenType.PLAIN:
            buff += token.data
            continue

        if token.ttype is TokenType.STYLE:
            buff += STYLE_TO_TAG.get(token.name, "")
            continue

    return buff


if __name__ == "__main__":
    from pytermgui import Container

    Container.styles.border = "60"

    print(
        BASE_HTML.format(
            content=to_html(Container("[141 bold]Welcome to HTML!", box="DOUBLE"))
        )
    )
