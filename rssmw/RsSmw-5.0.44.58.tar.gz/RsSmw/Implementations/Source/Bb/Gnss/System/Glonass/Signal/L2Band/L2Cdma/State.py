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

	def set(self, signal_state: bool, indexNull=repcap.IndexNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:L2CDma<US0>:[STATe] \n
		Snippet: driver.source.bb.gnss.system.glonass.signal.l2Band.l2Cdma.state.set(signal_state = False, indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param signal_state: No help available
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2Cdma')
		"""
		param = Conversions.bool_to_str(signal_state)
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:L2CDma{indexNull_cmd_val}:STATe {param}')

	def get(self, indexNull=repcap.IndexNull.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:L2CDma<US0>:[STATe] \n
		Snippet: value: bool = driver.source.bb.gnss.system.glonass.signal.l2Band.l2Cdma.state.get(indexNull = repcap.IndexNull.Default) \n
		No command help available \n
			:param indexNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'L2Cdma')
			:return: signal_state: No help available"""
		indexNull_cmd_val = self._cmd_group.get_repcap_cmd_value(indexNull, repcap.IndexNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SYSTem:GLONass:SIGNal:L2Band:L2CDma{indexNull_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
