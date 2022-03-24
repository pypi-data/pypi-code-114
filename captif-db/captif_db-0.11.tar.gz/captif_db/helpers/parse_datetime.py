from functools import lru_cache
from datetime import datetime, timedelta


DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y", "%d-%m-%y"]
TIME_FORMATS = ["%H:%M:%S", "%H:%M", "%I:%M %p"]
DATETIME_FORMATS = [" ".join([df, tf]) for df in DATE_FORMATS for tf in TIME_FORMATS]

FORMATS = {
    "datetime": DATE_FORMATS + DATETIME_FORMATS,
    "timedelta": TIME_FORMATS,
}


def is_datetime(dt):
    if isinstance(dt, str):
        dt = to_datetime(dt)
    return isinstance(dt, datetime) or isinstance(dt, timedelta)


def parse_am_pm(s):
    am = ("a.m.", "AM")
    pm = ("p.m.", "PM")
    return s.replace(*am).replace(*pm)


@lru_cache(maxsize=1)
def to_datetime(dt):
    dt = parse_am_pm(dt)
    for format_type, formats in FORMATS.items():
        for fmt in formats:
            try:
                dt = datetime.strptime(dt, fmt)
                if format_type == "timedelta":
                    dt = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
                return dt
            except ValueError:
                pass
    return dt
