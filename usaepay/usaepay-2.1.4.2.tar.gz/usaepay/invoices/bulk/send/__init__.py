import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /invoices/bulk/send
	Get invoice defaults
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	path='/invoices/bulk/send'
	data_list = data['Keys']
	return run_call('post','json',path,data_list,params)
