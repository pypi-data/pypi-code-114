from pathlib import Path

from pydantic import BaseModel


class Schema(BaseModel):
    """
    Base schema model beneath which fields can be declared.

    The schema is intended as an *abstract* representation of a data
    structure, rather than a container for the data itself.

    .. todo::

        Main thing we'll need here is something with a validator in the Config
        that lets us have external links even if they will have a different type (eg.
        specifying a video

    """

    @classmethod
    def make(cls, path: Path) -> 'Schema':
        """
        Make an instance of this schema by parsing all the spec objects
        relative to the provided path
        """



