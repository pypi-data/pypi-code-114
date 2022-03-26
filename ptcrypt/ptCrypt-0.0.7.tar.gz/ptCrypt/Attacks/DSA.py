from ptCrypt.Asymmetric import DSA


def repeatedSecretAttack(
    p: int,
    q: int,
    message1: any,
    r1: int,
    s1: int, 
    message2: any,
    r2: int,
    s2: int,
    hashFunction: callable = None
) -> int:
    """This attack requires two distinct messages and their signatures. 
    If two messages were signed with same private key and same secret value, 
    this function will return valid private key for DSA.

    Note that function can receive messages either as integer values, or as bytes.
    If bytes are passed, they will be processed into integers according to FIPS 186-4, 
    i.e. with DSA.prepareMessage function.

    Note also, that if messages are passed as integers, then hash function does not affect anything

    Parameters:
        message1: bytes
            first message
        
        signature1: DSA.Signature
            first message's signature
        
        message2: bytes
            second message
        
        signature2: DSA.Signature
            second message's signature

    Returns:
        result: int
            Recovered private key or None, if the attack has failed
    """

    if type(message1) is bytes:
        message1 = DSA.prepareMessage(message1, q, hashFunction)
    
    if type(message2) is bytes:
        message2 = DSA.prepareMessage(message2, q, hashFunction)

    diff = pow((s1 - s2) % q, -1, q)
    hashDiff = (message1 - message2) % q

    k = (hashDiff * diff) % q
    
    rInv = pow(r1, -1, q)
    x1 = (rInv * (s1 * k - message1)) % q
    x2 = (rInv * (s2 * k - message2)) % q

    if x1 == x2: return x1
    else: return None
