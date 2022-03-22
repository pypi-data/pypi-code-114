from abc import abstractmethod
from typing import Any, Dict, List, Tuple, Union
from pyvisflow.models.TComponent import TComponent, TComponentType
import re

from pyvisflow.models.TWatchInfo import TChartFilterWatch
from pyvisflow.core.reactive import Reactive

RE_match_array = re.compile(r'(?P<name>.+)(\[(?P<num>\d+)\])')


class Component(Reactive):
    def __init__(self, tag: str, type: TComponentType) -> None:
        super().__init__()
        self._tag = tag
        self._type = type
        self._attrs = {}
        self._styles = {}
        self._children: List[Component] = []

    def update_attrs(self, **kws):
        self._attrs.update(kws)
        return self

    def update_styles(self, **kws):

        for key, value in kws.items():
            self.set_prop(f'styles.{key}', value)

        # self._styles.update(kws)
        return self

    def _ex_get_react_data(self) -> Dict[str, Any]:
        if self._type == TComponentType.builtIn:
            data = {
                'attrs': self._attrs,
                'styles': self._styles,
            }

            return data

        return {}

    def to_model(self) -> TComponent:
        children = [c.to_model() for c in self._children]
        return TComponent(id=self._id,
                          type=self._type,
                          tag=self._tag,
                          attrs=self._attrs,
                          styles=self._styles,
                          children=children)
