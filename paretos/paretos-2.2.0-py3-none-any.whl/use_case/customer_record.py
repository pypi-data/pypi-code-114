from dataclasses import dataclass, field
from typing import List

from paretos.use_case.use_case import UseCase


@dataclass(frozen=True)
class CustomerRecord:
    customer_id: str
    company: str
    use_cases: List[UseCase] = field(default_factory=list)

    def show(self):
        print(self.__str__())
