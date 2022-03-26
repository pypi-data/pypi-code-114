# This file is placed in the Public Domain.


"kernel"


import getpass
import os
import pwd
import time


from .bus import Bus
from .config import Cfg
from .event import Event
from .parse import parse


def __dir__():
    return (
        "Cfg",
        "boot",
        "kcmd",
        "privileges",
        "root"
    )


class Cfg(Cfg):

    console = False
    daemon = False
    debug = False
    index = 0
    otxt = ""
    txt = ""
    verbose = False
    wd = ""


def boot(txt):
    parse(Cfg, txt)
    Cfg.console = "c" in Cfg.opts
    Cfg.daemon = "d" in Cfg.opts
    Cfg.verbose = "v" in Cfg.opts
    Cfg.debug = "z" in Cfg.opts


def kcmd(clt, txt):
    if not txt:
        return False
    Bus.add(clt)
    e = Event()
    e.channel = ""
    e.orig = repr(clt)
    e.txt = txt
    clt.handle(e)
    e.wait()
    return e.result


def privileges(name=None):
    if os.getuid() != 0:
        return
    if name is None:
        try:
            name = getpass.getuser()
        except KeyError:
            pass
    try:
        pwnam = pwd.getpwnam(name)
    except KeyError:
        return False
    os.setgroups([])
    os.setgid(pwnam.pw_gid)
    os.setuid(pwnam.pw_uid)
    os.umask(0o22)
    return True


def root():
    if os.geteuid() != 0:
        return False
    return True


def wait():
    while 1:
        time.sleep(1.0)
