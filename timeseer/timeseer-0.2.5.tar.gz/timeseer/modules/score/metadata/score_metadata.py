"""Timeseer score module to generate scores for metadata checks.

Scores for metadata checks are calculated based on their metadata group.
If one score indicates a failure, the total score will be a failure.
"""

from collections import defaultdict
from typing import List

from timeseer import CheckResult, ScoreInput, ScoreOutput, ScoreResult

META = {
    "scores": [
        dict(
            name="description",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="description"),
            ],
        ),
        dict(
            name="interpolation type",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="interpolation type"),
            ],
        ),
        dict(
            name="limits",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="limits"),
            ],
        ),
        dict(
            name="unit",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="unit"),
            ],
        ),
        dict(
            name="data types",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="data types"),
            ],
        ),
        dict(
            name="accuracy",
            kpi="Metadata",
            data_type="bool",
            checks=[
                dict(group="accuracy"),
            ],
        ),
    ],
}


def _calculate_score(results: List[CheckResult]) -> float:
    return max([result.result for result in results])


# pylint: disable=missing-function-docstring
def score(
    score_input: ScoreInput,
) -> ScoreOutput:
    metadata_lookup = {meta.name: meta for meta in score_input.check_metadata}

    by_group = defaultdict(list)
    for result in score_input.check_results:
        metadata = metadata_lookup[result.name]
        if metadata.group is None:
            continue
        by_group[metadata.group].append(result)
    scores = []
    for group_name, group_results in by_group.items():
        scores.append(ScoreResult(group_name, _calculate_score(group_results)))
    return ScoreOutput(scores)
