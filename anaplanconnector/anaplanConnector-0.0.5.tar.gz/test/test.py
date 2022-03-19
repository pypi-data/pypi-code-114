import base64
import requests
import json
import random
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding




# Cert
with open('./AnaplanPrivateKey.pem','r') as file:
    certText = base64.b64encode(file.read())

cert = base64.b64encode(certText.encode('utf-8')).decode('utf-8')

# Random String
random = "%030x" % random.randrange(16 ** 150)

# Signed String
backend = default_backend()
key = serialization.load_pem_private_key()

headers = {
    'authorization' : f'CACertificate {cert}',
    'Content-Type' : 'application/json'
}

data = {
    'encodedData' : random,
    'encodedSignedData': 
}

jsonData = json.dumps(data)
requests.request('POST','https://auth.anaplan.com/token/authenticate', headers=headers, data=jsonData)