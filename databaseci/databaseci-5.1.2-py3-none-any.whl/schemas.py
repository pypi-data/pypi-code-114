from schemainspect import get_inspector


def get_inspected(t):
    return get_inspector(t.c)


class Schemas:
    def inspect(self):
        with self._t_namedtuple() as t:
            i = get_inspected(t)

        return i
