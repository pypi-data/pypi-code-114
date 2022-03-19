from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dcatalog:
	"""Dcatalog commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dcatalog", core, parent)

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def get_value(self) -> str:
		"""SCPI: MMEMory:DCATalog \n
		Snippet: value: str = driver.massMemory.dcatalog.get_value() \n
		Returns the subdirectories of a particular directory. \n
			:return: dcatalog: No help available
		"""
		response = self._core.io.query_str('MMEMory:DCATalog?')
		return trim_str_response(response)

	def clone(self) -> 'Dcatalog':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dcatalog(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
