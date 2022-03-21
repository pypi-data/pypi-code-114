__version__ = '0.4.3'

import markdown as md

from .citation import citation
from .video import video
from .capitalized import capitalized


def marquedown(document: str, **kwargs):
    """Convert both Marquedown and Markdown into HTML."""

    if kwargs.get('citation', True):
        document = citation(document)

    if kwargs.get('video', True):
        document = video(document)
        
    html = md.markdown(document)

    if kwargs.get('capitalized', True):
        html = capitalized(html)

    return html