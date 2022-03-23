import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /paymentengine/payrequests/{requestkey}/confirm
	Confirm the status of a transaction
			requestkey (str) required
			Also can contain all fields from PayRequestConfirm

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'requestkey' in data:
		raise Exception('requestkey required for paymentengine.payrequests.confirm.post()')

	path='/paymentengine/payrequests/' + data['requestkey'] + '/confirm'
	return run_call('post','json',path,data,params)
