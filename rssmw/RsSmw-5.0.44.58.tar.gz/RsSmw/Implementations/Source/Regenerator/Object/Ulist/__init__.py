from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ulist:
	"""Ulist commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ulist", core, parent)

	@property
	def select(self):
		"""select commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_select'):
			from .Select import Select
			self._select = Select(self._core, self._cmd_group)
		return self._select

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:REGenerator:OBJect:ULISt:CATalog \n
		Snippet: value: List[str] = driver.source.regenerator.object.ulist.get_catalog() \n
		Queries files with user setting in the default directory. Listed are files with the file extension *.reg_list. Refer to
		'Accessing Files in the Default or Specified Directory' for general information on file handling in the default and in a
		specific directory. \n
			:return: filenames: filename1,filename2,... Returns a string of file names separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:REGenerator:OBJect:ULISt:CATalog?')
		return Conversions.str_to_str_list(response)

	def clone(self) -> 'Ulist':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ulist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
