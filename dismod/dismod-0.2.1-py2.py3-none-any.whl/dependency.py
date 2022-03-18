import os
from typing import Any
from typing import List


class DependencyContainer:
    def __init__(self, filepath: str) -> None:
        """ """
        self.filepath = filepath
        self.basename: str = self._parse_basename()
        self.imports: List[Any] = []

    def _parse_basename(self) -> str:
        """ """
        return os.path.basename(self.filepath)

    def add_import(
        self,
        imports: List[Any],
    ) -> None:
        """ """
        self.imports = imports
