from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scrambler:
	"""Scrambler commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scrambler", core, parent)

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def get_mode(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:SCRambler:MODE \n
		Snippet: value: bool = driver.source.bb.wlad.pconfig.scrambler.get_mode() \n
		Sets the mode for the scrambler. \n
			:return: mode: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLAD:PCONfig:SCRambler:MODE?')
		return Conversions.str_to_bool(response)

	def set_mode(self, mode: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLAD:PCONfig:SCRambler:MODE \n
		Snippet: driver.source.bb.wlad.pconfig.scrambler.set_mode(mode = False) \n
		Sets the mode for the scrambler. \n
			:param mode: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(mode)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLAD:PCONfig:SCRambler:MODE {param}')

	def clone(self) -> 'Scrambler':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scrambler(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
