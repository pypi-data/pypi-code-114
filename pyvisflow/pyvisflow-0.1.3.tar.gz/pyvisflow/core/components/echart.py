from abc import abstractmethod
from typing import Any, Dict, List, Union
from pyvisflow.core.dataManager import TDataFrameInfo
from pyvisflow.core.props import SubscriptableTypePropInfo, StrTypePropInfo, NumberTypePropInfo
from pyvisflow.core.props.dataFilterProp import DataFilterPropInfo
from pyvisflow.core.props.nameProp import NamePropInfo
from pyvisflow.core.props.typeProp import BoolTypePropInfo, TypePropInfo
from pyvisflow.core.reactive import Reactive
from pyvisflow.models.TComponent import TComponentType
import pandas as pd

from pyvisflow.models.TWatchInfo import TChartFilterWatch, TChartFilterTarget
from pyvisflow.utils.helper import df2array_dict
from .auto_create._echart import _EChart


class EChart(_EChart):

    __prop_path_mapping = {
        'title': 'option.title.text',
    }

    def __init__(
            self,
            data_info: TDataFrameInfo,
    ) -> None:
        super().__init__()

        self._data_id = data_info
        self._series = []
        self.update_styles(height='400px', width='100%')
        self._filter_watch_infos: List[TChartFilterWatch] = []

    def bar(self, x: str, y: str):
        self.add_series('bar', x, y)
        return self

    def pie(self, ):
        self._series.append({'type': 'pie'})

    def area(self, x: str, y: str):
        self._series.append({
            'type': 'line',
            'encode': {
                'x': x,
                'y': y
            },
            "areaStyle": {},
            "symbol": "none",
            "lineStyle": {
                "width": 0
            },
            "id": "test",
            "universalTransition": True,
        })

    def add_series(self, type: str, x: str, y: str):
        self._series.append({
            'type': type,
            'encode': {
                'x': x,
                'y': y
            },
            "id": "test",
            "universalTransition": True,
        })

        return self

    def set_option(self, prop: str, data: Union[Any, TypePropInfo]):
        if not prop.startswith('option.'):
            prop = f'option.{prop}'
        self.set_prop(prop, data)
        return self

    @property
    def series(self):
        p = self.get_prop('option.series')
        return SubscriptableTypePropInfo[str, StrTypePropInfo](p)

    @property
    def clickInfo(self):
        p = self.get_prop('clickInfo')
        return SubscriptableTypePropInfo[str, StrTypePropInfo](p)

    @property
    def data(self):
        p = DataFilterPropInfo('row')
        return SubscriptableTypePropInfo[str, StrTypePropInfo](p)

    def filters(self, condition: BoolTypePropInfo):
        logic = condition.valuator.cal(condition)
        target = TChartFilterTarget(id=self._id, logic=logic)
        filter = TChartFilterWatch(target=target)
        self._filter_watch_infos.append(filter)

    def _ex_get_react_data(self):
        data = super()._ex_get_react_data()
        data.update({
            'dataInfo': {
                'id': self._data_id.id
            },
            'option': {
                'tooltip': {},
                'dataset': {
                    'dimensions': [],
                    'source': {}
                },
                'xAxis': {},
                'yAxis': {},
                'series': []
            },
            'clickInfo': {},
        })
        return data
