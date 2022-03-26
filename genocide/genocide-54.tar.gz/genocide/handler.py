# This file is placed in the Public Domain.


"event handler"


import threading


from .bus import Bus
from .command import Cmd
from .callback import Cbs
from .object import Object
from .thread import launch


def __dir__():
    return (
        "Handler",
        "dispatch",
    )


class Handler(Object):

    def __init__(self):
        Object.__init__(self)
        self.errors = []
        self.stopped = threading.Event()
        self.register("event", dispatch)
        self.threaded = False

    def announce(self, txt):
        self.raw(txt)

    def handle(self, e):
        if self.threaded:
            e.thrs.append(launch(Cbs.callback, e, name=e.txt))
        else:
            Cbs.callback(e)

    def loop(self):
        while not self.stopped.is_set():
            self.handle(self.poll())

    def raw(self, txt):
        raise NotImplementedError

    def register(self, typ, cb):
        Cbs.add(typ, cb)

    def restart(self):
        self.stop()
        self.start()

    def say(self, channel, txt):
        self.raw(txt)

    def start(self):
        Bus.add(self)
        self.stopped.clear()
        launch(self.loop)

    def stop(self):
        pass


def dispatch(e):
    e.parse()
    f = Cmd.get(e.cmd)
    if f:
        f(e)
        e.show()
    e.ready()
