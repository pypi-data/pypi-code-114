"""Time series data should have strict increasing timestamps.

<p>Out of order time stamps can occur because of connection issues, causing the system
to rely on buffered data. Another common cause for out of order samples isthe daylight saving time
not handled correctly in the source.</p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>
Misaligned ordering of timestamps can hamper (automated) downstream analytics.
</p>
</div>
"""

from datetime import timedelta

import timeseer

_CHECK_NAME = "No out-of-order samples"

META = {
    "checks": [{"name": _CHECK_NAME, "kpi": "Integrity", "data_type": "bool"}],
    "conditions": [{"min_series": 1, "min_data_points": 2}],
    "signature": "univariate",
}


def _any_out_of_order_samples(df):
    return any(df.index.to_series().diff() < timedelta(0))


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    out_of_order = _any_out_of_order_samples(analysis_input.data)
    check = timeseer.CheckResult(_CHECK_NAME, float(out_of_order))
    return timeseer.AnalysisResult([check])
