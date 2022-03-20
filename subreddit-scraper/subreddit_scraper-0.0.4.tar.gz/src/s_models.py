"""Models"""
from typing import Union

__all__ = ["PostModel"]


class PostModel:
    """Model for a post."""

    post: dict[str, Union[str, int]] = None
    comments: list[dict[str, Union[str, int]]] = None
    subreddit: dict[str, str] = None
