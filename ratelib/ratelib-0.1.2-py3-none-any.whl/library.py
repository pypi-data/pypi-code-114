from .rate import Rate, RateFilter
from .nucleus import MetaStableError

from collections import OrderedDict


class Library:
    def __init__(self, path=None):
        self._rates = OrderedDict()
        if path is not None:
            self.load(path)

    def load(self, rlib_file: str):
        with open(rlib_file, "r") as fd:
            line_num = 0
            while True:
                lines = [fd.readline()]
                line_num += 1
                if not lines[0]:
                    break
                for i in range(3):
                    lines.append(fd.readline())
                    line_num += 1
                    if not lines[-1]:
                        msg = f"Unexpected EOF at {rlib_file}:{line_num}"
                        raise ValueError(msg)
                r = Rate()
                try:
                    r.init_by_lines(lines)
                except MetaStableError:
                    # Ignore meta stable entries
                    continue
                self.add_rate(r)

    @property
    def rates(self):
        return [r for i, r in self._rates.items()]

    def add_rate(self, r: Rate):
        r_id = hash(r)
        if r_id in self._rates:
            msg = "Rate '{}' already exists in library.".format(r)
            raise ValueError(msg)
        self._rates[r_id] = r

    def pop_rate(self, r: Rate):
        r_id = hash(r)
        if r_id not in self._rates:
            msg = "Rate '{}' does not exist in library.".format(r)
            raise ValueError(msg)
        return self._rates.pop(r_id)

    def find_rates(self, rate_filter: RateFilter):
        rez = Library()
        for r_id, r in self._rates.items():
            if rate_filter.check_matches(r):
                rez.add_rate(r)
        return rez

    def save(self, rlib_file):
        with open(rlib_file, "w") as fd:
            for rate in sorted(self.rates):
                for line in rate.reaclib_format():
                    fd.write(line)
