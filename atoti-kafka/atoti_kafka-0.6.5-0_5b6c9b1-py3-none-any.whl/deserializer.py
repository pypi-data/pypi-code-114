from ._kafka_deserializer import KafkaDeserializer

JSON_DESERIALIZER = KafkaDeserializer(
    name="io.atoti.loading.kafka.impl.serialization.JsonDeserializer"
)
"""Core JSON deserializer.

Each JSON object corresponds to a row of the table, keys of the JSON object must match columns of the table.
"""
