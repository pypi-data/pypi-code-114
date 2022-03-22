"""For percentage accuracy the value should be between 0 and 100.

<p>This check validates whether the accuracy percentage falls
within the expected range between 0 and 100.</p>
<p class="scoring-explanation">The score for this checks is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>Badly configured accuracy percentage can cause a wrong accuracy calculation.
</p>
</div>
"""

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Accuracy percentage is within range"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Accuracy",
            "data_type": "bool",
        }
    ],
    "conditions": [
        {"min_series": 1, "data_type": [DataType.FLOAT32, DataType.FLOAT64]}
    ],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    accuracy_percentage = analysis_input.metadata.get_field(fields.AccuracyPercentage)
    if accuracy_percentage is None:
        return timeseer.AnalysisResult()
    if accuracy_percentage < 0 or accuracy_percentage > 100:
        score = 1.0
    else:
        score = 0.0
    return timeseer.AnalysisResult(
        check_results=[timeseer.CheckResult(_CHECK_NAME, score)]
    )
