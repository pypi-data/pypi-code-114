# This file is placed in the Public Domain.


"things todo"


def __dir__():
    return (
        "tdo",
    )


import time


from .cls import Cls
from .command import Cmd
from .database import find, fntime, save
from .object import Object
from .parse import elapsed
from .thread import starttime


class Todo(Object):

    def __init__(self):
        super().__init__()
        self.txt = ""


def tdo(event):
    if not event.rest:
        nr = 0
        for fn, o in find("todo"):
            event.reply("%s %s %s" % (nr, o.txt, elapsed(time.time() - fntime(fn))))
        return
    o = Todo()
    o.txt = event.rest
    save(o)
    event.reply("ok")


def upt(event):
    event.reply(elapsed(time.time() - starttime))


Cls.add(Todo)
Cmd.add(tdo)
