# This file is placed in the Public Domain.


"event"


import threading


from .bus import Bus
from .object import Object
from .parse import parse


def __dir__():
    return (
        "Event",
    )


class Event(Object):

    def __init__(self):
        super().__init__()
        self._ready = threading.Event()
        self._result = None
        self.announce = False
        self.channel = ""
        self.errors = []
        self.orig = ""
        self.origin = ""
        self.result = []
        self.thrs = []
        self.type = "event"

    def bot(self):
        return Bus.byorig(self.orig)

    def parse(self, txt=None):
        parse(self, txt or self.txt)

    def ready(self):
        self._ready.set()

    def reply(self, txt):
        self.result.append(txt)

    def show(self):
        assert self.orig
        for txt in self.result:
            Bus.say(self.orig, self.channel, txt)

    def wait(self):
        self._ready.wait()
        for thr in self.thrs:
            thr.join()
        return self.result
