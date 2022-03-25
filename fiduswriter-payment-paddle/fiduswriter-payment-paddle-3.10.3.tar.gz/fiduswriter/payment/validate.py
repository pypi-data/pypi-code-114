# Adapted from
# https://developer.paddle.com/webhook-reference/verifying-webhooks

from django.conf import settings

import collections
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA1
from Crypto.Signature import PKCS1_v1_5
import phpserialize


def validate_webhook_request(query_dict):
    input_data = dict(query_dict)
    # Convert key from PEM to DER - Strip the first and last lines and
    # newlines, and decode
    public_key_encoded = settings.PADDLE_PUBLIC_KEY[26:-25].replace("\n", "")
    public_key_der = base64.b64decode(public_key_encoded)

    # input_data represents all of the POST fields sent with the request
    # Get the p_signature parameter & base64 decode it.
    signature = input_data["p_signature"][0]

    # Remove the p_signature parameter
    del input_data["p_signature"]

    # Ensure all the data fields are strings
    for field in input_data:
        input_data[field] = str(input_data[field][0])

    # Sort the data
    sorted_data = collections.OrderedDict(sorted(input_data.items()))

    # and serialize the fields
    serialized_data = phpserialize.dumps(sorted_data)

    # verify the data
    key = RSA.importKey(public_key_der)
    digest = SHA1.new()
    digest.update(serialized_data)
    verifier = PKCS1_v1_5.new(key)
    signature = base64.b64decode(signature)
    if verifier.verify(digest, signature):
        return True
    else:
        return False
