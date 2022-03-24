'''
ENG
    pysaur.math module, beta 0.4.

    What's new in beta 0.4: implementation of polynomials of variable x with coefficients - rational (integer) fractions, stable version

    Classes:
        plist: List for simple construction of polynomials: index - exponent, value - coefficient
        Fraction: Rational (integer) fraction in a/b format, where gcd(a, b) == 1
        Monom: A monomial of a variable x in the format: power, coefficient
        Polynom: A polynomial of the variable x - formed from different monomials

    Functions:
        polynom (expression): Converts an expression to a polynomial
        gcd (a, b): Finds the gcd of two polynomials a and b
        lcm (a, b): Finds the lcm of two polynomials a and b
        derivative (pol, n): Finds the nth derivative of the polynomial pol (by default the first)
        integral (pol): Finds the indefinite integral of the polynomial pol
        value (pol, arg): Finds the value of the polynomial pol at the point arg
        factor(pol): Factoring polynom pol to integer binomials (if exists)


UKR
    Модуль pysaur.math бета-версії 0.4.

    Що нового в версії 0.4: реалізація поліномів змінної х з коефіцієнтами - раціональними (цілочисельними) дробами, стабільна версія

    Класи:
        plist:  Список для простої побудови поліномів: індекс - показник степеня, значення - коефіцієнт
        Fraction:  Раціональний (цілочисельний) дріб у форматі a/b, де НСД(a, b) == 1
        Monom:  Одночлен (моном) змінної х у форматі: степінь, коефіціент
        Polynom: Поліном змінної х - утворений з різних мономів

    Функції:
        polynom(expression):  Перетворення виразу expression у поліном
        gcd(a, b): Знаходить НСД двох поліномів а та b
        lcm(a, b): Знаходить НСК двох поліномів а та b
        derivative(pol, n): Знаходить n-ну похідну полінома pol (за замовчуванням першу)
        integral(pol): Знаходить невизначений інтеграл полінома pol
        value(pol, arg): Знаходить значення полінома pol у точці arg
        factor(pol): Розклад на цілі множники-двочлени полінома pol (якщо такий існує)


'''

from .polynom import *
from .monom import *
from .fraction import *
if __name__ == '__main__':
    a = plist()
    a[6] = 1
    print(polynom(a))