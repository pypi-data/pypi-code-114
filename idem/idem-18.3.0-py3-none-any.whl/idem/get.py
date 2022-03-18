"""
This file contains routines to get sls files from references
"""
from typing import ByteString
from typing import Tuple


async def ref(hub, name: str, sls: str) -> Tuple[str, ByteString]:
    """
    Cache the given file from the named reference point
    """
    if hub.idem.RUNS[name]["params_processing"]:
        sources = hub.idem.RUNS[name]["param_sources"]
    else:
        sources = hub.idem.RUNS[name]["sls_sources"]

    for source in sources:
        proto = source[: source.index(":")].split("+")[0]
        path = sls.replace(".", "/")
        locs = [f"{path}.sls", f"{path}/init.sls"]
        for loc in locs:
            ref, cfn = await hub.idem.sls[proto].cache(source, loc)
            if cfn:
                return ref, cfn
    return "", b""
