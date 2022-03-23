import usaepay
from usaepay import run_call


def get(data={}):
	"""Calls /paymentengine/devices/{devicekey}/terminal-config
	Get a devices details
			devicekey (str) required

	Returns:
		Dictionary DeviceTerminalConfig
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.terminal-config.get()')

	path='/paymentengine/devices/' + data['devicekey'] + '/terminal-config'
	return run_call('get','json',path,data,params)

def put(data={}):
	"""Calls /paymentengine/devices/{devicekey}/terminal-config
	Register a device
			devicekey (str) required
			Also can contain all fields from DeviceTerminalConfig

	Returns:
		Dictionary DeviceResponse
	"""
	params={}
	if not 'devicekey' in data:
		raise Exception('devicekey required for paymentengine.devices.terminal-config.put()')

	path='/paymentengine/devices/' + data['devicekey'] + '/terminal-config'
	return run_call('put','json',path,data,params)
