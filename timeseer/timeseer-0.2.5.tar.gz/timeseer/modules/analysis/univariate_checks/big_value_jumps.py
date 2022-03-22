"""Identification of big jumps in consecutive values.

<p>This check identifies how many times over the time-frame of the analysis a sudden spike occurs.
A sudden spike is defined as an outlier wrt historical differences in consecutive values.</p>
<p><img src='../static/images/reporting/big_jumps.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where a positive or negative jump occurs. Imagine that 100 points are analyzed in a given time-frame
and there are 2 positive and 1 negative jumps. The score for this check in that case would be
97% = 1 - 3 / 100. Which means that for 90% of all points no jump is present.</p>
<div class="ts-check-impact">
<p>
Big sudden jumps in data often correspond to faults in the data captation chain.
Several calculations are sensitive to these type of sudden changes and process decision chains
based on such an outlier can propagate through the system.
Any type of anomaly detection based on normal behavior of the phyiscal sensor can act as a guide for
prioritization of callibration / maintenance.
</p>
</div>
"""

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


_CHECK_NAME = "Jumps"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Validity",
            "event_frames": ["Jump outlier"],
        },
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


def _get_quantiles(sketch):
    q25, q75 = [sketch.get_quantile_value(q) for q in [0.25, 0.75]]
    iqr = q75 - q25
    return q25, q75, iqr


def _get_relevant_jumps(values, jump_up_sketch, jump_down_sketch, strictness):
    ups = values[values > 0]
    down = values[values < 0]

    down_jumps = [False] * len(values)
    up_jumps = [False] * len(values)

    if len(ups) >= 30:
        _, up_q3, up_iqr = _get_quantiles(jump_up_sketch)
        up_jumps = values > (up_q3 + strictness * up_iqr)

    if len(down) >= 30:
        down_q1, _, down_iqr = _get_quantiles(jump_down_sketch)
        down_jumps = values < (down_q1 - strictness * down_iqr)

    if len(ups) < 30 and len(down) < 30:
        return None

    return up_jumps | down_jumps


def _handle_open_intervals(df, intervals):
    intervals["open"] = intervals["end_date"] == df.index[-1]
    return intervals


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


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _run_jump_check(
    analysis_input,
    median_archival_step,
    jump_up_sketch,
    jump_down_sketch,
    open_event_frames,
    strictness=3,
):  # pylint: disable=too-many-arguments
    df = _clean_dataframe(analysis_input.data)

    analysis_start = df.index[0]
    if analysis_input.analysis_start is not None:
        analysis_start = analysis_input.analysis_start

    value_diff = df["value"].diff()

    active_points = _get_relevant_jumps(
        value_diff, jump_up_sketch, jump_down_sketch, strictness
    )

    intervals = _get_intervals(active_points, df, "Jump outlier")
    intervals = _handle_open_intervals(df, intervals)
    intervals = merge_intervals_and_open_event_frames(
        analysis_start, intervals, open_event_frames
    )

    percentage = calculate_local_score(
        df, analysis_start, intervals, median_archival_step
    )

    frames = event_frames_from_dataframe(process_open_intervals(intervals))

    last_analyzed_point = df.index[-2]

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


def _get_relevant_statistic(analysis_input, stat_name):
    statistics = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == stat_name
    ]
    if statistics is None or len(statistics) == 0:
        return None
    return statistics[0]


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
    json_jump_up_sketch = _get_relevant_statistic(analysis_input, "Jump Up Sketch")
    json_jump_down_sketch = _get_relevant_statistic(analysis_input, "Jump Down Sketch")

    if (
        median_archival_step is None
        or json_jump_up_sketch is None
        or json_jump_down_sketch is None
    ):
        return timeseer.AnalysisResult()

    jump_up_sketch = jsonpickle.decode(json_jump_up_sketch)
    jump_down_sketch = jsonpickle.decode(json_jump_down_sketch)

    open_event_frames = _get_open_event_frames(analysis_input)

    pct_jumps, event_frames, last_analyzed_point = _run_jump_check(
        analysis_input,
        median_archival_step,
        jump_up_sketch,
        jump_down_sketch,
        open_event_frames,
    )

    if pct_jumps is None:
        return timeseer.AnalysisResult()

    check = timeseer.CheckResult(_CHECK_NAME, float(pct_jumps))
    return timeseer.AnalysisResult(
        check_results=[check],
        event_frames=event_frames,
        last_analyzed_point=last_analyzed_point,
    )
