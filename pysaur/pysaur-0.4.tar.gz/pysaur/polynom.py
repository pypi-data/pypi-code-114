'''Даний модуль містить створення найпростіших многочленів, для подальшого їхнього використання у складніших функціях'''

import pysaur.monom as mn
from itertools import groupby
from math import gcd as gc
import math


class plist:
    '''Список для простої побудови поліномів: індекс - показник степеня, значення - коефіцієнт'''
    def __init__(self, *els):

        self.lst = list(*els)

    def __setitem__(self, key, value):
        while True:
            try:
                self.lst[-key - 1] = value
                break
            except IndexError:
                self.lst.insert(0, 0)

    def __len__(self):
        self._delzeroes()
        return len(self.lst)

    def __getitem__(self, item):
        try:
            return self.lst[-item - 1]
        except IndexError:
            return 0

    def _delzeroes(self):
        while self.lst[0] == 0:
            if len(self.lst) == 1:
                break
            self.lst.remove(0)

    def __repr__(self):
        self._delzeroes()
        return str(self.lst)


def polynom(expression):
    '''Перетворення виразів у поліноми'''
    if isinstance(expression, int):
        expression = mn.fr.Fraction(expression)
        return Polynom(mn.Monom(0, expression))
    elif isinstance(expression, float):
        expression = mn.fr.float_to_fraction(str(expression))
        return Polynom(mn.Monom(0, expression))
    elif isinstance(expression, str):
        expression = list(expression)
        while ' ' in expression:
            expression.remove(' ')
        for i in range(len(expression) * 2):
            try:
                if expression[i] == '-' and i != 0:
                    if expression[i - 1] != '+':
                        expression.insert(i, '+')
            except IndexError:
                break
        expression = ''.join(expression)
        expression = expression.split('+')
        for i in range(len(expression)):
            expression[i] = expression[i].split('x')
            for j in range(2):
                try:
                    if expression[i][j] == '':
                        expression[i][j] = 1
                    elif expression[i][j] == '-':
                        expression[i][j] = -1
                    elif '^' in expression[i][j]:
                        expression[i][j] = expression[i][j][1:]
                except IndexError:
                    expression[i].append(0)
        lst = []
        for i in expression:
            lst.append(mn.Monom(int(i[1]), int(i[0])))
        return Polynom(*lst)
    elif isinstance(expression, mn.fr.Fraction):
        return Polynom(mn.Monom(0, expression))
    elif isinstance(expression, mn.Monom):
        return Polynom(expression)
    elif isinstance(expression, plist):
        return Polynom(*[mn.Monom(i, expression[i]) for i in range(len(expression), -1, -1)])
    return expression


class Polynom:
    '''Поліном змінної х - утворений з різних мономів.
    Оператори: додавання, віднімання, множення, цілочисельне ділення, ділення з остачею, остача від ділення,
    піднесення до натурального степеня, перевірка на рівність, модуль (по коефіцієнтам)

    Виводить на екран поліном у вигляді : axⁿ¹ + bxⁿ² ...
    '''
    def __init__(self, *monoms: mn.Monom):
        self.p = [*monoms]
        self.p.sort(key=lambda x: x.power, reverse=True)
        prts = [list(j) for k, j in groupby(self.p, lambda x: x.power)]
        self.parts = []
        for i in prts:
            self.parts.append(sum(i))
        while 0 in self.parts:
            if len(self.parts) == 1:
                break
            self.parts.remove(0)
        self._listed = plist()
        for i in self.parts:
            i = mn.monomize(i)
            self._listed[i.power] = i.coefficient
        self.power = len(self._listed) - 1

    def __len__(self):
        return len(self.parts)

    def __eq__(self, other):
        other = polynom(other)
        return self.parts == other.parts

    def __add__(self, other):
        other = polynom(other)
        return Polynom(*(self.p + other.p))

    def __neg__(self):
        return Polynom(*[-i for i in self.p])

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        other = polynom(other)
        ml = []
        for i in self.parts:
            for j in other.parts:
                ml.append(i*j)
        return Polynom(*ml)

    def __pow__(self, power, modulo=None):
        if power == 0:
            return polynom(1)
        x = Polynom(*self.p)
        a = Polynom(*self.p)
        for i in range(1, power):
            x *= a
        return x

    def __divmod__(self, other):
        other = polynom(other)
        lstpol = plist()
        pl = self._listed
        polpl = polynom(pl)
        while polpl.power >= other.power:
            lstpol[polpl.power - other.power] = mn.fr.Fraction(polpl._listed[polpl.power], other._listed[other.power])
            pol1 = lstpol[polpl.power - other.power]
            polpl -= other * Polynom(mn.Monom(polpl.power - other.power, pol1))
        return polynom(lstpol), polpl

    def __rdivmod__(self, other):
        other = polynom(other)
        return other.__divmod__(self)

    def __rmod__(self, other):
        other = polynom(other)
        return other.__mod__(self)

    def __rfloordiv__(self, other):
        other = polynom(other)
        return other.__floordiv__(self)

    def __floordiv__(self, other):
        if isinstance(other, mn.fr.Fraction) or isinstance(other, int):
            other = mn.fr.fractionize(other)
            return Polynom(*[i / other for i in self.parts])
        if isinstance(other, float):
            other = mn.fr.float_to_fraction(other)
            return Polynom(*[i / other for i in self.parts])
        return self.__divmod__(other)[0]

    def __mod__(self, other):
        return self.__divmod__(other)[1]

    def __rmul__(self, other):
        return self * other

    def __rsub__(self, other):
        other = polynom(other)
        return other.__add__(-self)

    def __radd__(self, other):
        other = polynom(other)
        return Polynom(*(self.p + other.p))

    def __repr__(self):
        vis = []
        for i in range(len(self.parts)):
            if i == 0:
                vis.append(str(self.parts[i]))
            elif self.parts[i].coefficient > 0:
                vis.append(f' + {self.parts[i]}')
            else:
                vis.append(f' - {abs(self.parts[i])}')
        return ''.join(map(str, vis))


def gcdp(a: Polynom, b: Polynom):
    '''Знаходить НСД двох поліномів а та b'''
    minpol = min(a, b, key=lambda pol: pol.power)

    if a == minpol:
        maxpol = b
    else:
        maxpol = a
    while minpol.power:
        r = maxpol % minpol
        if r == 0:
            if all(i.coefficient > 1 and i.coefficient.denominator == 1 for i in minpol.parts):
                minpol //= gc(*[int(i.coefficient) for i in minpol.parts])
            return minpol
        maxpol, minpol = minpol, r
    return 1


def counters(num: int):
    '''Знаходить УСІ дільники числа num'''

    lst = []
    for i in range(1, int(math.sqrt(abs(num))) + 1):
        if num % i == 0:
            lst.append(i)
            lst.append(num // i)
            lst.append(-i)
            lst.append(-num // i)
    return lst


def lcmp(a: Polynom, b: Polynom):
    '''Знаходить НСК двох поліномів а та b'''
    return a * b // gcdp(a, b)


def derivative(pol, n=1):
    '''Знаходить n-ну похідну полінома pol'''
    pol = polynom(pol)
    prts = []
    for i in pol.parts:
        prts.append(i.deriv(n))
    return Polynom(*prts)


def value(pol, arg):
    '''Знаходить значення полінома pol у точці arg'''

    val = 0
    for i in pol.parts:
        val += i.value(arg)
    return val


def from_power(num):
    nm = []
    for i in num:
        nm.append(str(mn.pows.index(i)))
    return int(''.join(nm))


def factor(pol: Polynom, type=int):
    '''Розкладає многочлен на множники, type - тип множників'''
    if type == int:
        lst = []
        while True:
            if 0 in [i.power for i in pol.parts]:
                lcoef = int(pol.parts[-1].coefficient)
                gd = gc(*[int(i.coefficient) for i in pol.parts])
                ld = counters(lcoef)
                if gd not in (0, 1):
                    lst.append(gd)
                    pol //= gd
                for i in ld:
                    if value(pol, i) == 0:
                        if i > 0:
                            if f'(x - {i})' not in lst:
                                lst.append(f'(x - {i})')
                            else:
                                lst.append('')
                                if any(a in mn.pows for a in lst[lst.index(f'(x - {i})') + 1]):
                                    lst[lst.index(f'(x - {i})') + 1] = mn.to_power(from_power(lst[lst.index(f'(x - {i})') + 1]) + 1)
                                else:
                                    lst.insert(lst.index(f'(x - {i})') + 1, mn.to_power(2))
                        else:
                            if f'(x + {-i})' not in lst:
                                lst.append(f'(x + {-i})')
                            else:
                                lst.append('')
                                if any(a in mn.pows for a in lst[lst.index(f'(x + {-i})') + 1]):
                                    lst[lst.index(f'(x + {-i})') + 1] = mn.to_power(
                                        from_power(lst[lst.index(f'(x + {-i})') + 1]) + 1)
                                else:
                                    lst.insert(lst.index(f'(x + {-i})') + 1, mn.to_power(2))
                        pol //= Polynom(mn.Monom(0, -i), mn.Monom(1, 1))
                        break
                else:
                    if pol == 1:
                        break
                    elif len(pol) != 1:
                        lst.append(f'({pol})')
                    else:
                        lst.append(str(pol))
                    break
            else:
                lst.append('x')
                pol //= polynom('x')
        for i in lst:
            if len(str(i)) == 1 and i not in mn.pows and lst.index(i) != 0:
                lst.remove(i)
                lst.insert(0, i)
        return ''.join(map(str, lst))


def integral(pol):
    '''Знаходить невизначений інтеграл полінома pol'''
    pol = polynom(pol)
    prts = []
    for i in pol.parts:
        prts.append(i.integ())
    return Polynom(*prts)


if __name__ == '__main__':
    print(polynom('-x^2-4x-2x-1'))



