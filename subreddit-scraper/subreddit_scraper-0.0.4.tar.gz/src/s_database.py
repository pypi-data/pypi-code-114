"""Database module"""
from prisma import Prisma, errors
from prisma.models import Post, Subreddit, Comment
from .s_parsers import PostModel
from rich.console import Console

__all__ = ["Database"]
console = Console()


class Database:
    """The database class, allows easy interfacing with the Prisma database."""

    def __init__(self):
        """Initializes the class."""
        self.conn = None

    async def connect(self):
        """Connects to the database."""
        if self.conn is None:
            self.conn = Prisma(auto_register=True)
            await self.conn.connect()
        return self.conn

    async def disconnect(self):
        """Disconnects from the database."""
        if self.conn.is_connected:
            await self.conn.disconnect()
            return True
        return False

    @staticmethod
    async def add(post: PostModel):
        """Adds a post to the database."""
        subredditD, postD, commentsL = post.subreddit, post.post, post.comments
        try:
            await Subreddit.prisma().create(data=subredditD)
        except errors.UniqueViolationError:
            pass
        postD["subredditName"] = subredditD["name"]
        await Post.prisma().create(data=postD)
        for comment in commentsL:
            comment["postId"] = postD["rId"]
            await Comment.prisma().create(data=comment)

    @staticmethod
    async def check_post(id: str):
        """Checks if a post is in the database."""
        data = await Post.prisma().find_first(where={"rId": {"contains": id}})
        if data is None:
            return False
        return True

    @staticmethod
    async def check_subreddit(name: str):
        """Checks if a subreddit is in the database."""
        data = await Subreddit.prisma().find_first(where={"name": {"contains": name}})
        if data is None:
            return False
        return True

    @staticmethod
    async def count(subreddit: str = None):
        """Counts the number of posts in the database, for a subreddit."""
        if subreddit is None:
            return await Post.prisma().count()
        return await Post.prisma().count(where=Post.subreddit.name.eq(subreddit))

    @staticmethod
    async def get(subreddit: str, page: int, perPage: int = 10):
        """Gets posts from the database, in a subreddit."""
        return await Post.findMany(
            where=Post.subreddit.name.eq(subreddit), skip=page * perPage, take=perPage
        )

    async def pages(self, subreddit: str, perPage: int = 10):
        """Gets the number of pages for all the posts in a subreddit."""
        return (await self.count(subreddit)) // perPage

    @staticmethod
    async def subreddits():
        """Gets all subreddits in the database."""
        return await Subreddit.prisma().findMany()
