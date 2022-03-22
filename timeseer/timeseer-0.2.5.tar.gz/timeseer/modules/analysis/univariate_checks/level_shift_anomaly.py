"""Anomaly based on level shift.

<p>Anomaly detection based on a significant difference in the means of
two consecutive sliding windows.</p>
<p><img src='../static/images/reporting/level_shift.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where a level shift anomaly occurs. Imagine that 100 points are analyzed in a given time-frame
and there are 10 level shift anomalies. The score for this check in that case would be
90% = 1 - 10 / 100. Which means that for 90% of all points no level shift anomaly occurs.</p>
<div class="ts-check-impact">
<p>
Level shifts could be indications of physical altercations to a sensor (e.g. camera being bumped) or
other types of issues within the sensor.
Several calculations are sensitive to these type of sudden changes and process decision chains
based on such an outlier can propagate through the system.
Any type of anomaly detection based on normal behavior of the phyiscal sensor can act as a guide for
prioritization of callibration / maintenance.
</p>
</div>
"""

import logging

from typing import List

import numpy as np
import pandas as pd

from adtk.detector import LevelShiftAD
from pandas.api.types import is_string_dtype

import timeseer

from timeseer import DataType, InterpolationType
from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    merge_intervals_and_open_event_frames,
    process_open_intervals,
    calculate_local_score,
)


_CHECK_NAME = "Level Shift Anomaly"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Validity",
            "event_frames": ["Level Shift Anomaly"],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_weeks": 1,
            "min_data_points": 300,
            "data_type": [DataType.FLOAT32, DataType.FLOAT64],
            "interpolation_type": [None, InterpolationType.LINEAR],
        }
    ],
    "signature": "univariate",
}

logger = logging.getLogger(__name__)


def _get_intervals(active_points, df, event_type):
    interval_grp = (active_points != active_points.shift().bfill()).cumsum()
    active_points[active_points.isna()] = 0
    active_points = np.array(active_points, dtype=bool)
    intervals = (
        df.assign(interval_grp=interval_grp)[active_points]
        .reset_index()
        .groupby(["interval_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    intervals["type"] = event_type
    return intervals


def _get_last_analyzed_point(df, window_size):
    if len(df) < window_size:
        return df.index[0]
    last_index = -2 * window_size
    return df.index[last_index]


def _handle_open_intervals(df, intervals):
    intervals["open"] = intervals["end_date"] == df.index[-1]
    return intervals


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _run_level_shift_ad(analysis_input, median_archival_step, open_event_frames):
    df = _clean_dataframe(analysis_input.data)

    window_size = 10
    if len(df["value"]) <= window_size:
        return None, pd.DataFrame(), df.index[0]

    analysis_start = df.index[0]
    if analysis_input.analysis_start is not None:
        analysis_start = analysis_input.analysis_start

    level_ad = LevelShiftAD(window=10)
    try:
        active_points = level_ad.fit_detect(df["value"])
    except (ValueError, RuntimeError) as err:
        logger.error("Error in level shift anomaly: %s", err)
        return None, pd.DataFrame(), _get_last_analyzed_point(df, window_size)

    intervals = _get_intervals(active_points, df, _CHECK_NAME)
    intervals = _handle_open_intervals(df, intervals)
    intervals = merge_intervals_and_open_event_frames(
        analysis_start, intervals, open_event_frames
    )

    percentage = calculate_local_score(
        df, analysis_start, intervals, median_archival_step
    )

    frames = event_frames_from_dataframe(process_open_intervals(intervals))

    last_analyzed_point = _get_last_analyzed_point(df, window_size)

    return percentage, list(frames), last_analyzed_point


def _is_relevant_open_event_frame(event_frame):
    return (
        event_frame.end_date is None
        and event_frame.type in META["checks"][0]["event_frames"]
    )


def _get_open_event_frames(
    analysis_input: timeseer.AnalysisInput,
) -> List[timeseer.EventFrame]:
    return [
        frame
        for frame in analysis_input.event_frames
        if _is_relevant_open_event_frame(frame)
    ]


def _get_relevant_statistic(analysis_input, requested_statistic):
    stat = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == requested_statistic
    ]
    if len(stat) == 0:
        return None
    return stat


def _is_valid_input(analysis_input: timeseer.AnalysisInput) -> bool:
    if len(_clean_dataframe(analysis_input.data)) == 0:
        return False
    if is_string_dtype(analysis_input.data["value"]):
        return False
    return True


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    if not _is_valid_input(analysis_input):
        return timeseer.AnalysisResult()

    median_archival_step = _get_relevant_statistic(
        analysis_input, "Archival time median"
    )
    if median_archival_step is None:
        return timeseer.AnalysisResult()

    open_event_frames = _get_open_event_frames(analysis_input)

    pct_anomaly, frames, last_analyzed_point = _run_level_shift_ad(
        analysis_input, median_archival_step[0], open_event_frames
    )

    if pct_anomaly is None:
        return timeseer.AnalysisResult()

    check = timeseer.CheckResult(_CHECK_NAME, float(pct_anomaly))
    return timeseer.AnalysisResult(
        [check], frames, last_analyzed_point=last_analyzed_point
    )
