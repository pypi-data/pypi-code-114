from ...core.entities.action import Action


class RunRepo:
    def run(self, action: Action) -> bool:
        raise NotImplementedError()

    def exists(self, action: Action) -> bool:
        raise NotImplementedError()
