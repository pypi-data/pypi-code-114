# -*- coding: utf-8

from collections import defaultdict
from typing import List
from porm.databases.api import _transaction
from tisdb.config import TsdbConfig
from tisdb.errors import FakeError
from tisdb.model.metricdb import TimeWindow
from tisdb.types import StoreType
from tisdb.model.mysql import Mtsv, Tkv, TkvUkRel, Metric, Tag, Tag_Rel
from tisdb.model import TsdbData, TsdbTags, MetricdbData, TsdbFields
from tisdb.types import StoreType
from datetime import datetime as dt


class TsdbApi(object):
    def __init__(self, store_type: StoreType, config: TsdbConfig):
        super().__init__()
        self._store_type = store_type
        self._config = config
        Mtsv.__CONFIG__.update(self._config)
        Tkv.__CONFIG__.update(self._config)
        TkvUkRel.__CONFIG__.update(self._config)

    def activate(self):
        value = TsdbData(metric="tisdb_test", tags=TsdbTags(env="test"))
        try:
            if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
                return self._test_insert_mydb(value)
            else:
                return self._test_insert_mydb(value)
        except Exception as ex:
            if not isinstance(ex, FakeError):
                raise ex

    def insert_ignore(self, value: TsdbData) -> TsdbData:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb(value)
        else:
            return self._insert_ignore_mydb(value)

    def insert_ignore_batch(self, value: List[TsdbData]) -> List[TsdbData]:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb_batch(value)
        else:
            return self._insert_ignore_mydb_batch(value)

    def _insert_ignore_mydb(self, value: TsdbData) -> TsdbData:
        """insert tsdb data into mysql type db

        Args:
            value (TsdbData): tsdb data

        Returns:
            TsdbData: tsdb data
        """
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        with mtsv.start_transaction() as _t:
            value.value_id = self._insert_tsdbdata(mtsv, value.tags, _t)
            return value

    def _insert_tsdbdata(self, mtsv: Mtsv, tags: TsdbTags, _t: _transaction) -> int:
        rels = []
        inserts = [Tkv.new(tagk=tagk, tagv=tagv) for tagk, tagv in tags.items()]
        Tkv.insert_many(inserts, t=_t, ignore=True)
        for tagk, tagv in tags.items():
            tkv = Tkv.get_one(t=_t, tagk=tagk, tagv=tagv)
            rel = TkvUkRel.new(tkv_pk=tkv.zzid, taguk=mtsv.taguk)
            rels.append(rel)
        TkvUkRel.insert_many(rels, t=_t, ignore=True)
        Mtsv.insert_many([mtsv], t=_t, ignore=True)
        ret = Mtsv.get_one(t=_t, metric=mtsv.metric,
                           ts=mtsv.ts, taguk=mtsv.taguk)
        return ret.zzid

    def _insert_ignore_mydb_batch(
        self, value: List[TsdbData], upsert=False
    ) -> List[TsdbData]:
        """insert tsdb data into mysql store in batch

        Args:
            value (List[TsdbData]): tsdb data to insert
            upsert (bool, optional): if update or insert data already in the store. Defaults to False.

        Returns:
            List[TsdbData]: tsdb data that newly inserted with pkid
        """
        if len(value) == 0:
            return []
        mtsvmaps = defaultdict(lambda: defaultdict(dict))
        for _v in value:
            mtsvmap = mtsvmaps[_v.metric]
            if "mtsv" not in mtsvmap[_v.tags_uuid]:
                mtsvmap[_v.tags_uuid]["mtsv"] = []
                mtsvmap[_v.tags_uuid]["tsdb"] = []
                mtsvmap[_v.tags_uuid]["tagkv"] = [
                    Tkv.new(tagk=tagk, tagv=tagv) for tagk, tagv in _v.tags.items()
                ]
                if upsert:
                    mtsvmap[_v.tags_uuid]["delete_terms"] = {
                        "metric": _v.metric,
                        "taguk": _v.tags_uuid,
                        "ts": (set(), "IN"),
                    }
            mtsvmap[_v.tags_uuid]["mtsv"].append(
                Mtsv.new(
                    metric=_v.metric,
                    ts=_v.ts,
                    taguk=_v.tags_uuid,
                    value=_v.get_value("value"),
                )
            )
            mtsvmap[_v.tags_uuid]["tsdb"].append(_v)
            if upsert:
                mtsvmap[_v.tags_uuid]["delete_terms"]["ts"][0].add(_v.ts)
            mtsvmaps[_v.metric] = mtsvmap
        rets = []
        _mtsv_obj = list(list(mtsvmaps.values())[0].values())[0]["mtsv"][0]
        with _mtsv_obj.start_transaction() as _t:
            for mtsvmap in mtsvmaps.values():
                for tags_uuid, mtsvtagkv in mtsvmap.items():
                    if upsert:
                        Mtsv.delete_many(t=_t, **mtsvtagkv["delete_terms"])
                    idx = 0
                    for ret in self._insert_tsdbdata_batch(
                        tags_uuid, mtsvtagkv["mtsv"], mtsvtagkv["tagkv"], _t
                    ):
                        mtsvtagkv["tsdb"][idx].value_id = ret.zzid
                        rets.append(mtsvtagkv["tsdb"][idx])
                        idx += 1
        return rets

    def _insert_tsdbdata_batch(
        self,
        tags_uuid: str,
        mtsvs: List[Mtsv],
        tkvs: List[Tkv],
        _t: _transaction,
    ) -> List[Mtsv]:
        """insert formatted tsdb data in batch

        Args:
            tags_uuid (str): uuid of these ts data
            mtsvs (List[Mtsv]): ts data
            tkvs (List[Tkv]): tags of these ts data
            _t (_transaction): transaction of this save

        Returns:
            List[Mtsv]: ts data with pkid
        """
        rels = []
        rets = []
        Tkv.insert_many(tkvs, t=_t, ignore=True)
        for _tkv in tkvs:
            tkv = Tkv.get_one(t=_t, **_tkv)
            rels.append(TkvUkRel.new(tkv_pk=tkv.zzid, taguk=tags_uuid))
        TkvUkRel.insert_many(rels, t=_t, ignore=True)
        Mtsv.insert_many(mtsvs, t=_t, ignore=True)
        for mtsv in mtsvs:
            ret = Mtsv.get_one(t=_t, metric=mtsv.metric,
                               ts=mtsv.ts, taguk=mtsv.taguk)
            rets.append(ret)
        return rets

    def upsert(self, value: TsdbData) -> TsdbData:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._upsert_mydb(value)
        else:
            return self._upsert_mydb(value)

    def _upsert_mydb(self, value: TsdbData) -> TsdbData:
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        with mtsv.start_transaction() as _t:
            Mtsv.delete_many(t=_t, metric=mtsv.metric,
                             ts=mtsv.ts, taguk=mtsv.taguk)
            value.value_id = self._insert_tsdbdata(mtsv, value.tags, _t)
            return value

    def upsert_batch(self, value: List[TsdbData]) -> List[TsdbData]:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb_batch(value, upsert=True)
        else:
            return self._insert_ignore_mydb_batch(value, upsert=True)

    def _test_insert_mydb(self, value: TsdbData) -> TsdbData:
        mtsv = Mtsv.new(
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            value=value.get_value("value"),
        )
        with mtsv.start_transaction() as _t:
            self._insert_tsdbdata(mtsv, value.tags, _t)
            raise FakeError()


class MetricdbApi(TsdbApi):
    def __init__(self, store_type: StoreType, config: TsdbConfig):
        super().__init__(store_type=store_type, config=config)
        self._store_type = store_type
        self._config = config
        Metric.__CONFIG__.update(self._config)
        Tag.__CONFIG__.update(self._config)
        Tag_Rel.__CONFIG__.update(self._config)

    def activate(self):
        value = MetricdbData(
            metric="tisdb_test", tags=TsdbTags(env="test"), fields=TsdbFields(
            value=311), tw=TimeWindow('DAY_1'), ts=dt.now())
        try:
            if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
                return self._test_insert_mydb(value)
            else:
                return self._test_insert_mydb(value)
        except Exception as ex:
            if not isinstance(ex, FakeError):
                raise ex

    def insert_ignore_batch(self, value: List[MetricdbData]) -> List[MetricdbData]:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb_batch(value)
        else:
            return self._insert_ignore_mydb_batch(value)

    def _insert_ignore_mydb_batch(
        self, value: List[MetricdbData], upsert=False,
        _t: _transaction = None
    ) -> List[MetricdbData]:
        """insert metricdb data into mysql store in batch

        Args:
            value (List[MetricdbData]): metricdb data to insert
            upsert (bool, optional): if update or insert data already in the store. Defaults to False.

        Returns:
            List[MetricdbData]: tsdb data that newly inserted with pkid
        """
        if len(value) == 0:
            return []
        metricmaps = defaultdict(lambda: defaultdict(dict))
        for _v in value:
            metricmap = metricmaps[_v.metric]
            if "metric" not in metricmap[_v.tags_uuid]:
                metricmap[_v.tags_uuid]["metric"] = []
                metricmap[_v.tags_uuid]["metricdb"] = []
                metricmap[_v.tags_uuid]["tag"] = [
                    Tag.new(tagk=tagk, tagv=tagv, tagid=TsdbTags.tagidf(tagk, tagv)) for tagk, tagv in _v.tags.items()
                ]
                if upsert:
                    metricmap[_v.tags_uuid]["delete_terms"] = {
                        "bid": _v.bid,
                        "metric": _v.metric,
                        "taguk": _v.tags_uuid,
                        "ts": (set(), "IN"),
                    }
            metricmap[_v.tags_uuid]["metric"].append(
                [
                    Metric.new(
                        bid=_v.bid,
                        metric=_v.metric,
                        ts=_v.ts,
                        taguk=_v.tags_uuid,
                        fieldk=_fk,
                        fieldv=_fv,
                    ) for _fk, _fv in _v.fields.items()
                ]
            )
            metricmap[_v.tags_uuid]["metricdb"].append(_v)
            if upsert:
                metricmap[_v.tags_uuid]["delete_terms"]["ts"][0].add(_v.ts)
            metricmaps[_v.metric] = metricmap
        rets = {}
        _metric_obj = list(list(metricmaps.values())[0].values())[0]["metric"][0][0]
        with _metric_obj.start_transaction() as _t:
            for metricmap in metricmaps.values():
                for tags_uuid, mtsvtagkv in metricmap.items():
                    if upsert:
                        Metric.delete_many(t=_t, **mtsvtagkv["delete_terms"])
                    for _m in self._insert_metricdbdata_batch(
                        tags_uuid, mtsvtagkv["metric"], mtsvtagkv["tag"], _t
                    ):
                        if _m.bid in rets:
                            metric_data = rets.get(_m.bid)
                            metric_data.fields[_m.fieldk] = _m.fieldv
                        else:
                            _f = TsdbFields()
                            _f[_m.fieldk] = _m.fieldv
                            ret = MetricdbData(metric=_m.metric, ts=_m.ts,
                                         fields=_f, bid=_m.bid)
                            rets[_m.bid] = ret
        return list(rets.values())

    def _insert_metricdbdata_batch(
        self,
        tags_uuid: str,
        mtsvs: List[List[Metric]],
        tkvs: List[Tag],
        _t: _transaction,
    ) -> List[Metric]:
        """insert formatted metric data in batch

        Args:
            tags_uuid (str): uuid of these ts data
            mtsvs (List[List[Metric]]): ts data
            tkvs (List[Tag]): tags of these ts data
            _t (_transaction): transaction of this save

        Returns:
            List[Metric]: ts data with pkid
        """
        Tag.insert_many(tkvs, t=_t, ignore=True)
        Tag_Rel.insert_many(
            [Tag_Rel.new(tagid=tkv.tagid, taguk=tags_uuid) for tkv in tkvs], t=_t, ignore=True)
        metrics = []
        for _m in mtsvs:
            metrics.extend(_m)
        Metric.insert_many(metrics, t=_t, ignore=True)
        rets = []
        for _m in metrics:
            ret = Metric.get_one(t=_t, bid=_m.bid, metric=_m.metric,
                                 ts=_m.ts, taguk=_m.taguk, fieldk=_m.fieldk)
            rets.append(ret)
        return rets

    def upsert_batch(self, value: List[MetricdbData]) -> List[MetricdbData]:
        if self._store_type in (StoreType.PORM, StoreType.MYSQL, StoreType.TIDB):
            return self._insert_ignore_mydb_batch(value, upsert=True)
        else:
            return self._insert_ignore_mydb_batch(value, upsert=True)

    def _test_insert_mydb(self, value: MetricdbData) -> MetricdbData:
        metrics = [Metric.new(
            bid=value.bid,
            metric=value.metric,
            ts=value.ts,
            taguk=value.tags_uuid,
            fieldk=_fk,
            fieldv=_fv) for _fk, _fv in value.fields.items()
        ]
        with metrics[0].start_transaction() as _t:
            self._insert_metricdbdata_batch(value.tags_uuid, [metrics], [], _t)
            raise FakeError()
