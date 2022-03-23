import astropayments
from astropayments import run_call


def get(data={}):
	"""Calls /publickey
	Retrieve a specific credit card token.

	Returns:
		String
	"""
	params={}
	path='/publickey'
	return run_call('get','string',path,data,params)
