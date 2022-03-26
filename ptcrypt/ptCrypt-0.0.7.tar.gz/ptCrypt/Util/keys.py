import hashlib
import random


FFC_APPROVED_LENGTHS = [
    (160, 1024),
    (224, 2048),
    (256, 2048),
    (256, 3072),
    (384, 7680),
    (512, 15360)
]

IFC_APPROVED_LENGTHS = [
    1024,
    2048,
    3072,
    7680,
    15360
]


ECC_APPROVED_LENGTHS = [
    160,
    224,
    256,
    384,
    512
]


APPROVED_HASHES = [
    hashlib.sha1,
    hashlib.sha224,
    hashlib.sha256,
    hashlib.sha384,
    hashlib.sha512
]


def getFFCSecurityLevel(N: int, L: int) -> int:
    """Returns security level of lengths pair for finite-field cryptography (DSA, DH, MQV)
    according to NIST SP800-57

    Given pair must be in FFC_APPROVED_LENGTHS, otherwise 0 is returned.

    Parameters:
        N: int
            smaller number bit length
        
        L: int
            bigger number bit length
    
    Returns:
        result: int
            Associated security level
    """

    if (N, L) not in FFC_APPROVED_LENGTHS: return 40
    elif (N, L) == FFC_APPROVED_LENGTHS[0]: return 80
    elif (N, L) == FFC_APPROVED_LENGTHS[1]: return 112
    elif (N, L) == FFC_APPROVED_LENGTHS[2]: return 128
    elif (N, L) == FFC_APPROVED_LENGTHS[3]: return 192
    elif (N, L) == FFC_APPROVED_LENGTHS[4]: return 256
    else: return 0


def getIFCSecurityLevel(N: int) -> int:
    """Returns security level of bit length for integer-factorization cryptography (RSA)
    according to NIST SP800-57

    Given number must be in IFC_APPROVED_LENGTHS, otherwise 0 is returned.

    Parameters:
        N: int
            key bit length
    

    Returns:
        result: int
            Associated security level
    """

    if N not in IFC_APPROVED_LENGTHS: return 40
    elif N == IFC_APPROVED_LENGTHS[0]: return 80
    elif N == IFC_APPROVED_LENGTHS[1]: return 112
    elif N == IFC_APPROVED_LENGTHS[2]: return 128
    elif N == IFC_APPROVED_LENGTHS[3]: return 192
    elif N == IFC_APPROVED_LENGTHS[4]: return 256


def getECCSecurityLevel(N: int):
    """Returns security level of bit length for elliptic-curve cryptography (ECDSA, EDH, EMQV)
    according to NIST SP800-57

    Parameters:
        N: int
            key bit length
    
    Returns:
        result: int
            Associated security level
    """

    if N < ECC_APPROVED_LENGTHS[0]: return 40
    elif N in range(ECC_APPROVED_LENGTHS[0], ECC_APPROVED_LENGTHS[1]): return 80
    elif N in range(ECC_APPROVED_LENGTHS[1], ECC_APPROVED_LENGTHS[2]): return 112
    elif N in range(ECC_APPROVED_LENGTHS[2], ECC_APPROVED_LENGTHS[3]): return 128
    elif N in range(ECC_APPROVED_LENGTHS[3], ECC_APPROVED_LENGTHS[4]): return 192
    else: return 256


def getFFCKeyLength(securityLevel: int) -> tuple:
    """Returns appropriate pair of bit lengths for keys to get required security level
    for finite-field cryptography according to NIST SP800-57

    Parameters:
        securityLevel: int
            required security level
    
    Returns:
        result: tuple
            Pair of appropriate bit lengths for keys as tuple (smallerLength, biggerLength)
            Note that if you need to conform to NIST standards you should use exact values returned from thsi function
    """

    if securityLevel <= 80: return FFC_APPROVED_LENGTHS[0]
    elif securityLevel in range(81, 113): return FFC_APPROVED_LENGTHS[1]
    elif securityLevel in range(113, 129): return FFC_APPROVED_LENGTHS[2]
    elif securityLevel in range(129, 193): return FFC_APPROVED_LENGTHS[3]
    else: return FFC_APPROVED_LENGTHS[4]


def getIFCKeyLength(securityLevel: int) -> int:
    """Retuns minimal key length to get requried security level for integer-factorization cryptography
    according to NIST SP800-57

    Parameters:
        securityLevel: int
            required security level
    
    Returns:
        result: int
            Bit length of key to use to get required security level. 
            Note that if you need to conform to NIST standards 
            you should use exact value returned from this function
    """

    if securityLevel <= 80: return IFC_APPROVED_LENGTHS[0]
    elif securityLevel in range(81, 113): return IFC_APPROVED_LENGTHS[1]
    elif securityLevel in range(113, 129): return IFC_APPROVED_LENGTHS[2]
    elif securityLevel in range(129, 193): return IFC_APPROVED_LENGTHS[3]
    else: return IFC_APPROVED_LENGTHS[4]


def getECCKeyLength(securityLevel: int) -> int:
    """Returns minimal key length to get required security level for elliptic-curve cryptography
    according to NIST SP800-57

    Parameters:
        securityLevel: int

    Returns:
        result: int
            Bit length of key to use to get required security level.
    """

    if securityLevel <= 80: return ECC_APPROVED_LENGTHS[0]
    elif securityLevel in range(81, 113): return ECC_APPROVED_LENGTHS[1]
    elif securityLevel in range(113, 129): return ECC_APPROVED_LENGTHS[2]
    elif securityLevel in range(129, 193): return ECC_APPROVED_LENGTHS[3]
    else: return ECC_APPROVED_LENGTHS[4]


def millerRabinTestsForFFC(N: int, L: int) -> int:
    """Returns recommended count of Miller-Rabin tests for finite-field cryptosystems with
    given key lengths to achieve 2**(-80) error probability according to FIPS 186-4, Appendix C.3.

    If given parameters N and L are not in FFC_APPROVED_LENGTHS, function returns 0.

    Parameters:
        N: int
            smaller prime length
        
        L: int
            bigger prime length
    

    Returns:
        result: int
            recommended count of tests to apply for both primes
    """

    if (N, L) not in FFC_APPROVED_LENGTHS: return 64
    if (N, L) == FFC_APPROVED_LENGTHS[0]: return 40
    if (N, L) == FFC_APPROVED_LENGTHS[1]: return 56
    if (N, L) == FFC_APPROVED_LENGTHS[2]: return 56
    if (N, L) == FFC_APPROVED_LENGTHS[3]: return 64

    return 40


def millerRabinAndLucasTestsForFFC(N: int, L: int) -> tuple:
    """Returns recommended count of Miller-Rabin test followed by single Lucas test for
    finite-field cryptosystems with given key lengths to achieve 2**(-80) error probability
    according to FIPS 186-4, Appendix C.3.

    If given parametes N and L are not in FFC_APPROVED_LENGTS, function returns None.

    Parameters:
        N: int
            smaller prime length
        
        L: int
            bigger prime length
    
    Returns:
        result: tuple
            pair of counts of Miller-Rabin tests followed by one Lucas test for smaller and bigger 
            prime respectively
    """

    if (N, L) not in FFC_APPROVED_LENGTHS: return (27, 2)
    if (N, L) == FFC_APPROVED_LENGTHS[0]: return (19, 3)
    if (N, L) == FFC_APPROVED_LENGTHS[1]: return (24, 3)
    if (N, L) == FFC_APPROVED_LENGTHS[2]: return (27, 3)
    if (N, L) == FFC_APPROVED_LENGTHS[3]: return (27, 2)
    return (27, 2)


def millerRabinTestsForIFC(N: int, withAuxiliaryPrimes: bool = False) -> tuple:
    """Returns recommended counts of Miller-Rabin tests for integer-factorization cryptosystems
    with given key length to achieve 2**(-80) error probability according
    to FIPS 186-4, Appendix C.3.

    If given key length is not in IFC_APPROVED_LENGTHS, function returns None.
    Note also that FIPS 186-4 does specify any values for 7680 and 15360, as they are not
    approved for use in IFC by FIPS 186-4, but SP800-57 specifies these values.
    So for these values function will return count of tests for 3072.

    Parameters:
        N: int
            cryptosystem key length
    
    Returns:
        result: tuple
            pair of counts of Miller-Rabin to apply. First element is count of tests to apply to 
            key factors. 
            And the second count is the count of tests to apply to primes p1, p2, q1 and q2.
            See FIPS 186-4, Appendix B.3. to find out more about p1, p2, q1 and q2.
    """

    if N not in IFC_APPROVED_LENGTHS: return (64, 0)

    if withAuxiliaryPrimes:
        if N == IFC_APPROVED_LENGTHS[0]: return (5, 28)
        if N == IFC_APPROVED_LENGTHS[1]: return (5, 38)
        if N >= IFC_APPROVED_LENGTHS[2]: return (4, 41)
        return (4, 41)
    else:
        if N == IFC_APPROVED_LENGTHS[0]: return (40, 0)
        if N == IFC_APPROVED_LENGTHS[1]: return (56, 0)
        if N == IFC_APPROVED_LENGTHS[2]: return (64, 0)
        return (64, 0)


def getIFCAuxiliaryPrimesLegths(N: int, probablePrimes: bool = False) -> tuple:
    """Returnes auxiliary primes (p1, p2) lengths for IFC primes generation according
    to table B.1, from FIPS 186-4, Appendix B.3.1. FIPS 186-4 specifies only values for
    1024, 2048 and 3072.

    Parameters:
        N: int
            IFC key length
        
        probablePrimes: bool
            indicates if p and q are generated as probable or provable primes. 
            There are different requirements for different generation methods.
    
    Returns:
        result: tuple
            p1 and p2 lengths, generated randomly but in such 
            a way that they satisfy conditions from FIPS 186-4
    """

    if probablePrimes:
        if N == IFC_APPROVED_LENGTHS[0]:
            return (random.randint(101, 495 // 2), random.randint(101, 496 // 2))
        elif N == IFC_APPROVED_LENGTHS[1]:
            return (random.randint(141, 1007 // 2), random.randint(141, 1007 // 2))
        elif N == IFC_APPROVED_LENGTHS[2]:
            return (random.randint(171, 1517 // 2), random.randint(171, 1518 // 2))
        elif N == IFC_APPROVED_LENGTHS[3]:
            return (random.randint(301, 3821 // 2), random.randint(301, 3822 // 2))
        elif N == IFC_APPROVED_LENGTHS[4]:
            return (random.randint(511, 7661 // 2), random.randint(511, 7661 // 2))
        else:
            return (random.randint(N // 5, N // 3), random.randint(N // 5, N // 3))
    else:
        if N == IFC_APPROVED_LENGTHS[0]:
            return (random.randint(101, 239 // 2), random.randint(101, 239 // 2))
        elif N == IFC_APPROVED_LENGTHS[1]:
            return (random.randint(141, 493 // 2), random.randint(141, 494 // 2))
        elif N == IFC_APPROVED_LENGTHS[2]:
            return (random.randint(171, 749 // 2), random.randint(171, 750 // 2))
        elif N == IFC_APPROVED_LENGTHS[3]:
            return (random.randint(301, 1901 // 2), random.randint(301, 1901 // 2))
        elif N == IFC_APPROVED_LENGTHS[4]:
            return (random.randint(511, 3819 // 2), random.randint(511, 3820 // 2))
        else:
            return (random.randint(N // 5, N // 3), random.randint(N // 5, N // 3))
