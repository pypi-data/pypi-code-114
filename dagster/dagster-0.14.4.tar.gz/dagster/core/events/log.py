from typing import Any, Dict, NamedTuple, Optional, Union

from dagster import check
from dagster.core.errors import DagsterInvariantViolationError
from dagster.core.events import DagsterEvent
from dagster.core.utils import coerce_valid_log_level
from dagster.serdes.serdes import (
    DefaultNamedTupleSerializer,
    WhitelistMap,
    deserialize_json_to_dagster_namedtuple,
    register_serdes_tuple_fallbacks,
    serialize_dagster_namedtuple,
    whitelist_for_serdes,
)
from dagster.utils.error import SerializableErrorInfo
from dagster.utils.log import (
    JsonEventLoggerHandler,
    StructuredLoggerHandler,
    StructuredLoggerMessage,
    construct_single_handler_logger,
)


class EventLogEntrySerializer(DefaultNamedTupleSerializer):
    @classmethod
    def value_to_storage_dict(
        cls,
        value: NamedTuple,
        whitelist_map: WhitelistMap,
        descent_path: str,
    ) -> Dict[str, Any]:
        storage_dict = super().value_to_storage_dict(value, whitelist_map, descent_path)
        # include an empty string for the message field to allow older versions of dagster to load the events
        storage_dict["message"] = ""
        return storage_dict


@whitelist_for_serdes(serializer=EventLogEntrySerializer)
class EventLogEntry(
    NamedTuple(
        "_EventLogEntry",
        [
            ("error_info", Optional[SerializableErrorInfo]),
            ("level", Union[str, int]),
            ("user_message", str),
            ("run_id", str),
            ("timestamp", float),
            ("step_key", Optional[str]),
            ("pipeline_name", Optional[str]),
            ("dagster_event", Optional[DagsterEvent]),
        ],
    )
):
    """Entries in the event log.

    These entries may originate from the logging machinery (DagsterLogManager/context.log), from
    framework events (e.g. EngineEvent), or they may correspond to events yielded by user code
    (e.g. Output).

    Args:
        error_info (Optional[SerializableErrorInfo]): Error info for an associated exception, if
            any, as generated by serializable_error_info_from_exc_info and friends.
        level (Union[str, int]): The Python log level at which to log this event. Note that
            framework and user code events are also logged to Python logging. This value may be an
            integer or a (case-insensitive) string member of PYTHON_LOGGING_LEVELS_NAMES.
        user_message (str): For log messages, this is the user-generated message.
        run_id (str): The id of the run which generated this event.
        timestamp (float): The Unix timestamp of this event.
        step_key (Optional[str]): The step key for the step which generated this event. Some events
            are generated outside of a step context.
        job_name (Optional[str]): The job which generated this event. Some events are
            generated outside of a job context.
        dagster_event (Optional[DagsterEvent]): For framework and user events, the associated
            structured event.
        pipeline_name (Optional[str]): (legacy) The pipeline which generated this event. Some events are
            generated outside of a pipeline context.
    """

    def __new__(
        cls,
        error_info,
        level,
        user_message,
        run_id,
        timestamp,
        step_key=None,
        pipeline_name=None,
        dagster_event=None,
        job_name=None,
    ):
        if pipeline_name and job_name:
            raise DagsterInvariantViolationError(
                "Provided both `pipeline_name` and `job_name` parameters to `EventLogEntry` "
                "initialization. Please provide only one or the other."
            )

        pipeline_name = pipeline_name or job_name
        return super(EventLogEntry, cls).__new__(
            cls,
            check.opt_inst_param(error_info, "error_info", SerializableErrorInfo),
            coerce_valid_log_level(level),
            check.str_param(user_message, "user_message"),
            check.str_param(run_id, "run_id"),
            check.float_param(timestamp, "timestamp"),
            check.opt_str_param(step_key, "step_key"),
            check.opt_str_param(pipeline_name, "pipeline_name"),
            check.opt_inst_param(dagster_event, "dagster_event", DagsterEvent),
        )

    @property
    def is_dagster_event(self) -> bool:
        return bool(self.dagster_event)

    @property
    def job_name(self) -> Optional[str]:
        return self.pipeline_name

    def get_dagster_event(self) -> DagsterEvent:
        if not isinstance(self.dagster_event, DagsterEvent):
            check.failed(
                "Not a dagster event, check is_dagster_event before calling get_dagster_event",
            )

        return self.dagster_event

    def to_json(self):
        return serialize_dagster_namedtuple(self)

    @staticmethod
    def from_json(json_str):
        return deserialize_json_to_dagster_namedtuple(json_str)

    @property
    def dagster_event_type(self):
        return self.dagster_event.event_type if self.dagster_event else None

    @property
    def message(self) -> str:
        """
        Return the message from the structured DagsterEvent if present, fallback to user_message
        """

        if self.is_dagster_event:
            msg = self.get_dagster_event().message
            if msg is not None:
                return msg

        return self.user_message


def construct_event_record(logger_message):
    check.inst_param(logger_message, "logger_message", StructuredLoggerMessage)

    return EventLogEntry(
        level=logger_message.level,
        user_message=logger_message.meta["orig_message"],
        run_id=logger_message.meta["run_id"],
        timestamp=logger_message.record.created,
        step_key=logger_message.meta.get("step_key"),
        job_name=logger_message.meta.get("pipeline_name"),
        dagster_event=logger_message.meta.get("dagster_event"),
        error_info=None,
    )


def construct_event_logger(event_record_callback):
    """
    Callback receives a stream of event_records. Piggybacks on the logging machinery.
    """
    check.callable_param(event_record_callback, "event_record_callback")

    return construct_single_handler_logger(
        "event-logger",
        "debug",
        StructuredLoggerHandler(
            lambda logger_message: event_record_callback(construct_event_record(logger_message))
        ),
    )


def construct_json_event_logger(json_path):
    """Record a stream of event records to json"""
    check.str_param(json_path, "json_path")
    return construct_single_handler_logger(
        "json-event-record-logger",
        "debug",
        JsonEventLoggerHandler(
            json_path,
            lambda record: construct_event_record(
                StructuredLoggerMessage(
                    name=record.name,
                    message=record.msg,
                    level=record.levelno,
                    meta=record.dagster_meta,
                    record=record,
                )
            ),
        ),
    )


register_serdes_tuple_fallbacks(
    {
        # These were originally distinguished from each other but ended up being empty subclasses
        # of EventLogEntry -- instead of using the subclasses we were relying on
        # EventLogEntry.is_dagster_event to distinguish events that originate in the logging
        # machinery from events that are yielded by user code
        "DagsterEventRecord": EventLogEntry,
        "LogMessageRecord": EventLogEntry,
        # renamed EventRecord -> EventLogEntry
        "EventRecord": EventLogEntry,
    }
)
