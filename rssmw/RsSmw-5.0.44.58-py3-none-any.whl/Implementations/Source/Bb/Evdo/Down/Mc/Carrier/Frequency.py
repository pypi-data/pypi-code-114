from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:CARRier<CH>:FREQuency \n
		Snippet: driver.source.bb.evdo.down.mc.carrier.frequency.set(frequency = 1.0, carrier = repcap.Carrier.Default) \n
		Sets the center frequency of the carrier in MHz. In some cases, not all center frequencies are defined by the selected
		band class. In case a non-existing frequency is input, the next available frequency is used. \n
			:param frequency: float Range: 100 to 3000
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:DOWN:MC:CARRier{carrier_cmd_val}:FREQuency {param}')

	def get(self, carrier=repcap.Carrier.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EVDO:DOWN:MC:CARRier<CH>:FREQuency \n
		Snippet: value: float = driver.source.bb.evdo.down.mc.carrier.frequency.get(carrier = repcap.Carrier.Default) \n
		Sets the center frequency of the carrier in MHz. In some cases, not all center frequencies are defined by the selected
		band class. In case a non-existing frequency is input, the next available frequency is used. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: frequency: float Range: 100 to 3000"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:DOWN:MC:CARRier{carrier_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)
