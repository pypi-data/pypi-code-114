import dataclasses
import datetime
import enum
from json import JSONEncoder

__all__ = ["RichEncoder"]


class RichEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime.datetime, datetime.date, datetime.time)):
            return o.isoformat()
        elif dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, enum.Enum):
            return o.value
        elif isinstance(o, datetime.timedelta):
            return (datetime.datetime.min + o).time().isoformat()
        elif callable(o):
            return o.__name__

        return super().default(o)
