from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, carrier=repcap.Carrier.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EVDO:UP:MC:CARRier<CH>:STATe \n
		Snippet: driver.source.bb.evdo.up.mc.carrier.state.set(state = False, carrier = repcap.Carrier.Default) \n
		Switches the selected carrier on or off. \n
			:param state: 1| ON| 0| OFF
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
		"""
		param = Conversions.bool_to_str(state)
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EVDO:UP:MC:CARRier{carrier_cmd_val}:STATe {param}')

	def get(self, carrier=repcap.Carrier.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:EVDO:UP:MC:CARRier<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.evdo.up.mc.carrier.state.get(carrier = repcap.Carrier.Default) \n
		Switches the selected carrier on or off. \n
			:param carrier: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Carrier')
			:return: state: 1| ON| 0| OFF"""
		carrier_cmd_val = self._cmd_group.get_repcap_cmd_value(carrier, repcap.Carrier)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EVDO:UP:MC:CARRier{carrier_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
