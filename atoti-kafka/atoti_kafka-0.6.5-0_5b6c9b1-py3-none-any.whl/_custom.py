import json
from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping

from atoti_core import deprecated, keyword_only_dataclass

from ._kafka_deserializer import KafkaDeserializer


@keyword_only_dataclass
@dataclass(frozen=True)
class CustomDeserializer(KafkaDeserializer):
    """Deserializer implemented in Python."""

    callback: Callable[[str], Mapping[str, Any]]
    batch_size: int

    def deserialize(self, data: str) -> str:
        """Deserialize JSON bytes in a string.

        Args:
            data: String that can be parsed as JSON.
                Keys are ids and values are strings containing Kafka value's message part.

        Returns:
            Stringified array of strings: ``{1: {column_1: ***, column_2: ***, ...}, 2: {***}, ...}``.
        """
        data_json: Dict[str, str] = json.loads(data)

        try:
            result: Dict[str, Mapping[str, Any]] = {}
            for row_id, json_row in data_json.items():
                row = self.callback(json_row)  # type: ignore[misc, operator]
                result[row_id] = row
            return json.dumps(result)
        except KeyError as error:
            raise ValueError(
                "Error in custom deserializer: Missing table column"
            ) from error

    def toString(self) -> str:  # pylint: disable=invalid-name
        """Get the name of the deserializer."""
        return self.name

    class Java:
        """Code needed for Py4J callbacks."""

        implements = ["io.atoti.loading.kafka.impl.serialization.IPythonDeserializer"]


def create_deserializer(
    callback: Callable[[str], Mapping[str, Any]], *, batch_size: int = 1
) -> KafkaDeserializer:
    deprecated(
        "`create_deserializer()` is deprecated, use `JSON_DESERIALIZER` instead."
    )
    return CustomDeserializer(
        name="PythonDeserializer",
        callback=callback,
        batch_size=batch_size,
    )
