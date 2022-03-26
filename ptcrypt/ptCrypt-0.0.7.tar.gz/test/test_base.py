import secrets
from ptCrypt.Math import base, primality
from datetime import datetime
import random


def testJacobi():
    a = 5
    n = 3439601197
    print(base.jacobiSymbol(a, n))


def testPartition():

    cases = [
        (b"\x00", 1),
        (b"\x00", 2),
        (b"\x00\x01", 1),
        (b"\x00\x01", 2),
        (b"\x00\x01\x02\x03\x04", 2)
    ]

    checks = [
        [b"\x00"],
        [b"\x00"],
        [b"\x00", b"\x01"],
        [b"\x00\x01"],
        [b"\x00\x01", b"\x02\x03", b"\x04"]
    ]

    for i in range(len(cases)):
        test = cases[i]
        result = base.partition(test[0], test[1])
        assert result == checks[i]


def testIntToBytes():

    cases = [
        (0x01, 2, "big"),
        (0x0102, 2, "big"),
        (0x0102, 1, "big"),
        (0x01, 2, "little"),
        (0x0102, 2, "little"),
        (0x0102, 1, "little")
    ]

    checks = [
        b"\x00\x01",
        b"\x01\x02",
        b"\x01\x02",
        b"\x01\x00",
        b"\x02\x01",
        b"\x02\x01"
    ]

    for i in range(len(cases)):
        value, size, byteorder = cases[i]
        result = base.intToBytes(value, size, byteorder)
        assert result == checks[i]


def testCrt():
    print("testCrt")

    numbersCount = 4
    numbersSize = 1024
    print(f"\tUsing {numbersCount} numbers of size {numbersSize * 8} bits (modulus size {numbersCount * numbersSize * 8} bits)")

    times = []
    for _ in range(100):
        modulus = base.bytesToInt(base.getRandomBytes(numbersSize))
        mods = [modulus]
        for _ in range(1, numbersCount):
            number = base.bytesToInt(base.getRandomBytes(numbersSize))
            while base.gcd(number, modulus) != 1:
                number = base.bytesToInt(base.getRandomBytes(numbersSize))
            
            mods.append(number)
            modulus *= number
        
        solution = base.bytesToInt(base.getRandomBytes(base.byteLength(modulus))) % modulus

        coeffs = []
        for number in mods:
            coeffs.append(solution % number)
        
        start = datetime.now()
        crtResult = base.crt(coeffs, mods)
        end = datetime.now()
        times.append((end - start).microseconds)
        assert solution == crtResult

    print(f"\tAverage time: {sum(times) / len(times)} microseconds")


def testGetGenerator():
    print("testGetGenerator")

    for _ in range(100):
        p, q = primality.getFfcPrimes(32, 512)
        g = base.getGenerator(p, q)
        assert pow(g, q, p) == 1


def testGetPrimitiveRoot():
    print("testGetPrimitiveRoot")
    
    for _ in range(100):
        p, q = primality.getFfcPrimes(64, 128)
        N = (p - 1) // q
        factors = primality.primeFactors(N)
        factors.append(q)
        print(factors)
        g = base.getPrimitiveRoot(p, factors)
        assert pow(g, p - 1, p) == 1


def testContinuedFraction():
    print("testContinuedFraction")

    assert base.continuedFraction(649, 200) == [3, 4, 12, 4]
    assert base.continuedFraction(4, 9) == [0, 2, 4]
    assert base.continuedFraction(355, 113) == [3, 7, 16]
    assert base.continuedFraction(17993, 90581) == [0, 5, 29, 4, 1, 3, 2, 4, 3]