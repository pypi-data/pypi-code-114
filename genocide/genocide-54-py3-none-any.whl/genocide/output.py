# This file is placed in the Public Domain.


"output"


import queue
import threading


from .command import Cmd
from .object import Object
from .thread import launch


class Output(Object):


    def __init__(self):
        Object.__init__(self)
        self.cache = Object()
        self.oqueue = queue.Queue()
        self.dostop = threading.Event()

    def dosay(self, channel, txt):
        pass

    def extend(self, channel, txtlist):
        if channel not in self.cache:
            self.cache[channel] = []
        self.cache[channel].extend(txtlist)

    def oput(self, channel, txt):
        self.oqueue.put_nowait((channel, txt))

    def output(self):
        while not self.dostop.is_set():
            (channel, txt) = self.oqueue.get()
            if self.dostop.is_set():
                break
            try:
                self.dosay(channel, txt)
            except Exception as ex:
                pass

    def size(self, name):
        if name in self.cache:
            return len(self.cache[name])
        return 0

    def start(self):
        self.dostop.clear()
        launch(self.output)
        return self

    def stop(self):
        self.dostop.set()
        self.oqueue.put_nowait((None, None))



def mre(event):
    if event.channel is None:
        event.reply("channel is not set.")
        return
    bot = event.bot()
    if event.channel not in bot.cache:
        event.reply("no output in %s cache." % event.channel)
        return
    for _x in range(3):
        txt = bot.cache[event.channel].pop(0)
        if txt:
            bot.say(event.channel, txt)
    sz = bot.size(event.channel)
    if sz:
        event.reply("(+%s more)" % sz)


Cmd.add(mre)
