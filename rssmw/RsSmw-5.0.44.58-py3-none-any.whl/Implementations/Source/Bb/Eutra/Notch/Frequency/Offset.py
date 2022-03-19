from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, freq_offset: int, notchFilter=repcap.NotchFilter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh<CH>:FREQuency:OFFSet \n
		Snippet: driver.source.bb.eutra.notch.frequency.offset.set(freq_offset = 1, notchFilter = repcap.NotchFilter.Default) \n
		Specifies the center frequency of the notch \n
			:param freq_offset: integer Range: -2000E6 to 2000E6
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(freq_offset)
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOTCh{notchFilter_cmd_val}:FREQuency:OFFSet {param}')

	def get(self, notchFilter=repcap.NotchFilter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh<CH>:FREQuency:OFFSet \n
		Snippet: value: int = driver.source.bb.eutra.notch.frequency.offset.get(notchFilter = repcap.NotchFilter.Default) \n
		Specifies the center frequency of the notch \n
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: freq_offset: No help available"""
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:NOTCh{notchFilter_cmd_val}:FREQuency:OFFSet?')
		return Conversions.str_to_int(response)
