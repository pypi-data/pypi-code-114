from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Parameter:
    id: str
    name: str
    type: str


@dataclass(frozen=True)
class UseCase:
    id: str
    name: str
    description: str
    input_parameters: List[Parameter] = field(default_factory=list)
    output_parameters: List[Parameter] = field(default_factory=list)

    def show(self):
        print(self.__str__())
