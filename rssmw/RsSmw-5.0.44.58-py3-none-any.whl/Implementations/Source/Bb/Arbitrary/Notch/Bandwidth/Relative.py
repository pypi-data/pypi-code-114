from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, no_bw_rel: float, notchFilter=repcap.NotchFilter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:NOTCh<CH>:BWIDth:RELative \n
		Snippet: driver.source.bb.arbitrary.notch.bandwidth.relative.set(no_bw_rel = 1.0, notchFilter = repcap.NotchFilter.Default) \n
		Sets the notch bandwidth relative to current clock frequency ([:SOURce<hw>]:BB:ARBitrary:NOTCh:CLOCk?) . The value is
		interdependet with the absolute bandwidth value,
		set with the command [:SOURce<hw>]:BB:ARBitrary:NOTCh<ch>:BWIDth[:ABSolute]. That is, you cna set the notch bandwidth in
		either way. \n
			:param no_bw_rel: float Range: 0 to 10
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(no_bw_rel)
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:NOTCh{notchFilter_cmd_val}:BWIDth:RELative {param}')

	def get(self, notchFilter=repcap.NotchFilter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:NOTCh<CH>:BWIDth:RELative \n
		Snippet: value: float = driver.source.bb.arbitrary.notch.bandwidth.relative.get(notchFilter = repcap.NotchFilter.Default) \n
		Sets the notch bandwidth relative to current clock frequency ([:SOURce<hw>]:BB:ARBitrary:NOTCh:CLOCk?) . The value is
		interdependet with the absolute bandwidth value,
		set with the command [:SOURce<hw>]:BB:ARBitrary:NOTCh<ch>:BWIDth[:ABSolute]. That is, you cna set the notch bandwidth in
		either way. \n
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: no_bw_rel: float Range: 0 to 10"""
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ARBitrary:NOTCh{notchFilter_cmd_val}:BWIDth:RELative?')
		return Conversions.str_to_float(response)
