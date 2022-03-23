from arrow_bpmn.__spi__ import BpmnNode
from arrow_bpmn.engine.listener.abstract_bpmn_engine_listener import BpmnEngineListener


class CycleDetectionListener(BpmnEngineListener):

    def before_node_execution(self, node: BpmnNode):
        super().before_node_execution(node)

    def after_node_execution(self, node: BpmnNode):
        super().after_node_execution(node)