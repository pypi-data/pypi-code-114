import usaepay
from usaepay import run_call


def delete(data={}):
	"""Calls /invoices/bulk
	Get invoice defaults
			Keys (list) required

	Returns:
		Dictionary Status
	"""
	params={}
	path='/invoices/bulk'
	data_list = data['Keys']
	return run_call('delete','json',path,data_list,params)
