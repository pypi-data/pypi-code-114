from pyvisflow.models.TComponent import TComponentType
from .components import Component


class Text(Component):
    def __init__(self, value:str) -> None:
        super().__init__('text', TComponentType.builtIn)
        self.set_prop('value',value)