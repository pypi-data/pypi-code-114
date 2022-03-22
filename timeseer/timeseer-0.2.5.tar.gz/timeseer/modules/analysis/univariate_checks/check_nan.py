"""There should be no NaN values in the data.

<p>It is possible for values to be recorded in a non-numerical format due to preprocessing or network issues.
These values are indicated as NaN (Not-a-Number).
Non-numerical reading of a sensor or dividing by zero in preprocessing are typical examples of this issue.</p>
<p><img src='../static/images/reporting/nan.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where the corresponding value is not defined (i.e. NaN).
Imagine that 100 points are analyzed in a given time-frame
and there are 10 points whose value is NaN.
The score for this check in that case would be
90% = 1 - 10 / 100. Which means that 90% of all points have valid values.</p>
<div class="ts-check-impact">
<p>
NaNs can hamper (automated) downstream analytics.
</p>
</div>
"""

from datetime import timedelta

import pandas as pd

import timeseer

from timeseer.analysis.utils import event_frames_from_dataframe

_CHECK_NAME = "NaNs"

META: dict = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Completeness",
            "event_frames": ["NaN"],
        }
    ],
    "conditions": [{"min_series": 1, "min_data_points": 1}],
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


def _get_active_points(df: pd.DataFrame):
    return df["value"].isna()


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].sort_index()


def _run_nan_check(df: pd.DataFrame, median_archival_step):
    df = _clean_dataframe(df)

    active_points = _get_active_points(df)
    intervals = _get_intervals(active_points, df, "NaN")
    check_active_time = _calculate_total_check_active_time(
        intervals, median_archival_step
    )
    frames = event_frames_from_dataframe(intervals)

    total_time = df.index[-1] - df.index[0]
    percentage = check_active_time / total_time

    return percentage, list(frames)


def _is_valid_input(median_archival_step):
    if median_archival_step is None or len(median_archival_step) == 0:
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
    if not _is_valid_input(median_archival_step):
        return timeseer.AnalysisResult()

    pct_active, frames = _run_nan_check(analysis_input.data, median_archival_step[0])
    check = timeseer.CheckResult(_CHECK_NAME, float(pct_active))
    return timeseer.AnalysisResult([check], frames)
