from typing import List

class Program:
    SIZE = 32

    def __init__(self, codes, qid: int, autopad=False):
        ncodes = len(codes)

        if ncodes < 2:
            raise ValueError("Programs must contain at least an output and an input.")

        if ncodes != Program.SIZE:
            if autopad and ncodes < Program.SIZE:
                codes += [0] * (Program.SIZE - len(codes))
            else:
                raise ValueError(f"Programs must be created with exactly {Program.SIZE} codes")

        self._codes = list(codes)
        self.qid = qid
        self.data = {}


    def __iter__(self):
        return iter(self._codes[0:len(self)])

    def __getitem__(self, ix):
        return self._codes[ix]

    def __len__(self):
        return self.find_end(0)

    def arity_at(self, ix):
        if ix == 0:
            return 1

        arity = self._codes[ix] // 1000
        if arity >= 10:
            arity = 0
        return arity

    def find_end(self, ix):
        l = 1
        while True:
            if ix >= Program.SIZE:
                # Invalid program
                return 0

            a = self.arity_at(ix)
            l += a - 1
            ix += 1

            if l == 0:
                return ix

    def find_parent(self, ix: int) -> int:
        """Find the parent of the opcode at ix."""
        depths = self.depths()
        code_depth = depths[ix]
        while ix > 0:
            ix -= 1
            d = depths[ix]
            if d < code_depth:
                break
        return ix

    def depths(self) -> List[int]:
        """Get the depths of each element in the program."""
        res = [-1] * len(self)

        # By convention the root of the program is at depth 1.
        # This leaves space for an output node at depth 0
        res[0] = 0
        for ix, _ in enumerate(self):
            arity = self.arity_at(ix)
            d = res[ix]
            if arity >= 1:
                res[ix+1] = d+1
            if arity == 2:
                c2 = self.find_end(ix+1)
                res[c2] = d+1
        return res

    def copy(self) -> "Program":
        copy = Program(self._codes[:], self.qid)
        copy.data = self.data.copy()

        return copy

    def __hash__(self):
        # Convert the codes anctually in use to a tuple
        t = tuple([self.qid] + self._codes[0 : len(self)])

        # Use buildin hash for tuples
        return hash(t)

    def __repr__(self):
        return "<P " + repr(self._codes) + ">"

    @staticmethod
    def from_json(json):
        p = Program(json["codes"], qid=json["qid"])
        p.data = json["data"]
        return p

    def to_json(self):
        return {"codes": self._codes, "data": self.data, "qid": self.qid}
