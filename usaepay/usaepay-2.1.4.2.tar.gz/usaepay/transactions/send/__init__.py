import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /transactions/{trankey}/send
	Email receipt for specific transaction.
			trankey (str) required
			Also can contain all fields from SendReceiptRequest

	Returns:
		Dictionary Status
	"""
	params={}
	if not 'trankey' in data:
		raise Exception('trankey required for transactions.send.post()')

	path='/transactions/' + data['trankey'] + '/send'
	return run_call('post','json',path,data,params)
