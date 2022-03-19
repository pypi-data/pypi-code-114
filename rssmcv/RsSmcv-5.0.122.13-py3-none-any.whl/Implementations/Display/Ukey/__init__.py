from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ukey:
	"""Ukey commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ukey", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	def set_name(self, name: str) -> None:
		"""SCPI: DISPlay:UKEY:NAME \n
		Snippet: driver.display.ukey.set_name(name = '1') \n
		No command help available \n
			:param name: No help available
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'DISPlay:UKEY:NAME {param}')

	def set_scpi(self, scpi: str) -> None:
		"""SCPI: DISPlay:UKEY:SCPI \n
		Snippet: driver.display.ukey.set_scpi(scpi = '1') \n
		No command help available \n
			:param scpi: No help available
		"""
		param = Conversions.value_to_quoted_str(scpi)
		self._core.io.write(f'DISPlay:UKEY:SCPI {param}')

	def clone(self) -> 'Ukey':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ukey(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
