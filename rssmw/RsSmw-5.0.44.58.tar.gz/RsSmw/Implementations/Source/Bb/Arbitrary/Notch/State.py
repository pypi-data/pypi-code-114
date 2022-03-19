from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, val_enable: bool, notchFilter=repcap.NotchFilter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:NOTCh<CH>:STATe \n
		Snippet: driver.source.bb.arbitrary.notch.state.set(val_enable = False, notchFilter = repcap.NotchFilter.Default) \n
		Enables the particular notch. \n
			:param val_enable: 1| ON| 0| OFF
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.bool_to_str(val_enable)
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:NOTCh{notchFilter_cmd_val}:STATe {param}')

	def get(self, notchFilter=repcap.NotchFilter.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:NOTCh<CH>:STATe \n
		Snippet: value: bool = driver.source.bb.arbitrary.notch.state.get(notchFilter = repcap.NotchFilter.Default) \n
		Enables the particular notch. \n
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: val_enable: 1| ON| 0| OFF"""
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:NOTCh{notchFilter_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
