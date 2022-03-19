from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BbConf:
	"""BbConf commands group definition. 7 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbConf", core, parent)

	@property
	def row(self):
		"""row commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	def get_conflict(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:OUTPut:BBConf:CONFlict \n
		Snippet: value: bool = driver.source.bb.nr5G.output.bbConf.get_conflict() \n
		Queries if there are existing output conflicts caused by mismatch between the nominal sample rate, playback rate and
		sample rate in any of the outputs of the baseband block. \n
			:return: any_outp_conflict: 1| ON| 0| OFF
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:OUTPut:BBConf:CONFlict?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'BbConf':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BbConf(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
