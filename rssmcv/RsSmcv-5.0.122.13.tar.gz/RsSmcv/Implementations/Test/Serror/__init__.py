from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Serror:
	"""Serror commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("serror", core, parent)

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import Set
			self._set = Set(self._core, self._cmd_group)
		return self._set

	def set_unset(self, path: int) -> None:
		"""SCPI: TEST:SERRor:UNSet \n
		Snippet: driver.test.serror.set_unset(path = 1) \n
		No command help available \n
			:param path: No help available
		"""
		param = Conversions.decimal_value_to_str(path)
		self._core.io.write(f'TEST:SERRor:UNSet {param}')

	def clone(self) -> 'Serror':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Serror(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
