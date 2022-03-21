import logging
from typing import Any, Callable, Tuple, Optional

from .serializers import serialize_object_value
from zpy.api.http.errors import ZHttpError
from zpy.api.http.status_codes import HttpStatus
from zpy.containers import shared_container
from zpy.utils.objects import ZObjectModel
from zpy.utils.values import if_null_get

_useAwsRequestId = False
_wrapPayloadKey = None
_useStatusFields = False
_custom_builder: Optional[Callable[[dict, HttpStatus, dict], Tuple[dict, int, dict]]] = None
_custom_error_builder: Optional[Callable[[dict, HttpStatus, dict], Tuple[dict, int, dict]]] = None


def setup_response_builder(
        use_aws_request_id: bool = False,
        wrap_payload_key: Optional[str] = None,
        use_status_fields: bool = False,
        custom_builder: Callable = None,
        custom_error_builder: Callable = None
) -> None:
    """
    Configure response builder according you need it
    @param use_aws_request_id: True if you work with aws services and need add aws request id into your response
    @param wrap_payload_key: Pass string key for wrap your payload
    @param use_status_fields: True if you need add 'status' and 'message' fields into response
    @param custom_builder: Function to update or build response according you need it
    @param custom_error_builder: Function to update or build error response according you need it
    @return: None
    """
    global _useAwsRequestId
    _useAwsRequestId = use_aws_request_id
    global _wrapPayloadKey
    _wrapPayloadKey = wrap_payload_key
    global _useStatusFields
    _useStatusFields = use_status_fields
    global _custom_builder
    _custom_builder = custom_builder
    global _custom_error_builder
    _custom_error_builder = custom_error_builder


class SuccessResponse(object):
    def __init__(self, status: HttpStatus = HttpStatus.SUCCESS) -> None:
        self._http_status_ = status

    @property
    def http_status(self):
        return self._http_status_


def update_error_response(response: dict, status: HttpStatus = HttpStatus.INTERNAL_SERVER_ERROR,
                          headers: Optional[dict] = None) -> Tuple[dict, int, dict]:
    """
    Http error response updater
    @param response: error response content
    @param status: http status
    @param headers: headers
    @return: tuple with response data

    @contact https://www.linkedin.com/in/zurckz
    @author Noé Cruz | Zurck'z 20
    @since 16-05-2020
    """
    http_status_code: int = status.value[0]
    if _useAwsRequestId is True:
        if type(response) is dict and "aws_request_id" in shared_container:
            response.update({"requestId": shared_container["aws_request_id"]})
    if _custom_builder is not None:
        response, code, headers = _custom_error_builder(response, status, headers)
        http_status_code = code
    return response, http_status_code, headers


def update_response(
        payload: dict, status: HttpStatus = HttpStatus.SUCCESS, headers: Optional[dict] = None
) -> Tuple[dict, int, dict]:
    """
    Http response updater
    @param payload:
    @param status:
    @param headers:
    @return: tuple with reponse data

    @contact https://www.linkedin.com/in/zurckz
    @author Noé Cruz | Zurck'z 20
    @since 16-05-2020
    """
    http_status_code = status.value[0]
    if _wrapPayloadKey is not None and _wrapPayloadKey != "":
        payload = {_wrapPayloadKey: payload}
    if _useStatusFields is True:
        if type(payload) is dict:
            payload.update({"status": status.value[1], "message": status.value[2]})
    if _useAwsRequestId is True:
        if type(payload) is dict and "aws_request_id" in shared_container:
            payload.update({"requestId": shared_container["aws_request_id"]})
    if _custom_builder is not None:
        payload, code, headers = _custom_builder(payload, status, headers)
        http_status_code = code
    return payload, http_status_code, headers


def response_builder(content_type: Optional[str] = 'application/json', headers: Optional[dict] = None):
    """
    HTTP Response builder, build response from data provided
    @param content_type: Response content type. Default: application/json
    @param headers: Extra headers
    @return: None

    @contact https://www.linkedin.com/in/zurckz
    @author Noé Cruz | Zurck'z 20
    @since 16-05-2020
    """
    extra_headers = {'Content-Type': content_type}

    def z_inner_builder(invoker: Callable):
        def wrapper_handler(*args, **kwargs):
            try:
                payload: Any = invoker(*args, **kwargs)

                if issubclass(payload.__class__, ZObjectModel) and issubclass(
                        payload.__class__, SuccessResponse
                ):
                    return update_response(payload.sdump(), payload.http_status)

                if issubclass(payload.__class__, ZObjectModel):
                    return update_response(payload.sdump())

                if issubclass(payload.__class__, SuccessResponse):
                    return update_response(
                        serialize_object_value(payload), payload.http_status
                    )
                return update_response(serialize_object_value(payload), headers=extra_headers)
            except ZHttpError as e:
                logging.exception("[ZCE] - An error was generated when processing request.")
                http_status: HttpStatus = e.status
                if e.reason is not None:
                    e.details = [e.reason] + if_null_get(e.details, [])
                err_response = {
                    "message": if_null_get(e.message, http_status.value[2]),
                    "code": http_status.value[1],
                    "details": e.details,
                }
                if e.metadata is not None:
                    err_response['metadata'] = e.metadata
                return update_error_response(
                    err_response,
                    http_status
                )
            except Exception as e:
                logging.exception(
                    "[UCE] - An unexpected error was generated when processing request.", exc_info=e
                )
                code: HttpStatus = HttpStatus.INTERNAL_SERVER_ERROR
                return update_error_response(
                    {"message": code.value[2], "code": code.value[1], "details": None}, code
                )

        wrapper_handler.__name__ = invoker.__name__
        return wrapper_handler

    return z_inner_builder
