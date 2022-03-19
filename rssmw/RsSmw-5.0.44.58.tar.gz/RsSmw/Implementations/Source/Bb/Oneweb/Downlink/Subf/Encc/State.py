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

	def set(self, state: bool, subframeNull=repcap.SubframeNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:STATe \n
		Snippet: driver.source.bb.oneweb.downlink.subf.encc.state.set(state = False, subframeNull = repcap.SubframeNull.Default) \n
		Enables/disables the PDCCH and PCFICH allocation. \n
			:param state: 0| 1| OFF| ON
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
		"""
		param = Conversions.bool_to_str(state)
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:STATe {param}')

	def get(self, subframeNull=repcap.SubframeNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ONEWeb:DL:[SUBF<ST0>]:ENCC:STATe \n
		Snippet: value: bool = driver.source.bb.oneweb.downlink.subf.encc.state.get(subframeNull = repcap.SubframeNull.Default) \n
		Enables/disables the PDCCH and PCFICH allocation. \n
			:param subframeNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subf')
			:return: state: 0| 1| OFF| ON"""
		subframeNull_cmd_val = self._cmd_group.get_repcap_cmd_value(subframeNull, repcap.SubframeNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ONEWeb:DL:SUBF{subframeNull_cmd_val}:ENCC:STATe?')
		return Conversions.str_to_bool(response)
