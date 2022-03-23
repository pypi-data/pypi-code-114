from enum import Enum

from paka.cmark import lowlevel


class Option(int, Enum):

    OPT_DEFAULT = lowlevel.OPT_DEFAULT  # type: int
    """Default options."""

    OPT_HARDBREAKS = lowlevel.OPT_HARDBREAKS  # type: int
    """Render “soft break” nodes as hard line breaks."""

    OPT_NOBREAKS = lowlevel.OPT_NOBREAKS  # type: int
    """Render “soft break” nodes as spaces."""

    OPT_SOURCEPOS = lowlevel.OPT_SOURCEPOS  # type: int
    """Render with “sourcepos” information."""

    OPT_UNSAFE = lowlevel.OPT_UNSAFE  # type: int
    """Allow raw HTML and unsafe links while rendering."""

    OPT_SMART = lowlevel.OPT_SMART  # type: int
    """Render straight quotes as curly, ``---`` as em dash, ``--`` as en dash."""


class EventType(int, Enum):

    EVENT_ENTER = lowlevel.EVENT_ENTER  # type: int
    """Entering node."""

    EVENT_EXIT = lowlevel.EVENT_EXIT  # type: int
    """Exiting node."""

    EVENT_DONE = lowlevel.EVENT_DONE  # type: int
    """Done iteration."""


class NodeType(int, Enum):

    NODE_NONE = lowlevel.NODE_NONE  # type: int
    """Error status."""

    NODE_CODE_BLOCK = lowlevel.NODE_CODE_BLOCK  # type: int
    """Block of code."""

    NODE_HTML_BLOCK = lowlevel.NODE_HTML_BLOCK  # type: int
    """Raw HTML block."""

    NODE_DOCUMENT = lowlevel.NODE_DOCUMENT  # type: int
    """Document."""

    NODE_BLOCK_QUOTE = lowlevel.NODE_BLOCK_QUOTE  # type: int
    """Block quote."""

    NODE_LIST = lowlevel.NODE_LIST  # type: int
    """List."""

    NODE_ITEM = lowlevel.NODE_ITEM  # type: int
    """List item."""

    NODE_CUSTOM_BLOCK = lowlevel.NODE_CUSTOM_BLOCK  # type: int
    """Block of custom."""

    NODE_PARAGRAPH = lowlevel.NODE_PARAGRAPH  # type: int
    """Paragraph."""

    NODE_HEADING = lowlevel.NODE_HEADING  # type: int
    """Heading."""

    NODE_THEMATIC_BREAK = lowlevel.NODE_THEMATIC_BREAK  # type: int
    """Thematic break."""

    NODE_FIRST_BLOCK = lowlevel.NODE_FIRST_BLOCK  # type: int
    """First block."""

    NODE_LAST_BLOCK = lowlevel.NODE_LAST_BLOCK  # type: int
    """Last block."""

    NODE_TEXT = lowlevel.NODE_TEXT  # type: int
    """Text."""

    NODE_SOFTBREAK = lowlevel.NODE_SOFTBREAK  # type: int
    """Soft break."""

    NODE_LINEBREAK = lowlevel.NODE_LINEBREAK  # type: int
    """Line break."""

    NODE_CODE = lowlevel.NODE_CODE  # type: int
    """Inline code."""

    NODE_HTML_INLINE = lowlevel.NODE_HTML_INLINE  # type: int
    """Inline HTML."""

    NODE_CUSTOM_INLINE = lowlevel.NODE_CUSTOM_INLINE  # type: int
    """Inline custom."""

    NODE_EMPH = lowlevel.NODE_EMPH  # type: int
    """Emphasis."""

    NODE_STRONG = lowlevel.NODE_STRONG  # type: int
    """Strong emphasis."""

    NODE_LINK = lowlevel.NODE_LINK  # type: int
    """Link."""

    NODE_IMAGE = lowlevel.NODE_IMAGE  # type: int
    """Image."""

    NODE_FIRST_INLINE = lowlevel.NODE_FIRST_INLINE  # type: int
    """First inline."""

    NODE_LAST_INLINE = lowlevel.NODE_LAST_INLINE  # type: int
    """Last inline."""


class ListType(int, Enum):

    BULLET_LIST = lowlevel.BULLET_LIST  # type: int
    """Bullet list."""

    ORDERED_LIST = lowlevel.ORDERED_LIST  # type: int
    """Ordered list."""

    NO_LIST = lowlevel.NO_LIST  # type: int
    """Node is not a list."""


class UnknowType(int, Enum):

    PAREN_DELIM = lowlevel.PAREN_DELIM  # type: int
    """``)``"""

    PERIOD_DELIM = lowlevel.PERIOD_DELIM  # type: int
    """``.``"""

    NO_DELIM = lowlevel.NO_DELIM  # type: int
    """No list delimiter."""
