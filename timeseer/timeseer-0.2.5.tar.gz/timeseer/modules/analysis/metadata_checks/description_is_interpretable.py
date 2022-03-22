"""The description should not be one character or all the same characters.

<p class="scoring-explanation">The score for this check is a simple boolean (True / False).
This check belongs to the score group Description.
If this check is True, it means that the score for group Description will be 0%.</p>
<div class="ts-check-impact">
<p>An interpretable description of series aids in onboarding and analysis by 3rd
parties that are less familiar with the process.
Due to time constraints sometimes the non-descriptive name of the series is copied for the description.
A good description provides information on the type as well as location of the sensor.
</p>
</div>
"""

import timeseer

from timeseer.metadata import fields

_CHECK_NAME = "Description is interpretable"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "kpi": "Metadata",
            "group": "Description",
            "data_type": "bool",
        }
    ],
    "conditions": [
        {
            "min_series": 1,
        }
    ],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: timeseer.AnalysisInput,
) -> timeseer.AnalysisResult:
    description = analysis_input.metadata.get_field(fields.Description)
    if description == "":
        return timeseer.AnalysisResult()
    different_character_count = len(set(description))
    if len(description) != 1 and different_character_count != 1:
        score = 0.0
    else:
        score = 1.0
    return timeseer.AnalysisResult(
        check_results=[timeseer.CheckResult(_CHECK_NAME, score)]
    )
