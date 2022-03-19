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

	def set(self, state: bool, addressField=repcap.AddressField.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:ADDRess<ST>:STATe \n
		Snippet: driver.source.bb.wlad.pconfig.mac.address.state.set(state = False, addressField = repcap.AddressField.Default) \n
		Activates/deactivates the selected address field. \n
			:param state: 0| 1| OFF| ON
			:param addressField: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
		"""
		param = Conversions.bool_to_str(state)
		addressField_cmd_val = self._cmd_group.get_repcap_cmd_value(addressField, repcap.AddressField)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:ADDRess{addressField_cmd_val}:STATe {param}')

	def get(self, addressField=repcap.AddressField.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:MAC:ADDRess<ST>:STATe \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.mac.address.state.get(addressField = repcap.AddressField.Default) \n
		Activates/deactivates the selected address field. \n
			:param addressField: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
			:return: state: 0| 1| OFF| ON"""
		addressField_cmd_val = self._cmd_group.get_repcap_cmd_value(addressField, repcap.AddressField)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:WLAD:PCONfig:MAC:ADDRess{addressField_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
