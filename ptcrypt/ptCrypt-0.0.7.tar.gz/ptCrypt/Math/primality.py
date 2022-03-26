import random
from typing import Iterable
from ptCrypt.Math import base, smallPrimes
from ptCrypt.Asymmetric.ECC import Curve
from ptCrypt.Util.keys import FFC_APPROVED_LENGTHS
from datetime import datetime
import hashlib
import secrets


def millerRabin(p: int, t: int) -> bool:
    """Miller-Rabin primality test. Error probability is (1/4)^t
    More about Miller-Rabin test:
    https://en.wikipedia.org/wiki/Miller–Rabin_primality_test

    To get same error probability with better performance consider 
    using less Miller-Rabin tests followed by one Lucas test.
    For example, FIPS 186-4 (DSA standard) recommends switching from 
    64 Miller-Rabin test to 19 Miller-Rabin tests followed by one Lucas 
    test for 160 bit prime q.

    Algorithm also specified in FIPS 186-4, Appendix C.3.1

    Parameters:
        p: int
            number to be tested
        t: int
            count of tests

    Returns: 
        result: bool
            True if the number is prime, else - False
    """
    if p <= 1: return False

    # Step 1. Find largest a such that (p - 1) % 2^a == 0
    k = 1
    b = 0
    while (p - 1) % k == 0:
        b += 1
        k = k << 1
    k = k >> 1
    b -= 1

    # Step 2. m = (p - 1) / 2^a
    m = (p - 1) // k

    # Step 3. wlen = len(w)
    plen = p.bit_length()

    # Step 4
    for _ in range(t):

        # Steps 4.1 and 4.2
        a = random.getrandbits(plen)
        if a <= 1 or a >= p - 1: continue

        # Step 4.3 and 4.4
        z = pow(a, m, p)
        if z == 1 or z == p - 1: continue

        # Step 4.5
        for _ in range(b - 1):
            # Steps 4.5.1, 4.5.2 and 4.5.3
            z = pow(z, 2, p)
            if z == 1: return False
            if z == p - 1: break

        if z == p - 1: continue

        # Step 4.6
        return False

    # Step 5
    return True


def lucasTest(n: int) -> bool:
    """Lucas pseudoprime primality test. Error probability 4/15
    It is recommended to run Lucas test after  few Miller-Rabin tests.
    Algorithm specified in FIPS 186-4, Appendix C.3.3

    Parameters:
        n: int
            number to be tested
    
    Returns:
        result: bool
            True if number is probably prime
            False if number is definitely composite
    """

    # Step 1
    if n % 2 == 0 or base.isPerfectSquare(n): return False

    # Step 2
    def sequence():
        value = 5
        while True:
            yield value
            if value > 0:
                value += 2
            else:
                value -= 2
            value = -value
    
    for d in sequence():
        s = base.jacobiSymbol(d, n)
        if s == 0: return False
        if s == -1: break

    # Step 3
    K = n + 1

    r = K.bit_length() - 1

    # Step 5
    Ui = 1
    Vi = 1

    Ut = 0
    Vt = 0

    invOfTwo = pow(2, -1, n)

    # Step 6
    for i in range(r - 1, -1, -1):
        # Step 6.1
        Ut = (Ui * Vi) % n

        # Step 6.2
        Vt = (Ui * Ui * d + Vi * Vi) % n
        Vt = (Vt * invOfTwo) % n

        # Step 6.3
        if (K >> i) & 1:
            # Steps 6.3.1 and 6.3.2
            Ui = ((Ut + Vt) * invOfTwo) % n
            Vi = ((Vt + Ut * d) * invOfTwo) % n
        else:
            # Steps 6.3.3 and 6.3.4
            Ui = Ut
            Vi = Vt
    
    # Step 7
    return Ui == 0


def trialDivisionTest(n: int) -> bool:
    """Test for primality by trial division. Unlike Lucas test or Miller-Rabin test, this 
    test is deterministic, but it is extremely slow. You should run this test only for
    small numbers of size around 32-bits.

    Parameters:
        n: int
            Number to check for primality
    
    Returns:
        result: bool
            True if number is definitely prime
            False if number is definitely not prime
    """

    root = base.iroot(2, n)
    if root * root == n: return False

    for prime in smallPrimes.SMALL_PRIMES:
        if n == prime: return True
        if n % prime == 0: return False
        if prime > n: return True
    
    x = smallPrimes.SMALL_PRIMES[-1]
    while x <= root:
        if n % x == 0: return False
        x += 2
    
    return True


def getPrime(n: int, checks: int = 10) -> int:
    """Generates random probable prime number using Miller-Rabin test

    Parameters:
        n: int
            bit length of generated number
            returned number is guaranteed to have this bit length

        checks: int
            count of primality checks to perform

    Returns: 
        result: int
            probable prime number with probability 0.25**(checks)
    """

    while True:
        if n <= 1: return

        num = random.getrandbits(n) | (2 ** (n - 1) + 1)

        def check_small_primes(n):
            for p in smallPrimes.SMALL_PRIMES:
                if n == p: return True
                if n % p == 0: return False
            return True

        if not check_small_primes(num): continue
        if millerRabin(num, checks): return num


def primeFactors(n: int, knownFactors: list = [], info: bool = False, timeout: int = 5) -> list:
    """Naive integer factorization function. Extremely slow.

    The fucntion first checks if the number is prime with 10 Miller-Rabin tests,
    and if it is then function will return list with only this particular number.

    Then, function divides given number by 2, 3, 5, 7, 9 and so on until it reaches
    square root of given number or until numbers is not equal to 1.

    Parameters:
        n: int
            number to be factorized

    Returns: 
        result: list
            all factors of n
    """
    if millerRabin(n, 10): return [n]
    if info: totalTime = datetime.now()

    factors = knownFactors[:]
    try:
        if info: 
            print("Checking small primes")
            start = datetime.now()

        for prime in smallPrimes.SMALL_PRIMES:
            if n <= prime:
                if n != 1: factors.append(n)
                if info: 
                    end = datetime.now()
                    print(f"Factors found in {end - totalTime}")

                return factors

            while n % prime == 0:
                factors.append(prime)
                n = n // prime
        if info: 
            end = datetime.now()
            print(f"Small primes checked in {end - start}")

        if millerRabin(n, 30):
            if info:
                end = datetime.now()
                print(f"Factors found in {end - totalTime}")
            factors.append(n)
            return factors

        if info:
            start = datetime.now()
            print("Trying Lenstra method")

        factor = lenstraFactor(n, timeout=timeout)
        while factor != None:
            while n % factor == 0:
                factors.append(factor)
                n = n // factor
            
            if n == 1:
                if info:
                    end = datetime.now()
                    print(f"Factors found in {end - totalTime}")

            factor = lenstraFactor(n, timeout=timeout)
        
        if info:
            end = datetime.now()
            print(f"Finished Lenstra factorization in {end - start}")
        
        if millerRabin(n, 30):
            if info:
                end = datetime.now()
                print(f"Factors found in {end - totalTime}")
            factors.append(n)
            return factors

        if info:
            print("Trying Pollard p - 1")
            start = datetime.now()

        factor = pollardFactor(n)
        while factor != None:
            while n % factor == 0:
                factors.append(factor)
                n = n // factor
            
            if n == 1:
                if info:
                    end = datetime.now()
                    print(f"Factors found in {end - totalTime}")
                return factors
            factor = pollardFactor(n)

        if info:
            end = datetime.now()
            print(f"Finished Pollard p - 1 in {end - start}")

        if millerRabin(n, 30):
            if info:
                end = datetime.now()
                print(f"Factors found in {end - totalTime}")
            factors.append(n)
            return factors

        if info:
            start = datetime.now()
            print(f"Trying plain division factorization")

        sqRoot = base.iroot(2, n)
        for i in range(smallPrimes.SMALL_PRIMES[-1] + 2, sqRoot, 2):
            while n % i == 0:
                n = n // i
                factors.append(i)
            if n < i: break
        if n > 1:
            factors.append(n)
        
        if info:
            end = datetime.now()
            print(f"Factors found in {end - totalTime}")
        return factors
    except KeyboardInterrupt:
        if info: print("Factorization interrupted. Returning current N and list of factors")
        return (n, factors)


def pollardFactor(n, init=2, bound=2**16, numbers: Iterable = smallPrimes.SMALL_PRIMES):
    """Pollard's p - 1 factorization method. This is a general customizable method.

    More details:
    https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm

    Parameters:
        n: int
            number to be factorized

        init: int
            initial value, 2 by default

        bound:
            smoothness bound, 65536 by default
        
        numbers: Iterable
            numbers that method must use for powers of init value.
            Note, that method doesn't just raise init to some ith power of the given iterable
            but searches for such power of ith number, that this power is greater or equal to smoothness bound.
            This trick generally increases success rate of the method. 
            If None given, list of small primes from smallPrimes module will be used.
            For list of small primes method successfully find factors up to 38 bits long.
    
    Returns:
        result: int
            prime divisor of n or None if algorithm fails
    """
    a = init

    for i in numbers:
        if i <= 1: continue

        power = i
        while power < bound: power *= i

        a = pow(a, power, n)
        d = base.gcd(a - 1, n)
        if d > 1 and d < n: return d
        if d == n: return None
    return None


def shaweTaylor(length: int, inputSeed: int, hashFunction: callable=hashlib.sha256) -> dict:
    """Shawe-Taylor random prime generation routine. Generated number is definitely prime.
    The algorithm is slow, but will with great chance work faster than getPrime function 
    up to 512 bit numbers.

    Algorithm specified by FIPS 186-4, Appendix C.6

    Parameters:
        length: int
            the length of the prime to be generated
        
        inputSeed: int
            the seed to be used for the generation of the requested prime

        hashFunction: callable
            hash function used during generation. The function must conform to 
            hashlib protocols. By default hashlib.sha256 is used

    Returns:
        dictionary with keys:
            status: bool
                True if generation succeeded
                False if generation failed
            
            prime: int
                generated prime number
            
            primeSeed: int
                a seed determined during generation
            
            primeGenCounter: int
                a counter determined during the generation of the prime
    """

    # Step 1
    if length < 2: return { "status": False, "prime": None, "primeSeed": None, "primeGenCounter": None}

    twoPowLengthMin1 = pow(2, length - 1)

    # Step 2
    if length < 33:

        # Steps 3, 4
        primeSeed = inputSeed
        primeGenCounter = 0

        while True:

            # Hash calculation for step 5
            hashPayload = base.intToBytes(primeSeed)
            hashPayload1 = base.intToBytes(primeSeed + 1)
            h = base.bytesToInt(hashFunction(hashPayload).digest())
            h1 = base.bytesToInt(hashFunction(hashPayload1).digest())

            # Steps 5, 6, 7
            #   c = Hash(primeSeed) ^ Hash(primeSeed + 1)
            c = h ^ h1
            #   c = 2^(length - 1) + (c mod 2^(length - 1))
            c = twoPowLengthMin1 + (c % twoPowLengthMin1)
            #   c = (2 * floor(c / 2)) + 1
            c = (2  * c // 2) + 1

            # Steps 8, 9
            primeGenCounter += 1
            primeSeed += 2

            # Step 10
            if trialDivisionTest(c):
                # Step 11
                return {"status": True, "prime": c, "primeSeed": primeSeed, "primeGenCounter": primeGenCounter}
            
            # Step 12
            if primeGenCounter > 4 * length:
                return {"status": False, "prime": None, "primeSeed": None, "primeGenCounter": None}
    
    # Step 14
    #   smallerLength = ceil(length / 2) + 1
    smallerLength = length // 2 + length % 2 + 1
    recursiveResult = shaweTaylor(smallerLength, inputSeed, hashFunction)

    status = recursiveResult["status"]
    c0 = recursiveResult["prime"]
    primeSeed = recursiveResult["primeSeed"]
    primeGenCounter = recursiveResult["primeGenCounter"]

    # Step 15
    if not status: return {"status": False, "prime": None, "primeSeed": None, "primeGenCounter": None}

    # Steps 16, 17
    outlen = hashFunction().digest_size * 8

    #   iterations = ceil(length / outlen) - 1
    iterations = length // outlen + (length % outlen != 0) - 1

    oldCounter = primeGenCounter

    twoPowOutlen = pow(2, outlen)
    twoPowLengthMin1 = pow(2, length - 1)

    #Step 18
    x = 0

    # Step 19
    for i in range(iterations + 1):
        hashPayload = base.intToBytes(primeSeed + i)
        h = base.bytesToInt(hashFunction(hashPayload).digest())
        x = x + h * pow(twoPowOutlen, i)
    
    # Steps 20, 21, 22
    primeSeed = primeSeed + iterations + 1
    x = twoPowLengthMin1 + (x % twoPowLengthMin1)

    #   t = ceil(x / (2 * c0))
    t = x // (2 * c0) + (x // (2 * c0) != 0)

    while True:
        # Steps 23, 24, 25
        if 2 * c0 + 1 > pow(2, length):
            #   t = ceil(2 ^ (length - 1) / (2 * c0))
            t = twoPowLengthMin1 // (2 * c0) + (twoPowLengthMin1 % (2 * c0) != 0)
    
        c = 2 * t * c0 + 1
        primeGenCounter += 1

        # Step 26
        a = 0

        # Step 27
        for i in range(iterations + 1):
            hashPayload = base.intToBytes(primeSeed + i)
            h = base.bytesToInt(hashFunction(hashPayload).digest())
            a = a + h * pow(twoPowOutlen, i)

        # Steps 28, 29, 30
        primeSeed = primeSeed + iterations + 1
        a = 2 + (a % (c - 3))
        z = pow(a, 2 * t, c)

        # Step 31
        if 1 == base.gcd(z - 1, c) and 1 == pow(z, c0, c):
            return {"status": True, "prime": c, "primeSeed": primeSeed, "primeGenCounter": primeGenCounter}
    
        # Step 32
        if primeGenCounter >= (4 * length + oldCounter):
            return {"status": False, "prime": None, "primeSeed": None, "primeGenCounter": None}

        # Step 33
        t = t + 1


def lenstraFactor(n: int, bound = 2**64, numbers: Iterable = smallPrimes.SMALL_PRIMES[:100], timeout = None) -> int:
    """Lenstra elliptic curve factorization method

    Parameter:
        n: int
            number to be factorized
        
        bound:
            smoothness bound, 65536 by default
        
        numbers: Iterable
            numbers that method must use for multipliers of points.
            Method doesn't just multiply points with some ith number
            but searches for such power of ith number, that this power is 
            greater or equal to smooth bound.
            This trick generlaly increases success rate of the method.
            By default first 100 prime numbers is used.
        
        timeout: int
            factorization timeout in seconds. By default None meaning no timeout.
            Without timeout method never returns until it finds prime divisor of n.
    
    Returns:
        result: int
            prime divisor of n or None if timeout reached
    """

    start = datetime.now()
    curvesCount = 0

    while 1:
        
        curvesCount += 1
        if timeout and (datetime.now() - start).seconds > timeout:
            return None

        a = random.randint(2, n - 1)
        b = random.randint(2, n - 1)
        A = random.randint(2, n - 1)

        B = (pow(b, 2, n) - pow(a, 3, n) - A * a) % n
        g = base.gcd(4 * pow(A, 3) + 27 * pow(B, 2), n)
        if g > 1 and g < n: return g

        curve = Curve.Curve(A, B, n)
        P = curve.point(a, b)
        if curve.hasSingularPoints(): continue

        for number in numbers:
            t = number
            while t < bound: t *= number

            Q = t * P
            if type(Q) is int:
                if Q < n: return Q
                break
            P = Q


def ifcProvablePrime(L: int, e: int, firstSeed: int, N1: int = 1, N2: int = 1, hashFunction: callable = hashlib.sha256) -> tuple:
    """Provable prime construction algorithm specified in FIPS 186-4, Appendix C.10.
    This algorithm is supposed to be used for integer-factorization cryptosystems (RSA), therefore
    L is supposed to be one of IFC_APPROVED_LENGTHS divided by 2.

    Besides the prime itself this algorithm can construct auxiliary primes p1 and p2 with lengths N1 and N2 respectively.
    To find out more about these primes see FIPS 186-4, Appendix B.3.1.

    Parameters:
        L: int
            required bit length for generated prime
        
        e: int
            IFC public exponent. 
            If, for some reason, you use this method for other purposes, set this value to 2 or any other prime number.
        
        firstSeed: int
            seed value for algorithm, this must be either some random value, or the value returned by this function 
            (if used for second prime generation in IF cryptosystems)

        N1: int
            required bit length for first auxiliary prime. 
            Default value is 1, meaning the first auxiliary prime won't be generated.
        
        N2: int
            required bit length for second auxiliary prime.
            Default value is 1, meaning the second auxiliary prime won't be generated.

        hashFunction: callable
            hash function to use for this algorithm. Function must conform to hashlib protocols.
            It is recommended to use one of APPROVED_HASHES. By default hashlib.sha256 is used.
    
    Returns:
        result: tuple
            tuple of values p, p1, p2 and pSeed, where:
                p - generated prime number,
                p1 - first auxiliary prime number
                p2 - second auxiliary prime number
                pSeed - seed value (this is used by IFC keys generation functions to generate the second prime)

            Note, function might return None if passed parameters are wrong, or generation fails. 
            If parameters are fine, then you should try again with new firstSeed value.
    """

    if L % 2: ceilL = L // 2 + 1
    else: ceilL = L // 2

    # Step 1. Check that N1 and N2 are appropriate. 
    # This doesn't check that N1 and N2 are safe. 
    # Check FIPS 186-4, Appendix B.3.1 for requirements to N1 and N2.
    if N1 + N2 > L - ceilL - 4: return None

    # Step 2
    if N1 == 1:
        p1 = 1
        p2Seed = firstSeed
    
    # Step 3
    if N1 >= 2:
        d = shaweTaylor(N1, firstSeed)
        if not d["status"]: return None
        p1 = d["prime"]
        p2Seed = d["primeSeed"]

    # Step 4
    if N2 == 1:
        p2 = 1
        p0Seed = p2Seed
    
    # Step 5
    if N2 >= 2:
        d = shaweTaylor(N2, p2Seed)
        if not d["status"]: return None
        p2 = d["prime"]
        p0Seed = d["primeSeed"]
    
    # Step 6
    d = shaweTaylor(ceilL + 1, p0Seed)
    if not d["status"]: return None

    p0 = d["prime"]
    pSeed = d["primeSeed"]

    outlen = hashFunction().digest_size * 8

    # Steps 7, 8, 9
    iterations = L // outlen
    if L % outlen == 0: iterations -= 1
    pGenCounter = 0
    x = 0

    # Step 10
    for i in range(iterations + 1):
        hashPayload = base.intToBytes(pSeed + i)
        hashResult = hashFunction(hashPayload).digest()
        x += base.bytesToInt(hashResult) * pow(2, i * outlen)
    
    # Steos 11, 12
    pSeed = pSeed + iterations + 1

    # 665857/470832 = 1.41421356237 is a good rational approximation of sqrt(2)
    coeff = pow(2, L - 1) * 665857 // 470832
    modulus = pow(2, L) - coeff
    x = coeff + (x % modulus)

    # Steps 13, 14
    if base.gcd(p0, base.gcd(p1, p2)) != 1: return None
    y = (1 - pow(p0 * p1, -1, p2)) % p2

    # Step 15
    coeff1 = 2 * y * p0 * p1 + x
    coeff2 = 2 * p0 * p1 * p2
    t = coeff1 // coeff2
    if coeff1 % coeff2: t += 1

    while True:

        # Step 16
        if (2 * (t * p2 - y) * p0 * p1 + 1) > pow(2, L):
            coeff1 = 2 * y * p0 * p1 + coeff
            t = coeff1 // coeff2
            if coeff1 % coeff2: t += 1
    
        # Steps 17, 18
        p = 2 * (t * p2 - y) * p0 * p1 + 1
        pGenCounter += 1

        # Step 19
        if base.gcd(p - 1, e) == 1:
            # Step 19.1
            a = 0

            # Step 19.2
            for i in range(iterations + 1):
                hashPayload = base.intToBytes(pSeed + i)
                hashResult = hashFunction(hashPayload).digest()
                a += base.bytesToInt(hashResult) * pow(2, i * outlen)
            
            # Step 19.3, 19.4, 19.5
            pSeed += iterations + 1
            a = 2 + (a % (p - 3))
            z = pow(a, 2 * (t * p2 - y) * p1, p)

            # Step 19.6
            if 1 == base.gcd(z - 1, p) and 1 == pow(z, p0, p): return (p, p1, p2, pSeed)
        
        # Steps 20, 21
        if pGenCounter >= 5 * L: return None
        t += 1


def getFfcPrimes(N: int, L: int) -> tuple:
    """Generates two primes for FFC. Generates provable primes for L <= 512 and probable primes for L > 512

    Parameters:
        N: int
            smaller prime bit length
        
        L: int
            bigger prime bit length
    
    Returns:
        result: tuple
            Returns pair of numbers (q, p) where q divides (p - 1). May return None if generation fails or N >= L.
    """

    if N >= L: return None

    if L <= 512:
        res = None
        tries = 0
        while not res and tries < 1000:
            res = getProvablePrimesForFFC(N, L)
            tries += 1
        return res
    else:
        res = None
        tries = 0
        while not res and tries < 1000:
            res = getProbablePrimesForFfc(N, L)
            tries += 1
        return res

def getProbablePrimesForFfc(N: int, L: int) -> tuple:
    """Generates probable primes p and q by algorithm from
    FIPS 186-4, Appendix A.1.1.2

    This is the simplified version of generation function. It does not perform
    any checks and doesn't allow you to change parameters except for the primes lengths.
    Full version of this method you can find in Asymmetric.DSA.generateProbablePrimes

    Parameters:
        N: int
            Bit length of q - smaller prime
            
        L: int
            Bit length of p - bigger prime
            
        seedLength: int
            Bit length of seed, must not be less than N
            
        hashFunction: callable
            Hash function conforming to hashlib protocols. By default hashlib.sha256 is used
            Hash function output length must not be less than N. 
            By FIPS 186-4 one of APPROVED_HASHES should be used
        
        forceWeak: bool
            Indicates if N and L should be verified to be approved by the standard. False by default.

    Returns:
        result: tuple
            Tuple of generated parameters:
                1. status: bool
                    True if generation was successful and False otherwise
                
                2. p: int
                    Bigger prime
                
                3. q: int
                    Smaller prime
                
                4. domainParameterSeed: int
                    Seed for for primes verification
                
                5. counter: int
                    Counter for primes verification
    """

    if (N, L) == FFC_APPROVED_LENGTHS[0]:
        pTests = 3
        qTests = 19
    elif (N, L) == FFC_APPROVED_LENGTHS[1]:
        pTests = 3
        qTests = 24
    elif (N, L) == FFC_APPROVED_LENGTHS[2]:
        pTests = 3
        qTests = 27
    else:
        pTests = 2
        qTests = 27

    outlen = hashlib.sha256().digest_size * 8
    if outlen < N: return None

    #   n = ceil(L / outlen) - 1
    if L % outlen == 0: n = L // outlen - 1
    else: n = L // outlen

    b = L - 1 - (n * outlen)

    # Some precalculated powers of two, so we dont calculate it on each iteration
    twoPowNMin1 = pow(2, N - 1)  # 2^(N - 1)
    twoPowSeedLength = pow(2, N)  # 2^seedlen
    twoPowOutLength = pow(2, outlen)  # 2^outlen
    twoPowLMin1 = pow(2, L - 1)  # 2^(L - 1)
    twoPowB = pow(2, b)  # 2^b

    while 1:
        while 1:
            domainParameterSeed = secrets.randbits(N) | 2 ** (N - 1)

            U = base.bytesToInt(hashlib.sha256(base.intToBytes(domainParameterSeed)).digest()) % twoPowNMin1

            q = twoPowNMin1 + U + 1 - (U % 2)

            if millerRabin(q, qTests):
                if lucasTest(q): break

        # Precalcualted value, to not calculate it in the loop
        twoTimesQ = 2 * q
        offset = 1
        for counter in range(0, 4 * L):

            W = 0
            for j in range(0, n):
                #   Vj = Hash((domain_parameter_seed + offset + j) mod 2^seedlen)
                hashPayload = base.intToBytes((domainParameterSeed + offset + j) % twoPowSeedLength)
                v = base.bytesToInt(hashlib.sha256(hashPayload).digest())

                # W = sum(Vj * 2^(j * outlen))
                W += v * pow(twoPowOutLength, j)

            # Last term of W calculation
            #   Vj = Hash((domain_parameter_seed + offset + j) % 2^seedlen)
            hashPayload = base.intToBytes((domainParameterSeed + offset + n) % twoPowSeedLength)
            v = int(base.bytesToInt(hashlib.sha256(hashPayload).digest()) % twoPowB)

            #   W += (Vn mod 2^b) * 2^(n * outlen)
            W += v * pow(twoPowOutLength, n)

            X = W + twoPowLMin1
            c = X % twoTimesQ
            p = X - (c - 1)
            if p >= twoPowLMin1:
                if millerRabin(p, pTests):
                    if lucasTest(p):
                        return (p, q)

            # Step 11.9
            offset = offset + n + 1

    return None

def getProvablePrimesForFFC(N: int, L: int) -> tuple:
    """Generates provabele primes p and q by algorithm from
    FIPS 186-4, Appendix A.1.2.1.2. This is the simplified implementation, that just generates primes.
    This function does not perform any checks and doesn't allow you to change parameters. Full version
    is in Asymmetric.DSA.generateProvablePrimes.

    Parameters:
        N: int
            Bit length of q - smaller prime
        
        L: int
            Bit length of p - bigger prime

    Returns:
        result: tuple
            primes p and q. Might return None on generation fail, 
            if it does, try running the function again.
    """
    firstSeed = 0

    twoPowNMin1 = pow(2, N - 1)
    while firstSeed < twoPowNMin1: 
        firstSeed = secrets.randbits(N)
        firstSeed |= (2 ** (N - 1) + 1)


    d = shaweTaylor(N, firstSeed)
    if not d["status"]: return None

    q = d["prime"]
    qSeed = d["primeSeed"]
    qGenCounter = d["primeGenCounter"]

    # Step 3
    #   p0Length = ceil(L / 2 + 1)
    if L % 2 == 0: p0Length = L // 2 + 1
    else: p0Length = L // 2 + 2

    d = shaweTaylor(p0Length, qSeed)
    if not d["status"]: return None

    p0 = d["prime"]
    pSeed = d["primeSeed"]
    pGenCounter = d["primeGenCounter"]

    outlen = hashlib.sha256().digest_size * 8

    if L % outlen == 0: iterations = L // outlen - 1
    else: iterations = L // outlen

    oldCounter = pGenCounter

    twoPowOutlen = pow(2, outlen)
    twoPowLMin1 = pow(2, L - 1)

    x = 0
    for i in range(iterations + 1):
        hashPayload = base.intToBytes(pSeed + i)
        h = base.bytesToInt(hashlib.sha256(hashPayload).digest())

        x = x + h * pow(twoPowOutlen, i)
    
    pSeed = pSeed + iterations + 1
    x = twoPowLMin1 + (x % twoPowLMin1)

    #   t = ceil(x / (2 * q * p0))
    if x % (2 * q * p0) == 0: t = x // (2 * q * p0)
    else: t = x // (2 * q * p0) + 1

    while True:

        if 2 * t * q * p0 + 1 > twoPowLMin1 * 2: t = twoPowLMin1 // (2 * q * p0) + (twoPowLMin1 % (2 * q * p0) != 0)

        p = 2 * t * q * p0 + 1
        pGenCounter += 1

        a = 0
        for i in range(iterations + 1):
            hashPayload = base.intToBytes(pSeed + i)
            h = base.bytesToInt(hashlib.sha256(hashPayload).digest())
            a = a + h * pow(twoPowOutlen, i)
    
        pSeed = pSeed + iterations + 1
        a = 2 + (a % (p - 3))
        z = pow(a, 2 * t * q, p)

        if 1 == base.gcd(z - 1, p) and 1 == pow(z, p0, p): return (p, q)    
        if pGenCounter > (4 * L + oldCounter): return None

        t += 1


