from abc import ABC

from arrow_bpmn.__spi__.bpmn_node import BpmnNode


class BpmnEngineListener(ABC):

    def before_node_execution(self, node: BpmnNode):
        pass

    def after_node_execution(self, node: BpmnNode):
        pass
