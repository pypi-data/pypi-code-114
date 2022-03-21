from ..app.run.run import RunOutput
from ..core.entities.action import Action


class App:
    def run(self, action: Action) -> RunOutput:
        raise NotImplementedError()
