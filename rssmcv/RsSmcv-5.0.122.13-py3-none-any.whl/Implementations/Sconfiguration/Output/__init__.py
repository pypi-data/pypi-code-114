from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 7 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def mapping(self):
		"""mapping commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import Mapping
			self._mapping = Mapping(self._core, self._cmd_group)
		return self._mapping

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.SystConfOutpMode:
		"""SCPI: SCONfiguration:OUTPut:MODE \n
		Snippet: value: enums.SystConfOutpMode = driver.sconfiguration.output.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SCONfiguration:OUTPut:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SystConfOutpMode)

	def set_mode(self, mode: enums.SystConfOutpMode) -> None:
		"""SCPI: SCONfiguration:OUTPut:MODE \n
		Snippet: driver.sconfiguration.output.set_mode(mode = enums.SystConfOutpMode.ALL) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.SystConfOutpMode)
		self._core.io.write(f'SCONfiguration:OUTPut:MODE {param}')

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
