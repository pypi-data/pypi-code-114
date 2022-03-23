from cryptography.hazmat.primitives.serialization import load_der_public_key, load_der_private_key
from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PrivateFormat
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.primitives.serialization import NoEncryption
from cryptography.hazmat.backends import default_backend

BACKEND = default_backend()

def export_private_key(private_key) -> bytes:
	""" Export a private key object as a bytes type. """

	return private_key.private_bytes(encoding = Encoding.DER, format = PrivateFormat.PKCS8, encryption_algorithm = NoEncryption())

def export_public_key(public_key) -> bytes:
	""" Export a public key object as a bytes type. """

	return public_key.public_bytes(encoding = Encoding.DER, format = PublicFormat.SubjectPublicKeyInfo)

def import_private_key(private_key: bytes):
	""" Import a bytes type private key as a private key object. """

	return load_der_private_key(private_key, password = None, backend = BACKEND)

def import_public_key(public_key: bytes):
	""" Import a bytes type public key as a public key object. """

	return load_der_public_key(public_key, backend = BACKEND)
