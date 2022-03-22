"""Upper limit set by the metadata should not be exceeded, taking into account the uncertainty
as defined by the accuracy in the metadata.

<p>Every measurement has an inherent uncertainty given by precision of the measuring
instrument as well as potential compression settings in the historian. So every value
should be interpreted with uncertainty bounds. This check identifies whether the upper limit,
if defined, is crossed taking these uncertainty bounds into account.</p>
<p><img src='../static/images/reporting/limits_accuracy.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where the corresponding value is above the given limit, taking into account the accuracy.
Imagine that 100 points are analyzed in a given time-frame
and there are 10 points whose value - accuracy is above the given limit.
The score for this check in that case would be
90% = 1 - 10 / 100. Which means that 90% of all points lie inside the limit even taken accuracy
into account.</p>
<div class="ts-check-impact">
<p>
When the sensor spec limits are exceeded this is an indication of sensor failure. This might mean the
sensor needs to be recalibrated.
</p>
</div>
"""

from datetime import timedelta
from typing import List

import pandas as pd

import timeseer

from timeseer import DataType
from timeseer.analysis.utils import event_frames_from_dataframe
from timeseer.metadata import fields

_CHECK_NAME = "Out-of-bounds (upper, accuracy)"
_EVENT_FRAME_NAME = "Out of bounds (upper, accuracy)"

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


def _get_active_points(df: pd.DataFrame, metadata: timeseer.Metadata):
    limit_high = metadata.get_field(fields.LimitHighFunctional)
    accuracy = metadata.get_field(fields.Accuracy)
    assert limit_high is not None
    assert accuracy is not None
    return df["value"] > limit_high - accuracy


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].dropna().sort_index()


def _run_limit_accuracy_check(
    metadata: timeseer.Metadata, df: pd.DataFrame, median_archival_step
):
    df = _clean_dataframe(df)

    active_points = _get_active_points(df, metadata)
    intervals = _get_intervals(active_points, df, _EVENT_FRAME_NAME)
    check_active_time = _calculate_total_check_active_time(
        intervals, median_archival_step
    )
    frames = event_frames_from_dataframe(intervals)

    total_time = df.index[-1] - df.index[0]
    percentage = check_active_time / total_time

    return percentage, list(frames)


def _is_input_valid(
    analysis_input: timeseer.AnalysisInput, median_archival_step: List[float]
):
    if analysis_input.metadata.get_field(fields.Accuracy) is None:
        return False
    if analysis_input.metadata.get_field(fields.LimitHighFunctional) is None:
        return False
    if median_archival_step is None or len(median_archival_step) == 0:
        return False
    if len(_clean_dataframe(analysis_input.data)) == 0:
        return False
    return True


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    median_archival_step = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == "Archival time median"
    ]
    if not _is_input_valid(analysis_input, median_archival_step):
        return timeseer.AnalysisResult()

    pct_active, frames = _run_limit_accuracy_check(
        analysis_input.metadata, analysis_input.data, median_archival_step[0]
    )
    check = timeseer.CheckResult(_CHECK_NAME, float(pct_active))
    return timeseer.AnalysisResult([check], frames)
