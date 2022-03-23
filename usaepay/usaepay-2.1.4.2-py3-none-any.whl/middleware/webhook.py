import hmac, hashlib
import usaepay

def verify(json_payload,signature,signature_key):
	"""Verify webhook signature

	Args:
		json_payload (str) required json formatted payload as string
		signature (str) required the signature you received and need to verify
		signature_key (str) required signature_key set for webhook

	Returns: Boolean

	"""
	expected_signature = hmac.new(signature_key.encode('utf-8'),json_payload.encode('utf-8'),digestmod=hashlib.sha256).hexdigest()
	return hmac.compare_digest(expected_signature,signature)