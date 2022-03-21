# -*- coding: utf-8 -*-

# External imports
from typing import List
from typing import Optional

from fastapi import Request


class UserCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.email: Optional[str] = None
        self.shell_login: Optional[str] = None
        self.password: Optional[str] = None
        self.active: bool = False

    async def load_data(self):
        form = await self.request.form()
        self.email = form.get("username")
        self.shell_login = form.get("shell_login")
        self.password = form.get("password")

    async def is_valid(self):
        if not self.email or not (self.email.__contains__("@")):
            self.errors.append("Email is required")
            # FIXME: abstract out hard-coded values
        # if (
        #     not self.shell_login
        #     or len(self.shell_login) not in range(4, 8 + 1)
        # ):
        #     self.errors.append(
        #         "Shell login id should be 4 - 8 characters"
        #     )
        if not self.password or not len(self.password) >= 8:
            self.errors.append("Password must be >= 8 chars")
        self.active = len(self.errors) == 0
        return self.active


# vim: set ts=4 sw=4 tw=0 et :
