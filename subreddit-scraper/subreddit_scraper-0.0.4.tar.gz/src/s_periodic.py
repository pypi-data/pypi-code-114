"""Class to run a function periodically, https://stackoverflow.com/a/37514633/12107639"""

import asyncio
from contextlib import suppress

__all__ = ["Periodic"]


class Periodic:
    """Class to run a function periodically, https://stackoverflow.com/a/37514633/12107639"""

    def __init__(self, func, time):
        """Initializes the class."""
        self.func = func
        self.time = time
        self.is_started = False
        self._task = None

    async def start(self):
        """Starts the periodic task."""
        if not self.is_started:
            self.is_started = True
            # Start task to call func periodically:
            self._task = asyncio.ensure_future(self._run())

    async def stop(self):
        """Stops the periodic task."""
        if self.is_started:
            self.is_started = False
            # Stop task and await it stopped:
            self._task.cancel()
            with suppress(asyncio.CancelledError):
                await self._task

    async def _run(self):
        """Runs the function periodically."""
        while True:
            await asyncio.sleep(self.time)
            self.func()
