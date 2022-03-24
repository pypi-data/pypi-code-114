import os
import json
import requests
from base64 import b64encode
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

publicPem='./AnaplanPublicKey.pem'
privatePem='./AnaplanPrivateKey.pem'

# Create header
with open(publicPem,'r') as file:
    publicPemText = file.read()

header = {
    'Authorization': f'CACertificate {b64encode(publicPemText.encode("utf-8")).decode("utf-8")}',
    'Content-Type' : 'application/json',
}

# Create body
randomBytes = os.urandom(150)
encodedData = str(b64encode(randomBytes).decode('utf-8'))


with open(privatePem, 'r') as file:
    privateKey = serialization.load_pem_private_key(file.read().encode('utf-8'),None,backend=default_backend())
signature = privateKey.sign(randomBytes,padding.PKCS1v15(), hashes.SHA512())
encodedSignedData = b64encode(signature).decode('utf-8')

body = {
    'encodedData' : encodedData,
    'encodedSignedData' : encodedSignedData,
}

res = requests.post('https://auth.anaplan.com/token/authenticate',data=json.dumps(body),headers=header)
print('URL')
print(res.request.url)
print('HEADER')
print(res.request.headers)
print('BODY')
print(res.request.body)
print('RESPONSE')
print(res.text)