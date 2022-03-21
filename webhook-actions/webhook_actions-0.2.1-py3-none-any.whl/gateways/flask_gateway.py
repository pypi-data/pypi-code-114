from __future__ import annotations

from flask import Flask, abort, request
from flask_classful import FlaskView, route
from webhook_actions.app.run.run import RunOutput

from ..app.app import App
from ..config import config
from ..core.entities.action import Action


class FlaskGateway(FlaskView):
    _app: App

    def __init__(self) -> None:
        super().__init__()
        self.web = _web

    def listen(self) -> None:
        self.web.run(port=config.port)

    @route("/<path:script>", methods=["POST"])
    def run(self, script):
        data = str(request.data, "utf-8")
        action = Action(script, data)
        output = self.app.run(action)

        if output == RunOutput.not_found:
            abort(404)
        elif output == RunOutput.fail:
            abort(500)

        return ""

    @property
    def app(self) -> App:
        return FlaskGateway._app

    @app.setter
    def app(self, app: App):
        FlaskGateway._app = app


_web = Flask(__package__)
FlaskGateway.register(_web, route_base="/")
