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

"""Project module."""

from dataclasses import dataclass

from .base import Base


@dataclass
class Project(Base):
    """Project class."""

    id: int
    project_key: str
    name: str
    chart_enabled: bool
    subtasking_enabled: bool
    project_leader_can_edit_project_leader: bool
    use_wiki_tree_view: bool
    text_formatting_rule: str
    archived: bool
    display_order: int
    use_dev_attributes: bool

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            project_key=data["projectKey"],
            name=data["name"],
            chart_enabled=data["chartEnabled"],
            subtasking_enabled=data["subtaskingEnabled"],
            project_leader_can_edit_project_leader=data[
                "projectLeaderCanEditProjectLeader"],
            use_wiki_tree_view=data["useWikiTreeView"],
            text_formatting_rule=data["textFormattingRule"],
            archived=data["archived"],
            display_order=data["displayOrder"],
            use_dev_attributes=data["useDevAttributes"],
        )
