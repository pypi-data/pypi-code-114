"""Scrapes a subreddit."""

import asyncpraw
from .s_parsers import Parser, Exceptions
from typing import Iterator, Union
from rich.console import Console

# --- Constants --- #

__all__ = ["Scraper"]

console = Console()
subredditTypehint = asyncpraw.reddit.models.Subreddit
searchTypeTypehint = Union[
    subredditTypehint.hot,
    subredditTypehint.new,
    subredditTypehint.rising,
    subredditTypehint.controversial,
    subredditTypehint.top,
]
parser = Parser()
Exceptions = Exceptions

# --- Functions --- #


class Scraper:
    """Class for scraping a subreddit and yielding posts."""

    @staticmethod
    async def return_search_type_from_string(
        subreddit: subredditTypehint, search_type: str
    ) -> searchTypeTypehint:
        """Return the search type from the given string."""
        if hasattr(subreddit, search_type):
            return getattr(subreddit, search_type)
        raise AttributeError(
            f"{subreddit.display_name} does not have a {search_type} search type."
        )

    @staticmethod
    async def yield_posts(
        limit: Union[int, None], search_type: searchTypeTypehint
    ) -> Iterator[asyncpraw.reddit.models.Submission]:
        """Yield posts from the given subreddit."""
        async for post in search_type(limit=limit):
            await post.load()
            yield post

    async def scrape(
        self, subreddit: subredditTypehint, search_type: str, database, char_limit: int
    ):
        """Scrape the given subreddit."""
        search_type = await self.return_search_type_from_string(
            subreddit=subreddit, search_type=search_type
        )
        async for post in self.yield_posts(
            limit=None,
            search_type=search_type,
        ):
            try:
                if await database.check_post(id=post.id):
                    yield Exceptions.Duplicate(
                        "Post in database"
                    ), post.id, post.url
                    continue
                raw_comments = post.comments.list()
                clean_comments = []

                for comment in raw_comments:
                    if isinstance(comment, asyncpraw.reddit.models.MoreComments):
                        comments = await comment.comments()

                        try:
                            comment = comments[0]
                        except IndexError:
                            continue

                        clean_comments.append(comment)
                    else:
                        clean_comments.append(comment)
                post.comments = clean_comments
                yield parser.post(
                    post, subreddit, char_limit=char_limit
                ), post.id, post.url
            except Exceptions.PostException as e:
                yield e, post.id, post.url
