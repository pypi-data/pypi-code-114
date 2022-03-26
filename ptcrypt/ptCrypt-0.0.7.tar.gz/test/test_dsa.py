import secrets
from ptCrypt.Asymmetric import DSA
from datetime import datetime
import hashlib
from ptCrypt.Math import base, primality
from ptCrypt.Util import keys
from ptCrypt.Attacks.DSA import repeatedSecretAttack
from random import getrandbits


def testProbablePrimeGeneration():
    print("testProbablePrimeGeneration")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    result = DSA.generateProbablePrimes(N, L, N, hashlib.sha256)

    p = result[1]
    q = result[2]
    assert primality.millerRabin(p, 10)
    assert primality.millerRabin(q, 10)
    assert (p - 1) % q == 0

    N, L = (32, 128)
    result = DSA.generateProbablePrimes(N, L, N, hashlib.sha256, forceWeak=True)

    p = result[1]
    q = result[2]
    assert primality.millerRabin(p, 10)
    assert primality.millerRabin(q, 10)
    assert (p - 1) % q == 0
    


def testProbablePrimeVerification():
    print("testProbablePrimeVerification")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    _, p, q, seed, counter = DSA.generateProbablePrimes(N, L, N)
    assert DSA.verifyProbablePrimesGenerationResult(p, q, seed, counter)

    N, L = (32, 128)
    _, p, q, seed, counter = DSA.generateProbablePrimes(N, L, N, forceWeak=True)
    assert DSA.verifyProbablePrimesGenerationResult(p, q, seed, counter, forceWeak=True)


def testProvablePrimeGeneration():
    print("testProvablePrimeGeneration")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    firstSeed = DSA.getFirstSeed(N, N)
    _, p, q, _, _, _, _, _ = DSA.generateProvablePrimes(N, L, firstSeed)

    assert primality.millerRabin(p, 10)
    assert primality.millerRabin(q, 10)

    N, L = (32, 128)
    firstSeed = DSA.getFirstSeed(N, N, forceWeak=True)
    _, p, q, _, _, _, _, _ = DSA.generateProvablePrimes(N, L, firstSeed, forceWeak=True)

    assert primality.millerRabin(p, 10)
    assert primality.millerRabin(q, 10)


def testUnverifiableG():
    print("testUnverifiableG")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    firstSeed = DSA.getFirstSeed(N, L)
    _, p, q, _, _, _, _, _ = DSA.generateProvablePrimes(N, L, firstSeed)
    g = DSA.generateUnverifiableG(p, q)[0]

    assert DSA.partiallyVerifyRootGeneration(p, q, g)

    N, L = (32, 128)
    firstSeed = DSA.getFirstSeed(N, L, forceWeak=True)
    _, p, q, _, _, _, _, _ = DSA.generateProvablePrimes(N, L, firstSeed, forceWeak=True)
    g = DSA.generateUnverifiableG(p, q)[0]

    assert DSA.partiallyVerifyRootGeneration(p, q, g)


def testProvablePrimeVerification():
    print("testProvablePrimeVerification")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    firstSeed = DSA.getFirstSeed(N, N)
    _, p, q, firstSeed, pSeed, qSeed, pGenCounter, qGenCounter = DSA.generateProvablePrimes(N, L, firstSeed)
    assert DSA.verifyProvablePrimesGenerationResult(p, q, firstSeed, pSeed, qSeed, pGenCounter, qGenCounter)

    N, L = (32, 128)
    firstSeed = DSA.getFirstSeed(N, N, forceWeak=True)
    _, p, q, firstSeed, pSeed, qSeed, pGenCounter, qGenCounter = DSA.generateProvablePrimes(N, L, firstSeed, forceWeak=True)
    assert DSA.verifyProvablePrimesGenerationResult(p, q, firstSeed, pSeed, qSeed, pGenCounter, qGenCounter, forceWeak=True)


def testVerifiableG():
    print("testVerifiableG")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    firstSeed = DSA.getFirstSeed(N, L)
    result = DSA.generateProvablePrimes(N, L, firstSeed)
    while result[0] == False:
        firstSeed = DSA.getFirstSeed(N, L)
        result = DSA.generateProvablePrimes(N, L, firstSeed)
    
    domainParameterSeed = base.intToBytes(result[3]) + base.intToBytes(result[4]) + base.intToBytes(result[5])
    p = result[1]
    q = result[2]
    g = DSA.generateVerifiableG(p, q, domainParameterSeed, 1)
    assert DSA.verifyRootGeneration(p, q, g, domainParameterSeed, 1)

    result = DSA.generateProbablePrimes(N, L, N)
    p = result[1]
    q = result[2]
    domainParameterSeed = base.intToBytes(result[3])
    g = DSA.generateVerifiableG(p, q, domainParameterSeed, 1)
    assert DSA.verifyRootGeneration(p, q, g, domainParameterSeed, 1)

    N, L = (32, 128)
    firstSeed = DSA.getFirstSeed(N, L, forceWeak=True)
    result = DSA.generateProvablePrimes(N, L, firstSeed, forceWeak=True)
    while result[0] == False:
        firstSeed = DSA.getFirstSeed(N, L, forceWeak=True)
        result = DSA.generateProvablePrimes(N, L, firstSeed, forceWeak=True)
    
    domainParameterSeed = base.intToBytes(result[3]) + base.intToBytes(result[4]) + base.intToBytes(result[5])
    p = result[1]
    q = result[2]
    g = DSA.generateVerifiableG(p, q, domainParameterSeed, 1)
    assert DSA.verifyRootGeneration(p, q, g, domainParameterSeed, 1)

    result = DSA.generateProbablePrimes(N, L, N, forceWeak=True)
    p = result[1]
    q = result[2]
    domainParameterSeed = base.intToBytes(result[3])
    g = DSA.generateVerifiableG(p, q, domainParameterSeed, 1)
    assert DSA.verifyRootGeneration(p, q, g, domainParameterSeed, 1)


def testRandomParamsVerification():
    print("testRandomParamsVerification")
    
    N, L = keys.FFC_APPROVED_LENGTHS[0]
    p, q, g = DSA.generateParams(N, L, False, False)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    
    p, q, g = DSA.generateParams(N, L, False, True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    p, q, g = DSA.generateParams(N, L, True, False)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    p, q, g = DSA.generateParams(N, L, True, True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)

    N, L = (32, 128)
    p, q, g = DSA.generateParams(N, L, False, False, forceWeak=True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    
    p, q, g = DSA.generateParams(N, L, False, True, forceWeak=True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    p, q, g = DSA.generateParams(N, L, True, False, forceWeak=True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)
    
    p, q, g = DSA.generateParams(N, L, True, True, forceWeak=True)
    assert DSA.partiallyVerifyRootGeneration(p, q, g)


def testKeysGeneration():
    print("testKeysGeneration")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    
    p, q, g = DSA.generateParams(N, L)
    public, private = DSA.generateKeys(p, q, g)
    
    p, q, g = DSA.generateParams(N, L)
    public, private = DSA.generateKeys(p, q, g, True)

    N, L = (32, 128)
    
    p, q, g = DSA.generateParams(N, L, forceWeak=True)
    public, private = DSA.generateKeys(p, q, g, forceWeak=True)
    
    p, q, g = DSA.generateParams(N, L, forceWeak=True)
    public, private = DSA.generateKeys(p, q, g, True, forceWeak=True)


def testSignature():
    print("testSignature")

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    msg = base.intToBytes(getrandbits(4096))

    p, q, g = DSA.generateParams(N, L)
    public, private = DSA.generateKeys(p, q, g)
    secret = DSA.generateSecret(p, q)

    r, s = DSA.sign(msg, p, q, g, private, secret)
    assert DSA.verify(msg, p, q, g, r, s, public)
    
    msg = base.intToBytes(getrandbits(4096))

    p, q, g = DSA.generateParams(N, L)
    public, private = DSA.generateKeys(p, q, g)
    secret = DSA.generateSecret(p, q)

    r, s = DSA.sign(msg, p, q, g, private, secret, None)
    assert DSA.verify(msg, p, q, g, r, s, public, None)

    N, L = (32, 128)
    msg = base.intToBytes(getrandbits(4096))

    p, q, g = DSA.generateParams(N, L, forceWeak=True)
    public, private = DSA.generateKeys(p, q, g, forceWeak=True)
    secret = DSA.generateSecret(p, q, forceWeak=True)

    r, s = DSA.sign(msg, p, q, g, private, secret)
    assert DSA.verify(msg, p, q, g, r, s, public)
    
    msg = base.intToBytes(getrandbits(4096))

    p, q, g = DSA.generateParams(N, L, forceWeak=True)
    public, private = DSA.generateKeys(p, q, g, forceWeak=True)
    secret = DSA.generateSecret(p, q, forceWeak=True)

    r, s = DSA.sign(msg, p, q, g, private, secret, None)
    assert DSA.verify(msg, p, q, g, r, s, public, None)


def testRepeatedSecretAttack():

    N, L = keys.FFC_APPROVED_LENGTHS[0]
    p, q, g = DSA.generateParams(N, L)
    public, private = DSA.generateKeys(p, q, g)

    secret = DSA.generateSecret(p, q)

    message1 = base.intToBytes(secrets.randbits(4096))
    r1, s1 = DSA.sign(message1, p, q, g, private, secret, hashFunction=None)

    message2 = base.intToBytes(secrets.randbits(4096))
    r2, s2 = DSA.sign(message2, p, q, g, private, secret, hashFunction=None)

    recoveredPrivate = repeatedSecretAttack(p, q, message1, r1, s1, message2, r2, s2)
    assert recoveredPrivate == private

    N, L = (32, 128)
    p, q, g = DSA.generateParams(N, L, forceWeak=True)
    public, private = DSA.generateKeys(p, q, g, forceWeak=True)

    secret = DSA.generateSecret(p, q, forceWeak=True)

    message1 = base.intToBytes(secrets.randbits(4096))
    r1, s1 = DSA.sign(message1, p, q, g, private, secret, hashFunction=None)

    message2 = base.intToBytes(secrets.randbits(4096))
    r2, s2 = DSA.sign(message2, p, q, g, private, secret, hashFunction=None)

    recoveredPrivate = repeatedSecretAttack(p, q, message1, r1, s1, message2, r2, s2)
    assert recoveredPrivate == private