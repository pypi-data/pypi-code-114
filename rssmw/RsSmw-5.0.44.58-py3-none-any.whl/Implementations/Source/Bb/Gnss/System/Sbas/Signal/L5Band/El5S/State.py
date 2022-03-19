from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, signal_state: bool, index=repcap.Index.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:SIGNal:L5Band:EL5S<US>:[STATe] \n
		Snippet: driver.source.bb.gnss.system.sbas.signal.l5Band.el5S.state.set(signal_state = False, index = repcap.Index.Default) \n
		Enables the corresponding signal from the GNSS system in the corresponding RF band. \n
			:param signal_state: 1| ON| 0| OFF
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
		"""
		param = Conversions.bool_to_str(signal_state)
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:SIGNal:L5Band:EL5S{index_cmd_val}:STATe {param}')

	def get(self, index=repcap.Index.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:SBAS:SIGNal:L5Band:EL5S<US>:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.system.sbas.signal.l5Band.el5S.state.get(index = repcap.Index.Default) \n
		Enables the corresponding signal from the GNSS system in the corresponding RF band. \n
			:param index: optional repeated capability selector. Default value: Nr1 (settable in the interface 'El5S')
			:return: signal_state: 1| ON| 0| OFF"""
		index_cmd_val = self._cmd_group.get_repcap_cmd_value(index, repcap.Index)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SYSTem:SBAS:SIGNal:L5Band:EL5S{index_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
