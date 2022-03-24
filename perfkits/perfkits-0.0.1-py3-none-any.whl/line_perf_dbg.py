import time
import bdb
import linecache


class LinePerfDbg(bdb.Bdb):
    def __init__(self, *sub, **kwargs):
        self._timer = kwargs.pop('timer', None) or time.perf_counter
        bdb.Bdb.__init__(self, *sub, **kwargs)
        self.clear()

    def clear(self):
        self._stats = {}
        self._last_time = None
        self._last_lineno = None
        self._last_code = None

    def _record_stats(self, time_value):
        if self._last_lineno is not None:
            code = self._last_code
            lineno = self._last_lineno
            if not code in self._stats:
                self._stats[code] = {}
            if lineno not in self._stats[code]:
                self._stats[code][lineno] = [0.0, 0]
            self._stats[code][lineno][0] += time_value - self._last_time
            self._stats[code][lineno][1] += 1

    def user_call(self, frame, argument_list):
        self.set_return(frame)

    def user_line(self, frame):
        t = self._timer()
        self._record_stats(t)
        self._last_time = t
        self._last_code = frame.f_code
        self._last_lineno = frame.f_lineno

    def gen_stats(self):
        ret = {}
        for code, stats in self._stats.items():
            filename = self.canonic(code.co_filename)
            ret[filename] = {
                'name': code.co_name,
                'stats': []
            }
            for lineno, values in sorted(stats.items(), key=lambda x: x[0]):
                line = linecache.getline(filename, lineno)
                ret[filename]['stats'].append([line.rstrip('\n'), *values])
        return ret

    def print_stats(self, stats):
        for filename, info in stats.items():
            print("%s in %s:" % (info['name'], filename))
            for entry in info['stats']:
                print('\t'.join(str(i) for i in entry))

    def runcall(self, func, *args, **kwargs):
        ret = bdb.Bdb.runcall(self, func, *args, **kwargs)
        t = self._timer()
        self._record_stats(t)
        return ret
