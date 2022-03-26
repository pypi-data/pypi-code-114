from lib2to3.pgen2 import pgen
from ptCrypt.Math import base, primality
import hashlib
from datetime import date, datetime
import secrets
from ptCrypt.Util.keys import FFC_APPROVED_LENGTHS


def generateProbablePrimes(N: int, L: int, seedLength: int, hashFunction: callable = hashlib.sha256, forceWeak: bool = False) -> tuple:
    """Generates probable primes p and q by algorithm from
    FIPS 186-4, Appendix A.1.1.2

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

    # Steps 1 and 2
    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak:
        return (False, None, None, None, None)
    if seedLength < N:
        (False, None, None, None, None)

    # Setting count of Miller-Rabin tests to perform before single Lucas test
    # according to Appendix C.3
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

    # Length of hash funciton output in bits
    outlen = hashFunction().digest_size * 8
    if outlen < N:
        return (False, None, None, None, None)

    # Steps 3 and 4
    #   n = ceil(L / outlen) - 1
    if L % outlen == 0: n = L // outlen - 1
    else: n = L // outlen

    b = L - 1 - (n * outlen)

    # Some precalculated powers of two, so we dont calculate it on each iteration
    twoPowNMin1 = pow(2, N - 1)  # 2^(N - 1)
    twoPowSeedLength = pow(2, seedLength)  # 2^seedlen
    twoPowOutLength = pow(2, outlen)  # 2^outlen
    twoPowLMin1 = pow(2, L - 1)  # 2^(L - 1)
    twoPowB = pow(2, b)  # 2^b

    while 1:
        while 1:
            # Steps 5, 6, 7
            domainParameterSeed = secrets.randbits(seedLength) | 2 ** (seedLength - 1)

            #   U = Hash(domain_parameter_seed) mod 2^(N - 1)
            U = base.bytesToInt(hashFunction(base.intToBytes(domainParameterSeed)).digest()) % twoPowNMin1

            #   q = 2^(N - 1) + U + 1 - (U  mod 2)
            q = twoPowNMin1 + U + 1 - (U % 2)

            # Step 8
            if primality.millerRabin(q, qTests):
                if primality.lucasTest(q): break

        # Precalcualted value, to not calculate it in the loop
        twoTimesQ = 2 * q

        # Step 10
        offset = 1

        # Step 11
        for counter in range(0, 4 * L):

            # Steps 11.1 and 11.2
            W = 0
            for j in range(0, n):
                #   Vj = Hash((domain_parameter_seed + offset + j) mod 2^seedlen)
                hashPayload = base.intToBytes((domainParameterSeed + offset + j) % twoPowSeedLength)
                v = base.bytesToInt(hashFunction(hashPayload).digest())

                # W = sum(Vj * 2^(j * outlen))
                W += v * pow(twoPowOutLength, j)

            # Last term of W calculation
            #   Vj = Hash((domain_parameter_seed + offset + j) % 2^seedlen)
            hashPayload = base.intToBytes((domainParameterSeed + offset + n) % twoPowSeedLength)
            v = int(base.bytesToInt(hashFunction(hashPayload).digest()) % twoPowB)

            #   W += (Vn mod 2^b) * 2^(n * outlen)
            W += v * pow(twoPowOutLength, n)

            # Steps 11.3, 11.4 and 11.5
            X = W + twoPowLMin1
            c = X % twoTimesQ
            p = X - (c - 1)

            # Step 11.6
            if p >= twoPowLMin1:

                # Step 11.7
                if primality.millerRabin(p, pTests):
                    if primality.lucasTest(p):

                        # Step 11.8
                        return (True, p, q, domainParameterSeed, counter)

            # Step 11.9
            offset = offset + n + 1

    return (False, None, None, None, None)


def verifyProbablePrimesGenerationResult(p: int, q: int, domainParameterSeed: int, counter: int, hashFunction=hashlib.sha256, forceWeak: bool = False) -> bool:
    """Verifies if primes were generated by algorithm from
    FIPS 186-4, Appendix A.1.1.2

    Note that verification takes at least as much time as generation

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        seed: int
            domainParameterSeed from generation function
        
        counter: int
            counter from generation function
            
        hashFunction: callable
            Hash function that conforms to hashlib protocols. 
            This function must be equal to the one used for primes generation
            By default hashlib.sha256 is used.
            By FIPS 186-4, one of APPROVED_HASHES should be used
        
        forceWeak: bool
            Indicates if p and q should be verified to have approved lengths. False by default

    Returns:
        result: bool
            True if verification succeeds
            False if verification fails
    """

    # Steps 1, 2
    N = q.bit_length()
    L = p.bit_length()

    # Step 3
    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return False

    # Setting count of Miller-Rabin tests to perform before single Lucas test
    # according to Appendix C.3
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

    # Step 4
    if counter > (4 * L - 1): return False

    # Steps 5, 6
    seedLength = domainParameterSeed.bit_length()
    if seedLength < N: return False

    # Precomputed value 2^(N - 1)
    twoPowNMin1 = pow(2, N - 1)

    # Step 7
    #   U = Hash(domain_parameter_seed) mod 2^(N - 1)
    hashPayload = base.intToBytes(domainParameterSeed)
    U = base.bytesToInt(hashFunction(hashPayload).digest()) % twoPowNMin1

    # Step 8
    #   computed_q = 2^(n - 1) + U + 1 - (U mod 2)
    computedQ = twoPowNMin1 + U + 1 - (U % 2)
    if computedQ != q: return False

    # Step 9
    if not primality.millerRabin(computedQ, qTests): return False
    if not primality.lucasTest(computedQ): return False

    outlen = hashFunction().digest_size * 8

    # Step 10
    #   n = ceil(L / outlen) - 1
    if L % outlen == 0: n = L // outlen - 1
    else: n = L // outlen

    # Step 11
    b = L - 1 - (n * outlen)

    # Some precalculated powers of two
    twoPowSeedLength = pow(2, seedLength)  # 2^seedlen
    twoPowOutLength = pow(2, outlen)  # 2^outlen
    twoPowLMin1 = pow(2, L - 1)  # 2^(L - 1)
    twoPowB = pow(2, b)  # 2^b
    twoTimesQ = 2 * q # 2 * q

    # Step 12
    offset = 1

    # Step 13
    for i in range(counter + 1):

        # Steps 13.1, 13.2
        W = 0
        for j in range(0, n):
            #   Vj = Hash((domain_parameter_seed + offset + j) mod 2^seedlen)
            hashPayload = base.intToBytes((domainParameterSeed + offset + j) % twoPowSeedLength)
            v = base.bytesToInt(hashFunction(hashPayload).digest())

            # W = sum(Vj * 2^(j * outlen))
            W += v * pow(twoPowOutLength, j)

        # Last term of W calculation
        #   Vj = Hash((domain_parameter_seed + offset + j) % 2^seedlen)
        hashPayload = base.intToBytes((domainParameterSeed + offset + n) % twoPowSeedLength)
        v = int(base.bytesToInt(hashFunction(hashPayload).digest()) % twoPowB)

        # W += Vn * 2^(outlen * n)
        W += v * pow(twoPowOutLength, n)

        # Steps 13.3, 13.4, 13.5
        X = W + twoPowLMin1
        c = X % twoTimesQ
        computed_p = X - (c - 1)

        # Step 13.6
        if computed_p < twoPowLMin1:
            offset = offset + n + 1
            continue

        # Step 13.7
        if primality.millerRabin(computed_p, pTests):
            if primality.lucasTest(computed_p):
                # Steps 14 and 15
                if i == counter and computed_p == p: return True
                else: return False

        # Step 13.9
        offset = offset + n + 1

    return False


def getFirstSeed(N: int, seedlen: int, forceWeak: bool = False):
    """Generates first seed for provable primes generation

    Parameters:
        N: int
            Length of prime q in bits
        
        seedlen: int
            length of seed to return, must not be less than N
        
        forceWeak: bool
            Indicates if N should be checked to be approved. False by default.
    
    Returns:
        firstSeed: int
            generated first seed or None if generation fails
    """

    firstSeed = 0
    
    if not forceWeak:
        nIsCorrect = False
        for lengths in FFC_APPROVED_LENGTHS:
            nIsCorrect = nIsCorrect or (N in lengths)
    else:
        nIsCorrect = True

    if not nIsCorrect: return None
    if seedlen < N: return None

    twoPowNMin1 = pow(2, N - 1)
    while firstSeed < twoPowNMin1: 
        firstSeed = secrets.randbits(seedlen)
        firstSeed |= (2 ** (seedlen - 1) + 1)
    return firstSeed


def generateProvablePrimes(N: int, L: int, firstSeed: int, hashFunction: callable = hashlib.sha256, forceWeak: bool = False) -> tuple:
    """Generates provabele primes p and q by algorithm from
    FIPS 186-4, Appendix A.1.2.1.2

    Parameters:
        N: int
            Bit length of q - smaller prime
        
        L: int
            Bit length of p - bigger prime
        
        firstSeed: int
            the first seed to be used
        
        hashFunction: callable
            Hash function conforming to hashlib protocols.
            Hash function output length must not be less than N
            By FIPS 186-4 one of APPROVED_HASHES should be used
    
        forceWeak: bool
            Indicates if N and L should be verified to be approved lengths. False by default.

    Returns:
        result: tuple
            tuple of generation results:
                1. status: bool
                    True if generation was successful and False otherwise
                
                2. p: int
                    Bigger prime
                
                3. q: int
                    Smaller prime
                
                4. firstSeed: int
                    Same as the firstSeed parameter. Will be used for verifications

                5. pSeed: int
                    pSeed for verification function
                
                6. qSeed: int
                    qSeed for verification function
                
                7. pGenCounter: int
                    pGenCounter for verification function
                
                8. qGenCounter: int
                    qGenCounter for verification function
    """

    # Step 1
    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return (False, None, None, None, None, None, None, None)
    
    # Step 2
    d = primality.shaweTaylor(N, firstSeed)
    if not d["status"]: return (False, None, None, None, None, None, None, None)

    q = d["prime"]
    qSeed = d["primeSeed"]
    qGenCounter = d["primeGenCounter"]

    # Step 3
    #   p0Length = ceil(L / 2 + 1)
    if L % 2 == 0: p0Length = L // 2 + 1
    else: p0Length = L // 2 + 2

    d = primality.shaweTaylor(p0Length, qSeed)
    if not d["status"]: return (False, None, None, None, None, None, None, None)

    p0 = d["prime"]
    pSeed = d["primeSeed"]
    pGenCounter = d["primeGenCounter"]

    outlen = hashFunction().digest_size * 8

    # Step 4, 5
    if L % outlen == 0: iterations = L // outlen - 1
    else: iterations = L // outlen

    oldCounter = pGenCounter

    twoPowOutlen = pow(2, outlen)
    twoPowLMin1 = pow(2, L - 1)

    # Steps 6, 7
    x = 0
    for i in range(iterations + 1):
        hashPayload = base.intToBytes(pSeed + i)
        h = base.bytesToInt(hashFunction(hashPayload).digest())

        x = x + h * pow(twoPowOutlen, i)
    
    # Steps 8, 9
    pSeed = pSeed + iterations + 1
    x = twoPowLMin1 + (x % twoPowLMin1)

    # Step 10
    #   t = ceil(x / (2 * q * p0))
    if x % (2 * q * p0) == 0: t = x // (2 * q * p0)
    else: t = x // (2 * q * p0) + 1

    while True:

        # Step 11
        if 2 * t * q * p0 + 1 > twoPowLMin1 * 2: t = twoPowLMin1 // (2 * q * p0) + (twoPowLMin1 % (2 * q * p0) != 0)

        # Steps 12, 13
        p = 2 * t * q * p0 + 1
        pGenCounter += 1

        # Steps 14, 15
        a = 0
        for i in range(iterations + 1):
            hashPayload = base.intToBytes(pSeed + i)
            h = base.bytesToInt(hashFunction(hashPayload).digest())

            a = a + h * pow(twoPowOutlen, i)
    
        # Steps 16, 17, 18
        pSeed = pSeed + iterations + 1
        a = 2 + (a % (p - 3))
        z = pow(a, 2 * t * q, p)

        # Step 19
        if 1 == base.gcd(z - 1, p) and 1 == pow(z, p0, p):
            return (True, p, q, firstSeed, pSeed, qSeed, pGenCounter, qGenCounter)
    
        # Step 20
        if pGenCounter > (4 * L + oldCounter): return (False, None, None, None, None, None, None, None)

        # Step 21
        t += 1


def verifyProvablePrimesGenerationResult(
    p: int,
    q: int, 
    firstSeed: int, 
    pSeed: int, 
    qSeed: int, 
    pGenCounter: int,
    qGenCounter: int,
    hashFunction: callable=hashlib.sha256,
    forceWeak: bool = False
) -> bool:
    """Verifies if primes were generated by algorithm from
    FIPS 186-4, Appendix 1.2.2

    Note that verification takes at least as much time as generation

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        firstSeed: int
            Seed that was passed to generation function
        
        pSeed, qSeed, pGenCounter, qGenCounter: int
            Parameters returned from generation function
        
        hashFunction: callable
            Hash function thath conforms to hashlib protocols.
            This function must be equal to the one used for primes generation
            By default hashlib.sha256 is used
            By FIPS 186-4, one of APPROVED_HASHES should be used
        
        forceWeak: bool
            Indicates if length of p and length of q should be verified to have approved bit length. False by default

    Returns:
        result: bool
            True if verification succeeds
            False if verification fails
    """

    L = p.bit_length()
    N = q.bit_length()

    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return False

    if firstSeed < pow(2, N - 1): return False
    if pow(2, N) <= q: return False
    if pow(2, L) <= p: return False
    if (p - 1) % q != 0: return False

    check, checkP, checkQ, firstSeed, checkPSeed, checkQSeed, checkPGenCounter, checkQGenCounter = generateProvablePrimes(N, L, firstSeed, hashFunction, forceWeak)

    if checkP != p: return False
    if checkQ != q: return False
    if checkPSeed != pSeed: return False
    if checkQSeed != qSeed: return False
    if checkPGenCounter != pGenCounter: return False
    if checkQGenCounter != qGenCounter: return False

    return True


def generateUnverifiableG(p: int, q: int, seed: int = 2, update: callable = lambda x: x + 1) -> tuple:
    """Generates g value for DSA according to algorithm from FIPS 186-4, Appendix A.2.1

    Note, according to the standard argument seed must be unique for primes pair, but this function
    will not guarantee this. It is a caller responsibility to provide seed and its update function. 
    Function will return seed along with g, so caller can mark it as used.

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime

        seed: int
            initial value of h, see FIPS 186-4 for details
        
        update: callable
            seed update function if initial seed turned out to be inappropriate
    
    Returns:
        result: tuple
            tuple of two values:
                g: int
                    Generated primitive root
                
                seed: int
                    Updated seed
    """

    e = (p - 1) // q

    while 1:
        g = pow(seed, e, p)
        if g != 1: break

        seed = update(seed)

    return (g, seed)


def partiallyVerifyRootGeneration(p: int, q: int, g: int) -> bool:
    """Checks partial validity of DSA parameters according to algorithm from FIPS 186-4, Appendix A.2.2

    Note that this function verifies correctness, but not security. As standard states:
    'The non-existence of a potentially exploitable relationship of g to another genrator g' (that is known to the entity
    that generated g, but may not be know by other entities) cannot be checked'

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        g: int
            Primitive root
    
    Returns:
        status: bool
            True if parameters is partially valid.
            False if parameters are definitely not valid
    """

    if g < 2 or g > p - 1: return False
    if pow(g, q, p) == 1: return True
    return False


def generateVerifiableG(p: int, q: int, domainParameterSeed: int, index: int, hashFunction: callable=hashlib.sha256) -> int:
    """Generates verifiable root for DSA. To generate more than one root for same primes, change index
    Algorithm is specified by FIPS 186-4, Appendix A.2.3

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        domainParameterSeed: int
            The seed returned by primes generation function. 
            When primes generated by algorithm from Appendix A.1.1.2 the domainParameterSeed value is used
            When primes generated by algorithm from Appendix A.1.2.1 the domainParameterSeed is concatenated parameters firstSeed + pSeed + qSeed

        index: int
            Number of root to generate. For same p and q this function can generate different roots for different index values.
            Index value must be bounded to 8 bit number
        
        hashFunction: callable
            hash function that conforms to hashlib protocols. By default hashlib.sha256 is used
    
    Returns:
        result: int
            Generated primitive root. May be returned None if generate goes wrong.
    """

    if index.bit_length() > 8: return (False, None, None, None)
    
    ggen = b"\x67\x67\x65\x6e"
    indexBytes = base.intToBytes(index)

    N = q.bit_length()
    e = (p - 1) // q

    count = 0

    while True:
        count = (count + 1) & 0xffff

        if count == 0: return None

        countBytes = base.intToBytes(count)
        U = domainParameterSeed + ggen + indexBytes + countBytes
        W = base.bytesToInt(hashFunction(U).digest())
        g = pow(W, e, p)
        if g >= 2: 
            return g


def verifyRootGeneration(
    p: int,
    q: int, 
    g: int, 
    domainParameterSeed: int, 
    index: int, 
    hashFunction: callable = hashlib.sha256
) -> bool:
    """Verifies that root were generated by algorithm from FIPS 186-4, Appendix A.2.4

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        g: int
            Primitive root
        
        domainParameterSeed: int
            seed returned from primes generation function and used for root generation
        
        index: int
            Primitive root index. See generateVerifiableG for details
    
        hashFunction: callable
            hash function that conforms to hashlib protocols. Must be the same function that was used for root generation
            By default hashlib.sha256 is used
    
    Returns:
        status: bool
            True if root were generated by FIPS 186-4 method
            False either if root is not correct at all, or if it is was not generated by FIPS 186-4
    """

    if not partiallyVerifyRootGeneration(p, q, g): return False

    ggen = b"\x67\x67\x65\x6e"

    index = index & 0xff
    indexBytes = base.intToBytes(index)

    N = q.bit_length()
    e = (p - 1) // q
    count = 0

    while True:
        count = (count + 1) & 0xffff

        if count == 0: return False

        countBytes = base.intToBytes(count)
        U = domainParameterSeed + ggen + indexBytes + countBytes
        W = base.bytesToInt(hashFunction(U).digest())
        computedG = pow(W, e, p)

        if g > 2:
            return computedG == g


def generateParams(
    N: int,
    L: int, 
    provablePrimes: bool = False,
    verifiableRoot: bool = False,
    hashFunction: callable = hashlib.sha256,
    forceWeak: bool = False
) -> tuple:
    """Generate random DSA parameters with minimal setup. 
    This function is not appropriate for systems with long lifecycle.

    Parameters:
        N: int
            bit length of q - smaller prime
        
        L: int
            bit length of p - bigger prime
        
        provablePrimes: bool
            specifies if generated primes must be provably primes. This function will not return
            any parameters for primes generation verification.
            By default value is False.
        
        verifiableRoot: bool
            specifies if generated root must be generated by verifiable root generation algorithm.
            This function will not return any parameters for root verification.
            By default value is False
        
        hashFunction: callable
            hash function to use for primes and root generation. Must conform to hashlib protocols.
            By default hashlib.sha256 is used
        
        forceWeak: bool
            Indicates if N and L should be verified to be approved by the standard.
    
    Returns:
        params: tuple
            tuple that contains generated p, q, and g. Will return None if passed wrong parameters,
            such as (N, L) pair not from APPROVED_LENGTHS or hash function digest size less than N
    """

    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return None
    outlen = hashFunction().digest_size * 8
    if outlen < N: return None

    if provablePrimes:
        firstSeed = getFirstSeed(N, N,forceWeak)
        result = generateProvablePrimes(N, L, firstSeed, hashFunction, forceWeak)
        while result[0] == False:
            firstSeed = getFirstSeed(N, N, forceWeak)
            result = generateProvablePrimes(N, L, firstSeed, hashFunction, forceWeak)
    else:
        result = generateProbablePrimes(N, L, N, hashFunction, forceWeak)
    
    p = result[1]
    q = result[2]
    domainParameterSeed = base.intToBytes(result[3])
    if provablePrimes:
        domainParameterSeed = domainParameterSeed + base.intToBytes(result[4]) + base.intToBytes(result[5])

    if verifiableRoot:
        index = 1
        g = generateVerifiableG(p, q, domainParameterSeed, 1, hashFunction)
        while g == None and index < 256:
            index += 1
            g = generateVerifiableG(p, q, domainParameterSeed, index, hashFunction)
        if g == None: return None
    else:
        g = generateUnverifiableG(p, q)[0]
        if g == None: return None

    return (p, q, g)


def generateKeys(p: int, q: int, g: int, useAdditionalBits: bool = False, forceWeak: bool = False) -> tuple:
    """Generates public and private keys for DSA by algorithms specified
    in FIPS 186-4, Appendix B.1.1 and B.1.2. This function implements both algorithms.
    Set useAdditionalBits to True to use algorithm from B.1.1 and to False to use algorithm from B.1.2

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        g: int
            Primitive root
        
        useAdditionalBits: bool
            Specifies the algorithm to use.
            True - use FIPS 186-4, Appendix B.1.1
            False - use FIPS 186-4, Appendix B.1.2
    
        forceWeak: bool
            Indicates if p and q should be verified to have approved lengths. False by default
    Returns:
        result: tuple
            Pair of keys:
                1. y: int
                    public exponent
                
                2. x: int
                    private exponent
    """

    N = q.bit_length()
    L = p.bit_length()

    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return (None, None)

    if useAdditionalBits:
        c = secrets.randbits(N + 64)
        x = (c % (q - 1)) + 1
    else:
        while True:
            c = secrets.randbits(N)
            if c <= q - 2: break
        x = c + 1
    
    y = pow(g, x, p)

    return (y, x)


def generateSecret(p: int, q: int, useAdditionalBits: bool = False, forceWeak: bool = False) -> int:
    """Generates per-message random secret by algorithms specified in FIPS 186-4, Appendix B.2

    Parameters:
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        useAdditionalBits: bool
            Specifies algorithm to use
            True - use FIPS 186-4, Appendix B.2.1
            False - use FIPS 186-4, Appendix B.2.2
        
        forceWeak: bool
            Indicates if p and q should be verified to have approved length. False by default
    
    Returns:
        result: int
            random number appropriate to use for DSA signing with given parameters.
            May return None if inappropriate parameters were given
    """

    N = q.bit_length()
    L = p.bit_length()

    if (N, L) not in FFC_APPROVED_LENGTHS and not forceWeak: return None

    if useAdditionalBits:
        c = secrets.randbits(N + 64)
        k = (c % (q - 1)) + 1
        
        try:
            pow(k, -1, q)
        except Exception:
            return None

        return k
    else:
        while True:
            c = secrets.randbits(N)
            if c <= q - 2: break
        k = c + 1
        
        try:
            pow(k, -1, q)
        except Exception:
            return None
        
        return k


def prepareMessage(
    message: bytes,
    q: int,
    hashFunction: callable = hashlib.sha256
) -> int:
    """Processes the message before signing or verifying according to FIPS 186-4.
    The procedure works as follows:
        1) compute zLength = min(N, outlen), 
            where outlen is the length of hash function. 
            If hash function is not specified, then just take N
        2) compute h = Hash(message) if hash function is specified, or jsut message otherwise
        3) take zLength leftmost bits of h and return as an integer
    
    So the value returned from this function can be directly inserted into signature/verification calculation

    Parameters:
        message: bytes
            Message to process
        
        q: int
            Smaller prime
        
        hashFunction: callable
            hash function to use for message process. Must conform to hashlib protocols.
            By default hashlib.sha256 is used. This value also might be None, then no hash function will be used
    
    Returns:
        result: int
            Processed message as integer
    """

    N = q.bit_length()

    zLength = N
    if hashFunction != None:
        outlen = hashFunction().digest_size * 8
        zLength = min(N, outlen)
        message = hashFunction(message).digest()
    
    message = base.bytesToInt(message)
    
    if message.bit_length() > zLength:
        message = message >> (message.bit_length() - zLength)
    
    return message


def sign(
    message: bytes,
    p: int,
    q: int,
    g: int,
    x: int,
    secret: int, 
    hashFunction: callable = hashlib.sha256
) -> tuple:
    """Signs message with given private key and secret

    Parmeters:
        message: bytes
            Message to be signed
        
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        g: int
            Primitive root
        
        x: int
            Secret exponent
        
        secret: int
            unique random secret for message signature
        
        hashFunction: callable
            hash function for signature. This function must conform to hashlib protocols. 
            By default hashlib.sha256 is used.
            If this value is None, message bytes will be signed instead of its hash

    Returns:
        result: tuple
            generated signature (r, s) for message
    """

    message = prepareMessage(message, q, hashFunction)
    
    r = pow(g, secret, p) % q
    s = (pow(secret, -1, q) * (message + x * r)) % q

    if r == 0 or s == 0: return None
    return (r, s)


def verify(
    message: bytes,
    p: int,
    q: int,
    g: int,
    r: int,
    s: int,
    y: int, 
    hashFunction: callable = hashlib.sha256
) -> bool:
    """Verifies given signature

    Parameters:
        message: bytes
            Message which signature is to be checked
        
        p: int
            Bigger prime
        
        q: int
            Smaller prime
        
        g: int
            Primitive root
        
        r, s: int
            Signature to check
        
        y: int
            Public exponent
        
        hashFunction: callable
            signature's hash function. This function must conform to hashlib protocols. 
            By default hashlib.sha256 is used.
            If this value is None, message bytes will be verified instead of its hash

    Returns:
        result: bool
            True if signature is valid
            False if signature is invalid
    """

    if r <= 0 or r >= q: return False
    if s <= 0 or r >= q: return False
    
    message = prepareMessage(message, q, hashFunction)

    w = pow(s, -1, q)
    u1 = (message * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    return v == r
