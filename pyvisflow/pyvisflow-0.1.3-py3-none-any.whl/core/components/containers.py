from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, TYPE_CHECKING, Union

import pandas as pd
from pyvisflow.core.components.components import Component
from pyvisflow.core.components.dataTable import DataTable
from pyvisflow.core.components.echart import EChart
from pyvisflow.core.components.input import Input
from pyvisflow.core.components.inputNumber import InputNumber
from pyvisflow.core.components.plotly import Plotly
from pyvisflow.core.components.select import Select
from pyvisflow.core.components.text import Text
from pyvisflow.core.layout import MarkdownLayout
from pyvisflow.core.props import BoolTypePropInfo, NamePropInfo

from pyvisflow.models.TComponent import TComponentType

if TYPE_CHECKING:
    from pyvisflow.core.props import TypePropInfo


class Container(Component):
    # appender_stack: List[Callable[[Component]
    def __init__(self, tag: str, type=TComponentType.builtIn) -> None:
        super().__init__(tag, type)
        # self._appender_stack = appender_stack

    def add_child(self, cp: Component):
        self._children.append(cp)
        return cp


class BoxContainer(Container):
    def __init__(self, sepc=0) -> None:
        super().__init__('box')
        self._spec = sepc
        self._on_before_data_fn = lambda data: data

    def box(self, ):
        cp = BoxContainer()
        cp._on_before_data_fn = self._on_before_data_fn
        self.add_child(cp)
        return cp

    def text(self,value:str):
        cp = Text(value)
        self.add_child(cp)
        return cp

    def dataTable(self, dataframe: pd.DataFrame, page_size=5):
        cp = DataTable(self._on_before_data_fn(dataframe))
        cp.page_size = page_size
        self.add_child(cp)
        return cp

    def tabs(self, names: Union[Iterable[str], Dict[str, str]]):
        cp = tabs.Tabs(names)
        self.add_child(cp)

        for box in cp.boxes:
            box._on_before_data_fn = self._on_before_data_fn

        return cp

    def plotly(self):
        cp = Plotly()
        self.add_child(cp)
        return cp

    def cols(self, spec: Union[int, List[int]]):
        cp = ColumnsContainer(spec)
        self.add_child(cp)

        for box in cp.boxes:
            box._on_before_data_fn = self._on_before_data_fn

        return cp.boxes

    def input(self, value=''):
        cp = Input(value)
        self.add_child(cp)
        return cp

    def inputNumber(self, value=0):
        cp = InputNumber(value)
        self.add_child(cp)
        return cp

    def select(self, options: Iterable[str]):
        cp = Select(options)
        self.add_child(cp)
        return cp

    def echart(self, data: pd.DataFrame):
        cp = EChart(self._on_before_data_fn(data))
        self.add_child(cp)
        return cp

    def markdown(self, md: str, **prop_mapping: TypePropInfo):
        layout = MarkdownLayout(md, prop_mapping)
        for cp in layout.parse_markdown():
            self.add_child(cp)
        return layout

    @property
    def isHover(self):
        p = self.get_prop('isHover')
        return BoolTypePropInfo(p)

    def _ex_get_react_data(self) -> Dict[str, Any]:
        data = super()._ex_get_react_data()
        data.update({'spec': self._spec, 'isHover': False})
        return data


class ColumnsContainer(Container):
    def __init__(
            self,
            #  appender_stack: List[Callable[[Component], Component]],
            spec: Union[int, List[int]]) -> None:
        super().__init__('columns-container')

        self._is_grid = not isinstance(spec, int)

        __spec = spec
        if isinstance(spec, int):
            __spec = [spec for _ in range(spec)]
        self._spec = __spec
        self._boxes = tuple([BoxContainer(s) for s in __spec])
        for box in self._boxes:
            self.add_child(box)

    @property
    def boxes(self):
        return self._boxes

    def _ex_get_react_data(self) -> Dict[str, Any]:
        data = super()._ex_get_react_data()
        data.update({'spec': self._spec, 'isGrid': self._is_grid})
        return data


import pyvisflow.core.components.tabs as tabs