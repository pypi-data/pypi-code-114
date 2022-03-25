from dataclasses import dataclass

from atoti_core import keyword_only_dataclass


@keyword_only_dataclass
@dataclass(frozen=True)
class KafkaDeserializer:
    """Kafka Deserializer."""

    name: str
    """Name of the deserializer."""
