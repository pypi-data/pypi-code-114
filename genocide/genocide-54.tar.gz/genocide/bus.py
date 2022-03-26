# This file is placed in the Public Domain.


"bus"


from .object import Object


def __dir__():
    return (
        "Bus",
    )


class Bus(Object):

    objs = []

    @staticmethod
    def add(o):
        "add listener"
        if repr(o) not in [repr(x) for x in Bus.objs]:
            Bus.objs.append(o)

    @staticmethod
    def announce(txt):
        "announce on bus"
        for o in Bus.objs:
            o.announce(txt)

    @staticmethod
    def byorig(orig):
        "return listener by origin"
        for o in Bus.objs:
            if repr(o) == orig:
                return o

    @staticmethod
    def say(orig, channel, txt):
        "send text to specific listener/channel"
        o = Bus.byorig(orig)
        if o:
            o.say(channel, txt)
