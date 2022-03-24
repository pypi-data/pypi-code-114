from .base import Update, UpdateType
from .openretractions import OpenRetractions

__all__ = ["Update", "UpdateType", "registry"]

registry = {
    "openretractions": OpenRetractions(),
}
