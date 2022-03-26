# This file is placed in the Public Domain.


"OTP-CR-117/19"


def __dir__():
    return (
        "bus",
        "callbacks",
        "class",
        "database",
        "event",
        "function",
        "find",
        "irc",
        "json",
        "kernel",
        "log",
        "model",
        "output",
        "parse",
        "reqquest",
        "repater",
        "table",
        "todo",
        "thread",
        "timer",
        "udp",
        "user",
    )


from genocide.table import Tbl


from genocide import config
from genocide import command
from genocide import database
from genocide import event
from genocide import function
from genocide import json
from genocide import kernel
from genocide import output
from genocide import parse
from genocide import repeater
from genocide import table
from genocide import thread
from genocide import timer

from genocide import find
from genocide import irc
from genocide import log
from genocide import model
from genocide import output
from genocide import request
from genocide import status
from genocide import todo
from genocide import udp
from genocide import user


for mn in __dir__():
    md = getattr(locals(), mn, None)
    if md:
        Tbl.add(md)
