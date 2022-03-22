"""Time series of type DICTIONARY should reference an existing dictionary.

<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>
Values in a time series of type DICTIONARY map to textual labels.
This conveys meaning to analytics users.
A time series that is missing this dictionary will be confusing as the user
will be presented with numerical values only.
</p>
</div>
"""

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Dictionary is present"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Data types",
            "data_type": "bool",
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "data_type": [DataType.DICTIONARY],
        }
    ],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    dictionary = analysis_input.metadata.get_field(fields.Dictionary)
    has_dictionary = dictionary is not None and len(dictionary.mapping) > 0

    return timeseer.AnalysisResult(
        check_results=[
            timeseer.CheckResult(_CHECK_NAME, float(not has_dictionary)),
        ],
    )
