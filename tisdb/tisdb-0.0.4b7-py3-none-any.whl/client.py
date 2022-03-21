# -*- coding: utf-8


from copy import deepcopy
from datetime import datetime, date
from typing import Dict, List

from sortedcontainers.sorteddict import SortedDict
from tisdb.api import TsdbApi
from tisdb.config import TsdbConfig
from tisdb.errors import ParamError
from tisdb.model.mysql import TSDB_CONFIG
from tisdb.types import OpType, StoreType
from tisdb.model import SaveResult, TsdbData, TsdbFields, TsdbTags
from porm.databases import MyDBApi


class TsdbClient(object):
    """Tsdb Client

    Args:
        store_type (StoreType): Tsdb store type support PORM,MYSQL,TIDB
        conn_conf (TsdbConfig): Tsdb connecting configuration
    """

    def __init__(
        self,
        store_type: StoreType = StoreType.PORM,
        conn_conf: TsdbConfig = TsdbConfig(),
    ):
        super().__init__()
        self.store_type = store_type
        self.config = conn_conf
        self.api = TsdbApi(self.store_type, self.config)
        # self.api.activate()

    def save(self, value: TsdbData, op_type: OpType = OpType.UPSERT) -> SaveResult:
        """Save timestamp data

        Args:
            value (TsdbData): Timestamp value to save
            op_type (OpType, optional): Saving operation type. Defaults to OpType.INSERT_IGNORE.

        Returns:
            SaveResult: Result of this save
        """
        if op_type == OpType.INSERT_IGNORE:
            ret = self.api.insert_ignore(value)
        elif op_type == OpType.UPSERT:
            ret = self.api.upsert(value)
        elif op_type == OpType.INSERT_ON_DUPLICATE_KEY_UPDATE:
            # ret = self.api.insert_on_duplicate_key_update(value)
            pass
        else:
            ret = self.api.insert_ignore(value)

        return SaveResult(data=[ret])

    def save_many(
        self, value: List[TsdbData], op_type: OpType = OpType.UPSERT
    ) -> SaveResult:
        """Save timestamp data in batch

        Args:
            value (List[TsdbData]): Timestamp value to save in batch
            op_type (OpType, optional): Saving operation type. Defaults to OpType.INSERT_IGNORE.

        Returns:
            List[SaveResult]:  Result of this save in batch
        """
        if op_type == OpType.INSERT_IGNORE:
            ret = self.api.insert_ignore_batch(value)
        elif op_type == OpType.UPSERT:
            ret = self.api.upsert_batch(value)
        elif op_type == OpType.INSERT_ON_DUPLICATE_KEY_UPDATE:
            # ret = self.api.insert_on_duplicate_key_update(value)
            pass
        else:
            ret = self.api.insert_ignore_batch(value)

        return SaveResult(data=ret)

    def parse_many(self, values: List[dict]) -> List[TsdbData]:
        """Parse many tsdb data from list

        Args:
            values (List[dict]): Tsdb data presents in dict type

        Returns:
            List[TsdbData]: parsed tsdb data list
        """
        return [self.parse(val) for val in values]

    def parse(self, value: Dict[str, object]) -> TsdbData:
        """Parse tsdb data from dictionary

        Args:
            value (dict): Tsdb data presents in dict type

        Returns:
            TsdbData: parsed tsdb data
        """
        ts_tmp = value["ts"]
        if isinstance(ts_tmp, datetime):
            ts = ts_tmp
        elif isinstance(ts_tmp, str):
            ts = datetime.fromisoformat(ts_tmp)
        elif isinstance(ts_tmp, date):
            ts = datetime(*ts_tmp.timetuple()[:6])
        else:
            ts = datetime.fromisoformat(ts_tmp)
        return TsdbData(
            metric=value["metric"],
            ts=ts,
            tags=TsdbTags(**value.get("tag", {})),
            fields=TsdbFields(
                value=value.get("field", {}).get(
                    "value", value.get("value", 0))
            ),
        )

    def _create_mydb(self, conn_conf: dict = None) -> MyDBApi:
        """Create api from mydb

        Args:
            conn_conf (dict, optional): connection config. Defaults to None.

        Returns:
            MyDBApi: mydb api of given connection configuration
        """
        conf = TSDB_CONFIG.copy()
        if conn_conf is not None:
            conf.update(conn_conf)
        return MyDBApi(database_name=conf.get("db", None), **conf)

    def create_tsdbdata_mydb(
        self, sql: str, param: dict = None, conn_conf: dict = None
    ) -> List[Dict]:
        """Create tsdbdata from mydb

        Args:
            sql (str): sql to excute that create ts data
            param (dict, optional): sql param. Defaults to None.
            conn_conf (dict, optional): connection config. Defaults to None.

        Returns:
            List[Dict]: ts data created from sql
        """
        mydb = self._create_mydb(conn_conf=conn_conf)
        ret = []
        for res in mydb.query_many(sql, param=param):
            ret.extend(self._parse_mydb_result(res))
        return ret

    def _parse_mydb_result(self, result: dict) -> List[Dict]:
        """Parse mydb query result to tsdb dict like format

        Args:
            result (dict): Mydb format data

        Raises:
            ParamError: Error when missing key needed or meeting key undefined

        Returns:
            List[Dict]: Tsdb dict format data
        """
        ts_tag = SortedDict()
        _metric_prefix = None
        _metric_sufix_value = {}
        _value = None
        _ts = None
        for key, val in result.items():
            if key == "metric":
                _metric_prefix = val
            elif key.startswith("tag"):
                # select 'm' as metric, 'g18' as tag_gameid, 'ntes' as tag_channel
                # 中抽取tag_后的字段作为tsvals的tag key
                ts_tag[key.split("_", 1)[1]] = val
            elif key == "ts":
                _ts = val
            elif key == "value":
                _value = val
            elif key.startswith("fieldvalue"):
                _metric_sub = key.split("_", 1)[-1]
                _metric_sufix_value[_metric_sub] = val
            else:
                raise ParamError(f"Error key: {key}")
        ret = []
        if _metric_sufix_value:
            ret.extend(
                {
                    "metric": f"{_metric_prefix}_{metric_sufix}",
                    "tag": ts_tag,
                    "ts": _ts,
                    "value": value,
                }
                for metric_sufix, value in _metric_sufix_value.items()
            )

        else:
            ret.append(
                {"metric": _metric_prefix, "tag": ts_tag, "ts": _ts, "value": _value}
            )
        return ret
