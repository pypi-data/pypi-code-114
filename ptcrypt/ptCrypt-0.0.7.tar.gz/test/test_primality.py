from distutils.log import info
from ptCrypt.Math import base, primality, smallPrimes
from ptCrypt.Asymmetric.RSA import getSeed
from datetime import date, datetime, time
import random

from ptCrypt.Util.keys import IFC_APPROVED_LENGTHS


def measurePrimalityTestTime():
    t = []
    t1 = []
    count = 0
    for _ in range(10):
        prime = random.getrandbits(2048)

        start = datetime.now()
        a = primality.millerRabin(prime, 10)
        end = datetime.now()
        t.append((end - start).microseconds)


    avg = sum(t) / len(t)
    avg1 = sum(t1) / len(t1)
    print(f"Avg time: {avg}")
    print(f"Avg time: {avg1}")
    print(f"Enhance: {avg1 / avg}")
    print(f"Count of primes: {count}")


def testLucas():
    print("testLucas")

    count = 0
    ms = []
    ls = []
    a = random.getrandbits(128)
    start = datetime.now()
    m = primality.millerRabin(a, 10)
    end = datetime.now()
    ms.append((end - start).microseconds)

    start = datetime.now()
    l = primality.lucasTest(a)
    end = datetime.now()
    ls.append((end - start).microseconds)

    avg = sum(ms) / len(ms)
    avg1 = sum(ls) / len(ls)
    print(avg)
    print(avg1)
    print(count)


def testShaweTaylor():
    print("testShaweTaylor")

    length = 1024

    t = []
    t1 = []
    start = datetime.now()
    q = primality.getPrime(length)
    end = datetime.now()
    t.append((end - start).microseconds)

    start = datetime.now()
    p = primality.shaweTaylor(length, random.getrandbits(length - 1))
    while not p["status"]:
        p = primality.shaweTaylor(length, random.getrandbits(length - 1))
    end = datetime.now()
    t1.append((end - start).microseconds)

    assert primality.millerRabin(p["prime"], 64)
    
    avg = sum(t) / len(t)
    avg1 = sum(t1) / len(t1)
    print(f"Avg: {avg} microseconds")
    print(f"Avg1: {avg1} microseconds")


def testPollardFactor():
    print("testPollardFactor")

    primeLength = 38
    i = 7
    p = primality.shaweTaylor(primeLength, i)["prime"]
    while not p:
        i += 1
        p = primality.shaweTaylor(primeLength, i)["prime"]
    
    i += 1
    q = primality.shaweTaylor(primeLength * 2, i)["prime"]
    while not q:
        i += 1
        q = primality.shaweTaylor(primeLength * 2, i)["prime"]

    n = p * q

    start = datetime.now()

    init = 2
    bound = 2**16
    factor = primality.pollardFactor(n, init = init, bound = bound, numbers=smallPrimes.SMALL_PRIMES)
    while not factor and bound < 2 ** primeLength:
        init *= 17
        bound *= 2
        factor = primality.pollardFactor(n, init = init, bound = bound, numbers=smallPrimes.SMALL_PRIMES)

    end = datetime.now()
    print(end - start)
    assert factor == p or factor == q


def testLenstraFactor():
    print("testLenstraFactor")

    primeLength = 35
    i = 7
    p = primality.shaweTaylor(primeLength, i)["prime"]
    while not p:
        i += 1
        p = primality.shaweTaylor(primeLength, i)["prime"]
    
    i += 1
    q = primality.shaweTaylor(primeLength * 2, i)["prime"]
    while not q:
        i += 1
        q = primality.shaweTaylor(primeLength * 2, i)["prime"]

    n = p * q

    start = datetime.now()
    factor = primality.lenstraFactor(n, timeout=60)

    end = datetime.now()
    print(end - start)
    assert factor == p or factor == q


def testIfcProvablePrime():
    print("testIfcProvablePrime")
    
    N = IFC_APPROVED_LENGTHS[0]
    N1 = 1
    N2 = 1

    res = None
    while res == None:
        seed = getSeed(N)
        res = primality.ifcProvablePrime(N // 2, 65537, seed, N1, N2)

    p, p1, p2, pSeed = res
    assert primality.millerRabin(p, 27)
    print(p)
    print(p1)
    print(p2)


def testGetFfcPrimes():
    print("testGetFfcPrimes")

    # Testing provable primes generation (L <= 512)
    for _ in range(100):
        p, q = primality.getFfcPrimes(32, 500)
        assert primality.millerRabin(p, 100)
        assert primality.millerRabin(q, 100)

    # Testing probable primes generation (L > 512)
    for _ in range(100):
        p, q = primality.getFfcPrimes(32, 600)
        assert primality.millerRabin(p, 100)
        assert primality.millerRabin(q, 100)


def testPrimeFactors():
    print("testPrimeFactors")

    for _ in range(100):
        n = base.bytesToInt(base.getRandomBytes(8))
        factors = primality.primeFactors(n, info=True)
        m = 1
        for factor in factors:
            assert primality.millerRabin(factor, 30)
            m *= factor
        assert n == m
