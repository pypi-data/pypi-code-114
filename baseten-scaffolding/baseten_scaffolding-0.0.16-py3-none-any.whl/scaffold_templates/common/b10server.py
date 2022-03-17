from common.lib_support import ensure_kfserving_installed
ensure_kfserving_installed()

import json
from http import HTTPStatus
import logging

import numpy as np
import tornado.web
from kfserving.handlers.http import HTTPHandler
from kfserving.kfserver import HealthHandler, KFServer, ListHandler, LivenessHandler

from common.config import do_sentry_init
from common.serialization import (
    DeepNumpyEncoder, b10_msgpack_deserialize, b10_msgpack_serialize
)

from pythonjsonlogger import jsonlogger


def _assign_request_to_inputs_instances_after_validation(request):
    # we will treat "instances" and "inputs" the same
    if "instances" in request and "inputs" not in request:
        request["inputs"] = request["instances"]
    elif "inputs" in request and "instances" not in request:
        request["instances"] = request["inputs"]
    return request


class B10HTTPBinaryHandler(HTTPHandler):
    def validate(self, request):
        if ("instances" in request and not isinstance(request["instances"], (list, np.ndarray))) or \
           ("inputs" in request and not isinstance(request["inputs"], (list, np.ndarray))):
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Expected \"instances\" or \"inputs\" to be a list or NumPy ndarray"
            )
        return _assign_request_to_inputs_instances_after_validation(request)


class B10HTTPHandler(HTTPHandler):
    def validate(self, request):
        if ("instances" in request and not isinstance(request["instances"], list)) or \
           ("inputs" in request and not isinstance(request["inputs"], list)):
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Expected \"instances\" or \"inputs\" to be a list"
            )
        return _assign_request_to_inputs_instances_after_validation(request)


class B10PredictHandler(B10HTTPBinaryHandler):
    def post(self, name: str):
        model = self.get_model(name)
        try:
            body = b10_msgpack_deserialize(self.request.body)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Unrecognized request format: %s" % e
            )
        request = self.validate(body)
        request = model.preprocess(request)
        response = model.predict(request)
        response = model.postprocess(response)
        try:
            final_response = b10_msgpack_serialize(response)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                reason="Unable to serialize model prediction to response: %s" % e
            )
        self.write(final_response)


class B10ExplainHandler(B10HTTPBinaryHandler):
    def post(self, name: str):
        model = self.get_model(name)
        try:
            body = b10_msgpack_deserialize(self.request.body)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Unrecognized request format: %s" % e
            )
        request = self.validate(body)
        request = model.preprocess(request)
        response = model.explain(request)
        response = model.postprocess(response)
        try:
            final_response = b10_msgpack_serialize(response)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                reason="Unable to serialize model prediction to response: %s" % e
            )
        self.write(final_response)


class PredictHandler(B10HTTPHandler):
    def post(self, name: str):
        model = self.get_model(name)
        try:
            body = json.loads(self.request.body)
        except json.decoder.JSONDecodeError as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Unrecognized request format: %s" % e
            )
        request = self.validate(body)
        request = model.preprocess(request)
        response = model.predict(request)
        response = model.postprocess(response)
        try:
            final_response = json.dumps(response, cls=DeepNumpyEncoder)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                reason="Unable to serialize model prediction to response: %s" % e
            )
        self.write(final_response)


class ExplainHandler(B10HTTPHandler):
    def post(self, name: str):
        model = self.get_model(name)
        try:
            body = json.loads(self.request.body)
        except json.decoder.JSONDecodeError as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.BAD_REQUEST,
                reason="Unrecognized request format: %s" % e
            )
        request = self.validate(body)
        request = model.preprocess(request)
        response = model.explain(request)
        response = model.postprocess(response)
        try:
            final_response = json.dumps(response, cls=DeepNumpyEncoder)
        except Exception as e:
            raise tornado.web.HTTPError(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                reason="Unable to serialize model prediction to response: %s" % e
            )
        self.write(final_response)


class B10Server(KFServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        do_sentry_init()
        _configure_logging()

    def create_application(self):
        return tornado.web.Application([
            # Server Liveness API returns 200 if server is alive.
            (r"/", LivenessHandler),
            (r"/v1/models",
             ListHandler, dict(models=self.registered_models)),
            # Model Health API returns 200 if model is ready to serve.
            (r"/v1/models/([a-zA-Z0-9_-]+)",
             HealthHandler, dict(models=self.registered_models)),
            (r"/v1/models/([a-zA-Z0-9_-]+):predict",
             PredictHandler, dict(models=self.registered_models)),
            (r"/v1/models/([a-zA-Z0-9_-]+):predict_binary",
             B10PredictHandler, dict(models=self.registered_models)),
            (r"/v1/models/([a-zA-Z0-9_-]+):explain",
             ExplainHandler, dict(models=self.registered_models)),
            (r"/v1/models/([a-zA-Z0-9_-]+):explain_binary",
             B10ExplainHandler, dict(models=self.registered_models)),
        ])


def _configure_logging():
    json_log_handler = logging.StreamHandler()
    json_log_handler.setFormatter(jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s'))
    logger = logging.getLogger()
    for handler in logger.handlers:
        logger.removeHandler(handler)
    logger.addHandler(json_log_handler)
