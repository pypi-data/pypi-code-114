from typing import Tuple

import requests

from arrow_bpmn.__spi__ import BpmnNode
from arrow_bpmn.__spi__ import CompleteAction
from arrow_bpmn.__spi__.action import ContinueAction, Actions
from arrow_bpmn.__spi__.execution import Environment
from arrow_bpmn.__spi__.execution import State


class HttpTask(BpmnNode):
    """
    A Http Task is a bpmn task extension used to send a http request.
    """

    def __init__(self, element: dict):
        super().__init__(element)

    @property
    def url(self) -> str:
        return self["url"]

    @property
    def method(self) -> str:
        return self["method"] or "get"

    @property
    def headers(self) -> dict:
        return self["headers"] or {}

    @property
    def var_name(self) -> str:
        return self["varName"] or "result"

    @property
    def request_expression(self) -> str:
        return self["requestExpression"]

    @property
    def request_expression_format(self) -> str:
        return self["requestExpressionFormat"] or "typescript"

    @property
    def response_expression(self) -> str:
        return self["responseExpression"]

    @property
    def response_expression_format(self) -> str:
        return self["responseExpressionFormat"] or "typescript"

    def execute(self, state: State, environment: Environment) -> Tuple[State, Actions]:

        def prepare_data() -> dict:
            """
            Prepares the http request body by invoking the request expression if present.
            :return: dict
            """
            if self.request_expression is None:
                return {}

            engine = environment.script_factory(self.request_expression_format, self.request_expression)
            return engine.invoke(state.properties)

        def extract_data(response):
            """
            Extracts the data from the response object by invoking the response expression if present.
            :param response: the response object
            :return: any
            """
            accept = self.headers["ACCEPT"] if "ACCEPT" in self.headers else "plain/text"

            if response.status_code != 200:
                raise ValueError(response.text)

            if self.response_expression is None:
                return response.text if accept == "plain/text" else response.json()

            engine = environment.script_factory(self.response_expression_format, self.response_expression)

            if accept == "application/json":
                return engine.invoke({"data": response.json})
            return engine.invoke({"data": response.text})

        def send_http_request():
            if self.method == "get":
                return requests.get(self.url, headers=self.headers)
            if self.method == "post":
                return requests.post(self.url, data=prepare_data(), headers=self.headers)
            if self.method == "put":
                return requests.put(self.url, data=prepare_data(), headers=self.headers)
            if self.method == "delete":
                return requests.delete(self.url, data=prepare_data(), headers=self.headers)
            if self.method == "head":
                return requests.head(self.url, headers=self.headers)
            if self.method == "options":
                return requests.options(self.url, headers=self.headers)

        state[self.var_name] = extract_data(send_http_request())

        actions = [ContinueAction(node) for node in environment.get_outgoing_nodes(self.id)]
        return state, [CompleteAction(self.id)] + actions

    def __repr__(self):
        return f"ReceiveTask({self.id})"
