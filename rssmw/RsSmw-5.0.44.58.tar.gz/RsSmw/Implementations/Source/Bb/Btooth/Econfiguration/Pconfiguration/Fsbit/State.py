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

	def set(self, state: bool, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:FSBit<CH0>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.fsbit.state.set(state = False, indexNull = repcap.IndexNull.Default) \n
		Enables / disables features, related to bit numbers 0 to 27 for the used feature set. See also Table 'Link layer
		features: Bit number and feature'. Information is transmitted via LL_FEATURE_REQ, LL_FEATURE_RSP,
		LL_PERIPHERAL_FEATURE_REQ. \n
			:param state: 1| ON| 0| OFF
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Fsbit')
		"""
		param = Conversions.bool_to_str(state)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:FSBit{indexNull_cmd_val}:STATe {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:FSBit<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.fsbit.state.get(indexNull = repcap.IndexNull.Default) \n
		Enables / disables features, related to bit numbers 0 to 27 for the used feature set. See also Table 'Link layer
		features: Bit number and feature'. Information is transmitted via LL_FEATURE_REQ, LL_FEATURE_RSP,
		LL_PERIPHERAL_FEATURE_REQ. \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Fsbit')
			:return: state: 1| ON| 0| OFF"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:FSBit{indexNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
