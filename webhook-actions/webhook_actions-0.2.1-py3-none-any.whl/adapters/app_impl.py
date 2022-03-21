from ..app.app import App
from ..app.run.run import Run, RunOutput
from ..core.entities.action import Action
from .repo_impl import RepoImpl


class AppImpl(App):
    def __init__(self) -> None:
        repo_impl = RepoImpl()
        self._run = Run(repo_impl)

    def run(self, action: Action) -> RunOutput:
        return self._run.execute(action)
