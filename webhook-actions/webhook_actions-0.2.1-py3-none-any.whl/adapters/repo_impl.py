from ..app.run.run_repo import RunRepo
from ..core.entities.action import Action
from ..gateways.script_gateway import ScriptGateway


class RepoImpl(RunRepo):
    def __init__(self) -> None:
        super().__init__()
        self.script_gateway = ScriptGateway()

    def run(self, action: Action) -> bool:
        return self.script_gateway.run(action)

    def exists(self, action: Action) -> bool:
        return self.script_gateway.exists(action)
