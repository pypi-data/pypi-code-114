"""Parser for Scraper output to Models."""

import asyncpraw, re
from . import s_models as models

__all__ = ["Parser", "Exceptions"]
PostModel = models.PostModel


class Exceptions:
    """Exceptions for the Parser."""

    class CommentException(Exception):
        """Parent Class for all comment Exceptions."""

        ...

    class PostException(Exception):
        """Parent class for all post Exceptions"""

        ...

    class NotParentComment(CommentException):
        """Raised when a comment isn't a parent/top level comment."""

        ...

    class AutomodComment(CommentException):
        """Raised when a comment is authored by automod."""

        ...

    class DeletedBody(CommentException):
        """Raised when a comment has a deleted body."""

        ...

    class BodyTooShort(CommentException):
        """Raised when a comment has a body that is too short."""

        ...

    class NoReplies(PostException):
        """Raised when a post has no decent replies (When parsing all comments raises one of the above comment errors)."""

        ...

    class Duplicate(PostException):
        """Raised when a post is already in the database."""

        ...


Exceptions = Exceptions()


class Parser:
    """Parser for Scraper output to Models."""

    @staticmethod
    def comment(comment: asyncpraw.reddit.models.Comment, postId: str, char_limit: int):
        """Comment Parser."""
        author = comment.author.name if comment.author is not None else "[deleted]"
        body = comment.body.strip()

        if len(body) < char_limit:
            raise Exceptions.BodyTooShort("Comment is too short.")

        if comment.parent_id.startswith("t1"):
            raise Exceptions.NotParentComment("Comment is not a parent comment.")

        if author == "AutoModerator":
            raise Exceptions.AutomodComment("Comment is an automod comment.")

        if body in ["[removed]", "[deleted]"]:
            raise Exceptions.DeletedBody("Comment has a deleted body.")

        data = {
            "rId": comment.id,
            "replies": len(comment.replies),
            "author": author,
            "body": body,
            "postId": postId,
        }

        return data

    def post(
        self, post: asyncpraw.reddit.models.Submission, subreddit, char_limit: int
    ):
        """Given post, first iterates through comments and tries to parse. If there are no worthy comments, the post raises a no replies error. After comment parsing, post data is compiled into a dictionary and a Model is created out of it."""
        raw_comments = post.comments

        if len(raw_comments) == 0:
            raise Exceptions.NoReplies("Post has no worthy replies.")
        
        parsed_comments = []
        for comment in raw_comments:
            try:
                #
                if len(parsed_comments) == 1:
                    break  # INFO: This prevents the parser from parsing more than one comment, remove this if you want to parse all comments. There might be a cleaner way to do this.
                #
                parsed_comments.append(
                    self.comment(comment=comment, postId=post.id, char_limit=char_limit)
                )
            except Exceptions.CommentException:
                continue

        if len(parsed_comments) == 0:
            raise Exceptions.NoReplies("Post has no worthy replies.")

        flair = ""
        if post.link_flair_text is not None and post.link_flair_text != "":
            flair = post.link_flair_text
        data = {
            "rId": post.id,
            "title": re.sub(r"\[.*\]", "", post.title).strip(),
            "flair": flair,
            "replies": post.num_comments,
            "image": post.url if post.url.startswith("https://i.redd.it") else None,
            "votes": post.ups,
        }

        Post: PostModel = PostModel()
        Post.post = data
        #
        Post.comments = [
            parsed_comments[
                0
            ]  # INFO: If you want the scraper to store all comments, remove this line, along with the other INFO one above this.
        ]
        #
        Post.subreddit = {
            "name": subreddit.display_name,
            "description": subreddit.description,
        }

        return Post
