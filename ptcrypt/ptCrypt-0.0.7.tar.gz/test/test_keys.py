from ptCrypt.Util.keys import ECC_APPROVED_LENGTHS, FFC_APPROVED_LENGTHS, IFC_APPROVED_LENGTHS, getECCKeyLength, getECCSecurityLevel, getFFCKeyLength, getFFCSecurityLevel, getIFCAuxiliaryPrimesLegths, getIFCKeyLength, getIFCSecurityLevel


def testGetFFCSecurityLevel():

    assert getFFCSecurityLevel(123, 123) == 0

    N, L = FFC_APPROVED_LENGTHS[0]
    assert getFFCSecurityLevel(N, L) == 80

    N, L = FFC_APPROVED_LENGTHS[1]
    assert getFFCSecurityLevel(N, L) == 112

    N, L = FFC_APPROVED_LENGTHS[2]
    assert getFFCSecurityLevel(N, L) == 128

    N, L = FFC_APPROVED_LENGTHS[3]
    assert getFFCSecurityLevel(N, L) == 192

    N, L = FFC_APPROVED_LENGTHS[4]
    assert getFFCSecurityLevel(N, L) == 256


def testGetIFCSecurityLevel():

    assert getIFCSecurityLevel(123) == 0

    N = IFC_APPROVED_LENGTHS[0]
    assert getIFCSecurityLevel(N) == 80

    N = IFC_APPROVED_LENGTHS[1]
    assert getIFCSecurityLevel(N) == 112

    N = IFC_APPROVED_LENGTHS[2]
    assert getIFCSecurityLevel(N) == 128

    N = IFC_APPROVED_LENGTHS[3]
    assert getIFCSecurityLevel(N) == 192

    N = IFC_APPROVED_LENGTHS[4]
    assert getIFCSecurityLevel(N) == 256


def testGetECCSecurityLevel():

    assert getECCSecurityLevel(100) == 0

    N = ECC_APPROVED_LENGTHS[0]
    assert getECCSecurityLevel(N) == 80

    N = ECC_APPROVED_LENGTHS[1]
    assert getECCSecurityLevel(N) == 112

    N = ECC_APPROVED_LENGTHS[2]
    assert getECCSecurityLevel(N) == 128

    N = ECC_APPROVED_LENGTHS[3]
    assert getECCSecurityLevel(N) == 192

    N = ECC_APPROVED_LENGTHS[4]
    assert getECCSecurityLevel(N) == 256


def testGetFFCKeyLength():
    assert getFFCKeyLength(79) == FFC_APPROVED_LENGTHS[0]
    assert getFFCKeyLength(80) == FFC_APPROVED_LENGTHS[0]
    assert getFFCKeyLength(81) == FFC_APPROVED_LENGTHS[1]
    assert getFFCKeyLength(112) == FFC_APPROVED_LENGTHS[1]
    assert getFFCKeyLength(113) == FFC_APPROVED_LENGTHS[2]
    assert getFFCKeyLength(128) == FFC_APPROVED_LENGTHS[2]
    assert getFFCKeyLength(129) == FFC_APPROVED_LENGTHS[3]
    assert getFFCKeyLength(192) == FFC_APPROVED_LENGTHS[3]
    assert getFFCKeyLength(194) == FFC_APPROVED_LENGTHS[4]
    assert getFFCKeyLength(256) == FFC_APPROVED_LENGTHS[4]
    assert getFFCKeyLength(512) == FFC_APPROVED_LENGTHS[4]


def testGetIFCKeylength():
    assert getIFCKeyLength(79) == IFC_APPROVED_LENGTHS[0]
    assert getIFCKeyLength(80) == IFC_APPROVED_LENGTHS[0]
    assert getIFCKeyLength(81) == IFC_APPROVED_LENGTHS[1]
    assert getIFCKeyLength(112) == IFC_APPROVED_LENGTHS[1]
    assert getIFCKeyLength(113) == IFC_APPROVED_LENGTHS[2]
    assert getIFCKeyLength(128) == IFC_APPROVED_LENGTHS[2]
    assert getIFCKeyLength(129) == IFC_APPROVED_LENGTHS[3]
    assert getIFCKeyLength(192) == IFC_APPROVED_LENGTHS[3]
    assert getIFCKeyLength(194) == IFC_APPROVED_LENGTHS[4]
    assert getIFCKeyLength(256) == IFC_APPROVED_LENGTHS[4]
    assert getIFCKeyLength(512) == IFC_APPROVED_LENGTHS[4]


def testGetECCKeyLength():
    assert getECCKeyLength(79) == ECC_APPROVED_LENGTHS[0]
    assert getECCKeyLength(80) == ECC_APPROVED_LENGTHS[0]
    assert getECCKeyLength(81) == ECC_APPROVED_LENGTHS[1]
    assert getECCKeyLength(112) == ECC_APPROVED_LENGTHS[1]
    assert getECCKeyLength(113) == ECC_APPROVED_LENGTHS[2]
    assert getECCKeyLength(128) == ECC_APPROVED_LENGTHS[2]
    assert getECCKeyLength(129) == ECC_APPROVED_LENGTHS[3]
    assert getECCKeyLength(192) == ECC_APPROVED_LENGTHS[3]
    assert getECCKeyLength(194) == ECC_APPROVED_LENGTHS[4]
    assert getECCKeyLength(256) == ECC_APPROVED_LENGTHS[4]
    assert getECCKeyLength(512) == ECC_APPROVED_LENGTHS[4]


def testGetIFCAuxiliaryPrimesLengths():

    N = 1024
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, True)
        assert p1Len > 100 and p2Len > 100 and p1Len + p2Len < 496
    
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, False)
        assert p1Len > 100 and p2Len > 100 and p1Len + p2Len < 239
    
    N = 2048
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, True)
        assert p1Len > 140 and p2Len > 140 and p1Len + p2Len < 1007
    
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, False)
        assert p1Len > 140 and p2Len > 140 and p1Len + p2Len < 494
    
    N = 3072
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, True)
        assert p1Len > 170 and p2Len > 170 and p1Len + p2Len < 1518
    
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, False)
        assert p1Len > 170 and p2Len > 170 and p1Len + p2Len < 750
    print(5)
    
    N = 7680
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, True)
        assert p1Len > 300 and p2Len > 300 and p1Len + p2Len < 3822
    
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, False)
        assert p1Len > 300 and p2Len > 300 and p1Len + p2Len < 1901
    
    N = 15360
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, True)
        assert p1Len > 510 and p2Len > 510 and p1Len + p2Len < 7661
    
    for _ in range(100):
        p1Len, p2Len = getIFCAuxiliaryPrimesLegths(N, False)
        assert p1Len > 510 and p2Len > 510 and p1Len + p2Len < 3820
