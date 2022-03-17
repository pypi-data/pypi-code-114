from io import BytesIO, RawIOBase
from typing import Any, Dict, Union, cast

from genpy import dynamic  # type: ignore
from mcap.mcap0.exceptions import McapError
from mcap.mcap0.records import Channel, Message, Schema
from mcap.mcap0.stream_reader import StreamReader


class Ros1Decoder:
    def __init__(self, source: Union[bytes, StreamReader]):
        if isinstance(source, StreamReader):
            self.__reader = source
        else:
            self.__reader = StreamReader(cast(RawIOBase, BytesIO(source)))

    @property
    def messages(self):
        channels: Dict[int, Channel] = {}
        schemas: Dict[int, Schema] = {}
        msg_types: Dict[str, Any] = {}
        for record in self.__reader.records:
            if isinstance(record, Schema):
                schemas[record.id] = record
                if record.encoding != "ros1msg":
                    raise McapError(
                        f"Can't decode schema with encoding {record.encoding}"
                    )
                if not record.name in msg_types:
                    msg_type = dynamic.generate_dynamic(  # type: ignore
                        record.name, record.data.decode()
                    )
                    msg_types[record.name] = msg_type[record.name]
            if isinstance(record, Channel):
                channels[record.id] = record
            if isinstance(record, Message):
                channel = channels[record.channel_id]
                schema = schemas[channel.schema_id]
                message = msg_types[schema.name]().deserialize(record.data)
                yield (channel.topic, record, message)
