# -*- coding: utf-8 -*-

# Standard imports
from typing import (
    List,
    Optional,
)

# External imports
from fastapi import Request


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.email: Optional[str] = None
        # self.shell_login: Optional[str] = None
        self.password: Optional[str] = None
        self.active: bool = False

    async def load_data(self):
        form = await self.request.form()
        # Since OAuth works on username field we
        # are considering username as email address.
        self.username = form.get("username")
        # But otherwise, schemas (and thus templates)
        # use "email" instead of "username".
        if self.email is None:
            self.email = self.username
        # self.shell_login = form.get("shell_login")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Username must be your email address")
        # if (
        #     not self.shell_login
        #     or len(self.shell_login) not in range(4, (8 + 1)
        # ):
        #     self.errors.append("A valid shell login name is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        self.active = len(self.errors) == 0
        return self.active


# vim: set ts=4 sw=4 tw=0 et :
