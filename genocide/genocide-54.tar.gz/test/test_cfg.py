# This file is placed in the Public Domain.


"config"


import unittest


from genocide.function import edit
from genocide.kernel import Cfg
from genocide.object import Object, update
from genocide.parse import parse


class Test_Cfg(unittest.TestCase):

    def test_parse(self):
        p = Cfg()
        parse(p, "mod=irc")
        self.assertEqual(p.sets.mod, "irc")

    def test_parse2(self):
        p = Cfg()
        parse(p, "mod=irc,rss")
        self.assertEqual(p.sets.mod, "irc,rss")

    def test_edit(self):
        d = Object()
        update(d, {"mod": "irc,rss"})
        edit(Cfg, d)
        self.assertEqual(Cfg.mod, "irc,rss")
