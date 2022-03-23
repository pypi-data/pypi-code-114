import usaepay
from usaepay import run_call


def post(data={}):
	"""Calls /paymentengine/devices/{devicekey}/kick
	Kick a device offline
			devicekey (str) required

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.kick.post()')

	path='/paymentengine/devices/' + data['devicekey'] + '/kick'
	return run_call('post','json',path,data,params)
