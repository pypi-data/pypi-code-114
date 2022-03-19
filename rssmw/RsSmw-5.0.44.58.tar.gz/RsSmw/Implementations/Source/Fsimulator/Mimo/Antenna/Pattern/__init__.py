from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AntModPatMode:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:PATTern:MODE \n
		Snippet: value: enums.AntModPatMode = driver.source.fsimulator.mimo.antenna.pattern.get_mode() \n
		Sets way the software extracts or calculates the antenna polarization patterns. \n
			:return: ant_mod_pat_mode: SEParate| SINGle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:PATTern:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AntModPatMode)

	def set_mode(self, ant_mod_pat_mode: enums.AntModPatMode) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:ANTenna:PATTern:MODE \n
		Snippet: driver.source.fsimulator.mimo.antenna.pattern.set_mode(ant_mod_pat_mode = enums.AntModPatMode.SEParate) \n
		Sets way the software extracts or calculates the antenna polarization patterns. \n
			:param ant_mod_pat_mode: SEParate| SINGle
		"""
		param = Conversions.enum_scalar_to_str(ant_mod_pat_mode, enums.AntModPatMode)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:ANTenna:PATTern:MODE {param}')

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
