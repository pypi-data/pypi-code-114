"""
This module is used to retrieve files from a json source
"""
import json
from typing import ByteString
from typing import Tuple

__virtualname__ = "json"


async def cache(hub, source: str, loc: str) -> Tuple[str, ByteString]:
    """
    Take a file from a location definition and cache it in memory
    """
    if source.startswith("json://"):
        source = source[7:]

    data = json.loads(source)

    return f"{loc}.sls", json.dumps(data[loc]).encode("utf-8")
