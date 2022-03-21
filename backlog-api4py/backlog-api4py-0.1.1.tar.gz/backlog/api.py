# Copyright 2022 Ryo H
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Backlog API module."""

from typing import List, Union

import requests

from .models import Project, Space, User


class BacklogApi(object):
    """Backlog API class."""

    SPACE_TYPES = {
        "jp": "backlog.jp",
        "com": "backlog.com",
        "tool": "backlogtool.com"
    }

    def __init__(self, space_key: str, space_type: str, api_key: str):
        """__init__ method.

        :param space_key: space key
        :param space_type: space type
        :param api_key: api key
        :raises ValueError: when initialization fails
        """
        if not space_key:
            raise ValueError("space_key must not be empty.")
        domain = self.SPACE_TYPES.get(space_type)
        if not domain:
            raise ValueError("space_type must be one of 'jp', 'com', 'tool'.")
        if not api_key:
            raise ValueError("api_key must not be empty.")

        self.base_url = f"https://{space_key}.{domain}/api/v2/"
        self.api_key = api_key

    def get_space(self) -> Space:
        """Get information about your space.

        :return: space information
        """
        url = "space"

        space = self._send_get_request(url)
        return Space.from_dict(space)

    def get_users(self) -> List[User]:
        """Get list of users in your space.

        :return: list of users
        """
        url = "users"

        users = self._send_get_request(url)
        return [User.from_dict(user) for user in users]

    def get_user(self, user_id: int) -> User:
        """Get information about user.

        :param user_id: user id
        :return: user information
        """
        url = f"users/{user_id}"

        user = self._send_get_request(url)
        return User.from_dict(user)

    def get_own_user(self) -> User:
        """Get own information about user.

        :return: user information
        """
        url = "users/myself"

        user = self._send_get_request(url)
        return User.from_dict(user)

    def get_projects(self) -> List[Project]:
        """Get list of projects.

        :return: list of projects
        """
        url = "projects"

        projects = self._send_get_request(url)
        return [Project.from_dict(project) for project in projects]

    def get_project(self, project_id_or_key: Union[int, str]) -> Project:
        """Get information about project.

        :param project_id_or_key: project id or project key
        :return: project information
        """
        url = f"projects/{project_id_or_key}"

        project = self._send_get_request(url)
        return Project.from_dict(project)

    def get_project_users(
            self, project_id_or_key: Union[int, str]) -> List[User]:
        """Get list of project members.

        :param project_id_or_key: project id or project key
        :return: list of project members
        """
        url = f"projects/{project_id_or_key}/users"

        users = self._send_get_request(url)
        return [User.from_dict(user) for user in users]

    def get_project_administrators(
            self, project_id_or_key: Union[int, str]) -> List[User]:
        """Get list of users who has project administrator role.

        :param project_id_or_key: project id or project key
        :return: list of project administrators
        """
        url = f"projects/{project_id_or_key}/administrators"

        administrators = self._send_get_request(url)
        return [User.from_dict(administrator)
                for administrator in administrators]

    def _send_get_request(self, path: str, query_params: dict = None):
        query_params = query_params or {}
        query_params["apiKey"] = self.api_key

        response = requests.get(self.base_url + path, params=query_params)
        return response.json()
