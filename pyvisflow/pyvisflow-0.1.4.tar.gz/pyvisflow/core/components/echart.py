from abc import abstractmethod
from typing import Any, Dict, List, Optional, Union
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
    def __init__(
            self,
            data_info: TDataFrameInfo,
    ) -> None:
        super().__init__()
        self._data_id = data_info
        self._series = []
        self.update_styles(height='400px', width='100%')
        self._filter_watch_infos: List[TChartFilterWatch] = []

    @property
    def utils(self, ):
        return Helper(self)

    def bar(self, x: str, y: str):
        self.set_option('series', [{
            'type': 'bar',
            'showBackground': True,
            'backgroundStyle': {
                'color': 'rgba(180, 180, 180, 0.2)'
            },
            'encode': {
                'x': x,
                'y': y
            },
            'id': self._id,
            "universalTransition": True,
        }]) \
        .set_option('xAxis', {'type': 'category'}) \
        .set_option('legend', {
                                'top': '5%',
                                'left': 'center'
                            },)

        return self

    def pie(self, itemName: str, value: str):
        self.set_option('series', [{
            'type': 'pie',
            'encode': {
                'itemName': itemName,
                'value': value
            },
            'id': self._id,
            "universalTransition": True,
        }]) \
        .set_option('xAxis', {'type': 'category'}) \
        .set_option('legend', {
                                'top': '5%',
                                'left': 'center'
                            },)
        return self

    def area(self, x: str, y: str):
        self.set_option('series', [{
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
            'id': self._id,
            "universalTransition": True,
        }]).set_option('xAxis', {'type': 'category'})

        return self

    def change_encode(self,
                      x: Union[str, StrTypePropInfo],
                      y: Union[str, StrTypePropInfo],
                      series_idx=0):

        encode = {'x': x, 'y': y}
        self.set_option(f'series[{series_idx}].encode', encode)

    # def change_axis(self,
    #                   xAxis: Union[str, StrTypePropInfo],
    #                   yAxis: Union[str, StrTypePropInfo]):

    #     encode = {
    #         'x':x,
    #         'y':y
    #     }
    #     self.set_option(f'xAxis', {
    #         'type':xAxisType
    #     })

    def set_option(self, prop: str, data: Union[Any, TypePropInfo]):
        if not prop.startswith('option.'):
            prop = f'option.{prop}'
        self.set_prop(prop, data)
        return self

    def set_series(self, idx: int, prop: str, data: Union[Any, TypePropInfo]):
        self.set_option(f'series[{idx}].{prop}', data)
        return self

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


class Helper():
    def __init__(self, echart: EChart) -> None:
        self._echart = echart

    def use_pie(self, itemName: str, value: str):
        self._echart.set_option('series', [{
            'type': 'pie',
            'encode': {
                'itemName': itemName,
                'value': value
            },
            'id': self._echart._id,
            "universalTransition": True,
        }]) \
        .set_option('legend', {
                                'top': '5%',
                                'left': 'center'
                            },)
        return PieHelper(self._echart)

    def use_bar(self, x: str, y: str):
        self._echart.set_option('series', [{
            'type': 'bar',
            'showBackground': True,
            'backgroundStyle': {
                'color': 'rgba(180, 180, 180, 0.2)'
            },
            'encode': {
                'x': x,
                'y': y
            },
            'id': self._echart._id,
            "universalTransition": True,
        }]).set_option('xAxis', {'type': 'category'})
        return BarHelper(self._echart)

    def use_line(self, x: str, y: str, color: Optional[str] = None):
        self._echart.set_option('series', [{
            'type': 'line',
            'encode': {
                'x': x,
                'y': y,
                'color' :color
            },
            'id': self._echart._id,
            "universalTransition": True,
        }]) \
        .set_option('xAxis', {'type': 'category'}) \
        .set_option('yAxis', {'type': 'value'}) \
        .set_option('tooltip', {'trigger': 'axis'})
        return LineHelper(self._echart)


class LineHelper():
    def __init__(self, echart: EChart) -> None:
        self._echart = echart

    def area_chart(self):
        '''
        基础面积图
        '''
        self._echart \
                    .set_series(0, 'areaStyle', {}) \
                    .set_series(0,'symbol','none') \
                    .set_series(0,'sampling','lttb') \
                    .set_series(0,  "lineStyle",{"width": 0}) \
                    .set_option('xAxis', {'type': 'category'})

        return self

    def smooth(self):
        '''
        平滑化
        '''
        self._echart \
                    .set_series(0, 'smooth', True) \

        return self


class BarHelper():
    def __init__(self, echart: EChart) -> None:
        self._echart = echart

    def showBackground(self, color: str = 'rgba(180, 180, 180, 0.2)'):
        '''
        显示柱子背景
        '''
        self._echart \
                    .set_series(0, 'showBackground', True) \
                    .set_series(0, 'backgroundStyle',  {
                        'color': color
                    }) \

        return self


class PieHelper():
    def __init__(self, echart: EChart) -> None:
        self._echart = echart

    def circle_chart(self):
        '''
        圆环图
        '''
        self._echart.set_series(0, 'labelLine', {
            'show': False
        }).set_series(0, 'emphasis', {
            'label': {
                'show': True,
                'fontSize': '40',
                'fontWeight': 'bold'
            }
        }).set_series(0, 'label', {
            'show': False,
            'position': 'center'
        }).set_series(0, 'itemStyle', {
            'borderRadius': 10,
            'borderColor': '#fff',
            'borderWidth': 2
        }).set_series(0, 'avoidLabelOverlap', False).set_series(
            0, 'radius', ['40%', '70%']).set_series(0, 'type', 'pie')

        return self

    def nightingale_rose_chart(self):
        '''
        南丁格尔玫瑰图
        '''
        self._echart \
                    .set_series(0, 'type', 'pie') \
                    .set_series(0, 'center',  ['50%', '50%']) \
                    .set_series(0, 'roseType', 'area') \
                    .set_series(0, 'itemStyle', {
                                                'borderRadius': 8
                                            }) \

        return self