from pathlib import Path
from subprocess import run

from ..app.run.run_repo import RunRepo
from ..config import config
from ..core.entities.action import Action


class ScriptGateway(RunRepo):
    def exists(self, action: Action) -> bool:
        return ScriptGateway.get_script_path(action).exists()

    def run(self, action: Action) -> bool:
        script_path = ScriptGateway.get_script_path(action)
        completedprocess = run([script_path, action.data])
        return completedprocess.returncode == 0

    @staticmethod
    def get_script_path(action: Action) -> Path:
        relative = action.path.split("/")
        return config.webhook_dir.joinpath(*relative)
