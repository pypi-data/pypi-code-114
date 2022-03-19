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

	def set(self, state: bool, offsetNull=repcap.OffsetNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet<CH0>:STATe \n
		Snippet: driver.source.bb.btooth.econfiguration.pconfiguration.offset.state.set(state = False, offsetNull = repcap.OffsetNull.Default) \n
		Enables / disables Offset0 to Offset5 of the offset setting table. \n
			:param state: 1| ON| 0| OFF
			:param offsetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Offset')
		"""
		param = Conversions.bool_to_str(state)
		offsetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(offsetNull, repcap.OffsetNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet{offsetNull_cmd_val}:STATe {param}')

	def get(self, offsetNull=repcap.OffsetNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet<CH0>:STATe \n
		Snippet: value: bool = driver.source.bb.btooth.econfiguration.pconfiguration.offset.state.get(offsetNull = repcap.OffsetNull.Default) \n
		Enables / disables Offset0 to Offset5 of the offset setting table. \n
			:param offsetNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Offset')
			:return: state: 1| ON| 0| OFF"""
		offsetNull_cmd_val = self._cmd_group.get_repcap_cmd_value(offsetNull, repcap.OffsetNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:BTOoth:ECONfiguration:PCONfiguration:OFFSet{offsetNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
