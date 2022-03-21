# -*- coding: utf-8 -*-

"""
Form class for creating a challenge via web UI.
"""

# External imports
from typing import List
from typing import Optional

from fastapi import Request


MIN_TITLE_LENGTH = 4
MIN_DESCRIPTION_LENGTH = 20


class ChallengeCreateForm:
    def __init__(self, request: Request, challenges: List = []):
        self.request: Request = request
        self.challenges: List = challenges
        self.errors: List = []
        self.title: Optional[str] = None
        self.author: Optional[str] = None
        self.url: Optional[str] = None
        self.description: Optional[str] = None
        self.date_posted: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.author = form.get("author")
        self.url = form.get("url")
        self.description = form.get("description")
        self.date_posted = form.get("date_posted")

    def is_valid(self):
        if not self.title or len(self.title) < MIN_TITLE_LENGTH:
            self.errors.append(
                f"A valid title of at least {MIN_TITLE_LENGTH} "
                "characters is required"
            )
        if self.title.lower() in [
            challenge.title.lower()
            for challenge in self.challenges
        ]:
            self.errors.append("A challenge with that title already exists")
        if not self.url or not (self.url.__contains__("http")):
            self.errors.append("Valid Url is required e.g. https://example.com")
        if not self.author or not len(self.author) >= 1:
            self.errors.append("A valid author is required")
        if (
            not self.description
            or len(self.description) < MIN_DESCRIPTION_LENGTH
        ):
            self.errors.append(
                f"A valid description of at least {MIN_DESCRIPTION_LENGTH} "
                "characters is required"
            )
        if not self.errors:
            return True
        return False


# vim: set ts=4 sw=4 tw=0 et :
