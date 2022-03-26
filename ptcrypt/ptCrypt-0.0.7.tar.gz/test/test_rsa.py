from hashlib import sha256
import hashlib
import os
import random
from ptCrypt.Math import base
from ptCrypt.Math import primality
from ptCrypt.Util.keys import IFC_APPROVED_LENGTHS, millerRabinTestsForIFC, getIFCSecurityLevel, getIFCAuxiliaryPrimesLegths
from ptCrypt.Asymmetric import RSA
from ptCrypt.Math.primality import millerRabin, shaweTaylor
from ptCrypt.Attacks.RSA import privateKeyFactorization, commonModulusAttack, wienerAttack, hastadAttack
from datetime import date, datetime


def testGenerateProvablePrimes():
    print("testGenerateProvablePrimes")

    e = 65537
    N = 2048
    testsCount = millerRabinTestsForIFC(N)[0]
    
    for _ in range(5):
        seed = RSA.getSeed(N)
        res = None
        while not res:
            seed = RSA.getSeed(N)
            res = RSA.generateProvablePrimes(e, N, seed)
        
        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)

    N = 512
    for _ in range(5):
        seed = RSA.getSeed(N, forceWeak=True)
        res = None
        while not res:
            seed = RSA.getSeed(N, forceWeak=True)
            res = RSA.generateProvablePrimes(e, N, seed, forceWeak=True)
        
        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)


def testGenerateProbablePrimes():
    print("testGenerateProbablePrimes")

    e = 65537
    N = 2048
    testsCount = millerRabinTestsForIFC(N)[0]

    for _ in range(1):
        res = RSA.generateProbablePrimes(e, N)
        assert res
        
        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)
    
    N = 512
    for _ in range(5):
        res = RSA.generateProbablePrimes(e, N, forceWeak=True)
        assert res

        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)


def testGenerateProvablePrimesWithConditions():
    print("testGenerateProvablePrimesWithConditions")

    e = 65537
    N = 1024
    testsCount = millerRabinTestsForIFC(N)[0]
    
    for _ in range(1):
        seed = RSA.getSeed(N)
        res = None
        while not res:
            seed = RSA.getSeed(N)
            res = RSA.geneareteProvablePrimesWithConditions(e, N, seed)        
        
        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)

    e = 65537
    N = 3072
    testsCount = millerRabinTestsForIFC(N)[0]
    
    for _ in range(1):
        seed = RSA.getSeed(N)
        res = None
        while not res:
            seed = RSA.getSeed(N)
            res = RSA.geneareteProvablePrimesWithConditions(e, N, seed)
        
        p, q = res
        assert millerRabin(p, testsCount) and millerRabin(q, testsCount)


def testGenerateProbablePrimesWithAuxiliaryPrimes():
    print("testGenerateProbablePrimesWithAuxiliaryPrimes")

    e = 65537

    for N in IFC_APPROVED_LENGTHS[:3]:
        testsCount = millerRabinTestsForIFC(N, False)[0]
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, probablePrimes=False)
        for _ in range(1):
            while True:
                seed = RSA.getSeed(N)
                res = shaweTaylor(p1Len, seed)
                if not res["status"]: continue
                p1 = res["prime"]
                primeSeed = res["primeSeed"]

                res = shaweTaylor(p2Len, primeSeed)
                if not res["status"]: continue

                p2 = res["prime"]
                primeSeed = res["primeSeed"]

                p = RSA.generateProbablePrimeWithAuxiliaryPrimes(p1, p2, N, e)
                if not p: continue

                assert millerRabin(p[0], testsCount)
                break


def testGenerateProbablePrimesWithConditions():
    print("testGenerateProbablePrimesWithConditions")

    e = 65537
    for N in IFC_APPROVED_LENGTHS[0:3]:

        testsCount = millerRabinTestsForIFC(N)[0]
        for _ in range(1):
            while True:
                seed = RSA.getSeed(N)
                res = RSA.generateProbablePrimesWithConditions(e, N, seed, probablePrimes = False)
                if not res: continue

                p, q = res

                assert millerRabin(p, testsCount) and millerRabin(q, testsCount)
                break

    for N in IFC_APPROVED_LENGTHS[0:3]:

        testsCount = millerRabinTestsForIFC(N)[0]
        for _ in range(1):
            while True:
                res = RSA.generateProbablePrimesWithConditions(e, N, None, probablePrimes = True)
                if not res: continue

                p, q = res

                assert millerRabin(p, testsCount) and millerRabin(q, testsCount)
                break


def testOAEPEncryptionAndDecryption():
    print("testOAEPEncryptionAndDecryption")

    e = 65537

    for N in IFC_APPROVED_LENGTHS[:1]:
        print(N)

        for _ in range(10):
            res = None
            while res == None:
                seed = RSA.getSeed(N)
                res = RSA.generateProbablePrimesWithConditions(e, N, seed)
    
            p, q = res
            n = p * q
            d = pow(e, -1, (p - 1) * (q - 1))
    
            maxLength = base.byteLength(n) - 2 * sha256().digest_size - 2
            m = os.urandom(maxLength)
            c = RSA.oaepEncrypt(e, n, m)
            m_ = RSA.oaepDecrypt(d, n, c)
            if m != m_:
                print(m)


def testPKCS1V15EncryptionAndDecryption():
    print("testPkcs1V15EncryptionAndDecryption")

    e = 65537
    for N in IFC_APPROVED_LENGTHS[:1]:
        
        for _ in range(10):
            res = None
            while res == None:
                seed = RSA.getSeed(N)
                res = RSA.generateProbablePrimesWithConditions(e, N, seed)
        
            p, q = res
            n = p * q
            d = pow(e, -1, (p - 1) * (q - 1))

            maxLength = base.byteLength(n) - 11
            m = os.urandom(maxLength)
            c = RSA.pkcs1v15Encrypt(e, n, m)
            m_ = RSA.pkcs1v15Decrypt(d, n, c)
            if m != m_:
                print(m_)
                print(m)


def testEMSAPSSEncodeAndVerify():
    print("testEMSA-PSSEncodeAndVerify")

    for _ in range(10):
        messageLength = random.randint(10, 100)
        message = base.getRandomBytes(messageLength)
        em = RSA.emsaPssEncode(message, len(message) * 128, 16)
        assert em != None
        assert RSA.emsaPssVerify(message, em, len(message) * 128, 16)


def testRSASSASignAndVerify():
    print("testRSASSASignAndVerify")

    e = 65537
    N = IFC_APPROVED_LENGTHS[0]
    res = None
    while res == None:
        seed = RSA.getSeed(N)
        res = RSA.generateProbablePrimesWithConditions(e, N, seed, True)
    
    p, q = res
    f = (p - 1) * (q - 1)
    d = pow(e, -1, f)
    n = p * q

    for _ in range(10):
        messageLenngth = base.byteLength(n)
        message = base.getRandomBytes(messageLenngth)
        signature = RSA.ssaPssSign(d, n, message)
        assert RSA.ssaPssVerify(e, n, message, signature)


def testEmsaPkcs1v15Encode():
    print("testEmsaPkcs1v15Encode")

    e = 65537
    N = IFC_APPROVED_LENGTHS[0]
    res = None
    while res == None:
        seed = RSA.getSeed(N)
        res = RSA.generateProbablePrimesWithConditions(e, N, seed, True)
    
    p, q = res
    f = (p - 1) * (q - 1)
    d = pow(e, -1, f)
    n = p * q

    for _ in range(10):
        messageLength = base.byteLength(n)
        message = base.getRandomBytes(messageLength)
        em = RSA.emsaPkcs1v15Encode(message, messageLength)
        assert em != None


def testSsaPkcs1V15SignAndVerify():
    print("testSsaPkcs1V15SignAndVerify")

    e = 65537
    N = IFC_APPROVED_LENGTHS[0]
    res = None
    while res == None:
        seed = RSA.getSeed(N)
        res = RSA.generateProbablePrimesWithConditions(e, N, seed, True)
    
    p, q = res
    f = (p - 1) * (q - 1)
    d = pow(e, -1, f)
    n = p * q

    for _ in range(10):
        messageLength = base.byteLength(n)
        message = base.getRandomBytes(messageLength)
        signature = RSA.ssaPkcs1v15Sign(d, n, message)
        assert RSA.ssaPkcs1V15Verify(e, n, message, signature)


def testGetParameters():
    print("testGetParameters")

    for _ in range(10):
        e, d, n, p, q = RSA.getParameters(256, forceWeak=True)
        message = base.bytesToInt(base.getRandomBytes(base.byteLength(n) - 1))
        
        encrypted = RSA.encrypt(e, n, message)
        decrypted = RSA.decrypt(d, n, encrypted)

        assert message == decrypted

    for _ in range(10):
        e, d, n, p, q = RSA.getParameters(512, forceWeak=True)
        message = base.bytesToInt(base.getRandomBytes(base.byteLength(n) - 1))
        
        encrypted = RSA.encrypt(e, n, message)
        decrypted = RSA.decrypt(d, n, encrypted)

        assert message == decrypted

    for _ in range(5):
        e, d, n, _, _ = RSA.getParameters(1024)
        maxLength = base.byteLength(n) - 2 * sha256().digest_size - 2
        message = base.getRandomBytes(maxLength)
        encrypted = RSA.oaepEncrypt(e, n, message)
        decrypted = RSA.oaepDecrypt(d, n, encrypted)
        assert message == decrypted
    
    for _ in range(5):
        e, d, n, _, _ = RSA.getParameters(2048)
        maxLength = base.byteLength(n) - 2 * sha256().digest_size - 2
        message = base.bytesToInt(base.getRandomBytes(maxLength))
        encrypted = RSA.encrypt(e, n, message)
        decrypted = RSA.decrypt(d, n, encrypted)
        assert message == decrypted


def testPrivateKeyFactorization():
    print("testPrivateKeyFactorization")

    for _ in range(10):
        e, d, n, p, q = RSA.getParameters(1024)
        fact = privateKeyFactorization(n, e, d)
        assert fact == (p, q) or fact == (q, p)


def testCommonModulusAttack():
    print("testCommonModulusAttack")
    
    for _ in range(10):
        e1, d, n, p, q = RSA.getParameters(1024)
        m = base.bytesToInt(base.getRandomBytes(1024 // 8 - 1))
        e2 = primality.getPrime(16)
        c1 = pow(m, e1, n)
        c2 = pow(m, e2, n)
        assert m == commonModulusAttack(c1, c2, e1, e2, n)


def testWienerAttack():
    print("testWienerAttack")

    for _ in range(50):
        d, e, n, p, q = RSA.getParameters(1024)
        m = base.bytesToInt(base.getRandomBytes(1024 // 8 - 1))
        c = pow(m, e, n)
        d_ = wienerAttack(n, e)
        assert d == d_
        assert pow(c, d_, n) == m


def testHastadAttack():
    print("testHastadAttack")

    for _ in range(10):
        e = 3
        message = base.bytesToInt(base.getRandomBytes(1024 // 8 - 1))
        modules = []
        ciphertexts = []

        for _ in range(e):
            p, q = RSA.generateProbablePrimes(e, 1024, forceWeak=True)
            n = p * q
            modules.append(n)
            ciphertexts.append(pow(message, e, n))

        start = datetime.now()
        m = hastadAttack(ciphertexts, modules, e)
        end = datetime.now()

        assert message == m
