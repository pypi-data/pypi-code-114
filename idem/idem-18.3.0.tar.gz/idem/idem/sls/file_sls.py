"""
This module is used to retrieve files from a local source
"""
import mimetypes
import os
from typing import ByteString
from typing import Tuple

__virtualname__ = "file"


async def process(hub, source_path: str, loc: str) -> Tuple[str, ByteString]:
    """
    Determine if a file has mimetypes, if so, unravel it and save it's tree in memory
    """
    filemimetypes = mimetypes.guess_type(source_path)
    if filemimetypes:
        for plugin in hub.idem.sls:
            if not hasattr(plugin, "MIMETYPE"):
                continue
            if plugin.MIMETYPE in filemimetypes:
                return await plugin.cache(source_path, loc)


async def cache(hub, source: str, loc: str) -> Tuple[str, ByteString]:
    """
    Take a file from a location definition and cache it in memory
    """
    # Check if the file has a mimetype and call the right plugin
    if source.startswith("file://"):
        source_path = source[7:]
    else:
        source_path = source

    if os.path.isfile(source_path):
        ref, mime_source = await hub.idem.sls.file.process(source_path, loc)
        if mime_source:
            return ref, mime_source

    # No mimetypes, read a plain SLS file
    full = os.path.join(source_path, loc)
    if os.path.isfile(full):
        with open(full, "rb") as rfh:
            in_memory_file = rfh.read()

        return full, in_memory_file
