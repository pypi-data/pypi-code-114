"""Min, mean and max time between archival.

<p>In historians points are often stored not at fixed time intervals,
but based on approximations. This means that the rate at which points are stored
(archived) is not fixed.
These statistics also provide initial insights in certain data captation issues.
For example a 0 or negative minimal archival points to timestamp duplicates or out of order samples.</p>"""

import pandas as pd
import numpy as np

import timeseer


META: dict = {
    "statistics": [
        {"name": "Archival time mean"},
        {"name": "Archival time min"},
        {"name": "Archival time max"},
        {"name": "Archival time median"},
    ],
    "run": "before",
    "conditions": [{"min_series": 1, "min_weeks": 1, "min_data_points": 300}],
    "signature": "univariate",
}


def _run_ts_archival_timing(df: pd.DataFrame):
    meas_times = df.index.to_series()
    diff_times = meas_times - meas_times.shift()
    diff_times.dropna()
    return (
        np.min(diff_times).total_seconds(),
        np.mean(diff_times).total_seconds(),
        np.max(diff_times).total_seconds(),
        pd.Timedelta(np.median(diff_times)).total_seconds(),
    )


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:

    (
        archival_min,
        archival_mean,
        archival_max,
        archival_median,
    ) = _run_ts_archival_timing(analysis_input.data)
    check_mean = timeseer.Statistic(
        META["statistics"][0]["name"], "hidden", float(archival_mean)
    )
    check_min = timeseer.Statistic(
        META["statistics"][1]["name"], "hidden", float(archival_min)
    )
    check_max = timeseer.Statistic(
        META["statistics"][2]["name"], "hidden", float(archival_max)
    )
    check_median = timeseer.Statistic(
        META["statistics"][3]["name"], "hidden", float(archival_median)
    )

    values = [
        ("Min", float(archival_min)),
        ("Max", float(archival_max)),
        ("Mean", float(archival_mean)),
        ("Median", float(archival_median)),
    ]
    table_statistics = timeseer.Statistic("Archival statistics", "table", values)
    return timeseer.AnalysisResult(
        statistics=[check_min, check_mean, check_max, check_median, table_statistics]
    )
