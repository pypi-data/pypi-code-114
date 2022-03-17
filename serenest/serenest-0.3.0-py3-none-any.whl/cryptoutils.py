#!/usr/bin/env python3

import math
import random
import gmpy2

def nth_root(root_me, root):
    """
    calculates the cubic root of a large number
    """
    as_mpz = gmpy2.mpz(root_me)
    result, exact = gmpy2.iroot(as_mpz, root)
    if exact:
        return int(result)
    return str(root_me) + " cannot be rooted to an exact integer"

def gcd(a,b):
    """
    Math already provides an implementation, no need to reinvent the wheel
    """
    return math.gcd(a,b)

def xgcd(a,b):
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a%b
    return a, prevx, prevy

def modinverse(a, modulo):
    if (a == 0):
        return 0
    gcd, inverse, _ = xgcd(a, modulo)
    if (gcd != 1):
        return str(a) + " doesn't have an inverse mod " + str(modulo)
    if (inverse < 0):
        inverse += modulo
    return inverse


def legendre(a, prime):
    """
    Determines whether a is a quadratic residue modulo prime
    In other words, makes sure a has a square root mod prime
    """
    if not(is_prime(prime)):
        return "the second argument is a composite"
    if (a == 0):
        return 0
    return pow(a, (prime-1)//2, prime)

def is_prime(candidate):
    """
    Just an alias for Rabin-Miller
    """
    return rabin_miller(candidate)

def rabin_miller(candidate, number_of_rounds = 100):
    """
    see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test for details
    Returns False if the number is found to be a composite;
    Returns True if the number is likely to be a prime.
    The higher the number of rounds, the more accurate the test will be.
    """
    if (candidate == 2 or candidate == 3 or candidate == 5 or candidate == 7):
        return True
    if (candidate % 2 == 0 or candidate % 3 == 0 or candidate % 5 == 0 or candidate % 7 == 0):
        return False
    r, s = 0, candidate - 1
    while s%2 == 0:
        r += 1
        s //= 2
    for _ in range(number_of_rounds):
        random_integer = random.randrange(2, candidate - 1)
        x = pow(random_integer, s, candidate)
        if (x == 1 or x == candidate - 1):
            continue
        for _ in range(r-1):
            x = pow(x, 2, candidate)
            if (x == candidate-1):
                break
        else:
            return False
    return True

def crt(remainders, modulos):
    """
    expects two lists: a list of remainders, and a list of coprime modulos
    [1, 2, 3], [5, 7, 8] will be interpreted as:
    
        x = 1 (mod 5)
        x = 2 (mod 7)
        x = 3 (mod 8)
    
    Returns (the value of x mod the product of all modulos, product of all modulos)
    """

    assert len(remainders) == len(modulos)

    x, mod = remainders[0], modulos[0]

    for i in range(1, len(modulos)):
        y = ((remainders[i]-x) * modinverse(mod, modulos[i])) % modulos[i]
        x, mod = y*mod + x, mod * modulos[i]

    return (x, mod)










