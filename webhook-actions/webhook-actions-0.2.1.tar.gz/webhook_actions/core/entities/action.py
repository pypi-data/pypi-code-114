class Action:
    def __init__(self, path: str, data: str) -> None:
        self.path = path
        self.data = data

    def __members(self):
        return (
            self.path,
            self.data,
        )

    def test(self):
        return self.__members()

    def __eq__(self, other) -> bool:
        if type(other) is type(self):
            return self.__members() == other.__members()
        return False

    def __hash__(self) -> int:
        return hash(self.__members())

    def __repr__(self) -> str:
        return str(self.__members())

    def __str__(self) -> str:
        return self.__repr__()
