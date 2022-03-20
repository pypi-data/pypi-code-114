from pathlib import Path
from ingesture.fields.base import BaseField


class Video(Path, BaseField):
    """
    An external video file!
    """

