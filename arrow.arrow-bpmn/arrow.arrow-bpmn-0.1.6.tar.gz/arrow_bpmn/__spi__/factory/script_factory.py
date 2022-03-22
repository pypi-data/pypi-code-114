from abc import ABC, abstractmethod

from scriptable.abstract_engine import ScriptableEngine


class ScriptFactory(ABC):

    @abstractmethod
    def __call__(self, language: str, script: str) -> ScriptableEngine:
        pass
