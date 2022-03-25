from abc import ABC, abstractmethod

from arrow_bpmn.parser.json.json_element import JSONElement
from arrow_bpmn.parser.xml.xml_element import XMLElement


class ParserExtension(ABC):

    @abstractmethod
    def parse_json(self, element: JSONElement) -> dict:
        pass

    @abstractmethod
    def parse_xml(self, element: XMLElement) -> dict:
        pass


class ArrowParserExtension(ParserExtension):

    def parse_json(self, element: JSONElement) -> dict:
        return {}

    def parse_xml(self, element: XMLElement) -> dict:
        if element.has_tag("bpmn:extensionElements"):
            extensions = element.get_tag("bpmn:extensionElements")
            expressions = {}
            if extensions.has_tag("arrow:initiateExpression"):
                expressions["initiateExpression"] = extensions.get_tag("arrow:initiateExpression").get_text(True)
            if extensions.has_tag("arrow:continueExpression"):
                expressions["continueExpression"] = extensions.get_tag("arrow:continueExpression").get_text(True)
            if extensions.has_tag("arrow:completeExpression"):
                expressions["completeExpression"] = extensions.get_tag("arrow:completeExpression").get_text(True)
            return expressions

        return {}
