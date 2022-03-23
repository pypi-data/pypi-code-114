from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from arrow_bpmn.__spi__.types import BpmnSource
from arrow_bpmn.model.process import Process
from arrow_bpmn.parser.abstract_parser_extension import ParserExtension, ArrowParserExtension


@dataclass
class BpmnParser(ABC):
    extension: ParserExtension = field(default_factory=lambda: ArrowParserExtension())

    @abstractmethod
    def parse(self, source: BpmnSource) -> List[Process]:
        pass

    def _concat_dicts(self, dict1: dict, dict2: dict):
        dict3 = {}
        dict3.update(dict1)
        dict3.update(dict2)
        return dict3
