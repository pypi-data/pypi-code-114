"""Counters should increase in value (until reset).

<p>
This check identifies when a counter goes down for a period.
</p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
time where there is a downward trend.
</p>
<div class="ts-check-impact">
<p>
Could impact downstream dashboards, reports or automated analytics.
</p>
</div>
"""
from typing import List

import pandas as pd

import timeseer

from timeseer import DataType
from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    merge_intervals_and_open_event_frames,
    calculate_local_score,
    process_open_intervals,
)

_CHECK_NAME = "Counter increase"
_EVENT_FRAME_NAME = "Counter decrease"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Validity",
            "event_frames": [_EVENT_FRAME_NAME],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_data_points": 1,
            "data_type": [
                DataType.FLOAT64,
                DataType.FLOAT32,
            ],
        }
    ],
    "signature": "univariate",
}


def _get_intervals(outliers, df, event_type):
    outliers = pd.Series(data=outliers, index=df.index).fillna(False)
    outlier_grp = (outliers != outliers.shift().bfill()).cumsum()
    outlier_intervals = (
        df.assign(outlier_grp=outlier_grp)[outliers]
        .reset_index()
        .groupby(["outlier_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    outlier_intervals["type"] = event_type
    return outlier_intervals


def _get_active_points(df: pd.DataFrame):
    return df["value"].diff() < 0


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _handle_open_intervals(df, intervals):
    intervals["open"] = intervals["end_date"] == df.index[-1]
    return intervals


def _run_increase_check(analysis_input, median_archival_step, open_event_frames):
    df = analysis_input.data
    df = _clean_dataframe(df)

    analysis_start = df.index[0]
    if analysis_input.analysis_start is not None:
        analysis_start = analysis_input.analysis_start

    active_points = _get_active_points(df)
    intervals = _get_intervals(active_points, df, _EVENT_FRAME_NAME)
    intervals = _handle_open_intervals(df, intervals)

    intervals = merge_intervals_and_open_event_frames(
        analysis_start, intervals, open_event_frames
    )

    percentage = calculate_local_score(
        df, analysis_start, intervals, median_archival_step
    )
    frames = event_frames_from_dataframe(process_open_intervals(intervals))

    last_analyzed_point = df.index[-1]

    return percentage, list(frames), last_analyzed_point


def _is_valid_input(
    analysis_input: timeseer.AnalysisInput, median_archival_step: List[float]
):
    if median_archival_step is None or len(median_archival_step) == 0:
        return False
    if len(_clean_dataframe(analysis_input.data)) == 0:
        return False
    return True


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


# pylint: disable=missing-function-docstring
def run(analysis_input: timeseer.AnalysisInput) -> timeseer.AnalysisResult:
    median_archival_step = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == "Archival time median"
    ]
    if not _is_valid_input(analysis_input, median_archival_step):
        return timeseer.AnalysisResult()

    open_event_frames = _get_open_event_frames(analysis_input)

    pct_active, frames, last_analyzed_point = _run_increase_check(
        analysis_input, median_archival_step[0], open_event_frames
    )
    check = timeseer.CheckResult(_CHECK_NAME, float(pct_active))
    return timeseer.AnalysisResult(
        [check], frames, last_analyzed_point=last_analyzed_point
    )
