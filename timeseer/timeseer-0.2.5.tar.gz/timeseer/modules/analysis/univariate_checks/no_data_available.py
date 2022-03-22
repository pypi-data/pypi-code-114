"""The data in a time series should be present within the analysis timeframe.

<p>
The data in a time series should be present within the analysis timeframe.
</p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>
No input - No output.
</p>
</div>
"""

import timeseer

_CHECK_NAME = "Data available"

META = {
    "checks": [{"name": _CHECK_NAME, "kpi": "Completeness", "data_type": "bool"}],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    no_data = len(analysis_input.data) == 0
    check = timeseer.CheckResult(_CHECK_NAME, float(no_data))
    return timeseer.AnalysisResult([check])
