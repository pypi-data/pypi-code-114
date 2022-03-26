import textwrap

from reportlab.pdfgen.canvas import Canvas

# Constants
WRAP_FACTOR = 2.16


# Utilities

def write_text(p: Canvas, x: int, y: int, text: str, font_size: int) -> int:
    # noinspection PyProtectedMember
    line_width = p._lineWidth

    p.setFontSize(font_size)
    p.drawString(x, y - font_size, text)  # y should point to the upper pixel of the text
    return line_width


def wrap_text(p: Canvas, x: int, y: int, text: str, font_size: int, size: int) -> int:
    # noinspection PyProtectedMember
    line_width = p._lineWidth

    h = 0

    p.setFontSize(font_size)
    wrapped = textwrap.wrap(text, int(size / font_size * WRAP_FACTOR))
    for k in range(len(wrapped)):
        p.drawString(x, y - font_size - h, wrapped[k])  # y should point to the upper pixel of the text
        h += line_width * font_size

    return h


def get_wrapped_text_height(p: Canvas, text: str, font_size: int, size: int) -> int:
    # noinspection PyProtectedMember
    line_width = p._lineWidth

    h = 0

    wrapped = textwrap.wrap(text, int(size / font_size * WRAP_FACTOR))
    for k in range(len(wrapped)):
        h += line_width * font_size

    return h
