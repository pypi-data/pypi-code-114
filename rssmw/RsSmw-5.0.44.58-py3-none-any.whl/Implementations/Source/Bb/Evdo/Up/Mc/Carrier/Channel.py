from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)

	def set(self, channel_param: int, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:UP:MC:CARRier<CH>:CHANnel \n
		Snippet: driver.source.bb.evdo.up.mc.carrier.channel.set(channel_param = 1, carrier = repcap.Carrier.Default) \n
		Sets carrier’s CDMA channel number. The available Channel values depend on the selected Band Class. In some cases, not
		all channel numbers can be used. In case a non-existing channel is input, the next available channel is used. \n
			:param channel_param: integer Range: 0 to 3000
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(channel_param)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:UP:MC:CARRier{carrier_cmd_val}:CHANnel {param}')

	def get(self, carrier=repcap.Carrier.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EVDO:UP:MC:CARRier<CH>:CHANnel \n
		Snippet: value: int = driver.source.bb.evdo.up.mc.carrier.channel.get(carrier = repcap.Carrier.Default) \n
		Sets carrier’s CDMA channel number. The available Channel values depend on the selected Band Class. In some cases, not
		all channel numbers can be used. In case a non-existing channel is input, the next available channel is used. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: channel_param: No help available"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:UP:MC:CARRier{carrier_cmd_val}:CHANnel?')
		return Conversions.str_to_int(response)
