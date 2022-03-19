from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wlist:
	"""Wlist commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("wlist", core, parent)

	@property
	def file(self):
		"""file commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	# noinspection PyTypeChecker
	def get_dasr(self) -> enums.ExtSeqAdwRate:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:WLISt:DASR \n
		Snippet: value: enums.ExtSeqAdwRate = driver.source.bb.esequencer.asequencing.wlist.get_dasr() \n
		No command help available \n
			:return: sample_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:WLISt:DASR?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqAdwRate)

	def set_dasr(self, sample_rate: enums.ExtSeqAdwRate) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:ASEQuencing:WLISt:DASR \n
		Snippet: driver.source.bb.esequencer.asequencing.wlist.set_dasr(sample_rate = enums.ExtSeqAdwRate.SR2G4) \n
		No command help available \n
			:param sample_rate: No help available
		"""
		param = Conversions.enum_scalar_to_str(sample_rate, enums.ExtSeqAdwRate)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:ASEQuencing:WLISt:DASR {param}')

	def clone(self) -> 'Wlist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wlist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
