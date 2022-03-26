import secrets


def gcd(n: int, m: int) -> int:
    """Euklidean algorithm. Finds greatest common divisor of n and m

    Parameters:
        n: int
            first number
        m: int
            second number

    Returns: 
        result: int
            greatest common divisor of n and m.
    """

    if not n:
        return m
    if not m:
        return n

    while n:
        n, m = m % n, n
    return m


def egcd(n: int, m: int) -> dict:
    """Extended Euklidean algorithm. Finds greatest common divisor of n and m

    Parameters:
        n: int
            first number
        m: int
            second number

    Returns: 
        result: tuple
            tuple of values (reminder, a, b), where
            reminder: int
                greatest common divisor
            a, b: int
                answers to equation an + bm = reminder
    """

    a, a_ = 0, 1
    b, b_ = 1, 0

    c, d = n, m

    q = c // d
    r = c % d
    while r:
        c, d = d, r
        a_, a = a, a_ - q * a
        b_, b = b, b_ - q * b

        q = c // d
        r = c % d

    return (d, a, b)


def isPerfectSquare(p: int) -> bool:
    """Checks if given number is a perfect square. 
    A perfect square is an integer that is a square of another integer.

    Parameters:
        p: int
            number to check
    
    Returns:
        result: bool
            True if number is a perfect square
            False if number is not a perfect square
    """
    
    if p <= 1: return False

    x = p // 2
    seen = set([x])
    while x * x != p:
        x = (x + (p // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def jacobiSymbol(a, n):
    """Recursive Jacobi symbol calculation
    Details:
    https://en.wikipedia.org/wiki/Jacobi_symbol

    Algorithm specified in FIPS 186-4, Appendix C.5

    Parameters:
        a: int
            numerator
        
        n: int
            denominator

    Returns:
        result: int
            returns Jacobi symbol (-1; 0; 1) or None, if 
            Jacobi symbol is not defined (for even and negative numbers)
    """

    if n <= 0 or n % 2 == 0: return None

    # Steps 1, 2 and 3
    a = a % n
    if a == 1 or n == 1: return 1
    if a == 0: return 0

    # Step 4
    e = 0
    a1 = a
    while a1 % 2 == 0:
        a1 >>= 1
        e += 1

    # Step 5
    if (e & 1) == 0: s = 1
    elif n % 8 in (1, 7): s = 1
    else: s = -1

    # Step 6
    if n % 4 == 3 and a1 % 4 == 3: s = -s

    # Step 7
    n1 = n % a1

    # Step 8
    return s * jacobiSymbol(n1, a1)



def eulersTotient(n: int, factors: list = None) -> int:
    """Function counts the positive integers up to a given integer n that are
    relatively prime to n. More about Euler's function:
    https://en.wikipedia.org/wiki/Euler%27s_totient_function

    Parameters:
        n: int
            number to be processed
        
        factors: list
            list of prime factors of n. If left empty, n is considered to be prime.
            Note, that function will NOT check for primality or try to factorize n

    Returns: 
        result: int
            Euler's totient of given number
    """

    if factors:
        count = {}
        for f in factors:
            count[f] = factors.count(f)
        result = 1
        for f in factors:
            result *= (f ** (count[f] - 1)) * (f - 1)
    else:
        return n - 1

    return result


def iroot(a, b):
    """Function to calculate a-th integer root from b. Example: iroot(2, 4) == 2

    Parameters:
        a: int
            Root power
        
        b: int
            Number to calculate root from
        
    Returns:
        result: int
            Integer a-th root of b
    """

    if b < 2:
        return b
    a1 = a - 1
    c = 1
    d = (a1 * c + b // (c ** a1)) // a
    e = (a1 * d + b // (d ** a1)) // a
    while c not in (d, e):
        c, d, e = d, e, (a1 * e + b // (e ** a1)) // a
    return min(d, e)


def intToBytes(n: int, length: int = 0, byteorder: str = "big") -> bytes:
    """Converts given integer number to bytes object

    Parameters:
        n: int
            number to convert to bytes
        
        byteorder: str
            order of bytes. Big endian by default
    
    Returns:
        result: bytes
            list of bytes of number n
    """

    nSize = (n.bit_length() + 7) // 8
    if nSize > length: return n.to_bytes(nSize, byteorder.lower())
    else: return n.to_bytes(length, byteorder.lower())


def byteLength(n: int) -> int:
    """Returns minimal amount of bytes to write given number

    Parameters:
        n: int

    Returns:
        result: int
            minimal amount of bytes to write n
    """
    return (n.bit_length() + 7) // 8


def bytesToInt(b: bytes, byteorder: str = "big") -> int:
    """Converts given bytes object to integer number

    Parameters:
        b: bytes
            bytes to convert into number
        
        byteorder: str
            order of bytes. Big endian by default
    
    Returns:
        result: int
            bytes converted to int
    """
    return int.from_bytes(b, byteorder)


def pad(data: bytes, size: int, value: int = 0) -> bytes:
    """Padds given data with given value until its length is not multiple by size

    Parameters:
        data: bytes
            Data to pad
        
        size: int
            Required size data length must be multiple to

        value: int
            Value to add to data. 0 by default
    """
    value = (value & 0xff)
    while len(data) % size:
        data += bytes([value])
    return data


def partition(b: bytes, length: int) -> list:
    """Partitions given byte string into list of byte strings of requested length

    Parameters:
        b: bytes
            byte string to partition
        
        length: int
            required part length
    
    Returns:
        result: list
            list of byte strings with required length or less
    """

    partsCount = len(b) // length
    if len(b) % length: partsCount += 1

    result = []
    for i in range(partsCount):
        if i * length + length > len(b): result.append(b[i * length:])
        else: result.append(b[i * length:i * length + length])
    return result


def xor(a: bytes, b: bytes, repeat: bool = False) -> bytes:
    """XORs two byte strings

    Parameters:
        a, b: bytes
            byte strings to XOR
        
    Returns:
        result: bytes
            XOR result
    """

    if repeat: iterations = max(len(a), len(b))
    else: iterations = min(len(a), len(b))

    result = b""
    for i in range(iterations):
        result += bytes([a[i % len(a)] ^ b[i % len(b)]])
    
    return result


def getRandomBytes(count: int, exclude: set = set()) -> bytes:
    """Returns random byte string with required length
    Bytes are generated with secrets module, so returned value should be
    appropriate for cryptographic usage.

    Parameters:
        count: int
            required length

        exclude: set
            set of int values, that must not appear in generated string

    Returns:
        result: bytes
            generated byte string
    """

    result = b""
    while len(result) != count:
        value = secrets.randbits(8)
        if value not in exclude:
            result += intToBytes(secrets.randbits(8))
    return result


def crt(coeffs: list, mods: list) -> int:
    """Chinese remainder theorem implementation for finding X in the system

    X = C1 (mod M1)
    X = C2 (mod M2)
    ...
    X = Cn (mod Mn)

    Parameters:
        coeffs: int
            list of parameters C1, C2,..., Cn
        
        mods: int
            list of modules M1, M2, ..., Mn
    
    Returns:
        result: int
            value of X such that X = C1 (mod M1), X = C2 (mod M2),..., X = Cn (mod Mn)

            The function may return None if either coeffs or mods (or both) is empty, 
            or if there is two modules M1 and M2 in modules such that gcd(M1, M2) != 1
    """

    count = min(len(coeffs), len(mods))
    if count == 0: return None

    currX = coeffs[0]
    currMod = mods[0]

    for i in range(1, count):
        newMod = mods[i]
        if gcd(currMod, newMod) != 1: return None

        y = (coeffs[i] - currX) % newMod
        inv = egcd(currMod, newMod)[1]
        y = (inv * y) % newMod

        currX = currX + currMod * y
        currMod *= newMod
    
    return currX % currMod


def getGenerator(p: int, q: int, seed: int = 2, update: callable = lambda x: x + 1) -> int:
    """For given two primes p and q such that q | (p - 1), 
    this function generates generator g of subgroup of order q in the finite group modulo p. 
    This function might be useful for implementing FFC, although there might be ananlogues
    of this function for a particular algorithm. For example, for DSA there are two appropriate functions
    in Asymmetric.DSA module.

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
    
        seed: int
            Initial seed. 2 by default
        
        update: callable
            seed update function. 
            If current seed turned out to be inappropriate this function should generate new seed given the old one
            By default it returns seed + 1
    
    Returns:
        result: int
            Generator of subgroup of order q modulo p.
    """

    e = (p - 1) // q
    while 1:
        g = pow(seed, e, p)
        if g != 1: break

        seed = update(seed)
    
    return g


def getPrimitiveRoot(p: int, factors: list) -> int:
    """Generates smallest primitive root modulo prime number p

    Parameters:
        p: int
            Modulo value
        
        factors: list
            List of prime divisors of value (p - 1)
    """
    seed = 2
    while True:
        if pow(seed, p - 1, p) != 1:
            seed += 1
        
        isGenerator = True
        for factor in factors:
            if pow(seed, factor, p) == 1:
                isGenerator = False
                break
        if isGenerator: return seed
        
        seed += 1


def continuedFraction(a: int, b: int, count: int = None) -> list:
    """Calculates continued fraction representation of rational number a / b

    Details: https://en.wikipedia.org/wiki/Continued_fraction

    Parameters:
        a: int
            nomiator of a rational number

        b: int
            denominator of a rational number
        
        count: int
            required count of coefficients to calculate. 
            By default None, so funcion will calculate all coefficients
    
    Returns:
        result: list
            list of coefficients of continued fractions representation: [a0, a1, a2,...]
    """

    res = []
    q = a // b
    r = a % b
    res.append(q)

    while r != 0:
        a, b = b, r
        q = a // b
        r = a % b
        res.append(q)
        if count and len(res) >= count:
            return res

    return res


def getConvergents(coeffs: list) -> list:
    """Calculates convergents of the continued fraction

    Details: https://en.wikipedia.org/wiki/Continued_fraction

    Parameters:
        coeffs: list
            coefficients of continued fractions
    
    Returns:
        result: list
            list of tuples (nominator, denominator) of continued fraction's convergents
    """

    convergents = []
    for i in range(len(coeffs)):
        if i == 0:
            n = coeffs[0]
            d = 1
        elif i == 1:
            n = coeffs[0] * coeffs[1] + 1
            d = coeffs[1]
        else:
            n = coeffs[i] * convergents[i - 1][0] + convergents[i - 2][0]
            d = coeffs[i] * convergents[i - 1][1] + convergents[i - 2][1]
        
        convergents.append((n, d))
    return convergents