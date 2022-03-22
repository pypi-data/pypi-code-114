"""Deadband should not be too big compared to range of tag.

<p>This check evaluates the ratio of the deadband as given in the metadata
to the total range as given in the metadata. Typical settings for this measurement are
in the range of [0.5-2]%</p>
<div class="ts-check-impact">
<p>A too high ratio, indicating a high deadband with regards to the typical values of the series
is an indication of compression issues. Badly compressed data, specifically overcompression,
can lead to critical events such as upsets, safety issues and downtime.</p>
</div>
"""

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Deadband to range ratio"

META = {
    "checks": [
        {
            "name": "Deadband to range ratio",
            "kpi": "Metadata",
            "group": "Compression",
        }
    ],
    "conditions": [
        {"min_series": 1, "data_type": [DataType.FLOAT32, DataType.FLOAT64]}
    ],
    "signature": "univariate",
}


def _get_deadband_to_range_ration(
    deadband: float, limit_low: float, limit_high: float
) -> float:
    return min([deadband / (limit_high - limit_low), 1])


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    metadata = analysis_input.metadata
    accuracy = metadata.get_field(fields.Accuracy)
    limit_low = metadata.get_field(fields.LimitLowFunctional)
    limit_high = metadata.get_field(fields.LimitHighFunctional)

    if accuracy is None:
        return timeseer.AnalysisResult()
    if accuracy < 0:
        return timeseer.AnalysisResult()
    if limit_low is None:
        return timeseer.AnalysisResult()
    if limit_high is None:
        return timeseer.AnalysisResult()
    if limit_high <= limit_low:
        return timeseer.AnalysisResult()

    ratio = _get_deadband_to_range_ration(accuracy, limit_low, limit_high)
    check = timeseer.CheckResult(_CHECK_NAME, float(ratio))
    return timeseer.AnalysisResult([check])
