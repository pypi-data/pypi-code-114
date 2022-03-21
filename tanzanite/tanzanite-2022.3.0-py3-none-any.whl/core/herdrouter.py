import asyncio
import threading


class HerdRouter(threading.Thread):
    """
    Class for running co-routines in a separate thread from loop runner.

    See https://agariinc.medium.com/
        advanced-strategies-for-testing-async-code-in-python-6196a032d8d7
    """

    def __init__(self, loop, target=None):
        """Initialize HerdRouter with event loop."""
        super().__init__(group=None, target=target)
        self._loop = loop
        self._rlock = threading.RLock()
        self.commands = set()

    async def _add_command(self, key):
        """Safely add to command set."""
        with self._rlock:
            self.commands.add(key)

    def add_command(self, key):
        """Run in object's event loop."""
        result = asyncio.run_coroutine_threadsafe(
            self._add_command(key),
            self._loop,
        )
        result.result()
