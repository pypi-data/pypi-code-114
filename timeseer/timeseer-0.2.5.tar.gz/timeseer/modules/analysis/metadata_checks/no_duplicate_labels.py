"""Dictionary labels should not be repeated with different values.

<p>Dictionaries, or 'digital sets' label discrete numerical values with a
textual representation.
For example, a valve could be 'OPEN' or 'CLOSED'.
'OPEN' could be stored as 1 and 'CLOSED' as 2.<p>
<p class="scoring-explanation">The score for this check is a simple boolean (True / False).</p>
<div class="ts-check-impact">
<p>Multiple numerical values should not be labeled the same.
This confuses analytics tooling that operates on numerical values, but allows
selection based on labels.</p>
</div>
"""

from collections import Counter

import timeseer

from timeseer import DataType
from timeseer.metadata import fields

_CHECK_NAME = "Labels are not duplicated"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Data types",
            "data_type": "bool",
        }
    ],
    "conditions": [{"min_series": 1, "data_type": [DataType.DICTIONARY]}],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    dictionary = analysis_input.metadata.get_field(fields.Dictionary)
    if dictionary is None:
        return timeseer.AnalysisResult()

    counter = Counter(v for v in dictionary.mapping.values())
    has_duplicates = any(count > 1 for count in counter.values())

    return timeseer.AnalysisResult(
        check_results=[
            timeseer.CheckResult(_CHECK_NAME, float(has_duplicates)),
        ],
    )
