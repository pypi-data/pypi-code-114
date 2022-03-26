import asyncio


from aiocoap.error import LibraryShutdown, NotObservable, ObservationCancelled
from aiocoap.protocol import ClientObservation


def __del__(self):
    if self._future.done():
        try:
            # Fetch the result so any errors show up at least in the
            # finalizer output
            self._future.result()
        except (ObservationCancelled, NotObservable):
            # This is the case at the end of an observation cancelled
            # by the server.
            pass
        except LibraryShutdown:
            pass
        except asyncio.CancelledError:
            pass


ClientObservation._Iterator.__del__ = __del__
