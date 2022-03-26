import random
import time
from ptCrypt.Math import base
from typing import Tuple, Iterator, Iterable, Optional


def privateKeyFactorization(n: int, e: int, d: int, timeout: int = None) -> tuple:
    """Factorization of RSA modulus with known public and private exponents

    Parameters:
        n: int
            RSA modulus
        
        e: int
            RSA public exponent
        
        d: int
            RSA private exponent
        
        timeout: int
            Timeout for factorization in seconds. 
            By default None, so function will run untill it finds a factor of n
    
    Returns:
        result: tuple
            factors p and q of n. Note that function does not guarantee p and q to be prime numbers.
            Function looks for divisor y of n and once such divisor found function returns tuple (y, n // y).
    """

    k = d * e - 1
    start = round(time.time())
    while True:
        if timeout and round(time.time()) - start > timeout: 
            return None
        t = k
        g = random.randint(2, n - 1)
        while t % 2 == 0:
            t = t // 2
            x = pow(g, t, n)
            y = base.gcd(x - 1, n)
            if x > 1 and y > 1:
                return (y, n // y)


def commonModulusAttack(c1: int, c2: int, e1: int, e2: int, n: int) -> int:
    """Common modulus attack on RSA. This attack allows decrypting message without private key, 
    when given same message encrypted with two different public exponents but same modulus.
    Note also, that greatest common divisor of public exponents must be equal to 1.
    Anyway, function calculates m^gcd(e1, e2), so if gcd(e1, e2) == 1 you get the decrypted message
    but if it is not, you get message encrypted with gcd(e1, e2).

    Parameters:
        c1: int
            m^e1 mod n
        
        c2: int
            m^e2 mod n
        
        e1, e2: int
            public exponents
        
        n: int
            common modulus
    
    Returns:
        result: int
            function returns m^gcd(e1, e2), which is just decrypted message if gcd(e1, e2) == 1
    """

    r, v, u = base.egcd(e1, e2)
    if r != 1: return None
    return (pow(c1, v, n) * pow(c2, u, n)) % n


def wienerAttack(n: int, e: int) -> int:
    """Attack on RSA with small private key. 
    This function finds private key using continued fractions by Wiener theorem.
    By the theorem, private key can be efficiently recovered if d < (N^0.25) / 3, but function
    does not check any conditions. If attack fails you will just get None.

    Parameters:
        n: int
            RSA modulus
        
        e: int
            RSA public exponent
    
    Returns:
        d: int
            RSA private exponent, or None if attack fails.
    """

    coeffs = base.continuedFraction(e, n)
    convergents = base.getConvergents(coeffs)

    for k, d in convergents:
        if not k: continue
        if (e * d - 1) % k: continue

        phi = (e * d - 1) // k

        b = n - phi + 1
        D = b ** 2 - 4 * n
        root = base.iroot(2, D)
        if root * root == D:
            
            x1 = (-b - root) // 2
            x2 = (-b + root) // 2
            if x1 * x2 == n: return d


def hastadAttack(ciphertexts: list, modules: list, e: int) -> int:
    """Hastad attack on RSA with small public key via Chinese remainder theorem.
    This attack works effectively for extremely small public keys (3, 7, 11) and
    takes exponentially more time with larger keys.

    Parameters:
        ciphertexts: list
            list of encrypted messages
        
        modules: list
            list of RSA modules
        
        e: int
            public key used for encryption
    
    Returns:
        message: int
            Decrypted message, or None if ciphertexts length is not equal to modules length 
            or e is larger than ciphertexts length
    """

    if len(ciphertexts) != len(modules): return None
    if e > len(ciphertexts): return None

    message = base.crt(ciphertexts[:e], modules[:e])
    return base.iroot(e, message)

