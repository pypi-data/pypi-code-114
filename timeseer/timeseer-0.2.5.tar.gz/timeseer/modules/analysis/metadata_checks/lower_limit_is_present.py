"""The series should have lower operating limits.

<p>Each sensor or lab measuring equipment has an inherent measurement range. Outside of this range
the readings from the sensor are unreliable. This information is typically present in the
sensor specification sheet.
Traditional historians also allow setting limits (often Low-Low, Low, High and High-High limits).
These limits are often based on process safety concerns or indeed taken from the normal operating range.
In all cases having access to these limits is essential for interpreting readings from the equipment.</p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).
This check belongs to the score group Limits.
If this check is True, it means that the score for group Limits will be 0%.
</p>
<div class="ts-check-impact">
<p>Missing or badly configured limits can cause missing warning signs of abnormal situations both
in the process as well as with the instrumentation.
</p>
</div>
"""

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Lower limit is present"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Limits",
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
    if analysis_input.metadata.get_field(fields.LimitLowPhysical) is None:
        score = 1.0
    else:
        score = 0.0
    return timeseer.AnalysisResult(
        check_results=[timeseer.CheckResult(_CHECK_NAME, score)]
    )
