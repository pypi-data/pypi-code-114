import json
import os.path
import shutil
from typing import List, Any, Dict

from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.screen import MDScreen

from assignment_tool.manager import Manager
from assignment_tool.utils import Assignment, Url


class CustomOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()
    my_callback = ObjectProperty()


class AssignmentScreen(MDScreen):
    heading = StringProperty()


class AssignmentManager(Manager):
    screen_name = "assignment"

    def __init__(self, app):
        super().__init__(app)

    def populate(
        self, courses: Dict, index: int, base_directory: str, filemanager: str
    ):
        urls = Url(lms=courses["lms_url"], compiler=courses["compiler_url"])
        current_course = courses["courses"][index]
        self.instance.heading = current_course["name"]
        course_path = os.path.join(base_directory, current_course["path"])
        workspace_filename = os.path.join(
            course_path, f".{os.path.basename(course_path)}.code-workspace"
        )

        # create_course_path
        os.makedirs(course_path, mode=0o0755, exist_ok=True)

        self.instance.ids.rv.data = []
        folders = []
        for idx, entry in enumerate(current_course["assignments"]):
            entry["course_path"] = course_path
            assignment = Assignment.from_dict(entry)
            folders.append({"path": assignment.path})
            self._add_item("abacus", assignment, urls, filemanager, workspace_filename)
            self._create_assignment_path(assignment.assignment_path, idx == 0)

        self._create_workspace_file(folders, workspace_filename)

    def _create_workspace_file(
        self, folders: List[Dict[str, Any]], workspace_filename: str
    ):
        workspace = {
            "folders": folders,
            "settings": {
                "[c]": {"editor.defaultFormatter": "xaver.clang-format"},
                "files.autoSave": "afterDelay",
                "files.exclude": {},
            },
        }
        for exclude in self.config.get("workspace.settings", "files.exclude").split():
            workspace["settings"]["files.exclude"][exclude] = True
        with open(workspace_filename, "w") as fd:
            json.dump(workspace, fd, indent=2)

    def _add_item(
        self,
        icon: str,
        assignment: Assignment,
        urls: Url,
        filemanager: str,
        workspace_filename: str,
    ):
        text = assignment.name
        self.instance.ids.rv.data.append(
            {
                "viewclass": "CustomOneLineIconListItem",
                "icon": icon,
                "text": text,
                "my_callback": lambda app: app.details.populate(
                    f"{self.instance.heading} / {text}",
                    assignment,
                    urls,
                    filemanager,
                    workspace_filename,
                ),
            }
        )

    def _create_assignment_path(
        self, assignment_path: str, make_default_task: bool = False
    ):
        os.makedirs(assignment_path, mode=0o755, exist_ok=True)

        # populate VSCode directories
        os.makedirs(os.path.join(assignment_path, ".vscode"), mode=0o755, exist_ok=True)
        vs_task_file = os.path.join(assignment_path, ".vscode", "tasks.json")
        template_name = "tasks_default.json" if make_default_task else "tasks.json"
        shutil.copy(
            os.path.join(self.app.directory, "assets", "vscode", template_name),
            vs_task_file,
        )
