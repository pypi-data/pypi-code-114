from typing import ByteString
from typing import Tuple

# https://pypi.org/project/gitfs2

try:
    import gitfs2.opener
    import fs.opener
    from fs.opener.parse import ParseResult

    HAS_LIBS = (True,)
except ImportError as e:
    HAS_LIBS = False, str(e)


def __virtual__(hub):
    return HAS_LIBS


__virtualname__ = "git"


async def cache(hub, source: str, loc: str) -> Tuple[str, ByteString]:
    """
    Take a file from git and cache it in the target location
    """
    result = fs.opener.parse(source)
    # Allow for git+http and git+https
    if "git+" in result.protocol:
        result = ParseResult(
            protocol=result.protocol[4:],
            username=result.username,
            password=result.password,
            params=result.params,
            resource=result.resource,
            path=result.path,
        )
    gitfs = gitfs2.opener.GitFSOpener()

    with gitfs.open_fs(
        source, create=True, writeable=False, parse_result=result, cwd=""
    ) as fh:
        # Now that the repo is cloned, process it like a normal file source
        return await hub.idem.sls.file.cache(fh.root_path, loc)
