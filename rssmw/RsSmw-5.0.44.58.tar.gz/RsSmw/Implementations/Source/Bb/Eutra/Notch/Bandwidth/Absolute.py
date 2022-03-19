from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	def set(self, bw_hz: int, notchFilter=repcap.NotchFilter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh<CH>:BWIDth:[ABSolute] \n
		Snippet: driver.source.bb.eutra.notch.bandwidth.absolute.set(bw_hz = 1, notchFilter = repcap.NotchFilter.Default) \n
		Sets the absolute notch bandwidth. The value is interdependent with the relative bandwidth value, set with the command
		[:SOURce<hw>]:BB:ARBitrary:NOTCh<ch>:BWIDth:RELative. That is, you cna set the notch bandwidth in either way. \n
			:param bw_hz: float Range: 0 to dynamic
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(bw_hz)
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:NOTCh{notchFilter_cmd_val}:BWIDth:ABSolute {param}')

	def get(self, notchFilter=repcap.NotchFilter.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:NOTCh<CH>:BWIDth:[ABSolute] \n
		Snippet: value: int = driver.source.bb.eutra.notch.bandwidth.absolute.get(notchFilter = repcap.NotchFilter.Default) \n
		Sets the absolute notch bandwidth. The value is interdependent with the relative bandwidth value, set with the command
		[:SOURce<hw>]:BB:ARBitrary:NOTCh<ch>:BWIDth:RELative. That is, you cna set the notch bandwidth in either way. \n
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: bw_hz: No help available"""
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:NOTCh{notchFilter_cmd_val}:BWIDth:ABSolute?')
		return Conversions.str_to_int(response)
