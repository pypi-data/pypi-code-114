'''Модуль для роботи з цілочисельними та десятковими періодичними дробами'''

import math as mt


def fractionize(num):
    if isinstance(num, int):
        return Fraction(num, 1)
    elif isinstance(num, float):
        return float_to_fraction(num)
    elif isinstance(num, str):
        return float_to_fraction(num)
    return num


def _sgn(num):
    return num // abs(num) if num != 0 else 0


def float_to_fraction(number): # числа виду 0.(6), 1.1(21) (в дужках - період)
    '''Перетворює десятковий кінцевий та періодичний дріб у звичайний (числа виду 0.(6), 1.1(21) (в дужках - період)).
    На вході - строка або число типу int або float. На виході - екземпляр класу Fraction.
    '''
    number = str(number)
    if '.' in number:
        prts = number.split('.')
        int_part = int(prts[0])
        if '(' in number:
            fl_part = (prts[1].split('(')[0])
            period = prts[1].split('(')[1][:-1]
            lf = len(fl_part) + len(period)
            lp = len(period)
            fl = int(fl_part + period)
            if fl_part == '':
                fl_part = 0
            else:
                fl_part = int(fl_part)

        else:
            fl_part = prts[1]
            period = '0'

            lf = len(fl_part) + 1
            lp = 1
            fl = int(fl_part + period)
            fl_part = int(fl_part)
    else:
        int_part = int(number)
        fl = 0
        fl_part = 0
        lf = 0
        lp = 0
        denom = 1
    try:
        denom = int('9' * lp + '0' * (lf - lp))
    except:
        denom = 1
    return Fraction(int_part, 1) + Fraction(fl - fl_part, denom)


class Fraction:
    '''Раціональний (цілочисельний) дріб у форматі a/b, де НСД(a, b) == 1'''
    def __init__(self, num1, num2=1):
        if isinstance(num1, Fraction):
            num2 = fractionize(num2)
        elif isinstance(num2, Fraction):
            num1 = fractionize(num1)
        while True:
            if isinstance(num1, Fraction) and isinstance(num2, Fraction):
                num1, num2 = num1.numerator * num2.denominator, num1.denominator * num2.numerator
            elif isinstance(num1, Fraction):
                num1, num2 = num1.numerator, num1.denominator * num2
            elif isinstance(num2, Fraction):
                num1, num2 = num1 * num2.denominator, num2.numerator
            else:
                break
        assert num2 != 0
        if _sgn(num1) != _sgn(num2):
            num1 = -abs(num1)
            num2 = abs(num2)
        else:
            num1 = abs(num1)
            num2 = abs(num2)
        self.numerator = num1 // mt.gcd(num1, num2)
        self.denominator = num2 // mt.gcd(num1, num2)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __ge__(self, other):
        other = fractionize(other)
        return self > other or self == other

    def __le__(self, other):
        other = fractionize(other)
        return self < other or self == other

    def __add__(self, other):
        other = fractionize(other)
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __radd__(self, other):
        other = fractionize(other)
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return self + (-other)

    def __pow__(self, power, modulo=None):
        assert power != 0 or self != 0
        if power == 0:
            return 1
        elif power == 1:
            return self
        a = Fraction(self.numerator, self.denominator)
        b = Fraction(self.numerator, self.denominator)
        for i in range(1, power):
            a *= b
        return a

    def __rsub__(self, other):
        other = fractionize(other)
        return other + (-self)

    def __rmul__(self, other):
        other = fractionize(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __mul__(self, other):
        other = fractionize(other)
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    def __truediv__(self, other):
        return self * Fraction(1, other)

    def __rtruediv__(self, other):
        other = fractionize(other)
        return other / self

    def __gt__(self, other):
        other = fractionize(other)
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other):
        other = fractionize(other)
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __eq__(self, other):
        other = fractionize(other)
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator

    def value(self, periodic=False, xn=12):
        if periodic:
            y = int(self.numerator)
            b = int(self.denominator)
            a = int(self.numerator)
            x = y // b
            if float(a / b) == int(a / b):
                n = [f'{x}']
            else:
                n = [f'{x}', '.']
                a1 = y
                b1 = b
                period = []
                xs = []
                aps = []
                while True:
                    a1 = 10 * (a1 % b1)
                    if a1 in aps:
                        fl_part = xs[:aps.index(a1)]
                        for i in xs[aps.index(a1):]:
                            period.append(i)
                        n.append(''.join(map(str, fl_part)))
                        if len(period) != 0 and any(i != 0 for i in period):
                            n.append(f'({"".join(map(str, period))})')
                        break
                    aps.append(a1)
                    x = a1 // b
                    xs.append(x)
            return ''.join(map(str, n))
        y = int(self.numerator)
        b = int(self.denominator)

        x = y // b
        if float(y / b) == int(y / b):
            n = [f'{x}']
        else:
            n = [f'{x}', '.']
            a1 = y
            b1 = b
            for i in range(xn):
                a1 = 10 * (a1 % b1)
                if a1 == 0:
                    break
                x = a1 // b
                n.append(x)
        return ''.join(map(str, n))

    def __repr__(self):
        if self.numerator == 0:
            return '0'
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return f'{self.numerator}/{self.denominator}'


def l_fraction(fraction: Fraction, n: int):
    fraction = fractionize(fraction)
    if n == 1:
        return fraction
    ifr = Fraction(int(fraction))
    return ifr + Fraction((fraction - ifr).numerator, l_fraction(fraction, n - 1))


if __name__ == '__main__':
    print(float_to_fraction('0.1(6)'))
