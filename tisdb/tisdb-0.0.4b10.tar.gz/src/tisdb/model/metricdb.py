# -*- coding: utf-8 -*-

from __future__ import annotations
from ast import Dict, List
import datetime
import dateutil.parser as dtparser
from enum import Enum
import simplejson as json
from tisdb.errors import BaseInfo, ParamError
from tisdb.model.tsdb import TsdbData, TsdbFields, TsdbTags
from hashlib import md5


class Unit(Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"
    WEEK = "week"
    MONTH = "month"


class TimeWindow(object):
    """Time window object

    Args:
        tw_str (str): time window string like "day_1"
    """

    def __init__(self, tw_str: str) -> None:
        self._unit, self._tw = tw_str.lower().split("_")
        self._tw = int(self._tw)
        self._unit = Unit[self._unit.upper()]

    def __str__(self) -> str:
        return f'{self._unit.value}_{self._tw}'.upper()


class MetricdbData(TsdbData):
    def __init__(
            self, metric: str, ts: datetime = datetime.datetime.now(), tags: TsdbTags = TsdbTags(), fields: TsdbFields = TsdbFields(),
            tw: TimeWindow = None, bid: str = None):
        super().__init__(metric, ts, tags, fields)
        self['tw'] = tw
        if bid:
            self._bid = bid
        else:
            uuid_gen = md5()
            bid_dict = self.get_data_key()
            _val = self.get_data_value()
            bid_dict.update(_val.pop('tag'))
            for key in _val['field'].keys():
                _val['field'][key] = None
            bid_dict.update(_val)
            uuid_gen.update(json.dumps(bid_dict).encode(encoding="utf-8"))
            self._bid = uuid_gen.hexdigest()

    @property
    def tw(self) -> TimeWindow:
        return self['tw']

    @property
    def fields(self) -> TsdbFields:
        return self['field']

    @property
    def bid(self) -> str:
        return self._bid

    @staticmethod
    def from_dict(data: Dict[str, object]) -> MetricdbData:
        tags = TsdbTags()
        fields = TsdbFields()
        _metric = None
        _tw = None
        _ts = None
        for col, val in data.items():
            col = col.lower()
            if col == 'metric':
                _metric = val
            elif col.startswith('tag'):
                _, _tagk = col.lower().split('_', 1)
                if _tagk == 'tw':
                    _tw = TimeWindow(val)
                tags[_tagk] = val
            elif col == 'value':
                fields[col] = val
            elif col.startswith('fieldvalue'):
                fields[col.split('_', 1)[1]] = val
            elif col == 'ts':
                _ts = dtparser.parse(val)
            else:
                raise ParamError(f"Error key: {col}")
        return MetricdbData(metric=_metric, tags=tags, fields=fields, tw=_tw, ts=_ts)

    def get_data_key(self) -> dict:
        """return key as icuser key

        Returns:
            dict: _description_
        """
        return {
            'metric': self.metric,
            'tw': str(self.tw),
            'ts': int(self.ts.timestamp() * 1000)
        }

    def get_data_value(self) -> dict:
        """return value as icuser value

        Returns:
            dict: {"tag":{}, "field": {}}
        """
        return {
            "field": self.fields.copy(),
            "tag": self.tags.copy(),
        }


class SaveResult(object):
    """Result of the save function

    Args:
        data (List[MetricdbData]): Tsdb data to save this time
        subcode (int): return subcode of this save result
        status (str): status of this save result
    """

    def __init__(
        self, data: List[MetricdbData], subcode: int = None, status: str = None
    ) -> None:
        super().__init__()
        self._data = data
        self._subcode = subcode or BaseInfo.SUBCODE
        self._status = status or BaseInfo.STATUS

    @property
    def data(self):
        return self._data
