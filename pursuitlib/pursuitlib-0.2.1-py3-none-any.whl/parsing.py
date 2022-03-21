from typing import Optional


def parseint(value, default: Optional[int] = None) -> Optional[int]:
    if value is not None:
        try:
            return int(value)
        except ValueError:
            return default
    else: return default


def parsefloat(value, default: Optional[float] = None) -> Optional[float]:
    if value is not None:
        try:
            return float(value)
        except ValueError:
            return default
    else: return default
