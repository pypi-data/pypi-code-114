"""Identification of sensor difference outliers between 2 series.

<p>This check identifies periods where for redundant sensors the typical
difference is significantly altered compared to normal.</p>
<p><img src='../static/images/reporting/sensor_outlier.svg'></p>
<p class="scoring-explanation">The score of this check is calculated based on the count of all
points where sensor drift is identified. Imagine that 100 points are analyzed in a given time-frame
and that drift is detected for 10 (consecutive) points. The score for this check in that case would be
90% = 1 - 10 / 100. Which means that for 90% of all points no drift occurs.</p>
<div class="ts-check-impact">
<p>Changes in a physical relation between a set of series could indicate process or instrumentation issues.</p>
</div>
"""

from datetime import timedelta

import pandas as pd
import numpy as np

import timeseer

from timeseer import DataType
from timeseer.analysis.utils import event_frames_from_dataframe


_CHECK_NAME = "Redundant sensor outlier"
_EVENT_FRAME_NAME = "Sensor outlier"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Accuracy",
            "event_frames": [_EVENT_FRAME_NAME],
        },
    ],
    "conditions": [
        {
            "min_series": 2,
            "max_series": 2,
        },
        {
            "min_weeks": 1,
            "min_data_points": 300,
            "data_type": [DataType.FLOAT32, DataType.FLOAT64],
        },
    ],
    "signature": "multivariate",
}


def _calculate_total_check_active_time(frames, median_archival_step):
    active_time = timedelta(0)
    for _, row in frames.iterrows():
        length = row["end_date"] - row["start_date"]
        if length == timedelta(0):
            length = timedelta(seconds=median_archival_step)
        active_time = active_time + length
    return active_time


def _is_frame_long_enough(frame):
    return (frame.end_date - frame.start_date) >= timedelta(hours=12)


def _filter_stale_event_frames(all_frames):
    filter_iterator = filter(_is_frame_long_enough, all_frames)
    return filter_iterator


def _get_anomalies(lower, upper, arr):
    a_lower = arr < lower
    a_upper = arr > upper
    return a_lower | a_upper


def _find_anomalous_times(diff_matrix):
    q25, q75 = np.nanquantile(np.array(diff_matrix, dtype=float), [0.25, 0.75], axis=0)
    iqr = q75 - q25
    upper = q75 + 1.5 * iqr
    lower = q25 - 1.5 * iqr
    return [_get_anomalies(lower, upper, x) for x in np.array(diff_matrix, dtype=float)]


def _make_diff_matrix(df):
    diff_matrix = np.zeros((df.shape[0], df.shape[1], df.shape[1]))
    for i in range(df.shape[1] - 1):
        for j in range(i + 1, df.shape[1]):
            diff_matrix[:, i, j] = df.iloc[:, i] - df.iloc[:, j]
    return diff_matrix


def _anomalous_times_per_series(anomalous_times_matrix, series):
    results = []
    for i in range(len(series) - 1):
        for j in range(i + 1, len(series)):
            results.append(
                {
                    "series_x": series[i],
                    "series_y": series[j],
                    "drifts": [time[i, j] for time in anomalous_times_matrix],
                }
            )
    return results


def _get_intervals(anomalies, df):
    anomalies = pd.Series(data=anomalies, index=df.index)
    interval_grp = (anomalies != anomalies.shift().bfill()).cumsum()

    intervals = (
        df.assign(interval_grp=interval_grp)[anomalies]
        .reset_index()
        .groupby(["interval_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    intervals["type"] = _EVENT_FRAME_NAME
    return intervals


def _get_results_per_series(
    series_anomaly, df, median_archival_step
) -> timeseer.BivariateCheckResult:
    anomalies = series_anomaly["drifts"]
    intervals = _get_intervals(anomalies, df)

    check_active_time = _calculate_total_check_active_time(
        intervals, median_archival_step
    )
    frames = event_frames_from_dataframe(intervals)

    total_time = df.index[-1] - df.index[0]
    percentage = check_active_time / total_time

    return timeseer.BivariateCheckResult(
        _CHECK_NAME,
        series_anomaly["series_x"],
        series_anomaly["series_y"],
        percentage,
        _filter_stale_event_frames(frames),
    )


def _clean_input(inputs):
    concatenated_df = (
        pd.concat(
            [
                series.data["value"][
                    ~series.data["value"].index.duplicated(keep="first")
                ]
                for series in inputs
            ],
            axis=1,
            sort=False,
        )
        .interpolate("linear")
        .dropna()
    )
    concatenated_df = concatenated_df[(concatenated_df != 0).all(1)]
    return concatenated_df


def _get_mv_median_archival_step(df):
    meas_times = df.index.to_series()
    diff_times = meas_times - meas_times.shift()
    diff_times.dropna()
    return pd.Timedelta(np.median(diff_times)).total_seconds()


def _run_detect_redundant_sensor_outlier(inputs):
    concatenated_df = _clean_input(inputs)
    median_archival_step = _get_mv_median_archival_step(concatenated_df)

    diff_matrix = _make_diff_matrix(concatenated_df)
    anomalous_times_matrix = _find_anomalous_times(diff_matrix)

    series = [series.metadata.series for series in inputs]
    anomalous_times_per_series = _anomalous_times_per_series(
        anomalous_times_matrix, series
    )

    return [
        _get_results_per_series(series_anomaly, concatenated_df, median_archival_step)
        for series_anomaly in anomalous_times_per_series
    ]


def run(
    analysis_input: timeseer.MultivariateAnalysisInput,
):  # pylint: disable=missing-function-docstring
    inputs = analysis_input.inputs

    results = _run_detect_redundant_sensor_outlier(inputs)

    return timeseer.AnalysisResult(bivariate_check_results=results)
