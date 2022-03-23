import dataclasses
import json
import os
from dataclasses import dataclass
from enum import Enum
from typing import Union, Tuple, TypeVar, Dict, Mapping, Iterable

from phonologic._error_analysis._levenshtein import ActionStep, Action


@dataclass(frozen=True)
class ErrorAnalysis:
    distance: int
    error_rate: float
    expected_length: int
    steps: Tuple[ActionStep, ...]


@dataclass(frozen=True)
class PhonologicalActionStep(ActionStep):
    action: Action
    expected: str
    actual: str
    cost: float
    deltas: Iterable["FeatureDelta"]


@dataclass(frozen=True)
class FeatureErrorAnalysis(ErrorAnalysis):
    distance: float
    error_rate: float
    expected_length: int
    steps: Tuple[PhonologicalActionStep, ...]


TAnalysis = TypeVar("TAnalysis", bound=ErrorAnalysis)


class ErrorAnalysisDict(Dict[str, Union[TAnalysis]]):
    def save(self, filename):
        def json_handler(o):
            if isinstance(o, Enum):
                return o.name
            if isinstance(o, Mapping):
                return {key: o[key] for key in o}
            if dataclasses.is_dataclass(o):
                return dataclasses.asdict(o)
            raise NotImplementedError(type(o))

        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            json.dump(self, f, indent=4, default=json_handler)
