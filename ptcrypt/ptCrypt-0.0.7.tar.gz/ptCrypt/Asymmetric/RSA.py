import random
import hashlib
import secrets
from sqlite3 import SQLITE_ALTER_TABLE
from ptCrypt.Math import base, primality
from ptCrypt.Util.keys import IFC_APPROVED_LENGTHS, getIFCSecurityLevel, millerRabinTestsForIFC, getIFCAuxiliaryPrimesLegths
from secrets import randbits


def getSeed(N: int, forceWeak: bool = False) -> int:
    """Returns seed appropriate for provable primes generation
    according to algorithm from NIST FIPS 186-4, Appendix B.3.2.1.
    This function uses OS random generator, which is supposed to 
    be secure enough for cryptographic usage.

    Parameters:
        N: int
            key bit length
        
        forceWeak: bool
            Indicates wether to disable input parameters' weakness check. False by default.
    Returns:
        seed: int
            seed to use for provable primes generation
    """

    if N not in IFC_APPROVED_LENGTHS and not forceWeak: return None
    secLvl = getIFCSecurityLevel(N)
    return randbits(2 * secLvl) | 2 ** (2 * secLvl- 1)


def generateProvablePrimes(e: int, N: int, seed: int, forceWeak: bool = False) -> tuple:
    """Generates provably prime numbers p and q for RSA.
    The algorithm is specified by FIPS 186-4, Appendix B.3.2.2.
    Note that FIPS 186-4 only allows N to be 2048 or 3072. This function, however,
    allows any value from IFC_APPROVED_LENGTHS that is greater or equal to 2048.

    Parameters:
        e: int
            RSA public exponent
        
        N: int
            required key size, which is the modulus size for IFC.
        
        seed: int
            random seed to use for primes generation, 
            use getSeed function to get this value
    
        forceWeak: bool
            Indicates wether to disable input parameters' weakness check. False by default.

    Returns:
        result: tuple
            generated primes p and q, or None. 
            None might be returned if either passed parameters are not appropriate by FIPS 186-4,
            or the generation simply fails. If parameters are fine, generate new seed with getSeed and
            run the function again.
    """

    # Steps 1, 2, 3 and 4
    if not forceWeak:
        if N < 2048: return None
        if N not in IFC_APPROVED_LENGTHS: return None
        if e <= 2**16 or e >= 2**256 or e % 2 == 0: return None
        securityStrength = getIFCSecurityLevel(N)
        if seed.bit_length() != 2 * securityStrength: return None

    # Step 5
    workingSeed = seed

    # Step 6
    L = N // 2
    N1 = 1
    N2 = 1
    firstSeed = workingSeed
    result = primality.ifcProvablePrime(L, e, firstSeed, N1, N2)
    if not result: return None
    p, p1, p2, pSeed = result
    workingSeed = pSeed

    # Step 7
    while True:

        # Step 7.1
        result = primality.ifcProvablePrime(L, e, workingSeed, N1, N2)
        if not result: return None
        q, q1, q2, qSeed = result

        # Step 7.2
        workingSeed = qSeed

        # Step 8
        if abs(p - q) > pow(2, N // 2 - 100): break

    # Steps 9, 10
    pSeed = 0
    qSeed = 0
    workingSeed = 0
    return (p, q)


def generateProbablePrimes(e: int, N: int, forceWeak: bool = False) -> tuple:
    """Generates probably prime numbers p and q for RSA.
    The algorithm is specified by FIPS 186-4, Appendix B.3.3.
    Note that FIPS 186-4 only allows N to be 2048 or 3072. This function, however,
    allows any value from IFC_APPROVED_LENGTHS that is greater or equal to 2048.

    Parameters:
        e: int
            RSA public exponent
        
        N: int
            required key size, which is the modulus size for IFC.
    
        forceWeak: bool
            Indicates wether to disable input parameters' weakness check. False by default.
    
    Returns:
        result: tuple
            generated primes p and q, or None. 
            None might be returned if either passed parameters are not appropriate by FIPS 186-4,
            or the generation simply fails. If parameters are fine, generate new seed with getSeed and
            run the function again.
    """

    # Steps 1, 2
    if not forceWeak:
        if N < 2048: return None
        if N not in IFC_APPROVED_LENGTHS: return None
        if e<= 2**16 or e >= 2**256 or e % 2 == 0: return None

    testsCount = millerRabinTestsForIFC(N)[0]
    
    # 665857/470832 = 1.41421356237 is a good rational approximation of sqrt(2)
    coeff1 = 665857 * pow(2, N // 2 - 1) // 470832

    # Step 4
    i = 0
    while True:
        # Steps 4.2 and 4.3
        p = secrets.randbits(N // 2) | 1

        # Step 4.4
        if p < coeff1: continue

        # Step 4.5
        if base.gcd(p - 1, e) == 1:
            if primality.millerRabin(p, testsCount): break
        
        # Steps 4.6, 4.7
        i += 1
        if i >= 5 * N // 2: return None
    
    # Step 5
    i = 0
    while True:
        # Steps 5.2 and 5.3
        q = secrets.randbits(N // 2) | 1

        # Step 5.4
        if abs(p - q) <= pow(2, N // 2 - 100): continue

        # Step 5.5
        if q < coeff1: continue

        # Step 5.6
        if base.gcd(q - 1, e) == 1:
            if primality.millerRabin(q, testsCount): break
        
        # Steps 5.7 and 5.8
        i += 1
        if i >= 5 * N // 2: return None
    
    return (p, q)


def geneareteProvablePrimesWithConditions(e: int, N: int, seed: int) -> tuple:
    """Provable primes generation method which satisfies security conditions from FIPS 186-4.
    Generation algorithm is specified by FIPS 186-4, Appendix B.3.4.
    Note that FIPS 186-4 only allows N to be 1024, 2048 or 3072. This function, however,
    allows any value from IFC_APPROVED_LENGTHS.

    Parameters:
        e: int
            public exponent for RSA
        
        N: int
            RSA key length
        
        seed: int
            random seed to use for generation
    
    Returns:
        result: tuple
            pair of provably prime numbers p and q such that n = p * q has length N.
            May return None if either passed parameters are incorrect, or generation fails.
            If parameters are good, retry generation with different seed.
    """

    # Steps 1, 2
    if N not in IFC_APPROVED_LENGTHS: return None
    if e <= 2 ** 16 or e >= 2 ** 256: return None
    # Steps 3, 4
    securityLevel = getIFCSecurityLevel(N)
    if seed.bit_length() != 2 * securityLevel: return None

    # Step 5
    workingSeed = seed

    p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N)
    q1Len, q2Len = getIFCAuxiliaryPrimesLegths(N)

    # Step 6
    res = primality.ifcProvablePrime(N // 2, e, workingSeed, p1Len, p2Len)
    if not res: return None

    p, p1, p2, pSeed = res
    workingSeed = pSeed

    # Step 7
    while True:
        res = primality.ifcProvablePrime(N // 2, e, workingSeed, q1Len, q2Len)
        if not res: return None

        q, q1, q2, qSeed = res
        workingSeed = qSeed

        # Step 8
        if abs(p - q) > pow(2, N // 2 - 100): break

    # Steps 9, 10
    qSeed = 0
    pSeed = 0
    workingSeed = 0
    return (p, q)


def generateProbablePrimesWithConditions(e: int, N: int, seed: int, probablePrimes: bool = False) -> tuple:
    """Generates probable primes p and q for RSA by algorithms specified in FIPS 186-4, Appendix B.3.5 and B.3.6.
    This function combines two algorithms, set probablePrimes to False to use algorirthm from Appendix B.3.5. and
    to True to use algorithm from Appendix B.3.6.
    Note that FIPS 186-4 only allows N to be 1024, 2048 or 3072. This function, however,
    allows any value from IFC_APPROVED_LENGTHS.

    Parameters:
        e: int
            RSA public exponent
        
        N: int
            key length
        
        seed: int
            seed to use for generation, only used for algorithm Appendix B.3.5, so if probablePrimes set to True,
            this value has no effect and can be set to None.
        
        probablePrimes: bool
            specifies which algorithm to use:
                True -> Appendix B.3.6.
                False -> Appendix B.3.5.
            
        forceWeak: bool
            Indicates wether to disable input parameters' weakness check. False by default.
    
    Returns:
        result: tuple
            pair of primes p and q or None. None might be returned either if passed parameters are incorrect, or
            if generation fails when probablePrimes is set to False. If parameters are fine, try using different seed.
    """

    # Steps 1, 2    
    if N not in IFC_APPROVED_LENGTHS: return None
    if e <= 2 ** 16 or e >= 2 ** 256: return None

    testsCount = millerRabinTestsForIFC(N)[0]

    # Steps 3, 4
    securityLevel = getIFCSecurityLevel(N)
    if not probablePrimes and seed.bit_length() != 2 * securityLevel: return None

    p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, probablePrimes = probablePrimes)
    q1Len, q2Len = getIFCAuxiliaryPrimesLegths(N, probablePrimes = probablePrimes)

    if not probablePrimes:
        # Step 5.1
        res = primality.shaweTaylor(p1Len, seed)
        if not res["status"]: return None
        p1 = res["prime"]
        primeSeed = res["primeSeed"]

        # Step 5.2
        res = primality.shaweTaylor(p2Len, primeSeed)
        if not res["status"]: return None
        p2 = res["prime"]
        primeSeed = res["primeSeed"]

        # Step 5.3
        p = generateProbablePrimeWithAuxiliaryPrimes(p1, p2, N, e)
        if not p: return None
        p, Xp = p

        while True:
            # Step 6.1
            res = primality.shaweTaylor(q1Len, primeSeed)
            if not res["status"]: return None
            q1 = res["prime"]
            primeSeed = res["primeSeed"]

            # Step 6.2
            res = primality.shaweTaylor(q2Len, primeSeed)
            if not res["status"]: return None
            q2 = res["prime"]
            primeSeed = res["primeSeed"]

            # Step 6.3
            q = generateProbablePrimeWithAuxiliaryPrimes(q1, q2, N, e)
            if not q: return None
            q, Xq = q

            # Step 7
            if abs(p - q) > pow(2, N // 2 - 100) and abs(Xp - Xq) > pow(2, N // 2 - 100): break

    else:
        # Step (4.1)
        Xp1 = secrets.randbits(p1Len) | 2 ** (p1Len - 1) | 1
        Xp2 = secrets.randbits(p2Len) | 2 ** (p2Len - 1) | 1

        # Step (4.2)
        while not primality.millerRabin(Xp1, testsCount): Xp1 += 2
        while not primality.millerRabin(Xp2, testsCount): Xp2 += 2

        # Step (4.3)
        res = generateProbablePrimeWithAuxiliaryPrimes(Xp1, Xp2, N, e)
        if not res: return None

        p, Xp = res

        while True:

            # Step (5.1)
            Xq1 = secrets.randbits(q1Len) | 2 ** (q1Len - 1) | 1
            Xq2 = secrets.randbits(q2Len) | 2 ** (q2Len - 1) | 1

            # Step (5.2)
            while not primality.millerRabin(Xq1, testsCount): Xq1 += 2
            while not primality.millerRabin(Xq2, testsCount): Xq2 += 2

            # Step (5.3)
            res = generateProbablePrimeWithAuxiliaryPrimes(Xq1, Xq2, N, e)
            if not res: return None

            q, Xq = res

            # Step (6)
            if abs(p - q) > 2 ** (N // 2 - 100) and abs(Xp - Xq) > 2 ** (N // 2 - 100): break
    
    # Step 8(7)
    Xp = 0
    Xq = 0
    Xp1 = 0
    Xp2 = 0
    Xq1 = 0
    Xq2 = 0
    primeSeed = 0
    p1 = 0
    p2 = 0
    q1 = 0
    q2 = 0

    return (p, q)


def generateProbablePrimeWithAuxiliaryPrimes(p1: int, p2: int, N: int, e: int) -> tuple:
    """Generates probable prime for RSA with auxilary primes by 
    algorithm specified in FIPS 186-4, Appendix C.9.

    Parameters:
        p1: int
        p2: int
            Auxiliary primes
        
        N: int
            key length
        
        e: int
            RSA public exponent
    
    Returns:
        result: tuple
            Pair of integers: probable prime number 
            and random integer used to generate that number
    """

    testsCount = millerRabinTestsForIFC(N)[0]

    # Steps 1, 2
    if base.gcd(2 * p1, p2) != 1: return None

    # R = 1 mod 2p1 and R = -1 mod p2
    R = (pow(p2, -1, 2 * p1) * p2) - ((pow(2 * p1, -1, p2) * 2 * p1 ))

    assert (R % (2*p1)) == 1 and (R % p2) == (-1 % p2)

    xLowBorder = 665857 // 470832 * pow(2, N // 2 - 1)
    xHighBorder = pow(2, N // 2) - 1

    # Step 3
    while True:
        X = secrets.randbits(N // 2) | 2 ** (N // 2 - 1)
        while X < xLowBorder or X > xHighBorder:
            X = secrets.randbits(N // 2) | 2 ** (N // 2 - 1)

        assert X <= xHighBorder and X >= xLowBorder

        # Step 4
        Y = X + ((R - X) % (2 * p1 * p2))

        # Step 5
        i = 0
        while True:

            # Step 6
            if Y >= pow(2, N // 2): break

            # Step 7
            if base.gcd(Y - 1, e) == 1:
                if primality.millerRabin(Y, testsCount): return (Y, X)

            # Steps 8, 9, 10
            i += 1
            if i >= 5 * (N // 2): return None
            Y = Y + (2 * p1 * p2)


def encrypt(e: int, n: int, m: int) -> int:
    """RSA encryption primitive by PKCS#1

    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
    
        m: int
            message to encrypt, must staisfy 0 <= m <= n - 1

    Returns:
        result: int
            encrypted message m^e mod n, or None, if m < 0 or m > n - 1
    """
    if m < 0 or m > n - 1: return None
    return pow(m, e, n)


def decrypt(d: int, n: int, c: int) -> int:
    """RSA decryption primitive by PKCS#1

    Parameters:
        d: int
            RSA private exponent
        
        n: int
            RSA modulus
    
        c: int
            message to decrypt, must satisfy 0 <= c <= n - 1

    Returs:
        result: int
            decrypted message c^d mod n, or None, if c < 0 or c > n - 1
    """

    if c < 0 or c > n - 1: return None
    return pow(c, d, n)


def sign(d: int, n: int, m: int) -> int:
    """RSA signature primitive by PKCS#1

    Parameters:
        d: int
            RSA private exponent

        n: int
            RSA modulus

        m: int
            messsage to sign
    
    Returns:
        result: int
            signature of the given message, or None, if m < 0 or m > n - 1
    """

    if m < 0 or m > n - 1: return None
    return pow(m, d, n)


def verify(e: int, n: int, s: int) -> int:
    """RSA verify primitive by PKCS#1

    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
        
        s: int
            signature to verify
    
    Returns:
        result: int
            returns message decrypted with given public key. 
            If returned message is equal to received message, then signature is correct
    """

    if s < 0 or s > n - 1: return None
    return pow(s, e, n)


def oaepEncrypt(e: int, n: int, message: bytes, label: bytes = b"", hashFunction: callable = hashlib.sha256) -> bytes:
    """RSA-OAEP encryption function specified by PKCS#1, Section 7.1.1.

    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
        
        message: bytes
            message to encrypt
        
        label: bytes
            optional additional label to add. By default - empty string
        
        hashFunction: callable
            hash function to use. Must conform to hashlib protocols, by default hashlib.sha256 is used
    
    Returns:
        result: bytes
            Encrypted message. 
            Might be equal to None if mLength > nLength - 2 * hashLength - 2,
            where mLength - length of the message in bytes,
            nLength - lenght of modulus in bytes,
            hashLength - lenght of hash output in bytes
    """

    nLength = len(base.intToBytes(n))
    mLength = len(message)
    lLength = len(label)
    hLength = hashFunction().digest_size

    # Step 1.b
    if mLength > nLength - 2 * hLength - 2: return None

    # Step 2
    lHash = hashFunction(label).digest()  # 2.a
    ps = b"\x00" * (nLength - mLength - 2 * hLength - 2)  # 2.b
    db = lHash + ps + b"\x01" + message  # 2.c
    seed = base.getRandomBytes(hLength)  # 2.d
    dbMask = MGF(seed, nLength - hLength - 1)  # 2.e
    maskedDb = base.xor(db, dbMask)  # 2.f
    seedMask = MGF(maskedDb, hLength)  # 2.g
    maskedSeed = base.xor(seed, seedMask)  # 2.h
    em = b"\x00" + maskedSeed + maskedDb  # 2.i

    # Step 3
    m = base.bytesToInt(em)
    c = encrypt(e, n, m)

    # Step 4
    return base.intToBytes(c, nLength)


def oaepDecrypt(d: int, n: int, ciphertext: bytes, label: bytes = b"", hashFunction: callable = hashlib.sha256) -> bytes:
    """RSA-OAEP decryption according to PKCS#1, Section 7.1.2

    Parameters:
        d: int
            RSA private exponent
        
        n: int
            RSA modulus
        
        ciphertext: bytes
            encrypted message
        
        label: bytes
            optional label. By default empty string is used
        
        hashFunction: callable
            hash function used for encryption. Must conform to hashlib protocols. By default hashlib.sha256 is used
    
    Returns:
        result: bytes
            Decrypted plaintext.
            Might return None if some paramters or ciphertext are non appropriate to OAEP scheme.
    """

    nLength = base.byteLength(n)
    hLength = hashFunction().digest_size

    # Step 1
    if len(ciphertext) != nLength: return None
    if nLength < 2 * hLength + 2: return None

    # Step 2
    c = base.bytesToInt(ciphertext)  # 2.a
    m = decrypt(d, n, c)  # 2.b
    em = base.intToBytes(m, nLength)  # 2.c

    # Step 3
    lHash = hashFunction(label).digest() # 3.a
    
    # Step 3.b
    Y = em[0]
    maskedSeed = em[1:1 + hLength]
    maskedDb = em[1 + hLength: nLength]

    # Steps 3.c - 3.f
    seedMask = MGF(maskedDb, hLength)
    seed = base.xor(maskedSeed, seedMask)
    dbMask = MGF(seed, nLength - hLength - 1)
    db = base.xor(maskedDb, dbMask)

    # Step 3.g
    lHash_ = db[:hLength]
    if lHash != lHash_: return None

    index = hLength
    while index < len(db):
        if db[index] == 1: break
        if db[index] != 0: return None
        index += 1
    
    # Step 4
    return db[index + 1:]


def MGF(seed: bytes, length: int, hashFunction: callable = hashlib.sha256) -> bytes:
    """Mask generation function specified by PKCS#1, Appendix B.2.1

    Parameters:
        seed: bytes
            generations seed
        
        length: int
            required mask length
        
        hashFunction: callable
            hash function to use. Must conform to hashlib protocols. By default hashlib.sha256 is used
    
    Returns:
        result: bytes
            generated mask
    """

    hashLength = hashFunction().digest_size

    # Step 1
    if length > 2 ** 32 * hashLength: return None

    # Step 2
    t = b""

    # Step 3
    top = length // hashLength
    if length % hashLength: top += 1
    for counter in range(top):
        c = base.intToBytes(counter, 4)  # 3.a
        t = t + hashFunction(seed + c).digest()  # 3.b
    
    # Step 4
    return t[:length]


def pkcs1v15Encrypt(e: int, n: int, message: bytes) -> bytes:
    """RSA-PKCS1v1.5 encryption function specified by PKC#1, Section 7.2.1
    This encryption scheme is not recommended for new applications, check oaepEncrypt instead.

    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
        
        message: bytes
            message to encrypt
    
    Returns:
        result: bytes
            Encrypted message.
            Might be equal to None if mLength > nLength - 11,
            where mLength - length of the message in bytes,
            nLength - length of modulus in bytes
    """

    nLength = base.byteLength(n)
    mLength = len(message)

    # Step 1
    if mLength > nLength - 11: return None

    # Step 2
    ps = base.getRandomBytes(nLength - mLength - 3, exclude=set([0]))  # 2.a
    em = b"\x00" + b"\x02" + ps + b"\x00" + message  # 2.b

    # Step 3
    m = base.bytesToInt(em)  # 3.a
    c = encrypt(e, n, m)  # 3.b

    # Steps 3.c and 4
    return base.intToBytes(c)


def pkcs1v15Decrypt(d: int, n: int, ciphertext: bytes) -> bytes:
    """RSA-PKCS1v1.5 decryption according to PKCS#1, Section 7.2.2

    Parameters:
        d: int
            RSA private exponent
        
        n: int
            RSA modulus
        
        ciphertext: bytes
            encrypted message
        
    Returns:
        result: bytes
            Decrypted plaintext.
            Might return None if some parameters are incorrect or ciphertext is corrupted.
    """

    nLength = base.byteLength(n)
    cLength = len(ciphertext)

    # Step 1
    if cLength < nLength - 1 or nLength < 11: return None

    # Step 2
    c = base.bytesToInt(ciphertext)  # 2.a
    m = decrypt(d, n, c)  # 2.b

    if m == None: return None

    em = base.intToBytes(m)  # 2.c

    # Step 3
    if em[0] != 2: return None

    i = 2
    while i < len(em) and em[i] != 0: i += 1
    if i >= len(em): return None
    if i < 9: return None

    message = em[i + 1:]

    # Step 4
    return message


def emsaPssEncode(
    message: bytes,
    emBits: int, 
    saltLength: int, 
    hashFunction: callable = hashlib.sha256
) -> bytes:
    """EMSA-PSS Encode method implementation by PKCS#1, Section 9.1.1

    Parameters:
        message: bytes
            message to encode
        
        emBits: int
            bit length of em
        
        saltLength: int
            length of salt
        
        hashFunction: callable
            hash function to use. Must conform to hashlib protocols. 
            By default hashlib.sha256 is used
    
    Returns:
        result: bytes
            Encoded message. Might return None if parameters are incorrect (see PKCS#1)
    """

    emLength = emBits // 8
    if emBits % 8: emLength += 1

    # Step 2
    mHash = hashFunction(message).digest()
    hashLength = len(mHash)

    # Step 3
    if emLength < hashLength + saltLength + 2: return None

    # Step 4
    salt = base.getRandomBytes(saltLength)

    # Steps 5, 6
    M = b"\x00" * 8 + mHash + salt
    H = hashFunction(M).digest()

    # Steps 7, 8
    ps = b"\x00" * (emLength - hashLength - saltLength - 2)
    db = ps + b"\x01" + salt

    # Steps 9, 10
    dbMask = MGF(H, emLength - hashLength - 1, hashFunction)
    maskedDb = base.xor(db, dbMask)

    # Step 11
    bitMask = 0xff
    for _ in range(8 * emLength - emBits): bitMask >>= 1

    maskedDb = bytes([maskedDb[0] & bitMask]) + maskedDb[1:]

    # Steps 12, 13
    em = maskedDb + H + b"\xbc"
    return em


def emsaPssVerify(
    message: bytes,
    encodedMessage: bytes, 
    emBits: int, 
    saltLength: int, 
    hashFunction: callable = hashlib.sha256
) -> bool:
    """EMSA-PSS Verification method implementation by PKCS#1, Section 9.1.2

    Parameters:
        message: bytes
            original message
        
        encodedMessage: bytes
            encoded message to verify
        
        emBits: int
            intended encoded message bit length
        
        saltLength: int
            length of salt
        
        hashFunction: callable
            hash function used to encode message. Must conform to hashlib protocols.
            By default hashlib.sha256 is used.
    
    Returns:
        result: bool
            True if message was encoded by emsaPssEncode method, False otherwise.
    """

    emLength = len(encodedMessage)

    # Step 2
    mHash = hashFunction(message).digest()
    hashLength = len(mHash)

    # Step 3
    if emLength < hashLength + saltLength + 2: return False

    # Step 4
    if encodedMessage[-1] != 0xbc: return False

    # Step 5
    maskedDb = encodedMessage[:emLength - hashLength - 1]
    H = encodedMessage[emLength - hashLength - 1:emLength - 1]

    # Step 6
    bitMask = 0xff
    for _ in range(8 * emLength - emBits): bitMask >>= 1
    bitMask = ~bitMask

    if bitMask & maskedDb[0] != 0: return False

    # Steps 7, 8
    dbMask = MGF(H, emLength - hashLength - 1, hashFunction)
    db = base.xor(maskedDb, dbMask)

    # Step 9
    bitMask = ~bitMask
    db = bytes([db[0] & bitMask]) + db[1:]
    
    # Step 10
    for i in range(emLength - hashLength - saltLength - 2):
        if db[i] != 0x00: return False
    
    if db[emLength - hashLength - saltLength - 2] != 1: return False
    
    # Steps 11, 12, 13, 14
    salt = db[-saltLength:]
    M = b"\x00" * 8 + mHash + salt
    H_ = hashFunction(M).digest()
    return H == H_


def ssaPssSign(d: int, n: int, message: bytes, hashFunction: callable = hashlib.sha256) -> bytes:
    """RSASSA-PSS signature generation implementation by PKCS#1, Section 8.1.1

    Parameters:
        d: int
            RSA private exponent
        
        n: int
            RSA modulus
        
        message: bytes
            message to sign
    
        hashFunction: callable
            Hash function to use for signature generation. Must conform to hashlib protocols. 
            By default hashlib.sha256 is used.
    Returns:
        result: bytes
            RSASSA-PSS signature
    """

    k = base.byteLength(n)
    modBits = n.bit_length()

    hashLength = hashFunction().digest_size
    emLength = (modBits - 1) // 8
    if (modBits - 1) % 8: emLength += 1
    saltLength = emLength - 2 - hashLength

    em = emsaPssEncode(message, modBits - 1, saltLength, hashFunction)

    m = base.bytesToInt(em)
    s = sign(d, n, m)
    
    return base.intToBytes(s, k)


def ssaPssVerify(e: int, n: int, message: bytes, signature: bytes, hashFunction: callable = hashlib.sha256) -> bool:
    """RSASSA-PSS verification implementation by PKCS#1, Section 8.1.2
    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
        
        message: bytes
            message that was signed
        
        signature: bytes
            RSASSA-PSS signature to check
        
        hashFunction: callable
            hash function that was used to generate signature. Must conform to hashlib protocols. 
            By default hashlib.sha256 is used.
    
    Returns:
        result: bool
            True if signature is correct and False otherwise
    """

    modBits = n.bit_length()
    k = base.byteLength(n)
    if len(signature) > k or len(signature) < k - 1: return False

    s = base.bytesToInt(signature)
    m = verify(e, n, s)

    emLength = (modBits - 1) // 8
    if (modBits - 1) % 8: emLength += 1

    em = base.intToBytes(m, emLength)

    hashLength = hashFunction().digest_size
    saltLength = emLength - hashLength - 2

    return emsaPssVerify(message, em, modBits - 1, saltLength, hashFunction)


def emsaPkcs1v15Encode(message: bytes, emLength: int, hashFunction: callable = hashlib.sha256) -> bytes:
    """EMSA-PKCS1-v1_5 encoding method implementation by PKCS#1, Section 9.2

    Parameters:
        message: bytes
            Message to encode
        
        emLength: int
            Desired length of the encoded message
        
        hashFunction: callable
            hash function to use. 
            Must be one of {hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha384, hashlib.sha512}
        
    Returns:
        em: bytes
            Encoded message. Might return null if hashfunction is not appropriate, or if emLength is too small
    """

    derHeader = None
    if hashFunction == hashlib.md5:
        derHeader = b"\x30\x20\x30\x0c\x06\x08\x2a\x86\x48\x86\xf7\x0d\x02\x05\05\x00\x04\x10"
    elif hashFunction == hashlib.sha1:
        derHeader = b"\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14"
    elif hashFunction == hashlib.sha256:
        derHeader = b"\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20"
    elif hashFunction == hashlib.sha384:
        derHeader = b"\x30\x41\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30"
    elif hashFunction == hashlib.sha512:
        derHeader = b"\x30\x51\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40"
    else:
        return None
    
    h = hashFunction(message).digest()
    T = derHeader + h
    tLength = len(T)
    if emLength < tLength + 11: return None
    
    ps = b"\xff" * (emLength - tLength - 3)
    em = b"\x00\x01" + ps + b"\x00" + T

    return em


def ssaPkcs1v15Sign(d: int, n: int, message: bytes, hashFunction: callable = hashlib.sha256) -> bytes:
    """RSASSA-PKCS1-v1_5-SIGN method implementation by PKCS#1, Section 8.2.1

    Parameters:
        d: int
            RSA private exponent
        
        n: int
            RSA modulus
        
        message: bytes
            Message to sign
        
        hashFunction: callable
            Hash function to use.
            Must be one of {hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha384, hashlib.sha512}

    Returns:
        signature: bytes
            Signature of the message or Null, if n is too small, hash function is not appropriate or
            RSA.sign returns None
    """

    k = base.byteLength(n)
    em = emsaPkcs1v15Encode(message, k, hashFunction=hashFunction)
    if em == None: return None
    m = base.bytesToInt(em)
    s = sign(d, n, m)
    if s == None: return None
    return base.intToBytes(s, k)


def ssaPkcs1V15Verify(e: int, n: int, message: bytes, signature: bytes, hashFunction: callable = hashlib.sha256) -> bool:
    """RSASSA-PKCS1-V1_5-VERIFY method implementation by PKCS#1, Section 8.2.2

    Parameters:
        e: int
            RSA public exponent
        
        n: int
            RSA modulus
        
        message: bytes
            Message corresponding to a signature
        
        signature: bytes
            Signature to check
        
        hashFunction: callable
            Hash function used for signature generation.
    
    Returns:
        result: bool
            True if the signature is correct and False otherwise.
    """

    k = base.byteLength(n)
    if len(signature) != k: return False

    s = base.bytesToInt(signature)
    m = verify(e, n, s)
    em_ = base.intToBytes(m, k)
    em = emsaPkcs1v15Encode(message, k, hashFunction)
    return em_ == em


def getParameters(N: int) -> tuple:
    """Simple RSA parameters generation
    
    Parameters:
        N: int
            required modulus bit length
        
        forceWeak: bool
            indicates if weakness check should be checked to be approved length by FIPS standard. False by default

    """

    if N < 1024:
        e = None
        res = None
        while not res:
            e = primality.getPrime(17)
            seed = getSeed(N, forceWeak=True)
            res = generateProvablePrimes(e, N, seed, forceWeak=True)
            if res != None:
                p, q = res
                f = (p - 1) * (q - 1)
                if base.gcd(e, f) != 1:
                    res = None
        n = p * q
        d = (base.egcd(e, f)[1]) % f
        return (e, d, n, p, q)

    elif N in IFC_APPROVED_LENGTHS:
        e = None
        res = None
        while not res:
            e = primality.getPrime(17)
            seed = getSeed(N)
            res = geneareteProvablePrimesWithConditions(e, N, seed)
            if res != None:
                p, q = res
                f = (p - 1) * (q - 1)
                if base.gcd(e, f) != 1:
                    res = None
        
        n = p * q
        d = (base.egcd(e, f)[1]) % f
        return (e, d, n, p, q)
    else:
        e = None
        res = None
        while not res:
            e = primality.getPrime(17)
            seed = getSeed(N, forceWeak=True)
            res = generateProbablePrimes(e, N, seed, forceWeak=True)
            if res != None:
                p, q = res
                f = (p - 1) * (q - 1)
                if base.gcd(e, f) != 1:
                    res = None
        
        n = p * q
        d = (base.egcd(e, f)[1]) % f
        return (e, d, n, p, q)
