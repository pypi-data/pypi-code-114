from typing import Dict, List
from pyvisflow.core.props import StrTypePropInfo, SubscriptableTypePropInfo
from pyvisflow.core.props.nameProp import NamePropInfo
from pyvisflow.models.TComponent import TComponentType
from .components import Component


class Plotly(Component):
    def __init__(self) -> None:
        super().__init__('plotly', TComponentType.builtIn)
        self._data: List[Dict] = []
        self._layout = {}

    @property
    def clickInfo(self):
        p = self.get_prop('clickInfo')
        return SubscriptableTypePropInfo[str, StrTypePropInfo](p)

    def add_data(self, data: Dict):
        self._data.append(data)
        return self

    def update_data(self, idx: int, data: Dict):
        self._data[idx].update(data)
        return self

    def update_layout(self, layout: Dict):
        self._layout.update(layout)
        return self

    def _ex_get_react_data(self):
        data = super()._ex_get_react_data()
        data.update({
            'data': self._data,
            'layout': self._layout,
            'config': {},
            'clickInfo': {},
        })

        return data