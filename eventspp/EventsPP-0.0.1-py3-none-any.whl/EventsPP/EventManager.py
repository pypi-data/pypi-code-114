from functools import wraps


class EventManager:
    __slots__ = '__events'

    def __init__(self):
        self.__events = None

    @staticmethod
    def __call(event, *args, **kwargs):
        if event is not None:
            return event(*args, **kwargs)

    @staticmethod
    def __make_event(function):

        @wraps(function)
        def event(*args, **kwargs):
            EventManager.__call(function, *args, **kwargs)

        return event

    def set_events(self, **schemas):

        class Events:
            pass

        for name, function in schemas.items():
            setattr(Events, name, EventManager.__make_event(function))

        self.__events = Events

    @property
    def events(self):
        return self.__events
