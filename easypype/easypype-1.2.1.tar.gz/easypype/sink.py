import abc


class Sink(abc.ABC):

    @abc.abstractproperty
    def data(self):
        pass

    @abc.abstractmethod
    def collect(self, data):
        pass


class ConcreteSink(Sink):
    """A Sink implementation. It holds the Pipe data.
    
    ...
    Properties:
    - data : object
        The data loaded in memory.
        
    Methods:
    - collect(data)
        Loads data into memory.
    - __init__()
        Creates an empty sink."""

    @property
    def data(self):
        """Returns all collected data."""
        return self._data

    def collect(self, data):
        """Collects the data payload."""
        self._data = data
