import asyncio
import signal
from typing import List


class AioThing:
    def __init__(self):
        self.starts: List[AioThing] = []
        self.waits: List[AioThing] = []
        self.started = False
        self.start = self._guard_start(self.start)
        self.stop = self._guard_stop(self.stop)
        self._current_task = None

    def _guard_start(self, fn):
        async def guarded_fn(*args, **kwargs):
            if self.started:
                return
            self.started = True
            self.setup_hooks()
            for aw in self.starts:
                await aw.start()
            for aw in self.waits:
                await aw.start_and_wait()
            self._current_task = asyncio.create_task(fn(*args, **kwargs))
            return self._current_task
        return guarded_fn

    def _guard_stop(self, fn):
        async def guarded_fn(*args, **kwargs):
            if not self.started:
                return
            self.started = False
            r = await fn(*args, **kwargs)
            await self.cancel()
            for aw in reversed(self.starts + self.waits):
                await aw.stop()
            return r
        return guarded_fn

    async def cancel(self):
        if self._current_task:
            self._current_task.cancel()
            await self._current_task
            self._current_task = None

    def task(self):
        return self._current_task

    async def start(self):
        pass

    async def stop(self):
        pass

    async def start_and_wait(self):
        await self.start()
        await self.task()

    def setup_hooks(self):
        pass


class AioRootThing(AioThing):
    def setup_hooks(self):
        for sig in (signal.SIGTERM, signal.SIGINT):
            asyncio.get_event_loop().add_signal_handler(sig, self._on_shutdown)

    def _on_shutdown(self):
        asyncio.get_event_loop().create_task(self.stop())
