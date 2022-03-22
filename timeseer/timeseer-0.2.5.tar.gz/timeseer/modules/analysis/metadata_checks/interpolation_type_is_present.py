"""Time series should indicate their interpolation type.

<p>
It is often required to know the value of a time series between recorded data
points.
</p>
<p>
Two types of interpolation are commonly used:
</p>
<dl>
    <dt>LINEAR interpolation</dt>
    <dd>The value is interpolated linearly between the previously recorded and the next value.</dd>

    <dt>STEPPED interpolation</dt>
    <dd>The value is assumed to be equal to the previously recorded value.</dd>
</dl>
<p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>
Without a well-defined interpolation type, linear interpolation can happen when
stepped interpolation was required, for example for setpoints. Furthermore correlation analysis
between two series will be skewed when (at least one of) the series are not interpolated correct.
</p>
</div>
"""

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Interpolation type is present"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Interpolation type",
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
    interpolation_type = analysis_input.metadata.get_field(fields.InterpolationType)

    has_interpolation_type = interpolation_type is not None

    return timeseer.AnalysisResult(
        check_results=[
            timeseer.CheckResult(_CHECK_NAME, float(not has_interpolation_type)),
        ],
    )
