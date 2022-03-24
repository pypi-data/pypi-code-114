'''Даний модуль містить створення найпростіших одночленів, для подальшого їхнього використання у складніших функціях'''
import pysaur.fraction as fr
pows = list('⁰¹²³⁴⁵⁶⁷⁸⁹')


def to_power(number: int):
    nm = []
    number = str(number)
    for i in number:
        nm.append(pows[int(i)])
    return ''.join(nm)


def monomize(num): # створення одночлену з числа
    if isinstance(num, int):
        num = fr.Fraction(num)
        return Monom(0, num)
    elif isinstance(num, float):
        num = fr.float_to_fraction(str(num))
        return Monom(0, num)
    elif isinstance(num, fr.Fraction):
        return Monom(0, num)
    return num


class Monom:
    '''Одночлен змінної х у форматі: степінь, коефіціент
    Оператори: додавання, віднімання, множення, піднесення до натурального степеня, перевірка на рівність,
    модуль (по коефіцієнтам)

    Методи:
        value(arg) - значення монома у точці arg
        deriv(n) - n-на похідна монома (за замовчуванням перша)
        integ() - невизначений інтеграл монома

    Виводить на екран одночлен у вигляді : axⁿ
    '''
    def __init__(self, power, coefficient):  # power - степінь, coefficient - коефіцієнт при степені
        self.power = power
        if not (isinstance(coefficient, float) or isinstance(coefficient, str)):
            self.coefficient = fr.fractionize(coefficient)
        else:
            self.coefficient = fr.float_to_fraction(str(coefficient))
        if self.coefficient == 0:
            self.power = 0

    def deriv(self, n=1):
        if n == 0:
            return self
        elif n == 1:
            return Monom(self.power - 1, self.coefficient * self.power)
        return self.deriv(n-1).deriv()

    def integ(self):
        return Monom(self.power + 1, self.coefficient / (self.power + 1))

    def __neg__(self):
        return Monom(self.power, -self.coefficient)

    def __abs__(self):
        return Monom(self.power, abs(self.coefficient))

    def __mul__(self, other): # множення одночленів
        other = monomize(other)
        return Monom(self.power + other.power, self.coefficient * other.coefficient)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        other = monomize(other)
        return self.power == other.power and self.coefficient == other.coefficient

    def __radd__(self, other):
        if other == 0:
            return self
        elif self == 0:
            return other
        other = monomize(other)
        return other.__add__(self)

    def __add__(self, other):  # додавання одночленів (лише з однаковим степенем!!!)
        if other == 0:
            return self
        elif self == 0:
            return other
        other = monomize(other)
        assert self.power == other.power
        return Monom(self.power, self.coefficient + other.coefficient)

    def __sub__(self, other): # віднімання одночленів (лише з однаковим степенем!!!)
        return self + (-other)

    def __rsub__(self, other):
        other = monomize(other)
        return -self.__radd__(other)

    def __truediv__(self, other):
        other = monomize(other)
        return Monom(self.power - other.power, self.coefficient / other.coefficient)

    def value(self, arg):
        if isinstance(arg, int) or isinstance(arg, fr.Fraction):
            arg = fr.fractionize(arg)
        elif isinstance(arg, float):
            arg = fr.float_to_fraction(arg)
        if self.power == 0:
            return self.coefficient
        return self.coefficient * arg ** self.power

    def __rtruediv__(self, other):
        other = monomize(other)
        return other / self

    def __pow__(self, power, modulo=None):
        x = Monom(self.power, self.coefficient)
        a = Monom(self.power, self.coefficient)
        for i in range(1, power):
            x *= a
        return x

    def __repr__(self):  # вивід одночлену на екран
        if self.power >= 0:
            if self.coefficient == 0:
                return '0'
            elif self.coefficient.denominator == 1:
                if self.power not in (0, 1):
                    if abs(self.coefficient) != 1:
                        return f'{self.coefficient}x{to_power(self.power)}'
                    elif self.coefficient == 1:
                        return f'x{to_power(self.power)}'
                    else:
                        return f'-x{to_power(self.power)}'
                elif self.power == 1:
                    if self.coefficient == 1:
                        return 'x'
                    elif self.coefficient == -1:
                        return '-x'
                    else:
                        return f'{self.coefficient}x'
                else:
                    return str(self.coefficient)
            else:
                if self.power not in (0, 1):
                    if abs(self.coefficient.numerator) != 1:
                        return f'{self.coefficient.numerator}x{to_power(self.power)}/{self.coefficient.denominator}'
                    elif self.coefficient.numerator == 1:
                        return f'x{to_power(self.power)}/{self.coefficient.denominator}'
                    else:
                        return f'-x{to_power(self.power)}/{self.coefficient.denominator}'
                elif self.power == 1:
                    if abs(self.coefficient.numerator) != 1:
                        return f'{self.coefficient.numerator}x/{self.coefficient.denominator}'
                    elif self.coefficient.numerator == 1:
                        return f'x/{self.coefficient.denominator}'
                    else:
                        return f'-x/{self.coefficient.denominator}'
                else:
                    return str(self.coefficient)
        else:
            if abs(self.coefficient) == 1:
                if self.power != -1:
                    if self.coefficient == 1:
                        return f'1/x{to_power(abs(self.power))}'
                    else:
                        return f'-1/x{to_power(abs(self.power))}'
                elif self.power == -1:
                    if self.coefficient == 1:
                        return '1/x'
                    else:
                        return '-1/x'
            elif self.coefficient.denominator == 1:
                if self.power != -1:
                    return f'{self.coefficient}/x{to_power(abs(self.power))}'
                else:
                    return f'{self.coefficient}/x'
            else:
                if self.power != -1:
                    return f'{self.coefficient.numerator}/({self.coefficient.denominator}x{to_power(abs(self.power))})'
                else:
                    return f'{self.coefficient.numerator}/({self.coefficient.denominator}x)'


def sgn(a):
    return fr._sgn(a.coefficient) if a.coefficient != 0 else 0


if __name__ == '__main__':
    a = Monom(2, 2)
    b = Monom(3, 6)
    print(a)
    print(b)

