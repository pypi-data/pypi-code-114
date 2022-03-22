"""Last updated point should not be further than 1 month.

<p>This check finds the last time a value was archived. If no value has been recorded in the last
month, the tag might no longer be in use.</p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>
A series that no longer puts out any measurements might be faulty or could indicate a network failure.
Failing to detect this could lead to wrong process operation when attempting to obtain a particular
interval of operation.
</p>
</div>
"""

from datetime import date, timedelta

import pandas as pd

import timeseer

_CHECK_NAME = "Recently updated"

META: dict = {
    "checks": [{"name": _CHECK_NAME, "kpi": "Timeliness", "data_type": "bool"}],
    "conditions": [
        {
            "min_series": 1,
            "min_data_points": 1,
        }
    ],
    "signature": "univariate",
}


def _is_last_point_old(df: pd.DataFrame, strictness: int = 1) -> bool:
    last_recorded_time = df.index[-1]
    today = date.today()
    cutoff_date = today - timedelta(weeks=strictness * 4)
    return last_recorded_time.date() <= cutoff_date


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    if len(analysis_input.data) == 0:
        return timeseer.AnalysisResult()

    is_too_old = _is_last_point_old(analysis_input.data)
    check = timeseer.CheckResult(_CHECK_NAME, float(is_too_old))
    return timeseer.AnalysisResult([check])
