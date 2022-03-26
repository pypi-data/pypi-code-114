# This file is placed in the Public Domain.


"callbacks"


from .function import register
from .object import Object, get
from .thread import launch


def __dir__():
    return (
        "Cbs",
    )


class Cbs(Object):

    cbs = Object()

    @staticmethod
    def add(name, cb):
        register(Cbs.cbs, name, cb)

    @staticmethod
    def callback(e):
        f = Cbs.get(e.type)
        if f:
            f(e)

    @staticmethod
    def get(cmd):
        return get(Cbs.cbs, cmd)


    @staticmethod
    def dispatch(e):
        e.thrs.append(launch(Cbs.callback, e, name=e.txt))
