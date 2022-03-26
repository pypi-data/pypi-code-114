import ptCrypt.Math.base as base


class Curve:

    class Point:

        ZERO = 'O'

        def __init__(self, curve, x, y):
            self.curve = curve
            self.x = x
            self.y = y

        def __add__(self, other):
            assert self.curve == other.curve

            if self.x == 'O':
                return other
            if other.x == 'O':
                return self

            if self == -other:
                return self.curve.point('O', 'O')

            l = 0
            if self != other:
                low = other.x - self.x

                if self.curve.p:
                    low = low % self.curve.p
                    r, a, b = base.egcd(low, self.curve.p)

                    if r != 1: return r

                    l = (other.y - self.y) * a % self.curve.p
                else:
                    l = (other.y - self.y) / low
            else:
                low = 2 * self.y

                if self.curve.p:
                    low = low % self.curve.p

                    r, a, b = base.egcd(low % self.curve.p, self.curve.p)
                    if r != 1: return r

                    l = (3 * pow(self.x, 2) + self.curve.a) * a % self.curve.p
                else:
                    l = (3 * pow(self.x, 2) + self.curve.a) / (2 * self.y)

            x3 = pow(l, 2) - self.x - other.x
            y3 = l * (self.x - x3) - self.y

            if self.curve.p:
                x3 = x3 % self.curve.p
                y3 = y3 % self.curve.p

            return self.curve.point(x3, y3)

        def __sub__(self, other):
            return self + (-other)

        def __neg__(self):
            return self.curve.point(self.x, -self.y)

        def __repr__(self):
            return f"({self.x}, {self.y})"

        def __eq__(self, other):
            return self.curve == other.curve and self.x == other.x and self.y == other.y

        def __mul__(self, number):
            Q = self
            R = self.curve.point(Curve.Point.ZERO, Curve.Point.ZERO)
            n = number
            while n > 0:
                if n % 2:
                    R = R + Q
                    if type(R) is int:
                        return R
                Q = Q + Q
                if type(Q) is int:
                    return Q
                n = n >> 1
            return R

        def __rmul__(self, number):
            return self * number

    def __init__(self, a, b, p=None):

        self.a = a
        self.b = b
        self.p = p

        if self.hasSingularPoints():
            print(f"[WARNING] Curve {self} has singular points")

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.p == other.p

    def __repr__(self):
        res = "x^3"
        if self.a >= 0:
            res += f"+{self.a}x"
        else:
            res += f"{self.a}x"

        if self.b >= 0:
            res += f"+{self.b}"
        else:
            res += f"{self.b}"

        if self.p:
            return res + f" over F({self.p})"
        else:
            return res

    def point(self, x, y):
        return Curve.Point(self, x, y)

    def hasSingularPoints(self):
        return 4 * pow(self.a, 3) + 27 * pow(self.b, 2) == 0
