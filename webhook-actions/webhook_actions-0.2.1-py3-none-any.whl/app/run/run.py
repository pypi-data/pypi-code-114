from enum import Enum
from threading import Thread

from tealprint import TealPrint

from ...core.entities.action import Action
from .run_repo import RunRepo


class RunOutput(Enum):
    success = 1
    fail = 2
    not_found = 3


class Run:
    def __init__(self, repo: RunRepo) -> None:
        self.repo = repo

    def execute(self, action: Action) -> RunOutput:
        if not self.repo.exists(action):
            return RunOutput.not_found

        # Run in background
        Thread(target=self.run_in_background, args=[action]).start()

        return RunOutput.success

    def run_in_background(self, action: Action) -> None:
        success = self.repo.run(action)
        if not success:
            TealPrint.warning(f"Action faild: {action}")
