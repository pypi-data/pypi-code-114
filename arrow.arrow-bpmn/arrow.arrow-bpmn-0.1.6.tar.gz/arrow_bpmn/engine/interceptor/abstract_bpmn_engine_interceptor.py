from abc import ABC

from arrow_bpmn.__spi__.bpmn_node import BpmnNode


class BpmnEngineInterceptor(ABC):

    def __call__(self, node: BpmnNode) -> BpmnNode:
        pass
