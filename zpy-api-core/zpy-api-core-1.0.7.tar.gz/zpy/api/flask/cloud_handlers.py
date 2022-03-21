import logging
from typing import Callable, Any, Optional
from zpy.containers import shared_container
from zpy.api.http.response import _useAwsRequestId
from zpy.logger import zL
from zpy.utils.values import if_null_get
from timeit import default_timer as timer
from datetime import timedelta
from functools import wraps
from zpy.app import zapp_context as api


def store_request_id(context) -> Optional[str]:
    """Extract aws request id from context

    Args:
        context ([type]): Lambda context
    """
    try:
        shared_container["aws_request_id"] = context.aws_request_id
        return context.aws_request_id
    except Exception as e:
        zL.ex("An error occurred while extracting aws request id", exc_info=e)
        return None


def event_processors(storage: dict, use_id: bool, logs: bool, send_logs: bool, *args, **kwargs):
    """Lambda event processors

    Args:
        @param storage:
        @param use_id:
        @param logs:
        @param send_logs:
    """
    try:
        if len(args) >= 2:
            event = args[0]
            storage['request'] = event
            if logs:
                api().logger.info(f"Request: {event}", shippable=send_logs)
            if _useAwsRequestId or use_id:
                storage['request_id'] = store_request_id(args[1])

        else:
            if "event" in kwargs:
                storage['request'] = kwargs['event']
                if logs:
                    api().logger.info(f"Request: {kwargs['event']}", shippable=send_logs)
            if "context" in kwargs:
                if _useAwsRequestId or use_id:
                    storage['request_id'] = store_request_id(args[1])
    except Exception as e:
        api().logger.ex("An error occurred while processing event!", exc_info=e)


def aws_lambda(logs: bool = True, save_id: bool = False, measure_time: bool = True, send_logs: bool = False,
               event_sender: Optional[Callable[[dict], Any]] = None):
    """Lambda Handler

    Args:
        @param event_sender:
        @param logs: (bool, optional): Logging request and response. Defaults to False.
        @param save_id: (bool, optional): Register aws lambda request id. Defaults to True.
        @param measure_time: (bool, optional): Measure elapsed execution time. Defaults to True.
        @param send_logs: Send event logs by log sender configured
    """
    api().release_logger()
    event = {}

    def callable_fn(invoker: Callable):
        @wraps(invoker)
        def wrapper(*args, **kwargs):
            event_processors(event, save_id, logs, send_logs, *args, **kwargs)
            start = 0.0
            if if_null_get(measure_time, False):
                start = timer()
            result = invoker(*args, **kwargs)
            event['response'] = result
            if logs:
                api().logger.info(f"Response: {result}", shippable=send_logs)
            if if_null_get(measure_time, False):
                end = timer()
                api().logger.info(f"Elapsed execution time: {timedelta(seconds=end - start)}", shippable=send_logs)
            if event_sender:
                event_sender(event)
            return result

        return wrapper

    return callable_fn
