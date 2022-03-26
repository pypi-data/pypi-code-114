# This file is placed in the Public Domain.


"thread"


import os
import queue
import threading
import time
import traceback
import types


from .event import Event


def __dir__():
    return (
        "Thr",
        "getexception",
        "getname",
        "launch",
    )


starttime = time.time()


class Thr(threading.Thread):

    def __init__(self, func, name, *args, daemon=True):
        super().__init__(None, self.run, name, (), {}, daemon=daemon)
        self.exc = None
        self.evt = None
        self.name = name
        self.queue = queue.Queue()
        self.queue.put_nowait((func, args))
        self.result = None

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        super().join(timeout)
        if self.evt:
            return self.evt
        return self.result

    def run(self):
        func, args = self.queue.get()
        if args and isinstance(args[0], Event):
            self.evt = args[0]
        self.setName(self.name)
        try:
            self.result = func(*args)
        except Exception as ex:
            self.exc = ex
            if self.evt:
                self.evt.reply(from_exception(ex))
        if self.evt:
            self.evt.ready()
            self.evt._result = self.result
        return self.evt


def from_exception(ex, txt="", sep=" "):
    result = []
    for fr in traceback.extract_tb(ex.__traceback__):
        result.append("%s:%s" % (os.sep.join(fr.filename.split(os.sep)[-2:]), fr.lineno))
    return "%s(%s) %s" % (getname(ex), ex, " ".join(result))


def getname(o):
    t = type(o)
    if isinstance(t, types.ModuleType):
        return o.__name__
    if "__self__" in dir(o):
        return "%s.%s" % (o.__self__.__class__.__name__, o.__name__)
    if "__class__" in dir(o) and "__name__" in dir(o):
        return "%s.%s" % (o.__class__.__name__, o.__name__)
    if "__class__" in dir(o):
        return o.__class__.__name__
    if "__name__" in dir(o):
        return o.__name__
    return None


def launch(func, *args, **kwargs):
    name = kwargs.get("name", getname(func))
    t = Thr(func, name, *args)
    t.start()
    return t
