import typing as t

import pandas as pd
import pytest
from pydantic import BaseModel
from taktile_types.enums.monitor import MonitorType
from taktile_types.schemas.monitor import MonitorData, MonitoringPayload

from tktl.future.monitor import Tracker, extract_monitor_element


class Model3(BaseModel):
    a: int
    b: float
    c: bool
    d: str


class Model2(BaseModel):
    a: t.Optional[int]
    b: t.Optional[float]
    c: t.Optional[bool]
    d: t.Optional[str]
    e: Model3


class Model1(BaseModel):
    a: int
    b: float
    c: bool
    d: str
    e: Model2


TEST_INSTANCE = Model1(
    a=1, b=2.0, c=True, d="string", e=Model2(e=Model3(a=5, b=6.0, c=False, d="string2"))
)


@pytest.mark.parametrize(
    "column, key, result, type_",
    [
        (pd.Series([1, 2, 3], dtype="int64"), "test", [1, 2, 3], MonitorType.NUMERIC),
        (
            pd.Series([1.0, 2.0, 3.0], dtype="float64"),
            "test",
            [1.0, 2.0, 3.0],
            MonitorType.NUMERIC,
        ),
        (
            pd.Series(["c", "", None], dtype="object"),
            "test",
            ["c", "", None],
            MonitorType.CATEGORY,
        ),
        (
            pd.Series([True, False, True], dtype="bool"),
            "test",
            [True, False, True],
            MonitorType.CATEGORY,
        ),
        (
            pd.Series(["a", "b", None], dtype="category"),
            "test",
            ["a", "b", None],
            MonitorType.CATEGORY,
        ),
        (
            pd.Series([1, 2, 3], dtype="category"),
            "test",
            [1, 2, 3],
            MonitorType.CATEGORY,
        ),
        (
            pd.Series(["2020-01-01", None, "2020-01-03"], dtype="datetime64[ns]"),
            "test",
            [1577836800, None, 1578009600],
            MonitorType.CATEGORY,
        ),
        (TEST_INSTANCE, "a", [1], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "b", [2.0], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "c", [True], MonitorType.CATEGORY,),
        (TEST_INSTANCE, "d", ["string"], MonitorType.CATEGORY,),
        (TEST_INSTANCE, "e.a", [None], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "e.b", [None], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "e.c", [None], MonitorType.CATEGORY,),
        (TEST_INSTANCE, "e.d", [None], MonitorType.CATEGORY,),
        (TEST_INSTANCE, "e.e.a", [5], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "e.e.b", [6.0], MonitorType.NUMERIC,),
        (TEST_INSTANCE, "e.e.c", [False], MonitorType.CATEGORY,),
        (TEST_INSTANCE, "e.e.d", ["string2"], MonitorType.CATEGORY,),
    ],
)
def test_monitor_extraction(column, key, result, type_):
    assert extract_monitor_element(column, key) == (result, type_)


def test_tracker():
    class FakeRequest:
        headers = {"user-agent": "test-agent"}

    tracker = Tracker(FakeRequest(), endpoint_name="test")

    tracker.log_categorical("key1", "value1")
    tracker.log_numerical("key2", 2)

    final_payload = tracker.finalize_payload()

    assert final_payload == MonitoringPayload(
        data={
            "key1": MonitorData(value=["value1"], type=MonitorType.CATEGORY),
            "key2": MonitorData(value=[2], type=MonitorType.NUMERIC),
        },
        timestamp=final_payload.timestamp,
        user_agent="test-agent",
        endpoint="test",
        git_sha="unknown",
        git_ref="unknown",
        repository_id="unknown",
    )
