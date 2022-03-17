#!/usr/bin/env python3

from math import ceil, sqrt
from serenest.cryptoutils import modinverse, is_prime, crt


def bsgs(generator, outcome, p):
    """
    Shanks' babystep-giantstep algorithm
    based on https://en.wikipedia.org/wiki/Baby-step_giant-step
    """
    if not(is_prime(p)):
        return str(p) + " is not a prime"
    
    #since p is prime, order = p-1
    order = p-1
    m = ceil(sqrt(order))
    babysteps = {}
    for i in range(m):
        next_pow = pow(generator, i, p)
        if next_pow in babysteps:
            break
        babysteps[next_pow] = i
    
    #giant steps
    intermediary = pow(modinverse(generator, p), m, p)
    gamma = outcome
    
    for i in range(m):
        if gamma in babysteps.keys():
            return i*m + babysteps[gamma]
        gamma = (gamma * intermediary)%p
    return "Are you sure " + str(generator) + " is a generator for " + str(p) + "?"

def polhig_hellman(generator, order, mod, outcome, factorisation):
    """
    factorisation is expected to be a list of pairs such that each entry is (base,power)
    returns x such that generator^x = outcome
    """
    remainders, modulos = [], []
    for factor in factorisation:
        exponent = pow(factor[0], factor[1])
        generator_i = pow(generator, order//exponent, mod)
        outcome_i = pow(outcome, order//exponent, mod)
        remainder_i = _reduce_prime_power(generator_i, factor[0], factor[1], mod, outcome_i)
        remainders.append(remainder_i)
        modulos.append(exponent)
    return crt(remainders, modulos)[0]


def _reduce_prime_power(generator, order_base, order_power, mod, outcome):
    """
    Returns x such that generator^x = outcome, for generator of order (order_base^order_power)
    based on Hoffstein, Pipher and Silverman, An Introduction to Mathematical Cryptography, 2nd edition
    """
    x = 0
    gen_to_the_power_one_less = pow(generator, pow(order_base, order_power-1, mod), mod) #this has order order_base

    for i in range(order_power):
        g_to_the_x = pow(generator, x, mod)
        h_i_base = (outcome * modinverse(g_to_the_x, mod)) % mod
        h_i = pow(h_i_base, pow(order_base, order_power - 1 - i, mod), mod)
        x_temp = bsgs(gen_to_the_power_one_less, h_i, mod)

        x = x + x_temp * pow(order_base, i, mod)
    return x


