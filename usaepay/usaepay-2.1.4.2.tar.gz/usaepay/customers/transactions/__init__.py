import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /customers/{custkey}/transactions
	Retrieve a existing customer
			custkey (str) required

	Returns:
		Dictionary TransactionList
	"""
	params={}
	if not 'custkey' in data:
		raise Exception('custkey required for customers.transactions.get()')

	path='/customers/' + data['custkey'] + '/transactions'
	return run_call('get','json',path,data,params)
