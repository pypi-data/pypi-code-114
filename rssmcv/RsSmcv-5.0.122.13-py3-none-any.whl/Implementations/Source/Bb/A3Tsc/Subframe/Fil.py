from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fil:
	"""Fil commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fil", core, parent)

	def set(self, freq_interleaver: bool, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:FIL \n
		Snippet: driver.source.bb.a3Tsc.subframe.fil.set(freq_interleaver = False, subframe = repcap.Subframe.Default) \n
		Enables/disables the frequency interleaver. \n
			:param freq_interleaver: OFF| ON| 1| 0 | 0| 1| OFF| ON
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
		"""
		param = Conversions.bool_to_str(freq_interleaver)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:FIL {param}')

	def get(self, subframe=repcap.Subframe.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:A3TSc:SUBFrame<CH>:FIL \n
		Snippet: value: bool = driver.source.bb.a3Tsc.subframe.fil.get(subframe = repcap.Subframe.Default) \n
		Enables/disables the frequency interleaver. \n
			:param subframe: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subframe')
			:return: freq_interleaver: OFF| ON| 1| 0 | 0| 1| OFF| ON"""
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:A3TSc:SUBFrame{subframe_cmd_val}:FIL?')
		return Conversions.str_to_bool(response)
