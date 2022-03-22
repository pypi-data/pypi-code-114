"""Identification of outlier based on inter-quartile range (IQR).

<p>This check is a traditional method for outliers where values are flagged
as anomalies if they are outside of a range defined by [q1 - 1.5 * iqr, q3 + 1.5 * iqr].
Here q1, q3 and iqr stand for 25th, 75th percentile and inter-quartile range (=q3-q1) respectively.</p>
<p><img src='../static/images/reporting/iqr.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where an IQR outlier occurs. Imagine that 100 points are analyzed in a given time-frame
and there are 7 outliers. The score for this check in that case would be
93% = 1 - 7 / 100. Which means that 93% of all points are not outliers.</p>
<div class="ts-check-impact">
<p>
Outliers in series can cloud downstream analytics and put the burden of removing these without
background knowledge on the algorithms instead of those in the know.
Several calculations are sensitive to these type of sudden changes and process decision chains
based on such an outlier can propagate through the system.
Any type of anomaly detection based on normal behavior of the phyiscal sensor can act as a guide for
prioritization of callibration / maintenance.
</p>
</div>
"""

from datetime import timedelta
from typing import List

import jsonpickle
import pandas as pd

import timeseer

from timeseer import DataType
from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    merge_intervals_and_open_event_frames,
    process_open_intervals,
    calculate_local_score,
)

_CHECK_NAME = "IQR Anomaly"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Validity",
            "event_frames": ["IQR Anomaly"],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_weeks": 1,
            "min_data_points": 300,
            "data_type": [DataType.FLOAT32, DataType.FLOAT64],
        }
    ],
    "signature": "univariate",
}


def _calculate_total_check_active_time(frames, median_archival_step):
    active_time = timedelta(0)
    for _, row in frames.iterrows():
        length = row["end_date"] - row["start_date"]
        if length == timedelta(0):
            length = timedelta(seconds=median_archival_step)
        active_time = active_time + length
    return active_time


def _handle_open_intervals(df, intervals):
    intervals["open"] = intervals["end_date"] == df.index[-1]
    return intervals


def _get_intervals(anomalies, df, event_type):
    interval_grp = (anomalies != anomalies.shift().bfill()).cumsum()
    intervals = (
        df.assign(interval_grp=interval_grp)[anomalies]
        .reset_index()
        .groupby(["interval_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    intervals["type"] = event_type
    return intervals


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _run_iqr_ad(
    analysis_input, median_archival_step, open_event_frames, sketch, strictness=3
):
    df = _clean_dataframe(analysis_input.data)

    analysis_start = df.index[0]
    if analysis_input.analysis_start is not None:
        analysis_start = analysis_input.analysis_start

    q25, q75 = [sketch.get_quantile_value(q) for q in [0.25, 0.75]]
    iqr = q75 - q25
    active_points = (df["value"] < (q25 - (strictness * iqr))) | (
        df["value"] > (q75 + (strictness * iqr))
    )

    intervals = _get_intervals(active_points, df, _CHECK_NAME)
    intervals = _handle_open_intervals(df, intervals)
    intervals = merge_intervals_and_open_event_frames(
        analysis_start, intervals, open_event_frames
    )

    percentage = calculate_local_score(
        df, analysis_start, intervals, median_archival_step
    )

    all_frames = event_frames_from_dataframe(process_open_intervals(intervals))

    last_analyzed_point = df.index[-1]

    return percentage, list(all_frames), last_analyzed_point


def _get_relevant_statistic(analysis_input, stat_name):
    statistics = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == stat_name
    ]
    if statistics is None or len(statistics) == 0:
        return None
    return statistics[0]


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


def _is_valid_input(analysis_input):
    return len(_clean_dataframe(analysis_input.data)) > 0


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    if not _is_valid_input(analysis_input):
        return timeseer.AnalysisResult()

    median_archival_step = _get_relevant_statistic(
        analysis_input, "Archival time median"
    )
    json_sketch = _get_relevant_statistic(analysis_input, "Value Sketch")
    if median_archival_step is None or json_sketch is None:
        return timeseer.AnalysisResult()
    sketch = jsonpickle.decode(json_sketch)

    open_event_frames = _get_open_event_frames(analysis_input)

    pct_outlier, frames, last_analyzed_point = _run_iqr_ad(
        analysis_input, median_archival_step, open_event_frames, sketch
    )

    check = timeseer.CheckResult(_CHECK_NAME, float(pct_outlier))
    return timeseer.AnalysisResult(
        [check], frames, last_analyzed_point=last_analyzed_point
    )
