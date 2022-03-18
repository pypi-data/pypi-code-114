from dataclasses import dataclass


async def sig_cache(hub, source, loc) -> bytes:
    ...


@dataclass
class CacheTarget:
    path: str
    value: bytes

    def __bool__(self):
        return bool(self.value)

    def __iter__(self):
        yield self.path
        yield self.value


async def post_cache(hub, ctx):
    # Validate the return
    if not ctx.ret:
        return CacheTarget("", b"")
    path, value = ctx.ret
    return CacheTarget(path, value)
