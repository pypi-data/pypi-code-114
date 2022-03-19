from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waveform", core, parent)

	@property
	def tag(self):
		"""tag commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tag'):
			from .Tag import Tag
			self._tag = Tag(self._core, self._cmd_group)
		return self._tag

	def get_counter(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:WAVeform:COUNter \n
		Snippet: value: int = driver.source.bb.arbitrary.ethernet.waveform.get_counter() \n
		No command help available \n
			:return: waveform_counter: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:ETHernet:WAVeform:COUNter?')
		return Conversions.str_to_int(response)

	def get_info(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:ETHernet:WAVeform:INFO \n
		Snippet: value: List[str] = driver.source.bb.arbitrary.ethernet.waveform.get_info() \n
		No command help available \n
			:return: arb_eth_wave_info: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:ETHernet:WAVeform:INFO?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Waveform':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Waveform(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
