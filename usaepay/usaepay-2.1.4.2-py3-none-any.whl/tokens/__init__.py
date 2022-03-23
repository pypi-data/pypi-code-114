import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /tokens
	Generate a credit card token

	Args:
		data (dict) TokenRequest

	Returns:
		Dictionary TokenResponse
	"""
	params={}
	path='/tokens'
	return run_call('post','json',path,data,params)

def get(data={}):
	"""Calls /tokens/{cardref}
	Retrieve a specific credit card token.
			cardref (str) required

	Returns:
		Dictionary Token
	"""
	params={}
	if not 'cardref' in data:
		raise Exception('cardref required for tokens.get()')

	path='/tokens'+ '/' + data['cardref']
	return run_call('get','json',path,data,params)
