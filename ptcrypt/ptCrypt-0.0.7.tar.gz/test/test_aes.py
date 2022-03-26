from pydoc import plain
from unittest import result
from ptCrypt.Symmetric.AES import AES


def testStateToBytes():
    input = bytes.fromhex("00112233445566778899aabbccddeeff")
    check = [
        [0x00, 0x44, 0x88, 0xcc],
        [0x11, 0x55, 0x99, 0xdd],
        [0x22, 0x66, 0xaa, 0xee],
        [0x33, 0x77, 0xbb, 0xff]
    ]
    assert AES.bytesToState(input) == check
    assert AES.stateToBytes(check) == input

def testSubBytes():

    data = [[i] for i in range(256)]
    AES.subBytes(data)
    i = 0
    for l in data:
        assert l[0] == AES.SBox[i]
        i += 1

    AES.invSubBytes(data)
    assert data == [[i] for i in range(256)]


def testShiftRows():
    state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    check1 = [[1, 2, 3, 4], [6, 7, 8, 5], [11, 12, 9, 10], [16, 13, 14, 15]]
    check2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    AES.shiftRows(state)
    assert state == check1

    AES.invShiftRows(state)
    assert state == check2


def testMixColumns():
    # Test data is taken from FIPS-197, Appendix B, round 1

    state = [
        [0xd4, 0xe0, 0xb8, 0x1e],
        [0xbf, 0xb4, 0x41, 0x27],
        [0x5d, 0x52, 0x11, 0x98],
        [0x30, 0xae, 0xf1, 0xe5]
    ]

    check1 = [
        [0x04, 0xe0, 0x48, 0x28],
        [0x66, 0xcb, 0xf8, 0x06],
        [0x81, 0x19, 0xd3, 0x26],
        [0xe5, 0x9a, 0x7a, 0x4c]
    ]

    check2 = [
        [0xd4, 0xe0, 0xb8, 0x1e],
        [0xbf, 0xb4, 0x41, 0x27],
        [0x5d, 0x52, 0x11, 0x98],
        [0x30, 0xae, 0xf1, 0xe5]
    ]

    AES.mixColumns(state)
    assert state == check1

    AES.invMixColumns(state)
    assert state == check2


def testAddRoundKey():
    # Test data is taken from FIPS-197, Appendix B round 0
    state = [
        [0x32, 0x88, 0x31, 0xe0],
        [0x43, 0x5a, 0x31, 0x37],
        [0xf6, 0x30, 0x98, 0x07],
        [0xa8, 0x8d, 0xa2, 0x34]
    ]

    key = b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c"

    check = [
        [0x19, 0xa0, 0x9a, 0xe9],
        [0x3d, 0xf4, 0xc6, 0xf8],
        [0xe3, 0xe2, 0x8d, 0x48],
        [0xbe, 0x2b, 0x2a, 0x08]
    ]

    AES.addRoundKey(state, key)
    assert state == check


def testKeyExapnsion():
    # Test data is taken from FIPS-197, Appendix A
    key1 = b"\x2b\x7e\x15\x16\x28\xae\xd2\xa6\xab\xf7\x15\x88\x09\xcf\x4f\x3c"
    check1 = [
        bytes.fromhex("2b7e151628aed2a6abf7158809cf4f3c"),
        bytes.fromhex("a0fafe1788542cb123a339392a6c7605"),
        bytes.fromhex("f2c295f27a96b9435935807a7359f67f"),
        bytes.fromhex("3d80477d4716fe3e1e237e446d7a883b"),
        bytes.fromhex("ef44a541a8525b7fb671253bdb0bad00"),
        bytes.fromhex("d4d1c6f87c839d87caf2b8bc11f915bc"),
        bytes.fromhex("6d88a37a110b3efddbf98641ca0093fd"),
        bytes.fromhex("4e54f70e5f5fc9f384a64fb24ea6dc4f"),
        bytes.fromhex("ead27321b58dbad2312bf5607f8d292f"),
        bytes.fromhex("ac7766f319fadc2128d12941575c006e"),
        bytes.fromhex("d014f9a8c9ee2589e13f0cc8b6630ca6")
    ]

    exp1 = AES.keyExpansion(key1)
    assert exp1 == check1

    key2 = bytes.fromhex("8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b")
    check2 = [
        bytes.fromhex("8e73b0f7da0e6452c810f32b809079e5"),
        bytes.fromhex("62f8ead2522c6b7bfe0c91f72402f5a5"),
        bytes.fromhex("ec12068e6c827f6b0e7a95b95c56fec2"),
        bytes.fromhex("4db7b4bd69b5411885a74796e92538fd"),
        bytes.fromhex("e75fad44bb095386485af05721efb14f"),
        bytes.fromhex("a448f6d94d6dce24aa326360113b30e6"),
        bytes.fromhex("a25e7ed583b1cf9a27f939436a94f767"),
        bytes.fromhex("c0a69407d19da4e1ec1786eb6fa64971"),
        bytes.fromhex("485f703222cb8755e26d135233f0b7b3"),
        bytes.fromhex("40beeb282f18a2596747d26b458c553e"),
        bytes.fromhex("a7e1466c9411f1df821f750aad07d753"),
        bytes.fromhex("ca4005388fcc5006282d166abc3ce7b5"),
        bytes.fromhex("e98ba06f448c773c8ecc720401002202")
    ]

    exp2 = AES.keyExpansion(key2)
    assert exp2 == check2

    key3 = bytes.fromhex("603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4")
    check3 = [
        bytes.fromhex("603deb1015ca71be2b73aef0857d7781"),
        bytes.fromhex("1f352c073b6108d72d9810a30914dff4"),
        bytes.fromhex("9ba354118e6925afa51a8b5f2067fcde"),
        bytes.fromhex("a8b09c1a93d194cdbe49846eb75d5b9a"),
        bytes.fromhex("d59aecb85bf3c917fee94248de8ebe96"),
        bytes.fromhex("b5a9328a2678a647983122292f6c79b3"),
        bytes.fromhex("812c81addadf48ba24360af2fab8b464"),
        bytes.fromhex("98c5bfc9bebd198e268c3ba709e04214"),
        bytes.fromhex("68007bacb2df331696e939e46c518d80"),
        bytes.fromhex("c814e20476a9fb8a5025c02d59c58239"),
        bytes.fromhex("de1369676ccc5a71fa2563959674ee15"),
        bytes.fromhex("5886ca5d2e2f31d77e0af1fa27cf73c3"),
        bytes.fromhex("749c47ab18501ddae2757e4f7401905a"),
        bytes.fromhex("cafaaae3e4d59b349adf6acebd10190d"),
        bytes.fromhex("fe4890d1e6188d0b046df344706c631e")
    ]

    exp3 = AES.keyExpansion(key3)
    assert exp3 == check3


def testEncryptDecrypt():
    # Test data is taken from FIPS-197, Appendix C
    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")
    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    check = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
    cipher = AES(key)

    assert cipher.encrypt(plaintext) == check
    assert cipher.decrypt(check) == plaintext

    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f1011121314151617")
    check = bytes.fromhex("dda97ca4864cdfe06eaf70a0ec0d7191")
    cipher = AES(key)

    assert cipher.encrypt(plaintext) == check
    assert cipher.decrypt(check) == plaintext

    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f")
    check = bytes.fromhex("8ea2b7ca516745bfeafc49904b496089")
    cipher = AES(key)

    assert cipher.encrypt(plaintext) == check
    assert cipher.decrypt(check) == plaintext