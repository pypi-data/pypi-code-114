from os import getenv

# Debug
DEBUG=bool(int(getenv("II_ENABLE_DEBUG", 0)))

# Logging
ENABLE_COLORS = bool(int(getenv("II_ENABLE_COLORS", 1)))
ENABLE_DATETIME_PREFIX = bool(int(getenv("II_ENABLE_DATETIME_PREFIX", 1)))
